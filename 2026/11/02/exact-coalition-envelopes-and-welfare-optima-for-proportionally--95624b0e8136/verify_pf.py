"""Exact rational checks for the 1D strong proportional-fairness envelope theorem.

This checks finite examples only; the universal proof is in RESULT.md.
No dependencies outside Python's standard library.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement


def fast_envelope(xs, alpha):
    n=len(xs)
    h=Q(1,1)/(alpha*n)
    z=[xs[i]-(i+1)*h for i in range(n)]
    p=[];p_arg=[]
    v=z[0]; arg=0
    for j in range(n):
        if z[j]>v: v=z[j];arg=j
        p.append(v);p_arg.append(arg)
    s=[None]*n;s_arg=[None]*n
    v=z[-1];arg=n-1
    for j in range(n-1,-1,-1):
        if z[j]<v: v=z[j];arg=j
        s[j]=v;s_arg[j]=arg
    rad=[h+p[j]-s[j] for j in range(n)]
    return rad,[xs[j]-rad[j] for j in range(n)],[xs[j]+rad[j] for j in range(n)],[(p_arg[j],s_arg[j]) for j in range(n)]


def brute_radii(xs,alpha):
    n=len(xs)
    h=Q(1,1)/(alpha*n)
    out=[]
    for i in range(n):
        values=[]
        for mask in range(1,1<<n):
            if not(mask>>i&1):continue
            S=[j for j in range(n) if mask>>j&1]
            values.append(len(S)*h-(xs[max(S)]-xs[min(S)]))
        out.append(max(values))
    return out


def brute_opt(xs, alpha):
    rr=brute_radii(xs,alpha)
    candidates={Q(0),Q(1)}
    for xi, ri in zip(xs,rr):
        if 0<=xi-ri<=1:candidates.add(xi-ri)
        if 0<=xi+ri<=1:candidates.add(xi+ri)
    candidates=[y for y in candidates if all(abs(y-x)>=r for x,r in zip(xs,rr))]
    if not candidates:return None
    def w(y):return sum(abs(y-x) for x in xs)
    return max(w(y) for y in candidates)


def fast_opt(xs, alpha):
    rr,L,R,witnesses=fast_envelope(xs,alpha)
    # Merge two already sorted lists; this procedure uses a sorted sweep
    # through the candidate coordinates and open exclusion intervals.
    coords=sorted(set([Q(0),Q(1)]+[u for u in L+R if 0<=u<=1]))
    prefix=[Q(0)]
    for x in xs: prefix.append(prefix[-1]+x)
    left=0;xi=0;best=None
    for y in coords:
        while left<len(xs) and L[left]<y:left+=1
        if left and y<R[left-1]:continue
        while xi<len(xs) and xs[xi]<=y:xi+=1
        w=(2*xi-len(xs))*y+prefix[-1]-2*prefix[xi]
        if best is None or w>best:best=w
    return best


def gap_intervals(xs, alpha):
    rr,L,R,_=fast_envelope(xs,alpha)
    lower=[Q(0)]+R
    upper=L+[Q(1)]
    return [(lower[k],upper[k],k) for k in range(len(xs)+1) if lower[k]<=upper[k]]


def gap_opt(xs,alpha):
    n=len(xs)
    S=[Q(0)]
    for x in xs:S.append(S[-1]+x)
    vals=[]
    for lo,hi,k in gap_intervals(xs,alpha):
        y=lo if 2*k<n else hi
        vals.append((2*k-n)*y+S[-1]-2*S[k])
    return max(vals) if vals else None


def test_case(xs,alpha):
    rr,L,R,wit=fast_envelope(xs,alpha)
    assert rr==brute_radii(xs,alpha),(xs,alpha,rr,brute_radii(xs,alpha))
    assert L==sorted(L) and R==sorted(R),(xs,alpha)
    h=Q(1,1)/(alpha*len(xs))
    for i,(a,b) in enumerate(wit):
        assert a<=i<=b
        assert rr[i]==(b-a+1)*h-(xs[b]-xs[a])
    assert fast_opt(xs,alpha)==brute_opt(xs,alpha),(xs,alpha)
    assert gap_opt(xs,alpha)==brute_opt(xs,alpha),(xs,alpha)
    # Exact membership is constant between all exclusion endpoints and centers.
    probes={Q(0),Q(1)}
    probes.update(y for y in L+R+list(xs) if 0<=y<=1)
    grid=sorted(probes)
    probes.update((a+b)/2 for a,b in zip(grid,grid[1:]))
    for y in probes:
        direct=all(abs(y-xs[j])>=rr[j] for j in range(len(xs)))
        swept=any(lo<=y<=hi for lo,hi,k in gap_intervals(xs,alpha))
        assert direct==swept,(xs,alpha,y,direct,swept)


def run():
    tests=0
    for n in range(1,7):
        for indices in combinations_with_replacement(range(5),n):
            xs=tuple(Q(i,4) for i in indices)
            for alpha in [Q(1),Q(3,2),Q(2),Q(5,2),Q(3)]:
                test_case(xs,alpha)
                tests+=1
    for n in (7,8):
        for indices in combinations_with_replacement(range(3),n):
            xs=tuple(Q(i,2) for i in indices)
            for alpha in [Q(1),Q(2),Q(4)]:
                test_case(xs,alpha)
                tests+=1
    # A tight topological example: n+1 singleton feasible components.
    for n in range(1,13):
        xs=[Q(2*i-1,2*n) for i in range(1,n+1)]
        rr,L,R,_=fast_envelope(xs,Q(2))
        assert all(t==Q(1,2*n) for t in rr)
        assert L==[Q(i,n) for i in range(n)]
        assert R==[Q(i,n) for i in range(1,n+1)]
    # Strict gap between optimal UFS and optimal coalition-wise 2-PF.
    xs=[Q(0),Q(17,24),Q(3,4)]
    rad,_,_,_=fast_envelope(xs,Q(2))
    assert rad==[Q(1,6),Q(7,24),Q(7,24)]
    assert fast_opt(xs,Q(2))==Q(31,24)
    assert all(abs(Q(1)-x)>=Q(1,6) for x in xs)  # distinct-location 2-UFS
    assert sum(abs(Q(1)-x) for x in xs)==Q(37,24)
    assert abs(Q(1)-xs[-1])<rad[-1]  # 2-PF fails at 1
    print('PASS: exact finite envelopes, witnesses and welfare optima:',tests,'instances')
    print('PASS: 12 sharp-component examples; strict UFS/PF welfare example')

if __name__=='__main__':run()
