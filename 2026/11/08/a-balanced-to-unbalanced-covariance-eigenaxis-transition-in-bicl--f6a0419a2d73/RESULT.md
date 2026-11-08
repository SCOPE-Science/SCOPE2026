# A balanced-to-unbalanced covariance eigenaxis transition in biclique stable-set polytopes

## Finding

Let \(K_{p,q}\) be the complete bipartite graph with parts \(A,B\) of sizes \(p,q\ge2\). Let \(X\) be sampled **uniformly from the distinct vertices**, not from the interior, of the Euclidean stable-set polytope \(P=\operatorname{STAB}(K_{p,q})\subset\mathbb R^{p+q}\). Put
\[
N=2^p+2^q-1,\qquad a=\frac{2^{p-1}}N,\qquad b=\frac{2^{q-1}}N.
\]
The covariance is exactly
\[
\Sigma=\operatorname{Cov}(X)=
\begin{pmatrix}
\frac a2 I_p+(\frac a2-a^2)J_p&-abJ_{p,q}\\
-abJ_{q,p}&\frac b2 I_q+(\frac b2-b^2)J_q
\end{pmatrix},
\]
where \(J_{u,v}\) is the all-ones \(u\)-by-\(v\) matrix and \(J_u=J_{u,u}\). Its complete spectrum consists of \(a/2\) (multiplicity \(p-1\)) on the \(A\)-contrast subspace, \(b/2\) (multiplicity \(q-1\)) on the \(B\)-contrast subspace, and the two eigenvalues
\[
\lambda_{\pm}=\frac{\ell_A+\ell_B\pm\sqrt{(\ell_A-\ell_B)^2+4pq\,a^2b^2}}2,
\quad \ell_A=\frac a2+p(\frac a2-a^2),\quad \ell_B=\frac b2+q(\frac b2-b^2)
\]
of the symmetric axial matrix
\[
L=\begin{pmatrix}\ell_A&-ab\sqrt{pq}\\-ab\sqrt{pq}&\ell_B\end{pmatrix}
\]
on the orthonormal basis \((\mathbf1_A/\sqrt p,\mathbf1_B/\sqrt q)\).

The largest eigenvalue is always \(\lambda_+\), and its eigenspace is one-dimensional (coordinates of opposite signs on the two parts). The least eigenvalue and its **entire** eigenspace exhibit a sharp balance transition:

* If \(p=q=k\), then \(\lambda_{\min}=\frac a2(1-k/N)\), with the unique least-eigenvalue line \(\mathbb R(\mathbf1_A,\mathbf1_B)\); the top eigenvalue is \(\lambda_+=a(k+1)/2\).
* If \(p>q\), then \(\lambda_{\min}=b/2\), with least eigenspace exactly \(\{(0,v):\sum_{j\in B}v_j=0\}\), of dimension \(q-1\).
* If \(q>p\), exchange \(A,B\).

Thus, with \(\kappa=\lambda_{\max}/\lambda_{\min}\),
\[
\kappa(P)=\frac{k+1}{1-k/(2^{k+1}-1)}\sim k+1\quad(p=q=k\to\infty),
\qquad \kappa(P)\sim 2^{p-q}\quad(p\to\infty,\ q\ge2\text{ fixed}).
\]
The asymptotics show a sharp difference between balanced growth and adding vertices to one part while holding the other fixed.

## Assumptions and scope

All integers \(p,q\ge2\) are included and there is no upper bound. Coordinates of \(P\) are the ordinary indicator-vector coordinates of graph stable sets, in the ambient standard Euclidean metric. Each of the \(N\) distinct vertices has equal probability. This is **not** uniform Lebesgue volume on \(P\), and the covariance ellipsoid is **not** a John or Löwner ellipsoid. The polytope is full-dimensional because it includes the origin and all coordinate unit vectors.

## Proof

**Vertex count and second moments.** A stable set of \(K_{p,q}\) lies wholly in \(A\) or wholly in \(B\). Consequently its vertices are exactly the indicator vectors of subsets of either part, with the empty set counted once, giving \(N=2^p+2^q-1\). Every such indicator is a vertex: any \(0/1\) point cannot be a nontrivial convex combination of distinct \(0/1\) points because each coordinate equal to \(0\) or \(1\) forces all contributing vertices to agree there. For \(i\in A\), \(\mathbb E X_i=a\); for \(j\in B\), \(\mathbb E X_j=b\). If \(i,i'\in A\) are distinct, \(\mathbb E X_iX_{i'}=2^{p-2}/N=a/2\); the analogous value on \(B\) is \(b/2\), whereas a mixed-part product is zero. On the diagonal \(X_i^2=X_i\). Subtracting the products of means yields the stated block covariance.

