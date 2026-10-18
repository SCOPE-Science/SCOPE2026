# An exact degree-parity conditional law for odd spanning-tree counts in uniform random graphs

## Finding
Let \(G\) be a uniformly sampled simple labeled graph on \(n\ge2\) vertices (each edge independently present with probability \(1/2\)). Write \(D=(\deg_G(i)\bmod2)_{i=1}^n\in\mathbb F_2^n\), let \(\tau(G)\) be its number of spanning trees (zero if disconnected), and put
\[
 a_k=\prod_{j=1}^{k}(1-2^{1-2j}),\qquad a_0=1.
\]
For every \(d\in\mathbb F_2^n\) with even coordinate sum, the conditional event is well-defined and obeys the complete formula
\[
 \Pr\{\tau(G)\text{ is odd}\mid D=d\}=
 \begin{cases}
 a_{(n-1)/2},&n\text{ odd, for every }d,\\
 0,&n\text{ even and }d=0,\\
 a_{(n-2)/2},&n\text{ even and }d\ne0.
 \end{cases}
\]
In particular, when \(n\) is odd, the parity of the spanning-tree count is **independent of the entire vertex-degree parity vector**, not merely of an individual degree parity. For even \(n\), the only exceptional degree-parity pattern is the all-even one. In both nonzero cases the conditional probability converges to \(\prod_{j\ge1}(1-2^{1-2j})\approx0.4194224418\) as the order grows.

## Assumptions and scope
All graphs here are finite, simple, undirected and labeled; there are no loops or parallel edges. The random graph is \(G(n,1/2)\), not a nonuniform-density graph. The handshaking identity forces the coordinate sum of \(D\) to be even. Conversely, every such vector occurs with positive probability: the linear map from edge indicators to the degree-parity vector is onto the even-sum subspace. We do not condition on exact integer degrees, only their residues modulo two. The finite product \(a_k\) is strictly positive for every \(k\ge0\).

## Proof
**1. The degree-constrained Laplacian minor.** Work over \(\mathbb F_2\). The matrix-tree theorem says \(\tau(G)\bmod2=\det B\), where \(B\) is the \((n-1)\)-square principal cofactor of the graph Laplacian. Put \(m=n-1\), and condition on \(D=d\). The \(\binom m2\) edges within vertices \(1,\dots,m\) can still be chosen independently and uniformly. Indeed, each edge from vertex \(i\le m\) to vertex \(n\) is then forced to equal \(d_i+\sum_{j\le m,j\ne i}A_{ij}\) in \(\mathbb F_2\), and the final vertex parity is automatically \(d_n\), by the even-sum constraint. This is a bijective parameterization of the conditioning fibre. Thus \(B\) is a **uniform symmetric \(m\)-square binary matrix with prescribed diagonal** \(b=(d_1,\dots,d_m)\): its off-diagonal upper-triangle entries are independent fair bits.

**2. Diagonal classes.** For a symmetric matrix \(H\) over \(\mathbb F_2\) and invertible \(P\), one has \(\operatorname{diag}(P^THP)=P^T\operatorname{diag}(H)\), because cross terms cancel in characteristic two. Congruence therefore gives a bijection between matrices of a prescribed nonzero diagonal vector and those of diagonal \(e_1\), since \(\mathrm{GL}_m(\mathbb F_2)\) acts transitively on nonzero vectors. Let \(p_0(m)\) and \(p_1(m)\) denote nonsingularity probabilities for zero and nonzero diagonal respectively. For zero diagonal, the matrices are alternating, so \(p_0(m)=0\) for odd \(m\). For even dimension \(2k\), the first off-diagonal row is nonzero with probability \(1-2^{-(2k-1)}\). Conditional on being nonzero, a nonsingular change of basis and symplectic elimination split off a nondegenerate alternating plane; the residual alternating form is uniform in dimension \(2k-2\). Hence
\[
 p_0(0)=1,\quad p_0(2k)=(1-2^{1-2k})p_0(2k-2)=a_k.
\]

**3. Nonzero diagonal.** By the congruence symmetry take the diagonal to be \(e_1\). Write
\[
 H=\begin{pmatrix}1&v^T\\v&C\end{pmatrix},
\]
where \(v\) is uniform and \(C\) is an independent uniform alternating matrix of dimension \(m-1\). Schur complementation of the top-left entry shows \(H\) is nonsingular precisely when \(C+vv^T\) is nonsingular.

