# Rigidity of the endpoint fractional-gradient deficit for nested ball towers
## Finding
Let \(N\ge 1\), \(s\in(0,1)\), and \(m\ge 1\). Let \(a_1,\ldots,a_m>0\), and suppose
\[
B_{r_m}(c_m)\subset\cdots\subset B_{r_1}(c_1)\subset\mathbb R^N,
\qquad r_1>\cdots>r_m>0.
\]
Define
\[
u=\sum_{j=1}^m a_j\mathbf 1_{B_{r_j}(c_j)}.
\]
Then
\[
u^*=\sum_{j=1}^m a_j\mathbf 1_{B_{r_j}(0)},
\]
and
\[
\|\nabla^s u\|_{L^1}\le \|\nabla^s u^*\|_{L^1}
=\sum_{j=1}^m a_j\|\nabla^s\mathbf 1_{B_{r_j}}\|_{L^1}.
\]
Writing \(G_j=\nabla^s\mathbf 1_{B_{r_j}(c_j)}\), one has the exact identity
\[
\|\nabla^s u^*\|_{L^1}-\|\nabla^s u\|_{L^1}
=\int_{\mathbb R^N}\left(\sum_{j=1}^m a_j|G_j(x)|-\left|\sum_{j=1}^m a_jG_j(x)\right|\right)\,dx.
\]
The right-hand side vanishes if and only if all centers coincide, \(c_1=\cdots=c_m\), with the assertion vacuous for \(m=1\). Thus every nonconcentric finite nested-ball tower has strictly larger endpoint fractional-gradient energy after symmetric decreasing rearrangement.

## Assumptions and scope
The balls are ordinary Euclidean balls and the coefficients are strictly positive. Only a finite nested chain is considered. The endpoint is \(L^1\), with fractional order \(s\in(0,1)\). No assertion is made here for infinite towers or for \(L^p\) with \(p>1\).

The Riesz fractional gradient is the standard operator
\[
\nabla^s v(x)=c_{N,s}\int_{\mathbb R^N}\frac{(v(y)-v(x))(y-x)}{|y-x|^{N+s+1}}\,dy,
\]
interpreted for the bounded-variation functions used here through its distributional extension. For every ball indicator, the gradient lies in \(L^1\), is nonzero away from the center and boundary, and points radially inward.

## Proof
Because the balls are nested and the coefficients are positive, every superlevel set of \(u\), except at finitely many jump levels, is one of the balls in the chain. Symmetric decreasing rearrangement preserves the measures of these superlevel sets, so the rearranged function is exactly
\[
u^*=\sum_{j=1}^m a_j\mathbf 1_{B_{r_j}(0)}.
\]

For a ball \(B_r(c)\), the known radial formula gives, away from \(\partial B_r(c)\cup\{c\}\),
\[
\nabla^s\mathbf 1_{B_r(c)}(x)
=-\frac{x-c}{|x-c|}\,\big|\nabla^s\mathbf 1_{B_r(c)}(x)\big|,
\]
and the magnitude is strictly positive there. By linearity,
\[
\nabla^s u=\sum_{j=1}^m a_jG_j.
\]
For the concentric rearrangement, all nonzero summands point in the same direction for almost every \(x\). Hence the Euclidean triangle inequality is an equality pointwise almost everywhere, and translation invariance yields
\[
\|\nabla^s u^*\|_{L^1}
=\sum_{j=1}^m a_j\|\nabla^s\mathbf 1_{B_{r_j}}\|_{L^1}.
\]
For arbitrary centers, pointwise triangle inequality and integration give
\[
\|\nabla^s u\|_{L^1}
\le\sum_{j=1}^m a_j\|\nabla^s\mathbf 1_{B_{r_j}}\|_{L^1}.
\]
Subtracting gives the displayed exact nonnegative deficit formula.

It remains to characterize equality. If all centers coincide, all gradients are positively collinear almost everywhere, so equality holds. Conversely, suppose \(c_i\ne c_j\) for some pair. When \(N\ge2\), the vectors \(x-c_i\) and \(x-c_j\) are collinear only on the affine line through \(c_i\) and \(c_j\), a null set; away from that line and the finitely many sphere boundaries and centers, \(G_i(x)\) and \(G_j(x)\) are nonzero and not positively collinear. Strict convexity of the Euclidean norm therefore makes the pointwise triangle inequality strict on a set of positive measure. When \(N=1\), after ordering \(c_i<c_j\), every \(x\in(c_i,c_j)\) outside the finitely many boundaries and centers gives opposite nonzero radial directions for the two gradients, again making the triangle inequality strict on a set of positive measure. Thus equality forces all centers to coincide.

## Verification
The argument uses only finite sums, the exact ball-gradient direction and nonvanishing properties, translation invariance, and the equality criterion in the Euclidean triangle inequality. All exceptional boundaries and centers are null sets. The one-dimensional and higher-dimensional equality cases are treated separately, so no collinearity argument is imported across dimensions.

The source paper states the needed ball facts explicitly and uses them for one translated inner ball inside a larger ball. The proof above independently rechecks the finite-chain rearrangement, the exact deficit identity, and the equality classification for arbitrary positive coefficients and arbitrary finite nested radii.

## Relationship to prior work
Giorgio Stefani's 2026 preprint proves that the Pólya–Szegő inequality for the \(L^p\) norm of the Riesz fractional gradient fails for every \(p\in[1,2)\). Its endpoint mechanism uses the particular function \(\mathbf 1_{B_2}+\mathbf 1_{B_1(e_1)}\), whose rearrangement aligns two ball gradients. The paper records the radial direction, nonvanishing, and integrability properties of fractional gradients of ball indicators.

The present statement converts that two-ball mechanism into a complete finite nested-ball endpoint classification: every positive nested tower satisfies the reverse endpoint inequality, its deficit is exactly the integrated triangle-inequality defect, and equality occurs exactly for a common center. Searches for nested-ball, concentric-equality, finite-tower, and equivalent alignment-defect formulations did not identify a statement covering this classification.

## Limitations
The theorem is confined to finite positive nested-ball step functions and to the \(L^1\) endpoint. The proof does not supply a quantitative lower bound for the deficit in terms of center separation, and it does not classify equality for arbitrary nonnested step functions. It also does not assert persistence of the strict inequality at any fixed \(p>1\) uniformly over all towers.

## References
1. G. Stefani, *Failure of the Pólya–Szegő inequality for the fractional gradient*, arXiv:2609.31233v1, first submitted 25 September 2026.
2. G. E. Comi, D. Spector, G. Stefani, *The fractional variation and the precise representative of \(BV^{\alpha,p}\) functions*, arXiv:2109.15263v5; later published in 2022. The ball-gradient facts used by the focal paper are traced there and in related fractional-variation work.
