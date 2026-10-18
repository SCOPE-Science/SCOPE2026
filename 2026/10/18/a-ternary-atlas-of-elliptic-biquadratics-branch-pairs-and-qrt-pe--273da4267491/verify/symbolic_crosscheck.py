"""Independent PGL_2(F_3)^2 orbit generation and four-chart ideal checks.
Requires sympy. Run as python verify/symbolic_crosscheck.py from package root.
Does not import census.py or use its squarefreeness algorithm.
"""
import json
from pathlib import Path
import sympy as S

P = Path(__file__).resolve().parent.parent
REC = json.loads((P/'data'/'orbits.json').read_text())
X,Y,Z,W = S.symbols('U V S T')
projective_points = ((1,0),(0,1),(1,1),(1,2))
B = lambda a,b: (a*a,a*b,b*b)

def decode(n):
    return tuple(n//3**i%3 for i in range(9))

def encode(v):
    for a in v:
        if a:
            t=1 if a==1 else 2
            return sum(((x*t)%3)*3**i for i,x in enumerate(v))
    raise AssertionError('zero form')

def square_action(m):
    a,b,c,d=m
    return ((a*a%3,2*a*b%3,b*b%3),
            (a*c%3,(a*d+b*c)%3,b*d%3),
            (c*c%3,2*c*d%3,d*d%3))

projective_matrices={}
for a in range(3):
 for b in range(3):
  for c in range(3):
   for d in range(3):
    if (a*d-b*c)%3:
     m=(a,b,c,d)
     if next(v for v in m if v)!=1:
      m=tuple(2*v%3 for v in m)
     projective_matrices[m]=square_action(m)
assert len(projective_matrices)==24
matrices=list(projective_matrices.values())

def transform(c,a,b,flip):
    out=[0]*9
    for i in range(3):
     for j in range(3):
      if not c[3*i+j]: continue
      for k in range(3):
       for l in range(3):
        v=c[3*i+j]*a[i][k]*b[j][l]
        dst=3*l+k if flip else 3*k+l
        out[dst]=(out[dst]+v)%3
    return encode(out)

def all_images(rep):
    c=decode(rep)
    return {transform(c,a,b,flip) for a in matrices for b in matrices
                                      for flip in (False,True)}

def smooth_by_ideals(rep):
    c=decode(rep)
    f=sum(c[3*i+j]*X**(2-i)*Y**i*Z**(2-j)*W**j
          for i in range(3) for j in range(3))
    for t,u in ((X,Z),(X,W),(Y,Z),(Y,W)):
        local=S.expand(f.subs({t:1,u:1}))
        variables=tuple(z for z in (X,Y,Z,W) if z not in (t,u))
        ideal=[local]+[S.diff(local,z) for z in variables]
        g=S.groebner(ideal,*variables,modulus=3)
        if list(g)!=[S.Integer(1)]: return False
    return True

def eval_form(c,x,y):
    a=B(*x);b=B(*y)
    return sum(c[3*i+j]*a[i]*b[j]
               for i in range(3) for j in range(3))%3

def ramification(c,point,axis):
    # The fibre binary quadratic and its two fibrewise derivatives both vanish.
    x,y=point
    if axis==0:
        A=sum(c[3*i]*B(*x)[i] for i in range(3))%3
        Q=sum(c[3*i+1]*B(*x)[i] for i in range(3))%3
        C=sum(c[3*i+2]*B(*x)[i] for i in range(3))%3
        s,t=y
    else:
        A=sum(c[j]*B(*y)[j] for j in range(3))%3
        Q=sum(c[3+j]*B(*y)[j] for j in range(3))%3
        C=sum(c[6+j]*B(*y)[j] for j in range(3))%3
        s,t=x
    return (2*A*s+Q*t)%3==0 and (Q*s+2*C*t)%3==0

def point_data(rep):
    c=decode(rep)
    pts={(i,j) for i,u in enumerate(projective_points)
                 for j,v in enumerate(projective_points)
                 if eval_form(c,u,v)==0}
    rc=[sum(ramification(c,(projective_points[i],projective_points[j]),axis)
             for i,j in pts) for axis in (0,1)]
    def deck(q,axis):
        neighbours=[p for p in pts if p[axis]==q[axis]]
        assert len(neighbours) in (1,2)
        return q if len(neighbours)==1 else next(p for p in neighbours if p!=q)
    def move(q): return deck(deck(q,0),1)
    def step(q,n):
        for _ in range(n): q=move(q)
        return q
    order=next(n for n in range(1,9) if all(step(p,n)==p for p in pts))
    return len(pts), sorted(rc), order

def main():
    visited=set()
    for r in REC['orbits']:
        images=all_images(r['representative'])
        assert r['size']==len(images),(r['representative'],'orbit size')
        assert not visited.intersection(images),'orbit overlap'
        visited.update(images)
        assert smooth_by_ideals(r['representative'])==r['smooth'], ('Groebner',r['representative'])
        if r['smooth']:
            N,ram,T=point_data(r['representative'])
            assert (N,ram,T)==(r['points'],r['ramification'],r['qrt_order'])
    assert len(visited)==9841
    # All normalized nonzero forms are present, not just a sampled subset.
    assert all((n in visited)==(next((n//3**i)%3 for i in range(9)
                             if (n//3**i)%3)!=2) for n in range(1,3**9))
    print('PASS: 24 projective matrices; 1152 ambient maps; 41 disjoint exhaustive orbits')
    print('PASS: exact Groebner smoothness in four charts for all 41 representatives')
    print('PASS: independently recomputed rational points, branch counts, deck orders')

if __name__=='__main__':main()
