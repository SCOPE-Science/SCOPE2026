# Square-minimal convex order for radial boundary distances of fixed-perimeter parallelograms

## Finding

Let \(Q\subset\mathbb R^2\) be a nondegenerate Euclidean parallelogram centered at the origin, with Euclidean perimeter \(L>0\). Let \(X_Q\) be uniformly distributed with respect to arclength along \(\partial Q\), and let \(S_L\) be any origin-centered square of the same perimeter, with \(X_{S_L}\) sampled by arclength. Then the squared radii obey the **convex-order comparison**
\[
|X_{S_L}|^2\le_{\mathrm{cx}}|X_Q|^2.
\]
Precisely, for every continuous convex function \(f:[0,\infty)\to\mathbb R\),
\[
\frac1L\int_{\partial S_L} f(|x|^2)\,ds\ \le\ \frac1L\int_{\partial Q} f(|x|^2)\,ds,
\qquad
\mathbb E|X_{S_L}|^2=\mathbb E|X_Q|^2=\frac{L^2}{48}.
\]
For every \(C^1\) strictly convex \(f\), equality holds if and only if \(Q\) is a Euclidean square. The order is reversed for concave \(f\), with the corresponding strictness for strictly concave \(C^1\) functions.

For every real \(p\), the weighted perimeter \(E_p(Q)=\int_{\partial Q}|x|^p\,ds\) is finite. At fixed \(L\), the square uniquely **minimizes** \(E_p\) for \(p<0\) or \(p>2\), and uniquely **maximizes** \(E_p\) for \(0<p<2\). The cases \(p=0\) and \(p=2\) are shape-independent. The quadratic case and the fact that every centrally symmetric parallelogram attains its value were already known; the claim here is the universal convex-order refinement, the strict transition outside those cases, and the smooth-weight rigidity.

Writing \(A=\operatorname{area}(Q)\), the following already-implicit polynomial moment identity illustrates the strength of the new convex-order statement:
\[
E_4(Q)=\frac{L^5}{1280}-\frac{L A^2}{12},\qquad
E_4(Q)-E_4(S_L)=\frac{L}{12}\left(\frac{L^4}{256}-A^2\right)\ge0.
\]
The deficit vanishes only at squares. The fourth-moment identity is already derivable from the one-point moment formula in the published fourth-chord calculation, and is not offered as new by itself. Finally, if \(f\in C^2([0,\infty))\), the integral \(\int_{\partial Q}f(|x|^2)\,ds\) depends **only** on \(L\), for every nondegenerate centered parallelogram \(Q\), if and only if \(f(t)=\alpha+\beta t\) for constants \(\alpha,\beta\in\mathbb R\).

## Assumptions and scope

Represent each parallelogram uniquely up to interchange and signs of generators by
\[
Q(u,v)=\{s u+t v:-1\le s,t\le1\},\quad u,v\in\mathbb R^2,
\quad a=|u|>0,\ b=|v|>0,\ c=\langle u,v\rangle,\ |c|<ab.
\]
Its perimeter is \(L=4(a+b)\), area is \(A=4\sqrt{a^2b^2-c^2}\), and all its boundary points have positive distance from the origin. The associated reference square has perpendicular generators of common length \((a+b)/2\). Convex order means equal means and comparison of expectations against **all** continuous convex test functions, not first-order stochastic dominance. The weight-rigidity assertion assumes the invariance for every positive perimeter and every nondegenerate parallelogram; it is not a claim about a single fixed perimeter.

## Proof

**1. Exact edge formula and suppression of skew.** Four edges parallel to the generators yield, for every continuous test function \(f\),
\[
I_f(Q):=\int_{\partial Q}f(|x|^2)\,ds
=2b\int_{-1}^1 f(a^2+b^2t^2+2ct)\,dt
+2a\int_{-1}^1 f(b^2+a^2t^2+2ct)\,dt.
\]
For convex \(f\), pairing the parameters \(t\) and \(-t\) and applying Jensen gives
\[
 f(z+2ct)+f(z-2ct)\ge 2f(z).
\]
Consequently \(I_f(Q)\ge I_f(R_{a,b})\), where \(R_{a,b}\) is the rectangle with generator lengths \(a,b\). For strictly convex \(f\), the comparison is strict whenever \(c\ne0\).

