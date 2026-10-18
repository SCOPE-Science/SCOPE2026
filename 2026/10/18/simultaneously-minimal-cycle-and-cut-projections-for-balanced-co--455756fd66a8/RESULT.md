# Simultaneously minimal cycle and cut projections for balanced complete multipartite graphs

## Finding

Let \(r\ge3\) and \(p\ge2\) be integers, and let \(G=K_{p,\ldots,p}\) be the unweighted complete \(r\)-partite graph whose parts all have \(p\) vertices. Give the real edge-coordinate space \(\mathbb R^{E(G)}\) any \(\ell_q\) norm, \(1\le q\le\infty\). For any reference orientation, let \(D\) be its vertex-edge incidence matrix; set \(Z=\ker D\) (cycle/flow space) and \(B=\operatorname{ran}(D^{\mathsf T})\) (cut space). Let \(P\) and \(Q\) be the Euclidean orthogonal projections onto \(Z\) and \(B\), respectively, so \(P+Q=I\).

**Theorem.** For every real \(1\le q\le\infty\), \(P\) minimizes operator norm among all real linear projections from \(\ell_q^{E(G)}\) onto \(Z\), and \(Q\) independently minimizes operator norm among all such projections onto \(B\). The two orthogonal projections are the unique projections onto their respective ranges commuting with all graph-automorphism-induced signed edge permutations. At the endpoint norms, their exact minimum values are

\[
\begin{aligned}
\min_{R^2=R,\,\operatorname{ran}R=Z}\|R\|_{\ell_1\to\ell_1}
&=\|P\|_{\ell_1\to\ell_1}
=3+\frac{2}{r}-\frac{8(rp-1)}{r(r-1)p^2},\\[3pt]
\min_{R^2=R,\,\operatorname{ran}R=B}\|R\|_{\ell_1\to\ell_1}
&=\|Q\|_{\ell_1\to\ell_1}
=2+\frac{2}{r}-\frac{4(rp-1)}{r(r-1)p^2}.
\end{aligned}
\]

The same sharp values hold on \(\ell_\infty^{E(G)}\); both minimum values on \(\ell_2^{E(G)}\) equal \(1\). For fixed \(p\), the first endpoint constant is strictly increasing in \(r\) when \(2\le p\le4\), strictly decreasing in \(r\) when \(p\ge8\), and increases to a unique finite peak before decreasing when \(5\le p\le7\).

## Assumptions and scope

All spaces and maps are over \(\mathbb R\). An edge is assigned coefficient one in every \(\ell_q\) norm. The orientation only changes signs of coordinate vectors and therefore does not affect any norm or minimum. A projection onto \(Z\) means a linear idempotent with **range exactly** \(Z\), considered on the entire edge-coordinate space; likewise for \(B\). The theorem concerns relative, not absolute, projection constants. It does not assert uniqueness among all norm-minimizing projections, only uniqueness among projections invariant under the stated automorphism action.

The graph has \(rp\) vertices and \(\binom r2p^2\) edges. Its cycle and cut dimensions are \(\binom r2p^2-rp+1\) and \(rp-1\). Both are nonzero on the stated domain.

## Proof

**1. Group action and fixed-flow lemma.** Regard an edge vector as an antisymmetric flow \(z_{xy}=-z_{yx}\) supported on adjacent vertices. A graph automorphism acts by relabeling vertices; in any fixed edge orientation this is a signed permutation of the edge coordinates and is an isometry of every real \(\ell_q\) norm. Write \(\Gamma\) for the full automorphism group. Both \(Z\) and \(B\) are invariant; the induced action is orthogonal for the Euclidean inner product.

