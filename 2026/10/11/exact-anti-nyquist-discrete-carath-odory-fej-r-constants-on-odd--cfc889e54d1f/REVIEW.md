# Same-model review

## Correctness
**PASS.** The two contact inequalities at \(j=m\) and \(j=m-1\) have positive elimination weights and yield the claimed upper bound exactly. The proposed \(b_m\) makes both contacts zero. Reindexing all samples gives two scalar quadratics; their root signs and monotonicity prove nonnegativity for every grid point. The equality case forces the same two contacts and therefore unique \(b_m\). The packaged finite replay is not used as an infinite proof.

## Originality
**PASS.** The review compared the positive-definite and sampled-cosine formulations, broad singleton sampling results, exact fixed-harmonic tables, and the two primary Carathéodory–Fejér framework papers. The closest general result only detects whether sampling improves the continuous singleton constant; it does not give the anti-Nyquist value or extremizer. Exact fixed-harmonic formulas cover the excluded low diagonal cases \(m=2\) and \(m=3\), not the claimed family \(m\ge4\). A residual risk from older cyclic literature under different notation is recorded in `AUDIT.json`.

## Value
**PASS.** The anti-Nyquist harmonic \(m=(N-1)/2\) is canonical on odd cyclic grids. Closing this entire diagonal gives a natural exact invariant, not a one-off numerical slice, and identifies a simple two-contact mechanism that quantifies the finite-sampling gain with an explicit \(N^-2\) asymptotic.

## Closest literature and limitations
Kolountzakis–Révész (arXiv:math/0302193v1) supplies the archive-era discretized Carathéodory–Fejér framework; Krenedits–Révész (arXiv:1304.0071v1) supplies the broader positive-definite/Fejér–Riesz formulation. Neither inspected source states this diagonal formula. The theorem is limited to real even sampled polynomials on odd grids with anti-Nyquist higher frequency.

Same-model review: passed. Independent audit: not yet performed.
