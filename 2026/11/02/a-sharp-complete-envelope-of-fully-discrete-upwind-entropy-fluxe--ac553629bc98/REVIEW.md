# Self-review

## Correctness — PASS

For \(N\ge3\), independent choice of the two neighbors yields necessary upper and lower bounds on the shared entropy flux after applying the physical consistency condition. The exact entropy production identity establishes sufficiency for **every** state vector and every cell. The upper and lower endpoints themselves are admissible. At Courant number greater than one they contradict each other for unequal pair states. The polynomial corollary follows from a degree-two divisibility factorization. The comparison interval was derived directly from Section 3.2 of the motivating primary source. A standard-library exact-rational checker passed 12,072 supplementary cases. No infinite theorem is inferred from finite tests.

## Originality — PASS under documented access limits

The motivating source gives a sufficient half-cell interval and does not assert necessary conditions for all consistent two-point entropy fluxes. Substituting the upwind flux and quadratic entropy gives a strict, exactly computable difference between its sufficient range and the complete range obtained here; for \(1/2<\nu\le1\) the sufficient range is empty for nonconstant interface pairs while the complete interval remains nonempty. Other flux-correction theories were inspected for potential stronger coverage. Historical-publishing priority is not certified: classical fully discrete entropy flux theories may use equivalent language, and relevant literature beyond accessible primary material remains a residual risk. Ordinary upwind stability and Jensen's inequality are not claimed as new.

## Mathematical value — PASS

The complete pointwise envelope is a natural classification without smoothness or polynomial assumptions; it is a sharp local feasibility boundary, not a selected benchmark parameter. Its exact distinction from a contemporary projection-based sufficient interval has potential use in understanding stability budgets and Courant restrictions. The result does not establish an alternative high-order DG algorithm or performance improvement.

## Closest literature and limits

The closest direct comparison is Liu, Jiang, and Zhang, arXiv:2610.30535v1, Section 3.2, equations (20)--(23). Other examined relevant sources include Kuzmin, Hajduk and Rupp, arXiv:2107.11283, and Kivva, arXiv:2004.02258. The proof concerns unrestricted real first-order upwind data with the fixed quadratic entropy. It is not a counterexample to the source's sufficient theorem. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
