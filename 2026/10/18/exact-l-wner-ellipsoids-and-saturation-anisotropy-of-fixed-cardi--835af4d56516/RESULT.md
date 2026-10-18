# Exact Löwner ellipsoids and saturation anisotropy of fixed-cardinality assignment polytopes

## Finding
Let \(2\le p\le q\) and \(1\le k\le p\) be integers. Let \(P_{p,q,k}\) be the convex hull, in the Frobenius metric on \(\mathbb R^{p\times q}\), of all zero-one matrices having exactly \(k\) ones and at most one in each row and column. Its unique minimum-intrinsic-volume enclosing (Löwner) ellipsoid is computed explicitly below, including singular affine-hull regimes.

Set \(\mu=\frac{k}{pq}\mathbf1_p\mathbf1_q^{\mathsf T}\). Let \(U_0=\mathbf1_p\mathbf1_p^{\mathsf T}/p\), \(U_1=I_p-U_0\), \(V_0=\mathbf1_q\mathbf1_q^{\mathsf T}/q\), and \(V_1=I_q-V_0\). For matrices \(Y\), define the orthogonal projections
\[
\Pi_{10}Y=U_1YV_0,\qquad
\Pi_{01}Y=U_0YV_1,\qquad
\Pi_{11}Y=U_1YV_1.
\]
The positive covariance eigenvalues, with multiplicities \(p-1\), \(q-1\), and \((p-1)(q-1)\), are respectively
\[
\lambda_{10}=\frac{k(p-k)}{pq(p-1)},\qquad
\lambda_{01}=\frac{k(q-k)}{pq(q-1)},\qquad
\lambda_{11}=\frac{k((p-1)(q-1)+k-1)}{pq(p-1)(q-1)}.
\]
Put
\[
d=(p-1)(q-1)+(p-1)\mathbf1_{k<p}+(q-1)\mathbf1_{k<q}.
\]
Let \(H\) be the orthogonal direct sum of those three projection spaces whose displayed eigenvalue is strictly positive; in particular \(H\) is perpendicular to the all-ones matrix. Then the Löwner ellipsoid is exactly
\[
\boxed{\quad E_{p,q,k}=\left\{\mu+Y:\ Y\in H,\ \sum_{ab\in\{10,01,11\}:\lambda_{ab}>0}\frac{\|\Pi_{ab}Y\|_F^2}{\lambda_{ab}}\le d,\quad \Pi_{ab}Y=0\text{ whenever }\lambda_{ab}=0\right\}.\quad}
\]
The **entire** contact set is exactly the \(\binom pk\binom qk k!\) assignment vertices; there are no other contacts. In particular, its full principal squared-semiaxis spectrum is \(d\lambda_{10}\) (multiplicity \(p-1\), if positive), \(d\lambda_{01}\) (multiplicity \(q-1\), if positive), and \(d\lambda_{11}\) (multiplicity \((p-1)(q-1)\)). Its intrinsic volume is
\[
\operatorname{vol}_d(E_{p,q,k})=\frac{\pi^{d/2}d^{d/2}}{\Gamma(1+d/2)}\prod_{ab:\lambda_{ab}>0}\lambda_{ab}^{r_{ab}/2},
\]
where \(r_{10}=p-1\), \(r_{01}=q-1\), and \(r_{11}=(p-1)(q-1)\).

The ratio of largest to smallest positive principal semiaxis is
\[
\boxed{\quad\mathcal A_{p,q,k}=\begin{cases}
\sqrt{\dfrac{(p-1)(q-1)+k-1}{(q-1)(p-k)}},&k<p,\\[4pt]
\sqrt{\dfrac{q}{q-p}},&k=p<q,\\[4pt]
1,&k=p=q.
\end{cases}\quad}
\]
In the square family \(p=q=n\ge3\), \(\mathcal A_{n,n,k}\) increases strictly through \(1\le k<n\), attains its sharp maximum \(\sqrt{n-1/(n-1)}\) at \(k=n-1\), and returns exactly to one at \(k=n\), when the affine hull loses its row and column variation modes. In particular the Löwner ellipsoid is a Euclidean ball exactly in the simplex case \(k=1\) and the square saturated case \(k=p=q\).

## Assumptions and scope
All arithmetic parameters are integers, with \(2\le p\le q\) and \(1\le k\le p\). A \(k\)-matching is viewed as its incidence matrix; the polytope uses its intrinsic Frobenius (ambient Euclidean) geometry, not an arbitrary affine re-embedding. A zero eigenvalue means an affine-hull constraint, not a zero-length semiaxis. The assignment vertices and their convex hull agree with the usual \(k\)-matching-polytope definition for the complete bipartite graph.

## Proof
**1. Mean and covariance.** Let \(X\) be uniformly distributed among the \(\binom pk\binom qk k!\) assignment matrices. Symmetry gives \(\mathbb EX=\mu\). For a coordinate edge \(e=(i,j)\), \(\mathbb P(X_e=1)=\pi=k/(pq)\). For distinct edges sharing a row or column, the joint probability is zero. For two edges with distinct rows and distinct columns, the joint probability is \(\rho=k(k-1)/(pq(p-1)(q-1))\). Therefore, in tensor notation, the covariance is
\[
C=\pi I_{pq}+\rho(J_p-I_p)\otimes(J_q-I_q)-\pi^2J_p\otimes J_q.
\]
The all-constant subspace is in its kernel. On the mutually orthogonal row-contrast, column-contrast and interaction spaces, the eigenvalues are \(\pi-(q-1)\rho\), \(\pi-(p-1)\rho\), and \(\pi+\rho\), respectively. Simplification yields the stated \(\lambda_{ab}\), with only the specified zero modes. Consequently \(H=\operatorname{range}C\) has dimension \(d\) and is exactly the direction space of the affine hull, because a finite random variable's covariance kernel consists precisely of linear functionals constant on its support.

