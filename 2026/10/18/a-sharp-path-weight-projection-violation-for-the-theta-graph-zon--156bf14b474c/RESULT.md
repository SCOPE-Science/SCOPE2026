# A sharp path-weight projection violation for the theta-graph zonotope

## Finding
Let \(H\) be the graph on vertices \(\{0,1,2,3,4,5\}\) with edges \(03,04,05,12,13,15,24\). It is a theta graph whose three internally disjoint paths from \(0\) to \(1\) have lengths \(2,2,3\). For arbitrary positive real numbers \(a,b,c\), weight the two edges on the path \(0-3-1\) by \(a\), the two edges on \(0-5-1\) by \(b\), and the three edges on \(0-4-2-1\) by \(c\). Use the five-dimensional reduced incidence realization defined below, and fix orthonormal projection directions
\[
 u=(1,-1,0,0,0)/\sqrt2,\qquad v=(0,0,1,-1,1)/\sqrt3.
\]
Write \(Z=Z(a,b,c)\) for the resulting full-dimensional zonotope and \(P_L\) for orthogonal projection onto the linear subspace \(L\). Its normalized two-direction projection ratio has the exact formula
\[
 \mathcal R(a,b,c)
 =\frac{\operatorname{Vol}_5(Z)\operatorname{Vol}_3(P_{\{u,v\}^\perp}Z)}
 {\operatorname{Vol}_4(P_{u^\perp}Z)\operatorname{Vol}_4(P_{v^\perp}Z)}
 =1+\frac{4abc}{3H(a,b,c)},
\]
where
\[
 H(a,b,c)=8ab(a+b)+3c(a+b)^2+4abc+2c^2(a+b).
\]
For **every** \(a,b,c>0\), the putative log-submodular projection inequality \(\mathcal R\le1\) is strictly reversed. More precisely, throughout this entire path-constant positive-weight class,
\[
 \boxed{1<\mathcal R(a,b,c)\le\frac{25}{24}},
\]
with equality in the upper bound **if and only if** \(a=b\) and \(c=2a\). The lower endpoint is an unattained infimum. In particular, the equal-weight instance gives \(\mathcal R(1,1,1)=28/27\), while \(\mathcal R(1,1,2)=25/24\).

## Assumptions and scope
The ambient Euclidean space is \(\mathbb R^5\) with the standard inner product and the five rows indexed by graph vertices \(0,1,2,3,4\); graph vertex \(5\) is the deleted incidence row. The seven columns, ordered as \(03,04,05,12,13,15,24\), are those of
\[
 A=\begin{pmatrix}
 1&1&1&0&0&0&0\\
 0&0&0&1&1&1&0\\
 0&0&0&-1&0&0&1\\
 -1&0&0&0&-1&0&0\\
 0&-1&0&0&0&0&-1
 \end{pmatrix}.
\]
If its columns are denoted \(g_1,\ldots,g_7\), define
\[
 (w_1,\ldots,w_7)=(a,c,b,c,a,b,c),\qquad
 Z(a,b,c)=\sum_{j=1}^{7}[0,w_jg_j].
\]
All weights are strictly positive, so the column matroid and full rank are unchanged. The claim fixes both the graph embedding and the two projection directions. It is **not** an optimum over arbitrary projections, arbitrary edge-by-edge weights, all graphs, or all zonoids.

## Proof
**1. Projection determinant identities.** For any spanning vectors \(z_1,\ldots,z_m\) in \(\mathbb R^d\), the volume of their zonotope is the sum of absolute maximal minors. If \(u\) is a unit vector, the \((d-1)\)-dimensional projected volume onto \(u^\perp\) is the sum of \(\left|\det(u,z_{i_1},\ldots,z_{i_{d-1}})\right|\); for an orthonormal pair \(u,v\), the analogous sum with \(u,v\) inserted gives the \((d-2)\)-dimensional projected volume. These formulas follow by applying the zonotope volume formula to the orthogonal projection of every generator, in an oriented orthonormal basis of the target subspace.

Put \(x=(1,-1,0,0,0)\) and \(y=(0,0,1,-1,1)\). They are perpendicular, with norms \(\sqrt2\) and \(\sqrt3\). For \(I\subseteq\{1,\ldots,7\}\), write \(A_I\) for the corresponding ordered column submatrix. Introduce the **unnormalized** determinant sums
\[
 \begin{split}
 V&=\sum_{|I|=5}\bigl|\det(A_I)\bigr|\prod_{j\in I}w_j,\\
 P&=\sum_{|I|=4}\bigl|\det(x,A_I)\bigr|\prod_{j\in I}w_j,\\
 Q&=\sum_{|I|=4}\bigl|\det(y,A_I)\bigr|\prod_{j\in I}w_j,\\
 W&=\sum_{|I|=3}\bigl|\det(x,y,A_I)\bigr|\prod_{j\in I}w_j.
 \end{split}
\]
Thus \(\operatorname{Vol}_5(Z)=V\), \(\operatorname{Vol}_4(P_{u^\perp}Z)=P/\sqrt2\), \(\operatorname{Vol}_4(P_{v^\perp}Z)=Q/\sqrt3\), and \(\operatorname{Vol}_3(P_{\{u,v\}^\perp}Z)=W/\sqrt6\). In particular, \(\mathcal R=VW/(PQ)\).

