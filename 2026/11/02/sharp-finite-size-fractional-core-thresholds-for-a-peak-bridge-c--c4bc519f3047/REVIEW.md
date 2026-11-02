# Scientific review

## Correctness — PASS
The claim is a sharp maximum over **all nonempty coalitions** and capped fractional candidate weights, not merely a lower-bound witness. The proof gives explicit full-coalition allocations attaining the odd/even expressions; normalized nonnegative dual voter weights certify the cost of serving any consecutive coalition block. Since nonadjacent blocks do not share useful candidates, summing their certificate-implied spending establishes the global upper bound. The strict inequality in the fractional blocking axiom is handled at equality. Uniqueness of the integral JR committee follows from singleton demands and a run-counting argument. Rational checks (80 instances), plus independent numerical coalition LPs (2,505 instances), agree, without replacing the infinite proof.

## Originality — PASS, with residual priority risk
The motivating 20 October 2026 paper is inspected at its definitions, Theorem 10, and Appendix E. It proves the asymptotic factor-two impossibility using an interior-coalition feasible deviation and does not present this exact finite-size all-coalition maximum. The present result bounds all coalitions, characterizes a sharp threshold for each population/bridge value, and exposes parity. Jin--Liu--Tao's 3 August 2026 approval-based incompatibility has a different domain and does not imply the exact real-valued formulas. Searches for aliases such as path/chain voting, peak--bridge, grand-coalition deviation and finite-size fractional-core ratio did not locate equivalent coverage. Unindexed work or a later source version could have an equivalent statement; independent priority verification remains open.

## Mathematical value — PASS
The motivating impossibility proof leaves a concrete finite-parameter quantitative gap: it exhibits a viable fractional blocking factor but does not quantify the strongest coalition or exact threshold for a fixed number of seats. Closing the maximum simultaneously over all coalitions and fractional deviations makes this standard counterexample a calibrated benchmark for best-of-both-worlds representation. The parity corrections and an explicit family of optimal primal and dual certificates are structural, not a numerical slice or a trivial reparameterization. The scope is this family, not a general improvement on the established universal factor-two theorem.

## Limits
The candidate-value interval is \(1/2<v<1\); the core has \(\beta=1\) and strict coalition-wide utility improvement. The proof is fully analytical, with finite tests used for corroboration. Publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
