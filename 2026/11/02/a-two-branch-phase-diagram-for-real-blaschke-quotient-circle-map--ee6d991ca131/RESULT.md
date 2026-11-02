# A two-branch phase diagram for real Blaschke-quotient circle maps

## Finding

For real \(-1<a,b<1\), put
\[
 B_c(z)=\frac{z-c}{1-cz},\qquad
 \Gamma_{a,b}(z)=z\frac{B_a(z)}{B_b(z)},\quad |z|=1.
\]
Write
\[
 L(a)=-\frac{1-a}{3+a},\qquad U(a)=\frac{1+a}{3-a},\qquad
 s_*=\frac{\sqrt3}{2},
\]
and, for \(s_*\le s<1\), define
\[
 r_\pm(s)=\frac{1\pm\sqrt{4s^2-3}}{2s}.
\]

**Exact topological classification.** The boundary map \(\Gamma_{a,b}\) is an orientation-preserving circle homeomorphism if and only if
\[
 L(a)\le b\le U(a)
\]
and it is **not** the case that
\[
 ab>0,\quad |a|>s_*,\quad
 r_-(|a|)<|b|<r_+(|a|).
\]
Its restriction is an orientation-preserving \(C^\infty\) circle diffeomorphism if and only if the endpoint inequalities are strict and it is **not** the case that
\[
 ab>0,\quad |a|\ge s_*,\quad
 r_-(|a|)\le |b|\le r_+(|a|).
\]
Thus, at each fixed \(|a|>\sqrt3/2\), the admissible values of \(b\) have **two disconnected intervals**, separated by an exact forbidden band of the same sign as \(a\). The band first appears at \(|a|=\sqrt3/2\); at that critical value, the unique parameter \(b=\operatorname{sgn}(a)/\sqrt3\) is a homeomorphism with a degenerate angular derivative, but not a circle diffeomorphism.

**Exact fold counts.** If \(b<L(a)\) or \(b>U(a)\), the map has exactly two simple angular turning points. If \(L(a)<b<U(a)\) and \(ab>0\), \(|a|>s_*\), and \(r_-(|a|)<|b|<r_+(|a|)\), it has exactly four simple angular turning points. In the homeomorphic region there are no sign-changing angular turning points; at an equality boundary, the angular derivative instead has one or two isolated zero contacts.

For example, at \(a=9/10\), \(b=1/2\), the angular derivative is positive at both diametral points \(1,-1\) but negative at the points with cosine \(29/36\). Thus endpoint testing alone misses a genuine four-fold obstruction.

For every admissible homeomorphic parameter pair (including equality boundaries), the Poisson extension of \(\Gamma_{a,b}\) is a sense-preserving harmonic diffeomorphism of the open unit disk onto itself, by the Radó–Kneser–Choquet theorem. This latter extension consequence is classical; the new content is the exact two-parameter boundary classification and fold bifurcation.

## Assumptions and scope

The real parameters satisfy \(a,b\in(-1,1)\); the quotient is evaluated on the unit circle, where its denominator never vanishes. A **circle homeomorphism** means a continuous bijection with a continuous inverse, with orientation preserving determined by topological degree \(+1\). A **circle diffeomorphism** means a \(C^\infty\) bijection with \(C^\infty\) inverse. An **angular turning point** is a point at which the derivative of a continuous lift of the angular map vanishes and changes sign. The adjective *simple* refers to a simple zero of this derivative as a function of the angle.

No assertion about injectivity or convolution of \(\Gamma_{a,b}\) outside the unit circle is made. No classification of the self-convolution of its normalized harmonic extension is claimed.

## Proof

