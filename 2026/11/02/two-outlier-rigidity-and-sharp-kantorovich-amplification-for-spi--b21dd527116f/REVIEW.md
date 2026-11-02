# Self-review

## Correctness — PASS

The theorem is a statement about the explicitly defined positive operator \(D_u=A^{-1/2}B_u^{1/2}AB_u^{1/2}A^{-1/2}\) on a real or complex Hilbert space. A direct rank-one similarity factorization reduces the possibly infinite-dimensional problem to the reducing space \(\operatorname{span}\{A^{1/2}u,A^{-1/2}u\}\). The proof computes its two-root trace and determinant and separately handles the one-dimensional reduction when \(u\) is an eigenvector. It checks the strict ordering of spectral outliers and the flat spectral value. Cauchy–Schwarz and the spectral functional calculus establish the exact possible interval for the orientation scalar; approximate endpoint spectral vectors prove sharpness without assuming norm attainment. Equality conditions are derived from both steps of the Kantorovich argument. The supplementary program passed 8,076 finite assertions. Those finite tests have not been used to infer infinite-dimensional results.

## Originality — PASS, subject to stated access risk

Ibrahim–Huang (arXiv:2610.23736v1, 2026), Theorem 4.2, establishes the endpoint's definition, and Theorem 4.3 proves qualitative log-majorization. Their Proposition 4.13 supplies a matrix expression in dimension two for determinant-one inputs, but it does not state the fixed-spike full two-outlier spectral classification for arbitrary dimension, its sharp norm envelope, or the endpoint eigenspace-attainment test in infinite dimensions. Zhu–Peng–Liu (2019) study generic rank-one singular-value inequalities, not this exact positive-operator spectrum. Higham (2020) explains the standard rank-two nature of a rank-one perturbation's singular-value change; this mechanism is acknowledged as background, not claimed new. The standard Kantorovich inequality supplies a scalar input to the proof, not the full theorem. Actual semantic record searches and comparisons with previous mathematical findings revealed no equivalent or dominating combined statement. An earlier article by Franco–Gan–Kim (2025) is a plausible source; its abstract and metadata were inspected, but its full text could not be inspected in full, so it remains a named originality risk rather than a claimed negative check.

## Mathematical value — PASS

Rank-one spiked spectra are a natural testing class for the newly defined near-spectral endpoint. The theorem gives the entire spectral response in every finite dimension and on infinite-dimensional Hilbert spaces: exactly two outliers, fixed product, opposite-direction motion, and the sharp orientation-dependent operator-norm range. It also distinguishes attainable extrema from limiting spectra, a distinction absent from matrix-only formulas. The exact linear growth and reciprocal collapse of extreme eigenvalues as the spectral condition number increases identify a meaningful sensitivity phenomenon. The conclusion is not presented as a novel Kantorovich inequality, a new rank-one SVD lemma, or a theorem for arbitrary positive second inputs. Its value rests on the complete naturally motivated spectral classification and endpoint-attainment boundary.

## Closest literature and limitations

The decisive primary comparison is to Ibrahim–Huang (2026), especially §§4–5, and to the generic singular-value bounds of Zhu–Peng–Liu (2019). The original 2025 near-geometric-mean article could not be inspected in full. The theorem is restricted to a single spectral spike, with strictly positive \(A\) and fixed \(\alpha>\beta>0\). Independent mathematical verification and definitive publication-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
