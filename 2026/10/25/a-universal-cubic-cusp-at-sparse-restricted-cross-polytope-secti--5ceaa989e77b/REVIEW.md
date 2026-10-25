# Scientific review: cubic section-volume cusp

## Correctness — PASS

The stated domain is the zero-sum unit sphere of normals to central hyperplanes through a prescribed facet barycenter, with integer dimension \(n\ge3\). The collective direction has unit length and is tangent to that sphere. The Fourier-integral formula is the same normalization as the primary section problem, and its positive constant cancels from the claimed volume ratio.

The proof separates the two nonzero coordinates from the \(n-2\) coordinates activated at order \(|s|\). A uniformly integrable second-order expansion applies to the first two coordinate factors. The quadratic coefficient is established by two exact beta integrals, with ratio ten. For the last \(n-2\) factors, the proof **does not** expand termwise beyond second order: a rescaling of the tail produces a convergent positive integral, which is evaluated exactly through two integrations by parts. The explicit error bound is \(O_n(s^4)\), and the final gamma simplification gives \(C_8=1001/(1024\sqrt3)>0\). An independently evaluated transverse direction has negative second variation. These facts prove the eighth-dimensional saddle and the one-dimensional failure of third differentiability.

The packaged script `artifacts/verify_cusp.py` was executed successfully and returns `VERIFY_OK`. Its exact SymPy calculations verify the moment ratio and eighth-dimensional coefficient; independent direct mpmath quadrature checks the unexpanded integral in several dimensions. The latter finite tests are supplementary, not proof of the asymptotic theorem. The smoothness assertion uses separately justified domination for derivatives through order two.

## Originality — PASS, with stated uncertainty

The primary 2026 paper of Brazitikos–Pandis supplies the relevant restricted-section problem and Fourier formula and conjectures the global maximum. Its complete Section 5 does not compute the third-order volume change at the sparse normal. The closest indexed public result, *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers* (October 2026), proves the two quadratic Hessian eigenvalues \(-3\) and \((n-8)/n\) but explicitly leaves the local type at \(n=8\) undecided. Its theorem cannot imply the sign or size of the cubic term: a zero quadratic coefficient permits both increases and decreases. The present sharp positive \(|s|^3\) coefficient settles that missing local comparison and holds for every fixed dimension \(n\ge3\).

Nayar–Tkocz prove log-concavity under coordinate dilations of a fixed section, not a third-order expansion under changing normals with the zero-sum constraint. Targeted mathematical-record searches for equivalent formulations, higher-order cusp behavior, critical eighth-dimensional saddle behavior, and possible stronger theorems produced the quadratic result as the closest match, not coverage of the new term. Residual risks include unindexed local regularity results, unpublished notes, and possible equivalent integral-asymptotic formulations.

## Value — PASS

The critical dimension \(n=8\) is the precise boundary where the known quadratic Hessian loses negative definiteness. Whether the candidate remains a local maximum there is an intrinsic mathematical question for the proposed section maximizer, not an arbitrary numerical slice. The positive cubic cusp gives the exact missing local classification and quantifies the first non-smooth correction in the canonical collective perturbation for **all** dimensions. It distinguishes quadratic degeneracy from local maximality without asserting or depending on the unresolved global conjecture. This is structural information about a natural geometric optimization problem, rather than a routine parameter substitution.

## Scope and residual risk

The proof is limited to the explicitly described collective geodesic and one transverse direction; it does not supply a full multivariate cubic normal form or classify global maximizers. The remainder is fixed-dimensional. Priority cannot be guaranteed against unindexed work. Independent replication by a separate auditor has not occurred.

Self-review: passed. Independent audit: not yet performed.
