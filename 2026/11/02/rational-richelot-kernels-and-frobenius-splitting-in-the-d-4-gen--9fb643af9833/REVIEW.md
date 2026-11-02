# Scientific review

## Correctness: PASS

The base curve is smooth exactly under the stated restrictions. Four independent proof steps are checked: the reciprocal quartic roots all lie in the quadratic extension by a norm-one argument, the four-to-one parameter map yields the closed frequencies, Frobenius-invariant even subsets modulo complements give the rational two-torsion orders, and Galois-stable perfect matchings give the Richelot kernel counts. A subtle case is the three-transposition action: there is no anti-invariant even subset, although seven matchings are invariant. The included finite-field checker independently enumerates roots, Frobenius permutations, sixteen two-torsion classes and fifteen matchings for every allowed parameter over ten distinct odd prime fields. Finite checks corroborate but do not establish the extension-uniform assertion; the general proof does.

## Originality: PASS, qualified by priority risk

Arul et al., arXiv:2102.11419, equations (2.1), (3.1) and (3.2), provide the exact genus-two family and the rational-Weierstrass parametrization; Section 3 assumes all six Weierstrass points rational, while the present result stratifies every nonsingular parameter, including all nonsplit cases. Bruin--Doerksen, arXiv:0902.3480, Section 4 and Proposition 4.3, develop the general Galois-stable Richelot matching theory. That general theory is explicitly prior work, not a new claim. In neither inspected manuscript passage did a complete closed arithmetic count of \(K\)-rational kernels for this pencil, including the seven-kernel \(2^3\) stratum, appear. Searches for the exact family, Frobenius matching distributions, alternate quadratic-splitting terminology, general isogeny classifications and the named authors found no exact statement implying these four parameter-frequency formulas. Negative search results are not priority certificates; equivalent analyses in unindexed special-family/isogeny-graph literature remain a genuine residual risk. A 2026 general Richelot factorization census was seen only at abstract level and is not represented as fully read.

## Mathematical value: PASS

The number of rational maximal isotropic \(J[2]\)-subgroup schemes is the natural local valency of the rational Richelot isogeny correspondence. Its exact joint distribution with the Frobenius branch type is useful even without a distinct-target classification. The striking distinction between the \(1^2 2^2\) and \(2^3\) strata -- both have rational two-torsion of size four but have respectively three and seven rational maximal isotropic kernels -- is not apparent from the rational torsion order. The result classifies every smooth parameter in the canonical one-dimensional \(D_4\) family for every odd finite field, rather than an arbitrary small-field example. Its scope is well delimited, and the computation is not the sole correctness support.

## Closest literature and limits

1. Arul--Booher--Groen--Howe--Li--Matei--Pries--Springer, *Doubly isogenous genus-2 curves with \(D_4\)-action*, arXiv:2102.11419, equation (2.1), Section 3 and Section 5. These establish the model, a split-branch parametrization, and applications to covers/isogenies, not the stated four-row Richelot-kernel census in the inspected passages.
2. Bruin--Doerksen, *The arithmetic of genus two curves with (4,4)-split Jacobians*, arXiv:0902.3480, Section 4; general Galois-invariant quadratic splitting and Richelot descent, but no found coefficient-specific four-row census.
3. Magma Handbook, “Richelot Isogenies,” provides the classical maximal-isotropic-kernel description.

Parameters \((c,s)\) may represent isomorphic curves, and distinct kernels can share targets. No count of distinct codomains or assurance that every target is a smooth genus-two Jacobian is given. Generalization beyond odd characteristic is excluded. The checker tests prime fields, not every finite extension. Priority risk persists; no independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
