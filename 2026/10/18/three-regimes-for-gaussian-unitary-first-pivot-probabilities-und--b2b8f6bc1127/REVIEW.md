# Review of the Gaussian-unitary norm-indexed pivot theorem

## Correctness — PASS
The proof reduces the exact first-column comparison to one half-normal variable and independent planar Gaussian norms. The angular tail formula is exact. Below the Euclidean exponent its four diagonal saddles have curvature \(2-q\); above that exponent the four axial saddles have curvature one, including the maximum norm; at the Euclidean exponent the whole angle is flat. The half-normal Mills ratio and a regular-variation Abelian limit provide both logarithmic powers and the displayed constants. The exact \(\ell^1\) identity and \(\ell^2\) endpoint reproduce earlier published values. The accompanying numerical checker passes 28 assertions; the proof does not infer an infinite limit from computation.

## Originality — PASS (qualified)
The 2025 GUE norm-effects article was examined for its complete two-dimensional comparison and proposed extensions. The 2026 *Random permutations using GEPP* full-text Sections 1, 4.1 and 5, including Proposition 6 and its proof, explicitly treat \(\ell^1\) and \(\ell^2\), not every \(\ell^q\) or the universal sharp constant for all \(q>2\). Queries for GUE first-pivot probabilities, generalized planar Gaussian norms, angular-saddle phase transitions, and equivalent extreme-value formulations found no direct published statement of the full theorem. Related work on pivot-error bounds studies different matrix and error objects. The saddle and Abelian methods themselves are not claimed as novel. An older Gaussian-tail theorem might imply part of the result when specialized; this is the main residual originality risk.

## Mathematical value — PASS
The norm used for a complex pivot is an actual numerical-algorithm design parameter, not an arbitrary substitute variable. The theorem gives a complete first-pivot asymptotic classification with leading constants and identifies a nonuniform, three-regime transition that is invisible from either known endpoint separately. The entire super-Euclidean range has one leading law, whereas the sub-Euclidean range has a continuum of decay exponents. This directly quantifies the probability of avoiding an initial row interchange under different comparison norms.

## Boundaries
All asymptotics fix \(q\) before sending the dimension to infinity. They concern the first pivot of dense GUE, not later pivots, floating-point stability or the full permutation. Earlier asymptotic machinery could contain abstract ingredients, and the result has not received independent validation.

Self-review: passed. Independent audit: not yet performed.
