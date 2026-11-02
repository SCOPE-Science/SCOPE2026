"""Independent linear-program checks and exact tail-threshold evaluation for weighted stars.
Scientific scope: finite positive-arm star metrics and real zero-mass atomic measures.
"""
from fractions import Fraction
import random
import numpy as np
from scipy.optimize import linprog

def tail_segments(radii, masses):
    assert len(radii)==len(masses)
    data=sorted((Fraction(r),Fraction(w)) for r,w in zip(radii,masses) if w>0)
    segments=[]
    right=sum((w for r,w in data),Fraction(0))
    previous=Fraction(0)
    j=0
    while j<len(data):
        radius=data[j][0]
        if radius>previous and right>0:
            segments.append((radius-previous,right))
        while j<len(data) and data[j][0]==radius:
            right-=data[j][1]
            j+=1
        previous=radius
    return segments

def norm_exact(radii,charges):
    p=tail_segments([r for r,c in zip(radii,charges) if c>0],[c for c in charges if c>0])
    n=tail_segments([r for r,c in zip(radii,charges) if c<0],[-c for c in charges if c<0])
    seg=sorted(p+n,key=lambda z:z[1],reverse=True)
    if not seg:return Fraction(0)
    aa=bb=Fraction(0)
    for j,(length,tail) in enumerate(seg):
        aa+=length
        bb+=length*tail
        gamma=bb/(2+aa)
        nxt=seg[j+1][1] if j+1<len(seg) else Fraction(0)
        if nxt<=gamma<=tail:
            return 2*gamma
    raise AssertionError('threshold scan has no root')

def norm_lp(radii,charges):
    n=len(radii); distances=np.zeros((n+1,n+1))
    for i,r in enumerate(radii,1):
        distances[0,i]=distances[i,0]=float(r)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            distances[i,j]=distances[j,i]=float(radii[i-1]+radii[j-1])
    # variables f_0...f_n, M, L. Max sum masses*f with sum of abs bound M and Lip bound L.
    c=np.zeros(n+3);c[:n+1]=[float(sum(charges))]+[-float(t) for t in charges]
    cons=[];bounds=[]
    for i in range(n+1):
        row=np.zeros(n+3);row[i]=1;row[n+1]=-1;cons.append(row);bounds.append(0)
        row=np.zeros(n+3);row[i]=-1;row[n+1]=-1;cons.append(row);bounds.append(0)
    for i in range(n+1):
        for j in range(i+1,n+1):
            row=np.zeros(n+3);row[i]=1;row[j]=-1;row[n+2]=-distances[i,j];cons.append(row);bounds.append(0)
            row=-row;row[n+2]=-distances[i,j];cons.append(row);bounds.append(0)
    row=np.zeros(n+3);row[-2]=row[-1]=1;cons.append(row);bounds.append(1)
    sol=linprog(c,A_ub=np.array(cons),b_ub=np.array(bounds),bounds=[(None,None)]*(n+1)+[(0,None)]*2,method='highs')
    assert sol.success,sol.message
    return -sol.fun

def check():
    rng=random.Random(108237)
    cases=0
    for n in range(1,8):
        for j in range(130):
            # repeated and heterogeneous radii, different signs, zero leaf values, positive/negative hub masses
            radii=[Fraction(rng.randrange(1,18),rng.randrange(1,8)) for k in range(n)]
            charges=[Fraction(rng.randrange(-12,13),rng.randrange(1,9)) for k in range(n)]
            exact=norm_exact(radii,charges)
            lp=norm_lp(radii,charges)
            if abs(float(exact)-lp)>1e-8:
                raise AssertionError((radii,charges,exact,lp))
            cases+=1
    for n in range(2,8):
        radii=[Fraction(1)]*n
        charges=[Fraction(1) if j%2==0 else Fraction(-1) for j in range(n)]
        assert abs(float(norm_exact(radii,charges))-norm_lp(radii,charges))<1e-9
        cases+=1
    print('OK: %d independent LP comparisons'%cases)
    # explicit unequal-arm exact example:
    radii=[Fraction(1),Fraction(2),Fraction(4),Fraction(7)]
    charges=[Fraction(2),Fraction(-3),Fraction(1),Fraction(-1)]
    answer=norm_exact(radii,charges)
    print('example radii:',list(map(str,radii)),'charges:',list(map(str,charges)),'norm:',answer, 'decimal',float(answer))
if __name__=='__main__':check()

def construct_optimal_function(radii,charges):
    """Return a rational BL-unit-ball witness, with hub as index zero."""
    radii=[Fraction(v) for v in radii]
    charges=[Fraction(v) for v in charges]
    positive=tail_segments([r for r,c in zip(radii,charges) if c>0],
                           [c for c in charges if c>0])
    negative=tail_segments([r for r,c in zip(radii,charges) if c<0],
                           [-c for c in charges if c<0])
    gamma=norm_exact(radii,charges)/2
    a=sum((width for width,height in negative if height>gamma),Fraction(0))
    b=sum((width for width,height in positive if height>gamma),Fraction(0))
    u=[Fraction(0)]+[min(r,b) if c>0 else -min(r,a) if c<0 else Fraction(0)
                         for r,c in zip(radii,charges)]
    mid=(max(u)+min(u))/2
    scale=Fraction(2)/(2+a+b)
    f=[scale*(z-mid) for z in u]
    assert max(map(abs,f)) + max(
        [abs(f[i]-f[j])/(radii[i-1]+radii[j-1])
         for i in range(1,len(f)) for j in range(i+1,len(f))] +
        [abs(f[0]-f[i])/radii[i-1] for i in range(1,len(f))] + [Fraction(0)]
    )<=1
    val=sum(c*(f[i+1]-f[0]) for i,c in enumerate(charges))
    assert val==2*gamma,(radii,charges,gamma,val)
    return f

def check_witnesses():
    rng=random.Random(7129)
    for n in range(1,11):
        for k in range(137):
            radii=[Fraction(rng.randrange(1,15),rng.randrange(1,6)) for _ in range(n)]
            charges=[Fraction(rng.randrange(-7,8),rng.randrange(1,5)) for _ in range(n)]
            construct_optimal_function(radii,charges)
    print('OK: 1370 exact rational optimizing witnesses')

if __name__=='__main__':
    check_witnesses()
