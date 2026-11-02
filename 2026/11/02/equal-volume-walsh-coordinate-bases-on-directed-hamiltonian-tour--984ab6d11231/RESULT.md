# Equal-volume Walsh coordinate bases on directed Hamiltonian tours

## Finding

Let \(n\ge3\). A directed Hamiltonian tour on \([n]\) is an \(n\)-cycle permutation \(\pi\); write \(X_{ij}(\pi)=\mathbf1_{\{\pi(i)=j\}}\) for \(i\ne j\) and \(\chi_{ij}=1-2X_{ij}\). The set of admissible arcs is \(E=\{(i,j):i\ne j\}\), of size \(m=n(n-1)\). Let \(\mu\) be **any** probability measure assigning strictly positive mass to **every** directed Hamiltonian tour. Its arc covariance matrix is \(C_\mu\), and \(d=n(n-3)+1\).

Construct the *crown graph* \(H_n\) with left vertices \(i_L\), right vertices \(j_R\), and an edge \((i_L,j_R)\) for each arc \((i,j)\in E\). For an arbitrary selected arc set \(S\subseteq E\), put \(F=E\setminus S\). Let \(c(F)\) be the number of connected components of the graph of omitted arcs, **including isolated vertices**. Then

\[
\boxed{\dim\ker C_\mu[S,S]=c(F)-1.}
\]

The constant function and the selected Walsh characters are linearly independent exactly when the omitted graph is connected. The largest possible number of selected nonconstant characters is \(d\), and at that maximum the admissible choices are **exactly** the complements of spanning trees of \(H_n\). Their number is

\[
\boxed{\tau_n=(n-1)n^{n-2}(n-2)^{n-1}.}
\]

Even when \(\mu\) is nonuniform, all these saturated, nonsingular Walsh Gram determinants are **identical**. If \(\operatorname{pdet}C_\mu\) denotes the product of its \(d\) positive eigenvalues, then for every \(S\) of size \(d\) the probability-normalized Gram matrix \(G_\mu(S)\) of \((1,(\chi_e)_{e\in S})\) satisfies

\[
\boxed{\det G_\mu(S)=\begin{cases}
4^d\operatorname{pdet}(C_\mu)/\tau_n,&E\setminus S\text{ is a spanning tree of }H_n,\\
0,&\text{otherwise.}
\end{cases}}
\]

Consequently **all** \(\tau_n\) saturated independent coordinate sets are D-optimal among selections with \(d\) nonconstant Walsh characters, simultaneously for every strictly positive \(\mu\).

When \(\mu\) is uniform on the \((n-1)!\) tours, its complete centered arc-covariance spectrum is

| Eigenvalue | Multiplicity |
|---|---:|
| \(0\) | \(2n-1\) |
| \(1/(n-1)\) | \(n(n-3)/2\) |
| \(n/((n-1)(n-2))\) | \((n-1)(n-2)/2\) |

At \(n=3\) the middle multiplicity is zero. In particular every independent maximal Walsh Gram determinant for the uniform law equals

\[
\boxed{\frac{4^{n(n-3)+1}}{(n-1)n^{n-2}(n-2)^{n-1}}
\left(\frac1{n-1}\right)^{\!n(n-3)/2}
\left(\frac{n}{(n-1)(n-2)}\right)^{\!(n-1)(n-2)/2}.}
\]

The sharp ratio of positive centered eigenvalues is \(n/(n-2)\) for \(n\ge4\); at \(n=3\) there is only one positive eigenvalue, hence the ratio is \(1\). This condition number concerns the *full centered arc family on its intrinsic range*, not each individual selected coordinate submatrix.

## Assumptions and scope

All matrices are real and all ranks, kernels, and determinants are over \(\mathbb R\). The probability-normalized Gram matrix uses the inner product \(\langle f,g\rangle_\mu=\sum_{\pi} \mu(\pi) f(\pi)g(\pi)\), without dividing by the number of features. For every \(n\ge3\), every tour must have **positive** measure; zero weights can create extra dependencies. No claim is made for the undirected or loop-allowing tour ensembles. The cographic graph has \(2n\) vertices even when some omitted arcs are absent.

## Proof

**(1) Exact support and covariance kernel.** For the *uniform* law, a given arc occurs in \((n-2)!\) of the \((n-1)!\) directed Hamiltonian cycles, so its probability is \(p=1/(n-1)\). Two distinct arcs are jointly possible exactly when they have different tails and heads and are not reversals of one another: they then form disjoint directed paths, possibly one path of length two, and occur together in \((n-3)!\) tours, with probability \(q=1/((n-1)(n-2))\). Otherwise the pair probability is zero.

