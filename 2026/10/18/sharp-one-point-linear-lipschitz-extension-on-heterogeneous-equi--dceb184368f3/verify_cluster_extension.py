"""Independent finite-dimensional test of clustered metric scalar Lipschitz extension."""
from fractions import Fraction as F
from itertools import product
import random
from scipy.optimize import linprog

R=random.Random(20261014)
checks=0

def formula(ms,aa,cc,rr):
    n=len(ms)
    dd=[cc-aa[j]*(1-F(1,ms[j])) for j in range(n)]
    assert all(z>0 for z in dd)
    # Exact sorted water-filling; no floating calculation.
    order=sorted(range(n),key=lambda j:rr[j]);
    for h in range(1,n+1):
        act=order[:h]
        L=(cc*sum((1/dd[j] for j in act),F(0))-1)/sum((rr[j]/dd[j] for j in act),F(0))
        if L>0 and all(cc-L*rr[j]>=0 for j in act) and all(cc-L*rr[j]<=0 for j in order[h:]):
            al=[max(F(0),(cc-L*rr[j])/dd[j]) for j in range(n)]
            assert sum(al)==1
            return L,al
    raise ValueError('no root')

def exact_T(ms,aa,cc,alpha,i):
    return (cc*sum((abs(alpha[j]) for j in range(len(ms)) if j!=i),F(0))
      + aa[i]*(abs(alpha[i]/ms[i]-1)+(ms[i]-1)*abs(alpha[i])/ms[i])
      + (cc-aa[i])*abs(alpha[i]-1))/2

def independent_lp(ms,aa,cc,rr):
    # Unrestricted signed, non-uniform mass over each individual leaf. Direct
    # transportation/tree-edge formula for differences of a free probability
    # coefficient vector and a unit mass at a leaf.
    k=len(ms);n=sum(ms); leaf_to_cluster=[]
    for j,m in enumerate(ms): leaf_to_cluster.extend([j]*m)
    start=[];t=0
    for m in ms: start.append(t);t+=m
    # Variables: n weights, for every leaf target n absolute values of
    # k cluster mass flows and n pendant-leaf flows; plus L.
    p=n+n*(k+n)+1; Lidx=p-1
    cobj=[0.0]*p;cobj[Lidx]=1.0
    A=[];b=[]
    for x in range(n):
      # subtree flow of the source measure mu - delta_x at each tree edge
      terms=[]
      for j in range(k):
        index=n+x*(k+n)+j; sign=[0.0]*n
        for v in range(start[j],start[j]+ms[j]):sign[v]=1.0
        constant=-(1.0 if leaf_to_cluster[x]==j else 0.0)
        for zsgn in (1.,-1.):
          row=[0.]*p
          for v in range(n):row[v]=zsgn*sign[v]
          row[index]=-1.;A.append(row);b.append(-zsgn*constant)
        terms.append(((float(cc-aa[j])/2),index))
      for v in range(n):
        j=leaf_to_cluster[v];index=n+x*(k+n)+k+v
        constant=-(1.0 if x==v else 0.0)
        for zsgn in (1.,-1.):
          row=[0.]*p;row[v]=zsgn;row[index]=-1.;A.append(row);b.append(-zsgn*constant)
        terms.append(((float(aa[j])/2),index))
      row=[0.]*p
      for factor,index in terms:row[index]+=factor
      row[Lidx]=-float(rr[leaf_to_cluster[x]])
      A.append(row);b.append(0.0)
    eq=[[0.0]*p];eq[0][:n]=[1.]*n
    bd=[(None,None)]*n+[(0,None)]*(p-n)
    res=linprog(cobj,A_ub=A,b_ub=b,A_eq=eq,b_eq=[1.0],bounds=bd,method='highs',options={'time_limit':5.0})
    assert res.success,(res.status,res.message,ms,aa,cc,rr)
    return res.fun

for k in range(2,6):
 for rep in range(120):
    ms=[R.randint(1,4) for _ in range(k)]
    cc=F(R.randint(3,10),3)
    # Choose radii near c/2.. 2c ensures triangle and desired variations.
    rr=[cc*F(R.randint(5,12),10) for _ in range(k)]
    aa=[F(R.randint(1,7),10)*min(cc,2*rr[j]) if ms[j]>1 else F(0) for j in range(k)]
    # Ensure |r_i-r_j|<=c, yes since ratio .5..1.2.
    assert all(abs(rr[i]-rr[j])<=cc<=rr[i]+rr[j] for i in range(k) for j in range(k) if i<j)
    lam,al=formula(ms,aa,cc,rr)
    assert max((exact_T(ms,aa,cc,al,i)/rr[i] for i in range(k)))==lam
    checks+=1
    # Exact random signed coefficient candidates: none can beat sharp formula.
    for _ in range(12):
        vv=[F(R.randint(-20,20),10) for j in range(k-1)]
        vv.append(1-sum(vv))
        ratio=max(exact_T(ms,aa,cc,vv,i)/rr[i] for i in range(k))
        assert ratio>=lam
        checks+=1
    if rep<10 and sum(ms)<=10:
        lp=independent_lp(ms,aa,cc,rr)
        assert abs(lp-float(lam))<1e-7,(k,rep,ms,lam,lp)
        checks+=1
print('PASSED', checks, 'exact rational and independent unrestricted optimization assertions')
print('sample',formula([10,10,10],[F(19,10)]*3,F(2),[F(1),F(11,10),F(19,10)]))
