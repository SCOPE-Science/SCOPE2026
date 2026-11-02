# Sharp two-sided projection constants for triangular graph edge spaces

## Finding

For every integer \(n\ge5\), let \(G=J(n,2)=L(K_n)\) be the triangular graph on the two-element subsets of \([n]\), with an edge whenever two subsets meet in one element. Give its real oriented edge space \(\mathbb R^{E(G)}\) the coordinate \(\ell_1\) norm. Write \(C=\operatorname{im} B^{\mathsf T}\) for its cut/gradient space and \(Z=\ker B\) for its circulation space, where \(B\) is any vertex-edge signed incidence matrix.

The exact relative projection constants are

\[
\inf_{P^2=P,\,\operatorname{im}P=C}\|P\|_{1\to1}
=\frac{(n-2)(3n-1)}{n(n-1)},\qquad
\inf_{P^2=P,\,\operatorname{im}P=Z}\|P\|_{1\to1}
=\frac{2(2n-5)}{n-1}.
\]

Both infima are attained by the complementary Euclidean orthogonal projections \(Q=B^{\mathsf T}(BB^{\mathsf T})^+B\) and \(R=I-Q\), respectively. Each of these is the **unique projection invariant under the induced action of the label-permutation group** \(S_n\) onto its respective range. Here \((\cdot)^+\) is the Moore–Penrose inverse. The exact norm gap is

\[
\|R\|_{1\to1}-\|Q\|_{1\to1}
=\frac{n^2-3n-2}{n(n-1)}>0,
\]

and the constants converge to \(4\) and \(3\), respectively, as \(n\) increases. The endpoint \(n=4\) is the familiar octahedral/complete-tripartite graph and is not asserted as a new case.

## Assumptions and scope

All graphs are simple, finite, undirected, unweighted, and connected; \(n\) is an integer at least \(5\). An arbitrary reference orientation is fixed. On \(\mathbb R^{E(G)}\), \(\|x\|_1=\sum_{e\in E(G)}|x_e|\). The incidence matrix \(B\) has \(+1\) at the tail and \(-1\) at the head of an oriented edge. Thus \(BB^{\mathsf T}\) is the combinatorial vertex Laplacian. A projection is any real linear idempotent with the stated range, not necessarily symmetric or group-invariant. The relative projection norm is its operator norm in the given ambient \(\ell_1\) edge space.

The number of vertices is \(N=\binom n2\), every vertex has degree \(2(n-2)\), and the number of graph edges is \(M=N(n-2)\). Consequently, \(\dim C=N-1\) and \(\dim Z=M-N+1\).

## Proof

**1. The invariant circulation obstruction.** Let \(H\subseteq S_n\) fix the vertex \(u=\{1,2\}\). Its action has three vertex orbits: \(A=\{u\}\), \(D=\{\{a,j\}:a\in\{1,2\},\,j\ge3\}\), and \(F=\{\{i,j\}:3\le i<j\le n\}\). Every edge within \(D\) or within \(F\) can have its endpoints interchanged by some element of \(H\). A signed edge flow invariant under \(H\) therefore vanishes on these edges. There is exactly one \(H\)-orbit of edges between \(A\) and \(D\), and one between \(D\) and \(F\). Their signed flows each have a single scalar amplitude. An invariant circulation has zero divergence at \(u\), forcing the first amplitude to vanish; it has zero divergence at any vertex of \(F\), forcing the second to vanish. Hence \(Z^H=\{0\}\).

Let \(s_v=B^{\mathsf T}\mathbf 1_v\) be the oriented vertex star. This lies in \(C\), is invariant under the stabilizer of \(v\), and the family \(\{s_v\}\) spans \(C\). If a projection onto \(Z\) commutes with all label permutations, it sends each \(s_v\) into the stabilizer-fixed part of \(Z\), which is zero. As it is the identity on \(Z\), it must be \(R\). Now let \(T\) be the difference between an invariant projection onto \(C\) and \(Q\). It maps \(Z\) into \(C\) and annihilates \(C\); its Euclidean adjoint therefore restricts to an equivariant map \(C\to Z\). The same star argument forces this map, and hence \(T\), to vanish. Thus \(Q\) and \(R\) are the unique \(S_n\)-invariant projections onto their ranges. Averaging an arbitrary projection over \(S_n\) retains its range and idempotence and does not increase its \(\ell_1\)-operator norm, since every induced signed edge permutation is an isometry. Hence both \(Q\) and \(R\) minimize the norms **among all projections**.

