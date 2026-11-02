# Exact two-point squared geodesic distance on rectangular flat Klein bottles

## Finding

For any real \(a,b>0\), let \(K_{a,b}\) be the flat Klein bottle obtained by quotienting the Euclidean plane by the isometries
\[
\tau(x,y)=(x+2a,y),\qquad \sigma(x,y)=(-x,y+b).
\]
Its area is \(2ab\). Let \(P,Q\) be independent area-uniform points and let \(\rho\) be the intrinsic geodesic metric. Set \(M(a,b)=\mathbb E[\rho(P,Q)^2]\) and
\[
B(a,b)=\frac{a^2}{3}+\frac{b^2}{12}-\frac{2a^4}{45b^2}.
\]
Then the **complete aspect-ratio formula** is
\[
M(a,b)=B(a,b)+H(a,b),\qquad
H(a,b)=\begin{cases}
0,&0<a\le b,\\[3pt]
\displaystyle\frac{4}{15b^2a^2}\int_b^a(u^2-b^2)^{5/2}\,du,&a>b.
\end{cases}
\]
The integral is elementary. For \(a>b\), the exact closed form is
\[
H(a,b)=\frac{a\sqrt{a^2-b^2}(8a^4-26a^2b^2+33b^4)-15b^6\operatorname{arcosh}(a/b)}{180b^2a^2}.
\]
For example, \(M(1,1)=67/180\) and \(M(1,2)=59/90\).

The correction turns on at the **sharp ratio \(a/b=1\)**. With \(b>0\) fixed,
\[
H(a,b)\sim\frac{2^{11/2}}{105b^{3/2}}(a-b)^{7/2}
\quad\text{as }a\downarrow b\text{ from above}.
\]
Consequently \(a\mapsto M(a,b)\) is three times continuously differentiable but not four times continuously differentiable at \(a=b\).

Let \(T_{a,b}=\mathbb R^2/(2a\mathbb Z\times b\mathbb Z)\) be the **equal-area rectangular flat torus**. For independent uniform \(P_T,Q_T\),
\[
\mathbb E[d_T(P_T,Q_T)^2]=\frac{a^2}{3}+\frac{b^2}{12}.
\]
There is a **strict global Klein-bottle/torus gap**:
\[
0<\mathbb E[d_T(P_T,Q_T)^2]-M(a,b)
=\frac{2a^4}{45b^2}-H(a,b)
\quad\text{for every }a,b>0.
\]
In the entire regime \(a\le b\), this gap is exactly \(2a^4/(45b^2)\).

## Assumptions and scope

The metric is the intrinsic shortest-path metric induced by the Euclidean covering plane, **not** the extrinsic distance in an immersion of the Klein bottle into three-dimensional space. The quotient is smooth, compact, flat and nonorientable. The two random points are independent and uniformly distributed by Riemannian area. Both parameters are strictly positive; no boundary or degenerate quotient is included in the theorem. Statements at \(a=b\) use the continuous value in either branch. The torus comparator has the same fundamental rectangular dimensions and area \(2ab\), but it is not the orientable double cover of \(K_{a,b}\) (which has vertical period \(2b\)).

## Proof

**1. Exact nearest-image reduction.** A fundamental rectangle is \([0,2a)\times[0,b)\). For representatives \(P=(x,y)\) and \(Q=(x',y')\), define
\[
\delta_{2a}(z)=\min_{k\in\mathbb Z}|z-2ka|,\quad
U=\delta_{2a}(x-x'),\quad V=\delta_{2a}(x+x'),\quad W=|y-y'|.
\]
The even powers of the glide reflection supply lifts of \(Q\) of the form \((x'+2ka,y'+2jb)\); the odd powers supply \((-x'+2ka,y'+(2j+1)b)\). Because \(|y-y'|\le b\), the best vertical displacements among these are respectively \(W\) and \(b-W\). Hence, for every pair of representatives,
\[
\rho(P,Q)^2=\min\{U^2+W^2,\ V^2+(b-W)^2\}. \tag{1}
\]
No finite search truncation is used in (1).

**2. An independent-uniform representation.** The original \(x,x'\) are independent Haar-uniform modulo \(2a\). The torus homomorphism \((x,x')\mapsto(x-x',x+x')\pmod{2a}\) is surjective with finite kernel (degree two); it therefore sends Haar measure to product Haar measure. In particular \(U,V\) are independent uniform variables on \([0,a]\). They are independent of \(W\), whose density is
\[
f_W(w)=\frac{2(b-w)}{b^2},\qquad 0\le w\le b.
\]
Thus (1), together with these explicitly independent variables, is also an exact distributional representation of squared intrinsic distance.

