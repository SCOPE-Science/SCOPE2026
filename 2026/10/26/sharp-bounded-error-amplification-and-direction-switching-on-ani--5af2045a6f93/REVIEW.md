# Review of sharp weighted-rook edge-gradient stability

## Correctness — PASS

The domain is every rectangular rook graph \(K_a\mathbin{\square}K_b\), with \(2\le a\le b\) integers and strictly positive directionwise conductances. The operator is the **Euclidean** orthogonal projector onto energy-normalized edge gradients, with its norm measured in coordinate \(\ell^\infty\). The proof diagonalizes the weighted vertex Laplacian into three nonconstant tensor eigenspaces, obtains its Moore–Penrose inverse, and computes both classes of absolute projection row sums by finite combinatorial counts. The cross-direction entries have support of exactly \(2(b-1)\) or \(2(a-1)\) edges and common magnitude \(\kappa\). Strict arithmetic–geometric mean determines the unique conductance-ratio maximizer, and the quadratic threshold equation determines the two worst-direction switches. Direct exact-rational checks on independently constructed matrices passed 39,265 assertions across 55 configurations. Numerical/finite testing is not treated as a proof of universal claims.

## Originality — PASS within inspected material

The 2008 Jiang–Lim–Yao–Ye paper supplies graph Hodge least-squares projection, and the 2013 Kassel–Wu paper supplies the transfer-current/Green-function correspondence. Their relevant full-text sections do not state the specific weighted Cartesian-product row norms, the unique optimal conductance ratio, or the twice-switching worst output direction. Published mathematical records on cactus transportation spaces and edge Riesz transforms concern different operators or norms. Previously documented exact edge projections for complete multipartite graphs or weighted Boolean cubes do not cover this two-factor complete-graph product in general; the four-cycle is a shared special case, not the full theorem. The literature search was targeted but not exhaustive, and an older equivalent electrical-network or line-graph formula remains possible.

## Value — PASS

Uniformly bounded edge errors under weighted least-squares gradient fitting are measured exactly by the induced maximum-coordinate norm, rather than by the automatic Hilbert norm one. A natural two-direction family exhibits explicit conductance-tuning and two stability transitions; its optimally weighted amplification grows like \(\sqrt{b/2}\) on \(K_2\mathbin{\square}K_b\) while its equal-conductance amplification remains below four. The graph aspect ratio and conductance contrast therefore control a substantive, non-Hilbertian stability phenomenon. This is a complete natural classification, not merely a reparameterization or isolated small example.

## Limitations and residual risk

The result concerns conductance weights constant per edge direction, and its priority has not been independently established. The reviewed full texts give the general framework, not an independent uniqueness guarantee. The standalone checker does not certify infinite families. Arbitrary edge-dependent weights and higher Cartesian products remain outside the claim.

Self-review: passed. Independent audit: not yet performed.
