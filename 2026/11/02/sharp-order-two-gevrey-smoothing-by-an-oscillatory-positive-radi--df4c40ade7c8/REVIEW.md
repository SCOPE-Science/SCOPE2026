# Self-review

## Correctness — PASS

The claim is an exact asymptotic for the coefficients of one fixed positive-weighted disk reproducing-kernel difference, plus a sharp global boundary regularity classification. The proof checks measure normalization, radial orthogonality, moment positivity, the Tricomi integral representation and its imaginary-axis limiting justification, the exact gamma factors, the K-Bessel large-parameter sector, and the phase of \((-i\eta)^{(2\alpha+1)/4}\). The inverse-moment denominator contributes only a strictly smaller exponential term, and Fourier coefficients prove both smoothness and exclusion of all smaller Gevrey orders. The critical nonstandard asymptotic is documented in DLMF 13.8.11, with the relevant fixed complex argument \(-i\eta\). Numerical checks are supplementary and do not certify infinite-degree behavior.

Residual scientific limit: no parameter-uniform statement is proved. The non-Gevrey claim concerns the entire circle, not every local point. The oscillatory cosine can vanish on individual indices, so the sharp asymptotic is an absolute-envelope formula, not a per-index lower bound.

## Originality — PASS, historical priority provisional

The closest focal paper is H. Xiong and H. Xu, *Semiclassical asymptotics for Bergman projections with Gevrey weights* (arXiv:2403.14157; initial March 21, 2024). Its main theorem gives interior local semiclassical Gevrey symbols under strict plurisubharmonicity; it neither assumes a single disk with a boundary-oscillatory positive measure nor states a sharp Gevrey index for an exact fixed-space kernel correction. Hitrik and Stone (arXiv:2105.14402) likewise treat smooth semiclassical exponential weights. Hagger, Liu, Taskinen and Virtanen (arXiv:2011.04699) consider radial oscillatory symbols for Toeplitz operators on a *fixed* space, rather than changing its measure and inverting monomial moments. The DLMF transforms and the Fourier-Gevrey theorem are explicitly used as known mathematical ingredients; novelty is not claimed for those tools.

Targeted searches for exact oscillatory radial Bergman kernel coefficients, their \(e^{-c\sqrt n}\) envelope, and Gevrey regularity found no decisive equivalent statement. This is qualified evidence, not a proof that all literature has been exhausted. An implicit consequence of broader uninspected Fourier-Laplace transform or reproducing-kernel perturbation theorems remains a live historical-priority risk.

## Mathematical value — PASS

Boundary asymptotics of Bergman kernels ordinarily reflect boundary regularity of their weights. Here the weight remains strictly positive but oscillates without limit at the boundary, while the entire *difference* from the classical power-weighted kernel is unexpectedly smooth, and its regularity has a sharp, universal Gevrey threshold. The result makes the cancellation quantitative by giving a fully normalized oscillatory leading constant, including its parameter-dependent phase and an intrinsic proof that smaller Gevrey exponents fail. It is therefore a natural classification of a concrete boundary-regularity mechanism, not merely an arbitrary numerical value.

## Limitations and follow-up

The result does not give full-kernel boundary regularity, parameter-uniform asymptotics, statements for multidimensional domains, or local non-Gevrey failure at each boundary point. Its historical-priority assessment requires independent expert checking, particularly of general saddle-point asymptotics and kernel perturbation literature.

Self-review: passed. Independent audit: not yet performed.
