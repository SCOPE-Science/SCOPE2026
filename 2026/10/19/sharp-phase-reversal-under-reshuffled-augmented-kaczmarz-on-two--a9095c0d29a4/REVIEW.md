# Independent mathematical audit

## correctness

PASS

Morshed's Eq. (18) gives the fixed-penalty primal/auxiliary recurrence on unit rows; Algorithm 2 as printed is the adaptive counterpart, not a constant-penalty specification. The record explicitly specializes to fixed penalty, so Eq. (18) suffices. Eliminating z, with y=x-bar(b) and q=1-p, gives y_{k+1}=2q y_k-q y_{k-1}+p xi_{i_k}; take y_{-1}=y_0+z_0. The companion matrix T=[[2q,-q],[1,0]] has roots q±i sqrt(pq) of modulus sqrt(q). Thus deterministic starts decay and stable covariance limits exist at both phases. In a separate symbolic reconstruction with unit noise variance, solve the three independent entries of X=A X A^T+B B^T with (A,B)=(T,(p,0)^T) for IID and (T^2,(T-I)(p,0)^T) for the epoch-boundary process driven by independent opposite-sign pairs. The mid-epoch covariance is T X T^T+(p,0)^T(p,0), as the fresh first signed observation is independent of the boundary state. Solving these equations in the companion coordinates reproduces all three risk numerators and both difference factors in RESULT.md. The quadratic in H is 5(p-4/5)^2+4/5; the boundary difference has positive numerator 4q(1-q^2+4q^3), and the mid-epoch difference changes sign only at p=3-sqrt(5). Evaluation at p down to zero gives both reshuffled slopes sigma^2/4 and IID limit sigma^2/2. The frozen verifier validates the displayed covariance substitutions and factorizations, not a claim about finite-time or sample-path ordering.

## originality

PASS

The supported distinct claim is the fixed-phase reshuffled risks and their sharp within-epoch comparison for the two inconsistent identical rows, not the algorithm, the exact IID formula (already implied by a prior white-noise momentum theorem), or reshuffling variance as a general mechanism. The closest prior heavy-ball reshuffling theorem averages over a randomized epoch offset and does not give the conditional sign reversal. This is a bounded best-of-knowledge decision.

## value

PASS

The smallest inconsistent data set with fresh random epochs isolates a real distinction between evaluation at epoch boundaries and at intermediate updates. The exact parameter where an improvement becomes a penalty at the intermediate phase is useful when interpreting stationary comparisons that report only an endpoint or a time average. The example defeats inference of a per-phase ordering from a favorable epoch-boundary result, without claiming a general ordering, and contributes more than a recomputation of known IID variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
