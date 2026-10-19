# Scientific review

## Correctness — PASS
The claim is the complete positive feasibility spectrum for every alphabet size at least three, together with the strictly finite statement that binary 18 is absent through length 13. The upper bound 20 follows from the published, quantified Sun–Ge theorem, with \(s=t=3\). Explicit witnesses for each of 1–20 have exact two-/three-deletion descendant-set checks; a separate bitset implementation exhausts every unordered binary pair of each length 3–13. Embedding the two- or three-symbol examples into a larger alphabet leaves descendant equality unchanged. No finite experiment is used to exclude all larger binary lengths. The certificate programs are executed from their included paths, and no verification status is inferred from historical logs.

## Originality — PASS, with residual risk
Sun–Ge (2026, arXiv:2606.25822, Theorem 1.1, Definition 1.5 and Section 6) establish the general bound and expressly propose a feasibility conjecture, displaying examples only at deletion orders one and two. The 2024 Zhang–Ge–Zhang work treats the extreme counts 19 and 20, which are credited and not claimed anew. The 2026 Wang–Li–Fu work addresses a different question about extrema, and no known implication from those bounds produces witnesses for all intermediate values. The novel claim centers on explicitly realizing all intermediate values, particularly 18 over three symbols, and the finite binary obstruction through length 13. Searches of equivalent terminology, exact parameters and related records found no dominating characterization. Remaining risks: unpublished or unindexed examples and lack of full inspection of the 2024 conference text; neither has been represented as proof of novelty.

## Value — PASS
The question is explicitly posed as an open feasibility-spectrum problem by the motivating article, and feasible seed values determine whether its run-constrained asymptotic lifting coefficient is achievable. Closing the entire positive spectrum at three deletions for every alphabet of size at least three is a natural classification, not an arbitrary one-off parameter. The binary-versus-ternary distinction at value 18 and the finite length-13 obstruction provide an informative boundary for the unresolved binary case.

## Closest literature and boundaries
The upper bound and endpoint feasibility predate this result. Three-deletion insertion feasibility, binary 18 at length at least 14, and classification of all witness-pair types are not proved. A full-text originality comparison with the 2024 ISIT paper remains incomplete and should be resolved independently before publication claims are treated as final.

Self-review: passed. Independent audit: not yet performed.
