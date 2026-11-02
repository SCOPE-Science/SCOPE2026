# A universal negative-type exponent for matching subdivisions of cliques

## Finding

Let \(m,r\) be integers with \(r\ge 2\) and \(m\ge 2r\). Starting with the unit-edge complete graph \(K_m\), subdivide once each of \(r\) vertex-disjoint edges, replacing each such edge by a path of two unit edges; call the resulting graph \(G_{m,r}\), and give its \(m+r\) vertices the shortest-path metric \(d\). Define \(p_*\in(0,1)\) as the unique solution of
\[
3^{p_*}(2-2^{p_*})=2(2^{p_*}-1)^2.
\]
Then, for **every** such \(m,r\), the supremal \(p\)-negative-type exponent of \((V(G_{m,r}),d)\) equals the same number
\[
\wp(G_{m,r})=p_*=0.706863663237331\ldots.
\]
The metric has strict \(p\)-negative type for \(0\le p<p_*\), nonstrict \(p_*\)-negative type with an equality space of dimension exactly \(r-1\), and no \(p\)-negative type for any \(p>p_*\). Equivalently, \(d^{p/2}\) embeds isometrically into real Hilbert space exactly when \(0\le p\le p_*\). Its **minimal affine embedding dimension** is \(m+r-1\) when \(0<p<p_*\) and is exactly \(m\) when \(p=p_*\).

## Assumptions and scope

Every vertex and every edge is retained during the subdivision, except that each selected original edge is replaced by two unit-length edges through one new vertex. The subdivided edges form a matching (their original endpoints are pairwise distinct). The theorem requires at least two subdivided edges: the one-edge-subdivision case is not asserted. There are \(t=m-2r\ge0\) untouched original vertices.

A metric has \(p\)-negative type if, for every real vector \(f\) indexed by its vertices with \(\sum_v f_v=0\), one has
\[
Q_p(f):=\sum_{u,v}f_u f_v\,d(u,v)^p\le0,
\]
where the diagonal entries are taken to be zero, including at \(p=0\). Strict negative type means strict inequality for every nonzero zero-sum vector. The \(p=0\) assertion is made using this off-diagonal convention.

Write each subdivided edge's former endpoints as \(u_i,v_i\), its new intermediate vertex as \(w_i\), with \(1\le i\le r\), and write the untouched original vertices as \(y_j\), with \(1\le j\le t\). Their nonzero distances are: \(d(u_i,v_i)=2\); \(d(u_i,w_i)=d(v_i,w_i)=1\); \(d(w_i,w_j)=3\) for \(i\ne j\); \(d(w_i,x)=2\) for every original vertex \(x\notin\{u_i,v_i\}\); and all other distinct original-original distances equal \(1\).

## Proof