**1. Angular derivative and degree.** Every real Blaschke factor has degree one on the circle, and
\[
 \frac{d}{dt}\arg B_c(e^{it})
 =\frac{1-c^2}{1-2c\cos t+c^2}.
\]
Consequently \(\Gamma_{a,b}\) has degree \(1+1-1=1\). Its angular lift \(\theta_{a,b}(t)\) has derivative
\[
 \theta'_{a,b}(t)=1+
 \frac{1-a^2}{1-2a\cos t+a^2}
 -\frac{1-b^2}{1-2b\cos t+b^2}.
\]
Both denominators are strictly positive. On putting \(x=\cos t\), the sign is that of
\[
 N_{a,b}(x)=4abx^2-4b(1+ab)x+1-a^2+3b^2+a^2b^2. \tag{1}
\]
This is an exact identity, not an asymptotic formula.

A continuous lift of a degree-one circle map is strictly increasing if and only if its analytic derivative is everywhere nonnegative: the reverse implication uses the fact that an analytic nonnegative derivative with total integral \(2\pi\) cannot vanish identically on any interval. Therefore \(\Gamma_{a,b}\) is an orientation-preserving circle homeomorphism exactly when \(N_{a,b}(x)\ge0\) on \([-1,1]\). It is a smooth orientation-preserving diffeomorphism exactly when the inequality is strict. Necessity follows because a differentiable increasing function has nonnegative derivative; at a zero derivative the inverse cannot be \(C^1\).

**2. Endpoint restrictions.** The endpoint values factor as
\[
 \begin{aligned}
 N_{a,b}(1)&=(a-1)(b-1)(1+a-(3-a)b),\\
 N_{a,b}(-1)&=(a+1)(b+1)(1-a+(3+a)b).
 \end{aligned} \tag{2}
\]
Because \(-1<a,b<1\), both have the required nonnegative signs precisely when \(L(a)\le b\le U(a)\); they are strictly positive precisely when both inequalities are strict.

**3. Opposite signs and degenerate cases.** If \(ab\le0\), then (1) is concave or affine in \(x\). Its minimum on \([-1,1]\) occurs at an endpoint, so the two conditions (2) are sufficient as well as necessary. The cases \(a=0\) and \(b=0\) are thereby included.

**4. Same-sign interior obstruction.** Replacing \((a,b,x)\) by \((-a,-b,-x)\) leaves (1) unchanged. It is therefore enough to consider \(0<a,b<1\). The quadratic is now strictly convex and its vertex is at
\[
 x_0=\frac{1+ab}{2a}>0.
\]
The vertex lies in \((-1,1)\) precisely when
\[
 a>\frac12,\qquad b<V(a):=2-\frac1a.
\]
Moreover \(V(a)<a\) for every \(0<a<1\), and
\[
 U(a)-V(a)=\frac{3(1-a)^2}{a(3-a)}>0. \tag{3}
\]
Outside this vertex regime, the endpoint test is sufficient. Inside it, direct substitution into (1) yields
\[
 N_{a,b}(x_0)=\frac{a-b}{a}
 \bigl(1-a^2-ab+a^2b^2\bigr). \tag{4}
\]
Here \(a-b>0\), so only the sign of the quadratic
\[
 Q_a(b)=a^2b^2-ab+1-a^2
\]
matters. Its discriminant is \(a^2(4a^2-3)\). For \(a<s_*\), the polynomial is strictly positive for all real \(b\); for \(a=s_*\), it is nonnegative with one double root \(b=1/\sqrt3\). For \(s_*<a<1\), it is negative exactly when
\[
 r_-(a)<b<r_+(a).
\]
Both roots belong to the vertex regime: they are positive, and
\[
 4a-3>\sqrt{4a^2-3},\qquad
 (4a-3)^2-(4a^2-3)=12(1-a)^2>0
\]
shows \(r_+(a)<2-1/a=V(a)\). Equation (3) then places the entire forbidden band strictly between \(0\) and \(U(a)\). The symmetry in the first sentence of this step handles both negative parameters. This proves both classifications, with weak conditions for homeomorphisms and strict conditions for diffeomorphisms.

