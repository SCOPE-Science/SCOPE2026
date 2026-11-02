# Exact hyperbolic circumcircle sampling law and a sharp half-exponential tail

## Finding

Fix any two distinct points \(A,B\) of the curvature-\(-1\) hyperbolic plane, at distance \(d>0\), and let \(O\) be the midpoint of their geodesic. Put
\[
a=\tanh(d/4),\qquad R=\tanh(T/2),\qquad 0<a,R<1.
\]
Choose a third point \(X\) uniformly either by hyperbolic arclength on the circle of radius \(T\) about \(O\), or by hyperbolic area in the disk of radius \(T\) about \(O\). Let \(E\) be the event that the nondegenerate geodesic triangle \(ABX\) has a genuine **hyperbolic circumcircle** (rather than a horocycle or hypercycle). Degenerate choices have probability zero.

Define \(f_a(u)=0\) when \(0<u\le a^2\), and for \(a^2<u<1\), define
\[
f_a(u)=\frac2\pi\arccos\!\left(\frac{|u^2-a^2|}{u(1-a^2)}\right).
\]
The exact circle-sampling probability is \(\mathbb P_{\rm circle}(E)=f_a(R)\). In particular, it vanishes for \(T\le T_0=2\operatorname{artanh}(a^2)\); it increases strictly to one at \(T=d/2\), then decreases strictly to zero as \(T\to\infty\).

For \(a^2\le u<1\), set
\[
z_a(u)=\sqrt{\frac{u^2-a^4}{1-u^2}},\qquad
J_a(u)=\arctan\!\left(\frac{z_a(u)}{a^2}\right)+\frac{z_a(u)}{1-a^2},
\]
and define the piecewise elementary function
\[
H_a(R)=\begin{cases}J_a(R),&a^2<R\le a,\\
2J_a(a)-J_a(R),&a<R<1.
\end{cases}
\]
Then the *complete disk-sampling law* is
\[
\boxed{\mathbb P_{\rm disk}(E)=\begin{cases}
0,&0<R\le a^2,\\
\displaystyle\frac{f_a(R)}{R^2}-\frac{2(1-R^2)}{\pi R^2}H_a(R),&a^2<R<1.
\end{cases}}
\]
The disk probability has exactly one global maximizer, at a radius \(R_*(a)\in(a,1)\); it is characterized exactly by \(f_a(R_*)=\mathbb P_{\rm disk}(E)\). Thus the most favorable uniform disk is strictly larger than the unique most favorable uniform circle.

Both probabilities have sharp rare-event tails for each fixed \(d>0\):
\[
\lim_{T\to\infty}e^{T/2}\mathbb P_{\rm circle}(E)
=\frac4\pi\sqrt{\cosh(d/2)},\qquad
\lim_{T\to\infty}e^{T/2}\mathbb P_{\rm disk}(E)
=\frac8\pi\sqrt{\cosh(d/2)}.
\]
The factor two between the leading constants is exact. No claim is made about a random pair \(A,B\); the two anchors are fixed.

## Assumptions and scope

Hyperbolic curvature equals \(-1\), and uniformity means normalized intrinsic arclength or intrinsic area, not Euclidean area in a disk model. The two anchors are distinct and fixed, and the sampling center is their hyperbolic midpoint. All asserted probabilities are for \(T>0\), with equality/tangency and collinearity null sets disregarded. A hyperbolic circumcircle means a circle with a **finite interior center**, not a horocycle or hypercycle. The orientation of the fixed segment is immaterial by isometry invariance.

## Proof