**1. The critical equation and its unique solution.** Put \(a=2^p\), \(b=3^p\), and
\[
F(p)=b(2-a)-2(a-1)^2.
\]
We have \(F(0)=1\), \(F(1)=-2\). For \(0<p<1\), the ratio
\[
R(p)=\frac{2(2^p-1)^2}{3^p(2-2^p)}
\]
is strictly increasing from zero to infinity: its logarithmic derivative is
\[
\frac{R'(p)}{R(p)}
=\frac{2a\log2}{a-1}+\frac{a\log2}{2-a}-\log3
>4\log2-\log3>0.
\]
Hence there is a unique \(p_*\in(0,1)\) with \(F(p_*)=0\); \(F\) is positive below this point in \((0,1)\) and negative above. For \(p\ge1\), \(a\ge2\), so \(F(p)<0\).

**2. An orthogonal block decomposition of the powered-distance form.** Consider the zero-sum subspace of \(\mathbb R^{m+r}\). Because the distance matrix is invariant under exchanging each \(u_i,v_i\), under permutations of the \(r\) triples \((u_i,v_i,w_i)\), and under permutations of the \(t\) untouched original vertices, it decomposes as the direct orthogonal sum of the following invariant spaces.

The \(r\) independent endpoint-antisymmetric directions \(e_{u_i}-e_{v_i}\) have distance-matrix eigenvalue \(-a\). The untouched-original contrasts, when \(t\ge2\), have eigenvalue \(-1\), with multiplicity \(t-1\).

The paired-block standard modes assign the common value \(x_i\) to \(u_i,v_i\), the value \(z_i\) to \(w_i\), and zero to all untouched originals, subject to the two constraints \(\sum_i x_i=\sum_i z_i=0\). Directly collecting the distance contributions gives
\[
Q_p=\sum_{i=1}^r \bigl[(2a-4)x_i^2-4(a-1)x_i z_i-b z_i^2\bigr].
\]
Thus the relevant \(2\)-by-\(2\) symmetric block is
\[
S_p=\begin{pmatrix}2a-4&-2(a-1)\\-2(a-1)&-b\end{pmatrix},
\qquad \det S_p=2\bigl[b(2-a)-2(a-1)^2\bigr]=2F(p).
\]
At \(p=p_*\), this is negative semidefinite with a one-dimensional kernel; each of the \(r-1\) independent standard representations contributes one kernel vector. For \(p>p_*\), the same standard space contains a vector giving \(Q_p>0\). This proves the universal upper bound and the endpoint's prospective nullity.

**3. Strictness of every remaining component at the endpoint.** Let
\[
c=a-1,\qquad d=b-1,\qquad k=2c-d
\]
with \(a,b\) evaluated at \(p_*\). Because \(0<p_*<1\), strict concavity of positive powers yields \(b<2a-1\), hence \(k>0\), while \(0<c<1\). The endpoint equation is equivalent to
\[
(1+d)(1-c)=2c^2.
\]
The only remaining component is the orbit-constant zero-sum space, where all matched original endpoints receive a common value \(x\), all inserted vertices a common value \(z\), and the untouched original vertices a common value \(y\), with \(2rx+rz+ty=0\).

If \(t>0\), eliminate \(y=-r(2x+z)/t\) and set \(h=r/t\). Direct distance counting gives
\[
Q_{p_*}=-r\begin{pmatrix}x&z\end{pmatrix}
\begin{pmatrix}
2(1-c+2h)&2(c+h)\\
2(c+h)&rk+1+d+h
\end{pmatrix}
\binom{x}{z}.
\]
The leading entry is positive. Substituting \((1+d)(1-c)=2c^2\), the determinant is exactly
\[
2r(1-c)k+h\bigl[6-2c+4(r-1)k\bigr]>0.
\]
Therefore the matrix is positive definite and the orbit-constant quadratic form strictly negative for every nonzero zero-sum orbit-constant vector.

If \(t=0\), then \(z=-2x\) and the same counting instead gives
\[
Q_{p_*}=-2r\bigl[3-c+2(r-1)k\bigr]x^2<0
\]
for nonzero \(x\). Thus the orbit-constant component never contributes a zero direction.

The antisymmetric and untouched-original components are also strictly negative. All zero-sum vectors therefore have \(Q_{p_*}\le0\), and the entire equality space has dimension exactly \(r-1\), coming solely from the standard modes.

**4. Strictness at smaller powers and failure above.** The established interval theorem for negative type (Li and Weston, 2009) says that \(p_*\)-negative type with \(p_*>0\) implies strict \(p\)-negative type for every \(0\le p<p_*\). For \(p>p_*\), the standard mode in Step 2 has a positive direction (if \(p<1\), its determinant is negative; if \(p\ge1\), its first diagonal entry is nonnegative and its off-diagonal entry is nonzero). Hence the threshold is sharp for all powers.

**5. Embedding dimensions.** Schoenberg's finite-metric theorem identifies the squared Euclidean distance Gram matrix with \(-\frac12 JD^pJ\), where \(J\) is the orthogonal projection onto the zero-sum space. Its rank is the minimum affine embedding dimension. For \(0<p<p_*\), strict negative type gives rank \((m+r)-1\). At \(p=p_*\), exactly \(r-1\) eigenvalues vanish on the zero-sum subspace, giving rank \((m+r)-1-(r-1)=m\).

## Verification

The included `verify.py` builds each graph independently by its adjacency list, obtains all shortest-path distances using breadth-first search, and compares them to the distance-type formula. It constructs an orthonormal zero-sum Helmert basis and checks the full projected powered-distance spectra below, at and above the predicted exponent. It also separately compares the global-mode direct quadratic form with the analytical matrix, checks the standard-block determinant, and calculates the critical root independently by bisection. It passed 136 structural and spectral assertions across 16 graphs with \(r\) between \(2\) and \(5\) and \(t\) among \(0,1,2,4\). These are supplementary finite checks only: the all-parameter conclusion follows from the proof above.

To reproduce, run `python verify.py` in a Python 3 environment with NumPy installed. The checker uses no network access or third-party data files.

## Relationship to prior work

Obata and Zakiyyah (2018, Theorem 3.9) show that **deleting** at least two disjoint edges of a complete graph yields an unpowered quadratic embedding constant of zero. The present metric retains a new degree-two vertex on every removed edge; pairs of new vertices are at distance three, so its powered-distance matrix is not the deleted-matching metric. The new result computes the sharp variable exponent strictly below one and its varying equality-space dimension.

The graph-join computations of Lou, Obata and Huang (2020) and Młotkowski and Obata (2024) treat ordinary quadratic embedding constants and graph-join structures. The present graphs with at least two subdivisions have connected complementary graphs and hence no nontrivial complete-join decomposition, so those formulas do not directly cover the claimed two-parameter family. Choudhury and Nandi (2023) focus on unpowered quadratic embedding constants and distance spectra of other graph constructions. Li and Weston (2009) supply the general negative-type interval principle used in the proof, not the concrete critical equation here.

## Limitations

The theorem does not cover a single subdivided edge, adjacent subdivided edges, arbitrary subdivision lengths, nonmatching edge sets, weighted graph metrics or arbitrary p-powered kernels. The displayed decimal is an approximation; the exact endpoint is specified by its unique root. The numerical tests cover only finite parameters and are not exhaustive evidence for the infinite family. Historical mathematical priority has not been independently certified: an equivalent unpublished or differently indexed result cannot be ruled out solely by literature searches.

## References

1. N. Obata and A. Y. Zakiyyah, *Distance matrices and quadratic embedding of graphs*, Electronic Journal of Graph Theory and Applications 6 (2018), 37–60. DOI: `10.5614/ejgta.2018.6.1.4`; open PDF: https://media.neliti.com/media/publications/237871-distance-matrices-and-quadratic-embeddin-1ae8dc80.pdf .
2. Z. Lou, N. Obata, and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752, https://arxiv.org/abs/2001.06752 .
3. W. Młotkowski and N. Obata, *Quadratic Embedding Constants of Fan Graphs and Graph Joins*, arXiv:2403.16348, https://arxiv.org/abs/2403.16348 .
4. P. N. Choudhury and R. Nandi, *Quadratic Embedding Constants of Graphs: Bounds and Distance Spectra*, arXiv:2306.15589, https://arxiv.org/abs/2306.15589 .
5. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, https://arxiv.org/abs/0901.0695 .
