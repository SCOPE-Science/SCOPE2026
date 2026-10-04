# Review

## Correctness

PASS. The upper bound is exact: \(\mathrm{ML}\)-refutability is r.e., so \(\mathrm{ML}\) theoremhood is co-r.e.; \(\mathrm{Skvo}\) theoremhood is r.e., so its complement is co-r.e.; their intersection is co-r.e.

For hardness, a fixed strongly aperiodic Wang tileset \(A\) is used. The coordinatewise product \(W\otimes A\) tiles iff \(W\) tiles because \(A\) tiles, and it cannot tile periodically because every periodic product tiling would project to a periodic \(A\)-tiling. The primary source's two canonical-formula correspondences then give
\[
W\text{ tiles}
\iff
\alpha_{W\otimes A}\in\mathrm{ML}\setminus\mathrm{Skvo}.
\]
The map is computable, so Berger's \(\Pi^0_1\)-complete tiling problem many-one reduces to the separation set.

## Originality

PASS. Almeida–Knudstorp prove proper inclusion by applying their two correspondences to a single aperiodic tileset. They do not state a complexity classification of the whole difference. Pawlowski proves \(\Pi^0_1\)-completeness of \(\mathrm{ML}\) itself, which does not imply hardness after imposing non-membership in \(\mathrm{Skvo}\).

The added ingredient is a uniform aperiodicization: tensor every input tileset with one fixed strongly aperiodic set. Candidate-specific database and literature searches for the difference, co-r.e. completeness, product tiles, and aperiodicization located no equivalent theorem.

## Value

PASS. The primary paper settles both undecidability questions and proper inclusion, making the natural next structural question the size of the gap. The theorem gives the sharp arithmetical-hierarchy answer: recognizing formulas that witness the inclusion is already maximally co-r.e. hard. It strengthens a single-separator existence result to a complete uniform classification of the separation set.

## Closest literature and limitations

Almeida–Knudstorp (2026), especially Theorems 2.16 and 2.19, the tiling equivalences in Sections 4 and 5, and Corollary 5.7, is the direct source. Pawlowski (2026) supplies an independent exact complexity result for \(\mathrm{ML}\), while Jeandel–Rao supplies a concrete fixed strongly aperiodic Wang set.

The reduction is computability-theoretic and does not imply a sharp finite-time or formula-size bound.

Same-model review: passed. Independent audit: not yet performed.
