# Parity-fused counting refinement in symplectic oppositeness graphs

## Finding
Let \(q\) be any prime power, \(n\ge2\), and \(V\) a \(2n\)-dimensional vector space over \(\mathbb F_q\) with a nondegenerate alternating bilinear form. Let \(G_{n,q}\) have as vertices all Lagrangian (maximal totally isotropic) \(n\)-subspaces; distinct vertices are adjacent exactly when their intersection is zero. Fix one vertex \(A\), give it a singleton colour, and give every other vertex a common colour. For \(0\le s\le n\) put
\[
\mathcal O_s=\{X:\dim(X\cap A)=s\}.
\]
The stable ordinary one-dimensional colour-refinement partition, with synchronous rounds counted from the initial marking, is **exactly**:

- For even \(n\ge4\): all \(n+1\) individual classes \(\mathcal O_0,\ldots,\mathcal O_n\); stabilization is reached in **three rounds**, and three is necessary.
- For odd \(n\ge3\): \(\mathcal O_0\), \(\mathcal O_n\), and the unions \(\mathcal O_{2i-1}\cup\mathcal O_{2i}\) for \(1\le i\le(n-1)/2\); this is reached **by two rounds** and is already stable (one round suffices when \(n=3\); two rounds are necessary for odd \(n\ge5\)). There are exactly \((n+3)/2\) classes, strictly coarser than the \(n+1\) orbit strata of the symplectic stabilizer of \(A\).
- For \(n=2\): the three classes \(\mathcal O_0,\mathcal O_1,\mathcal O_2\) are reached after **one round**.

Thus an odd/even rank transition controls whether a single individualized Lagrangian allows two-variable counting logic \(C^2\) to recover its complete geometric intersection profile. The order of each stratum is
\[
|\mathcal O_s|={n\brack s}_q\,q^{(n-s)(n-s+1)/2},
\]
where the brackets denote a Gaussian binomial coefficient. Class sizes in the odd case are sums of the paired sizes. This is an **intra-graph** colour-class statement, not a claim that \(G_{n,q}\) is identified against every other graph by \(C^2\).

## Assumptions and scope
The graph relation is **oppositeness** (zero-dimensional intersection), not adjacency in the usual dual polar graph (intersection dimension \(n-1\)). All finite fields, including characteristic two, are covered. A round replaces a colour by the pair consisting of the old colour and the multiset of neighbours' old colours. The initial colour of \(A\) is distinct. We work with the entire Lagrangian vertex set; no external field coordinatization or extra unary predicates enter the graph. As usual, a Gaussian coefficient is zero outside \(0\le t\le m\) and \({0\brack0}_q=1\).

## Proof
**1. Geometric orbits and the symmetric-matrix quotient.** By the symplectic extension principle (or a basis construction), the subgroup of the symplectic group fixing \(A\) acts transitively on each \(\mathcal O_s\). Choosing \(s\)-dimensional \(A\cap X\) and then a transverse Lagrangian in its symplectic quotient gives the stated size formula. Hence each \(\mathcal O_s\) is equitable as part of the full orbit partition, and refinement cannot split it.

Let \(p_{s,t}\) be the number of neighbours \(Y\in\mathcal O_t\) of a fixed \(X\in\mathcal O_s\). Select a symplectic basis \((e_1,\ldots,e_n,f_1,\ldots,f_n)\) with \(A=\langle e_1,\ldots,e_n\rangle\) and \(X=\langle e_1,\ldots,e_s,f_{s+1},\ldots,f_n\rangle\). Its transverse Lagrangian \(C=\langle f_1,\ldots,f_s,e_{s+1},\ldots,e_n\rangle\) identifies all neighbours of \(X\) with graphs of symmetric \(n\)-by-\(n\) matrices \(T:C\to X\). The intersection \(Y\cap A\) is the kernel of the principal symmetric block of \(T\) indexed by the last \(m=n-s\) coordinates: the first \(s\) input coordinates must be zero to eliminate the \(f_1,\ldots,f_s\) components, and the remaining \(f_{s+1},\ldots,f_n\) components vanish precisely on that kernel.

