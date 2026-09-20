# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Fourier transformation converts the tubal-scalar algebra into the product algebra \(R\cong\mathbb C^p\) and the t-product into independent matrix products. Therefore the t-Krylov module is exactly the product of the ordinary Fourier-slice Krylov spaces. The free-module criterion follows from the primitive frequency idempotents: a free \(R^r\) has complex dimension \(r\) in every component, while equal component dimensions permit bases to be chosen independently and assembled into an \(R\)-basis.

Ordinary matrix Arnoldi has a nonzero orthogonalized residual before its Krylov grade and a zero residual at the grade. Since t-Arnoldi applies these processes simultaneously in Fourier space, the first noninvertible subdiagonal tubal scalar appears exactly at the minimum Fourier grade. It is globally happy precisely when all grades are equal. This matches the older t-Arnoldi definition of breakdown through a zero Fourier coefficient of the subdiagonal tubal scalar.

The proposed continuation is an exact identity. Componentwise pseudoinversion of the residual norm gives \(w_k=q_kh_k\) for nonzero residuals and \(0=0\) on frozen frequencies. Thus \(q^**q\) is the active-frequency idempotent. Frequencywise Arnoldi orthogonality gives the cross relations, and the support masks generate the direct-sum decomposition into ideals \(Rp_j\). Each frequency reaches an invariant cyclic space at its own grade, which proves exact tensor-function recovery at \(\nu_{\max}\) and the Parseval error decomposition.

The explicit \(p=2\) real family was checked algebraically and numerically. The Fourier grades are \((1,m)\), the first residual norms are \((0,1)\), and for \(m=8\) the one-step exponential relative error is approximately \(0.6246333323\). The positive-tolerance family has exact grades \((m,m)\) but first residuals \((\epsilon,1)\); with \(\epsilon=10^{-4}\) and tolerance \(10^{-3}\), the source normalization rule triggers although the second frequency remains inaccurate. The verification artifact reproduces these values and the support-orthogonality identities.

## Originality

**PASS, to the best of our knowledge.** The full 2026 Bouyghf--El Ghomari--El Ichi preprint was inspected. Its normalization algorithm computes every Fourier-vector norm and stops if one falls below tolerance; the Arnoldi algorithm calls this routine after each orthogonalization. Searches within the full text did not locate a discussion of partial/happy breakdown, frequency deflation, or zero-Fourier support continuation.

The full Reichel--Ugwu t-Arnoldi paper was also inspected. It explicitly defines breakdown by noninvertibility of a subdiagonal tubal scalar, assumes the iteration count is chosen to avoid such breakdown, identifies zero Fourier coefficients as the obstruction, and describes the method as simultaneous ordinary Arnoldi on the Fourier frontal slices. These statements are prior art and are not claimed here. The earlier El Ichi--Jbilou--Sadaka tubal-Krylov work and the Kilmer--Braman--Hao--Hoover t-product framework were also checked for the surrounding algebraic context.

Classical block Krylov methods use deflation when block rank drops; in particular, block rational Arnoldi literature treats premature breakdown and deflation. This is an important analogue, but it does not itself state the product-ring/free-module characterization of t-Arnoldi breakdown, the exact minimum/maximum Fourier-grade boundary, or the idempotent-normalized projective continuation presented here.

The originality claim is therefore limited to the combined result: (i) first breakdown equals the minimum Fourier Krylov grade; (ii) unequal grades make the cyclic t-Krylov module non-free; (iii) support-idempotent normalization yields a projective Arnoldi frame that continues to the maximum grade; (iv) tensor-function error decomposes over only unfinished frequencies and becomes exact at the maximum grade; and (v) the current positive-tolerance global stop rule has an open premature-stop family even when all exact grades are equal.

The main residual originality risk is simultaneous or not-yet-indexed follow-up work prompted by the very recent 2026 preprint. No highly relevant inaccessible paper was identified whose title or abstract specifically signals this Fourier-partial-breakdown cure.

## Value

**PASS.** The issue is structural rather than cosmetic. A single finished Fourier slice can stop the ordinary unit-tubal process even when another Fourier slice has an arbitrarily longer Krylov chain. The explicit family makes the ratio \(\nu_{\max}/\nu_{\min}\) unbounded and shows substantial tensor-function error at the first partial breakdown.

The continuation has a simple computational interpretation: freeze only converged frequencies and continue ordinary Arnoldi on the others. It preserves exact Fourier-slice Arnoldi behavior, proves exact termination at the largest grade, and can avoid padded frontal matvecs. It also explains the obstruction algebraically: the target cyclic module is generally projective rather than free over the tubal-scalar product algebra.

The finite-tolerance family is directly relevant to the normalization rule in the recent tensor-function algorithm because its stop condition is triggered by any small Fourier residual. Replacing a global stop with frequency locking separates local convergence from global convergence without changing the underlying matrix Arnoldi steps.

## Limitations

The principal theorem is exact-arithmetic. The finite-tolerance example establishes premature termination of a global threshold rule but does not supply a backward-stable locking threshold, roundoff analysis, or certified tensor-function error estimator. The support-deflated frame is not unit-tubal orthonormal; software and formulas that assume \(V^**V=I\) require a frequency-ragged or projective adaptation.

The module theorem is stated over complex tubal scalars. Real inputs impose conjugate symmetry on Fourier slices and masks, although the displayed two-frequency counterexample is entirely real. The result treats a lateral-vector t-tubal Arnoldi process, not block or tubal-global variants. The tensor-function exactness conclusion assumes the primary matrix function is defined on every relevant spectrum.

## Sources inspected

- Bouyghf, El Ghomari, and El Ichi, arXiv:2609.11369v1, full paper including the normalization and tubal-Arnoldi algorithms and tensor-function approximation sections.
- Reichel and Ugwu, arXiv:2110.04796, full paper including normalization, the t-Arnoldi algorithm, its explicit breakdown definition, and the Fourier-slice interpretation.
- El Ichi, Jbilou, and Sadaka, *On tensor tubal-Krylov subspace methods*, article metadata/abstract and accessible preprint material.
- Kilmer, Braman, Hao, and Hoover, SIAM J. Matrix Anal. Appl. 34 (2013), for t-product/t-linear algebra background.
- Elsworth and Guettel, SIAM J. Matrix Anal. Appl. 41 (2020), for the classical block-rational Arnoldi deflation analogue.

No source was used to claim that pseudoinversion itself is new; Moore--Penrose inversion and frequencywise t-product algebra are standard ingredients. The novelty assessment concerns their specific support-idempotent use to resolve partial tubal-Arnoldi breakdown and the resulting grade/module theorems.
