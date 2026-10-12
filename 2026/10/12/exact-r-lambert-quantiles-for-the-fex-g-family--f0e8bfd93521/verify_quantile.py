import math
P = math.e/(math.e-1.0)
def kappa(u):
    return -math.log(1.0 + math.log(1.0-u/P))
def neg_branch(k):
    def h(t): return t*(math.exp(t)-1.0)-k
    lo=-max(2.0,2.0*k+2.0)
    while h(lo)<0.0: lo*=2.0
    hi=-1e-15
    for _ in range(220):
        mid=(lo+hi)/2.0
        if h(mid)>0.0: lo=mid
        else: hi=mid
    return (lo+hi)/2.0
def T(w):
    return P*(1.0-math.exp(-(1.0-(1.0-w)**w)))
def baseline_prob(u):
    t=neg_branch(kappa(u))
    return 1.0-math.exp(t),t
for u in (1e-6,0.1,0.5,0.9,1.0-1e-6):
    w,t=baseline_prob(u)
    assert 0.0<w<1.0 and t<0.0
    assert abs(T(w)-u)<2e-12
a,b=1.7,2.3
for u in (0.1,0.5,0.9):
    w,t=baseline_prob(u)
    x=(1.0-math.exp(t/b))**(1.0/a)
    G=1.0-(1.0-x**a)**b
    assert abs(G-w)<2e-12
    assert abs(T(G)-u)<2e-12
print("VERIFY_OK")
