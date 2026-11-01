# Optimal multipartite embeddings reduce exactly to spherical line codes

## Finding
For integers \(m\ge2\) and \(t\ge1\), let \(X_{m,t}\) be the unit-edge shortest-path metric of the complete multipartite graph with one class of size \(m\) and \(t\) other classes of size two. Put
\[
C_m=\sqrt{3-2/m},\qquad \mu_m=(m-2)/(2m).
\]
Then its least bi-Lipschitz distortion into a real Hilbert space is exactly
\[
\boxed{c_2(X_{m,t})=C_m}\quad(m\ge2,\ t\ge1).
\]
There is a precise rigidity classification of **all** optimal embeddings. After translating, applying a Hilbert isometry, and normalizing their smallest distance ratio to one, their \(m\)-point part is a centered regular simplex of edge length \(2\); every other part is an antipodal pair \(\{u_j,-u_j\}\), where the \(t\) unit vectors \(u_j\) are orthogonal to the simplex span and satisfy
\[
\boxed{|\langle u_i,u_j\rangle|\le\mu_m\quad(i\ne j).}
\]
Conversely every such configuration attains the optimal distortion. Thus, defining the spherical **line**-code dimension
\[
\mathfrak d(t,\mu)=\min\bigl\{d\ge1:\exists\ u_1,\dots,u_t\in\mathbb R^d,\ \|u_j\|=1,\ |\langle u_i,u_j\rangle|\le\mu\ (i\ne j)\bigr\},
\]
the least affine dimension of any optimal embedding is
\[
\boxed{\mathrm{dim}_{\min}(X_{m,t})=(m-1)+\mathfrak d(t,\mu_m).}
\]
The dimension has a sharp dichotomy: \(\mathrm{dim}_{\min}(X_{2,t})=t+1\), whereas for each fixed \(m\ge3\),
\[
\boxed{\mathrm{dim}_{\min}(X_{m,t})=m-1+\Theta_m(\log(t+1))\qquad(t\to\infty).}
\]
For \(m\ge3\), \(t\ge2\), and \(\delta_m=\sqrt{2(1-\mu_m)}\), explicit bounds are
\[
\frac{\log t}{\log(1+2/\delta_m)}\le\mathfrak d(t,\mu_m)\le
\left\lceil\frac{2}{\mu_m^2}\log\bigl(2t(t-1)\bigr)\right\rceil.
\]
An exact finite instance is \(\mathfrak d(7,1/6)=6\), hence \(\mathrm{dim}_{\min}(X_{3,7})=8\).

## Assumptions and scope
All metric spaces and scalar products are real. The graph has \(m+2t\) vertices. Distinct vertices belonging to the same part are distance \(2\); vertices belonging to different parts are distance \(1\). A bi-Lipschitz embedding \(f\) has distortion \(\max_{x\ne y}\|f(x)-f(y)\|/d(x,y)\) divided by \(\min_{x\ne y}\|f(x)-f(y)\|/d(x,y)\). A nonconstant finite-point map into a Hilbert space attains both extrema; we rescale so the latter equals \(1\). The minimum affine dimension concerns embeddings attaining the **globally optimal distortion**, not embeddings at larger allowed distortion. At \(t=1\), \(\mathfrak d(1,\mu)=1\) by definition. For \(m=2\), \(\mu_m=0\); for \(m\ge3\), \(0<\mu_m<1/2\).

## Proof
**1. A two-class Hilbert lower bound.** Given finite vectors \(a_1,\dots,a_m\) and \(b_1,b_2\), let their barycenters be \(\bar a\) and \(\bar b\), and their average squared deviations be \(V_A=m^{-1}\sum_i\|a_i-\bar a\|^2\) and \(V_B=2^{-1}\sum_j\|b_j-\bar b\|^2\). Hilbert-space expansion gives the exact identities
\[
V_A=\frac1{m^2}\sum_{i<j}\|a_i-a_j\|^2,\qquad
V_B=\frac14\|b_1-b_2\|^2,
\]
\[
\frac1{2m}\sum_{i=1}^m\sum_{j=1}^2\|a_i-b_j\|^2=V_A+V_B+\|\bar a-\bar b\|^2.
\]
Fix any two-point part \(B\) of \(X_{m,t}\) and the \(m\)-point part \(A\). For a normalized embedding with distortion \(C\), all same-part Euclidean distances are at least \(2\), while all cross-part distances are at most \(C\). Therefore
\[
C^2\ge V_A+V_B+\|\bar a-\bar b\|^2
\ge 2(m-1)/m+1=3-2/m=C_m^2.
\]
No symmetry or finite target-dimension assumption was made.

**2. Attainment for every number of parts.** Take a centered regular simplex \(a_1,\ldots,a_m\) with squared edge length \(4\), spanning an \((m-1)\)-dimensional subspace. Its vertex squared norm is \(2(m-1)/m\). In a perpendicular \(t\)-dimensional subspace take orthonormal unit vectors \(u_1,\ldots,u_t\) and represent the \(j\)-th two-point part by \(\{u_j,-u_j\}\). Same-part distances are exactly \(2\); large-part-to-pair distances are exactly \(C_m\); and distinct-pair-class distances equal \(\sqrt2\). Since \(\sqrt2\le C_m\) for \(m\ge2\), all cross-part Euclidean distances lie in \([1,C_m]\). Thus this is a normalized embedding of distortion \(C_m\), attaining the lower bound.

