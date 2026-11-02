"""Direct finite-field verification of radical-square-zero quiver-algebra tuple orbits.
Requires only Python 3 standard library. Run: python3 verify_radical_square_zero.py.
"""
from itertools import product

def components(n, edges):
    par=list(range(n))
    def root(a):
        while a!=par[a]:a=par[a]
        return a
    for a,b in edges:par[root(a)]=root(b)
    return len({root(a) for a in range(n)})

def expected(q,m,n,edges):
    Q=q**m; S=0
    for bits in product((0,1),repeat=len(edges)):
        F=[e for e,bit in zip(edges,bits) if bit]
        S+=(Q*(q-1))**components(n,F)*(Q-1)**len(F)
    assert S%(q-1)**n==0
    return S//(q-1)**n

def run(q,m,n,edges):
    vectors=list(product(range(q),repeat=m))
    zero=(0,)*m
    all_states=set()
    for colors in product(vectors,repeat=n):
        allowed=[]
        for a,b in edges:
            d=tuple((colors[a][j]-colors[b][j])%q for j in range(m))
            if d==zero:allowed.append(vectors)
            else:allowed.append([tuple(t*x%q for x in d) for t in range(q)])
        for val in product(*allowed):all_states.add((colors,val))
    # The unit group has a diagonal torus and an independent radical coordinate on each edge.
    units=list(product(range(1,q),repeat=n))
    radicals=list(product(range(q),repeat=len(edges)))
    inv={t:pow(t,-1,q) for t in range(1,q)}
    orbits=0
    while all_states:
        colors,val=all_states.pop()
        orbit=[]
        for t in units:
            scalars=[(t[a]*inv[t[b]])%q for a,b in edges]
            for s in radicals:
                new=[]
                for e,(a,b) in enumerate(edges):
                    factor=scalars[e]
                    shift=s[e]*inv[t[b]]
                    new.append(tuple((factor*val[e][j]+shift*(colors[b][j]-colors[a][j]))%q for j in range(m)))
                orbit.append((colors,tuple(new)))
        all_states.difference_update(orbit)
        orbits+=1
    want=expected(q,m,n,edges)
    assert orbits==want,(q,m,n,edges,orbits,want)
    print('q',q,'m',m,'n',n,'edges',edges,'orbits',orbits)
    return orbits

if __name__=='__main__':
    cases=[
      (2,1,2,((0,1),)),
      (3,2,2,((0,1),)),
      (2,2,3,((0,1),(0,2))),
      (3,2,3,((0,1),(0,2))),
      (2,1,4,((0,2),(0,3),(1,2),(1,3))),
      (3,1,4,((0,2),(0,3),(1,2),(1,3))),
      (2,2,4,((0,2),(0,3),(1,2),(1,3))),
      (3,2,1,((0,0),)),
      (2,2,2,((0,1),(0,1))),
      (2,2,3,((0,1),(1,2),(2,0))),
    ]
    for case in cases:run(*case)
    print('RADICAL_SQUARE_ZERO_TUPLE_ORBITS_OK',len(cases))