Let \(B\) be the \(2n\)-by-\(m\) unsigned vertex-edge incidence matrix of \(H_n\), \(T\) the arc-transposition matrix \((ij)\mapsto(ji)\), and \(J\) the all-ones matrix. The second-moment matrix is

\[
\mathbb E(XX^{\mathsf T})=(p+q)I-q(B^{\mathsf T}B+T)+qJ,
\]

hence

\[
C_{\mathrm{unif}}=(p+q)I-q(B^{\mathsf T}B+T)+(q-p^2)J.
\]

The bipartite graph \(H_n\) is connected for \(n\ge3\). Thus \(\operatorname{rank}B=2n-1\). Each row-sum and each column-sum of every tour matrix is \(1\), whence \(\operatorname{ran}B^{\mathsf T}\subseteq\ker C_\mu\) for *every* probability law \(\mu\).

For a vector \(v\in\ker B\), its total coordinate sum is zero, and the transpose map \(T\) preserves \(\ker B\). The covariance restriction is \((p+q)I-qT\). Splitting \(\ker B\) into \(T=+1\) symmetric and \(T=-1\) skew parts yields eigenvalues \(p\) and \(p+2q\). The symmetric part consists of zero-diagonal symmetric \(n\)-by-\(n\) matrices with all row sums zero; its dimension is \(n(n-3)/2\), since the unsigned incidence matrix of \(K_n\) has rank \(n\) for \(n\ge3\). The skew part has dimension \((n-1)(n-2)/2\) by the rank \(n-1\) of the oriented incidence matrix of \(K_n\). Both eigenvalues are positive whenever their eigenspaces are nonzero. Dimension counting therefore gives

\[\ker C_{\mathrm{unif}}=\operatorname{ran}B^{\mathsf T},\qquad
\operatorname{rank}C_{\mathrm{unif}}=n(n-3)+1=d.\]

For any full-support \(\mu\), a linear combination \(\sum_e z_eX_e\) has zero \(\mu\)-variance exactly when it is constant on *every* Hamiltonian tour. The same is true under the uniform law. It follows that \(\ker C_\mu=\ker C_{\mathrm{unif}}=\operatorname{ran}B^{\mathsf T}\), proving law-independent covariance rank and kernel. The stated uniform spectrum follows as well; \(p+2q=n/((n-1)(n-2))\).

**(2) Arbitrary selected coordinates.** Embed \(a\in\mathbb R^S\) into \(\mathbb R^E\) by extending it by zero on \(F\). It lies in \(\ker C_\mu\) exactly when \(a=B^{\mathsf T}z\) for vertex potentials \(z\in\mathbb R^{2n}\), with \(z_{i_L}+z_{j_R}=0\) on all omitted edges \((i,j)\in F\). Each component of the bipartite graph \((V(H_n),F)\) has one free alternating scalar potential, even if it consists of an isolated vertex, yielding a \(c(F)\)-dimensional solution space. The only potentials annihilated by \(B^{\mathsf T}\) are global alternating constants on connected \(H_n\), a one-dimensional kernel. Therefore \(\dim\ker C_\mu[S,S]=c(F)-1\). The block Gram determinant of constant and Walsh features equals \(4^{|S|}\det C_\mu[S,S]\) by a Schur-complement centering operation. Connected omitted graphs require at least \(2n-1\) edges; equality means a spanning tree.

**(3) Exact saturated determinants.** Choose the signed incidence \(A\) of the bipartite crown graph and delete one row, obtaining the full-row-rank \((2n-1)\)-by-\(m\) matrix \(A_0\). Multiplying some rows by \(-1\) converts between signed and unsigned incidence without changing row spaces. Put \(r=2n-1\). Choose an orthonormal \(m\)-by-\(d\) matrix \(U\) spanning \(\ker A_0\), and let \(V=A_0^{\mathsf T}(A_0A_0^{\mathsf T})^{-1/2}\), an orthonormal \(m\)-by-\(r\) matrix for the orthogonal complement. The square matrix \([U\ V]\) is orthogonal.

For complementary index sets \(S,F\), with \(|S|=d\), \(|F|=r\), the complementary-minor identity for an orthogonal matrix gives

\[|\det U[S,:]|^2=|\det V[F,:]|^2
=\frac{\det A_0[:,F]^2}{\det(A_0A_0^{\mathsf T})}.\]

The incidence matrix of a graph is totally unimodular, so the numerator is \(1\) precisely when \(F\) is a spanning tree, and otherwise \(0\). By the matrix-tree theorem the denominator is \(\tau_n\). As \(C_\mu=U D U^{\mathsf T}\) with \(D\) positive definite on \(\mathbb R^d\), \(\det D=\operatorname{pdet}C_\mu\), and

