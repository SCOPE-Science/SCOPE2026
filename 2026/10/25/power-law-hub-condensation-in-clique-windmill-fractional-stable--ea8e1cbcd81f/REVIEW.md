# Scientific review

## Correctness — PASS

The claim is a single fixed-clique-size theorem with an exact finite fiber and two asymptotic probability laws. For a hub coordinate \(t\), the fractional block fiber is \(c_r-t^r\) for \(t\le1/2\), by partition into the half-cube and exactly-one-large-coordinate caps, and \((1-t)^r\) above \(1/2\). The integral polytope fiber is a Cartesian product of \(r\)-simplices. These facts give both exact volumes. After division by \(c_r^m\), the first fractional volume integral has the scaled integrand \((1-u^r/(c_rm))^m\), dominated by \(e^{-u^r/c_r}\), yielding the gamma constant and the uniform-point hub law. The true hub coordinate is exactly beta-distributed with parameters \((1,rm+1)\). Direct hull, quadrature and distributional diagnostics passed in the supplied `check.py`; only the analytical argument certifies the infinite limits. Risks: no rate of convergence or uniformity in varying \(r\) is established.

## Originality — PASS, qualified

The relevant source matching the graph edge-relaxation object most closely is Hamano–Hibi–Ohsugi (arXiv:1603.09613), whose main results are about Ehrhart series and Gorenstein properties, not uniform-point hub concentration. Steingrímsson's earlier all-graph deletion recurrence can compute finite volumes and therefore dominates isolated finite-volume calculations; the claimed new content is the exact familywise marginal limit and the sharp power-law residual volume amplification. Okada–Tsuchiya (arXiv:2003.12271), the middle-period primary geometric source, treats enriched and ordinary poset polytopes but not this edge-relaxation law. Separate published comparisons cover complete-graph fractional-polytope enclosing spheres, odd-cycle ellipsoids, and windmill symmetric-edge inballs, all different functionals. Accessible related full texts and indexed records revealed no result implying the new theorem. Residual risk: an unindexed volume-limit or graph-packing probability paper could subsume it.

## Mathematical value — PASS

This quantifies a geometric phenomenon that cannot be read from the fixed-block integrality gap alone: a shared single hub changes the dimension-dependent concentration exponent of a uniform polytope point. Even when \(r=2\), so every leaf block has an integral edge relaxation, triangles sharing one vertex generate a growing \(\sqrt m\) volume ratio and a half-normal hub limit rather than the exponential scale of the integral polytope. The complete fixed-\(r\) family gives a sequence of distinct rational condensation exponents and explicit limiting laws. The result identifies a natural systematic gap in the geometry of graph-packing relaxations, not an arbitrary selected small polytope or a finite experiment.

Self-review: passed. Independent audit: not yet performed.
