# Scientific review: orientation-dependent ridge distortion in Hybrid LSLU

## Correctness — PASS

The stated first-iterate limit follows from the actual pivoted rectangular Hessenberg stage. In exact arithmetic, the right basis is \(l_1=u/u_g\), the leading Hessenberg entry is \(h_1=(Au)_p/u_g\), and the subdiagonal entry is a nonzero selected coordinate of \(\varepsilon[e_pAu-(Au)_p e]/(\beta u_g)\). The one-dimensional ridge minimizer yields the claimed scalar filter. The orthogonality and nonzero-noise hypotheses establish genuine first-stage nonbreakdown; no iterate at exact breakdown is assumed. Sharp bounds follow from the \(\ell_2\)–\(\ell_\infty\) inequalities and explicit isometries. Equating the two endpoint errors proves the unique minimax calibration. The standalone exact checker independently reconstructs the first step on two nontrivial isometric test families. Scientific risk: no result is asserted for later stages or automatically tuned parameters.

## Originality — PASS, with residual risks

The primary 2024 paper [1] defines the projected regularization and proves a condition-number-dependent residual comparison, not the sharp isometric orientation filter or fixed-parameter minimax obstruction. The related H-CMRH method [2] gives the analogous nonorthogonal-coordinate framework on square systems, and the later sketched LSLU paper [3] studies a different projected/sketched fidelity penalty. The inspected relevant full-text sections do not state the two endpoint extremizers or the minimax formula. Searches of mathematical records for Hybrid LSLU, basis-dependent Tikhonov scaling, isometric one-step filters, and equivalent regularization formulations did not identify an implicating claim. The structural fact that nonorthogonal coordinate norms differ from Euclidean norms is established background and is not attributed to this result. Remaining risks include less-searchable analyses of quasi-minimal-residual ridge filters, equivalent Hessenberg one-step calculations, and unspecified earlier versions of conference material. Failure to find a formula is not proof of publication priority.

## Value — PASS

The parameter in the source's projected ridge objective is meaningful only after accounting for its basis normalization. The sharp range \([1/\sqrt n,\sqrt m]\) quantifies how much parameter interpretation can change **without any conditioning pathology**, and the exact minimax formula shows that no orientation-blind scalar retuning can uniformly match ordinary Euclidean Tikhonov regularization. This is a reproducible limiting benchmark for fixed-parameter comparisons and a useful caution when transferring ridge scales between orthogonal and nonorthogonal projected solvers. The effect is restricted to one stage, known isometries, infinitesimal data noise orthogonal to the forward range, and the original full-pivoted formulation. No practical failure of GCV or other adaptive rules is claimed.

## Closest literature

[1] Brown, Chung, Nagy and Sabaté Landman, arXiv:2409.05239 (2024): Algorithm 4, Algorithm 5, Eq. (28), Theorem 3.1 and Sections 3.2–4.

[2] Brown, Sabaté Landman and Nagy, arXiv:2401.06918 (2024): Section 4 and Theorem 4.1.

[3] Sabaté Landman et al., arXiv:2502.02721 (2025): Sections 3.1–3.3 and the distinct sketched fidelity objective.

Self-review: passed. Independent audit: not yet performed.
