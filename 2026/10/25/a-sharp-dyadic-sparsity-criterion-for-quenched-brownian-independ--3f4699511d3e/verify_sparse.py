"""Exact finite checks of the dyadic-sparse bootstrap covariance calculation.

Requires only the Python standard library.  No finite calculation is used
as a substitute for the asymptotic proof.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def parity_digit(s, j):
    return (s >> j) & 1


def f_from_bits(s, bits):
    return -1 if sum(b * parity_digit(s, j) for j,b in enumerate(bits))%2 else 1


def g(s, ps):
    v = Q(1)
    for j,p in enumerate(ps):
        if parity_digit(s,j): v *= 1-2*p
    return v


def b_uniform(ps):
    return Q(1) if not ps else __import__('math').prod(1-p for p in ps)


def binomial_residue(n, q):
    masses = [Q(0) for _ in range(q)]
    for s in range(n+1): masses[s % q] += Q(comb(n,s),2**n)
    return masses


def main():
    checks=0
    for n in range(1,25):
        for r in range(0,min(5,n.bit_length())):
            ps=[Q(1+((n+3*j)%3),5) for j in range(r)]
            q=2**r
            avg=sum((g(s,ps) for s in range(q)),Q(0))/q
            assert avg==b_uniform(ps)
            checks+=1
            for s in range(q):
                direct=Q(0)
                for bits in product((0,1),repeat=r):
                    mass=Q(1)
                    for bit,p in zip(bits,ps): mass*=p if bit else 1-p
                    direct+=mass*f_from_bits(s,bits)
                assert direct==g(s,ps)
                checks+=1
            dist=binomial_residue(n,q)
            expected=sum((dist[s]*g(s,ps) for s in range(q)),Q(0))
            direct=sum((Q(comb(n,s),2**n)*g(s,ps) for s in range(n+1)),Q(0))
            assert expected==direct
            checks+=1
            # Exact total-variation control of binomial residues.
            tv=sum((abs(x-Q(1,q)) for x in dist),Q(0))/2
            assert abs(expected-avg)<=2*tv
            checks+=1
    # Cross-time factorization of independent environmental rows,
    # checked directly by all bit paths for the first 8 steps.
    arrays={n:[Q(1+((n+2*j)%3),5) for j in range(min(2,n.bit_length()))]
            for n in range(1,9)}
    for N in range(2,9):
        path_corr=Q(0)
        for xs in product((0,1),repeat=N):
            s=0; vals=[]
            for n,x in enumerate(xs,1):
                s+=x
                vals.append(g(s,arrays[n]))
            path_corr += Q(1,2**N)*sum((vals[i]*vals[j]
                             for i in range(N) for j in range(i+1,N)),Q(0))
        pair_corr=Q(0)
        for i in range(1,N):
            for j in range(i+1,N+1):
                pair_corr += sum((Q(comb(i,s)*comb(j-i,t),2**j)*
                                g(s,arrays[i])*g(s+t,arrays[j])
                                for s in range(i+1) for t in range(j-i+1)),Q(0))
        assert path_corr==pair_corr
        checks+=1
    print(f'PASS: {checks} exact rational identities and comparisons.')
    print('PASS: uniform-residue means equal products of (1-p) for all tested rows.')
    print('PASS: independent-row cross moments match direct full-path enumeration.')
    print('LIMIT: the quenched functional limit and density criterion require the analytic proof.')

if __name__=='__main__': main()