**2. Balancing the side lengths.** For the rectangle, write
\[
G_f(a,b):=I_f(R_{a,b})
=4\int_0^a f(x^2+b^2)\,dx+4\int_0^b f(y^2+a^2)\,dy.
\]
For \(C^1\) convex \(f\), fix \(s=a+b\), assume \(a\ge b\), and differentiate the function \(b\mapsto G_f(s-b,b)\). An exact cancellation of the moving-endpoint terms gives
\[
\frac{d}{db}G_f(s-b,b)
=8ab\int_0^1\left[f'(a^2t^2+b^2)-f'(b^2t^2+a^2)\right]\,dt\le0,
\]
since \((a^2-b^2)(1-t^2)\ge0\) and the derivative of a convex function is nondecreasing. Thus balancing the lengths decreases every convex squared-radius boundary moment. For strictly convex differentiable \(f\), this derivative is strictly negative when \(a>b\), because the two arguments are strictly ordered for \(0\le t<1\). Hence
\[
I_f(Q)\ge G_f(a,b)\ge G_f(s/2,s/2)=I_f(S_L),
\]
with equality only for squares when \(f\) is strictly convex.

For general continuous convex \(f\), smooth convex approximations converge uniformly on the compact interval containing the squared radii of both bodies. Passing to the limit proves the inequality. Taking \(-f\) gives the concave comparison. For \(f(t)=t\), the edge formula evaluates to \(I_f(Q)=\frac43(a+b)^3=L^3/48\); dividing by \(L\) yields the common squared-radius mean. This establishes the convex order.

**3. Power weights.** Apply the comparison to \(f(t)=t^{p/2}\). It is strictly convex on the positive axis when \(p<0\) or \(p>2\) and strictly concave when \(0<p<2\); each boundary stays away from the origin. The cases \(p=0,2\) are constant/affine. Therefore the stated global extremum and uniqueness classification follows without differentiating in \(p\).

**4. Exact quartic deficit.** Direct integration of the edge formula for \(f(t)=t^2\) gives
\[
I_{t^2}(Q)=\frac45(a+b)^5-\frac{16}{3}(a+b)(a^2b^2-c^2)
=\frac{L^5}{1280}-\frac{L A^2}{12}.
\]
Since \(A=4\sqrt{a^2b^2-c^2}\le4ab\le(a+b)^2=L^2/16\), with equality only for a square, subtracting the square value gives the displayed nonnegative exact deficit. In probabilistic normalization,
\[
\operatorname{Var}(|X_Q|^2)=\frac{4(a+b)^4}{45}-\frac{A^2}{12},
\qquad
\operatorname{Var}(|X_Q|^2)-\operatorname{Var}(|X_{S_L}|^2)
=\frac{(a+b)^4-A^2}{12}.
\]
Thus the fourth-moment deficit quantifies the area defect *exactly*, not just asymptotically.

**5. Rigidity of shape-independent radial weights.** The affine functions \(f(t)=\alpha+\beta t\) plainly give \(I_f(Q)=\alpha L+\beta L^3/48\), independent of shape. Conversely suppose \(f\in C^2([0,\infty))\) and \(I_f(Q)\) is shape-independent at each perimeter. With fixed \(a,b>0\), vary the inner product \(c\in(-ab,ab)\). The edge formula is twice differentiable in \(c\), and vanishing of its second derivative at \(c=0\) implies
\[
0=8b\int_{-1}^1t^2 f''(a^2+b^2t^2)\,dt
+8a\int_{-1}^1t^2 f''(b^2+a^2t^2)\,dt.
\]
Fix \(a\) and send \(b\downarrow0\), obtaining \(\int_{-1}^1 t^2 f''(a^2t^2)\,dt=0\) for every \(a>0\). Equivalently \(\int_0^a z^2 f''(z^2)\,dz=0\) for every \(a>0\). Differentiating with respect to \(a\) gives \(a^2f''(a^2)=0\); continuity at zero forces \(f''\equiv0\) on \([0,\infty)\). This proves the stated necessity and sufficiency.

