# Sharp \(L^\infty\) projection norms and norming vertices for complete-split metric graphs

## Finding
Let \(m,k\ge2\) be integers and let \(G_{m,k}=\overline{K_m}\vee K_k\) be the complete split graph, with every edge realized as a unit interval and endowed with arclength measure. Let \(S_{m,k}\) be the space of continuous real functions that are affine on each edge and let \(P_{m,k}\) denote the arclength-\(L^2\) orthogonal projector onto this space. Then
\[
\boxed{\|P_{m,k}\|_{L^\infty\to L^\infty}=\frac{7m^2+26mk+24k^2-23m-44k+20}{3(m+2k-2)(m+2k-1)}.}
\]
All, and only, the \(m\) independent-class vertices are norming evaluation locations. Thus a single explicit sign choice of the reproducing kernel at any such vertex attains the operator norm. The sharp negative excursion of \(P_{m,k}f\), over measurable \(0\le f\le1\), is \((\|P_{m,k}\|-1)/2\); a maximizing input is the indicator of the negative part of a norming vertex kernel.

There is an exact threshold:
\[
\|P_{m,k}\|>2\quad\Longleftrightarrow\quad m\ge4
\qquad(m,k\ge2).
\]
For each fixed \(k\), the norm tends to \(7/3\) as \(m\to\infty\); for each fixed \(m\), it tends to \(2\) as \(k\to\infty\). In particular, \(7/3\) is the supremum of these norms over all such complete-split graphs, but is not attained by a finite pair.

## Assumptions and scope
The graph is simple and finite. Its first class \(I\) consists of \(m\) pairwise nonadjacent vertices, and its second class \(C\) is a \(k\)-vertex clique; every vertex of \(I\) is adjacent to every vertex of \(C\). Edge lengths are one, edge densities are one, and vertices carry zero arclength mass. \(L^\infty\) is the essential-supremum norm on the disjoint edge interiors, with continuous spline representatives at vertices. The projection is the real orthogonal projection of \(L^2\) onto \(S_{m,k}\), extended by its finite-rank kernel to \(L^\infty\). No nonunit edge weights or higher polynomial degrees are included.

## Proof
**Mass-matrix reduction.** Write \(\varphi_v\) for the nodal hat at vertex \(v\). For every edge \(uv\), direct integration gives diagonal mass contributions \(1/3\) at both endpoints and off-diagonal contributions \(1/6\). Hence, with \(D\) the degree diagonal and \(A\) the adjacency matrix, \(6M=2D+A\). Set \(L=m+2k-2\) and \(a=2m+2k-3\). In the order \(I,C\),
\[
6M=B=\begin{pmatrix}2k\,\mathrm{Id}_m&\mathbf1_m\mathbf1_k^{\mathsf T}\\
\mathbf1_k\mathbf1_m^{\mathsf T}&a\,\mathrm{Id}_k+\mathbf1_k\mathbf1_k^{\mathsf T}\end{pmatrix}.
\]
The matrix is positive definite because \(M\) is the Gram matrix of independent nodal hats. For a vertex \(z\), the evaluation kernel is
\[
K_z(t)=\sum_v (M^{-1})_{vz}\varphi_v(t).
\]
Its operator evaluation norm is the exact \(L^1\) kernel norm \(R_z=\int_G|K_z|\,ds\). Since every projected function is affine on every edge, its global supremum is attained at a graph vertex; therefore \(\|P\|=\max_z R_z\).

**Inverting the two-class mass matrix.** Splitting each class into its constant and sum-zero eigenspaces, or multiplying the displayed matrix directly, shows that for \(z\in I\), the coefficients \((M^{-1})_{vz}\) equal
\[
\frac{3L+1}{kL}\ (v=z),\qquad \frac1{kL}\ (v\in I\setminus\{z\}),\qquad -\frac2{kL}\ (v\in C).
\]
For \(z\in C\), all independent-class coefficients equal \(u=-2/(kL)\); the coefficient at \(z\) is \(v=4/(kL)+6(k-1)/(ka)\); and the other clique coefficients equal \(w=2(m-2k)/(kaL)\). These formulas are exactly verifiable by multiplication by \(B\), remembering the factor \(6\) in \(M^{-1}=6B^{-1}\). Note \(u<0<v\) and \(\operatorname{sign}(w)=\operatorname{sign}(m-2k)\).

**Exact kernel integrals.** For endpoint values \(s,t\), put
\[
J(s,t)=\int_0^1|(1-x)s+xt|\,dx=
\begin{cases}(|s|+|t|)/2,&st\ge0,\\
(s^2+t^2)/(2|s-t|),&st<0.
\end{cases}
\]
The independent-class vertex norm is
\[
R_I=kJ\left(\frac{3L+1}{kL},-\frac2{kL}\right)
+k(m-1)J\left(\frac1{kL},-\frac2{kL}\right)
+\binom k2\frac2{kL},
\]
which simplifies exactly to the boxed expression. For a clique vertex,
\[
R_C=mJ(v,u)+m(k-1)J(w,u)+(k-1)J(v,w)+\binom{k-1}2|w|.
\]
All clique vertex evaluations are equal by symmetry.

