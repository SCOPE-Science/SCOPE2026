#!/usr/bin/env python3
"""Exact rational checks for a one-edge FJ seed-ranking construction.
All arithmetic is carried out using fractions.Fraction.
"""
from fractions import Fraction as Q


def instance(m):
    assert isinstance(m, int) and m >= 2
    eps = Q(1, 10 * m**4)
    alpha = [Q(m*m-i*i) for i in range(m)]
    beta = [i*eps for i in range(m)]
    A, B = sum(alpha), sum(beta)
    thresholds_leaf = [((1+B)*Q(2*i+1)/eps-(1+A))/2 for i in range(m-1)]
    t_first = thresholds_leaf[0]/2
    delta = 1/(1+A+alpha[0]+t_first)
    kappa = (1+B+2*beta[-1]+2*eps**2)/2
    assert 0 < kappa < 1 and 0 < delta < 1
    t_last = ((1+B)*((1+A)/2+alpha[-1])-(1+A)*eps**2)/(2*eps**2)
    times = [t_first]+thresholds_leaf+[t_last]
    assert len(times) == m+1 and 0 < times[0]
    assert all(x < y for x,y in zip(times, times[1:])), (m,times)
    # Numerator lines (affine in t), with common positive denominator n*(1+A+t)
    lines = [(Q(1), Q(0))]
    lines += [(delta*((1+A)*(1+beta[i]/(1+B))+alpha[i]),
               delta*(1+2*beta[i]/(1+B))) for i in range(m)]
    lines.append((delta*kappa*(1+A)/(1+B),delta*kappa*2/(1+B)))
    assert len(lines) == m+2
    assert all(lines[i][1] < lines[i+1][1] for i in range(m+1))
    for j,t in enumerate(times):
        p,q = lines[j], lines[j+1]
        assert p[0]+p[1]*t == q[0]+q[1]*t
        assert all(p[0]+p[1]*t >= a+b*t for a,b in lines)
    probes = [times[0]/2] + [(u+v)/2 for u,v in zip(times,times[1:])] + [times[-1]+1]
    for j,t in enumerate(probes):
        values = [a+b*t for a,b in lines]
        assert values[j] == max(values)
        assert values.count(values[j]) == 1
    # Explicit matrix inverse identity checked via exact Gauss-Jordan independently.
    def inverse(mat):
        n = len(mat)
        z = [[Q(mat[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
        for i in range(n):
            k = next(k for k in range(i,n) if z[k][i])
            z[i],z[k] = z[k],z[i]
            x = z[i][i]
            z[i] = [a/x for a in z[i]]
            for k in range(n):
                if k==i: continue
                x=z[k][i]
                z[k]=[a-x*b for a,b in zip(z[k],z[i])]
        return [row[n:] for row in z]
    # indices 0=a, 1=b, i+2=v_i; row follows edge target
    for t in [Q(0),times[0],times[-1],times[-1]+1]:
        M=[[Q(i==j) for j in range(m+2)] for i in range(m+2)]
        for i in range(m):
            M[0][0]+=alpha[i]; M[0][i+2]-=alpha[i]
            M[1][1]+=beta[i]; M[1][i+2]-=beta[i]
        M[0][0]+=t; M[0][1]-=t
        H=inverse(M)
        s=[Q(1),delta*kappa]+[delta]*m
        truth=[s[j]*sum(H[i][j] for i in range(m+2)) for j in range(m+2)]
        predicted=[(aa+bb*t)/(1+A+t) for aa,bb in [lines[0],lines[-1]]+lines[1:-1]]
        assert truth==predicted, (m,t,truth,predicted)
    return times,eps,delta,kappa


def main():
    for m in range(2,18):
        ts,eps,delta,kappa=instance(m)
        print(f'm={m}, n={m+2}: PASS {len(ts)} distinct positive switches; monotone unique optimizers')
        if m==2:
            print('m=2 exact data:', 'eps',eps,'delta',delta,'kappa',kappa,'switches',ts)
    print('ALL_EXACT_RATIONAL_CHECKS_PASSED')


if __name__=='__main__':
    main()
