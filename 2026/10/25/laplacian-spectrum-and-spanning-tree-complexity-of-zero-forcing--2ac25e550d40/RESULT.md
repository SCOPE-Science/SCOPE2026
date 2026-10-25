# Laplacian spectrum and spanning-tree complexity of zero-forcing reconfiguration graphs of uniform clique bouquets

## Finding
For integers \(r\ge3\) and \(m\ge2\), write \(G_{r,m}=K_1\vee(rK_m)\) for the graph consisting of \(r\) cliques of order \(m+1\) sharing precisely their one universal vertex. A set of blue vertices is **zero forcing** if repeating the rule “a blue vertex with exactly one white neighbor colors that neighbor blue” eventually makes every vertex blue. Let \(R_{r,m}\) be the simple graph whose vertices are *minimum-cardinality* zero-forcing sets of \(G_{r,m}\), two such sets adjacent exactly when their symmetric difference has size two. Let \(L=L(R_{r,m})\) be the ordinary unnormalized graph Laplacian and let \(\chi_{r,m}(\lambda)=\det(\lambda I-L)\).

Define \(c_t=\binom rt(m-1)^t\). The complete spectral factorization is
\[
\begin{aligned}
\chi_{r,m}(\lambda)
&=\lambda(\lambda-r-m)(\lambda-(r+1)m)^{r-1}
(\lambda-r(m+1))^{(m-1)^r}\
&\qquad\cdot\prod_{t=1}^{r-1}
\left[(\lambda-(r+t+1)m)^{r-t-1}
\left(\lambda^2-[r+(3t+1)m]\lambda
+mt[2r+1+(2t+1)m]\right)\right]^{c_t}.
\end{aligned}
\]
It is a polynomial of degree \(N=m^{r-1}(m+r)\), the number of minimum zero-forcing sets. The least positive Laplacian eigenvalue has multiplicity \(r(m-1)\) and is
\[
\lambda_2(R_{r,m})=\frac{r+4m-\sqrt{r^2+4m(m-1)}}{2}.
\]
The **number of spanning trees** of the reconfiguration graph is
\[
\tau(R_{r,m})=(r+1)^{r-1}[r(m+1)]^{(m-1)^r}
\prod_{t=1}^{r-1}
\left(mt[2r+1+(2t+1)m]\right)^{c_t}
\left[(r+t+1)m\right]^{(r-t-1)c_t}.
\]
These are consequences of the one spectral factorization, not separate unrelated claims.

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. The hub vertex is \(h\), and the disjoint peripheral parts \(U_1,\ldots,U_r\) each have cardinality \(m\). In particular, \(m\ge2\) ensures that a fully blue part can force the hub. The graph \(R_{r,m}\) uses only minimum *ordinary* zero-forcing sets, not all feasible sets, not positive-semidefinite or leaky forcing sets, and adjacency means one-for-one token exchange. Eigenvalues use \(L=D-A\), not the normalized Laplacian. The formulas are claimed for all integers \(r\ge3,m\ge2\), with no upper bound.

## Proof
**1. Characterize feasible white complements.** Let \(W=V(G_{r,m})\setminus S\). If two vertices of one peripheral clique are white, they are adjacent true twins, so no exterior blue vertex can force either while both remain white. Thus every zero-forcing set has \(|W\cap U_i|\le1\). If \(W\) contains the hub together with one white vertex of every peripheral part, then every blue peripheral vertex sees both the hub and its part's white vertex; there is no possible initial force. Hence \(|W|\le r\). Conversely, suppose these constraints hold. If the hub is blue, every part with a white vertex also has a blue vertex that can force it. If the hub is white, \(|W|\le r\) ensures that some peripheral part is entirely blue; a vertex of that part first forces the hub, and the preceding argument applies. Therefore the maximum feasible white sets have size \(r\), choose at most one vertex per part (including the hub singleton), and omit exactly one of the \(r+1\) parts. Consequently the minimum zero-forcing size is \(1+r(m-1)\) and \(R_{r,m}\) is the basis-exchange graph of this explicitly described rank-\(r\) truncated partition matroid.

**2. Describe its vertices and edges.** Type \(A\) configurations omit the hub and choose one white vertex from each peripheral part: there are \(m^r\). Type \(B_i\) configurations contain the hub and omit peripheral part \(i\), choosing one white vertex from each of the other \(r-1\) parts: there are \(m^{r-1}\) for each \(i\). Exchanging one member gives: within \(A\), change one coordinate; within \(B_i\), change one retained coordinate; between \(A\) and \(B_i\), replace the \(i\)-th peripheral representative by the hub; between \(B_i\) and \(B_j\), exchange representatives of omitted/retained parts while the other coordinates agree. This exhausts every edge because any two maximum complements differ by precisely two elements exactly in these cases. Thus \(|V(R_{r,m})|=m^{r-1}(m+r)\).

**3. Decompose the Laplacian.** For each coordinate space \(\mathbb R^m\), split into the constants \(\mathbf1\) and its orthogonal mean-zero subspace \(V\) of dimension \(m-1\). Tensor products give a direct sum of invariant harmonic sectors indexed by a subset \(T\subseteq[r]\): coordinates in \(T\) belong to \(V\), all others are constant. Put \(t=|T|\) and \(s=r-t\). A sector has one \(A\)-coordinate, and one \(B_i\)-coordinate for each \(i\notin T\); the sector appears with multiplicity \((m-1)^t\). The restricted Laplacian for any fixed tensor basis vector has matrix
\[
M_T=\begin{pmatrix}
r+mt & -\mathbf1_s^\mathsf T\
-m\mathbf1_s & (r+t+1)mI_s-mJ_s
\end{pmatrix}
\]
(the nonsymmetric presentation is due only to unnormalized constant-coordinate bases; it is similar to a real symmetric matrix). This matrix is checked directly from the four edge types: \(A\)-to-\(B_i\) sends one chosen representative to the hub, whereas \(B_i\)-to-\(A\) sums over all \(m\) possible representatives. Changing a mean-zero coordinate has Laplacian contribution \(m\), while changing a constant coordinate contributes zero. Each \(B_i\)-to-\(B_j\) transfer sums over an omitted coordinate, contributing \(-m\).