**2. Exact potential for one edge column.** Fix the oriented graph edge \(e=(\{1,2\},\{1,3\})\), with the first vertex its tail. Put

\[
a=\frac{n+1}{2n(n-1)},\qquad b=\frac1{2n(n-1)}.
\]

Define a potential \(\phi\) on the vertices of \(G\) by \(\phi(\{1,2\})=a\), \(\phi(\{1,3\})=-a\), \(\phi(\{2,j\})=b\) and \(\phi(\{3,j\})=-b\) for \(4\le j\le n\), and zero elsewhere. It has mean zero. Directly counting neighbors shows that \((BB^{\mathsf T}\phi)(\{1,2\})=(2n-3)a-(n-3)b=1\), \((BB^{\mathsf T}\phi)(\{2,j\})=(n+1)b-a=0\), and every remaining coordinate is zero except the antisymmetric entry \(-1\) at \(\{1,3\}\). Thus \(BB^{\mathsf T}\phi=B\mathbf 1_e\). The \(e\)-column of \(Q\) is therefore \(B^{\mathsf T}\phi\).

**3. Exact edge-column norms.** Only five types of edges give a nonzero absolute potential difference. Their multiplicities and absolute differences are, respectively:

| Edge type | Number | Difference |
|---|---:|---:|
| \(+a\) to \(-a\) | \(1\) | \(2a\) |
| \(\pm a\) to the corresponding \(\pm b\) | \(2(n-3)\) | \(a-b\) |
| \(\pm a\) to zero | \(2(n-2)\) | \(a\) |
| \(\pm b\) to zero | \(2(n-3)(n-2)\) | \(b\) |
| \(+b\) to \(-b\) | \(n-3\) | \(2b\) |

Summing gives

\[
\sum_f |Q_{fe}|=4(n-2)a+2(n-3)(n-2)b
=\frac{(n-2)(3n-1)}{n(n-1)}.
\]

The diagonal value is \(Q_{ee}=2a=(n+1)/(n(n-1))<1\). Consequently, \(\sum_f|R_{fe}|=1+\sum_f|Q_{fe}|-2Q_{ee}=2(2n-5)/(n-1)\). The group \(S_n\) acts transitively on (undirected) edges and changes only column signs under orientation choices, so these column sums equal the full \(\ell_1\)-operator norms. Step 1 makes them sharp global projection constants, completing the proof.

## Verification

Run `python3 johnson_cycle_checker.py` using Python 3 standard library. The script constructs every edge and every potential column for \(3\le n\le9\) with exact rational arithmetic; verifies \(BB^{\mathsf T}\phi=B\mathbf 1_e\), symmetry and incidence identities of \(Q\), the uniform column norms of \(Q\) and \(I-Q\), and the diagonal effective-resistance value. The expected terminating output is `CHECK_OK: exact incidence, potential, symmetry, and full column norms`.

These finite checks are supplementary. The derivation for every integer \(n\ge5\), especially global optimality without an invariance restriction, is proved in the preceding paragraphs.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023 preprint, published 2024) develop invariant projections on graph cycle spaces, emphasizing tori and Hamming graphs. Their uniqueness argument based on stabilizer-fixed cycles motivates the present analysis, but their inspected statements do not supply the sharp triangular-graph formulas. Abascal et al. (2018) study Johnson-graph vertex eigenspaces and projections onto those eigenspaces, which are different operators on a different ambient space from the edge-space cycle and cut projections here. The lower-order identity \(J(4,2)\cong K_{2,2,2}\) is part of the pre-existing complete-multipartite regime and is not the new theorem. The result is not an implication of either cited numerical theorem; its additional stabilizer calculation and exact edge-column sum are required.

## Limitations

The formulas cover \(J(n,2)\) for integers \(n\ge5\) with unit edges and real \(\ell_1\) edge norms; they are not claims about arbitrary Johnson graphs \(J(n,k)\), nonuniform weights, general \(\ell_p\) edge norms, or extrinsic projection constants. The invariant projections are unique, but arbitrary norm-minimizing projections are not claimed to be unique. Literature searches cannot establish absolute historical priority, and equivalent formulas under other terminology remain possible. No independent audit has been performed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public version 2023-05-21; Proceedings of Symposia in Pure Mathematics 106 (2024). https://arxiv.org/abs/2305.12582
2. J. Abascal, A. Bah, M. Banuelos, D. Uminsky and O. Vasquez, *A non-iterative parallelizable eigenbasis algorithm for Johnson graphs*, arXiv:1812.04230, first public version 2018-12-11. https://arxiv.org/abs/1812.04230
