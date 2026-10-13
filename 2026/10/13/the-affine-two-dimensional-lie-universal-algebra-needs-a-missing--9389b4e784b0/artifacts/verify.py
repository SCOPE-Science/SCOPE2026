from collections import Counter

def endos(q):
    return [(a,b,d) for a in range(q) for b in range(q) for d in range(q)
            if a*(1-d)%q==0]

def mul(x,y,q):
    a,b,d=x; A,B,D=y
    return (a*A%q,(a*B+b*D)%q,d*D%q)

def rank(x,q):
    a,b,d=x
    if a*d%q: return 2
    if a or b or d: return 1
    return 0

for q in (2,3,5,7,11):
    S=endos(q); N=len(S)
    assert N==2*q*q-q
    assert [sum(rank(x,q)==r for x in S) for r in range(3)]==[1,q*q-1,q*(q-1)]
    idem=[x for x in S if mul(x,x,q)==x]
    assert len(idem)==q+2
    zero=(0,0,0)
    nil=[x for x in S if mul(x,x,q)==zero]
    assert len(nil)==q

    csizes=[]
    center=[]
    for x in S:
        c=sum(mul(x,y,q)==mul(y,x,q) for y in S)
        csizes.append(c)
        if c==N: center.append(x)
    assert set(center)=={(0,0,0),(1%q,0,1%q)}
    dist=Counter(csizes)
    assert dist==Counter({N:2,2*q:2*(q-1),2*q-1:q*(2*q-3)})
    assert sum(csizes)==4*q**3-3*q
    assert N!=q*q
    print({"q":q,"endomorphisms":N,"centralizers":dict(sorted(dist.items()))})
print("VERIFY_OK")
