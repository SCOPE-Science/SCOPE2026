# Sharp Hilbert distortion and rigidity transitions for clique-joined rook graphs

## Finding

For integers \(m,n\ge 2\) and \(h\ge 1\), let \(G_{m,n,h}=K_h\vee(K_m\square K_n)\) be the simple graph obtained by joining every vertex of a clique to every vertex of a rectangular rook graph. All graph edges have length one, and the metric is the shortest-path metric. Write \(M=\max\{m,n\}\), \(N=\min\{m,n\}\), and
\[
L_{m,n,h}=\frac{4N(M-1)+MN(1-1/h)}{2MN+M-N}.
\]
Then the exact least distortion into any real Hilbert space is
\[
\boxed{c_2(G_{m,n,h})^2=\max\{2,L_{m,n,h}\}.}
\]
In particular, the distortion is strictly greater than \(\sqrt{2}\) if and only if \((h-1)/(2h)>1/m+1/n\). On the balanced family \(m=n=q\),
\[
c_2(G_{q,q,h})^2=\max\left\{2,\frac52-\frac2q-\frac1{2h}\right\},
\qquad
\lim_{q,h\to\infty}c_2(G_{q,q,h})=\sqrt{5/2}.
\]

Optimal-embedding rigidity has an exact classification, always with the noncontractive normalization \(d_G(x,y)\le\|f(x)-f(y)\|\le c_2d_G(x,y)\):

1. If \(L_{m,n,h}<2\), there are infinitely many pairwise noncongruent optimal embeddings.
2. If \(L_{m,n,h}=2\), all optimal embeddings are congruent. Their squared side lengths along the two rook coordinates are both \(2\), while the hub clique has squared side length \(1\).
3. If \(L_{m,n,h}>2\) and \(M>N\), all optimal embeddings are congruent. The squared side lengths along the larger and smaller rook coordinates are respectively \(4-L_{m,n,h}\) and \(L_{m,n,h}\), and the hub clique has squared side length \(1\).
4. If \(L_{m,n,h}>2\) and \(m=n\), all optimal embeddings have two rook-coordinate squared side lengths \(u\) and \(4-u\), with \(4-L_{m,n,h}\le u\le L_{m,n,h}\); every such value occurs, yielding infinitely many noncongruent optimal embeddings.

In cases 2–4, the two centered regular-simplex factors and the centered hub simplex span mutually orthogonal subspaces, share the same centroid, and every optimum has affine dimension exactly \(m+n+h-3\). Congruence means equality of all labelled pairwise distances, equivalently an affine isometry of their spans.

## Assumptions and scope

The parameters \(m,n,h\) are integers in the indicated ranges. The target is an arbitrary real Hilbert space; no assumption of finite target dimension, equivariance, faithfulness, or symmetry of the embedding is made in proving optimality. A rook vertex is a pair \((i,j)\); two distinct rook vertices have graph distance one if precisely one coordinate differs and distance two if both differ. Hub-to-rook and distinct hub-to-hub distances are one. Every embedding is rescaled to be noncontracting; its squared expansion is the maximum squared Euclidean-to-graph distance ratio. A zero-dimensional hub simplex is allowed when \(h=1\).

## Proof

**1. Quadrilateral obstruction.** For any four Hilbert vectors \(a,b,c,d\), the quadrilateral identity is
\[
\|a-b\|^2+\|a-c\|^2+\|d-b\|^2+\|d-c\|^2
-\|a-d\|^2-\|b-c\|^2
=\|a+d-b-c\|^2\ge0.
\]
Take the four rook vertices on any rectangle with distinct row and column indices. Both diagonals have graph distance two, hence image-squared distance at least \(4\). Each of its four sides has graph distance one and image-squared distance at most \(D^2\). It follows immediately that \(D^2\ge2\) for every noncontracting \(D\)-Lipschitz embedding.

Assume the first rook coordinate has \(M\) labels and the second \(N\) labels, so \(M\ge N\). Let \(U\) and \(V\) be the mean squared image distance over first-coordinate and second-coordinate rook edges respectively. Each first-coordinate edge appears in exactly \(N-1\) rectangles and each second-coordinate edge in exactly \(M-1\). Averaging the quadrilateral inequality, with both diagonals squared at least \(4\), gives
\[
U+V\ge4,\qquad 1\le U,V\le D^2.
\]

