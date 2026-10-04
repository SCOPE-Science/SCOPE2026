# Same-model review

## Correctness
PASS. The theorem reduces to one set inclusion. If \(R(g)=K\), then \(g(s)\le K z_\alpha\sqrt{s}\) pointwise, so every Brownian path admitted by \(g\) is admitted by the square-root envelope. A calibrated candidate therefore forces the envelope crossing quantile to be at least \(c_\alpha(\Delta)\). The square-root boundary attains equality by definition of that quantile. The conversion from Brownian partial-sum boundary to mean half-width was checked against the confidence-horizon formula in Theorem 3.3.

## Originality
PASS, with a recorded literature risk. The closest source, Confidence Horizons, gives the power family and the square-root member, but the inspected theorem, appendix duality, group-sequential discussion, and power appendix do not formulate or prove the global minimization over arbitrary deterministic boundary shapes for worst fixed-time-relative width. Wang–Tsiatis optimize a group-sequential testing family under different design criteria. Jennison–Turnbull establish repeated confidence intervals but the material inspected does not state this global boundary-shape optimization. Targeted semantic/database searches returned no equivalent claim.

## Value
PASS. Bounded-horizon sequential inference requires choosing how precision is distributed across information times. The result supplies a criterion-specific, horizon-wide design guarantee with no numerical search over shapes: if the priority is to minimize the largest multiplicative precision loss relative to ordinary fixed-time Gaussian intervals, a square-root/Pocock-shaped boundary is globally optimal, not merely a convenient member of a parametric family. This clarifies when the \(q=1/2\) design has a principled advantage despite other \(q\) values being preferable for power or stopping-time objectives.

## Closest literature and limitations
The central source is Mathis–Waudby-Smith, arXiv:2608.03889v1. The older comparison sources are Wang–Tsiatis (1987), DOI 10.2307/2531959, and Jennison–Turnbull (1984), DOI 10.1016/0197-2456(84)90148-X. The result is restricted to the Brownian asymptotic design problem and its stated minimax loss. It does not claim finite-sample validity, a unique minimizer, or optimality for power, expected stopping time, or average width. Full text of the two older comparison papers was not available in the inspected material, so terminological duplication remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