**3. Conditional integration.** Put \(D=U^2-V^2\). Then
\[
\rho(P,Q)^2=U^2+W^2-(D-b^2+2bW)_+,
\quad\text{where }z_+=\max(z,0).
\]
Direct integration with the triangular density gives
\[
g(D):=\mathbb E[(D-b^2+2bW)_+\mid D]
=\begin{cases}
0,&D\le-b^2,\\
(D+b^2)^3/(12b^4),&-b^2<D<b^2,\\
D-b^2/3,&D\ge b^2.
\end{cases} \tag{2}
\]
Since \(U,V\) are identically distributed, \(D\) has a symmetric distribution. Pairing \(D\) with \(-D\) in (2) yields the identity
\[
\frac{g(D)+g(-D)}2
=\frac{b^2}{12}+\frac{D^2}{4b^2}
-\frac{(|D|-b^2)_+^2}{4b^2}. \tag{3}
\]
The elementary moments are
\[
\mathbb E[U^2]=\frac{a^2}3,\qquad
\mathbb E[W^2]=\frac{b^2}6,\qquad
\mathbb E[D^2]=2\left(\frac{a^4}5-\frac{a^4}9\right)=\frac{8a^4}{45}.
\]
Taking expectations in (3) and the preceding identity proves
\[
M(a,b)=B(a,b)+\frac{1}{4b^2}\mathbb E[(|U^2-V^2|-b^2)_+^2]. \tag{4}
\]

**4. Sharp active-set boundary and evaluation.** The last expectation in (4) vanishes identically exactly when \(a\le b\); for \(a>b\) it is positive. By symmetry, the positive region in the square \([0,a]^2\) is twice the region \(b<u<a\), \(0<v<\sqrt{u^2-b^2}\). Integrating first in \(v\) gives
\[
\begin{aligned}
H(a,b)&=\frac{1}{2b^2a^2}\int_b^a\int_0^{\sqrt{u^2-b^2}}(u^2-b^2-v^2)^2\,dv\,du\\
&=\frac{4}{15b^2a^2}\int_b^a(u^2-b^2)^{5/2}\,du.
\end{aligned}
\]
An antiderivative is
\[
\frac{u\sqrt{u^2-b^2}(8u^4-26b^2u^2+33b^4)
-15b^6\operatorname{arcosh}(u/b)}{48}.
\]
It vanishes at \(u=b\); inserting both limits yields the asserted closed form.

**5. Regularity at the transition.** Write \(a=b+\varepsilon\) with \(\varepsilon>0\). Uniformly for \(u\in[b,b+\varepsilon]\), \(u^2-b^2=2b(u-b)+O((u-b)^2)\), so
\[
\int_b^{b+\varepsilon}(u^2-b^2)^{5/2}\,du
\sim\frac{2}{7}(2b)^{5/2}\varepsilon^{7/2}.
\]
Substitution into the integral formula proves the stated coefficient. More precisely, the change of variables \(u=b+\varepsilon t\) gives
\[
H(b+\varepsilon,b)=\frac{4\varepsilon^{7/2}}{15b^2(b+\varepsilon)^2}
\int_0^1 (2bt+\varepsilon t^2)^{5/2}\,dt.
\]
The factor multiplying \(\varepsilon^{7/2}\) is smooth and nonzero at \(\varepsilon=0\); differentiation under the integral is justified there because \(2b+\varepsilon t\) stays positive. Therefore \(H\) has continuous derivatives through order three, whereas its fourth derivative from the right diverges as a nonzero multiple of \(\varepsilon^{-1/2}\). The left branch is identically zero. Adding the analytic baseline \(B\) does not change the differentiability classification.