\[\det C_\mu[S,S]=\det D\,\det U[S,:]^2\]

establishes the common determinant for every strictly positive \(\mu\). No assumption that \(\mu\) is symmetric is needed.

**(4) Exact number of bases.** The \(2n\)-vertex crown graph is \((n-1)\)-regular. Its Laplacian spectrum is \(0\) once, \(2(n-1)\) once, \(n-2\) with multiplicity \(n-1\), and \(n\) with multiplicity \(n-1\). Indeed, diagonalizing the cross-part adjacency \(J_n-I_n\) on constant and zero-sum vectors immediately gives these four sectors. The eigenvalue form of the matrix-tree theorem now gives

\[\tau_n=\frac{2(n-1)\,n^{n-1}(n-2)^{n-1}}{2n}=(n-1)n^{n-2}(n-2)^{n-1}.\]

For the uniform law, multiply the two nonzero covariance eigenvalues to obtain the displayed explicit Walsh Gram determinant.

## Verification

Run `python3 checker.py` in the same directory. It requires only Python's standard library and deterministically enumerates all tours for \(3\le n\le7\), checks each exact one- and two-arc moment, and checks the predicted eigenvalue equations on fundamental-cycle generators of the crown incidence kernel. It enumerates every maximal coordinate set for \(n=3,4\), comparing determinant positivity with complementary-tree connectivity and verifying equal positive determinants. For \(n=4\), an intentionally asymmetric strictly positive tour law with weights \((1,2,3,4,5,9)\) is checked exhaustively; \(384\) of the \(792\) saturated coordinate sets are nonsingular, and all have covariance determinant \(5/221184\). The uniform \(n=4\) positive Walsh Gram determinant is \(64/729\). A deterministic collection of \(120\) coordinate sets at \(n=5\) receives an additional tree/determinant check. Numerical extrapolation is not used in the proof.

## Relationship to prior work

The dimension and row/column constraints of asymmetric travelling-salesperson tour polytopes, the total unimodularity of bipartite graph incidence matrices, and the matrix-tree theorem are classical. In particular, Fischetti studies facets of the asymmetric travelling-salesperson polytope [1], while Billera and Sarangarajan study its faces and relation to permutation-matrix polytopes [2]. Their dimension/face theory is not asserted as new here. Graph-incidence spanning-tree bases are a standard network-simplex theorem [3], and the design-theory literature relates D-optimality of certain *incomplete-block* designs to spanning-tree counts [4]. Those connections are distinct from the present all-law equality of maximal Walsh coordinate determinants on Hamiltonian tours and its exact uniform covariance spectrum. The statement is an explicitly derived combination, not a claim that its ingredients or the cographic-basis mechanism were previously unknown.

## Limitations

The claim is restricted to strictly positive laws on **all** directed Hamiltonian tours and to first-order arc coordinate Walsh features. The equal-volume identity does not claim that chosen coordinates have equal *condition numbers*, nor that determinants of different feature cardinalities are comparable. The general probability law has an explicit common determinant **in terms of its covariance pseudo-determinant**, not a closed expression independent of its weights. The uniform pseudo-determinant has the closed product above. An alternative equivalent formulation in older design-theory or polyhedral literature cannot be entirely excluded by the bounded literature review, especially the full text of [1], which was not available for material comparison. Independent mathematical validation has not been performed.

## References

[1] M. Fischetti, “Facets of the Asymmetric Traveling Salesman Polytope,” *Mathematics of Operations Research* 16(1) (1991), 42–56. First published online 1991-02-01. https://doi.org/10.1287/moor.16.1.42

[2] L. J. Billera and A. Sarangarajan, “All 0–1 Polytopes are Traveling Salesman Polytopes,” Cornell University Technical Report No. 1086 (February 1994); public full-text scan at https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Billera/BilleraSarangtsp.pdf. The report cover verifies the publication **month**, not an exact day.

[3] F. Furini, *Network Optimization: Bases and spanning trees*, https://fabiofurini.github.io/network-optimization/network-simplex/network-simplex/bases-and-spanning-trees/; and *Total unimodularity and integrality*, https://fabiofurini.github.io/network-optimization/flows/network-flow-models/total-unimodularity-and-integrality/.

[4] R. A. Bailey and A. Sajjad, “Optimal Incomplete-Block Designs with Low Replication: A Unified Approach Using Graphs,” *Journal of Statistical Theory and Practice* 15, article 84 (2021), https://doi.org/10.1007/s42519-021-00215-x.
