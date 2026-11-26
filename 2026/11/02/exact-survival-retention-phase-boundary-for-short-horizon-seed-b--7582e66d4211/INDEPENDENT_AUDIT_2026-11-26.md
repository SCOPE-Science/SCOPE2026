# Independent mathematical audit

## correctness

PASS

The source's sibling-bank two-year expression reduces to A(A+B)+BD+(1-A)C under h=s(1-r)/r and z=g+b(1-g); each of its four terms was matched. At t=1-g=0 the baseline is 1. With P=2h²+6h+4 and Q=h²+5h+5, the exact derivative there is h(bQ-P)/(1+h)^3, so b>P/Q makes a sufficiently small positive t advantageous. For t>0, A,B,C strictly increase with b, D is fixed, A>=C and 1-A>0; differentiating the expression therefore gives strict survival monotonicity. At b=P/Q the denominator is positive: K-t>0, U=Q+2(h+2)t>0 and V=Q(z+h)>0, where K=1+h. I independently formed the rational expression in SymPy, cancelled it exactly, and transformed the remaining bivariate polynomial to the degree-four Bernstein basis in t. All 65 coefficients agree with the displayed table, and the final row gives the strict positive contribution h^12. Thus at threshold E2<1 for t>0, including t=1; monotonicity implies strict failure below it. The independent calculation also checked the b=1 factorization, which proves failure for h>=(sqrt(5)-1)/2 and t>0. The threshold derivative with respect to h is 2(2h²+6h+5)/Q²>0, with limits 4/5 and 2. Every h>0 is realizable by taking any s in (0,1) and r=s/(s+h), so the universal floor is sharp. The rational example gives E2-1=19650205/6450554528. Replay: python3 /workspace/branches/reproduce_frozen_math.py 1 (Python 3 and SymPy).

## originality

PASS

The pointwise site-lottery formula, the finite-horizon mechanism, and an approximate numerical 0.8 cutoff are known and credited. The distinct result is eliminating g globally for the exact finite-horizon expression, including strict threshold equality and the parameter-dependent physical exclusion. The inspected primary derivation and numerical results do not supply the necessary all-g inequality. Neither of the inspected related threshold families uses the same expression or objective. This is a bounded assessment, not a priority guarantee.

## value

PASS

The theorem resolves an optimization question motivated by the original ecology model and its approximate cutoff. It replaces a parameter scan and a local sufficient condition with the exact eligibility region for any partial-dormancy advantage, including exclusion at equality and a competition regime in which even perfect seed survival cannot help. A user of this exact finite-horizon proxy can decide feasibility without optimizing over germination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
