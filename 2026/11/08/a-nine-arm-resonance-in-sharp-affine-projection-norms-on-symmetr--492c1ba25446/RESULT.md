# A nine-arm resonance in sharp affine projection norms on symmetric metric double stars

## Finding

Let \(d\ge2\) be an integer. Form a metric tree \(T_{d,t}\) from two vertices \(u,v\), an edge of length \(t>0\) between them, and exactly \(d\) disjoint pendant edges of length one attached to **each** of \(u\) and \(v\). Equip the edges with arclength measure, without atoms at vertices. Write \(P_{d,t}\) for the real \(L^2\)-orthogonal projection onto continuous functions that are affine on every edge. Its exact \(L^\infty\)-operator norm \(L_d(t)\) is given by the formula below. **Precisely the \(2d\) outer leaves are norming evaluation locations**; neither hub nor any edge-interior point is norming.

Put
\[
U=\frac{4(3d+4t)}{(d+2t)(3d+2t)},\qquad
V=\frac{8t}{(d+2t)(3d+2t)},\qquad
F(a,b)=\frac{a^2+b^2}{2(a+b)}\quad(a,b>0).
\]
Then
\[
\boxed{L_d(t)=F(3+U/4,U/2)+\frac{5(d-1)U}{24}
+\frac{5dV}{24}+tF(U/2,V/2).}
\]
For each fixed \(d\), the branch-length dependence undergoes an exact integer threshold:

* If \(2\le d\le8\), \(L_d(t)\) is **strictly increasing** for all \(t>0\), and \(L_d(t)<7/3\) for every finite \(t\).
* If \(d\ge9\), \(L_d(t)\) has **exactly one critical point on \((0,\infty)\)**. It is a strict global maximum. There is exactly one finite crossing \(t_*(d)>0\) of \(L_d(t)=7/3\); the norm is smaller than \(7/3\) before the crossing and larger afterwards. In particular this two-hub tree has an operator norm strictly above the sharp family-wide supremum \(7/3\) of unit-arm metric stars.

The endpoint and first-order large-bridge laws are
\[
\lim_{t\downarrow0}L_d(t)=\frac{7d+3}{3(d+1)},\qquad
\lim_{t\to\infty}L_d(t)=\frac73,\qquad
\lim_{t\to\infty}t\left(L_d(t)-\frac73\right)=\frac{d-8}{6}.
\]
At the borderline \(d=8\), the next asymptotic coefficient is
\[
\lim_{t\to\infty}t^2\left(L_8(t)-\frac73\right)=-\frac43.
\]

## Assumptions and scope

The integer degree \(d\) may be any \(d\ge2\), and the central-edge length \(t\) is an arbitrary positive real. The vertex set has \(2d+2\) elements, with two hubs and \(2d\) leaves. All pendant lengths and all edge densities are one. The \(L^2\) and \(L^\infty\) spaces are real, and both norms use arclength measure. The bounded operator \(P_{d,t}\) acts on measurable essentially bounded input functions and has values in the finite-dimensional continuous affine spline space. The norm is attained by the sign of a leaf evaluation kernel (an admissible real \(L^\infty\) input).

## Proof

**1. Invert the nodal Gram matrix.** Let \(\phi_z\) be the continuous hat function for vertex \(z\), taking value one at \(z\) and zero at the other vertices. An edge of length \(\ell\) contributes \(\ell\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}/6\) to the corresponding \(L^2\) Gram matrix \(M\). In the vertex order \((u,v,\text{leaves at }u,\text{leaves at }v)\), the matrix \(6M\) has hub diagonal \(2(d+t)\), central hub off-diagonal \(t\), leaf diagonals \(2\), and hub-leaf off-diagonals \(1\). Eliminating the leaf block gives the two-hub Schur complement
\[
S=\begin{pmatrix}h&t\\t&h\end{pmatrix},\qquad h=\frac{3d}{2}+2t.
\]
Its inverse has diagonal \(h/(h^2-t^2)\) and off-diagonal \(-t/(h^2-t^2)\). Therefore the **actual** hub-hub block of \(M^{-1}\) is \(\begin{psmallmatrix}U&-V\\-V&U\end{psmallmatrix}\), with \(U,V\) as above. The row of \(M^{-1}\) at a specified outer leaf at \(u\) has the following nodal entries: \(-U/2\) at \(u\), \(+V/2\) at \(v\), \(3+U/4\) at that leaf, \(U/4\) at each other leaf at \(u\), and \(-V/4\) at every leaf at \(v\). The hub row at \(u\) has \(U,-V,-U/2,+V/2\) at those corresponding classes. These identities follow directly from block inversion and hold for **all** \(d\ge2,t>0\).

