# Sharp positive Lipschitz interpolation at the three midpoints of an obtuse isosceles triangle

## Finding
For every real \(h\) with \(0<h\leq 1\), let
\[
A=(-1,0),\quad B=(1,0),\quad C=(0,h),\quad
M=(0,0),\quad U=(-1/2,h/2),\quad V=(1/2,h/2).
\]
Equip \(X_h=\{A,B,C\}\) and \(Y_h=\{A,B,C,M,U,V\}\) with their inherited Euclidean distances. Write \(\operatorname{Lip}(f)=\max_{x\ne y}|f(x)-f(y)|/\|x-y\|_2\), with real scalar values, and consider linear operators \(T\colon\operatorname{Lip}(X_h)/\mathbb R\to\operatorname{Lip}(Y_h)/\mathbb R\) that extend data at the three vertices. Then the exact least operator norm is
\[
\boxed{\lambda_h=\frac{1+h^2}{\sqrt{1+h^2}+h(\sqrt{1+h^2}-1)}.}
\]
The minimum is attained simultaneously at **all three** edge midpoints by one positive (convex-combination) operator. Thus the same formula is the relative projection constant \(\lambda(\mathcal F(X_h),\mathcal F(Y_h))\) of the corresponding real Lipschitz-free spaces. The construction, using real scalar coefficients, also has operator norm at most \(\lambda_h\) for functions with values in any real Banach space. Scalar functions prove optimality of that universal upper bound.

The apex angle at \(C\) is at least \(\pi/2\), so the interval \(0<h\le1\) describes **every nondegenerate obtuse or right isosceles Euclidean triangle up to similarity**. At the right-isosceles endpoint,
\[
\lambda_1=\frac{2}{2\sqrt2-1}=1.093836321356054\ldots.
\]
By contrast, conventional affine midpoint averaging on all three edges has exact six-point extension norm \(\sqrt{1+h^2}/h\), which diverges as \(h\downarrow0\); the optimal norm instead converges to \(1\). This gives a sharp, uniformly stable positive replacement on increasingly flat isosceles cells.

## Assumptions and scope
All domain distances are ordinary planar Euclidean chord distances, **not** intrinsic graph-path distances. The functions are real valued and Lipschitz seminorms are quotiented by constants. A linear extension is required to respect constants (equivalently, to be a map on these quotients), but its vertex coefficients are otherwise unrestricted, including signed coefficients. The minimization is over all such linear operators, not merely positive or symmetry-equivariant ones. Scale invariance extends the result to all similar configurations, but the formulas assume half-base length one. Let
\[
L=\sqrt{1+h^2},\qquad D=L+h(L-1),\qquad
p=\frac{Lh}{2D},\qquad\lambda=\frac{L^2}{D}.
\]
For \(0<h\le1\), \(1<L\le\sqrt2\), \(D>0\), \(0<p<1/2\), and \(\lambda>1\). The optimal operator is
\[
(Tf)(A)=f(A),\quad(Tf)(B)=f(B),\quad(Tf)(C)=f(C),
\]
\[
\boxed{(Tf)(M)=p f(A)+p f(B)+(1-2p)f(C),}\quad
(Tf)(U)=\frac{f(A)+f(C)}2,\quad
(Tf)(V)=\frac{f(B)+f(C)}2.
\]
The coefficients in every row are nonnegative and sum to one.

## Proof
**1. Unrestricted lower bound.** Reflect the plane in the vertical axis, interchanging \(A,B\) and \(U,V\) while fixing \(C,M\). For any real-linear constant-preserving extension \(S\), conjugation by this reflection produces another extension of the same norm. Averaging the two gives a reflection-equivariant extension with no larger norm. Its value at the fixed point \(M\) must have the form
\[
(Sf)(M)=q[f(A)+f(B)]+(1-2q)f(C)
\]
for some unrestricted \(q\in\mathbb R\). The coefficient sum is one because constants are preserved.

First take the admissible one-Lipschitz vertex data \(f(A)=f(B)=L\), \(f(C)=0\). Since \(d(C,M)=h\), its extension forces the norm to be at least \(2L|q|/h\). Next take \(f(A)=0\), \(f(B)=2\), \(f(C)=L\). These data are one-Lipschitz: the three source distances are \(2,L,L\), and \(|2-L|\le L\) follows from \(L\ge1\). Since \(d(A,M)=1\), the norm is at least \(|L-2(L-1)q|\). Therefore every extension satisfies
\[
\|S\|\ge \max\left\{\frac{2L|q|}{h},\,|L-2(L-1)q|\right\}.
\]
Define \(q_*=Lh/(2D)\). The two unsigned positive branches agree there:
\[
\frac{2Lq_*}{h}=L-2(L-1)q_*=\frac{L^2}{D}=\lambda.
\]
For \(q\le q_*\), the second absolute-value term is at least \(\lambda\); for \(q\ge q_*\), the first term is at least \(\lambda\). This includes negative \(q\) and proves \(\|S\|\ge\lambda\) without any positivity assumption.

**2. Construction and all fifteen pairs.** The displayed operator is constant-preserving and positive since
\[
1-2p=\frac{D-Lh}{D}=\frac{L-h}{D}>0.
\]
Suppose \(\operatorname{Lip}(f)\le1\). On the three old-vertex pairs, the same bound holds unchanged. The pairs \((A,U),(C,U),(B,V),(C,V)\) satisfy the bound \(1\) exactly by edge averaging. The pair \((U,V)\) satisfies \(|Tf(U)-Tf(V)|=|f(A)-f(B)|/2\le1=d(U,V)\).

For \((M,U)\), expand relative to \(f(C)\):
\[
Tf(M)-Tf(U)=(p-1/2)[f(A)-f(C)]+p[f(B)-f(C)].
\]
Since \(0<p<1/2\), its absolute value is at most \(((1/2-p)+p)L=L/2=d(M,U)\). Reflection gives the same estimate for \((M,V)\).

