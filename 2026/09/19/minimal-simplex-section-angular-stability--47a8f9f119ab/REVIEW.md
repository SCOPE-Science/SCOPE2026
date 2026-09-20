# Review — Quantitative stability and exact Hessian for minimal central simplex sections

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The one-positive formula is exact. If the unique positive coordinate is \(s\) and the negative magnitudes are \(b_j=sp_j\), then
\[
f_{sX_1-\sum b_jX_j}(0)
=\frac1s\prod_j(1+p_j)^{-1}.
\]
The zero-sum and unit-norm constraints give \(\sum p_j=1\) and \(s=(1+\sum p_j^2)^{-1/2}\). Dividing by the facet-parallel value produces the displayed factorization into \(\sec\theta\) times an AM-GM factor at least one. The inverse distance estimate follows from the chordal identity \(\|a-a_*\|^2=2(1-\cos\theta)\).

The global sublevel threshold is supported by the recent critical-point classification. On the closure of any sign chamber with at least two positive and two negative coordinates, a minimizer either has a zero coordinate or is an interior constrained local minimum. Zero-coordinate strata reduce exactly to a smaller regular-simplex problem and give the ratios \(B_{n,m}\). An interior local minimum has at most three coordinate values; the three-value case is excluded as a local minimum by Ambrus–Gárgyán, while a two-value point has the explicitly computed gamma-convolution ratio \(R_{n,k}\). Equality in the global minimum theorem excludes value \(1\) in both finite families, so \(\rho_n>1\).

For the Hessian, a tangent vector at the facet normal has first coordinate zero and remaining coordinates summing to zero. Along the great-circle perturbation \(a(t)=a_*\cos t+v\sin t\), differentiating the exact chamber formula gives zero first derivative and second logarithmic derivative
\[
-(n-2)+(n-1)+\frac{n-1}{n}\|v\|^2
=\frac{2n-1}{n}
\]
for unit \(v\). Hence the spherical Hessian is the stated scalar multiple of the metric. The proof is analytic; no numerical computation is required.

## Originality

The primary 2026 source was inspected at its main minimum theorem, probabilistic section formula, critical-point theorem, two-value proposition, three-value non-minimum proposition, and discussion of the earlier literature. It establishes the sharp global minimum and equality cases but does not state a Hessian, an angular stability inequality, or a quantitative near-minimizer theorem.

Dirksen's 2017 paper gives a partial result for the minimum in a restricted sign regime, but the literature located does not state the \(\sec\theta\) deficit, its inverse distance estimate, the finite global sublevel gap, or the spherical Hessian. The newer paper by Myroshnychenko–Tang–Tatarko–Tkocz explicitly concerns stability of Webb's sharp **maximum** section theorem, not stability of the minimum.

Searches using combinations of “minimal central slices”, “regular simplex”, “stability”, “near-minimizer”, “facet-parallel”, “Hessian”, “second variation”, and equivalent section terminology did not locate the three stated refinements. The recent minimum paper contains no occurrences of “Hessian”, “stability”, or “quantitative”. Originality is therefore asserted only to the best of our knowledge. The recency of the sharp-minimum theorem leaves a real residual risk of not-yet-indexed parallel observations.

## Value

The exact minimum theorem identifies the extremizers but does not quantify how section volume grows away from them. The present result supplies three complementary refinements: a closed-form factorization and explicit geometric \(\sec\theta\) barrier on a full sign chamber; an explicit global deficit threshold below which every near-minimizer is forced into one of those chambers; and the complete local quadratic form, which is isotropic with eigenvalue \((2n-1)/n\) for \(\log V\). These statements turn the new qualitative extremal theorem into a usable local and small-deficit stability theory.

## Limitations

The chamber inequality is not claimed outside the one-positive/one-negative sign regime. The global near-minimizer theorem is restricted to deficits below \(\rho_n-1\), and \(\rho_n\) is not claimed optimal. No dimension-free global stability bound for arbitrary deficit is proved, and higher-order terms beyond the Hessian are not classified. The literature check cannot exclude future or presently unindexed work on the very recent minimum theorem.
