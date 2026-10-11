#!/usr/bin/env python3
from fractions import Fraction

weights=[
    (Fraction(2,3),Fraction(1,3)),
    (Fraction(3,5),Fraction(2,5)),
    (Fraction(4,7),Fraction(3,7)),
    (Fraction(5,8),Fraction(3,8)),
]

def top_two(scores):
    order=sorted(range(len(scores)), key=lambda z:scores[z], reverse=True)
    return order[0],order[1]

checks=0
witnesses=0
for d in range(2,9):
    for e in range(2,9):
        for alpha,beta in weights:
            assert alpha>beta>0 and alpha+beta==1
            center=[Fraction(1,d)]*d+[Fraction(1,e)]*e
            verts=[]

            # Same-row vertices and explicit additive-score witnesses.
            for i in range(d):
                for j in range(e):
                    for jp in range(e):
                        if j==jp:
                            continue
                        v=[Fraction(0)]*(d+e)
                        v[i]=1
                        v[d+j]=alpha
                        v[d+jp]=beta
                        verts.append(tuple(v))

                        p=[Fraction(-1000-r) for r in range(d)]
                        q=[Fraction(-20-s) for s in range(e)]
                        p[i]=0
                        q[j]=0
                        q[jp]=-1
                        grid=[p[r]+q[s] for r in range(d) for s in range(e)]
                        a,b=top_two(grid)
                        assert divmod(a,e)==(i,j)
                        assert divmod(b,e)==(i,jp)
                        witnesses+=1

            # Same-column vertices and explicit additive-score witnesses.
            for j in range(e):
                for i in range(d):
                    for ip in range(d):
                        if i==ip:
                            continue
                        v=[Fraction(0)]*(d+e)
                        v[i]=alpha
                        v[ip]=beta
                        v[d+j]=1
                        verts.append(tuple(v))

                        p=[Fraction(-20-r) for r in range(d)]
                        q=[Fraction(-1000-s) for s in range(e)]
                        p[i]=0
                        p[ip]=-1
                        q[j]=0
                        grid=[p[r]+q[s] for r in range(d) for s in range(e)]
                        a,b=top_two(grid)
                        assert divmod(a,e)==(i,j)
                        assert divmod(b,e)==(ip,j)
                        witnesses+=1

            assert len(verts)==d*e*(d+e-2)
            assert len(set(verts))==len(verts)

            R2=1+alpha*alpha+beta*beta-Fraction(1,d)-Fraction(1,e)
            for v in verts:
                d2=sum((v[t]-center[t])**2 for t in range(d+e))
                assert d2==R2

            # Cyclic same-row contact certificate.
            acc=[Fraction(0)]*(d+e)
            for i in range(d):
                for j in range(e):
                    jp=(j+1)%e
                    v=[Fraction(0)]*(d+e)
                    v[i]=1
                    v[d+j]=alpha
                    v[d+jp]=beta
                    for t,x in enumerate(v):
                        acc[t]+=x
            avg=[x/Fraction(d*e) for x in acc]
            assert avg==center
            checks+=1

print(f"VERIFY_OK two-lineup-product-simplices parameter_weight_cases={checks} lineup_witnesses={witnesses} exact=yes")
