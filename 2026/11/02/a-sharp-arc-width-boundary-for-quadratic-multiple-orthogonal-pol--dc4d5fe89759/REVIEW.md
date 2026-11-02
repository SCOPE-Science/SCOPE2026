# Scientific review

## Correctness — PASS

The original non-Laurent multi-index \((1,1)\) requires exactly two zero-moment equations. The two-by-two linear system is nonsingular because \(u>0\) and the two rotations differ. Rotating the resulting polynomial gives a real quadratic, and the elementary strict Schur/Jury inequalities produce the exact root-in-disk criterion \((1+v)u>2|v||\cos(\theta/2)|\). The proof handles equality as exactly one unimodular root, and strict failure as one exterior root. Bounds on the first two cosine moments force the criterion for every even probability measure whenever \(\alpha\le\arccos(1/\sqrt3)\). A symmetric endpoint-pair measure reverses the inequality for every larger admissible half-width; weak smoothing with a positive flat background gives genuinely smooth full-support examples without losing the strict violation. The exact endpoint-pair angular phase boundary and the uniform-density contrast follow algebraically. The accompanying standard-library checker passed **14,215 finite assertions**; those checks do not replace the infinite-family proof.

## Originality — PASS under inspected evidence

Mínguez Ceniceros and Van Assche (2008) introduced the same original orthogonality and exhibited disjoint-arc examples but did not state a lowest-index sharp universal angular-support threshold. Kozhan and Vaktnäs (2026, arXiv:2603.21468v1) prove strict localization for a distinct *Laurent* formulation and explicitly separate the two definitions. Gharakhloo, Kosmakov, and Miyahara (2026, arXiv:2606.27594) give general reduction formulas for original MOPUC and a different high-degree arc-indicator escape regime; their results do not state or directly imply the universal smooth-measure half-width dichotomy. Search queries for quadratic, Schur/Jury, Angelesco, rotated-measure, and sharp-angle formulations returned no matching published result. An inaccessible or unindexed prior specialized theorem is still possible, so the appraisal is not a proof of historical novelty.

## Value — PASS

The question of whether disjoint arc support forces zeros of the original multiple orthogonal polynomial into the disk is naturally motivated by the contrast with the new Laurent disk-localization theorem. The sharp geometric half-width \(\arccos(1/\sqrt3)\) separates universal interior behavior from genuinely smooth full-support escape already at index \((1,1)\). Exact angular phase information and the opposite behavior of uniform arc measures distinguish a structural transition from an isolated counterexample.

## Closest literature and limitations

Primary texts examined: Mínguez Ceniceros–Van Assche, *Multiple Orthogonal Polynomials on the Unit Circle* (2008), Sections 2–3; Kozhan–Vaktnäs, *Zeros of Laurent multiple orthogonal polynomials on the unit circle* (2026), Sections 1–2 and 4–5; Gharakhloo–Kosmakov–Miyahara, *Reduction of Multiple Orthogonal Polynomials to Standard Orthogonal Polynomials* (2026), Sections 3.2 and 6. The claim is restricted to symmetric angular measures and their rotations with separated equal-length covering arcs at the original multi-index \((1,1)\), and makes no higher-degree or general nonsymmetric assertion. The general reduction theorem and unindexed older results remain residual overlap risks.

Self-review: passed. Independent audit: not yet performed.
