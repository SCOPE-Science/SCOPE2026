# Scientific review

## Correctness — PASS
For \(n\ge2\), the mixed moment is reconstructed by marking a directed two-cycle and separately counting targets not hit by any remaining arrow. Subtracting marginal means yields the exact covariance identity. The discrete anti-monotone covariance inequality applied to \(P\) and \(h(P)=(1-P)^{n-2}\) yields the sharp bound, including strictness and equality conditions. Fixed-point orthogonality follows from conditional renormalization after forbidding a target. A standalone exact-rational checker passed 318 assertions; the unrestricted conclusions depend on the analytic argument, not the finite checks.

## Originality — PASS, with residual priority risk
The principal motivating 2022 paper concerns uniform mapping component and cycle length statistics. Hansen–Jaworski (2008) handles exchangeable random indegrees, whereas nonuniform common-target mappings induce nonexchangeable target indegrees; its main conditional result does not directly give the heterogeneous bound. Prior research records for uniform mapping terminal/cyclic dependence and fixed-point-degree orthogonality were treated as covering their respective special cases. The contribution tested here is precisely the sharp all-target-vector two-cycle covariance inequality and its equality classification. A historical argument based on weighted occupancy or a general p-mapping calculus may still imply the statement, and priority requires independent investigation.

## Value — PASS
A two-cycle is the simplest nontrivial recurrent component of a functional graph. The inequality proves a robust opposition between the number of unchosen targets and two-cycle formation, despite arbitrary target heterogeneity and possible zero weights, with a sharp numerical covariance guarantee. The zero one-cycle covariance supplies a contrasting structural boundary. This is a finite, natural all-parameter dependence law, not a computation for a selected parameter list.

## Scope and limitations
The law requires independent outputs sharing a common target distribution. It does not imply negative association, extend to arbitrary origin-dependent arrays, or classify longer directed cycles. The exact-covariance calculus is elementary but the global inequality and its equality case are separately proved; historical priority remains open.

Self-review: passed. Independent audit: not yet performed.