For the pairs \((A,M)\) and \((B,M)\), positivity and the source Lipschitz conditions give
\[
|Tf(M)-f(A)|\le 2p+(1-2p)L
=L-2(L-1)p=\lambda,
\]
where \(d(A,M)=d(B,M)=1\). For \((C,M)\),
\[
|Tf(M)-f(C)|\le p|f(A)-f(C)|+p|f(B)-f(C)|\le2pL=\lambda h.
\]
These cover all pairs except \((B,U)\) and \((A,V)\). For them the source inequalities give
\[
\frac{|Tf(U)-f(B)|}{d(B,U)}\le
R:=\frac{2+L}{\sqrt{9+h^2}}=\frac{2+L}{\sqrt{L^2+8}},
\]
with the reflected bound for \((A,V)\).

**3. Uniform bound for the remaining pairs.** Direct algebra gives
\[
\lambda-1=(L-1)\frac{L-h}{D},\quad
R-1=(L-1)\frac{4}{\sqrt{L^2+8}\,[L+2+\sqrt{L^2+8}]}.
\]
For \(0<h\le1\), the bounds \(L-h\ge\sqrt2-1\), \(D\le2\sqrt2-1\), and \(L\ge1\) show
\[
\frac{L-h}{D}\ge\frac{\sqrt2-1}{2\sqrt2-1}
>\frac29\ge
\frac{4}{\sqrt{L^2+8}\,[L+2+\sqrt{L^2+8}]}.
\]
The strict middle comparison is exactly \(5\sqrt2>7\). Hence \(R<\lambda\). All fifteen unordered pairs now obey \(\operatorname{Lip}(Tf)\le\lambda\operatorname{Lip}(f)\). Combining this upper bound with step 1 proves optimality and attainment. The two vertex data in step 1 attain the bound on \((C,M)\) and \((A,M)\) for the constructed operator.

**4. Ordinary affine interpolation comparison.** The usual edge-midpoint rule replaces the displayed formula for \(M\) by \([f(A)+f(B)]/2\). The witness \(f(A)=f(B)=L,\ f(C)=0\) produces ratio \(L/h\) on \((C,M)\). All other pairs have ratio at most \(\max\{1,R\}\le L/h\): the estimates above remain valid with \(p=1/2\), and \(R\le\lambda<L/h\), where
\[
\frac{L}{h}-\lambda=\frac{L(L-h)}{hD}>0.
\]
Thus its exact six-point norm is \(L/h\). As \(h\downarrow0\), \(\lambda\to1\) while \(L/h\to\infty\).

**5. Free-space and Banach-valued interpretation.** Finite real Lipschitz spaces modulo constants are dual to their Lipschitz-free spaces. The standard duality between linear extensions and projections gives the stated relative projection constant (see Basso, arXiv:2104.14238, Eq. (1.6)). Every inequality in steps 2–3 uses only a triangle inequality, so the displayed positive weighted formula also bounds extensions of arbitrary real Banach-valued data by \(\lambda\). Scalar data obstruct any smaller uniform constant over all target Banach spaces. \(\square\)

## Verification
An independently executable standard-library script `verify_midpoint.py` enumerates the six extreme real Lipschitz potentials on the three old vertices (anchored at \(f(A)=0\)) and checks every one of the fifteen unordered pairs of new points. It uses 70-digit Decimal arithmetic at 124 rational heights, including the right-angle endpoint and two near-degenerate cases. This yields 11,160 finite checks and separately checks both analytic equality witnesses. The printed success marker is `FINITE_EXTREME_CHECK_OK`. The proof above, not the finite sample, establishes the continuum theorem, boundary, and sharpness among all linear extensions.

## Relationship to prior work
Bruè, Di Marino and Stra (2018) construct linear Lipschitz extensions via random projections under doubling hypotheses. Their Theorem 4.1 supplies broad existence and quantitative bounds, not this exact six-point geometry or its sharp positive weights. Basso (2021), Section 1 and Section 5, relates finite Lipschitz extension moduli to relative projection constants and linear programs; his results provide the framework but do not evaluate the indicated obtuse isosceles family.

The earlier *The sharp Euclidean triangle constant for barycentric Lipschitz-free \(p\)-interpolation* studies the **fixed affine barycentric map on an entire triangle**, not minimum-norm interpolation on six discrete points. At \(p=1\) its constant for the apex angle agrees with the conventional affine value \(L/h\) derived here. It does not imply the strictly smaller optimal discrete constant \(\lambda_h\). Existing symmetry-specific results on equilateral simplices and regular polygons with edge midpoints concern different vertex metrics; their formulas do not specialize to these non-equilateral obtuse triangles.

## Limitations
The exact formula is asserted only for Euclidean obtuse or right **isosceles** triangles and their three edge midpoints, not acute isosceles triangles, arbitrary scalene triangles, full continuous triangular interiors, or globally patched triangulations. The universal Banach-valued upper bound is proved for the explicit coefficientwise operator; no optimality claim is made for each individual Banach target independently. The originality comparison leaves residual risk from less-indexed exact finite-metric interpolation literature. Independent mathematical audit has not been performed.

## References
- E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533, first public 23 January 2018; especially Sections 3–4.
- G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238, first public 29 April 2021; Sections 1 and 5.
- *The sharp Euclidean triangle constant for barycentric Lipschitz-free \(p\)-interpolation*, publicly accessible published-finding corpus mathematics record, 11 October 2026, identifier `2026/10/11/SCOPE-the-sharp-euclidean-triangle-constant-for-barycentric-lipschitz--f5c526629bea`; inspected RESULT.md.
