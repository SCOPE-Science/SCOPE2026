# Self-review

## Correctness — PASS

The bias-to-slope map is explicit and surjective onto the two-dimensional open square. The exact implicit derivatives yield a concave quadratic in the second slope, whose vertex is strictly interior, followed by a strictly increasing one-variable rational function. This proves the unattained triangular supremum without relying on a grid. The one-neuron derivative has exactly one interior zero and vanishes at both endpoints; its limiting coefficient is \(4/27\). The independent-coordinate Hessian factorization gives the determinant identity. All nonstandard derivatives were reconstructed symbolically and checked against independent exact-equilibrium finite differences by `verify.py`. The tests are supplementary, not the basis for the infinite quantifiers.

## Originality — PASS, with historical residual risk

The directly motivating primary source, arXiv:2610.31386v1/v2, gives a general bound, an explicit one-unit witness of coefficient \(1/8\), and a two-copy determinant coefficient \(1/64\); it specifically disclaims sharpness of its constant. Its theorem, proof, numerical sections, and appendices on derivative identities and local envelopes were inspected. The older primary arXiv:2110.03310v3 is a finite-depth explicit ICNN method, with Section 6.3 derivative-product bounds, not the triangular fixed-point optimization. A 2024 implicit differentiation paper and a compositional-curvature paper were checked at abstract/metadata level and their general identities were treated as relevant antecedents rather than novel claims. No covering exact bias-envelope or normalized width contrast was identified in the actual indexed-record and literature searches. The possibility of an older equivalent optimization, especially outside PDE applications, remains.

## Mathematical value — PASS

The contraction-gap exponent alone does not specify the necessary amplitude of a usable curvature or determinant envelope. These complete exact architecture-specific optimizations show a genuine, substantial width effect under fixed normalization: coefficient \(1/4\) versus \(4/27\) and a fourfold determinant comparison. They provide a concrete lower barrier for attempts to sharpen universal PDE evaluation certificates, and prevent a one-neuron extremizer from being mistaken for a sharp width-independent prefactor. The theorem does not claim a globally optimal universal constant or a training/solver guarantee.

## Scientific limitations

Suprema for the coupled architecture require bias parameters approaching infinity; they are not achieved by any finite trained model. The four-unit two-dimensional construction is separable. Third derivatives and globally optimal prefactors over arbitrary width are not classified. Historic priority beyond the inspected sources remains subject to independent checking.

Self-review: passed. Independent audit: not yet performed.
