# Scientific review

**Correctness — PASS.** The proof identifies the exact endpoint Gram-inverse row for every integer number of cells, reduces monotone inputs to step functions, and exhausts all boundary and critical points of the step response. Later cells are excluded by explicit alternating-difference bounds; the one- and two-cell exceptions are evaluated separately. The rational recurrence proves strict convergence of the optimal boundary defect to the algebraic limit. The standalone exact-rational checker enumerated all candidates for 120 finite cell counts and passed; enumeration is a check, not the infinite argument.

**Originality — PASS, with documented access risk.** Accessible primary texts on spline-projection stability establish unrestricted operator norms and periodic Franklin Lebesgue constants, not the optimal monotone-input endpoint range. The unrestricted uniform bound \(2\) implies only a weaker interval \([-1/2,3/2]\) for generic inputs in \([0,1]\), whereas the present sharp limit is \((\sqrt3-1)/2<1/2\). Previously recorded one-knot projector results give unrestricted bounds, not a monotone all-grid sequence. The related Oswald 2013 chapter remained inaccessible in full; abstract-level evidence indicates a different emphasis but cannot exclude implicit overlap. Unindexed equal statements remain possible.

**Value — PASS.** Boundary range excursions of least-squares spline projections are mathematically natural stability invariants for ordered measurements and finite-element approximation. The theorem gives a complete sharp all-grid endpoint law, explicit minimizing step locations, and an unattained universal limit, distinguishing shape-constrained risk from generic \(L^\infty\) amplification. It neither relies on nor asserts broader global shape preservation.

**Closest literature.** Oswald, arXiv:math/0611573v1, gives the one-dimensional unrestricted bound and a higher-dimensional counterexample. Passenbrunner, arXiv:1103.1950v1, treats periodic Franklin projections and quotes the unrestricted sharp uniform-mesh constant. Oswald (2013), DOI 10.1007/978-1-4614-4565-4_24, was abstract-only.

**Limits and risks.** Full text of Oswald (2013) was not obtained. Interior values and nonuniform partitions were not treated. These caveats do not weaken the universal quantifiers of the stated endpoint theorem.

Self-review: passed. Independent audit: not yet performed.