**5. Exact turning-point counts.** When \(b>U(a)\), equations (2) give \(N(1)<0<N(-1)\). When \(b<L(a)\), they give \(N(-1)<0<N(1)\). A polynomial of degree at most two with opposite endpoint signs has precisely one simple zero in \((-1,1)\). Each interior cosine root corresponds to two simple angular zeros, hence two turning points. In the forbidden interior band, (4) is negative while both endpoint values are positive. Strict convexity gives exactly two simple roots in \((-1,1)\), hence four simple turning points. At the transition values these roots coalesce in the interior or contact an endpoint; the angular derivative is then nonnegative and has isolated zero contacts, as asserted.

**6. Exact rational four-fold witness.** At \(a=9/10\), \(b=1/2\), formula (1) has vertex at \(x_0=29/36\), and
\[
 N_{a,b}(x_0)=-\frac{23}{900},\qquad
 N_{a,b}(1)=\frac{17}{400},\qquad
 N_{a,b}(-1)=\frac{2337}{400}.
\]
Thus the derivative changes sign four times even though the two endpoint tests pass. These are exact rational identities.

**7. Harmonic extension.** A degree-one circle homeomorphism is an orientation-preserving homeomorphism from the boundary of the disk onto the boundary of a convex domain. The classical Radó–Kneser–Choquet theorem therefore makes its Poisson integral a harmonic diffeomorphism of the open disk onto the disk. No boundary smoothness assumption is required for this implication, so equality cases are included.

## Verification

The file `CHECK.py` is a standalone Python 3 checker using only the standard library. It checks the quadratic numerator identity, both endpoint factorizations, vertex identity and the rational four-fold witness using exact fractions, and compares the stated strict phase criterion against the true quadratic minimum on a deterministic random sample of the full real parameter square. Run it with `python CHECK.py`. The checker is supplementary: finite sampling does not establish a universal classification; steps 1–7 above supply the proof.

## Relationship to prior work

Wang and Zhong's 2026 construction of a counterexample to Dorff's harmonic-convolution problem uses the same real rational Blaschke-quotient boundary map at the particular parameters \(a=-10/11\), \(b=1/44\), and verifies strict angular positivity at that one pair. Their paper explicitly observes stability under small parameter changes but does not state a global two-parameter criterion or the disconnected admissible bands. The present theorem classifies that underlying boundary family completely; it does **not** sharpen the paper's self-convolution theorem.

A previously indexed calculation of the self-convolution Jacobian threshold along the single ray \(a=-10/11\), and a calculation of the unique real-axis fold point for the original ellipse, concern the convolution of a **normalized harmonic extension**, rather than the global boundary homeomorphism problem. Their statements do not imply the full two-parameter criterion or the separate four-turning-point phase obtained here. The angular Poisson-kernel identity and the Radó–Kneser–Choquet theorem are classical inputs, not claimed as new.

## Limitations

The phase classification is for the explicitly defined two-real-parameter family, not arbitrary quotients of finite Blaschke products, complex parameters or arbitrary circle diffeomorphisms. The Poisson extension consequence is classical and does not establish preservation or failure of harmonic convolution. Relevant literature may contain an unindexed equivalent parameter calculation; no independent audit has been conducted.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1, first public version 2026-09-10. Sections 1, 3–5 and 7–8 give the rational boundary construction, Poisson extension, and self-convolution test.
2. T. Radó, H. Kneser and G. Choquet, classical Radó–Kneser–Choquet theorem for harmonic Poisson extensions of circle homeomorphisms onto convex boundaries; see the exposition and references in Wang–Zhong, Section 2.3.
3. *Exact parameter threshold for the Dorff counterexample's rational witness*, publicly indexed mathematical result (2026). This concerns a fixed-parameter Jacobian witness and not the present boundary-map phase classification.
4. *Unique real-axis fold point in the Dorff ellipse counterexample*, publicly indexed mathematical result (2026). This concerns the harmonic self-convolution and not the boundary circle map.
