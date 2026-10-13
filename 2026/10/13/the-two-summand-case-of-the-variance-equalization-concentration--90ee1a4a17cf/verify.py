from fractions import Fraction


def k_of(a):
    if not (Fraction(0) < a <= 1):
        raise ValueError('alpha must lie in (0,1]')
    return a.denominator // a.numerator


def tau_of(a):
    k = k_of(a)
    t = k * (k + 1) * a - k
    assert 0 < t <= 1
    return k, t


def nu(m):
    return {-(m - 1) + 2*i: Fraction(1, m) for i in range(m)}


def mix(p, q, wp, wq):
    out = {}
    for x, px in p.items():
        out[x] = out.get(x, Fraction(0)) + wp * px
    for x, qx in q.items():
        out[x] = out.get(x, Fraction(0)) + wq * qx
    return {x:v for x,v in out.items() if v}


def T(a):
    k, t = tau_of(a)
    return mix(nu(k), nu(k+1), t, 1-t)


def conv(p, q):
    out = {}
    for x, px in p.items():
        for y, qy in q.items():
            out[x+y] = out.get(x+y, Fraction(0)) + px*qy
    return out


def q2_direct(a, b):
    d = conv(T(a), T(b))
    lo, hi = min(d), max(d)
    # For integer support, a half-open interval of length two can be shifted
    # to contain either one integer or two consecutive integers.
    return max(d.get(j,0) + d.get(j+1,0) for j in range(lo-1, hi+1))


def q2_formula(a, b):
    ka, ta = tau_of(a)
    kb, tb = tau_of(b)
    if ka == kb:
        k = ka
        return Fraction(1, k+1) + ta*tb/Fraction(k*(k+1),1)
    return min(a,b)


def var_direct(a):
    d = T(a)
    mean = sum(Fraction(x)*p for x,p in d.items())
    return sum((Fraction(x)-mean)**2*p for x,p in d.items())


def var_formula(a):
    k, _ = tau_of(a)
    return Fraction(k*(k+1),1) * (1 - Fraction(2*k+1,3)*a)


def alpha_from_var(v):
    # v(alpha) is continuous and strictly decreasing. Search the unique cell.
    for k in range(1, 200):
        vlo = Fraction(k*k-1,3)       # v(1/k)
        vhi = Fraction(k*(k+2),3)     # limit at 1/(k+1)
        if vlo <= v < vhi or (k == 199 and v == vhi):
            a = Fraction(3,2*k+1) * (1 - v/Fraction(k*(k+1),1))
            if Fraction(1,k+1) < a <= Fraction(1,k):
                return a
            if a == Fraction(1,k+1):
                return a
    raise ValueError(v)


def check_uniform_pair_identity():
    for r in range(1,25):
        for s in range(1,25):
            d=conv(nu(r),nu(s))
            central=d.get(0,0)+d.get(1,0)
            assert central == Fraction(1,max(r,s)), (r,s,central)


def sample_alphas(limit=18):
    vals={Fraction(1,1)}
    for k in range(1,limit+1):
        # canonical cell (1/(k+1), 1/k], with several rational interior points
        vals.add(Fraction(1,k))
        for den in range(2,8):
            a=Fraction(den-1,den)*Fraction(1,k+1)+Fraction(1,den)*Fraction(1,k)
            vals.add(a)
    return sorted(vals)


def main():
    check_uniform_pair_identity()
    vals=sample_alphas()
    for a in vals:
        assert var_direct(a)==var_formula(a), a
    checked=0
    for i,a in enumerate(vals):
        for b in vals[:i+1]:
            qd=q2_direct(a,b)
            qf=q2_formula(a,b)
            assert qd==qf, (a,b,qd,qf)
            av=alpha_from_var((var_formula(a)+var_formula(b))/2)
            lhs=qd
            rhs=q2_formula(av,av)
            assert lhs <= rhs, (a,b,av,lhs,rhs)
            if a != b:
                assert lhs < rhs, (a,b,av,lhs,rhs)
            checked += 1
    # A concrete case outside Kanter's alpha_i >= 1/2 range.
    a,b=Fraction(1,3),Fraction(1,5)
    av=alpha_from_var((var_formula(a)+var_formula(b))/2)
    assert av==Fraction(11,45)
    assert q2_formula(a,b)==Fraction(1,5)
    assert q2_formula(av,av)==Fraction(97,405)
    print('VERIFY_OK')
    print('pairs_checked', checked)
    print('example_alpha_star', av)
    print('example_lhs', q2_formula(a,b))
    print('example_rhs', q2_formula(av,av))


if __name__=='__main__':
    main()
