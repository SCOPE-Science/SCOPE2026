# Mathematical assessment: remote fractional Dirichlet impurities

## Correctness — PASS

The claim concerns \(L^\alpha\) where \(L\) is the *spectral* half-line Dirichlet Jacobi Laplacian, fixed \(k\ge2\), distinct fixed scaled positions, and \(0<\alpha<3/2\). The sine transform yields the precise finite zero-energy Green Gram matrix; the domain condition follows from \(\theta^{2-2\alpha}\) integrability. The dense-range quadratic-form factorization proves the exact largest-eigenvalue threshold for every finite site set. The three asymptotic regimes follow, respectively, from the Riemann–Lebesgue lemma, a \(1/\theta\) cosine-difference calculation, and dominated rescaling. The cosine-integral identity gives the explicitly normalized continuum kernel. Strictly positive off-diagonal Green entries and a two-by-two determinant supply the cooperative-binding criterion. There is no inference from finite experiments to an infinite theorem. The accompanying checker passed 35 targeted finite assertions, including sine quadrature independent of the closed special-function formula, exact classical \(\alpha=1\) cases, leading spectral limits, and a strict fractional cooperative pair.

**Scope risks:** asymptotic equalities do not decide finite-site positivity at an exact critical limiting equality; the finite set of sites must remain separated on the scale \(R\); alternative half-line fractional operators are different objects. The proof uses only standard, explicitly stated spectral and Fourier lemmas.

## Originality — PASS, qualified

The nearest primary work is Gerhat–Krejčiřík–Štampach, *Criticality transition for positive powers of the discrete Laplacian on the half line* (arXiv:2307.09919, 2023). Its spectral Green integral, subcriticality range, and localized criticality methods are prior art. The current claim does not rebrand any of these as new. Inspection of its mathematical statements and proof sections showed no all-\(k\) *moving-site* sharp coupling asymptotic, no exact \(\alpha=1/2\) off-diagonal logarithmic limit for macroscopically separated sites, and no strict two-site cooperative-binding phase surface. The 2025 half-lattice spectral/dynamical analysis addresses interior-energy spectral properties, and the 2026 optimal fractional Hardy-weight work uses a different half-line fractional realization. Full explicit comparison and residual risks are in `AUDIT.json`.

**Priority risks:** standard sine-transform and finite-rank perturbation tools could have been combined elsewhere to obtain an equivalent result under the labels capacity, multi-point Hardy inequality, or point interactions. Search nonmatches do not prove global novelty. The contribution is the full coupled asymptotic phase law, not its constituent techniques or the known one-point special case.

## Mathematical value — PASS

A natural spectral-stability question asks for the *largest allowed attraction* to finitely many local defects as the defects recede from a Dirichlet boundary. Single-defect criticality and nonsharp Hardy bounds do not determine what happens under several defects. The answer gives an exact finite-rank criterion and a sharp large-distance formula for every fixed number and configuration of impurity sites, with an explicit phase transition between asymptotic independence and nonvanishing collective interaction. Most importantly, the strict two-site window shows that jointly bound states can emerge even though each constituent stays spectrally nonbinding, throughout a nontrivial continuous interval of fractional orders. The result is therefore a structural classification of a motivated interaction threshold, not a mere numerical slice or restatement of subcriticality.

## Closest literature and boundaries

The main comparison is arXiv:2307.09919, in particular its Green kernel and Sections 3–4. Relevant context includes Athmouni, arXiv:2510.10680, and Štampach–Waclawek, arXiv:2608.26936; the latter cannot be substituted without changing the fractional boundary realization. The theorem does not address the critical range \(\alpha\ge3/2\), uniform growth of the number of sites, equality at limiting spectral thresholds, nor exact negative eigenvalue energies.

Self-review: passed. Independent audit: not yet performed.