**2. Every vertex satisfies equality.** Fix any assignment vertex \(X\), and write \(Y=X-\mu\). Its row-sum vector has exactly \(k\) ones, as does its column-sum vector. Orthogonal decomposition gives
\[
\|\Pi_{10}Y\|_F^2=\frac{k(p-k)}{pq},\quad
\|\Pi_{01}Y\|_F^2=\frac{k(q-k)}{pq},\quad
\|\Pi_{11}Y\|_F^2=\frac{k((p-1)(q-1)+k-1)}{pq}.
\]
These formulas follow by projecting the row and column sums and subtracting their squared norms from \(\|Y\|_F^2=k-k^2/(pq)\). Each displayed positive squared norm is its covariance eigenvalue times its projection-space dimension. Thus
\[
\langle Y,C_H^{-1}Y\rangle=\sum_{ab:\lambda_{ab}>0}\frac{\|\Pi_{ab}Y\|_F^2}{\lambda_{ab}}=d.
\]
All assignment vertices are exactly on the claimed ellipsoid; convexity shows the whole polytope lies inside. Every listed zero-one assignment is an extreme point, because any convex combination producing a zero-one matrix must agree in every coordinate. Since the ellipsoid is strictly convex within its affine hull, a nontrivial convex combination of distinct vertices lies strictly inside it. Thus the vertices are the complete set of contacts.

**3. Global minimum and uniqueness.** Work in the \(d\)-dimensional affine hull, translating the mean to the origin. Any ellipsoid containing every vertex has a positive definite shape matrix \(A\), center \(c\), and inequalities \((X-c)^{\mathsf T}A^{-1}(X-c)\le1\) at all vertices. Averaging yields
\[
1\ge\operatorname{tr}(A^{-1}C_H)+(\mu-c)^{\mathsf T}A^{-1}(\mu-c)
\ge d\left(\frac{\det C_H}{\det A}\right)^{1/d}.
\]
The second inequality is arithmetic-geometric mean for the eigenvalues of \(A^{-1/2}C_HA^{-1/2}\). Hence \(\det A\ge d^d\det C_H\); the proposed shape \(A=dC_H\) attains equality. Equality requires simultaneously \(c=\mu\) and \(A=dC_H\), proving uniqueness among all translated and rotated ellipsoids.

**4. Spectrum and anisotropy.** The volume formula follows by multiplying the principal semiaxes. For \(k<p\), the eigenvalues obey \(\lambda_{11}\ge\lambda_{01}\ge\lambda_{10}>0\), since their consecutive differences are \(p\rho\) and \((q-p)\rho\); the first is strict if \(k>1\). At \(k=p<q\), the row-contrast eigenvalue vanishes and the ratio of the two remaining eigenvalues is \(q/(q-p)\). At \(k=p=q\), only the interaction space survives, and the ellipsoid is round in its intrinsic dimension. The displayed anisotropy formula and the square-family strict increase and final collapse follow immediately.

## Verification
The standalone standard-library script `check.py` explicitly enumerates assignments for all \(44\) profiles with \(2\le p\le5\) and \(p\le q\le6\), across all \(1\le k\le p\). It checks the vertex count, every coordinate-pair joint probability by exact rational arithmetic, the three eigenvalues' nonnegative domains, the affine-hull rank, the exact projection-norm identities and the exact Mahalanobis equality. It inspected \(7{,}925\) individual assignments and returned `PASS`. The proof above, not finite testing, establishes the universal statement.

## Relationship to prior work
Gill and Linusson's 2009 work determines the vertices, affine dimension, faces and one-skeleton diameter of the \(k\)-assignment polytope. Torres's 2023 work gives a broader bipartite \(k\)-matching polytope description and normality. The geometry of extremal ellipsoids is explicitly studied for the distinct *metric polytope* by Gartsman and Linial (2023). The present claim instead determines the least-volume Frobenius ellipsoid around the fixed-rank rectangular assignment vertices. Existing descriptions of facets or John (inscribed) ellipsoids do not determine a Löwner (enclosing) ellipsoid; polarity would require a result on the polar polytope, not on this polytope itself. The general covariance contact argument is standard; the specifically evaluated three-eigenspace spectrum, all-rank enclosing ellipsoid, intrinsic boundary regimes, and sharp square saturation transition are the stated contribution.

## Limitations
The theorem is for complete bipartite assignment polytopes, not arbitrary bipartite graphs. It determines the minimum-volume enclosing ellipsoid, not the maximum-volume inscribed one. The metric is the ordinary Frobenius metric. It makes no claim about new normality, face incidence, or combinatorial diameter results. Prior-art screening cannot exclude an unindexed equivalent result phrased in partial-rook or design-covariance language. Independent mathematical validation remains outstanding.

## References
1. J. Gill and S. Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148–161; doi:10.1016/j.disopt.2008.10.003. Author-approved postprint: https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.
2. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910 (first public version 2023-06-20), https://arxiv.org/abs/2306.11910.
3. R. Gartsman and N. Linial, *On the Löwner-John Ellipsoids of the Metric Polytope*, arXiv:2305.02113 (2023), https://arxiv.org/abs/2305.02113.