## Verification

The companion standalone Python program `verify_parallelogram.py` uses `fractions.Fraction` arithmetic to integrate the exact squared-radius polynomial along all four edges, with nondegenerate rational directions parametrized by the rational circle \((\cos\theta,\sin\theta)=((1-t^2)/(1+t^2),2t/(1+t^2))\). It checked \(305\) rational parallelogram systems. For each system it independently reconstructed \(E_0\), \(E_2\), \(E_4\), the exact area deficit, and the expected ordering of \(E_6\); explicit equal-side orthogonal systems and unequal/skew examples tested equality. The exact run returned:

`EXACT_CHECK_OK systems=305 E0 E2 E4 area-deficit E6 convex-power equality; square_cases=3`

These finite tests are *not* a proof of the universal convex-order inequality or the \(C^2\) rigidity; those statements follow from the preceding analytic argument.

## Relationship to prior work

Csató, Giovagnoli and Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1 (public 20 August 2026), treat weighted perimeter optimization among convex curves. Their introduction and Section 3.2 expressly credit Sachs with the fact that **all centered parallelograms share the quadratic moment** at fixed perimeter. That invariant, the square's value at exponent two, and the surrounding classical perimeter problem are **not claimed as new** here. Their Theorem 1.4 concerns comparisons with a degenerate needle under particular monotonicity and symmetry assumptions, rather than fixed-perimeter convex ordering of square and all skew parallelograms.

The present statement instead compares all convex functions of the squared radial distance, including nonmonotone convex tests, and proves square rigidity for all strictly convex such weights, together with an only-if classification of all \(C^2\) shape-independent radial weights. The exact fourth-moment area identity itself is **not new**: it follows by elementary rearrangement of the single-point boundary fourth-moment formula displayed in the published *Fourth-chord moment amplification and angular phase transition for parallelograms*. The convex-order and only-if rigidity claims are not implied by that one moment. Nor are they implied merely by the known quadratic equality or the cited needle bounds; the proof uses two global Jensen/balancing comparisons.

Relevant mathematical-record comparisons additionally distinguished boundary-radial moments from pairwise chord-distance fourth moments, radial mean bodies, projection-width statistics, and Hausdorff-continuity results. Those are different random variables or questions, and title/parameter similarity alone is not treated as mathematical novelty evidence.

## Limitations

The geometric class is exactly the nondegenerate centrally positioned planar parallelograms with Euclidean arclength sampling; no assertion concerns arbitrary quadrilaterals, translated origins, other sampling measures, or all centrally symmetric convex curves. The earlier German-language Sachs papers were not independently available for full inspection here; their established quadratic-moment statement is acknowledged through the 2026 primary source. Historical priority for the universal convex-order refinement and rigidity remains open to independent literature audit. The finite verification code cannot establish infinite-dimensional or continuum claims by enumeration.

## References

1. Gyula Csató, Davide Giovagnoli, Prosenjit Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, publicly posted 2026-08-20. https://arxiv.org/html/2608.19851v1 . Consulted: introduction, Theorem 1.4, Sections 3.2 and 3.3, references.
2. H. Sachs, *Über eine Klasse isoperimetrischer Probleme. I, II*, Wissenschaftliche Zeitschrift der Martin-Luther-Universität Halle-Wittenberg, Mathematisch-Naturwissenschaftliche Reihe 8 (1958/59), 121–134; historical attribution as reproduced and discussed in the preceding reference. Primary text not inspected.
3. *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e . The displayed boundary single-point moment \(m_4\) contains the quartic area identity; no independent novelty claimed for it.
4. Aleksandr Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1, posted 2026-07-09, https://arxiv.org/abs/2607.08869 . Abstract-level comparison: interior versus boundary convex order for the **same** body; full text inaccessible.