**2. Integrate the signed kernels exactly.** The evaluation kernel at a vertex \(z\) is \(K_z(y)=\sum_w(M^{-1})_{zw}\phi_w(y)\). On an edge of length \(\ell\), its endpoint coefficients \(a,b\) give integral \(\ell(|a|+|b|)/2\) when they have the same sign. When they have opposite signs with positive magnitudes \(a,b\), the integral is \(\ell F(a,b)\). All adjacent coefficients in the above rows have opposite signs. Summing the \(2d+1\) edges gives the leaf norm \(L_d(t)\) displayed in the Finding and the hub norm
\[
H_d(t)=\frac{5d(U+V)}{12}+tF(U,V).
\]
For any vertex \(z\), choosing the measurable input \(f=\operatorname{sgn}K_z\) attains its evaluation norm. Since an interior point of each edge evaluates as a **strict convex combination** of its two endpoint evaluation functionals, and those endpoint kernels have opposite signs on a positive-length initial subsegment of the same edge, an edge-interior evaluation has strictly smaller norm than the larger endpoint norm.

**3. All leaves, not the hubs, are norming.** Set
\[
D_0=3(d+2t)^2(3d+2t)(3d^2+8dt+3d+4t^2+4t)>0,
\qquad x=d-2\ge0.
\]
Exact algebra in the preceding formulas yields
\[
L_d(t)-H_d(t)=\frac{2Q(x,t)}{D_0},
\]
where the positive-coefficient certificate is
\[
\begin{aligned}
Q(x,t)={}&9x^5+81x^4+288x^3+504x^2+432x+144\\
&+t(60x^4+420x^3+1080x^2+1200x+480)\\
&+t^2(162x^3+842x^2+1424x+776)\\
&+t^3(216x^2+752x+640)+t^4(136x+240)+32t^5.
\end{aligned}
\]
Every coefficient is strictly positive, giving \(L_d(t)>H_d(t)\) without an omitted parameter case. Reflection across the bridge makes every leaf equivalent and every hub equivalent, completing the location classification.

**4. The overshoot threshold is exactly nine leaves per hub.** Another exact algebraic identity is
\[
L_d(t)-\frac73=\frac{4R_d(t)}{D_0},
\]
where
\[
\begin{aligned}
R_d(t)={}&4(d-8)t^4+4d(3d-25)t^3+d^2(11d-109)t^2\\
&+3d^3(d-17)t-9d^4.
\end{aligned}
\]
For the eight-or-fewer regime, every coefficient of this polynomial is nonpositive and its constant coefficient is negative: \(R_d(t)<0\) for \(2\le d\le8,t>0\). For \(d\ge9\), its coefficients in descending powers have exactly one sign change (zero coefficients ignored): the top two are positive, the constant is negative, and the remaining coefficients turn positive in descending order: the coefficient of \(t^2\) at \(d=10\) and that of \(t\) at \(d=18\). Descartes' rule of signs and \(R_d(0)<0\), \(R_d(t)\to+\infty\) imply a unique positive crossing.

