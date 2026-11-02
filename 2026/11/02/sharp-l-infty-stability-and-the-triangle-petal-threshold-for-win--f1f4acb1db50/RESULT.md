# Sharp \(L^\infty\) stability and the triangle-petal threshold for windmill metric-graph splines

## Finding
For integers \(s\ge2\) and \(k\ge1\), form the **windmill graph** \(H_{s,k}=K_1\vee\bigl(\bigsqcup_{j=1}^k K_s\bigr)\): \(k\) copies of \(K_{s+1}\) sharing precisely one hub vertex. Replace each edge by an interval of length one and use arclength measure. Let \(P_{s,k}\) be the real \(L^2\)-orthogonal projection onto the continuous functions affine on every edge.

Its exact, attained \(L^\infty\)-operator norm is \(\mathcal C_s(k)\), defined explicitly below by six rational terms. For \(k>1\), **exactly the non-hub vertices** are norming evaluation points; for \(k=1\), all vertices are norming.

The sharp threshold at amplification two is
\[
\|P_{s,k}\|_{L^\infty\to L^\infty}>2
\quad\Longleftrightarrow\quad s=2\ \text{and}\ k\ge9.
\]
For \(s\ge3\), every finite windmill projector has norm strictly less than two; for \(s=2\), its exact norm is
\[
\mathcal C_2(k)=\frac{3664k^3+348k^2-13k+1}{450k^2(4k+1)},
\]
which increases strictly in \(k\). The sharp supremum over all \(s\ge2\), \(k\ge1\) is
\[
\sup_{s\ge2,\,k\ge1}\|P_{s,k}\|_{L^\infty\to L^\infty}=\frac{458}{225},
\]
approached along growing bouquets of triangles but not attained by any finite windmill. In particular, a branched metric graph with **no degree-one vertices** can have projection amplification strictly exceeding two, whereas all windmills built from petals of size at least four remain strictly below two.

## Assumptions and scope
All graph edges have unit physical length and constant density one; there is one affine finite element per edge, no additional interior knots, and all vertex traces of projected functions agree at common vertices. Input functions are arbitrary real essentially bounded measurable functions on the disjoint edge interiors, with values at vertices irrelevant to their \(L^2\) classes. The output is continuous and its \(L^\infty\) norm equals its maximum over the graph vertices. Both parameters \(s,k\) are positive integers with \(s\ge2,k\ge1\). The topology is a bouquet of complete graphs, not an abstract discrete signal space or a two-dimensional filled simplicial complex.

For real numbers \(u,v\), define the absolute-affine integral
\[
J(u,v)=\int_0^1|(1-t)u+tv|\,dt
=\begin{cases}
(|u|+|v|)/2,&uv\ge0,\\
(u^2+v^2)/(2(|u|+|v|)),&uv<0.
\end{cases}
\]
Write
\[
\begin{aligned}
U&=\frac{2(3s-1)}{ks(2s-1)},&
H&=-\frac2{ks(2s-1)},\\
D&=\frac2{ks(2s-1)(3s-1)},&
A&=\frac{6(3s-2)}{(2s-1)(3s-1)}+D,\\
&&B&=-\frac6{(2s-1)(3s-1)}+D.
\end{aligned}
\]
Then the exact norm in the finding is
\[
\boxed{\mathcal C_s(k)=J(A,H)+(s-1)J(A,B)+(s-1)J(B,H)
+\binom{s-1}{2}|B|+s(k-1)J(D,H)+(k-1)\binom s2 D.}
\]
Every quantity on the right is an explicit rational number for the stated parameters, with no optimization or numerical integration remaining.

## Proof
**1. Nodal Gram inverse.** Let \(\phi_v\) be the hat function equal to one at vertex \(v\), zero at other vertices, and affine on every edge. Direct integration of the products of endpoint hats gives the Gram matrix \(G=(\langle\phi_u,\phi_v\rangle)\) satisfying
\[
6G=2\operatorname{diag}(\deg v)+\operatorname{Adj}(H_{s,k}).
\]
Order the hub first and the \(k\) sets of \(s\) outer vertices next. Every outer diagonal block of \(6G\) is \(C=(2s-1)I_s+\mathbf1\mathbf1^{\mathsf T}\), the hub diagonal is \(2ks\), and the hub-to-outer entries are one. The elementary inverse
\[
C^{-1}=\frac1{2s-1}I_s-\frac1{(2s-1)(3s-1)}\mathbf1\mathbf1^{\mathsf T}
\]
has row sum \(1/(3s-1)\). Its hub Schur complement is
\[
S=2ks-\frac{ks}{3s-1}=\frac{3ks(2s-1)}{3s-1}>0.
\]
Consequently the inverse Gram matrix \(Q=G^{-1}\) has precisely five entry types in its hub row or any outer row: hub-to-hub \(U\), hub-to-outer \(H\), an outer row at its own vertex \(A\), at the other \(s-1\) vertices of the same petal \(B\), and at every vertex of another petal \(D\). These are exactly the five rational expressions above. Their signs are \(U,A,D>0\) and \(H,B<0\) for all admissible parameters.

**2. Exact row norm and norming vertices.** At any vertex \(v\), the integral kernel representing the evaluation \((P_{s,k}f)(v)\) is \(K_v(x)=\sum_uQ_{vu}\phi_u(x)\). On an edge joining \(a,b\), it is affine with endpoint values \(Q_{va},Q_{vb}\). Thus the sharp vertex-evaluation norm is \(\int|K_v|=\sum_{ab\in E}J(Q_{va},Q_{vb})\), attained by the measurable input \(f=\operatorname{sgn}K_v\). Since projected functions are affine on each edge, the output maximum occurs at a vertex; since the absolute value of an affine combination of evaluation kernels is convex, no edge-interior evaluation can exceed the largest vertex row norm.

