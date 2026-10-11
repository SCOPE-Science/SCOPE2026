# Sharp overlap transition for the \(p\)-joint numerical radius of two rank-one projections

## Finding
Let \(P=uu^*\), \(Q=vv^*\) be rank-one orthogonal projections on a complex Hilbert space, and let \(c=|\langle u,v\rangle|\). For \(p\ge1\), define the balanced joint numerical radius
\[
J_p(P,Q)=\sup_{\|x\|=1}\left(\frac{\langle Px,x\rangle^p+\langle Qx,x\rangle^p}{2}\right)^{1/p}.
\]
The maximizing-ray geometry changes **exactly** at \(c_p=1-1/p\). When \(0<c<1\) and \(c\ge c_p\),
\[
J_p(P,Q)=\frac{1+c}{2}
\]
and there is exactly one maximizing complex ray, the positive bisector of the two generating rays. When \(0<c<c_p\), there are exactly two maximizing rays exchanged by the bisector reflection and the radius is strictly above \((1+c)/2\); their angle is determined by a **unique explicit monotone scalar equation** given below.

In the Euclidean case, the full algebraic phase diagram is
\[
J_2(P,Q)^2=\begin{cases}
\dfrac{(1-c^2)^2}{2(1-2c^2)},&0\le c\le\tfrac12,\\[5pt]
\dfrac{(1+c)^2}{4},&\tfrac12\le c\le1.
\end{cases}
\]
The two branches meet with continuous first derivative but different second one-sided derivatives: \(19/2\) and \(1/2\), respectively, at \(c=1/2\). Thus the radius squared is \(C^1\) but not \(C^2\) at the overlap transition.

## Assumptions and scope
The Hilbert space is complex and has dimension at least two, with no upper dimension restriction. The parameter \(p\) is an arbitrary real number satisfying \(1\le p<\infty\). Inner-product convention does not affect the assertion. Normalize the generators by \(\|u\|=\|v\|=1\), and choose phases for \(0<c<1\) so that
\[
v=c u+\sin\gamma\, w,\qquad w\perp u,\quad \|w\|=1,\quad\gamma=\arccos c\in(0,\pi/2).
\]
Write \(x_\theta=\cos\theta\,u+\sin\theta\,w\). For \(0<c<1-1/p\), define \(\theta_*\in(0,\gamma/2)\) uniquely by
\[
\frac{\log\bigl(\sin(\gamma-\theta_*)/\sin\theta_*\bigr)}{\log\bigl(\cos\theta_*/\cos(\gamma-\theta_*)\bigr)}=2p-1.
\]
Then
\[
J_p(P,Q)=\left(\frac{\cos^{2p}\theta_*+\cos^{2p}(\gamma-\theta_*)}{2}\right)^{1/p},
\]
and the entire maximizing-ray set consists precisely of the rays spanned by \(x_{\theta_*}\) and \(x_{\gamma-\theta_*}\). If \(0<c<1\) and \(c\ge1-1/p\), the sole maximizing ray is spanned by \(x_{\gamma/2}\).

The endpoints are also classified. If \(c=0\), \(J_p=2^{-1/p}\); the only maximizing rays for \(p>1\) are the two orthogonal generator rays, while for \(p=1\) every ray contained in their two-dimensional span maximizes. If \(c=1\), then \(P=Q\), \(J_p=1\), and their common range is the unique maximizing ray.

## Proof
**1. Exact rank-two and phase reduction.** Write any unit vector \(x=y+z\) with \(y\in\operatorname{span}\{u,v\}\) and \(z\perp\operatorname{span}\{u,v\}\). Both expectations are homogeneous quadratic functions of \(y\); replacing \(x\) by \(y/\|y\|\) strictly increases their positive balanced mean unless \(z=0\), so every maximizer belongs to the span. In the orthonormal basis \((u,w)\), fixing the coordinate magnitudes and aligning their phases maximizes the second expectation without changing the first. For \(0<c<1\), both coordinates must have strictly positive magnitudes at an optimum (the derivative from either endpoint toward the interior is strictly positive). Up to global phase, a maximizer is \(x_\theta\), \(0<\theta<\pi/2\). If \(\theta>\gamma\), moving to \(\gamma\) increases both expectations, so in fact \(0<\theta\le\gamma\). Thus maximize
\[
G_p(\theta)=\frac{\cos^{2p}\theta+\cos^{2p}(\gamma-\theta)}{2},\qquad0\le\theta\le\gamma.
\]
The function is symmetric about \(\alpha=\gamma/2\).

