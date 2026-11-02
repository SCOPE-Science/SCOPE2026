# Scientific review

## Correctness — PASS

The exact statement and proof use the normalized Fourier convention \(h_k=(2\pi)^{-1}\int h(\theta)e^{-ik\theta}d\theta\) and the Poisson multiplier \(r^{|n|}\). Taylor expansion through second order is uniform in two circle derivatives at fixed radius because the Poisson operator smooths the real \(C^3\) trace. The first and second arclength derivatives reduce respectively to a vanishing mean and to the Parseval difference \((\|h\|_2^2-\|D_rh\|_2^2)/2\), with \(D_r\) the real Fourier diagonal operator. Constant \(h\) cancels, as required by exact rotation invariance.

The proof explicitly establishes the strict frequency ordering \(|d_k(r)|<r\) for all \(k\ge3\), including the \(k=3\) boundary computation, and compares the only two surviving candidates \(d_1=r\) and \(d_2=(3r^2-1)/2\). This gives an all-mode theorem rather than an inference from finite tests. The perturbation stays an embedded strictly convex Jordan curve for each fixed radius and smooth \(h\), justifying replacement of convex-hull perimeter by curve length. The checker completed 762 supplementary assertions, including finite direct quadratures; its finite tests are not the proof of the infinite claim.

## Originality — PASS on available evidence

Zhong–Kalaj, *Sharp mean-width and Jacobian bounds for Euclidean and hyperbolic harmonic maps*, arXiv:2609.09316 (first public September 8, 2026), Theorem 1.4, Corollary 1.5 and Theorem 1.8, prove a sharp **global** planar perimeter inequality and one-radius rigidity. The full relevant source sections on Poisson applications, planar perimeter, and rigidity do not give the quadratic form, frequency multipliers, exact sharp local gap, or the \(r=1/3\) change of extremal directions. Those conclusions require new second-variation and spectral calculations and are not logical consequences of global nonnegativity and rigidity alone.

Koh–Kovalev (arXiv:0911.0623) prove an **area**-contraction result for harmonic disk automorphisms; Geleta (arXiv:2601.14717) addresses Lebesgue **area** of images. Their conclusions do not calculate the perimeter Hessian. Relevant published research results on Gaussian torsion and Bergman-pole angular Hessians concern different geometric functionals. An implicit equivalent calculation in older convex-geometric or harmonic-variation literature remains a genuine, bounded residual originality risk.

## Value — PASS

The new quadratic stability profile quantitatively refines a sharp global perimeter inequality in the natural class of boundary circle rearrangements. The frequency competition is structurally informative: the most weakly controlled direction switches **exactly** from boundary mode two to mode one as the interior observation radius passes \(1/3\), despite the unchanged global circle-extremizer rigidity. All Hessian eigenvalues and equality cases are explicit, rather than a generic local convexity statement or a routine bound. It supplies a usable local sharp constant for future stability investigations, with no claim of a uniform nonlinear stability theorem.

## Scope and remaining risks

The proof holds at each fixed \(0<r<1\) for a fixed real smooth boundary perturbation; the error term may deteriorate with frequency or as the radius approaches an endpoint. The comparison with earlier unindexed literature cannot establish absolute uniqueness, and independent mathematical checking has not been performed.

Self-review: passed. Independent audit: not yet performed.