**Strict comparison, including both sign branches.** In the range \(m\le2k\), substituting \(w\le0\) into the latter formula and clearing positive factors yields
\[
R_I-R_C=\frac{2(m-1)Q_-(m-2,k-2)}{3k^2L^2(L+1)a\,[kL+m-1]},
\]
where the following polynomial has strictly positive coefficients:
\[
\begin{aligned}
Q_-(x,y)={}&x^4(y^3+10y^2+27y+22)\\
&+x^3(7y^4+79y^3+303y^2+488y+285)\\
&+x^2(18y^5+223y^4+1079y^3+2551y^2+2955y+1351)\\
&+x(20y^6+264y^5+1506y^4+4641y^3+8039y^2+7372y+2796)\\
&+8y^7+108y^6+688y^5+2590y^4+6014y^3+8424y^2+6516y+2140.
\end{aligned}
\]
When \(m>2k\), write \(x=m-2k>0\), \(y=k-2\ge0\). The same evaluation gives
\[
R_I-R_C=\frac{2Q_+(x,y)}{3(m-1)L(L+1)[kL+m-1]},
\]
where
\[
\begin{aligned}
Q_+(x,y)={}&2x^4+x^3(y^2+27y+37)\\
&+x^2(10y^3+146y^2+362y+248)\\
&+x(32y^4+362y^3+1179y^2+1526y+696)\\
&+32y^5+328y^4+1236y^3+2218y^2+1929y+657.
\end{aligned}
\]
The expressions follow by rational simplification of the displayed \(J\)-sum; they can be checked independently using the included exact-arithmetic script. Every denominator is positive for \(m,k\ge2\), and each numerator is strictly positive on its domain. Therefore \(R_I>R_C\) for all allowed parameters. Every edge has at least one clique endpoint; at an interior point its kernel is a strict convex combination of endpoint kernels, so its evaluation norm is strictly below \(R_I\). Hence the only norming locations are the independent-class vertices.

**Threshold, defect and limits.** Direct subtraction yields
\[
R_I-2=\frac{m^2+2km-5m-8k+8}{3L(L+1)}.
\]
For \(m=2\) the numerator equals \(-4k+2<0\); for \(m=3\) it is \(-2k+2<0\); for \(m\ge4\) it equals \(2k(m-4)+(m-1)(m-4)+4\), which is positive. Constants belong to the range, hence \(\int_GK_z\,ds=1\) at every vertex. For \(0\le f\le1\), the smallest value \(P f(z)\) is exactly \(-\int_{K_z<0}|K_z|=-(R_z-1)/2\). Maximizing this over vertices gives the defect; affine interpolation cannot create a more negative value in an edge interior. For the supremum norm, choose \(f=\mathrm{sgn}(K_z)\) at a norming vertex. Dividing the norm formula by the leading homogeneous terms gives the asserted two one-parameter limits. The exact norm is strictly below \(7/3\) at finite parameters because
\[
\frac73-R_I=\frac{2(2k^2+km+k+m-3)}{3L(L+1)}>0,
\]
with the last identity checked by direct expansion.

## Verification
The included standalone script `verify_split_spline.py` (SymPy) constructs and inverts the complete finite-element mass matrices with rational arithmetic for 72 parameter pairs, integrates the resulting signed affine kernels exactly, and independently confirms the closed-form expression and the strict clique–independent comparison. It additionally forms the symbolic rational difference in each sign regime, expands its numerator after shifting parameters to nonnegative coordinates, and checks that all polynomial coefficients are positive. These latter identities provide all-parameter algebraic certificates, not a finite-size argument. The exact displayed formulas and polynomial coefficients are sufficient to verify the universal proof without running software. Run `python verify_split_spline.py` with SymPy 1.10 or later.

## Relationship to prior work
Uniform \(L^\infty\) stability of the \(L^2\) spline projector was studied by Shadrin, proving de Boor's conjecture for intervals, and his discussion of finite-element projector bounds includes the distinction between spline and general element spaces. That result does not determine the exact norm on a branching metric graph or identify its norming vertices. Kayumov analyzed exact and uniform spline projector norms on intervals, not branching metric graphs. The finite-element mass-matrix literature, including Huang, Kamenski and Lang, describes the requisite matrices, but addresses different questions such as explicit time-step stability. Boman investigated weighted \(L^p\) estimates on finite-element spaces, rather than the exact complete-split graph formula in the accessible abstract; full-text overlap with that paper was not established. Exact projector formulas on balanced multipartite graphs, complete bipartite graphs and windmill graphs are related but do not imply the split-graph result because the additional clique edges change the Gram matrix and its inverse. This comparison is about mathematical implication, not merely different titles.

## Limitations
The equality cases are asserted for the **locations** of operator norming evaluations, not as a uniqueness classification of all extremizing input functions (which may be altered on zero sets of the evaluation kernel). All edge lengths and densities are uniform. This is an exact formula for one particular finite-dimensional orthogonal projector, not the least norm among arbitrary projections onto the spline subspace. The claim does not address general chordal graphs, arbitrary part sizes, other target norms or higher-order splines. Overlap in not fully accessible historical finite-element literature remains possible. The independent scientific audit is not performed.

## References
1. A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline-projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, preprint at https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/spn0.pdf (especially theorem I and section 4.1.2).
2. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418v1, first public August 30, 2004, https://arxiv.org/abs/math/0408418 (abstract, introduction and linear-spline background inspected; results concern intervals rather than complete-split metric graphs).
3. W. Huang, L. Kamenski and J. Lang, *Stability of explicit one-step methods for P1-finite element approximation of linear diffusion equations on anisotropic meshes*, arXiv:1602.08055v1, first public February 25, 2016, https://arxiv.org/abs/1602.08055 .
4. M. Boman, *Estimates for the \(L^2\)-projection onto continuous finite element spaces in a weighted \(L^p\)-norm*, BIT Numerical Mathematics (2006), DOI 10.1007/s10543-006-0062-3 (abstract consulted; full text not available for close reading).