For \(s\ge1\), the \(s-1\) differences among the \(B_i\) coordinates have eigenvalue \((r+t+1)m\); the remaining two-dimensional block (the \(A\) coordinate and uniform \(B_i\) direction) has characteristic polynomial
\[
q_t(\lambda)=\lambda^2-[r+(3t+1)m]\lambda+mt[2r+1+(2t+1)m].
\]
When \(t=0\), \(q_0(\lambda)=\lambda(\lambda-r-m)\). When \(t=r\), there are no \(B_i\) sectors and the sole eigenvalue is \(r(m+1)\), with multiplicity \((m-1)^r\). Multiplying factors over the \(\binom rt\) choices of \(T\) proves the displayed factorization.

**4. Lowest positive eigenvalue.** For \(1\le t<r\) the two-dimensional block is similar to the symmetric matrix
\[
\begin{pmatrix}
r+mt&-\sqrt{m(r-t)}\
-\sqrt{m(r-t)}&(2t+1)m
\end{pmatrix}.
\]
Its lower eigenvalue increases strictly with \(t\): both diagonal entries increase, and the magnitude of the negative off-diagonal entry decreases. More formally, a Rayleigh minimizer for such a matrix can be taken coordinatewise nonnegative, and on nonnegative vectors its quadratic form strictly increases as \(t\) increases. The \(t=1\) lower root is less than the \(t=0\) positive root \(r+m\), because its first diagonal entry equals \(r+m\) but has a nonzero off-diagonal entry. The additional eigenvalues \((r+t+1)m\) are at least \((r+1)m>r+m\), and \(r(m+1)>r+m\). Therefore \(\lambda_2\) is the lower root of \(q_1\). Its discriminant is \(r^2+4m(m-1)\), giving the claimed formula and multiplicity \(r(m-1)\).

**5. Trees.** The Laplacian has exactly one zero eigenvalue (also clear from the factorization), so the reconfiguration graph is connected. The matrix-tree theorem gives \(\tau(R_{r,m})=N^{-1}\prod_{\lambda_j>0}\lambda_j\). For \(t\ge1\), the product of the roots of \(q_t\) is its constant term \(mt[2r+1+(2t+1)m]\). The \(t=0\) sector contributes \((r+m)[(r+1)m]^{r-1}\). Dividing by \(N=(r+m)m^{r-1}\) leaves \((r+1)^{r-1}\); together with the remaining factors this proves the spanning-tree product.

## Verification
Run the two independent standard-library Python scripts `verify.py` and `verify_laplacian.py` from the same folder. The first enumerates all initial blue sets for several small clique bouquets, runs the zero-forcing process independently of the structural criterion, and compares their actual minimum forcing-set exchange graphs with the predicted combinatorics. The second builds the exchange graph directly and performs exact integer Bareiss determinant tests: \(\det(L+uI)\) for \(u\in\{1,2,5\}\), and one Kirchhoff cofactor, for \((r,m)\in\{(2,2),(2,3),(3,2),(3,3),(4,2)\}\). Its output is stored in `verification_output.txt`. All tested determinant comparisons agree. The all-parameter statement is proved in the preceding steps rather than inferred from finite tests.

## Relationship to prior work
Boyer et al. introduced and studied the zero-forcing polynomial [1]. Geneson, Haas, and Hogben introduced the minimum-set exchange reconfiguration graph and studied common graph families [2]. Neither article derives this spectral factorization for uniform clique bouquets. Later work by X. Wang establishes broader descriptions and polynomials for ordinary and leaky forcing sets in common-clique unions [3]; therefore the underlying minimum-set classification and forcing polynomial are **not** claimed as new here, and serve solely as input to the new Laplacian calculation. Spectral work on rank-two matroid basis graphs with a single parallel class [4] concerns a different matroid structure; it does not give the stated rank-at-least-three uniform-partition spectral blocks or the resulting product. The originality claim is the complete factorization (and its exact spectral and tree consequences), not the elementary partition-matroid encoding.

## Limitations
The theorem does not cover unequal peripheral clique sizes, arbitrary block graphs, the normalized or signless Laplacian, or mixing-time bounds for a specified Markov chain. Literature priority remains susceptible to unindexed work on truncated partition matroid basis graphs. The two computational verifiers check finite instances only. No independent mathematical audit has been performed.

## References
[1] K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (first public version 2018-01-26), https://arxiv.org/abs/1801.08910.

[2] J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (first public version 2020-09-01), https://arxiv.org/html/2009.00220v1.

[3] X. Wang, *Modular Compression of Leaky Forts and Leaky Forcing Polynomials* (2026), https://www.researchgate.net/publication/405317381_Modular_Compression_of_Leaky_Forts_and_Leaky_Forcing_Polynomials.

[4] *Laplacian factorization and an eigenspace transition for rank-two parallel-class matroid polytopes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-laplacian-factorization-and-an-eigenspace-transition-for-rank-tw--b10901525680.
