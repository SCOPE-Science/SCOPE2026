# Self-review

## Correctness — PASS
For every allowed side orientation, four explicit support-line inequalities and a positive linear combination eliminate the rectangle center, giving a sharp bound on the product of its half-edge parameters. The explicit family of rectangles attains it; its fifth-facet slack factors into a nonnegative expression throughout the full closed angle interval. The sine comparison determines the global maximum; positive multipliers, AM–GM equality, and independent normal constraints force uniqueness for each orientation and exactly five global rectangles. All endpoints and scaling are covered. The standalone `verify.py` independently checks the radical identities at high precision over 1,001 orientations and seeded feasible rectangles, but those finite checks are supplementary to the proof.

## Originality — PASS, with limits
Cabello et al. (arXiv:1405.1223, complete arXiv HTML inspected) prove exact algorithmic solvability for arbitrary convex polygons, not this orientation formula or equality classification. A 2017 Math Stack Exchange discussion already anticipates the right geometric candidate and approximate size: both answers explicitly leave symmetry or contact assumptions unproved. Sroysang's 2015 full paper establishes an inverse *covering* assertion for fixed-perimeter rectangles, not this maximization. The indexed 2026 result on regular **even** polygons cannot cover the pentagon; its full text was not retrievable. The present novelty assessment concerns the unconditional proof, every-orientation envelope, and rigidity, **not** the preexisting candidate or its numeric estimate. Equivalent historical derivations remain possible.

## Value — PASS
The all-angle closed formula solves the natural rotating-rectangle optimization in a fixed regular pentagon; the strict angular variation and the classification of every maximizing position add structure beyond evaluating a known candidate. The nonnegative support combination is a clean transferable proof method rather than a mere computer-generated number. This is a deliberately bounded exact result, not a solution for every odd regular polygon.

## Closest literature and scientific limitations
The closest general analysis is Cabello et al. (2014), Theorem 4, and the closest exact-object public discussion is the conditional 2017 pentagon question and answers. The 2015 cover problem and 2026 even-polygon result use related objects but do not entail this exact statement. Priority is not asserted against unlocated literature. There is no independent validation.

Self-review: passed. Independent audit: not yet performed.
