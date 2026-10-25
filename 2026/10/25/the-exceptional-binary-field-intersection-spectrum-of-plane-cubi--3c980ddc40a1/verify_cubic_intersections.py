"""Complete exact census of coprime pairs of binary ternary cubics.

Run: python verify_cubic_intersections.py
Python 3 standard library only. Ordered coefficients: X^3,X^2Y,X^2Z,XY^2,XYZ,
XZ^2,Y^3,Y^2Z,YZ^2,Z^3. A mask is the corresponding bit vector.
"""
from collections import Counter
from itertools import product

C2=((2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2))
C3=((3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),
    (1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3))
INDEX={v:k for k,v in enumerate(C3)}
POINTS=[(v>>2&1,v>>1&1,v&1) for v in range(1,8)]

def product_form(line,quad):
    mask=0
    for k in range(3):
        if line>>k&1:
            for j,e in enumerate(C2):
                if quad>>j&1:
                    m=tuple(e[t]+(k==t) for t in range(3))
                    mask ^= 1<<INDEX[m]
    return mask

def factor_set():
    factors=[0]*1024
    for line in range(1,8):
        for quad in range(1,64):
            f=product_form(line,quad)
            factors[f] |= (1<<(line-1)) | (1<<(7+quad-1))
    return factors

def point_mask(c):
    out=0
    for k,p in enumerate(POINTS):
        v=0
        for i,(a,b,d) in enumerate(C3):
            if c>>i&1:v ^= p[0]**a * p[1]**b * p[2]**d
        if v==0:out |= 1<<k
    return out

def mul_poly(a,b):
    out={}
    for e in a:
        for d in b:
            t=tuple(e[i]+d[i] for i in range(3))
            out[t]=out.get(t,0)^1
    return {k:1 for k,v in out.items() if v}

def poly_pow(a,n):
    out={(0,0,0):1}
    for _ in range(n):out=mul_poly(out,a)
    return out

def coordinate_map(rows):
    lin=[{tuple(int(i==j) for i in range(3)):1
          for j in range(3) if rows[t]>>j&1} for t in range(3)]
    powers=[[poly_pow(c,n) for n in range(4)] for c in lin]
    result=[]
    for a,b,c in C3:
        poly=mul_poly(mul_poly(powers[0][a],powers[1][b]),powers[2][c])
        result.append(sum(1<<INDEX[e] for e in poly))
    return result

def change_form(c,substitution):
    out=0
    for k in range(10):
        if c>>k&1:out ^= substitution[k]
    return out

def projective_substitutions():
    matrices=[r for r in product(range(1,8),repeat=3)
              if len({0,*r,r[0]^r[1],r[0]^r[2],r[1]^r[2],r[0]^r[1]^r[2]})==8]
    assert len(matrices)==168
    return [coordinate_map(r) for r in matrices]

def main():
    div=factor_set()
    zero=[point_mask(j) for j in range(1024)]
    counts=Counter();shared=Counter();maximal=set()
    for a in range(1,1024):
        for b in range(a+1,1024):
            k=(zero[a]&zero[b]).bit_count()
            if div[a]&div[b]:shared[k]+=1
            else:
                counts[k]+=1
                if k==6:maximal.add((a,b))
    assert counts=={0:69972,1:163191,2:162918,3:85554,4:23604,5:3339,6:210}
    assert shared=={1:21,2:126,3:4746,4:6216,5:2457,6:378,7:21}
    assert len(maximal)==210
    assert sum(counts.values())+sum(shared.values())==1023*1022//2
    maps=projective_substitutions()
    remaining=set(maximal);orbits=[]
    while remaining:
        rep=min(remaining)
        orbit={tuple(sorted(change_form(m,im) for m in rep)) for im in maps}
        assert orbit<=maximal
        remaining-=orbit
        orbits.append((rep,len(orbit)))
    assert orbits==[((10,180),84),((10,660),28),((10,670),28),
                   ((16,446),28),((57,407),42)]
    print('ordered coprime intersection counts:',dict(sorted((k,2*v) for k,v in counts.items())))
    print('ordered shared component distinct forms:',dict(sorted((k,2*v) for k,v in shared.items())))
    print('extremal unordered pairs:',len(maximal))
    print('extremal PGL3 orbits:',orbits)
    print('PASS')
if __name__=='__main__':main()
