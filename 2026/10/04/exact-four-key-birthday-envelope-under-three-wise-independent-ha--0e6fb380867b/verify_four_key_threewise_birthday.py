from fractions import Fraction
from itertools import product, combinations

def ptype(vals):
    c={}
    for x in vals:c[x]=c.get(x,0)+1
    return ''.join(map(str,sorted(c.values(),reverse=True)))

def upper(q):
    return {'1111':Fraction((q-1)*(q-2),q*q),'211':Fraction(0),'22':Fraction(3*(q-2),q*q),'31':Fraction(4,q*q),'4':Fraction(0)}

def lower(q):
    if q==4:return {'1111':Fraction(0),'211':Fraction(3,4),'22':Fraction(0),'31':Fraction(1,4),'4':Fraction(0)}
    return {'1111':Fraction((q-1)*(q-5),q*q),'211':Fraction(6*(q-1),q*q),'22':Fraction(0),'31':Fraction(0),'4':Fraction(1,q*q)}

def moments(q,P):
    assert sum(P.values(),Fraction(0))==1 and all(x>=0 for x in P.values())
    assert P['211']+2*P['22']+3*P['31']+6*P['4']==Fraction(6,q)
    assert P['31']+4*P['4']==Fraction(4,q*q)

def law(q,P):
    buckets={k:[] for k in ['1111','211','22','31','4']}
    for y in product(range(q),repeat=4):buckets[ptype(y)].append(y)
    d={}
    for t,m in P.items():
        if m:
            w=m/len(buckets[t])
            for y in buckets[t]:d[y]=w
    assert sum(d.values(),Fraction(0))==1
    return d

def triple(q,d):
    for inds in combinations(range(4),3):
        tab={}
        for y,p in d.items():
            k=tuple(y[i] for i in inds); tab[k]=tab.get(k,Fraction(0))+p
        assert len(tab)==q**3 and all(p==Fraction(1,q**3) for p in tab.values())

def run():
    symbolic=0
    for q in range(4,5001):
        U,L=upper(q),lower(q); moments(q,U); moments(q,L)
        assert U['1111']==Fraction((q-1)*(q-2),q*q)
        assert L['1111']==max(Fraction(0),Fraction((q-1)*(q-5),q*q))
        symbolic+=1
    exact=0; tables=0
    for q in range(4,11):
        for P in (lower(q),upper(q)):
            d=law(q,P); triple(q,d)
            assert sum(p for y,p in d.items() if len(set(y))==4)==P['1111']
            exact+=1; tables+=4*q**3
    mix=0
    for q in range(4,101):
        L,U=lower(q),upper(q)
        for t in [Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(6,7),Fraction(1)]:
            P={k:(1-t)*L[k]+t*U[k] for k in L}; moments(q,P); mix+=1
    print(f'VERIFY_OK symbolic_checks={symbolic} exact_assignment_checks={exact} triple_tables_checked={tables} mixture_checks={mix}')
if __name__=='__main__':run()
