# Scientific review

## Correctness — PASS

The exact identity for the sketched Ritz perturbation reduces to a cross-Gram block. The sharp bound follows by resolving the norm of this block against its diagonal Rayleigh quotient and maximizing a scalar rational function at \(t=1-\varepsilon^2\). The spectral reality criterion follows by disjoint normal-matrix eigenvalue disks and conjugate-pair counting. An explicit SPD four-by-four block construction attains the perturbation norm, generates exactly \(\beta\pm\sqrt{\delta^2-\gamma^2\varepsilon^2/(1-\varepsilon^2)}\), and is defective at equality. The source verifier passes 1742 deterministic exact and seeded numerical checks; these do not establish the universal quantifiers, which rest on the written proof. No unproved numerical inference is made.

## Originality — PASS under accessible comparisons

Liu--Liu's arXiv:2610.22261 (Sections 3.1 and 5.3) explicitly describes nonreal sketched Ritz pairs, develops real-Schur extraction, and proves a *local selected-characteristic-subspace* theorem; it neither states the attained distortion-to-Ritz-residual norm \(\varepsilon/\sqrt{1-\varepsilon^2}\) nor the all-eigenvalue reality threshold and exceptional-point family. Nakatsukasa--Tropp (2024, Sections 6.3 and 6.8) supplies the sketched extraction method and already observes the nonreal possibility; this is correctly treated as prior knowledge, not a new result. Stewart (2011) supplies general oblique-projection background: intermediate block-norm facts might be classical, but the full text was not inspected. Searches of research records and relevant literature did not surface the **combined sharp numerical eigenproblem criterion**. Unindexed or older equivalents remain possible; no universal historical uniqueness is claimed.

## Mathematical value — PASS

The explicit condition separates sketches guaranteed to preserve entirely real Ritz spectra from configurations where even an arbitrarily small almost-isometry distortion can produce complex pairs when the Ritz gap shrinks. The constant is attained and the boundary is an exact defective-eigenvalue collision. This produces a quantitative, design-relevant decision threshold for when ordinary real symmetric Ritz treatment is safe in the idealized sketch setting, complementing rather than replacing real-Schur remedies. Its motivation is numerical spectral extraction, not a gratuitous matrix example.

## Closest literature and limits

The closest source is the October 2026 sketched eigensolver analysis by Liu and Liu, followed by Nakatsukasa and Tropp (2024). Earlier general oblique-projection and nonsymmetric spectral-perturbation results are important precursors. The theorem assumes sketch embedding of the entire joint space and supplies no probabilistic embedding guarantee, no floating-point analysis, and no global convergence statement for sSI or sTraceMIN. The two-mode example proves sharpness across admissible problems, not instability of every sketch outside the bound.

Self-review: passed. Independent audit: not yet performed.