**2. Exhaustive coefficient calculation.** The determinant sums above involve, respectively, \(\binom75=21\), \(\binom74=35\), \(35\), and \(\binom73=35\) explicitly specified integer determinants of size five. Direct integer expansion gives the complete four polynomials
\[
\begin{aligned}
 V&=4abc^3+6ab^2c^2+6a^2bc^2=2abc^2(3a+3b+2c),\\
 P&=12abc^2,\\
 Q&=c\bigl(8a^2b+3a^2c+8ab^2+10abc+2ac^2+3b^2c+2bc^2\bigr)=cH(a,b,c),\\
 W&=6bc^2+6ac^2+16abc=2c(8ab+3ac+3bc).
\end{aligned}
\]
For example, the nonzero unweighted maximal determinants of \(A\) have absolute value one and occur for exactly sixteen five-column choices. Their weighted spanning-tree sum gives \(V=2abc^2(3a+3b+2c)\). The complete coefficient dictionaries for all four sums are enumerated independently from the displayed matrix by `check_weighted_theta.py`; its procedure exhausts every subset and calculates each signed determinant through an exact integer Leibniz expansion (rather than sampling weight values). At unit weights these four sums are \((V,P,Q,W)=(16,12,36,28)\), agreeing with the published unweighted determinant table.

**3. Universal positive defect.** Expanding these polynomials and cancelling terms yields the exact identity
\[
 VW-PQ=16a^2b^2c^4.
\]
Every factor is strictly positive for the assumed domain. Since \(P,Q>0\), this proves the strict failure of the projection inequality and, after division, the rational expression for \(\mathcal R\).

**4. Sharp optimization and uniqueness.** Put \(s=a+b\), \(p=ab\). Then \(s,c>0\), \(0<p\le s^2/4\), and
\[
 \mathcal R-1=\frac{4cp}{3\bigl[(8s+4c)p+3cs^2+2c^2s\bigr]}.
\]
For fixed \(s,c\), this expression is strictly increasing in \(p\), since its denominator has a strictly positive part independent of \(p\). Therefore equality at its maximum demands \(p=s^2/4\), or equivalently \(a=b=d>0\). Setting \(t=c/d\) then gives
\[
 \mathcal R(d,d,td)-1=\frac{t}{3(t+2)^2},\qquad t>0.
\]
The derivative is \((2-t)/(3(t+2)^3)\), positive for \(t<2\) and negative for \(t>2\). Hence the global maximum is \(1/24\) at \(t=2\), and the equality condition is precisely \(a=b\), \(c=2a\). The expression tends to zero as \(t\) approaches either endpoint \(0\) or \(+\infty\), while remaining strictly positive at every finite positive triple; hence the stated lower infimum is one and is not attained.

## Verification
Run the standalone Python 3 standard-library checker from this directory with `python check_weighted_theta.py`. It enumerates **all** maximal minors for each of the four determinant sums, compares their complete monomial-coefficient dictionaries with the four displayed polynomials, checks the exact identity \(VW-PQ=16a^2b^2c^4\) coefficient-by-coefficient, and evaluates several positive integer triples with exact fractions, including \((1,1,1)\) and \((1,1,2)\). The continuum positivity and equality claims are proved by the preceding symbolic identities and elementary monotonicity argument, not by finite numerical tests. No external libraries or downloads are required.

## Relationship to prior work
Fradelizi, Hubard, Manui, Ndiaye, Wang and Zvavitch (arXiv:2608.12681v1, Section 3.4) introduced this exact theta graph, incidence realization and projection pair as a minimal-generator graphical counterexample, with equal edge weights and ratio \(28/27\). That value and their determinant-volume identity are **prior results**, not claimed as new. The new statement is the **complete positive path-constant three-weight law**, strict failure throughout this natural two-dimensional weight-moduli space, and the sharp ratio \(25/24\) with its unique optimizing proportions. The prior table gives total unweighted determinant counts but not their path-weight monomial decomposition.

Skorupinski (arXiv:2608.07702v1) investigates log-submodularity and unimodular generator systems; the positive projection theorem requiring unimodularity of the **augmented** generator configuration does not apply here, since the two appended projection vectors produce nonunit maximal minors even at the source's equal-weight case. The separately published four-dimensional directional phase-diagram example studies a different zonotope and varies a generator's direction, not the edge weights of this five-dimensional graphical theta example. None of these compared claims entails the present weighted identity or its sharp optimization.

## Limitations
This is a fixed-projection, path-constant positive-weight classification, not an upper bound for the projection ratio of all graphical zonotopes or even all individually weighted theta-graph embeddings. The chosen reduced incidence representation uses the ordinary Euclidean metric, which is not invariant under arbitrary graph-coordinate changes. At zero edge weight one may lose full dimension; only **limits** as weights degenerate are discussed. Priority is based on accessible literature and indexed findings; earlier equivalent calculations in unindexed sources cannot be ruled out. No independent external mathematical audit is asserted.

## References
1. M. Fradelizi, A. Hubard, A. Manui, C. S. Ndiaye, S. Wang, A. Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681v1, August 13, 2026, especially Section 3.4, https://arxiv.org/abs/2608.12681.
2. R. Skorupinski, *Zonoid volumes are not log-submodular*, arXiv:2608.07702v1, August 7, 2026, https://arxiv.org/abs/2608.07702.
3. *Exact two-parameter directional phase diagram for a zonotope log-submodularity counterexample*, published research note, October 2026, archival identifier `f4edcfe36776`.
