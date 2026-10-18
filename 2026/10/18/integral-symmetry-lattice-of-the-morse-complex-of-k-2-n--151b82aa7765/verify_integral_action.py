from itertools import permutations,product
from collections import Counter

def inversion_sign(seq):
    return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def pair_chain(n,i,j):
    # 0-index flags x=4i,y=4i+2,p=4i+1,q=4i+3
    factors=[]
    if i==j:
        for k in range(n):
            if k!=i:factors.append((4*k+1,4*k+3))
    else:
        factors.append((4*i+3,4*j+1))
        for k in range(n):
            if k!=i and k!=j:factors.append((4*k+1,4*k+3))
    out={}
    for bits in product((0,1),repeat=n-1):
        ordered=[4*i,4*j+2]+[factors[k][bits[k]] for k in range(n-1)]
        key=tuple(sorted(ordered));out[key]=(-1)**sum(bits)*inversion_sign(ordered)
    return out

def induced(n,pi,sw,s):
    a=[]
    for k in s:
        i,t=divmod(k,4)
        tt=(2,3,0,1)[t] if sw else t
        a.append(4*pi[i]+tt)
    return tuple(sorted(a)),inversion_sign(a)

def action_ratio(n,pi,sw,i,j,cache):
    si,sj=(pi[j],pi[i]) if sw else (pi[i],pi[j]);v=cache[(si,sj)]
    ratios=set()
    for s,c in cache[(i,j)].items():
        t,sign=induced(n,pi,sw,s)
        ratios.add(c*sign*v[t])
    assert len(ratios)==1,(n,pi,sw,i,j,ratios)
    return next(iter(ratios))

for n in range(2,6):
    cache={(i,j):pair_chain(n,i,j) for i in range(n) for j in range(n)}
    good=True
    # choose normalization according to positive action on ordered pairs for leaf perms
    # b_i,j signs so ratio leaf action = sign(pi) b_{pi i,pi j}/b_{ij}
    # choose b_i,j by canonical mapping from seed orbit (0,0) and (0,1)
    b={}
    for i in range(n):
        pi=next(p for p in permutations(range(n)) if p[0]==i)
        b[(i,i)]=action_ratio(n,pi,0,0,0,cache)*inversion_sign(pi)
    for i in range(n):
        for j in range(n):
            if i==j:continue
            pi=next(p for p in permutations(range(n)) if p[0]==i and p[1]==j)
            b[(i,j)]=action_ratio(n,pi,0,0,1,cache)*inversion_sign(pi)
    # A signed diagonal change of integral basis conjugates the raw action.
    for pi in permutations(range(n)):
        for sw in (0,1):
            sig=inversion_sign(pi)
            for i in range(n):
                for j in range(n):
                    ti,tj=(pi[j],pi[i]) if sw else (pi[i],pi[j])
                    c=b[(i,j)]*action_ratio(n,pi,sw,i,j,cache)*b[(ti,tj)]
                    expected=sig*((-1)**(n*sw) if i==j else (-1)**((n+1)*sw))
                    if c!=expected:
                        good=False;print('FAIL',n,pi,sw,i,j,c,expected);break
                if not good:break
            if not good:break
        if not good:break
    assert good
    print('VERIFY_OK',n,'oriented-simplex-terms',sum(len(v) for v in cache.values()))
