# Sharp negative type and covariance thresholds for projective-plane incidence metrics

## Finding

Let \(\Pi\) be any finite projective plane of order \(q\ge2\) (including non-Desarguesian planes when they exist). Its point–line incidence/Levi graph \(G_\Pi\) has shortest-path distance \(d\). Write \(N=q^2+q+1\), so the graph has \(2N\) vertices, and let \(p_q\) be the unique positive solution of
\[
\sqrt q\,(3^{p_q}-1)=2^{p_q}.
\]
Then \(d^p\) is conditionally negative semidefinite exactly for \(0<p\le p_q\), and is strictly conditionally negative definite for \(0<p<p_q\). Its smallest squared-Euclidean embedding dimension is \(2N-1\) below the threshold and exactly \(N\) at the threshold.

For \(p,t>0\), the distance covariance kernel \(K_{t,p}(x,y)=\exp(-t\,d(x,y)^p)\) is positive semidefinite **if and only if** the following two explicit inequalities hold. Put \(u=\exp(-t)\), \(v=\exp(-t2^p)\), and \(w=\exp(-t3^p)\). Then
\[
1+(N-1)v-(q+1)u-q^2w\ge0,
\qquad
1-v-\sqrt q\,(u-w)\ge0.
\]
For \(t>0\), strict positive definiteness holds if and only if both inequalities are strict. At \(t=0\) the kernel is the rank-one all-ones kernel. For every \(0<p\le p_q\) the two inequalities are strict for all \(t>0\).

In particular, for ordinary graph distance (\(p=1\)), there is a sharp **positive-bandwidth phase transition**:
\[
\exp(-t d)\succeq0\quad\Longleftrightarrow\quad t=0\;\text{or}\;t\ge\tfrac12\log q.
\]
At \(t=\frac12\log q\) the kernel has rank \(N+1\), and for \(t>\frac12\log q\) it is strictly positive definite. For \(p>p_q\), all sufficiently small positive \(t\) fail positive semidefiniteness, whereas all sufficiently large \(t\) give strictly positive-definite kernels.

## Assumptions and scope

A finite projective plane of order \(q\ge2\) has \(N\) points and \(N\) lines, each incident with \(q+1\) elements of the other type. Any two distinct points lie on exactly one common line, and any two distinct lines share exactly one point. The theorem is conditional on such a plane existing; no assertion is made for nonexistent orders. Distances in its incidence graph are \(0\) on the diagonal, \(1\) for incident point–line pairs, \(2\) for distinct vertices of the same type, and \(3\) for nonincident point–line pairs. Conditional negative semidefiniteness of a symmetric matrix \(D\) means \(z^*Dz\le0\) for every real/complex vector \(z\) whose coordinates sum to zero; strictness means strict inequality for each nonzero such vector. The embedding dimension is the least integer \(m\) admitting distinct points in \(\mathbb R^m\) whose squared Euclidean pairwise distances equal \(d^p\).

## Proof

Let \(M\) be the \(N\times N\) point–line incidence matrix, \(J\) the all-ones matrix, and \(I\) the identity. The projective-plane axioms give \(M\mathbf1=(q+1)\mathbf1\), \(M^T\mathbf1=(q+1)\mathbf1\), and
\[
MM^T=M^TM=qI+J.
\]
Thus on the orthogonal complement of the constant vector, every singular value of \(M\) is \(\sqrt q\). The powered distance matrix is
\[
D_p=\begin{pmatrix}
2^p(J-I)&3^pJ+(1-3^p)M\\
3^pJ+(1-3^p)M^T&2^p(J-I)
\end{pmatrix}.
\]
Its four real eigenvalue blocks, with multiplicities \(1,1,N-1,N-1\) respectively, are
\[
\begin{aligned}
L_0&=(N-1)2^p+(q+1)+q^2 3^p,\\
L_a&=(N-1)2^p-(q+1)-q^2 3^p,\\
L_+&=-2^p+\sqrt q(3^p-1),\\
L_-&=-2^p-\sqrt q(3^p-1).
\end{aligned}
\]
The \(L_0\) eigenspace is the all-ones line; all others are orthogonal to constants. For \(p\ge0\), \(L_-<0\). Also \(L_a(0)=-1\), and
\[
\frac{dL_a}{dp}=(q^2+q)2^p\log2-q^2 3^p\log3<0
\]
since \((q+1)\log2<q\log3\) for every \(q\ge2\), and \(2^p\le3^p\). Thus the only sign change on the mean-zero subspace can occur at \(L_+\). Rearranging \(L_+=0\) gives \((3/2)^p-(1/2)^p=1/\sqrt q\). This left side is strictly increasing from \(0\) to infinity as \(p\) increases from \(0\), yielding precisely one root \(p_q\). The asserted negative-type threshold and its strictness follow. For a finite conditionally negative-distance matrix with zero diagonal, the centered Gram matrix \(-\frac12HD_pH\), where \(H=I-\frac1{2N}J\), has eigenvalues equal to the negatives of the mean-zero distance eigenvalues divided by two. Its rank is \(2N-1\) when \(p<p_q\), and \(N\) at equality. Classical Euclidean distance-matrix theory then gives the least embedding dimensions.

