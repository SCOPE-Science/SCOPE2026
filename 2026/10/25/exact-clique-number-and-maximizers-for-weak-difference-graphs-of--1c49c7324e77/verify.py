from itertools import combinations
from math import comb
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
import numpy as np

def closed(t,a):
    return t+sum(comb(t,j)*a**j for j in range((t+1)//2,t-1)) if t%2 else t+comb(t,t//2)//2*a**(t//2)+sum(comb(t,j)*a**j for j in range(t//2+1,t-1))

def exact_mip(t,a):
    sets=[s for s in range(1,2**t-1)]
    w=np.array([a**s.bit_count() if s.bit_count()<=t-2 else 1 for s in sets],dtype=float)
    bad=[(i,j) for i, s in enumerate(sets) for j, u in enumerate(sets) if i<j and s & u == 0]
    cons=lil_matrix((len(bad),len(sets)),dtype=float)
    for row,(i,j) in enumerate(bad):cons[row,i]=1;cons[row,j]=1
    res=milp(-w,integrality=np.ones(len(sets)),bounds=Bounds(np.zeros(len(sets)),np.ones(len(sets))),constraints=LinearConstraint(cons.tocsr(),-np.inf,1),options={'time_limit':50,'mip_rel_gap':0.0})
    opt=round(-res.fun) if res.fun is not None else None
    return opt,res.message,len(sets),len(bad)
for t,a in [(5,1),(5,2),(5,3),(5,4),(6,1),(6,2),(6,3),(7,1)]:
    expect=closed(t,a)
    actual,status,n,m=exact_mip(t,a)
    print({'t':t,'q':a+1,'expected':expect,'actual':actual,'support_classes':n,'constraints':m,'solver':status},flush=True)
    assert actual==expect and 'optimal' in status.lower()
print('VERIFY_OK')

# Check the middle-pair extremizers (on the quotient graph, independently
# of field-element choices) and enumerate their number in even dimension.
def middle_family_census(t):
    assert t%2==0
    middle=[s for s in range(1,2**t-1) if s.bit_count()==t//2]
    full=(1<<t)-1
    pairs=[(s,full^s) for s in middle if s < (full^s)]
    assert len(pairs)==comb(t,t//2)//2
    choices=0
    above=[s for s in range(1,full) if t//2<s.bit_count()<=t-2]
    coatom=[s for s in range(1,full) if s.bit_count()==t-1]
    for bits in range(1<<len(pairs)):
        family=above+coatom+[pr[(bits>>i)&1] for i,pr in enumerate(pairs)]
        assert all(u&v for ix,u in enumerate(family) for v in family[ix+1:])
        choices+=1
    return choices
assert middle_family_census(6)==2**(comb(6,3)//2)
print('MAXIMIZER_SUPPORT_CENSUS_OK')