**1. Geometric criterion and radial exclusion.** An isometry of the Poincare unit disk takes \(O\) to its center and \(A,B\) to the Euclidean points \((-a,0),(a,0)\), with \(d=4\operatorname{artanh}(a)\). Write \(X=(u\cos\theta,u\sin\theta)\), where \(0<u<1\). When \(\sin\theta\ne0\), the unique Euclidean circumcircle through these three points has center \((0,c)\) and radius \(\sqrt{a^2+c^2}\), with
\[
c=\frac{u^2-a^2}{2u\sin\theta}.
\]
A Euclidean circle is a genuine hyperbolic circle precisely when it is strictly inside the unit disk; for this circle the condition is \(|c|+\sqrt{a^2+c^2}<1\), equivalently \(2|c|<1-a^2\). Hence
\[
E\quad\Longleftrightarrow\quad
|\sin\theta|>\frac{|u^2-a^2|}{u(1-a^2)}.
\tag{1}
\]
For \(0<u\le a\), the right side is less than one exactly when \(u>a^2\), since \(u(1-a^2)-(a^2-u^2)=(u-a^2)(1+u)\). For \(a\le u<1\), it is less than one since \(u(1-a^2)-(u^2-a^2)=(1-u)(u+a^2)>0\). This proves the inner forbidden disk and describes the entire admissibility locus, up to null boundaries.

**2. Circle probability and its monotonicity.** Hyperbolic arclength on a circle centered at \(O\) is uniform in the disk-model polar angle \(\theta\). For any \(q\in[0,1]\), the fraction of angles with \(|\sin\theta|>q\) is \(2\arccos(q)/\pi\). Apply (1) with \(u=R\). On \((a^2,a)\), the ratio in (1) decreases strictly from one to zero; on \((a,1)\), it increases strictly from zero to one. Thus the asserted monotonicity, threshold, and peak follow. Since \(R=a\) means \(T=2\operatorname{artanh}(a)=d/2\), the peak location has the stated intrinsic form.