For positive \(t\), set \(u=e^{-t},v=e^{-t2^p},w=e^{-t3^p}\), so \(1>u>v>w>0\). The covariance matrix has block form
\[
K_{t,p}=\begin{pmatrix}
(1-v)I+vJ&(u-w)M+wJ\\
(u-w)M^T+wJ&(1-v)I+vJ
\end{pmatrix}.
\]
The same singular-value decomposition gives eigenvalues
\[
\begin{aligned}
A_0&=1+(N-1)v+(q+1)u+q^2w&&\text{(multiplicity 1)},\\
A_a&=1+(N-1)v-(q+1)u-q^2w&&\text{(multiplicity 1)},\\
A_-&=1-v-\sqrt q(u-w)&&\text{(multiplicity \(N-1\))},\\
A_+&=1-v+\sqrt q(u-w)&&\text{(multiplicity \(N-1\))}.
\end{aligned}
\]
Here \(A_0,A_+>0\), so the remaining two conditions are simultaneously necessary and sufficient for positive semidefiniteness, and strict inequalities characterize strict positive definiteness. If \(0<p\le p_q\), the preceding Gram embedding realizes \(d(x,y)^p=\|v_x-v_y\|^2\) with pairwise distinct vectors; the Gaussian kernel \(e^{-t\|v_x-v_y\|^2}\) is strictly positive definite for every \(t>0\) (e.g. by its strictly positive Fourier density).

For \(p=1\), write \(z=e^{-t}\). Direct factorization gives
\[
A_a=(1-z)(1-qz+q^2z^2)>0,
\qquad
A_-=(1-z^2)(1-\sqrt q\,z).
\]
Thus for \(t>0\) the exact threshold is \(z\le q^{-1/2}\), or \(t\ge\frac12\log q\), with \(N-1\) vanishing eigenvalues only at equality, giving rank \(2N-(N-1)=N+1\). Finally, for \(p>p_q\), the positive mean-zero eigenvalue \(L_+\) makes the corresponding eigenvalue of \(K_{t,p}=J-tD_p+O(t^2)\) negative for sufficiently small \(t>0\). As \(t\to\infty\), \(K_{t,p}\to I\), establishing strict positive definiteness at all sufficiently large \(t\).

## Verification

The accompanying standalone `plane_covariance_check.py` enumerates the Desarguesian projective planes \(\operatorname{PG}(2,q)\) for \(q\in\{2,3,5\}\), constructs their incidence and shortest-path matrices, and compares the numerical eigenvalues with each exact spectral formula. It also checks both sides of the ordinary-distance covariance threshold. Running `python plane_covariance_check.py` with NumPy and SciPy prints 66 passed diagnostic assertions. These finite checks are corroboration rather than a proof for all planes and exponents. The proof above uses only the projective-plane axioms and therefore applies even to non-Desarguesian planes.

As an illustration that both Gaussian inequalities are needed at general exponents, at \(q=2,p=2,t=\log2\) one has \(A_a=-17/128<0\), although \(A_-=15/16-255\sqrt2/512>0\).

## Relationship to prior work

The projective-plane Levi graph and its incidence axioms are standard; De Winter, Lazebnik and Verstraëte (2008) develop it in an extremal-cycle setting, not in the powered-distance positive-definiteness setting. Sánchez (2011) develops a general framework for the supremal negative-type exponent of finite metrics and treats complete bipartite graphs; the present result specializes to the considerably different projective incidence metric and determines an explicit infinite-family threshold and covariance region. Spectral data of the Heawood graph (the \(q=2\) case) are classical, but eigenvalues of a graph adjacency matrix alone do not state the full powered-metric and bandwidth classification obtained here. Other literature could contain an equivalent formulation; novelty is therefore subject to bounded inspection rather than globally certified.

## Limitations

The result applies only to the shortest-path metric on point–line incidence graphs of finite projective planes that exist. It does not classify the individual connected components or number of intervals of the two-inequality admissibility set at general \(p>p_q\). It gives no quantitative conditioning bounds. Finite checker runs do not independently certify the infinite proofs, and no independent mathematical audit has occurred. The claimed comparison with prior results is based on a bounded review and may miss equivalent unindexed literature.

## References

- S. De Winter, F. Lazebnik, J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics **15** (2008), R143, DOI: https://doi.org/10.37236/867 (published 2008-11-30). Public full text: https://mathweb.ucsd.edu/~jverstra/PAPERS/maxc8-ElJCombRevised.pdf.
- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1 (first public 2011-08-02), https://arxiv.org/abs/1108.0451.
- DistanceRegular.org, *Incidence graphs*, https://www.math.mun.ca/distanceregular/indexes/incidencegraphs.html (graph taxonomy; no publication date claimed).