A hub row has \(ks\) hub-outer edges and \(k\binom s2\) within-petal edges. Its norm is
\[
\mathcal H_s=ksJ(U,H)+k\binom s2|H|
=\frac{12s^2-9s+2}{3s(2s-1)}.
\]
An outer row has one hub-to-self edge, \(s-1\) hub-to-petal-mate edges, \(s-1\) self-to-mate edges, \(\binom{s-1}{2}\) mate-to-mate edges, \(s(k-1)\) hub-to-remote edges and \((k-1)\binom s2\) remote-petal edges. Counting them gives exactly the displayed six-term formula for \(\mathcal C_s(k)\).

To compare rows for all parameters, put \(x=k-1\ge0\), \(y=s-2\ge0\) and
\[
T(s,k)=3k^2s^2(2s-1)(3s-1)^2(3ks-2k+1)>0.
\]
A direct rational expansion and cancellation gives
\[
\frac{T(s,k)(\mathcal C_s(k)-\mathcal H_s)}{k-1}
=x^2 D_2(y)+xD_1(y)+D_0(y)\qquad(k>1),
\]
where
\[
\begin{aligned}
D_2(y)&=2(y+2)(3y+4)(9y^3+51y^2+96y+58),\\
D_1(y)&=2(y+2)(3y+5)(18y^3+99y^2+171y+94),\\
D_0(y)&=2(3y+5)^2(3y^3+18y^2+33y+19).
\end{aligned}
\]
All three polynomials are strictly positive for \(y\ge0\). At \(k=1\) the row norms coincide by complete-graph symmetry. Thus the outer row is strictly largest exactly when \(k>1\), establishing the asserted norming vertices.

**3. The sharp threshold.** For \(s\ge3\), put \(x=k-1\ge0\), \(z=s-3\ge0\). Exact cancellation gives
\[
T(s,k)(2-\mathcal C_s(k))=x^3E_3(z)+x^2E_2(z)+xE_1(z)+E_0(z),
\]
with
\[
\begin{aligned}
E_3(z)&=(z+3)(3z+7)(9z^3+51z^2+78z+20),\\
E_2(z)&=9(z+2)^2(z+3)(3z+8)(5z+13),\\
E_1(z)&=(3z+8)^2(21z^3+159z^2+401z+337),\\
E_0(z)&=(z+3)(3z+7)(3z+8)^3.
\end{aligned}
\]
Each term is strictly positive. Hence \(\mathcal C_s(k)<2\) for all \(s\ge3,k\ge1\).

When \(s=2\), simplifying the same six-term expression instead yields
\[
\mathcal C_2(k)-2=\frac{64k^3-552k^2-13k+1}{450k^2(4k+1)}.
\]
The numerator is negative for integers \(1\le k\le8\) and positive for integers \(k\ge9\): its derivative \(192k^2-1104k-13\) is positive for \(k\ge6\), and direct substitution at \(k=8,9\) gives values \(-2663\) and \(1828\), respectively. For \(1\le k\le5\) the numerator is visibly at most \(64(5)k^2-552k^2-13k+1<0\). For \(k=6,7\), monotonicity from six to eight and negativity at eight suffice. This establishes the exact transition.

Finally,
\[
\frac{d}{dk}\mathcal C_2(k)=\frac{2272k^3+104k^2+k-2}{450k^3(4k+1)^2}>0\quad(k\ge1)
\]
and
\[
\frac{458}{225}-\mathcal C_2(k)=\frac{568k^2+13k-1}{450k^2(4k+1)}>0.
\]
The limit along positive integers \(k\to\infty\) is \(458/225\). All other petals satisfy \(\mathcal C_s(k)<2<458/225\), proving sharpness and nonattainment of the family supremum.

## Verification
The companion `verify_windmill.py` uses only the Python standard library and exact rational arithmetic. It separately builds and inverts the complete nodal Gram matrix for small graphs, reconstructs all evaluation-row norms without using the five-entry inverse formula, and tests the certificate identities and classifications over many integer parameter pairs. On this package, it passed **12,460 exact assertions**: 240 full-matrix/row checks, 7,332 rational-identity checks, and 4,888 threshold checks. The proof for unbounded integer parameters rests on the displayed inverse and positive-coefficient polynomial identities, not on extrapolating finite experiments.

Run: `python3 verify_windmill.py`.

## Relationship to prior work
Orthogonal spline-projection stability on an interval was studied by Kayumov (2004); his source uses interval partitions and second-order \(L\)-splines, not a junction graph. Oswald (2006) treats two-dimensional simplicial finite elements and recalls the interval bound of three; his counterexamples do not determine the present graph-bouquet constants. Arioli and Benzi (2017) give metric-graph finite-element mass-matrix formulas and numerical conditioning analysis, not sharp \(L^\infty\) norms of orthogonal projection on windmills. The present contribution is a topology-specific **exact norm**, together with the sharp distinction between triangular petals and larger clique petals.

## Limitations
Only complete-clique petals of a common size and common unit edge lengths/densities are treated. The formula does not address unequal petal sizes, weighted or subdivided edges, higher spline degrees, nonorthogonal transfer, or PDE semigroups. The originality comparison covers the identified primary literature and mathematical records but cannot exclude previously unindexed equivalent calculations. The finite-parameter checker is corroboration of an algebraic proof, not independent peer review.

## References
1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first publicly posted 2004-08-30. https://arxiv.org/abs/math/0408418
2. P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19. https://arxiv.org/abs/math/0611573
3. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, IMA Journal of Numerical Analysis 38 (2018), 1119–1163, first paper version publicly available by 2015; https://doi.org/10.1093/imanum/drx029 .