Fix a vertex \(v\) in part \(A\). We claim that the only divergence-free flow fixed by its stabilizer \(\Gamma_v\) is zero. An invariant flow takes one constant value \(b\) on all edges directed from \(v\) to vertices outside \(A\), and one constant value \(a\) on all edges directed from any vertex in \(A\setminus\{v\}\) to vertices outside \(A\), by independent within-part permutations and permutations of the other parts. Every edge joining two parts different from \(A\) has flow zero: a stabilizer automorphism can exchange its endpoints by swapping those two equally sized parts. Zero divergence at \(v\) forces \((r-1)p b=0\), hence \(b=0\). At any vertex outside \(A\), zero divergence now forces \((p-1)a=0\), hence \(a=0\) since \(p\ge2\). This proves the claim.

The vectors \(D^{\mathsf T}\delta_v\), as \(v\) runs over the vertices, span \(B\) and each is fixed by \(\Gamma_v\). If \(T:B\to Z\) commutes with \(\Gamma\), then \(T(D^{\mathsf T}\delta_v)\) is a \(\Gamma_v\)-fixed cycle, hence zero. Therefore \(T=0\). If \(S:Z\to B\) commutes with \(\Gamma\), its Euclidean adjoint \(S^{\mathsf T}:B\to Z\) also commutes, so \(S=0\).

**2. Optimality in every exponent.** Any projection \(R\) onto \(Z\) can be written \(R=P+TQ\) with \(T:B\to Z\). If \(R\) commutes with \(\Gamma\), so does \(T\), hence \(R=P\) by step 1. Every projection \(R\) onto \(Z\), invariant or not, has an average \(\overline R=|\Gamma|^{-1}\sum_{g\in\Gamma}gRg^{-1}\). This remains a projection onto \(Z\) because it fixes every element of \(Z\) and has range contained in \(Z\); it is invariant, hence equals \(P\). As the group acts isometrically in every \(\ell_q\), convexity gives \(\|P\|_q\le\|R\|_q\). The same argument, using the vanishing maps \(Z\to B\), proves uniqueness and minimality of \(Q\) for every \(q\). Both are nonzero orthogonal projections, so their \(\ell_2\) norms are \(1\).

**3. Transfer-current computation.** The orthogonal cut projector equals \(Q=D^{\mathsf T}(DD^{\mathsf T})^+D\), with the superscript \(+\) denoting the Moore–Penrose pseudoinverse. Fix an edge \(e=uv\), where \(u\) lies in part \(A\) and \(v\) in distinct part \(C\), and choose its orientation \(u\to v\). Introduce

\[
 b_0=\frac1{(r-1)p^2},\quad c_0=\frac1{rp^2},\quad
 U=(p-1)b_0+c_0=\frac{rp-1}{r(r-1)p^2},\quad V=b_0-c_0.
\]

Set the potential \(h\) to be \(U\) at \(u\), \(-V\) at the other vertices of \(A\), \(-U\) at \(v\), \(V\) at the other vertices of \(C\), and zero elsewhere. Its coordinates sum to zero. The Laplacian identity \(DD^{\mathsf T}h=\delta_u-\delta_v\) follows directly from every vertex having degree \((r-1)p\) and the adjacency sums over the other parts. Thus \(Q\delta_e=D^{\mathsf T}h\). All its entries can be grouped by graph-edge type:

| Edge type | Multiplicity | Absolute coefficient in \(Q\delta_e\) |
|---|---:|---:|
| The chosen edge | \(1\) | \(2U\) |
| One endpoint chosen, the other in the opposite chosen part | \(2(p-1)\) | \(U-V=(p-2)b_0+2c_0\) |
| Neither endpoint chosen, across the two chosen parts | \((p-1)^2\) | \(2V\) |
| A chosen endpoint joined to one of the remaining parts | \(2p(r-2)\) | \(U\) |
| An unchosen vertex of a chosen part joined to a remaining part | \(2p(p-1)(r-2)\) | \(V\) |
| Between two remaining parts | All remaining edges | \(0\) |

Because \(p\ge2\), every displayed absolute value is nonnegative as written. Summation and simplification give

