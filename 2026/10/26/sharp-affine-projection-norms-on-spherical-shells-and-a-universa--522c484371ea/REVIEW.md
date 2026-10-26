# Scientific review: affine projection on concentric spherical shells

## Correctness — PASS

The result fixes integer dimensions at least two, normalized Euclidean shell measure and the finite-rank orthogonal projection onto affine functions. Direct moment integration gives the covariance \(q_d(r)\) and the symmetric reproducing kernel \(1+(x\cdot y)/q_d(r)\). Rotational invariance and convexity locate the sharp kernel absolute row sum at the outer boundary, where a sign-valued test datum establishes equality; kernel symmetry gives the \(L^1\) identity. Slicing the signed cap proves the all-dimensional exact formula. The monotone difference \(r-q_d(r)\) proves a unique contact radius. A local cap expansion proves a positive one-sided term of order \((d+3)/2\) with its stated coefficient and the precise differentiability loss. Direct planar cap integration yields \(2-\sqrt3\). No finite computation is used in place of these proofs.

The provided executable passed 205 cap/quadrature checks in dimensions two through nine and eight high-precision contact-scaling checks in dimensions two through five. These do not constitute exhaustive or independent verification of the infinite family.

## Originality — PASS within inspected evidence

The author-hosted text of Hansen–Atkinson–Chien, doi:10.1093/imanum/drm052, concerns polynomial/hyperinterpolation norms on a filled disk and does not state a moving inner-hole contact theorem. The full available texts of Wade, arXiv:1209.4328, and Li–Xu, arXiv:1310.2283, develop weighted-ball hyperinterpolation and ball spectral approximation, not the sharp concentric-shell \(L^1/L^\infty\) affine norm and its contact singularity. Other research-record comparisons concerned simplexes, radial holomorphic spaces, and finite Fourier projectors; their objects and conclusions do not imply the present contact law. Known full-disk and circular-boundary constants, and the covariance-kernel identity, are explicitly treated as benchmarks/standard tools, not as discoveries. A bibliographic residual risk is an unindexed annulus-specific projector calculation; absence from searches is not a proof of priority.

## Value — PASS

Least-squares affine projection is a basic approximation operator whose sharp \(L^\infty\) and \(L^1\) norms measure worst-case data amplification. A concentric hole is a natural geometric domain perturbation. The new exact formula controls all hole radii in every dimension, while the unique contact and its dimension-dependent nonsmoothness identify where negative kernel regions first encounter the moving domain boundary. The coefficient and differentiability threshold distinguish this statement from a routine kernel calculation or an arbitrary finite example.

## Scope and remaining risks

These are self-review assessments, not third-party validation. Source inspection does not exclude all earlier or unindexed literature. The proof does not cover higher-degree approximation, nonconcentric geometry or globally monotone dependence on the hole radius.

Self-review: passed. Independent audit: not yet performed.