**2. A strictly monotone stationary-point ratio.** On \(0<\theta<\alpha\), put
\[
N(\theta)=\log\frac{\sin(\gamma-\theta)}{\sin\theta},\quad
D(\theta)=\log\frac{\cos\theta}{\cos(\gamma-\theta)},\quad F(\theta)=\frac{N(\theta)}{D(\theta)}.
\]
Both logarithms are positive. Differentiating \(G_p\) gives
\[
\operatorname{sgn}G_p'(\theta)=\operatorname{sgn}\bigl(F(\theta)-(2p-1)\bigr).
\]
Moreover,
\[
\frac{N'(s)}{D'(s)}=\cot s\,\cot(\gamma-s)=:r(s),
\qquad -D'(s)=\frac{\sin\gamma}{\cos s\cos(\gamma-s)}>0.
\]
As \(0<\gamma<\pi/2\), \(r(s)\) is strictly decreasing for \(0<s<\alpha\): the derivative of \(\log r(s)\) is \(-2/\sin(2s)+2/\sin(2(\gamma-s))<0\), because \(\sin(2(\gamma-s))-\sin(2s)=2\cos\gamma\sin(\gamma-2s)>0\). Since \(N(\alpha)=D(\alpha)=0\), integration yields
\[
F(\theta)=\frac{\int_\theta^\alpha r(s)b(s)\,ds}{\int_\theta^\alpha b(s)\,ds},\quad
b(s)=\frac{\sin\gamma}{\cos s\cos(\gamma-s)}>0.
\]
It follows by strict weighted averaging that \(F\) itself strictly decreases on \((0,\alpha)\), with endpoint limits
\[
\lim_{\theta\downarrow0}F(\theta)=+\infty,\qquad
\lim_{\theta\uparrow\alpha}F(\theta)=\cot^2\alpha=\frac{1+c}{1-c}.
\]
Consequently, if \(2p-1\le(1+c)/(1-c)\), equivalently \(c\ge1-1/p\), the function \(G_p\) is strictly increasing toward the midpoint; the midpoint is its unique maximum. If \(2p-1>(1+c)/(1-c)\), there is exactly one \(\theta_*\in(0,\alpha)\) at which the sign of \(G_p'\) changes from positive to negative. Reflection about \(\alpha\) gives exactly two global maxima, and the midpoint is a local minimum. This proves the entire transition including strictness at equality.

**3. Values and boundary overlap.** At the bisector both expectations equal \((1+c)/2\), giving the flat-in-\(p\) upper branch. The two separated maxima are strictly higher than the bisector. When \(c=0\), the two expectations are nonnegative and sum to at most one. For \(p=1\), equality requires membership of the projector span; for \(p>1\), strict convexity of the power function forces one expectation to equal one and the other zero. When \(c=1\), both projections coincide and are maximized only on the shared range.

**4. Closed Euclidean formula.** For \(p=2\), set \(z=\cos(2\theta-\gamma)\in[c,1]\). Double-angle identities give the exact quadratic
\[
G_2(\theta)=\frac{2-c^2+2cz+(2c^2-1)z^2}{4}.
\]
For \(0\le c<1/2\) its unique maximizing \(z\) is \(z_*=c/(1-2c^2)\in[c,1)\), resulting in \((1-c^2)^2/[2(1-2c^2)]\). The general phase theorem places the maximum at \(z=1\) for \(c\ge1/2\), yielding \((1+c)^2/4\). The sharp branch gap for \(0\le c<1/2\) is
\[
J_2(P,Q)^2-\frac{(1+c)^2}{4}=\frac{(1+c)^2(1-2c)^2}{4(1-2c^2)}>0.
\]
Differentiation of the two rational expressions gives the claimed \(C^1\)-but-not-\(C^2\) transition.

## Verification
The enclosed standalone `verify_projection_pair.py` performs exact rational checks of the Euclidean quadratic maximization for representative overlaps and finite numerical checks of the general-\(p\) scalar branch and its reflected maximizers. It ran successfully and printed `TWO_PROJECTION_P_JOINT_PHASE_AND_EUCLIDEAN_EXACT_CHECKS_OK`. These finite calculations are supplementary to the full analytical proof, not substitutes for its all-\(p\) quantifiers or uniqueness statements.

## Relationship to prior work
Aljawi, Alotaibi, Dragomir, and Feki (2026) define weighted two-operator Euclidean numerical radii and discuss power-mean generalizations; setting their semi-inner-product weight to the identity, balancing two operators, and specializing to projections motivates this problem. The accessible abstract presents general inequalities rather than this exact angle-and-exponent optimization; the article's inaccessible body remains an originality risk.

Feki (2024), Theorems 2.3 and 2.25 and Corollary 2.26, proves bounds for general two-operator joint numerical radii. These do not supply exact phase thresholds or classify optimizing rays for a fixed nonorthogonal projection pair. Bottazzi and Varela (arXiv:2303.04128v1), Section 2, define \(p\)-joint radii for compressed coordinate-projection families in their study of subspace moments; their results do not provide the present exact two-ray overlap profile. The normalization by \(1/2\) is made explicit so it is not confused with unbalanced definitions. No claim that joint numerical radii themselves are new is made.

## Limitations
The theorem concerns exactly two *rank-one orthogonal projection operators*, the balanced two-entry power mean, and \(p\ge1\). It makes no claim for more than two projections, higher ranks, general operator pairs, or weighted asymmetry. The scalar equation for the separated branch is uniquely solvable but is not claimed to admit an elementary closed form for arbitrary real \(p\). A fully inspected copy of the motivating 2026 article could not be obtained; an unindexed equivalent computation remains a specific originality risk. Independent scientific validation has not been performed.

## References
1. S. Aljawi, A. H. Alotaibi, S. S. Dragomir, K. Feki, *New inequalities for the A-joint weighted numerical radius with applications*, AIMS Mathematics **11** (2026), 20535–20557. DOI: 10.3934/math.2026835. First verified public publication: 2026-07-13.
2. K. Feki, *Inequalities for the A-joint numerical radius of two operators and their applications*, Hacettepe Journal of Mathematics and Statistics **53** (2024), 22–39. DOI: 10.15672/hujms.1142554.
3. T. Bottazzi, A. Varela, *Minimal self-adjoint compact operators, moment of a subspace and joint numerical range*, arXiv:2303.04128v1 (2023), especially Section 2, Remark 2.