\[
 S:=\|Q\delta_e\|_1
=2U+2(p-1)(U-V)+2(p-1)^2V+2p(r-2)U+2p(p-1)(r-2)V
=2+\frac2r-\frac{4(rp-1)}{r(r-1)p^2}.
\]

The diagonal coefficient of \(Q\delta_e\) is \(2U\), with \(0<2U<1\) on the stated domain. Therefore \(\|P\delta_e\|_1=1-2U+(S-2U)=1+S-4U\), yielding the first endpoint formula. The automorphism group acts transitively on unoriented edges, so every column of each projector has the same absolute column sum. The operator \(\ell_1\) norm is the maximum absolute column sum; hence the formulas are exact operator norms, not merely upper bounds. Finally, \(P\) and \(Q\) are real symmetric matrices, so their \(\ell_\infty\) norms equal their \(\ell_1\) norms. Step 2 establishes optimality at both endpoints.

**4. Part-count transition.** Writing the first formula as \(L(r,p)\), exact subtraction gives

\[
L(r+1,p)-L(r,p)
=-\frac{2\bigl[(p^2-4p)r-(p^2+4p-8)\bigr]}
{p^2r(r-1)(r+1)}.
\]

For \(p\le4\) the bracket is negative for every \(r\ge3\), while for \(p\ge8\) it is positive for every \(r\ge3\). For \(5\le p\le7\), the bracket changes sign once at \(r_*=(p^2+4p-8)/(p^2-4p)\), which exceeds \(3\) and is not an integer. The unique peak is at \(r=8\), \(r=5\), and \(r=4\), respectively for \(p=5,6,7\).

## Verification

A standalone Python 3 script, `verify.py`, uses only exact rational arithmetic. Across \(20\) finite graph sizes (\(3\le r\le7\), \(2\le p\le5\)) it checks the potential Laplacian identity, zero divergences of projected columns, and both proposed sharp endpoint norms on each of \(2970\) edge columns. For the smaller cases it additionally verifies \(5353\) matrix entries of \(P^2=P\). It checks \(780\) further exact finite-difference identities for the transition formula. These are finite consistency tests; the statements for all integer parameters and all exponents rely on the preceding proof.

To reproduce: run `python3 verify.py` from the directory containing this document and the program. No network access or external Python packages are needed.

## Relationship to prior work

The invariant-projection framework and its representation-theoretic uniqueness criterion are developed by Dilworth, Kutzarova, and Ostrovskii in their 2023 preprint, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582, first submitted 21 May 2023). Their explicit families include tori and Hamming graphs. The present theorem treats the different two-parameter family of balanced complete multipartite graphs and explicitly computes both complementary projection constants, including their simultaneous optimality for all real \(\ell_q\) norms.

The same authors' earlier *Analysis on Laakso graphs with application to the structure of transportation cost spaces* (arXiv:2007.07949, 2020) examines multibranching diamond graphs; its one-level graphs correspond to complete bipartite graphs. The present domain requires at least three parts, so no bipartite special case is asserted as new. Known complete-graph calculations apply to part size one; that case is likewise excluded. General graph-equivariance principles provide a starting point but do not supply the explicit multipartite formulas or their part-count phase transition without the new stabilizer and transfer-current calculations.

## Limitations

The claim concerns equal part sizes and unit edge weights; unequal sizes or arbitrary positive edge weights break the stated permutation symmetry and are not addressed. For intermediate exponents other than \(2\), the theorem proves simultaneous optimality but does not provide closed forms for the numerical operator norms. It does not assert that the orthogonal minimizer is the only minimizer without an equivariance restriction. A search of relevant literature and research records did not reveal the exact two-parameter result, but cannot exclude an equivalent formulation in unindexed sources. Independent external review has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (21 May 2023), https://arxiv.org/abs/2305.12582. Published in *Proceedings of Symposia in Pure Mathematics* 106 (2024), pp. 97–131.
2. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949v1 (15 July 2020), https://arxiv.org/abs/2007.07949.
