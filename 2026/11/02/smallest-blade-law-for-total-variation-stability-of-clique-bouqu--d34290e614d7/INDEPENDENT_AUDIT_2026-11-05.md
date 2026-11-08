# Independent mathematical audit

## correctness

PASS

For clique bouquet with m unit-weight blades k_i, hub and K=sum k_i outer vertices, the linear heat generator -L gives directional derivative D of J(f)=sum_edges |f(u)-f(v)|. On a hub-excluding cut with selected blade counts x_i, independently reconstructed D=X(K-2X)-sum_i[(k_i^2+3k_i+1)x_i-(k_i+3)x_i^2]. D-(K-2k_*-1)J is separately convex (quadratic coefficient k_i+K-2k_* >=0), so its box maximum occurs at complete-blade corners, where it equals 2X(k_*-X)<=0. The smallest whole blade gives equality. Level-set coarea decomposition and triangle inequality on zero-difference edges extend D<=mu J to any real signal. Gronwall then yields N(t)<=exp(mu t), initial derivative gives N(t)=1+mu t+O(t^2), and all-time contraction iff K<=2k_*+1. Independently reconstructed literal-edge Laplacians validated 340 integer blade profiles and 41,370 cut derivatives and inequalities. Finite cases corroborate; the coarea/convexity proof supplies universal quantifiers.

## originality

PASS

Graph total-variation denoising and nonlinear TV flow are distinct from linear heat semigroup contractivity in the sum of absolute edge gradients. Ollivier Wasserstein contraction and pointwise gradient estimates provide general tools but do not state the exact integer smallest-blade threshold. The general coarea reduction is classical; the new part is exact optimization across the bouquet family and full classification.

## value

PASS

The discrete diffusion/TV interplay is a natural stability problem; the exact parameter K-2k_*-1 gives a sharp logarithmic norm, an explicit worst-case small blade, and complete all-time contraction classification. The three-blade star and two-blade near-equality tests are mathematically motivated boundaries rather than arbitrary cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