**2. Centroid obstruction.** Let \(A\) be the mean squared distance of rook images from their centroid and \(B\) the corresponding quantity for the \(h\) hub images. If \(W\) is the mean squared image distance across pairs of rook vertices that differ in both coordinates, the Hilbert variance identity gives
\[
A=\frac{(M-1)U+(N-1)V+(M-1)(N-1)W}{2MN},\qquad W\ge4.
\]
Likewise the mutual hub distances are at least one, so
\[
B=\frac1{h^2}\sum_{a<b}\|z_a-z_b\|^2\ge\frac{h-1}{2h}.
\]
The mean squared distance over all hub-to-rook pairs is \(A+B+\|\overline x-\overline z\|^2\) and is at most \(D^2\), because every such graph distance equals one. Since \(M-1\ge N-1\),
\[
(M-1)U+(N-1)V=(M-1)(U+V)-(M-N)V
\ge4(M-1)-(M-N)D^2.
\]
Consequently,
\[
D^2(2MN+M-N)\ge 4N(M-1)+MN(1-1/h),
\]
which together with the quadrilateral bound proves \(D^2\ge\max\{2,L_{m,n,h}\}\). Notice that the argument treats every Hilbert embedding, including nonsymmetric ones.

**3. Attaining the bound.** In mutually orthogonal real spaces take centered regular simplices \(p_1,\ldots,p_M\), \(q_1,\ldots,q_N\), and \(z_1,\ldots,z_h\), having pairwise squared side lengths \(s\), \(t\), and \(1\), respectively. Explicit coordinates are \(p_i=\sqrt{s/2}(e_i-M^{-1}\mathbf1_M)\), \(q_j=\sqrt{t/2}(e_j-N^{-1}\mathbf1_N)\), and \(z_a=2^{-1/2}(e_a-h^{-1}\mathbf1_h)\). Map the rook vertex \((i,j)\) to \(p_i\oplus q_j\oplus0\) and the hub vertex \(a\) to \(0\oplus0\oplus z_a\). The squared image distances are \(s,t\) on the two kinds of rook edges, \(s+t\) on rook diagonals, \(1\) on hub edges, and
\[
R(s,t)=\frac{M-1}{2M}s+\frac{N-1}{2N}t+\frac{h-1}{2h}
\]
on hub-to-rook pairs.

If \(L_{m,n,h}\le2\), set \(s=t=2\). Then \(1\le R(2,2)\le2\), with the last inequality equivalent to \((h-1)/(2h)\le1/M+1/N\), itself equivalent to \(L_{m,n,h}\le2\). All metric constraints hold with squared distortion \(2\). If \(L_{m,n,h}>2\), note that \(2<L_{m,n,h}<5/2\); set \(s=4-L_{m,n,h}\) on the larger coordinate and \(t=L_{m,n,h}\) on the smaller. Then \(1<s<2<t<5/2\), \(s+t=4\), and direct substitution gives \(R(s,t)=L_{m,n,h}\). Thus every squared distance divided by squared graph distance lies between \(1\) and \(L_{m,n,h}\), attaining the lower bound.

**4. All optimal configurations in the binding phase.** At \(L_{m,n,h}=2\), every rook side must have squared length \(2\), by applying the quadrilateral inequality with the universal upper bound \(2\), and every rook diagonal must have squared length \(4\). The lower centroid bound becomes an equality; hence all hub squared sides equal \(1\), the hub and rook centroids coincide, and all hub-to-rook squared distances equal \(2\). These labelled distances determine a unique congruence class, necessarily the orthogonal-simplex construction.

When \(L_{m,n,h}>2\), equality in the centroid lower bound forces every rook diagonal squared to be exactly \(4\), all hub squared sides to be \(1\), coincident centroids, and every hub-to-rook squared distance to be \(L_{m,n,h}\). It also forces \(U+V=4\). Summing the nonnegative quadrilateral defects over all rectangles shows every defect vanishes, so the rook vectors satisfy \(x_{ij}+x_{i'j'}=x_{ij'}+x_{i'j}\). Hence they split additively into first- and second-coordinate vectors. Equality of both diagonals to \(4\) forces the two coordinate-difference spans to be orthogonal and their squared pairwise distances to be constants \(u,v\) with \(u+v=4\). Thus both coordinate factors are regular simplices. Fixed hub-to-rook squared distances and coincident centroids force the regular hub simplex to be orthogonal to both rook factors.

