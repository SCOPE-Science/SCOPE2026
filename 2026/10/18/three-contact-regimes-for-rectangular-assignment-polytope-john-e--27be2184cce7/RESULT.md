# Three contact regimes for rectangular assignment-polytope John ellipsoids

## Finding

Fix integers \(2\le m<n\) and \(1\le k<m\). Let \(P_{m,n,k}\) be the convex hull of all \(m\)-by-\(n\) zero-one matrices with exactly \(k\) ones, at most one in each row and column, equipped with the Frobenius Euclidean metric in its affine hull \(H_k=\{X:\sum_{ij}X_{ij}=k\}\). This has dimension \(d=mn-1\).

Define \(V_r=\mathbf1_r\mathbf1_r^{\mathsf T}/r\), \(U_r=I_r-V_r\), and, on matrices of total entry sum zero,
\[
P_R(Y)=U_mYV_n,\qquad P_C(Y)=V_mYU_n,\qquad P_I(Y)=U_mYU_n.
\]
The three operators are Frobenius-orthogonal projectors of ranks \(m-1\), \(n-1\), and \((m-1)(n-1)\). Set
\[
A=\frac{m-1}{mn},\quad B=\frac{n-1}{mn},\quad D=\frac{(m-1)(n-1)}{mn},\quad
s=\frac{k}{mn},\quad
U=\frac{(m-k)^2}{mn(m-1)},\quad
V=\frac{(n-k)^2}{mn(n-1)}.
\]
There is a unique positive \(q\) with
\[
A\min(q,U)+B\min(q,V)+Dq=s^2.
\]
Write \(\alpha=\min(q,U)\), \(\beta=\min(q,V)\) and \(C=s\mathbf1_m\mathbf1_n^{\mathsf T}\). The unique maximum-volume inscribed ellipsoid is
\[
\boxed{E_{m,n,k}=\left\{X\in H_k:\frac{\|P_R(X-C)\|_F^2}{\alpha}+\frac{\|P_C(X-C)\|_F^2}{\beta}+\frac{\|P_I(X-C)\|_F^2}{q}\le1\right\}.}
\]
Its squared principal semiaxes are \(\alpha\) with multiplicity \(m-1\), \(\beta\) with multiplicity \(n-1\), and \(q\) with multiplicity \((m-1)(n-1)\). Its exact intrinsic volume is
\[
\operatorname{Vol}_d(E_{m,n,k})=\frac{\pi^{d/2}}{\Gamma(1+d/2)}\,\alpha^{(m-1)/2}\beta^{(n-1)/2}q^{(m-1)(n-1)/2}.
\]
Every coordinate nonnegativity face contacts the ellipsoid; all row-cap faces contact exactly when \(q\ge U\), and all column-cap faces contact exactly when \(q\ge V\). No other facet contacts occur. For \(k=1\) the row and column inequalities are redundant and neither type contacts.

For \(m<n\), one has \(U<V\), so the formula exhibits three possible *strict* contact patterns: coordinate only, coordinate plus row, or all three types. Define
\[
q_0=\frac{k^2}{mn(mn-1)},\qquad q_1=\frac{2k-m}{mn(n-1)}.
\]
Then the exact piecewise evaluation is
\[
q=\begin{cases}
q_0,&k^2(m-1)\le(m-k)^2(mn-1),\\
q_1,&k^2(m-1)>(m-k)^2(mn-1)\ \text{and}\ 2k-m\le(n-k)^2,\\
\dfrac{k^2-(m-k)^2-(n-k)^2}{mn(m-1)(n-1)},&2k-m>(n-k)^2.
\end{cases}
\]
The third case necessarily implies the first threshold has been crossed. Boundary equalities activate the corresponding additional contact class. All three strict patterns occur: \((m,n,k)=(4,9,3)\) has coordinate only; \((4,5,3)\) has coordinate and row contacts; \((7,8,6)\) has all three types.

## Assumptions and scope

The restrictions \(m<n\) and \(k<m\) exclude the equal-side-length case and the lower-dimensional saturated matching regime. Matrices and ellipsoids are measured intrinsically in the affine hyperplane \(H_k\), not in the full ambient space. A "contact" means that the ellipsoid intersects the indicated supporting face; when \(k>1\), all coordinate, row-cap, and column-cap faces listed are facets. No claim is made here for arbitrary sparse bipartite graphs or for \(k=m\).

## Proof

**1. Polytope inequalities and symmetry.** The standard \(k\)-assignment polytope equality identifies
\[
P_{m,n,k}=\{X\in H_k:X_{ij}\ge0,\ \sum_jX_{ij}\le1,\ \sum_iX_{ij}\le1\}.
\]
The uniform matrix \(C\) satisfies every inequality strictly, hence the affine hull has dimension \(mn-1\). The maximum-volume inscribed ellipsoid is unique. Its image under arbitrary row and column permutations is another maximum-volume ellipsoid, so uniqueness makes the center equal to \(C\) and its positive shape operator commute with the group \(S_m\times S_n\). The orthogonal zero-sum representation decomposes into the three mutually inequivalent irreducible row, column, and interaction summands. Thus the shape operator must be \(\Sigma=\alpha P_R+\beta P_C+qP_I\) with positive scalars. This symmetry deduction concerns the *global* maximum, not merely the best symmetric candidate.

