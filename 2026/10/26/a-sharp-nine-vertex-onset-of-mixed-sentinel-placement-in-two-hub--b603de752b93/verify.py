"""Exact rational checks for the two-hub two-sentinel incidence theorem.

Requires Python 3 standard library only. Finite enumerations are checks,
not substitutes for the theorem's general proof.
"""
from fractions import Fraction as F
from math import comb
import json


def probs(m, p):
    assert m >= 2 and F(0) < p < F(1)
    q = 1-p
    r = 1-p*p
    b = 1-q*q
    hh = m*q*q
    hl = q*q*((m-1)+(1+m*p)*r**(m-2))
    if m == 2:
        ll = hh
    else:
        ll = q*q*((m-2)+q*q*(2+(m-2)*b)+2*b*q*(1+(m-1)*p)*r**(m-3))
    return {"HH":1-hh/(m+2), "HL":1-hl/(m+2), "LL":1-ll/(m+2)}


def raw_polynomial(m):
    """Power coefficients of f=(U_LL-U_HL)/(p(1-p)^2)."""
    def add(a,b):
        return [((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))) for i in range(max(len(a),len(b)))]
    def mul(a,b):
        c=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    def power(a,n):
        z=[F(1)]
        for _ in range(n):z=mul(z,a)
        return z
    # Difference divided by q^2; its zero at p=0 cancels.
    p=[F(0),F(1)]; q=[F(1),F(-1)]; r=[F(1),F(0),F(-1)]
    b=[F(0),F(2),F(-1)]
    q2=mul(q,q)
    lhs=add([F(m-2)],add(mul(q2,add([F(2)], [F(0),F(2*(m-2)),F(-(m-2))])), mul(mul(mul([F(2)],b),q),mul([F(1),F(m-1)],power(r,m-3)))))
    rhs=add([F(m-1)],mul([F(1),F(m)],power(r,m-2)))
    diff=add(lhs,[-x for x in rhs])
    assert diff[0] == 0
    return diff[1:]


def bernstein_negative_on_segment(poly,left):
    """Bernstein coefficients of -poly(p) on p=left+(1-left)t."""
    n=len(poly)-1
    mon=[F(0)]*(n+1)
    for k,a in enumerate(poly):
        for j in range(k+1):
            mon[j]-=a*comb(k,j)*left**(k-j)*(1-left)**j
    return [sum(mon[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]


def brute(m,p):
    """Enumerate edge states, find all outbreak components, average over seeds."""
    n=m+2
    edges=[(h,2+i) for i in range(m) for h in (0,1)]
    total={k:F(0) for k in ("HH","HL","LL")}
    ss={"HH":{0,1},"HL":{0,2},"LL":{2,3}}
    for bits in range(1<<len(edges)):
        par=list(range(n))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        for k,(a,b) in enumerate(edges):
            if bits>>k&1:
                par[find(a)]=find(b)
        comp=[find(i) for i in range(n)]
        nedge=bits.bit_count()
        weight=p**nedge*(1-p)**(2*m-nedge)
        for typ,sensors in ss.items():
            seen={comp[x] for x in sensors}
            total[typ]+=weight*sum(comp[i] in seen for i in range(n))/n
    return total


def main():
    checks=0
    for m in range(2,7):
        for p in (F(1,3),F(1,2),F(2,3)):
            assert brute(m,p)==probs(m,p),(m,p)
            checks+=1
    # Expected polynomial factorizations are asserted coefficient by coefficient.
    f5=[F(1),0,-3,-18,33,-5,-17,8]
    f6=[F(2),0,0,-42,60,16,-64,15,22,-10]
    assert raw_polynomial(5)==f5
    assert raw_polynomial(6)==f6
    expected5=[1995,3855,5510,6708,7296,7360,7200,6720]
    expected6=[34820250689,130840487848,215172026370,283058412200,332256472000,363573600000,379976000000,384160000000,376320000000,358400000000]
    b5=bernstein_negative_on_segment(f5,F(1,2))
    b6=bernstein_negative_on_segment(f6,F(11,20))
    assert b5==[F(z,6720) for z in expected5]
    assert b6==[F(z,358400000000) for z in expected6]
    assert min(b5)>0 and min(b6)>0
    def U(m,p):
        z=probs(m,p)
        return {k:(1-v)*(m+2) for k,v in z.items()}
    u7=U(7,F(11,20))
    assert u7['HL']<u7['HH'] and u7['HL']<u7['LL']
    assert u7['HL']-u7['HH']==F(-3306362852256057,81920000000000000)
    assert u7['LL']-u7['HL']==F(5900587445173509,204800000000000000)
    for m in range(8,101):
        z=probs(m,F(1,2))
        assert z['HL']>z['HH'] and z['HL']>z['LL']
        assert ((1+F(m,2))*F(3,4)**(m-2))<1
        assert F(3*m-14,16)-F(3,8)*F(3,4)**(m-3)>0
    report={
      'type':'exact_replay_certificate',
      'model':'independent_bond_K_2_m_uniform_seed_two_monitors',
      'exhaustive_graph_size_range':'2 <= m <= 6',
      'exhaustive_transmission_parameters':['1/3','1/2','2/3'],
      'exhaustive_graph_parameter_cases':checks,
      'exhaustive_edge_states':sum(3*2**(2*m) for m in range(2,7)),
      'bernstein_m5_numerators':expected5,'bernstein_m5_denominator':6720,
      'bernstein_m6_numerators':expected6,'bernstein_m6_denominator':358400000000,
      'm7_at_11_over_20_UM_minus_UHH':str(u7['HL']-u7['HH']),
      'm7_at_11_over_20_ULL_minus_UM':str(u7['LL']-u7['HL']),
      'large_m_tested':'8 <= m <= 100 (finite corroboration; proof covers all m >= 8)',
      'result':'all_exact_checks_passed'
    }
    print(json.dumps(report,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
