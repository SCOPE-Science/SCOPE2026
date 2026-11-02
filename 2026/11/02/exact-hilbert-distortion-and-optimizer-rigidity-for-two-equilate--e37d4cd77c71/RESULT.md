# Exact Hilbert distortion and optimizer rigidity for two equilateral blocks

## Finding

Let \(a,b\ge 2\) be integers and \(u,w,v>0\) satisfy \(u\le 2v\) and \(w\le 2v\). Define a finite metric \(X=A\sqcup B\), with \(|A|=a\) and \(|B|=b\), by assigning distance \(u\) between distinct points of \(A\), distance \(w\) between distinct points of \(B\), and distance \(v\) across the two blocks. Put
\[
\Sigma=\frac{a-1}{2a}u^2+\frac{b-1}{2b}w^2.
\]
Then the least bi-Lipschitz distortion of \(X\) into an arbitrary real Hilbert space is exactly
\[
\boxed{c_2(X)=\max\left\{1,\frac{\sqrt\Sigma}{v}\right\}.}
\]
All optimizers are rigid up to a common similarity: after choosing a noncontracting normalization they have distances \(u,w,\max\{v,\sqrt\Sigma\}\) on the three pair orbits, respectively. In particular, if \(\Sigma>v^2\), *every* optimal realization consists of two mutually orthogonal centered regular simplices, of edge lengths \(u\) and \(w\), having the **same centroid**. In that regime the least possible dimension, and the affine dimension of every optimal realization, equals \(a+b-2\). At \(\Sigma=v^2\), the space embeds isometrically in that dimension; at \(\Sigma<v^2\), the least isometric dimension is instead \(a+b-1\).

As a graph-metric consequence, let \(G_{a,b}=K_a\vee\overline{K_b}\) be the complete split graph with clique size \(a\) and independent-set size \(b\), for \(a,b\ge2\), with all edges of length one. Then
\[
\boxed{c_2(G_{a,b})=\sqrt{\frac52-\frac1{2a}-\frac2b}.}
\]
Its optimally normalized configurations, unique up to Euclidean isometry, have clique-pair distance \(1\), independent-pair distance \(2\), and every cross-pair distance \(\sqrt{5/2-1/(2a)-2/b}\). Their affine dimension is exactly \(a+b-2\). The sharp two-parameter distortion approaches \(\sqrt{5/2}\) as both parameters tend to infinity.

## Assumptions and scope

The metric is a **finite, labeled, two-equilateral-block metric**, with positive distances and the stated triangle conditions; all its points are distinct. For \(u,w\le2v\), every triangle contains either two or three points in one block, so the triangle inequality holds. A Hilbert embedding \(f\) is allowed to be nonlinear and to have an arbitrary target dimension. Its distortion is the infimum of \(D\ge1\) for which, after a common positive rescaling, \(d(x,y)\le\|f(x)-f(y)\|\le Dd(x,y)\) for every distinct pair.

This is metric (nonlinear) Hilbert distortion, **not** the Banach--Mazur distance of a Lipschitz-free space, the norm of an edge-space projection, or distortion into a line.

## Proof

**1. A universal centroid identity.** Write the embedded points as \(x_1,\ldots,x_a\) and \(y_1,\ldots,y_b\), and their centroids as \(\bar x\) and \(\bar y\). For arbitrary vectors in any real Hilbert space, the polarization identity implies
\[
\frac1{ab}\sum_{i=1}^a\sum_{j=1}^b\|x_i-y_j\|^2
=\frac1{2a^2}\sum_{i,k=1}^a\|x_i-x_k\|^2
+\frac1{2b^2}\sum_{j,l=1}^b\|y_j-y_l\|^2
+\|\bar x-\bar y\|^2.
\]
The last term is nonnegative, with equality precisely for matching centroids.

**2. Global lower bound.** Rescale any admissible embedding to be noncontracting. Its distinct within-block distances are at least \(u\) and \(w\), and its cross-block distances at most \(Dv\). Applying the identity gives
\[
D^2v^2\ge \frac{a-1}{2a}u^2+\frac{b-1}{2b}w^2=\Sigma.
\]
Thus \(D\ge\max\{1,\sqrt\Sigma/v\}\). This argument is independent of symmetry assumptions on the embedding or target dimension.