**3. Rigidity of *every* optimum.** Suppose a normalized embedding has distortion \(C_m\). For each pair class \(B_j\), both inequalities in step 1 must be equalities. Hence *all* distances within \(A\) are exactly \(2\), both points in \(B_j\) are exactly distance \(2\) apart, and \(\bar b_j=\bar a\). Moreover each of the \(2m\) cross distances has square at most \(C_m^2\), and their average equals \(C_m^2\), so each is equal to \(C_m\). Translate the common barycenter to the origin. Then \(A\) is a centered regular simplex with squared vertex norm \(2(m-1)/m\); and \(B_j\) equals \(\{u_j,-u_j\}\) for a unit vector \(u_j\). The equality \(\|a_i\pm u_j\|^2=C_m^2=\|a_i\|^2+1\) for both signs yields \(\langle a_i,u_j\rangle=0\). Thus every \(u_j\) is perpendicular to the full simplex span.

For two distinct pair classes, their four squared cross distances have values \(2+2\langle u_i,u_j\rangle\) and \(2-2\langle u_i,u_j\rangle\). As these represent graph distances \(1\), they must lie between \(1\) and \(C_m^2\). Hence
\[
|\langle u_i,u_j\rangle|\le\min\bigl\{1/2,(C_m^2-2)/2\bigr\}=\frac{m-2}{2m}=\mu_m.
\]
The same inequalities suffice for all distances to meet the normalized bounds. This proves the full rigidity classification, its converse and the exact dimension formula by orthogonal span additivity.

**4. The dimension dichotomy.** At \(m=2\), all distinct vectors must have zero pairwise inner products, forcing \(\mathfrak d(t,0)=t\). For fixed \(m\ge3\), let \(\mu=\mu_m>0\) and \(\delta=\sqrt{2(1-\mu)}\). Any admissible unit vectors have pairwise Euclidean separation at least \(\delta\). Open balls of radius \(\delta/2\) around them are disjoint and contained in a radius \(1+\delta/2\) ball. Comparing \(d\)-dimensional volumes gives \(t\le(1+2/\delta)^d\), proving the displayed lower bound.

For the upper bound choose \(t\) independent vectors uniformly from \(\{-1/\sqrt d,1/\sqrt d\}^d\). Their inner product is the average of \(d\) independent Rademacher signs. Hoeffding's inequality and the union bound give
\[
\Pr\{\exists i<j:\ |\langle u_i,u_j\rangle|>\mu\}\le t(t-1)\exp(-d\mu^2/2).
\]
Taking \(d=\lceil2\mu^{-2}\log(2t(t-1))\rceil\) makes this probability at most \(1/2\), so admissible vectors exist. Together these two estimates prove \(\mathfrak d(t,\mu_m)=\Theta_m(\log t)\).

**5. An exact seven-line certificate.** For \(m=3\) we have \(\mu=1/6\). Seven vectors forming a centered regular simplex in \(\mathbb R^6\) have pairwise inner product \(-1/6\), so \(\mathfrak d(7,1/6)\le6\). Conversely for any seven unit vectors with coherence at most \(1/6\), their positive-semidefinite Gram matrix has trace \(7\) and squared Frobenius norm at most \(7+42/36=49/6\). Cauchy--Schwarz on its nonzero eigenvalues yields \(\operatorname{rank}G\ge\operatorname{tr}(G)^2/\operatorname{tr}(G^2)\ge6\). Thus \(\mathfrak d(7,1/6)=6\).

## Verification
Execute `python3 verify_paired_multipartite.py` using standard-library Python 3. The script checks exact rational squared-distance identities for 154 feasible simplex/code cases comprising 33,217 graph-pair comparisons, 640 independent exact-rational Hilbert barycenter/variance identities and the seven-line Welch rank certificate. It also tests the admissibility conditions of the constructed code classes. The universal theorem rests on the proof above; these finite computations are reproducibility diagnostics, not a purported exhaustive proof of infinite families.

## Relationship to prior work
Vallentin's 2005 preprint (*Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716) determines Euclidean distortion in distance-regular families, including strongly regular balanced complete multipartite graphs. The present \(K_{m,2,\ldots,2}\) family is generally unbalanced and not distance-regular, and the new exact identification of every optimizer with a spherical **line** code and its linear-versus-logarithmic dimension dichotomy are additional conclusions not supplied by the compared theorems.

Robertson's *Negative type and bi-Lipschitz embeddings into Hilbert space* (arXiv:2309.16070) gives the sharp distortion of complete bipartite metrics and an orthogonal-simplex construction. Its bipartite case (one pair class) is a known antecedent rather than claimed new; the multi-pair coherence constraint and optimal-rank collapse are not consequences of having an optimal embedding on each two-part restriction in isolation. Das and Mohanty's *On Squared Distance Matrix of Complete Multipartite Graphs* (arXiv:2012.04341) studies the unoptimized squared-distance-matrix spectrum/inertia, not the minimizing Euclidean distortion and rank of all its realizations. Spherical-code estimates supply standard volume and probabilistic bounds; their joint use with the sharp *rigidity* condition is the proposed metric-embedding contribution.

## Limitations
The statement concerns the complete multipartite graph metric with exactly one class of size \(m\) and all other classes of size two. It does not resolve arbitrary part-size profiles, classify the exact spherical line-code dimension for every \(m,t\), or treat embedding dimension under nonoptimal distortion. The logarithmic asymptotic is for fixed \(m\ge3\), and its constants depend on \(m\). Spherical-code bounds are generally not sharp for finite parameters. The source comparison cannot rule out an equivalently formulated result in unindexed literature. Independent scientific audit has not been performed.

## References
- F. Vallentin, *Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716, first public version 30 September 2005, https://arxiv.org/abs/math/0509716.
- G. Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, arXiv:2309.16070, first public 27 September 2023, https://arxiv.org/abs/2309.16070.
- J. Das and S. Mohanty, *On Squared Distance Matrix of Complete Multipartite Graphs*, arXiv:2012.04341, https://arxiv.org/abs/2012.04341.
