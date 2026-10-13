# Scientific review

## Correctness — PASS

The two update matrices are exact for the given scalar quadratic. A zero-delay update is rank one, and multiplying the block factors yields a monodromy matrix with characteristic roots zero and the explicit product of \(p_L\). The path-adjacency characteristic recurrence proves the cosine-root formula and its unbounded largest-root asymptotics. The period-three stability intervals follow from two strict quadratic inequalities. Exact tests for every binary period through length eight, short-run characteristic polynomials, and nilpotent period-three monodromy support the algebra; the all-period conclusions are analytical rather than enumerative.

## Originality — PASS (scoped, with historical risk)

Generic Floquet/Schur criteria are established and credited to classical sources and Duman–Çelik Kızılkan–Aydın (2016); the special calculation is not a new general stability criterion. Mitliagkas et al. (2016) examine random-delay-induced momentum; McMahan–Streeter (2014) analyze delayed online-learning regret. Čermák–Jánský (2014) study autonomous constant-lag stability switches, which do not determine this time-periodic reset/stale word. The specific all-binary-period multiplicative law, exact roots, and arbitrarily large finite-time cancellation were not found in the inspected materials or the searched published mathematical records. Residual risk: an equivalent specialized identity may appear in historical switching-difference-equation literature.

## Value — PASS

The all-pattern formula replaces repeated \(2\times2\) matrix-product eigenanalysis by a combinatorial run decomposition and exact path-spectrum factors. It gives a complete test for any prescribed finite periodic schedule and reveals a non-obvious disconnected stability region even for a period-three schedule. Finite-time cancellation at arbitrarily large prescribed stepsizes is a rigorous boundary phenomenon in optimization under stale gradients, with explicit caveats about tuning and noise. This is a precise dynamical classification rather than a mere new test instance.

## Limits and verification state

The theorem is scalar, quadratic, deterministic, periodic, exact-arithmetic, and assumes at least one fresh step per period. It does not give robustness guarantees in the large-stepsize regime. The comparison with older periodic delay literature cannot exclude undiscovered equivalent proofs.

Self-review: passed. Independent audit: not yet performed.