**2. Exact facet-support constraints.** For an ellipsoid with center \(C\) and shape \(\Sigma\), the maximum of a linear functional with affine normal \(z\) equals its value at \(C\) plus \(\sqrt{\langle z,\Sigma z\rangle_F}\). The affine projection of an entry normal \(E_{ij}\) is \(E_{ij}-\mathbf1_m\mathbf1_n^{\mathsf T}/(mn)\). The three squared projection norms are \(A,B,D\), while its coordinate slack is \(s\). Consequently all coordinate constraints together are equivalent to \(A\alpha+B\beta+Dq\le s^2\).

The affine row normal is \(\mathbf e_i\mathbf1_n^{\mathsf T}-\mathbf1_m\mathbf1_n^{\mathsf T}/m\). It lies entirely in the row summand, has squared norm \(n(m-1)/m\), and has slack \((m-k)/m\). Thus all row caps require \(\alpha\le U\). Similarly all column caps require \(\beta\le V\). No further constraints are needed by the displayed halfspace description. Each equality is equivalent to the corresponding supporting face contacting the ellipsoid, because the shape is positive definite. In particular the coordinate constraint becomes active at the optimum, as shown next.

**3. Global volume optimality.** Maximizing ellipsoid volume is equivalent to maximizing
\[
(m-1)\log\alpha+(n-1)\log\beta+(m-1)(n-1)\log q
\]
subject to the three scalar linear inequalities above and positivity. This objective is strictly concave, and its maximum exists and is unique because feasible shapes are bounded and the objective tends to minus infinity at zero eigenvalues. The coordinate-budget inequality is active since increasing \(q\) would otherwise increase the volume. The coefficients in the logarithmic objective equal \(mn\) times the coordinate-budget coefficients \(A,B,D\). Hence the Karush–Kuhn–Tucker equations yield equal uncapped eigenvalues and capped values \(\alpha=\min(q,U)\), \(\beta=\min(q,V)\). The remaining equation is precisely \(A\min(q,U)+B\min(q,V)+Dq=s^2\); its left side is strictly increasing from zero to infinity, proving existence and uniqueness. Strict concavity and the preceding global symmetry argument prove the stated ellipsoid is the unique John ellipsoid.

**4. Phase boundaries, spectra, and contact points.** Since \((x-k)^2/(x-1)\) is strictly increasing for integers \(x>k\), \(U<V\). Before the first cap, the equality budget gives \(q=q_0\); the test \(q_0\le U\) is the displayed first threshold. Once the row cap activates, solving \(AU+(B+D)q=s^2\) gives \(q=q_1\). Comparing \(q_1\) to \(V\) gives the second threshold \(2k-m\le(n-k)^2\). When both caps activate, the residual interaction eigenvalue is the third piecewise expression. Contact equivalences follow directly from the support equalities. Every coordinate inequality touches, since the budget is always active.

More explicitly, with \(z_{ij}\) the affine projected entry normal, the coordinate contact point is \(C-\Sigma z_{ij}/s\). When \(q\ge U\), the point \(C+\Sigma g_i/((m-k)/m)\) contacts the \(i\)-th row cap, where \(g_i\) is its affine normal from Step 2. When \(q\ge V\) the analogous formula with the column normal and slack \((n-k)/n\) gives column contacts. These points lie in the polytope because the entire ellipsoid does. Eigenvalue multiplicities yield the volume formula.

## Verification

The companion standalone standard-Python checker `verify.py` uses exact rational arithmetic. It separately assembles the row/column/interaction projections of each affine facet normal, checks their orthogonality and support variances, and verifies explicitly constructed contact points obey every assignment inequality. It also checks the water-filling equation and phase boundaries across thousands of rectangular parameter triples. The checker reports **8,318 exact parameter instances, 3,703 projected facet inequalities, and 2,851 explicit contact points**. These checks are finite corroboration; the proof above establishes all infinitely many instances.

## Relationship to prior work

Gill and Linusson's *The k-assignment polytope* (2009) supplies the exact rectangular halfspace description, facets, and one-skeleton combinatorics. Torres's *Normality of k-Matching Polytopes of Bipartite Graphs* (first arXiv version, 20 June 2023) establishes the corresponding bipartite fractional-matching equivalence and normality. Neither examined full text supplies this rectangular John ellipsoid or its three distinct facet-contact patterns. When the two side lengths are equal, row and column cap symmetries coincide; that symmetric subfamily does not determine the asymmetric row-only regime or the two distinct cap thresholds here. General convex-optimization formulations of inscribed ellipsoids likewise do not themselves state these explicit spectral and contact classifications.

## Limitations

The statement does not cover \(m=n\), \(k=m\), sparse bipartite edge sets, or non-Euclidean metrics. No claim is made of publication-priority certification; an equivalent characterization under optimal experimental design, transportation polytopes, or maximum-volume inscribed ellipsoid terminology could exist. Finite computational checks do not certify the infinite-family theorem independently.

## References

1. J. Gill and S. Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148–161, DOI: `10.1016/j.disopt.2008.10.003`. Author manuscript: https://www.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf .
2. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, first posted 20 June 2023. https://arxiv.org/html/2306.11910v1 .
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant on his 60th Birthday (1948), 187–204 (classical existence/uniqueness and extremal-ellipsoid theory).
