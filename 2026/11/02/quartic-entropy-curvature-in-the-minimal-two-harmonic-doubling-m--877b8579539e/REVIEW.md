# Scientific review: quartic entropy curvature in the minimal two-harmonic doubling-map deformation

## Correctness — PASS

The precise claim concerns every fixed real \((a,b)\), the analytic small-parameter family \(T_{\varepsilon,a,b}(x)=2x+\varepsilon[u_{a,b}(2x)-2u_{a,b}(x)]\pmod1\), and the unique absolutely continuous invariant measure. Differentiating the transfer-operator invariance identity at doubling gives the Lyapunov Hessian \(-\sigma_D^2(w')/4\). Fourier orthogonality identifies its full two-harmonic kernel. The smooth change of coordinates \(x\mapsto x+\varepsilon u(x)\) eliminates the order-one map perturbation and leaves \(\varepsilon^2u v'\). Applying the Hessian gives the quartic coefficient. The exact Fourier calculation yields \(\sigma_D^2((uv')')=(a^2+b^2)(9a^2+5b^2)/16\). The attached executable symbolic calculation checks this polynomial identity and the kernel, and independent numerical transfer iteration gives compatible limiting values. The proof, not numerical convergence, establishes the infinite asymptotic. The theorem asserts neither a nonlocal parameter bound nor a uniform error over unbounded amplitudes.

## Originality — PASS within inspected evidence

The inspected complete paper of Pollicott–Vytnova (arXiv:2201.04752; DOI:10.1007/s00220-022-04495-7), particularly its Lanford-family example and transfer-operator/pressure theorems, gives rigorous bounds but no minimal two-harmonic Hessian kernel and no explicit quartic response. De la Llave–Shub–Simó (DOI:10.3934/dcdsb.2008.10.597), whose full author-hosted article was inspected, treat single-harmonic expanding maps with an additive rotation parameter and establish averaged versus pointwise entropy comparisons of different form. Galatolo–Pollicott (arXiv:1603.07762), whose complete article's linear-response and doubling-map sections were inspected, determine first-order invariant-density controls and Fourier solutions, not this fourth-order Lyapunov effect. Scientific-index comparisons involving a mean-field linear-response spectral radius and an annealed variance onset treat mathematically different claims, as do the closest accessible historical findings. The general machinery of linear response and conjugacy is credited; the claimed contribution is the explicit null space together with its nonzero anisotropic fourth-order entropy coefficient, not the existence of perturbation theory. Residual risk: mathematical indexing is not exhaustive, and an independently found earlier exact coefficient would change this assessment.

## Value — PASS

The quadratic response is completely degenerate on a **natural, minimal-frequency, two-dimensional tangent space to the conjugacy orbit**, even though the simple linear family is generically not exactly conjugate to doubling at nonzero perturbation. The theorem resolves what the first genuine entropy curvature is along this flat space: order four, always negative, with an explicit anisotropic coefficient and the sharp minimum two-harmonic cutoff. This is a motivated structural benchmark for entropy rigidity and parameter sensitivity, not a scalar substitution or a low-accuracy numerical increment. No downstream theorem beyond this exact self-contained perturbative classification is claimed.

## Limits and closest literature

All sources are identified in RESULT.md. The explicit coefficient is proved only for the specified degree-two expanding family and its two-harmonic tangent directions. The wider smooth infinite-Fourier kernel and finite-amplitude Lyapunov bounds are outside scope. External scientific priority and independent validation have not been certified.

Self-review: passed. Independent audit: not yet performed.
