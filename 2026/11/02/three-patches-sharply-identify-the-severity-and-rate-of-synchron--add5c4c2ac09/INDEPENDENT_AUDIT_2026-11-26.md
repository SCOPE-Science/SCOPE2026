# Independent mathematical audit

## correctness

PASS

For the product of j specified stationary indicators, local flips contribute ja(p_{j-1}-p_j)-jb p_j and catastrophes multiply the product in expectation by (1-q)^j. Irreducibility and exchangeability follow from the positive local rates and symmetric generator. Dividing the balance equations gives m=x(1-s), A=sq/2 and B=s(q-q^2/3). The ratio B/A identifies q; the range [4/3,2) is exactly 0<q<=1. The strict inequality s<1-m is exactly x<1. Reconstruct a,b,c with any positive total local rate; the first three balance equations recover the supplied moments, proving actual realizability on every stated finite N, not just a moment constraint. Exchangeable three-site laws are equivalent to these three moments by inclusion-exclusion. Two-site laws fix only m and sq, and all q' in (2A/(1-m),1] give the same law after reconstruction, including a one-sided continuum at q=1. Rescaling the time unit leaves the law unchanged. The (x,s,q) to (m,A,B) determinant is -(1-s)sq^2/6, and the second triangular change has determinant m^5/[(1-A)^3(1-B)^2]. At fixed interior x,s the limiting Jacobian has rank two at q=0, so the smallest singular value and determinant vanish quadratically; the implied c/(a+b) grows like 1/q on that path. An independent diagnostic solved the lumped occupancy-count stationary chain on states 0 through N, rather than the full configuration chain, for N=3–9 and 504 combinations of local and event rates and severities including q=1; normalized inverse errors were below 3e-10 in floating point and the illustrative two-site ambiguity agreed. The exact proof is not based on this finite check. The packaged CHECKER.py instead checks the full-state rational generator for N=3,4, with 10,975 checks recorded in VERIFICATION.md; it was inspected, not executed. To replay the package use Python 3.10 or newer, since int.bit_count is used despite the stated 3.8 minimum. This does not change the mathematics.

## originality

PASS

The binomial-catastrophe forward factorial-moment structure is established, and its small-order algebra is close to the inverse. The supported distinction is the full-capacity finite-patch static inverse with all three normalized coordinates unknown, its exact feasible region, the two-patch continuum, and the fixed-x,s singularity order. The stated general moment precedent does not include the finite-capacity rates in its hypotheses, and the inspected same-day results cover different objectives or a known-severity boundary, not the unknown-severity inverse.

## value

PASS

A common event's frequency and per-site severity are exactly confounded in the two-site stationary law but not in the three-site law. This gives a sharp, natural observation-design distinction and explicit model-checking constraints with a quantitative weak-severity limit. It does not claim field-data efficiency, unknown detection, dependence between local rates, or recovery of absolute time scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
