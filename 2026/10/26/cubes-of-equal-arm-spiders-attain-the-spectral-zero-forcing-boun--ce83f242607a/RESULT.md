# Cubes of equal-arm spiders attain the spectral zero-forcing bound

## Finding

**Theorem.** Let \(m\ge2\) and \(\ell\ge4\) be integers. Let \(T=S_m(\ell)\) be the tree with one central vertex and \(m\) internally disjoint arms, each a path of \(\ell\) edges. Then, for the ordinary third power, in which two distinct vertices are adjacent if their distance in \(T\) is at most three,
\[
Z(T^3)=M(T^3)=3(m-1).
\]
Here \(Z\) is the ordinary zero-forcing number and \(M\) is maximum nullity over real symmetric matrices with exactly the prescribed nonzero off-diagonal positions. In particular, the real minimum rank of \(T^3\) is \(1+m\ell-3(m-1)\). This proves the third-power case of Conjecture 10 in Abiad--Flagg--Ghasemi Nezhad--Zeijlemaker (2026) for all its admissible numbers of arms and arm lengths.

## Assumptions and scope

All graphs are finite, simple, and undirected. The center is \(c\), and the vertex at distance \(j\) on arm \(i\) is \(v_{i,j}\), for \(1\le i\le m\) and \(1\le j\le\ell\). The symbol \(T^3\) denotes graph power with distances at most three, **not** the strict third power with edges only at exact distance three. A black vertex may color its unique white neighbor black. A zero-forcing set is a black starting set from which every vertex can eventually be colored. No claim is made for arm lengths below four, unequal-arm spiders, or graph powers four and above.

## Proof

Write \(A\) for the adjacency matrix of \(T\), and let
\[
\lambda_j=2\cos\!\left(\frac{j\pi}{\ell+1}\right),\qquad j=1,2,3.
\]
These are three distinct eigenvalues of the adjacency matrix of the \(\ell\)-vertex path. Every \(\lambda_j\) is also an eigenvalue of \(A\) with multiplicity at least \(m-1\). Indeed, let \(x^{(j)}\) be a nonzero eigenvector of the path matrix for \(\lambda_j\). On arm \(i\), assign the coordinate vector \(a_i x^{(j)}\), and assign zero at the center, where the real numbers \(a_i\) satisfy \(\sum_{i=1}^m a_i=0\). The eigenvector equation holds at every arm vertex because the center coordinate vanishes, and at the center because the first arm coordinates sum to zero. The coefficient space has dimension \(m-1\). The eigenspaces for the three distinct eigenvalues are independent, supplying \(3(m-1)\) dimensions in total.

Put \(s_1=\lambda_1+\lambda_2+\lambda_3\), \(s_2=\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3\), and \(s_3=\lambda_1\lambda_2\lambda_3\). Consider the real symmetric matrix
\[
Q=(A-\lambda_1 I)(A-\lambda_2 I)(A-\lambda_3 I)
 = A^3-s_1A^2+s_2A-s_3I.
\]
Its kernel contains the three independent eigenspaces just constructed, so \(\operatorname{null}(Q)\ge3(m-1)\). We check that its off-diagonal support is **exactly** \(T^3\), a necessary step before invoking the maximum-nullity bound.

Because \(T\) is a tree, any two vertices at distance exactly two have one two-step walk between them and no three-step walk, so \(Q_{uv}=-s_1\) at distance two. Also \(Q_{uv}=1\) at distance three, since there is a unique three-step geodesic; and \(Q_{uv}=0\) at distance greater than three. For adjacent vertices \(u,v\), the tree has no common neighbor, and
\[
Q_{uv}=(A^3)_{uv}+s_2=\deg_T(u)+\deg_T(v)-1+s_2.
\]
Every edge has one endpoint of degree at least two, hence \((A^3)_{uv}\ge2\). If \(\ell\ge5\), the three \(\lambda_j\) are nonnegative and the first two are positive, giving \(s_1>0\) and \(s_2\ge0\). If \(\ell=4\), the three eigenvalues are \(\varphi,\varphi^{-1},-\varphi^{-1}\), with \(\varphi=(1+\sqrt5)/2\); therefore \(s_1=\varphi>0\) and \(s_2=(\sqrt5-3)/2>-2\). Thus \(Q_{uv}\ne0\) for all adjacent vertices, while the distance-two entries are nonzero because \(s_1>0\). We conclude \(Q\in\mathcal S(T^3)\) and consequently
\[
3(m-1)\le\operatorname{null}(Q)\le M(T^3)\le Z(T^3).
\]

