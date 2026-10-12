# Scientific review: sharp true-residual frontier for one-step SPD sketched GMRES

## Correctness — PASS

The matrix-embedding hypothesis is explicitly restricted to \(\operatorname{span}\{r,Ar\}\), and positivity of the Gram matrix makes the scalar sketched minimizer unique. Its actual true-residual norm equals the unsketched GMRES angle sine times an oblique projection penalty. Maximizing the penalty over symmetric \(2\times2\) Gram matrices with spectrum in \([1-\varepsilon,1+\varepsilon]\) gives exactly \((1-\varepsilon^2)^{-1/2}\). The elementary eigenvalue-weight proof of the Kantorovich inequality gives the sharp SPD sine \((\kappa-1)/(\kappa+1)\). One two-mode construction attains both maxima simultaneously. The exact rational examples verify threshold equality and strict overshoot. The independent source-code checks are supplementary and do not substitute for the inequalities.

## Originality — PASS, with residual risk

Bucci–Durastante [1, Section 2] explicitly describe sketched GMRES and possible true-residual nonmonotonicity, but their central claim is a sketched-AA equivalence. Burke–Güttel–Soodhalter [2, Section 3] have a strictly weaker generic embedding quasi-optimality factor; it does not imply this exact SPD one-step factor or its sharp nonexpansion threshold. Epperly–Webber [3, Section 2] address expected sketched-regression error, not this deterministic one-step envelope. Burke–Carson–Ma [4] and Jang–Grigori [5] study numerical stability and orthogonalization. Existing sharp unsketched GMRES(1) bounds and classical oblique-projection geometry are credited rather than presented as original. Residual risk: an unindexed classical projector-angle inequality may contain the abstract norm-distortion lemma, although no inspected source explicitly covers the combined SPD safety frontier.

## Value — PASS

The gap is directly motivated by the sketched-GMRES literature's distinction between true and sketched residual monotonicity. A necessary-and-sufficient tolerance \(\varepsilon\le2\sqrt\kappa/(\kappa+1)\), rather than merely a sufficient generic distortion estimate, is useful when deciding whether a sketch can be trusted to preserve one-step true-residual descent. The proof provides dimension-two equality and strict-growth examples, with a finite-precision and multi-step limitation. The condition-number/embedding interaction is more informative than a small isolated numerical example.

## Literature and limitations

Scientific sources: [1] https://arxiv.org/html/2607.04904v1; [2] https://arxiv.org/html/2311.14206v2; [3] https://arxiv.org/html/2605.19096v2; [4] https://arxiv.org/html/2503.19086v3; [5] https://doi.org/10.1002/nla.70029. This is not a claim of independent audit or exhaustive uniqueness. The finding does not cover general nonsymmetric matrices or later iterations.

Self-review: passed. Independent audit: not yet performed.