**3. Sharp construction.** Take orthogonal real Euclidean summands \(U\cong\mathbb R^a\), \(V\cong\mathbb R^b\), and, if necessary, a one-dimensional summand \(W\). In \(U\) put
\[
x_i=\frac{u}{\sqrt2}\left(e_i-\frac1a\mathbf1_a\right),
\qquad 1\le i\le a,
\]
and in \(V\oplus W\) put
\[
y_j=\frac{w}{\sqrt2}\left(e_j-\frac1b\mathbf1_b\right)+h e_0,
\qquad 1\le j\le b,
\]
where \(h=\sqrt{\max\{0,v^2-\Sigma\}}\), and the \(e_0\) term is omitted if \(h=0\). The first simplex has squared radius \((a-1)u^2/(2a)\), the second \((b-1)w^2/(2b)\). Consequently the within-block distances are exactly \(u,w\), while every cross-block squared distance is \(\Sigma+h^2=\max\{\Sigma,v^2\}\). The construction is noncontracting and attains the claimed distortion.

**4. Equality and rigidity.** When \(\Sigma>v^2\), any noncontracting optimal embedding has \(D^2v^2=\Sigma\). Equality in both upper and lower bounds of the centroid identity forces *every* within-block pair to realize its original length, every cross-block pair to have squared distance exactly \(\Sigma\), and the two centroids to coincide. In an equilateral point set, subtracting its centroid yields a regular simplex. Double-centering the constant cross-distance matrix shows that the two centered simplex subspaces are orthogonal. The pairwise distance matrix therefore determines all optimal configurations up to Euclidean isometry, even among nonsymmetric candidate embeddings. Their affine span has dimension \((a-1)+(b-1)\), since each simplex is nondegenerate.

When \(\Sigma\le v^2\), the construction is isometric. Every distortion-one embedding has the prescribed pairwise distances. After double-centering, the same two simplex subspaces are orthogonal, and the displacement of their centroids is orthogonal to both. Its squared length is \(v^2-\Sigma\), so the affine dimension is \(a+b-2\) if equality holds and \(a+b-1\) if the inequality is strict. A distance matrix has a unique Hilbert realization up to affine isometry; hence all optimal configurations are rigid also in the isometric regime.

**5. Graph specialization.** In \(G_{a,b}\) the clique distances are \(u=1\), the independent-set distances are \(w=2\), and the cross distances are \(v=1\). Therefore \(\Sigma=(a-1)/(2a)+2(b-1)/b=5/2-1/(2a)-2/b\). For \(a,b\ge2\), \(\Sigma\ge5/4>1\), so the nonisometric branch applies. The claimed exact graph formula and optimizer properties follow.

## Verification

A standalone, standard-library Python checker is provided in `checker.py`. It constructs the proposed positive-semidefinite Gram matrix in exact rational arithmetic. For each valid tested parameter tuple it checks all squared-distance entries, rank, and distortion factors, including both the isometric and nonisometric branches and the transition boundary. It separately tests the arbitrary-Hilbert centroid identity on independently generated rational vector configurations and verifies the complete-split specialization. It returned:

`CHECK_OK rational_matrix_cases= 2448 identity_cases= 448 validated_relations= 244464 branches= <,=,>`

Reproduce with `python3 checker.py` in a directory containing that file. The construction and all-parameter inequalities above supply the proof; the finite checker does not claim to enumerate arbitrary real parameters, target dimensions, or embeddings.

## Relationship to prior work

Gavin Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space* (first arXiv submission September 27, 2023, arXiv:2309.16070), develops a distorted-negative-type characterization and in its Theorem 4.3 gives exact Hilbert distortion for complete bipartite graph metrics and their common-exponent snowflakes. That result corresponds to **equal** within-block distances in the two-block setting. The present statement addresses independently variable within-block distances and gives the complete split-graph formula and all-optimal-embedding rigidity with exact minimum dimensions. Robertson's general variational characterization is relevant background, but does not state those evaluated formulas or the strict optimizer classification.

Vallentin's distance-regular-graph embedding work (arXiv:math/0509716) and Cioabă--Gupta--Ihringer--Kurihara's work (arXiv:2109.09708) concern regular graph families. The nonregular complete split graphs in this result are outside that distance-regular scope. These comparisons do not constitute an exhaustive guarantee of historical priority, and equivalent older formulations using Euclidean distance matrices or regular simplex configurations remain possible.

## Limitations

No claim is made for arbitrary within-block distance heterogeneity, three or more nontrivial clusters, or nonlinear targets other than real Hilbert spaces. The claim does not establish that its formulas have never appeared under another name. The equality statements assume a common noncontracting normalization and yield uniqueness only up to Euclidean isometry (or arbitrary global similarity before normalization). No external independent validation has been performed.

## References

1. Gavin Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070, first submitted 2023-09-27. https://arxiv.org/abs/2309.16070
2. Frank Vallentin, *Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716, first submitted 2005-09-30. https://arxiv.org/abs/math/0509716
3. Sebastian M. Cioabă, Himanshu Gupta, Ferdinand Ihringer and Hirotake Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708, first submitted 2021-09-20. https://arxiv.org/abs/2109.09708