Write \(N_j=j(j+1)/2\), and let \(I_q(h)\) count invertible symmetric \(h\)-by-\(h\) matrices, with \(I_q(0)=1\). Counting choices of the kernel \(t\)-subspace and a nondegenerate symmetric form on its quotient gives the **full equitable quotient**
\[
p_{s,t}=q^{N_n-N_m}{m\brack t}_q I_q(m-t)
       =q^{N_n}H_m(t),\qquad
H_m(t)={m\brack t}_q q^{-(N_m-N_{m-t})}\eta_{m-t},
\]
where \(m=n-s\) and \(\eta_h=I_q(h)/q^{N_h}\). In particular, every vertex has degree \(q^{N_n}\).

**2. Nonsingular symmetric matrices in every characteristic.** For all \(h\ge0\),
\[
\eta_h=\prod_{j=1}^{\lceil h/2\rceil}(1-q^{-(2j-1)}).
\]
Here is a derivation rather than an appeal to a matrix table. Extend a symmetric \((h-1)\)-by-\((h-1)\) matrix by a uniformly chosen last row, column and diagonal. If the upper-left matrix has nullity zero, nonsingularity of the extension has probability \(1-q^{-1}\). If it has nullity one, the extension is nonsingular exactly when the appended linear functional does not annihilate its kernel, again with probability \(1-q^{-1}\). Higher nullity cannot produce a nonsingular extension. Since the proportion of \((h-1)\)-matrices with nullity one is \({h-1\brack1}_q q^{-(h-1)}\eta_{h-2}\),
\[
\eta_h=(1-q^{-1})\bigl(\eta_{h-1}+{h-1\brack1}_q q^{-(h-1)}\eta_{h-2}\bigr).
\]
Starting from \(\eta_0=1\) and \(\eta_1=1-q^{-1}\), substitution yields \(\eta_{2j}=\eta_{2j-1}\) and \(\eta_{2j+1}=\eta_{2j}(1-q^{-(2j+1)})\), proving the product. The block-extension argument uses only matrix rank and works in characteristic two.

**3. A parity-cancellation lemma for the quotient rows.** Set \(D_m(t)=H_m(t)-H_{m-1}(t)\), \(1\le m\le n\), interpreting absent coefficients as zero. For every \(t\) with \(0\le t<m\), let \(h=m-t\). Using
\[
\frac{{m\brack t}_q}{{m-1\brack t}_q}=\frac{q^m-1}{q^{m-t}-1}
\]
and the product for \(\eta\), direct cancellation yields
\[
D_m(t)=\begin{cases}
-q^{-m}H_{m-1}(t),&h\text{ odd},\\[2pt]
\dfrac{q^{-h}-q^{-m}}{1-q^{-h}}H_{m-1}(t),&h\text{ even}.
\end{cases}
\]
Furthermore \(D_m(m)=q^{-N_m}\). For \(h\ge3\) odd, the Gaussian ratio
\[
\frac{H_{m-1}(t+1)}{H_{m-1}(t)}
=\frac{1-q^{-(h-1)}}{q^{t+1}-1}
\]
proves \(D_m(t+1)=q^{-m}H_{m-1}(t)=-D_m(t)\). For \(h=1\) the same identity follows directly from \(H_m(m)=q^{-N_m}\) and \(H_{m-1}(m-1)=q^{-N_{m-1}}\). Thus **consecutive quotient rows with parameters \(m,m-1\) have equal sums in consecutive columns \((t,t+1)\) whenever \(m-t\) is odd**. When \(m\) is even also \(D_m(0)=0\); when \(m\) is odd the first cancelling pair is \((0,1)\). These identities hold for every prime power \(q\).

**4. First two refinement rounds.** Initially just \(A=\mathcal O_n\) is marked. Round one separates \(\mathcal O_0\), its neighbours, from the other nonanchor vertices. For any \(s\notin\{0,n\}\), the round-two signature is determined by the number of neighbours in \(\mathcal O_0\), which by Step 1 is \(p_{s,0}=q^{N_n}\eta_{n-s}\). The factors in Step 2 imply that \(\eta_{2j}=\eta_{2j-1}\) and that the values for successive \(j\) decrease strictly. Consequently for odd \(n\) round two gives exactly the pairs \((\mathcal O_1,\mathcal O_2),(\mathcal O_3,\mathcal O_4),\ldots\), along with \(\mathcal O_0\) and \(\mathcal O_n\). For even \(n\ge4\), round two gives the singleton \(\mathcal O_1\), then the pairs \((\mathcal O_2,\mathcal O_3),(\mathcal O_4,\mathcal O_5),\ldots\), along with \(\mathcal O_0\) and \(\mathcal O_n\). For \(n=2\) the three rank strata already appear at round one; for \(n=3\), round one already gives the odd-rank stable partition, whereas odd \(n\ge5\) requires round two.

