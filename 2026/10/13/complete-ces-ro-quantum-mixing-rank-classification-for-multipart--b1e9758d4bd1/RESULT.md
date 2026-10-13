# Complete Cesàro quantum-mixing rank classification for multipartite graphs

## Finding

For any integer \(r\ge 2\) and arbitrary positive integers \(n_1,\ldots,n_r\), let \(G=K_{n_1,\ldots,n_r}\) be the connected, simple, unweighted complete multipartite graph with \(N=\sum_i n_i\) vertices. Write \(d=\#\{i:n_i=2\}\) and \(s=\#\{i:n_i=1\}\). Its adjacency continuous-time quantum walk has Cesàro average mixing matrix
\[
\widehat M(G)=\lim_{T\to\infty}\frac1T\int_0^T
\bigl(e^{itA(G)}\circ e^{-itA(G)}\bigr)\,dt,
\]
where \(\circ\) denotes entrywise product. The exact rank is
\[
\boxed{\operatorname{rank}\widehat M(G)=N-d-\mathbf 1_{\{s=2\}}.}
\]
More strongly, the full kernel is spanned by the difference of the two standard basis vectors within each part of size two, together with the difference of the two singleton-part vertices **exactly when** there are precisely two singleton parts. These kernel vectors have disjoint supports and are linearly independent. Consequently \(\widehat M(G)\) is positive definite precisely when there is no part of size two and the number of singleton parts is not two.

For example, \(K_{1,1,2}\) (the diamond graph) has rank \(2\) on four vertices, whereas \(K_{1,1,1}\) has full rank three. For \(K_{2,2,\ldots,2}\) the rank is half the graph order.

## Assumptions and scope

Vertices of different parts are adjacent and vertices of the same part are nonadjacent. The Hamiltonian is the **adjacency matrix**, not the graph Laplacian or its normalized version. All parts and all multiplicities are arbitrary, subject to \(r\ge2\) and \(n_i\ge1\). The average is the ordinary infinite-time Cesàro mean, not an optimized time-sampling distribution. An empty span is understood as the zero subspace. The number of singleton parts may be zero or one. No assumptions of regularity, simple eigenvalues, or distinct part sizes are made.

## Proof

**1. Spectral-projector formula and positivity.** Write the real symmetric adjacency spectral decomposition as \(A=\sum_{\lambda}\lambda E_\lambda\), where the sum is over **distinct** eigenvalues and \(E_\lambda\) is the orthogonal projector onto the full corresponding eigenspace. Expanding \(e^{itA}\circ e^{-itA}\) and averaging each scalar exponential shows, without a nonresonance hypothesis, that
\[
\widehat M=\sum_{\lambda}E_\lambda\circ E_\lambda.
\]
Every term is positive semidefinite by the Schur product theorem, so the kernel of the sum is the intersection of the kernels of its terms.

**2. The exact zero-eigenvalue projector.** Let \(V_i\) denote part \(i\), and \(\mathbf1_i\) its indicator. The space of vectors supported on \(V_i\) with coordinate sum zero is an adjacency eigenspace of eigenvalue zero. In addition, any vector constant on each part, with value \(a_i\) on \(V_i\), has eigenvector equations
\[
\lambda a_i=S-n_i a_i,\qquad S=\sum_j n_j a_j.
\]
If \(\lambda=0\), then \(n_i a_i=S\) for every \(i\), and \(S=rS\) implies \(S=0\) because \(r\ge2\). Thus there are no extra zero modes. Writing \(I_i,J_i\) for identity and all-ones matrices on part \(i\), the projector is precisely
\[
E_0=\bigoplus_{i:n_i\ge2}\left(I_i-\frac1{n_i}J_i\right),
\]
with zero blocks on singleton parts. Its Schur square has blocks
\[
(E_0\circ E_0)|_{V_i}=\left(1-\frac2{n_i}\right)I_i+\frac1{n_i^2}J_i
\qquad(n_i\ge2).
\]
On the constant direction of a part this has eigenvalue \(1-1/n_i>0\); on each internal contrast it has eigenvalue \(1-2/n_i\), zero exactly for \(n_i=2\). Therefore \(\ker(E_0\circ E_0)\) consists exactly of all vectors supported on singleton vertices, plus one contrast line per part of size two. Every contrast vector of a part of size at least three is already excluded.

**3. The singleton contrast projector.** Let \(s\) be the number of singleton parts and let \(W\) be their union, of size \(s\). If \(s\ge2\), the \((-1)\)-eigenspace consists exactly of vectors supported on \(W\) whose coordinates sum to zero. Indeed, for a part-constant eigenvector of eigenvalue \(-1\), the eigenvector equations become \((n_i-1)a_i=S\). A singleton forces \(S=0\), so all nonsingleton part values vanish. Conversely any zero-sum vector on \(W\) is a \((-1)\)-eigenvector. If \(s=0\), the same equations force \(S=0\), since otherwise \(1=\sum_i n_i/(n_i-1)>1\); hence no \((-1)\)-eigenvector arises on the part-constant space. If \(s=1\), the possible singleton contrast space has dimension zero. Thus, for \(s\ge2\),
\[
E_{-1}|_W=I_s-\frac1sJ_s,\qquad
(E_{-1}\circ E_{-1})|_W=\left(1-\frac2s\right)I_s+\frac1{s^2}J_s,
\]
with zeros off \(W\). The latter matrix is strictly positive definite on \(W\) for \(s\ge3\), while for \(s=2\) it is \(J_2/4\), whose kernel is exactly the difference of the two singleton vertices.

**4. The one-singleton boundary.** If \(s=1\), the previous projector is absent. Since the graph is connected, the Perron eigenvalue is simple with a strictly positive real unit eigenvector \(v\), and its projector is \(E_\rho=vv^{\mathsf T}\). Its Schur square equals \((v\circ v)(v\circ v)^{\mathsf T}\), which has a strictly positive entry on the unique singleton coordinate. Consequently the intersection of \(\ker(E_0\circ E_0)\) with \(\ker(E_\rho\circ E_\rho)\) has no singleton-supported vector. For \(s=0\) the zero-eigenvalue projector already excludes every direction except the pair contrasts; for \(s\ge2\) the \((-1)\)-projector excludes all singleton directions except the single contrast when \(s=2\).

**5. No other projector removes the claimed null vectors.** Any eigenvector for an eigenvalue other than zero is orthogonal to the within-part zero-eigenspace and hence constant on each part. Therefore every such spectral projector has equal columns (and rows) at the two vertices of a size-two part, as does its entrywise square; \(E_0\circ E_0\) also annihilates their difference as shown above. Similarly, when there are exactly two singleton parts, any eigenvector at an eigenvalue other than \(-1\) is orthogonal to their difference, hence has equal coordinates there. All corresponding projectors and their entrywise squares annihilate that difference, while \(E_{-1}\circ E_{-1}=J_2/4\) on those coordinates also annihilates it. Thus all the exhibited difference vectors lie in the kernel of **every** Schur-square summand.

Steps 2–4 give an upper bound \(d+\mathbf1_{\{s=2\}}\) on the nullity, while Step 5 gives exactly that many independent kernel vectors. Equality follows, proving the rank and positive-definiteness classification.

## Verification

An accompanying standalone Python/NumPy checker `verify.py` constructs the adjacency matrix and the independent matrix spectral-projector sum for every nondecreasing part-size list with \(2\le r\le5\), sizes \(1\) through \(4\), and graph order at most \(18\). It compares the numerically computed nullity against the formula for \(119\) graphs, checks row stochasticity and each predicted kernel vector, and uses exact rational arithmetic to validate the \(0\) and \((-1)\) projection formulas on \(86\) smaller cases. Reproduce from the containing directory by running `python3 verify.py` (NumPy required). The expected success output includes `VERIFY_OK independent_matrix_cases=119 exact_projector_cases=86 distinct_eigenvalue_groups=526 diamond_rank=2/4`.

The finite computations check the formulas independently on specified examples; the proof above, not the enumeration, establishes the claim for every admissible collection of part sizes.

## Relationship to prior work

The fundamental expansion of average mixing into Schur squares of adjacency spectral projectors is due to Godsil and is explained explicitly by Coutinho, Godsil, Guo and Zhan. The latter also developed rank/combinant-algebra methods and treated various small graphs. Baptista, Coutinho and Marques consider generalized observation-time sampling and compare it with the ordinary Cesàro average. Their short-path and complete-bipartite sampling examples do not state the present standard-average nullspace classification for arbitrary unequal part sizes. Known complete-graph and some regular cases are special instances; the precise and uniform distinction between independent parts of size two and the two-singleton boundary is obtained here from the exact kernel calculation. An earlier cycle/balanced-multipartite paper addresses instantaneous uniform mixing, which has a different quantifier and cannot imply the rank formula.

## Limitations

The theorem is for real, symmetric, unweighted **adjacency** quantum walks, not Laplacian or discrete/coined models. It does not give the complete nonzero eigenvalue spectrum of the average mixing matrix, mixing times, or optimized randomized-time uniformity. It is possible that a differently phrased published structural theorem on equitable partitions or spectral projector Schur products entails this classification; literature search alone cannot eliminate that risk. The computational checker is finite and is not a certification of the unrestricted theorem.

## References

1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, v3, https://arxiv.org/html/1103.2578v3.
2. G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, v1, https://arxiv.org/html/1709.03591v1.
3. P. Baptista, G. Coutinho and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378, first public version 31 August 2023, https://arxiv.org/html/2308.16378v1.
4. J. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236, https://arxiv.org/abs/2404.02236.
5. P. Lo, S. Rajaram, D. Schepens, D. Sullivan, C. Tamon and J. Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059, https://arxiv.org/abs/quant-ph/0509059.