If \(M>N\), equality in the use of \(V\le D^2\) also forces \(V=D^2=L_{m,n,h}\). Consequently \(v=L_{m,n,h}\) and \(u=4-L_{m,n,h}\), so all labelled distances are fixed and the optimum is rigid. If \(M=N\), the coefficient of \(V\) vanishes; the complete remaining constraints are \(u+v=4\) and \(1\le u,v\le L_{m,n,h}\), equivalently \(4-L_{m,n,h}\le u\le L_{m,n,h}\). Each choice is attained by the construction above, so this is the complete one-parameter classification. In all binding cases, the three orthogonal simplex spans have dimensions \(M-1\), \(N-1\), and \(h-1\).

**5. Nonrigidity below the threshold.** If \(L_{m,n,h}<2\), the construction with \(s=t=2\) has squared hub-to-rook distance \(R(2,2)<2\) and at least \(1\). Moving the entire hub simplex together by a vector of squared length strictly between \(0\) and \(2-R(2,2)\) in a new direction orthogonal to all three simplex spaces changes precisely the hub-to-rook squared distance, without violating any distortion constraint. These configurations are optimal but pairwise noncongruent. This completes the classification.

## Verification

The standalone `CHECKER.py` uses exact rational Gram matrices of the three mutually orthogonal simplices. It enumerates all labelled vertex pairs and checks both \(d_G^2\le\|f(x)-f(y)\|^2\le c_2(G)^2d_G^2\) and attainment of the lower and upper ratios. It also checks the derived threshold equivalence, the hub/rook centroid squared radii, and distinct balanced strict-phase choices. The completed run checked 224 integer parameter triples, 154006 exact pairwise inequalities, and 20 alternative balanced configurations. These are finite consistency checks, not a proof of the quantified theorem or rigidity; those are proved above.

Run with a standard Python 3 interpreter: `python CHECKER.py`. There are no external packages or datasets.

## Relationship to prior work

Vallentin determined least Euclidean distortion for distance-regular graph families including Hamming graphs (arXiv:math/0509716, §4.1). Cioabă, Gupta, Ihringer, and Kurihara extend the distance-regular analysis (arXiv:2109.09708). The present graphs are **not** distance-regular: the hub degree exceeds a rook vertex degree by \((m-1)(n-1)>0\). The core Hamming graph alone has distortion \(\sqrt2\), which supplies only the first lower bound here; the additional sharp centroid obstruction from the joined clique and the rigidity transition are not provided by those distance-regular conclusions. Cardoso, Díaz, and Rojo study eigenvalues of distance matrices for graph joins (DOI below); a distance-spectrum calculation by itself is not an optimal bi-Lipschitz Hilbert-embedding classification. Targeted comparisons located no earlier statement directly covering the joint parameter formula and optimal-configuration classification. This is a qualified comparison, not an independent priority certification.

## Limitations

Only simple unweighted joins of a clique with a **two-coordinate** rook graph are treated, with real Hilbert targets and unrestricted target dimension. Weighted joins, higher Hamming dimensions, and different target Banach spaces are not addressed. Below the strict threshold only existence of multiple optimum classes is asserted, not their complete classification. Prior equivalent work under different graph-join or semidefinite-programming terminology remains a priority risk. No independent mathematical review has been performed.

## References

1. S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, original arXiv posting 2021-09-20, https://arxiv.org/abs/2109.09708 .
2. F. Vallentin, *Optimal distortion embeddings of distance regular graphs into Euclidean spaces*, originally posted 2005-09-30, https://arxiv.org/abs/math/0509716 .
3. D. M. Cardoso, R. C. Díaz, O. Rojo, *Distance matrices on the H-join of graphs: A general result and applications*, Linear Algebra Appl. 559 (2018), 34–53, https://doi.org/10.1016/j.laa.2018.08.024 .
