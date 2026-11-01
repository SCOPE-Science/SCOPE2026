# Review of the sharp two-cap Godbersen allocation theorem

## Correctness

**PASS (self-review).** The exact two-parameter formula is reconstructed from the mixed-area formula, three coordinate facets, their areas, and the volume of two disjoint tetrahedral caps. The factorization of \(\rho-5/3\) proves the full edge-contact plateau and its iff equality condition. Fixing \(c=s^3+t^3\) reduces optimization to the sum \(u=s+t\); the derivative bound is strictly negative throughout the feasible interval. The endpoint constraints yield exactly the sharp piecewise lower profile and one-cut upper profile, including the quarter-volume transition. Eleven independent rational difference-body volume reconstructions and 66 exact grid identity checks passed. Residual mathematical risk: the analytic proof, not a machine-verified theorem prover, bears the universal conclusion; the finite tests do not establish all real cases.

## Originality

**PASS (best-knowledge self-review).** The 2026 Godbersen equality papers prove \(\rho\leq3\), and do not give this two-cap fixed-volume sharp profile. Sadovsky's anti-blocking coordinate-projection formula is acknowledged: it provides an established general technique for the first algebraic evaluation and is not claimed as new. The new proposed contribution is the sharp two-cut redistribution law, the exact \(c=1/4\) change of optimizer, the persistent \(5/3\) edge-contact plateau, and equality cases. Published one-corner and all-corner special-family calculations do not state this fixed-two-corner optimization. Textual/semantic searches did not identify an equivalent result, but priority is provisional: a classical volume-constrained cap-redistribution theorem could still cover the result implicitly.

## Mathematical value

**PASS.** The Godbersen inequality identifies the simplex equality case but not the quantitative distance of natural truncation families from it. Removing the same fraction of a tetrahedron's volume by one or two corner cuts is a geometrically natural perturbation comparison. The finding gives the *entire* sharp feasible range for the normalized mixed volume at each prescribed removed fraction, with a genuine geometry-driven threshold where the cap boundaries meet and a nonobvious constant plateau. It is an exact complete natural family optimization, not a new proof of the known general inequality or an arbitrary numerical example. The method may serve as a benchmark for quantitative stability questions; no downstream theorem is claimed.

## Closest prior work and scope

Relevant primary texts were examined in their online full-text forms: Fryš–Kotrbatý–Mouamine–Wang (arXiv:2610.06806v2), Friedland–Putterman–Szusterman (arXiv:2610.04527v2), Sadovsky (arXiv:2312.03473v3), and Kotrbatý (arXiv:2502.02149). The first two prove universal sharp Godbersen bounds and equality; Sadovsky provides the anti-blocking projection formula on which the finite family computation can be based. The present theorem's restricted two-corner, disjoint-cap scope is essential. An alternative pre-existing corollary within the anti-blocking literature remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
