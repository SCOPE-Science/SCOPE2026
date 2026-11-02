# Review of the affine-projection norm theorem

## Correctness

**PASS.** The normalized affine reproducing kernel is reconstructed from exact diagonal covariance. Symmetric-variable convexity identifies the maximum, and the full support of the independent uniform factors gives a strict maximizer classification. The Irwin–Hall inclusion–exclusion identity and a beta-coordinate marginal yield the finite exact formula; an independent ball-coordinate central limit argument gives the sharp mixed-dimensional asymptotic. The included `verification.py` compared two independent integral representations at 24 parameter pairs, 24 rational instances, and the explicit disk-cylinder value. Finite checks support, but do not replace, the proof.

## Originality

**PASS with stated priority risk.** The closest inspected original paper on cylinder polynomial expansions is Wade (arXiv:0906.2408), but that paper uses a Chebyshev axial weight and a discrete Radon-data reconstruction operator whose bound has a growing polynomial-degree parameter. Li–Xu (arXiv:1310.2283) treats ball polynomial and Sobolev estimates. A published exact simplex affine projector and prior exact cube, cross-polytope, and simplex-product results concern geometrically different bodies. The pure-cube boundary family and classical ball facts are not separately claimed as new. No inspected source proves or implies the mixed ball–cube formula or asymptotic continuum. Some older equivalent formulation under total-degree-one Lebesgue constants could still exist.

## Value

**PASS.** Exact worst-case amplification and the corresponding sharp positivity defect are directly interpretable in uniform-stability estimates for low-order polynomial least squares on disk/cylinder/box product domains. The closed finite-beta evaluation replaces a multidimensional optimization, determines all maximizing locations, gives a symbolic disk-cylinder benchmark, and identifies a sharp continuous geometry-dependent high-dimensional coefficient. These features involve the full infinite family and are not merely a renamed special case of the pure cube or simplex formulas.

## Scientific limits

The norm is for the specified uniform-volume real orthogonal projector, not a minimum over all projectors. There is no higher-degree extension, no claim for arbitrary weights, and no independent validation.

Self-review: passed. Independent audit: not yet performed.