**6. Strict torus comparison.** A torus coordinate difference taken modulo a circle of circumference \(2a\) has shortest displacement uniform on \([0,a]\); for circumference \(b\) it is uniform on \([0,b/2]\). The squared-distance mean on the torus is therefore \(a^2/3+b^2/12\). When \(a>b\), strictly
\[
0<H(a,b)<\frac{4}{15b^2a^2}\int_0^a u^5\,du=\frac{2a^4}{45b^2}.
\]
When \(a\le b\), \(H=0\). This establishes the strict comparison in every positive aspect ratio.

## Verification

The standalone `verify.py` uses only Python's standard library. It checks the exact rational specializations, evaluates the positive-part integral by independent composite Simpson quadrature and compares it with the closed form, checks the nearest-image reduction against explicit deck-transformation enumeration, and independently samples uniform point pairs to compare sample means with the analytical expectations. Reproducible command: `python verify.py`. The following values are consequences of the proof, not numerical conjectures:
\[
M(1,1)=\frac{67}{180},\qquad M(1,2)=\frac{59}{90},\qquad M(2,1)=0.952360310568027\ldots.
\]
The verification run completed successfully. Its maximum absolute deck-orbit discrepancy across the enumerated test cases was approximately \(7.11\times10^{-15}\). The random-sampling checks used independent deterministic pseudorandom draws and checked agreement within six estimated standard errors plus a fixed numerical allowance. All claimed universal conclusions follow from the exact argument above; finite sampling alone would not prove them.

## Relationship to prior work

Matveev (1997) describes geodesic-flow structures on the Klein bottle via covering-plane and glide-reflection quotients. El Mir (2010, inspected 2020 revision) explicitly presents the flat Klein-bottle glide-reflection quotient and its one-parameter metric family while studying conformal systolic inequalities. Davis and Recio-Mitter (2019) establish geodesic complexity and detailed pointwise cut-locus polytopes for flat Klein bottles. These provide context for the quotient metric and minimizer structure; neither inspected text states or directly supplies the random-pair squared-distance integral, the explicit all-aspect mean, the \(7/2\)-order transition, or the strict equal-area torus comparison. Katz and Sabourau (2026) investigate systolic area and the distinguished square flat Klein bottle, a different invariant. The Geomstats Klein-bottle implementation computes nearest representatives; it does not report the integrated two-point moment. Prior descriptions of the covering geometry are not claimed as new.

## Limitations

Only the second moment of the intrinsic pairwise distance is evaluated in closed form; an explicit cumulative distribution and arbitrary higher moments are not claimed. The numerical closed form for \(a\gg b\) exhibits cancellation, so the positive one-dimensional integral is the more stable representation. The result concerns the rectangular family and the specified equal-area rectangular torus, not all flat tori or all Riemannian Klein-bottle metrics. Exhaustive historical priority and independent mathematical assessment have not been established; unindexed earlier treatments of geometric-probability moments could overlap.

## References

- V. S. Matveev, *Quadratically integrable geodesic flows on the torus and on the Klein bottle* (first public preprint 1997-12-23), arXiv:solv-int/9712019, https://arxiv.org/abs/solv-int/9712019.
- C. El Mir, *Bavard’s systolically extremal Klein bottles and three dimensional applications* (first public preprint 2010-07-06; inspected 2020 revision), arXiv:1007.0877, https://arxiv.org/abs/1007.0877.
- D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles* (first public preprint 2019-12-16), arXiv:1912.07411, https://arxiv.org/abs/1912.07411.
- M. G. Katz and S. Sabourau, *Klein bottle and optimal systolic inequality for nonpositively curved surfaces* (first public preprint 2026-09-06), arXiv:2609.06705, https://arxiv.org/abs/2609.06705.
- Geomstats, *KleinBottleMetric* source documentation, https://geomstats.github.io/_modules/geomstats/geometry/klein_bottle.html (accessed 2026-10-27; no source-first-publication date inferred).