**5. Unimodality in bridge length.** Differentiation gives \(L'_d(t)=C_d(t)/D_1\), where
\[
D_1=3(d+2t)^3(3d+2t)^2(3d^2+8dt+3d+4t^2+4t)^2>0
\]
and the derivative numerator is the explicit degree-seven polynomial
\[
\begin{aligned}
C_d(t)={}&-256(d-8)t^7-128d(11d-92)t^6\\
&-128d(23d^2-223d+2)t^5\\
&-64d^2(42d^2-601d+12)t^4\\
&-48d^3(11d^2-662d+15)t^3\\
&+24d^4(35d^2+682d-1)t^2\\
&+288d^5(2d^2+17d+1)t+108d^6(d^2+6d+1).
\end{aligned}
\]
For integer \(2\le d\le8\), all coefficients are nonnegative, and the constant is positive. For integer \(d\ge9\), their signs, read from highest to lowest degree and ignoring zeros, change exactly once, from negative to positive. In detail, the coefficients of powers seven and six are negative for \(d\ge9\); that of power five becomes negative at \(d=10\), that of power four at \(d=15\), and that of power three at \(d=61\). All coefficients of powers two, one and zero are positive. The claimed three transition integers follow by evaluating the factored quadratic polynomials at adjacent integers and noting their monotonicity after the relevant thresholds. Descartes' rule and \(C_d(0)>0\), \(C_d(t)\to-\infty\) give **one and only one** positive critical point for \(d\ge9\), with the derivative changing from positive to negative. This establishes the strict unique global maximum and the monotonicity regime.

**6. Endpoint limits.** Substituting \(t\downarrow0\) in the explicit norm formula gives \((7d+3)/[3(d+1)]\); comparison with the previously established sharp unit-arm star norm shows that this is the norm for one \(d\)-arm star, not for a collapsed single \(2d\)-arm star. Highest-degree terms give \(L_d(t)\to7/3\). The quartic in Step 4 gives \(t(L_d(t)-7/3)\to(d-8)/6\). At \(d=8\), its leading coefficient vanishes and the next order gives \(-4/3\) after multiplication by \(t^2\). No limiting statement is used as a substitute for the exact finite-parameter formulas.

## Verification

Run `python verify_double_star_projection.py` with the accompanying `requirements.txt`. The program checks, symbolically, the identity for \(L_d-H_d\) and all 21 positive coefficients in its \((d-2,t)\) certificate, the exact \(7/3\) crossing identity, and the entire derivative polynomial identity. It then independently constructs and inverts the full \((2d+2)\)-vertex rational Gram matrix at 35 combinations of degrees and rational bridge lengths and integrates the absolute kernels over **every edge** at **every vertex**. It verifies the resulting two evaluation norms against the formulas. Finite matrix tests alone cannot prove the infinite-parameter statements; Steps 1–6 give the universal argument.

## Relationship to prior work

The classical theory of \(L^\infty\) bounds for real \(L^2\)-spline orthoprojectors on intervals, including de Boor's question and Shadrin's result, supplies the approximation-theoretic context. Kayumov's public preprint, *Least-squares approximation by second-order L-splines* (arXiv:math/0408418, August 30, 2004), analyzes interval-generated exponential and trigonometric splines, not the branched metric-tree geometry here. Oswald's 2006 preprint provides an unbounded family of \(L^\infty\) projector norms on two-dimensional simplicial triangulations, rather than an exact constant on a one-dimensional metric tree. Boman's 2006 article investigates weighted \(L^p\) estimates for continuous finite-element projections; its accessible abstract does not give the present exact family formula. The prior exact weighted metric-star projection formula yields \((7d+3)/(3(d+1))\) for equal \(d\)-arm stars, but does not cover a tree with two distinct branching vertices coupled by a central edge. In particular the new \(d=9\) overshoot cannot follow merely from the star upper envelope \(7/3\). The comparison with Boman's unavailable full text is an unresolved coverage risk, not evidence of absence.

## Limitations

The result covers only symmetric double stars with unit, equally weighted pendant edges; it does not cover different leaf counts at the two hubs, variable edge densities, vertex atoms, higher-degree splines or complex-valued endpoint norms. It is a same-authority algebraic and analytical derivation, **not** an independently refereed theorem. A similar theorem could exist in differently indexed literature. Only the explicit first-order and boundary second-order limits above are asserted.

## References

1. Alexander Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first public version August 30, 2004. https://arxiv.org/abs/math/0408418
2. A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Mathematica **187** (2001), 59–137. https://doi.org/10.1007/BF02392832
3. Mats Boman, *Estimates for the \(L^2\)-projection onto continuous finite element spaces in a weighted \(L^p\)-norm*, BIT Numerical Mathematics **46** (2006), 249–260. https://doi.org/10.1007/s10543-006-0062-3
4. Peter Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first public version November 19, 2006. https://arxiv.org/abs/math/0611573
