# Scientific review

## Correctness — PASS

On the gauge quotient the derivative is the weighted Gram matrix of the optimal plan; strict positivity separates the Perron gauge eigenvalue and rectangular rank-nullity forces genuine zero modes. Differentiating the actual fixed-parameter two-state recurrence gives the stated quadratic modal polynomial. Its Schur inequalities certify local attraction; an affine disk-root test reduces every intermediate eigenvalue to the zero and top endpoints. The low-coupling branch is uniquely optimal by determinant/zero-mode lower bounds; the high-coupling branch is uniquely optimal by the critical-root equation and a strictly negative quadratic evaluation to its right. Analytic comparison with the ordinary Sinkhorn rate and a positive \(2\times4\) realization close the proof. The packaged checker passed 27,178 finite checks, including direct finite-difference differentiation; these tests are not substituted for the proof.

## Originality — PASS (residual bibliographic risk)

The source map and its homotopy objective convergence are Xu and Chen's. The previously available two-atom calculation (`e038ddd6-5b39-4dea-ad43-68455bd41cbc`) already identifies the single-positive-mode critical-damping optimizer and the quarter-eigenvalue slowdown/speedup frontier. Those are **not** claimed as new. The new statement addresses \(n\ge m+2\), where obligatory zero eigenmodes change the optimizer for \(0<L<1/4\), a regime impossible in the prior two-atom model; the proof handles all nongauge modes by a sharp endpoint lemma. Gao et al. analyze classical SK and distinct PAGD/OSMS updates, while the overrelaxation literature treats other recurrences. Searches of available prior claims and published mathematical records did not identify a coverage theorem for this exact rectangular two-state minimax. A semantically equivalent unindexed algorithmic analysis remains a risk; database silence is not proof of originality.

## Mathematical value — PASS

Rectangular transport is common and introduces genuine rank-deficiency in the normalized fixed-point Jacobian. Using the previously sharp single-mode parameter can be provably and substantially suboptimal: with \(L=0.04\), the rectangular optimal factor is approximately \(0.11324\) whereas the two-atom critical-damping parameter gives approximately \(0.17076\). The theorem gives a precise practical spectral tuning rule, identifies the structural reason for the difference, and quantifies its sharp extent for every permitted spectrum through realizable positive plans. This is more than renaming a scalar calculation; both the zero-mode competition and endpoint domination must be established for the full vector iteration.

## Closest literature and limits

Xu–Chen arXiv:2605.30267 (Algorithm 1); Gao–Qu–Ye–Udell arXiv:2608.11760 (Sections 3–4, different algorithms); Lehmann et al. arXiv:2012.12562 (overrelaxation); Thibault et al. arXiv:1711.01851 (overrelaxed projections); and the earlier two-atom result `e038ddd6-5b39-4dea-ad43-68455bd41cbc`. Scope is local fixed-parameter, not global homotopy; defective top modes admit polynomial transients and the historical overlap judgment is conditional on accessible evidence.

Self-review: passed. Independent audit: not yet performed.