For the converse, initially color the three outermost vertices on every arm except the \(m\)-th black. Within each of the first \(m-1\) arms, process \(t=\ell-3,\ell-4,\ldots,1\), using \(v_{i,t+3}\) to force \(v_{i,t}\). Such a source lies at depth at least four, has no neighbors in the other arms or at the center in \(T^3\), and all its same-arm neighbors except its target have already been colored. Once the first \(m-1\) arms are black, use \(v_{1,3}\) to force \(c\), then \(v_{1,2}\) to force \(v_{m,1}\), then \(v_{1,1}\) to force \(v_{m,2}\), and then \(c\) to force \(v_{m,3}\). Finally, for \(t=4,5,\ldots,\ell\), use \(v_{m,t-3}\) to force \(v_{m,t}\). All these forces are valid by the distance rule, and the initial set has exactly \(3(m-1)\) vertices. Hence \(Z(T^3)\le3(m-1)\), finishing the proof.

## Verification

Run the included standalone checker with `python3 verify.py` from the package directory. It checks the prescribed forcing seed and the cubic matrix's exact off-diagonal support on forty parameter pairs \(2\le m\le6\), \(4\le\ell\le11\); checks three independent arm-antisymmetric eigenmodes numerically for each; and independently enumerates every smaller candidate zero-forcing set on eight small cases (specified by the checker's output). The general proof is symbolic and does not depend on these finite checks.

## Relationship to prior work

The 2026 paper of Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker proves the upper bound \(Z(S_m(\ell)^k)\le (m-1)k\), states equality as Conjecture 10, and supplies a polynomial-spectral lower-bound criterion in Theorem 20. The new point here is an admissible triple of path eigenvalues for **every** \(\ell\ge4\), a uniform verification of every mandatory matrix-support entry, and the resulting sharp cubic bound for all \(m\). These facts are not automatic from the 2026 conditional spectral theorem. The explicit upper-bound forcing schedule is included for completeness and was already available in that paper.

DeAlba and collaborators (2012) treat ordinary powers of paths and strict powers of trees; strict powers differ from the ordinary cube here. Chang and Lin's work on powers of cycles and trees proves equality of maximum nullity and zero forcing for **squares** of arbitrary trees, not their ordinary cubes. The square-power case is therefore not presented as a contribution.

## Limitations

No claim is made for fourth or higher powers, for unequal arm lengths, or for shorter arms. The main research source explicitly poses a stronger conjecture encompassing all powers; this theorem resolves only its complete cubic subfamily. The result and finite numerical tests have received the specified self-review only, not independent audit or independent mathematical validation. Unindexed or otherwise inaccessible prior equivalent findings remain a residual publication-priority risk.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first posted 2026-10-02), Sections 3 and 4, particularly Proposition 9, Conjecture 10, Theorem 20, and Example 23. https://arxiv.org/abs/2610.03892
2. L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald, and A. Yielding, *Minimum rank of powers of trees*, Electronic Journal of Linear Algebra 23 (2012), 151–163. https://doi.org/10.13001/1081-3810.1511
3. G. J. Chang and J. C.-H. Lin, *Minimum rank of powers of cycles and trees*, publicly available manuscript, Section 4 (squares of trees). https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
4. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648.
