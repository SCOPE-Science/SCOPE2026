"""Independent exact-rational balance and comparison checks for three-site, two-particle on/off ZRP. No third-party packages."""
from fractions import Fraction
from itertools import product


def verify(c):
    states=[]
    for occ in product(range(3), repeat=3):
        if sum(occ)!=2: continue
        for phase in product((0,1),repeat=3):
            if all(phase[j] or occ[j] for j in range(3)):
                states.append((occ,phase))
    assert len(states)==18
    Z=3*c*c+7*c+3
    pi={}
    for occ,phase in states:
        used=[i for i,n in enumerate(occ) if n]
        if len(used)==1:
            numerator=2*(c+1) if not phase[used[0]] else c*(c+1)
        else:
            ons=sum(phase[j] for j in used)
            numerator=[1, 2*c, 2*c*c][ons]
        pi[(occ,phase)]=numerator/(3*Z)
    assert sum(pi.values())==1
    balance={q:Fraction(0) for q in states}
    for (occ,phase),p in pi.items():
        for i in range(3):
            if occ[i] and not phase[i]:
                ph=list(phase);ph[i]=1
                dst=(occ,tuple(ph))
                balance[(occ,phase)]-=p*c;balance[dst]+=p*c
            if occ[i] and phase[i]:
                for j in range(3):
                    if i==j:continue
                    n=list(occ);n[i]-=1;n[j]+=1
                    ph=list(phase);ph[j]=0
                    dst=(tuple(n),tuple(ph))
                    rate=Fraction(occ[i],2)
                    assert dst in balance
                    balance[(occ,phase)]-=p*rate;balance[dst]+=p*rate
    assert all(v==0 for v in balance.values())
    pair=sum(p for (n,phase),p in pi.items() if max(n)==2)
    actual=(c+1)*(c+2)/Z
    modified=(c+2)/(3*c+4)
    gap=(c+2)/((3*c+4)*Z)
    assert pair==actual and actual-modified==gap and gap>0
    return len(balance)

if __name__=='__main__':
    cs=[Fraction(i,j) for i in range(1,31) for j in (1,2,3,5,7,11)]
    states=sum(verify(c) for c in cs)
    print('PASS',len(cs),'rational rates;',states,'balance entries; exact strict gap and normalization')
