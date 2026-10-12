# Self-review

## Correctness
PASS. A diagonal row-column \(\mathbb C^*\)-action with binary-separated weights has exactly the matrix coordinate points as projective fixed points. Every \(r\times r\) permanent is a semi-invariant for this action because all of its monomials have the same total row-plus-column weight.

When \(r\ge2\), every coordinate matrix annihilates every defining permanent. Hence the permanental variety has exactly \(mn\) fixed points. Euler localization applies to singular and reducible complex algebraic varieties, so projectivity gives
\[
\chi_{\mathrm{top}}(P_{m,n}^r)=mn.
\]
Constructible additivity gives the vanishing Euler characteristic of the complement.

The bundled checker independently verifies coordinate-weight separation, semi-invariance, and direct permanent evaluation on a finite grid. Finite computation is regression evidence only.

## Originality
PASS. The archival source defines the same permanental schemes and uses torus fixed points on their Fano schemes, but its stated results concern the geometry of those Fano schemes rather than the global Euler characteristic of the base permanental variety.

A later same-object paper studies codimension, components, and singular loci with a \(\mathbb C^*\)-action and explicitly emphasizes how poorly understood permanental geometry remains. Targeted literature and full-text searches did not locate the all-parameter Euler formula or a stronger Poincaré or motivic statement implying it.

Residual risk remains because the localization argument is short and may be folklore.

## Value
PASS. Permanental varieties are a basic but difficult counterpart of determinantal rank loci and include the permanent hypersurface important in geometric complexity theory. The result gives a uniform global invariant in all dimensions and ranks and shows that every nontrivial permanental rank condition is invisible to ordinary Euler characteristic.

Self-review: passed. Independent audit: not yet performed.
