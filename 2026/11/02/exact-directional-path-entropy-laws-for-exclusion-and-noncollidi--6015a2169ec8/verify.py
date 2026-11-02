"""Deterministic finite-state checks for ring exclusion and the sine Doob chain.

Runs with Python standard library only. Analytic proofs appear in RESULT.md.
"""
from itertools import combinations
from math import pi, sin, cos, log, comb, isclose

assertions=0

def check(value, target=0.0, tol=3e-9):
    global assertions
    assert abs(value-target) <= tol * max(1.0,abs(target)), (value,target)
    assertions+=1

def h(config,n):
    value=1.0
    for i,a in enumerate(config):
        for b in config[i+1:]:
            value*=2*sin(pi*(b-a)/n)
    return value

def neighbors(S,n):
    q=set(S)
    for x in S:
        y=(x+1)%n
        if y not in q:
            yield tuple(sorted(q-{x}|{y}))

for n in range(3,11):
    for k in range(1,n):
        states=list(combinations(range(n),k))
        H={s:h(s,n) for s in states}
        pi_nc={s:H[s]**2/(n**k) for s in states}
        pi_ex={s:1/comb(n,k) for s in states}
        R=sin(pi*k/n)/sin(pi/n)
        lamb=k-R
        alpha=(k-R)*(1-(k+R)/n)
        beta=R-k*(n-k)/(n-1)
        check(sum(pi_nc.values()),1)
        check(sum(pi_ex.values()),1)
        flux_nc={s:0.0 for s in states}
        flux_ex={s:0.0 for s in states}
        mean_nc=mean_ex=forward=reverse=0.0
        for s in states:
            moves=list(neighbors(s,n))
            traffic=k-len(moves)
            mean_nc+=pi_nc[s]*traffic
            mean_ex+=pi_ex[s]*traffic
            check(sum(H[t]/H[s] for t in moves),R)
            for t in moves:
                q=H[t]/H[s]
                flux_nc[t]+=pi_nc[s]*q
                flux_ex[t]+=pi_ex[s]
                forward+=pi_nc[s]*(q*log(q)-q+1)
                reverse+=pi_ex[s]*(-log(q)-1+q)
            check(sum(H[t] for t in moves),(k-lamb)*H[s])
        for s in states:
            check(flux_nc[s],R*pi_nc[s])
            check(flux_ex[s],(k-(k-len(list(neighbors(s,n)))))*pi_ex[s])
        check(mean_nc,(k*k-R*R)/n)
        check(mean_ex,k*(k-1)/(n-1))
        check(forward,alpha)
        check(reverse,beta)
        check(forward,lamb-mean_nc)
        check(reverse,mean_ex-lamb)
        check(alpha >= -1e-10,1)
        check(beta >= -1e-10,1)
        # Finite-time path-relative-entropy intercepts from stationary laws.
        init_f=sum(pi_nc[s]*log(pi_nc[s]/pi_ex[s]) for s in states)
        init_r=sum(pi_ex[s]*log(pi_ex[s]/pi_nc[s]) for s in states)
        for time in (0.125,1.0,2.5):
            # The h endpoint telescope has zero stationary expectation.
            check(init_f + time*forward, init_f+time*alpha)
            check(init_r + time*reverse, init_r+time*beta)

for k in (2,3,4,7):
    n=2000
    R=sin(pi*k/n)/sin(pi/n)
    a=(k-R)*(1-(k+R)/n)
    b=R-k*(n-k)/(n-1)
    a0=pi*pi*k*(k*k-1)/(6*n*n)
    b0=k*(k-1)/n
    check(a/a0,1,0.012)
    check(b/b0,1,0.012)

for rho in (.2,.3,.5,.8):
    n=3000
    k=round(n*rho)
    R=sin(pi*k/n)/sin(pi/n)
    alpha=(k-R)*(1-(k+R)/n)
    beta=R-k*(n-k)/(n-1)
    x=sin(pi*rho)/pi
    check(alpha/n,(rho-x)*(1-rho-x),0.0005)
    check(beta/n,x-rho*(1-rho),0.0005)

print(f"PASS {assertions} deterministic assertions; enumerated all unlabeled configurations for 3<=n<=10, 1<=k<n")

# A separate distance-counting formula for the stationary initial divergences
# of the two-particle process (no full-state enumeration here).
for n in (4,5,10,20,100,500,1500):
    c=comb(n,2)
    d_ex=log(n*n/c)-2*log(n)/(n-1)
    d_ex_sum=0.0
    d_nc_sum=0.0
    for d in range(1,n):
        chord=2*sin(pi*d/n)
        number=n-d
        p_nc=number*chord*chord/(n*n)
        p_ex=number/c
        d_ex_sum+=p_ex*log((1/c)/(chord*chord/(n*n)))
        d_nc_sum+=p_nc*log((chord*chord/(n*n))/(1/c))
    check(d_ex,d_ex_sum)
    if n>=500:
        check(d_ex,log(2),0.035)
        check(d_nc_sum,1-log(2),0.02)
    R=2*cos(pi/n)
    alpha=(2-R)*(1-(2+R)/n)
    beta=R-2*(n-2)/(n-1)
    for t in (0.25,1.0,2.0):
        if n>=500:
            check(d_nc_sum+t*n*n*alpha, 1-log(2)+pi*pi*t,0.03)
            check((d_ex+t*n*n*beta)/n,2*t,0.025)
print(f"PASS {assertions} total deterministic assertions")