**Orthogonal decomposition.** The \(A\)-contrast and \(B\)-contrast spaces are mutually orthogonal and have eigenvalues \(a/2,b/2\), respectively. Their common orthogonal complement is spanned by the two normalized part-indicators, on which the covariance is \(L\). Because \(ab\sqrt{pq}>0\), \(L\) has two distinct eigenvalues \(\lambda_-<\lambda_+\). Also \(0<a,b<1/2\), so \(\ell_A>a/2\) and \(\ell_B>b/2\). The strict variational inequality \(\lambda_+>\max\{\ell_A,\ell_B\}\) implies \(\lambda_+>\max\{a/2,b/2\}\), establishing the unique principal axis. The off-diagonal entries are negative, so the upper axial eigenvector has opposite-signed coefficients.

**Balanced case.** If \(p=q=k\), then \(a=b=2^{k-1}/N\), with \(N=2^{k+1}-1\). Direct diagonalization of \(L\) on the sum and difference axes gives
\[
\lambda_+=\frac{a(k+1)}2,\qquad
\lambda_-=\frac a2\left(1-\frac{k}{N}\right)<\frac a2.
\]
Thus the global all-ones direction is the **only** least-eigenvalue line, and division gives the balanced condition number.

**Unbalanced case.** Without loss of generality \(p>q\ge2\). Set \(U=2^p\), \(V=2^q\); then \(V\le U/2\), \(p\ge3\), and \(a>b\). A direct expansion gives the exact determinant identity
\[
\det\left(L-\frac b2 I_2\right)
=\frac{qb}{8N^2}\bigl[(U-1)(U-V)-pU\bigr].
\]
The bracket is at least \(U[(U-1)/2-p]>0\): the last inequality follows from \(2^p-1>2p\) for every integer \(p\ge3\), established by induction (true at \(p=3\); doubling increases the left side by more than the right). The first leading diagonal element is \(\ell_A-b/2>0\), since \(\ell_A>a/2>b/2\). Sylvester's criterion therefore gives \(L-(b/2)I_2\succ0\), i.e. both axial eigenvalues strictly exceed \(b/2\). Also \(a/2>b/2\), so the \(B\)-contrast space, and only that space, is the least eigenspace. Interchanging part labels proves the remaining case.

**Asymptotics.** For \(p=q=k\), the displayed exact condition number satisfies \(k/(2^{k+1}-1)\to0\). For fixed \(q\ge2\) as \(p\to\infty\), one has \(a\to1/2\), \(b\sim2^{q-p-1}\), \(p(a/2-a^2)\to0\), and \(L\to\operatorname{diag}(1/4,0)\). Hence \(\lambda_+\to1/4\) and the exact least eigenvalue is \(b/2\sim2^{q-p-2}\), yielding \(\kappa\sim2^{p-q}\). This completes the proof for all sizes and every limiting regime claimed.

## Verification

The standalone `verify.py` enumerates all distinct stable sets for each \(2\le p,q\le7\): 36 size profiles and 2,988 vertex occurrences in total. It computes every coordinate covariance exactly as a rational number and compares with the displayed block formula; it then compares numerical eigenvalues against all predicted spectral multiplicities and checks the ordering. The output is `BICLIQUE_VERTEX_COVARIANCE_CHECKS_PASSED`. These finite computations check algebra and implementation, not the infinite theorem, which is proved above. Run with `python verify.py` (Python 3 and NumPy required).

## Relationship to prior work

Aliniaeifard, Benedetti, Bergeron, Li, and Saliola give a systematic account of stable-set-polytope vertices, one-skeleta, and **graph-theoretic** diameter, but not the uniform-vertex Euclidean covariance spectrum (arXiv:1804.00360, originally posted 2018-04-02). Aprile, Faenza, Fiorini, Huynh, and Macchia study extension complexity of stable-set polytopes of bipartite graphs rather than vertex-coordinate second moments (arXiv:1702.08741, originally posted 2017-02-28). The origin-centered stable-set polytope of \(K_{p,q}\) is also affinely **isometric**, by complementing one coordinate block, to the order polytope of a poset consisting of two comparable antichains; a known John-ellipsoid analysis of such order polytopes addresses the continuous-volume containment optimizer, not this vertex-uniform covariance measure. An existing full balanced-family Löwner-ellipsoid claim gives all its contact vertices and its optimizing ellipsoid; those data are not the covariance of the uniform measure on the vertex set (the Löwner center differs from the discrete vertex barycenter already for two vertices per part). These distinctions are about mathematical statements and sampling measures, not wording.

## Limitations

The result covers \(p,q\ge2\), unweighted ordinary indicator coordinates, and vertex-uniform sampling only. It does not assert claims about uniform interior volume, general complete multipartite graphs, arbitrary coordinate weights, random stable sets with nonuniform probabilities, or John and Löwner ellipsoids. No claim of independent proof audit or exhaustive historical uniqueness is made. An earlier uncatalogued equivalent formula for Bernoulli mixture covariance could potentially imply the result; this historical risk remains.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first posted 2018-04-02. https://arxiv.org/abs/1804.00360
2. M. Aprile, Y. Faenza, S. Fiorini, T. Huynh and M. Macchia, *Extension complexity of stable set polytopes of bipartite graphs*, arXiv:1702.08741, first posted 2017-02-28. https://arxiv.org/abs/1702.08741
