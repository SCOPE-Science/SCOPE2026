# Independent mathematical audit

## correctness

PASS

PASS. Alternating bipartite visits are independent iid uniform streams of B and A labels. Since the starting A vertex is already observed, the A completion count equals C_a-1 in law and B count equals C_b, so the terminal side is B iff C_b>=C_a (including tie because B is visited at odd times). Inclusion–exclusion for missing coupons combined with the product geometric-stage PGF proves the exact rational sum for a,b>=1. Monotone geometric-stage coupling proves p>1/2 iff b>=a, with strict inequalities due to positive tie mass (a=1 boundary yields 1). Standard coupon collector centering m log m and Gumbel convergence yield logistic difference and n/log n imbalance window for b/n->1. Fourier inversion of the lattice tie probability, the characteristic-function bound from the slowest geometric stage and Plancherel for g(x)=exp(-x-exp(-x)) rigorously imply n Pr(C_n=C_n') -> integral g^2=1/4. Thus p_n=1/2+1/(8n)+o(1/n), and TV from uniform over 2n-1 unvisited vertices is |p_n-n/(2n-1)|~1/(8n), with n=2 exactly uniform. Inspected verify.py compares two independent exact recursions on a,b<=10, 314 rational assertions, not substitutes for limits.

## originality

PASS

Best-of-knowledge PASS for the precise complete-bipartite quantitative boundary, logistic transition and balanced tie/TV constants. Generic Markov-chain joint cover-time formulas can yield finite law by specialization, and Gumbel comparison is classical; the submitted sharp finite majority dichotomy plus scaled transition and 1/8 TV invariant are assessed jointly, not claimed as unprecedented general coupon-collector facts.

## value

PASS

PASS. Last discovered vertex is a natural graph cover-time statistic; part asymmetry, a surprising strict tie advantage in balanced graphs, a size-ratio transition at n/log n and sharp total-variation decay are motivated quantitative questions for exact random-walk coverage. Distinguishing an explicit finite formula from nontrivial all-size and asymptotic sharp laws gives more than mechanical application of generic inclusion–exclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
