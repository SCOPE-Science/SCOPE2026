# Self-review

## Correctness — PASS

The displayed three-dimensional ellipsoid section formula is derived from a linear image of the unit ball, with the correct plane-area Jacobian. Its coefficient functions are separated exactly by evaluating at three distinct offsets; their span dimension is therefore the minimum number of terms, not merely an upper bound. The parity argument isolates the nonzero odd term, while the Rayleigh quotient distinguishes scalar versus nonscalar quadratic forms. The focal exception follows from the principal semiaxis and focus formula. The nonellipsoid implication uses the explicit published Theorem 4.2 of Fish–Ryabogin–Sun–Yaskin (arXiv:2610.10229) rather than any unsupported experimental extrapolation. Exact-rational coefficient-rank witnesses and direct geometric plane-section computations passed for five models. The main claim is restricted to dimension three, all unit directions and a common near-zero offset interval.

## Originality — PASS with priority risk

A statement comparison with Fish–Ryabogin–Sun–Yaskin, §§1, 3–4, finds its finite-versus-infinite rigidity theorem but no optimal term-count stratification or focus exception. Yaskin–Zawalski's separation classification studies a related origin-symmetric isotropic-volume function; its hypotheses do not cover displaced focal ellipsoids. Agranovsky's centered-ellipsoid formula and algebraic section results supply background formulas, not this minimal-rank classification. Targeted searches using “local separable section rank,” “ellipsoid focal rank two,” and “Radon transform separation rank” did not expose an equivalent published theorem. Lack of an indexed hit is not proof of novelty; older finite-rank literature remains a meaningful priority risk.

## Value — PASS

The rank is the intrinsic minimal number of direction–offset product functions required to encode local section tomography. Completing its finite/infinite classification for all convex spatial bodies refines a recent geometric characterization into a complete quantitative invariant. The exceptional origin-at-focus family exhibits a nonobvious geometry-driven rank drop for noncentered bodies. All four ranks are attained by canonical examples; the classification is not an arbitrarily selected numerical table or a restatement of the finite-rank rigidity theorem.

## Verification limits

The Python checks are finite and do not independently certify the external geometric rigidity result. The proof's geometric-rigidity dependency, historical priority uncertainty, and absence of independent external audit remain explicit.

Self-review: passed. Independent audit: not yet performed.