**5. Why odd rank stops and even rank separates.** When \(n\) is odd, each paired pair of rows has \(s=2i-1\) and \(s+1=2i\), hence \(m=n-s\) even. Step 3 gives identical neighbour counts into both singleton cells and into every current pair \(\mathcal O_{2j-1}\cup\mathcal O_{2j}\). This is an equitable partition, so no subsequent refinement can split it.

When \(n\ge4\) is even, a current unresolved pair has \(s=2i\), \(s+1=2i+1\), with \(m=n-s\) even and \(m\ge2\). The round-two cell \(\mathcal O_1\) is a singleton stratum. Step 3 gives
\[
p_{s,1}-p_{s+1,1}
=-q^{N_n-m}H_{m-1}(1)<0.
\]
Thus round three separates every unresolved pair, making each \(\mathcal O_s\) an individual colour class. Because round two has unresolved pairs for all even \(n\ge4\), three rounds are necessary. These exhaustive cases prove the theorem. \(\square\)

## Verification
Two independent, standard-library Python programs accompany this result. `verify_direct.py` constructs every Lagrangian and the **full actual oppositeness graph** over \(\mathbb F_2\) in ranks two, three and four, runs synchronous refinement, and checks vertex counts, degrees, and the exact partition in each round; it covers 15, 135, and 2,295 vertices. `verify_quotient.py` obtains the equitable quotient **independently** from Gaussian-binomial moment inversion and verifies the claimed stable partitions for 35 parameter cases (\(q=2,3,4,5\), ranks through twelve), together with exhaustive symmetric-matrix rank distributions over \(\mathbb F_2\) in dimensions at most five and over \(\mathbb F_3\) in dimensions at most four. Execute each with Python 3.11+ in the directory containing the program. Their captured outputs are included. These tests are finite corroboration; the all-parameter theorem is proved by Steps 1–5.

## Relationship to prior work
Worawannotai (2012) studies the usual dual polar graph and its Terwilliger algebra, providing the classical distance-stratified perspective. Moorhouse and Williford (2015) develop association schemes based on symplectic dual polar graphs and describe every distance relation, including the oppositeness relation. Kiefer, Schweitzer and Selman (2015) give the general equivalence between two-variable counting types and colour refinement, including orbit-related distinctions. We use the classical symplectic geometry and matrix counting framework but establish **which of the geometric strata are actually separated by the single-anchor colour-refinement iteration on the oppositeness graph**. None of the inspected statements directly gives the odd-rank parity fusion, even-rank sharp three-round recovery, or the two-round odd stabilization. Existing association-scheme intersection parameters may encode the same quotient implicitly; the priority of this precise logical consequence needs independent specialist review.

## Limitations
No claim of novelty for the classical symplectic orbit decomposition, Gaussian coefficient formulas, symmetric-matrix rank census, or dual-polar association scheme is made. The odd-rank result is a strict coarsening of the **symplectic stabilizer** orbit decomposition; this theorem does not independently determine whether a larger full graph automorphism group merges some of those strata. Even rank gives equality with the full marked graph's automorphism orbits because the symplectic stabilizer is transitive on each separated stratum. The theorem does not give an identification sentence against arbitrary competing graphs, and does not cover point-line incidence graphs, other polar types, or multiple marked vertices. The finite tests are not substitutes for the infinite proof; possible specialized prior formulations remain a priority risk.

## References
1. Chalermpong Worawannotai, *Dual polar graphs, the quantum algebra \(U_q(\mathfrak{sl}_2)\), and Leonard systems of dual \(q\)-Krawtchouk type*, arXiv:1205.2144, first public 2012-05-10. https://arxiv.org/abs/1205.2144
2. Sandra Kiefer, Pascal Schweitzer, Erkal Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first public 2015-03-30. https://arxiv.org/abs/1503.08792
3. G. Eric Moorhouse and Jason Williford, *Double Covers of Symplectic Dual Polar Graphs*, arXiv:1504.01067, first public 2015-04-04. https://arxiv.org/abs/1504.01067
