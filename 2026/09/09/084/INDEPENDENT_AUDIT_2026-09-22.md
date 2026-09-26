# Independent audit — 2026/09/09/084

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS, with numerical-certification scope

The Fourier slice normalization follows by integrating exp(−||x||₄⁴) radially on the four-dimensional section: Γ(2)=1, so the section volume equals (c₀⁵/π)∫₀∞∏ψ(a_j t)dt. The coordinate section is exactly B₄⁴ and has volume c₀⁴=10.799516629… . The two-coordinate section has exact ratio 2^{1/4} to it, giving 12.842862… within I₂. I independently reran the deposited stdlib integration script, reproducing the remaining midpoints 12.939335, 13.080374, 13.152008, 12.325771 and its stated tail/Simpson error ledger. The six reported intervals are disjoint where needed, widths below 0.001, and the diagonal-to-coordinate lower ratio is >1.2177. The rounding allowance is a quantified analytic estimate rather than directed-rounding interval arithmetic; these are certified by the stated derivative/tail majorants and floating allowance, not by a bit-level interval library.

## Originality — PASS

König, arXiv:2409.06432, studies extremal l_p section directions and Fourier methods, but the consulted text does not tabulate these six dimension-five p=4 enclosures. Their explicit bounded numerical profile is a limited new computational datum, without a general extremal theorem.

## Scientific value — PASS

The table gives a concrete comparison for a canonical body and checks direction ordering among six named normals. It does not establish a Mahler rigidity constant or prove the diagonal is globally maximal among all directions.

Sources: https://arxiv.org/pdf/2409.06432 ; https://arxiv.org/abs/2302.04347 . Open primary texts sufficed.
