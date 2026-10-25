# Scientific review: parity-stable rank varieties of square-zero derivations

## Correctness — PASS

Every derivation on the truncated polynomial algebra has form \(D_f=f(t)\partial_t\); in characteristic two, \(D_f^2=0\) is exactly \(ff'=0\) modulo the truncation. Given the least nonzero degree \(v\), square-zero imposes precisely the odd-index coefficient vanishings through degree \(n-v\), whereas \(\operatorname{rank}D_f=\min\{m,\lceil(n-v)/2\rceil\}\). The low-rank and high-rank counts follow from explicit free coordinate charts. These yield the claimed reduced variety isomorphism types and finite-field counts. The independent standalone code exhaustively computed all candidate differentials and actual matrix ranks in 17 small cases across two finite fields; these finite checks support but cannot prove the uniform assertion. The proof covers all characteristic-two fields and all positive \(m\).

## Originality — PASS, with residual literature risk

Avramov–Buchweitz–Iyengar's square-zero differential-module results concern arbitrary module-linear differential matrices, not Leibniz derivations; Premet's regular-derivation work assumes characteristic greater than two; Skryabin's prime-truncated Jacobson–Witt enumeration specializes in one variable and characteristic two to truncation length two, not the full family. A known complete rank spectrum for all derivations does not determine the square-zero subloci. Terminologically similar matrix-algebra work on maps preserving square-zero elements uses a different condition. Searches with square-zero, restricted Witt, rank-stratified and differential formulations did not reveal an implication covering the stated geometric isomorphisms. The uninspected matrix-algebra full text and the possible existence of a wider restricted-Witt scheme classification remain explicit priority risks; neither accessible comparison supplies stronger coverage. Literature-search absence is not proof of absolute novelty.

## Value — PASS

The rank of a square-zero differential controls the dimension of its homology. Determining all reduced rank varieties, rather than isolated cardinalities, produces an invariant family and a sharp half-rank geometric transition. Isomorphic rank strata for lengths \(2m\) and \(2m+1\), whose underlying algebras have different dimensions, represent a motivated parity-stability phenomenon. The classification applies over arbitrary characteristic-two fields and yields complete finite-field distributions.

## Boundaries and verification

All arguments address reduced rank strata. Nothing here establishes smoothness or reducedness of the original scheme-theoretic equation \(D^2=0\), classifies automorphism orbits, or treats other characteristics. The standalone program checks 17 exhaustive small field/length pairs by a computation independent of the valuation formulas. Absolute publication priority and third-party mathematical verification are not claimed.

Self-review: passed. Independent audit: not yet performed.
