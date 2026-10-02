# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: **PASS**. On a totally bounded set, a finite \(r/4\)-net of points outside \(B(x,r)\) supplies internal functionals whose values drop by more than \(r/2\) at every such point, so every metric neighborhood contains a relative metric-functional weak neighborhood. This proves equality of the two subspace topologies and the proper-space bounded-convergence corollary. For the locally finite binary \(\mathbb R\)-tree, every pointwise limit of internal functionals is either another internal functional or an end Busemann functional: properness handles bounded subnets and compactness of the end space handles escaping subnets. The explicit rays \(0^{n-1}1\ldots\) with radial length \(2(n-1)+C\) keep exactly one Busemann functional at level \(C\) while all others diverge, yielding precisely the horoball; radial length \(3n\) makes every metric functional diverge and hence gives every point as a d-weak limit.

Originality: **PASS**. The motivating metric-functional topology paper proves the topology/convergence equivalence and gives non-Hausdorff every-point phenomena on a snowflaked real line, while earlier CAT(0) weak-topology work concerns a different projection/Delta notion. No inspected source or earlier published record states the total-boundedness rigidity theorem, exact Busemann-horoball realization, or an every-point sequence in a proper CAT(0) tree. Later published tree refinements postdate this record and therefore do not cover its originality at publication time.

Scientific value: **PASS**. The two theorems identify a sharp geometric mechanism: precompactness suppresses the weak/metric discrepancy, while escape to infinity can create maximal nonuniqueness even in a proper complete CAT(0) tree. Exact horoballs as limit sets provide a reusable model family, not merely a one-off pathology.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
