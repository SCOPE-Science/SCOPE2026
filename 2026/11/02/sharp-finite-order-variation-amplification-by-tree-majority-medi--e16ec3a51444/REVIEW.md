# Scientific review

## Correctness — PASS
The result is a one-input variation-gain theorem for synchronous majority-median filtering on finite unweighted trees, not a two-input stability assertion. For binary inputs, strict majority at a flipping vertex yields \(2b_v-\deg(v)\ge1\); summing over the flip forest proves the stronger \(J(Mx)\le2J(x)-c(F)\). The finite-order optimization uses both \(J(Mx)\le n-1\) and integer input cut sizes. Order-statistic threshold commutation and the exact coarea identity extend the result to all real signals. Explicit extremizers attain the upper bound for both parities, including separately verified small orders. Reproducible tests passed on all labeled trees through six vertices and further samples; the universal proof is analytical.

## Originality — PASS, subject to literature risk
The relevant 2013 and 2014 primary majority-dynamics papers concern information retention, period-two behavior, random-graph consensus, and a temporal Lyapunov functional, not the sharp one-step edge-variation ratio. The 2026 finite-tree study characterizes stabilization time, rather than the one-step variation operator's growth envelope. published-finding corpus searches for the formula, majority dynamics, tree cut amplification, and median variation found no directly covering record. These are statement-level comparisons, not novelty certification. An equivalent bound hidden in older majority/median-filter literature remains a residual risk.

## Mathematical value — PASS
The precise object is a classical nonlinear neighborhood filter on the edge-BV seminorm, where ordinary time-step dynamics need not reduce variation. The new flip-component deficit gives a structural explanation for a universal bound; the exact order-dependent optimum and parity-specific extremal constructions quantify the maximum possible amplification. Transferring a sharp binary dynamical estimate to arbitrary real signals by coarea is operationally relevant for median filtering and produces a natural complete extremal invariant, not a sampled special case.

## Scope and limitations
No assertion is made for non-tree graphs, edge weights, asynchronous dynamics, other median definitions, or the global two-input Lipschitz modulus. Primary full texts were inspected selectively around their definitions, theorem statements, and energy arguments; source-specific limitations and unresolved historical coverage are recorded in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