If \(m\) is odd, \(C\) has even dimension. When \(C\) is nonsingular, the inverse \(C^{-1}\) is alternating, so \(v^TC^{-1}v=0\); the rank-one update remains nonsingular. When \(C\) is singular, its radical has even dimension at least two, so a rank-one update cannot restore full rank. It follows that \(p_1(m)=p_0(m-1)=a_{(m-1)/2}\).

If \(m\) is even, \(C\) has odd dimension \(r=m-1\). Its radical has odd dimension, and a rank-one update can give nonsingularity only when \(\dim\ker C=1\). In that case, for a nonzero radical vector \(w\), nonsingularity is equivalent to \(v^Tw=1\), which has conditional probability \(1/2\). Count all alternating forms \(C\) of dimension \(r\) with a one-dimensional radical: choose its nonzero radical line (\(2^r-1\) choices), then a nondegenerate alternating form on the \((r-1)\)-dimensional quotient. Out of the \(2^{r(r-1)/2}\) alternating forms, their proportion is \((2^r-1)2^{-(r-1)}p_0(r-1)\). Multiplying by \(1/2\) gives
\[
 p_1(m)=(1-2^{-r})p_0(r-1)=p_0(m)=a_{m/2}.
\]
These arguments include the boundary \(m=1\), using \(p_0(0)=1\).

**4. Substitute the graph parameters.** The conditional vector \(b\) vanishes if and only if the entire feasible degree-parity vector \(d\) vanishes: the last component is the sum of the preceding ones. When \(n\) is odd, \(m\) is even and \(p_0(m)=p_1(m)=a_{m/2}\). When \(n\) is even, \(m\) is odd and \(p_0(m)=0\), while \(p_1(m)=a_{(m-1)/2}\). These are exactly the three displayed cases. The infinite product converges to a positive constant since \(\sum_{j\ge1}2^{1-2j}<\infty\).

## Verification
The accompanying standalone `verify.py` performs exhaustive graph enumeration for every \(2\le n\le6\), computes degree-parity vectors and Laplacian-cofactor determinants directly over \(\mathbb F_2\), and compares all conditional frequencies with the formula by exact rational arithmetic. It additionally enumerates all symmetric matrices with every possible fixed diagonal through dimension five, checking the claimed diagonal-class nonsingularity probabilities. These finite checks are corroboration, not substitutes for the all-order argument above. Execute with `python verify.py` (Python standard library only).

## Relationship to prior work
The degree-residue problems and random symmetric binary matrix rank counts used by Balister, Powierski, Scott and Tan motivated examining a different statistic on the same random-graph fibres: the parity of the spanning-tree count. Their full-text analysis of parity-conditioned partitions includes MacWilliams' unconditional rank count but does not state this conditional spanning-tree parity law. Eppstein proves the deterministic obstruction that every even-order Eulerian graph has an even spanning-tree count; the zero case above is consistent with, but not the entire content of, that theorem. Wood establishes the limiting unconditioned sandpile-group distribution, including the approximately \(0.4194\) limiting probability of an odd number of spanning trees, whereas the present result conditions on **each entire labeled degree-parity vector and is exact for every finite order**. The product factors derive from standard alternating-form counting, but their exact conditional graph-level invariance requires the fibre bijection and diagonal congruence argument.

## Limitations
The statement concerns only parity, not the full integer spanning-tree count, exact degree sequences, or arbitrary edge probabilities. It does not supply a new general enumeration of binary symmetric matrices; it uses well-known alternating-form counting. It does not establish historical priority against all possible differently indexed treatments of random Laplacians. The result is proved mathematically and has received no independent audit.

## References
1. P. Balister, E. Powierski, A. Scott, and J. Tan, *Counting partitions of \(G_{n,1/2}\) with degree congruence conditions*, arXiv:2105.12612, first posted 26 May 2021; Random Structures & Algorithms 62 (2023), 564–584. https://arxiv.org/abs/2105.12612
2. D. Eppstein, *On the Parity of Graph Spanning Tree Numbers*, Technical Report 96-14, University of California, Irvine, 1996. https://www.ics.uci.edu/~eppstein/pubs/Epp-TR-96-14.pdf
3. M. M. Wood, *The distribution of sandpile groups of random graphs*, arXiv:1402.5149 (2014), J. Amer. Math. Soc. 30 (2017), 915–958. https://arxiv.org/abs/1402.5149
4. J. MacWilliams, *Orthogonal matrices over finite fields*, American Mathematical Monthly 76 (1969), 152–164 (rank-count theorem cited in Reference 1).
