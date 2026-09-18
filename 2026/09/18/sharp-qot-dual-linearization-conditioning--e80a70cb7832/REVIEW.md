# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof combines the sharp \(\ell=\varepsilon^{1/(d+2)}\) support geometry of arXiv:2609.20400 with the support operator of arXiv:2509.08547. The pulled-back optimal density is a doubly stochastic Markov kernel. The local overlap estimate and nonlocal Poincare lemma give its two-step kernel an order-\(\ell^2\) spectral gap, hence its nonconstant singular values are at most \(1-c\ell^2\). On the gauge-fixed perturbation space this yields an order-\(\ell^2\) lower bound for the density-weighted edge energy. Since the density is at most order \(\ell^{-d}\) on its support, the unweighted support quadratic form is at least order \(\ell^{d+2}=\varepsilon\), giving order-one dual curvature. Section-volume control gives the order-\(\ell^{-2}\) upper curvature scale.

The spectral exponents are matched by explicit modes. The common constant perturbation has curvature \(\Theta(\ell^{-2})\). A fixed Lipschitz perturbation paired with its negative pullback through the inverse Brenier map varies by only \(O(\ell)\) across the support and has curvature \(O(1)\). The linearized rate then follows from the standard optimal scalar step for a positive self-adjoint operator. No nonlinear large-step claim is used.

## Originality

The inspected linear-convergence paper arXiv:2509.08547 proves qualitative strict spectral contraction but does not state the small-regularization spectrum or condition-number exponent. The PL paper arXiv:2605.27175 provides quantitative curvature by generic overlap chains but does not state this sharp smooth-marginal conditioning law. The geometry paper arXiv:2609.20400 supplies the ingredients and explicitly suggests sharpening PL and algorithmic analyses, but its inspected results do not state the theorem above.

Searches for QOT combined with Hessian spectrum, spectral gap, conditioning, and the exponent \(2/(d+2)\), together with repository searches by the source identifier and equivalent terminology, found no public equivalent statement. The main residual risk is *Geometry and Convergence of Quadratically Regularized Optimal Transport II*, cited by Part I as a 2026 working paper. It was not available for inspection and could overlap. Originality is therefore assessed only to the best of our knowledge.

## Value

The result turns a qualitative local contraction theorem into a sharp stiffness law: the soft curvature remains order one while the stiff curvature grows as \(\varepsilon^{-2/(d+2)}\). This gives the exact power law for the local spectral condition number and for optimally tuned scalar-step linearized convergence.

## Limitations

The theorem is restricted to the smooth continuous quadratic-cost setting and sufficiently small regularization. It is local to the optimizer linearization and does not justify the larger local step globally. Semi-discrete transport, rough marginals, general costs, discretization, and finite precision are not covered. The unavailable companion working paper leaves nonzero simultaneous-work risk.