**3. Exact disk integration.** In Euclidean polar coordinates, hyperbolic area is \(4u(1-u^2)^{-2}\,du\,d\theta\); the total area of the disk of Euclidean radius \(R\) is \(4\pi R^2/(1-R^2)\). Thus
\[
\mathbb P_{\rm disk}(E)=\frac{2(1-R^2)}{R^2}\int_{a^2}^{R}\frac{u f_a(u)}{(1-u^2)^2}\,du\quad (R>a^2).
\tag{2}
\]
The integrand's angular derivative is, for \(u\ne a\),
\[
f_a'(u)=\begin{cases}
\displaystyle\frac{2(u^2+a^2)}{\pi u\sqrt{(1-u^2)(u^2-a^4)}},&a^2<u<a,\\
\displaystyle-\frac{2(u^2+a^2)}{\pi u\sqrt{(1-u^2)(u^2-a^4)}},&a<u<1.
\end{cases}
\tag{3}
\]
Indeed \(u^2(1-a^2)^2-(u^2-a^2)^2=(1-u^2)(u^2-a^4)\). Direct substitution \(y=u^2=a^4+(1-a^4)\sin^2\phi\) yields
\[
\int_{a^2}^{R}\frac{u^2+a^2}{u(1-u^2)^{3/2}\sqrt{u^2-a^4}}\,du=J_a(R).
\tag{4}
\]
For clarity, the substitution in (4) splits its angular integrand into \(a^2/y+(1+a^2)/(1-y)\), whose integrals are respectively \(\arctan(\tan\phi/a^2)\) and \(\tan\phi/(1-a^2)\). Therefore \(\int_{a^2}^{R}f_a'(u)/(1-u^2)\,du=2H_a(R)/\pi\). Integration by parts in (2), using \(f_a(a^2)=0\) and \(d[1/(2(1-u^2))]/du=u/(1-u^2)^2\), gives exactly the stated elementary disk formula. The apparent kink of \(f_a\) at \(u=a\) causes no boundary term because \(f_a\) is continuous.

**4. Unique disk optimum.** Let \(F(R)=\mathbb P_{\rm disk}(E)\). Writing (2) as a positive-weight average of \(f_a\), including the zero-weighted central interval, gives
\[
F'(R)=\frac{2}{R(1-R^2)}\bigl(f_a(R)-F(R)\bigr)
\tag{5}
\]
for \(R>a^2\). The prefactor follows by differentiating the normalized area \(R^2/(1-R^2)\). For \(a^2<R\le a\), strict increase of \(f_a\) gives \(F(R)<f_a(R)\), so \(F'>0\). For \(R>a\), the function \(f_a\) decreases strictly. At every zero of \(g(R)=f_a(R)-F(R)\) in this interval, (5) implies \(g'(R)=f_a'(R)<0\). The sharp asymptotics proved next show \(F(R)>f_a(R)\) for all sufficiently large \(R<1\). Continuity implies the existence of a zero and the strict negative derivative at *each* zero ensures uniqueness. Consequently \(F\) has exactly one maximum, strictly beyond \(R=a\).

**5. Sharp tails.** The ratio in (1), on \(R>a\), has derivative \((1+a^2)/(1-a^2)\) at \(R=1\). With \(R=\tanh(T/2)\),
\[
1-R=2e^{-T}+O(e^{-2T}),\quad \frac{1+a^2}{1-a^2}=\cosh(d/2),\quad
\arccos(1-s)=\sqrt{2s}\,(1+O(s)).
\]
This proves \(\mathbb P_{\rm circle}(E)\sim (4/\pi)\sqrt{\cosh(d/2)}e^{-T/2}\). Finally, radial hyperbolic area has density \(\sinh t/(\cosh T-1)\) for \(0<t<T\), whence
\[
\mathbb P_{\rm disk}(E)=\frac{\int_0^T\sinh t\,\mathbb P_{\rm circle,t}(E)\,dt}{\cosh T-1}.
\]
Integrating the preceding positive asymptotic gives a numerator asymptotic to \((4/\pi)\sqrt{\cosh(d/2)}e^{T/2}\), while \(\cosh T-1\sim e^T/2\). The disk coefficient is thus twice the circle coefficient, as claimed.

## Verification

The accompanying `verify.py` independently evaluates the Poincare circumcircle-containment inequality for random triples, tests the polynomial radical identity using rational arithmetic, differentiates the proposed antiderivative numerically, compares the closed disk formula to independently integrated radial area, samples from the correct hyperbolic area distribution, and checks the sharp outer asymptotics and the unique sign transition. Execute with `python verify.py`; it uses the Python standard library and reports `ALL_CHECKS_PASSED` upon success. Finite tests corroborate but do not replace the analytic proofs of (1)–(5).

## Relationship to prior work

Beardon (2022, Theorem 1.1 and Lemma 3.1) records the classical classification of circumcycles into circles, horocycles, and hypercycles and the role of perpendicular bisectors. An expository Glasgow hyperbolic-geometry page states the fixed-two-vertices admissibility region in terms of two horocycles; this geometric locus is **not** claimed as new. The result here is the precise intrinsic-arclength and intrinsic-area probability law, an evaluated elementary disk formula, the unique optimal sampling disk, and the sharp half-exponential escape constants. Prior results on spherical random polygons, hyperbolic circle perimeter, and unrelated circumradius tails do not give this probability problem.

## Limitations

The two anchors are fixed; their randomization is not addressed. The third point is sampled from a circle or disk centered at their midpoint, and translating the sampling center changes the law. The exact disk formula is not asserted to be a new geometric characterization of hyperbolic circumcycles. The proof does not cover curvatures other than \(-1\) without metric rescaling, nor does it derive the distribution of the finite circumradius conditional on existence. Historical priority for the fully evaluated sampling laws is subject to further bibliographic checking, especially older geometry literature.

## References

1. A. F. Beardon, *Circumscribed hyperbolic triangles*, Archiv der Mathematik 119 (2022), 439–448; public online date 2022-08-08, https://doi.org/10.1007/s00013-022-01761-x .
2. W. W. S. (University of Glasgow), *The circumcircle of a hyperbolic triangle*, https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/circumcircle.html . Undated educational source describing the two-horocycle locus.
3. W. W. S. (University of Glasgow), *The circumcircle theorem*, https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/circumproof2.html . Undated educational proof of a side-length existence criterion.
