# Central-binomial endpoint projection norms on antipodally augmented hypercubes

## Finding

For each integer \(n\geq5\), let \(F_n\) be the simple graph on \(\mathbb F_2^n\) in which two vertices are adjacent exactly when their Hamming distance is \(1\) or \(n\). Thus \(F_n\) is the ordinary binary \(n\)-cube augmented by the perfect matching of antipodal pairs. Equip its real unoriented edge-coordinate space with the standard Euclidean inner product and its coordinate \(\ell_1\) and \(\ell_\infty\) norms. Let \(Q_n\) be the Euclidean-orthogonal projection onto the cut space and \(P_n=I-Q_n\) the corresponding projection onto the cycle space. Put \(k=\lceil n/2\rceil\) and \(c_k=4^{-k}\binom{2k}{k}\). Then

\[
\|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}
=\frac n2+1-c_k,
\qquad
\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}
=\frac n2+2-c_k-\frac{4(1-2^{-n})}{n+1}.
\]

Every edge column realizes each asserted norm. In particular, adding the antipodal matching increases the **cut projection** endpoint norm over that of the ordinary \(n\)-cube by exactly

\[
\frac12-4^{-\lceil n/2\rceil}\binom{2\lceil n/2\rceil}{\lceil n/2\rceil}>0.
\]

The central-binomial correction is constant between each consecutive odd and even dimension: writing \(b_n=\|Q_n\|_{1\to1}-n/2\), one has \(b_{2k-1}=b_{2k}=1-c_k\) for every \(k\ge3\). As \(n\to\infty\),

\[
\|Q_n\|_{1\to1}=\frac n2+1-\sqrt{\frac{2}{\pi n}}+O(n^{-3/2}),
\qquad
\|P_n\|_{1\to1}=\frac n2+2-\frac4{n+1}-\sqrt{\frac{2}{\pi n}}+O(n^{-3/2}).
\]

## Assumptions and scope

The graph \(F_n\) is unweighted, connected, simple, and has \(2^n\) vertices and \((n+1)2^{n-1}\) edges. All projections are **canonical Euclidean-orthogonal** projections in real edge coordinates; no assertion is made about minimum norms among arbitrary nonorthogonal projections. Edge orientations are arbitrary and change neither the norms nor the absolute column sums.

Fix an oriented incidence matrix \(D\) with one column per edge. The cut space is \(\operatorname{im}(D^{\mathsf T})\), the cycle space is \(\ker D\), and \(Q_n=D^{\mathsf T}(DD^{\mathsf T})^+D\), where the superscript \(+\) denotes the Moore–Penrose pseudoinverse. Since these operators are real symmetric, their induced \(\ell_1\) and \(\ell_\infty\) norms agree. The theorem addresses \(n\ge5\); lower dimensions are used only as verification controls because they coincide with familiar smaller graph families.

## Proof

**1. Edge transitivity.** Write \(F_n\) as the Cayley graph of \(V=\mathbb F_2^{n+1}/\langle\mathbf1\rangle\), with one generator for the image of each coordinate vector \(e_i\). A representative can be uniquely chosen with first bit zero; in the remaining \(n\) bits, the first generator flips all bits, while the other generators each flip one bit. This recovers the stipulated antipodal augmentation. The images of the \(n+1\) generators have precisely one linear dependency, their total sum being zero, and every \(n\) of them form a basis. Permuting these generators therefore defines an automorphism of \(V\). Together with translations, these automorphisms act transitively on unoriented edges. Consequently all columns of either orthogonal projection have identical absolute column sums.

**2. Exact edge-source potential.** Source one unit of current from \(0\) to the first generator \(e_1\) in the quotient representation. The real characters are indexed by even-cardinality subsets \(S\subseteq\{1,\ldots,n+1\}\); the graph Laplacian has eigenvalue \(2|S|\) on character \(\chi_S\). The unique mean-zero potential solving \(Lu=\delta_0-\delta_{e_1}\) is consequently

\[
 u(x)=2^{-n}\sum_{\substack{|S|\text{ even}\\1\in S}}
 \frac{\chi_S(x)}{|S|}.
\]

For the representative \(x=(0,y)\) with \(|y|=j\), set \(U_j=u(x)\). The reciprocal identity \(1/(r+1)=\int_0^1t^r\,dt\), followed by the odd-subset generating function and the substitution \(z=(1+t)/2\), gives the exact beta-integral formula

\[
 U_j=\int_{1/2}^{1}
 \bigl[z^{n-j}(1-z)^j-z^j(1-z)^{n-j}\bigr] \,dz,
 \qquad 0\le j\le n.
\]

This integral proves \(U_{n-j}=-U_j\) and \(U_j>U_{j+1}\) for all \(0\le j<n\). In particular, \(\operatorname{sgn}U_j=\operatorname{sgn}(n-2j)\), with zero at the central index when \(n\) is even. This sign fact is essential for evaluating absolute currents; it is not inferred from numerical testing.

**3. Currents on ordinary cube edges.** An edge changing one of the \(n\) retained bits connects weights \(j\) and \(j+1\). There are \(\binom nj(n-j)\) such edges. Their total absolute potential drop is therefore

\[
 T_n=\sum_{j=0}^{n-1}\binom nj(n-j)(U_j-U_{j+1})
 =\sum_{j=0}^{n}\binom nj(n-2j)U_j.
\]

Interchanging the finite sum and the beta integral, the binomial identities

\[
 \sum_{j=0}^n\binom nj(n-2j)z^{n-j}(1-z)^j=n(2z-1),
 \quad
 \sum_{j=0}^n\binom nj(n-2j)z^j(1-z)^{n-j}=-n(2z-1)
\]

show that \(T_n=2n\int_{1/2}^1(2z-1)\,dz=n/2\).

**4. Currents on antipodal matching edges.** The matching pairs a retained binary string \(y\) with its complement, and their potentials are \(U_j\) and \(-U_j\). Counting each unordered pair exactly once, its total absolute current is

\[
 B_n=\sum_{j=0}^n\binom nj|U_j|.
\]

For \(z\in[1/2,1]\) introduce the binomial-majority bias

\[
 H_n(z)=\sum_{j=0}^n\operatorname{sgn}(n-2j)
 \binom nj z^{n-j}(1-z)^j.
\]

The sign and antisymmetry properties already proved yield \(B_n=2\int_{1/2}^1H_n(z)\,dz\). For any integer \(k\ge1\), adding the final Bernoulli trial converts the sign-majority statistic on \(2k-1\) trials to that on \(2k\) trials, with a tie scored zero; the two central boundary contributions cancel because

\[
 \binom{2k-1}{k-1}z^{k-1}(1-z)^k\,z
 =\binom{2k-1}{k}z^k(1-z)^{k-1}(1-z).
\]

Hence \(H_{2k-1}(z)=H_{2k}(z)\). Moreover \(H_{2k-1}(1/2)=0\), \(H_{2k-1}(1)=1\), and differentiation of its binomial tail gives

\[
 H'_{2k-1}(z)=\frac{2(2k-1)!}{((k-1)!)^2}
 [z(1-z)]^{k-1}.
\]

Integration by parts and the change of variable \(w=z(1-z)\) now give

\[
 \begin{aligned}
 B_{2k-1}=B_{2k}
 &=1-2\int_{1/2}^1(z-1/2)H'_{2k-1}(z)\,dz\\
 &=1-\frac{(2k)!}{(k!)^2\,4^k}
 =1-4^{-k}\binom{2k}{k}.
 \end{aligned}
\]

Adding the two edge classes yields the asserted \(\|Q_n\|_{1\to1}=T_n+B_n\). Step 1 makes the displayed column sum the operator norm, not merely a lower bound.

**5. Cycle projection and asymptotics.** The diagonal entry of \(Q_n\) in any edge is its effective resistance. It lies strictly between zero and one and is constant by edge transitivity. Since \(\operatorname{tr}Q_n=|V|-1=2^n-1\), division by the number of edges yields

\[
 q_n=(Q_n)_{e,e}=\frac{2(1-2^{-n})}{n+1}.
\]

For every edge column, the absolute column sum of \(I-Q_n\) is the corresponding sum for \(Q_n\), plus \(1-2q_n\). This proves the formula for \(P_n\). The classical central-binomial asymptotic \(4^{-k}\binom{2k}{k}=(\pi k)^{-1/2}+O(k^{-3/2})\), together with \(k=\lceil n/2\rceil\), proves both stated expansions. Finally, the ordinary binary cube has cut-projection norm \((n+1)/2\) by Dilworth–Kutzarova–Ostrovskii, Theorem 45; the difference is \(1/2-c_k>0\) for \(k\ge3\), since \(c_k\) strictly decreases from \(c_1=1/2\).

## Verification

A standalone exact-rational program, `verify_folded_cube.py`, accompanies this result. It constructs the potential a second way, from finite character sums rather than beta integrals; reconstructs every edge current from the actual augmented-cube adjacency for dimensions \(3\) through \(11\); and checks vertexwise Laplacian conservation and both formulas. It also independently solves grounded graph Laplacian systems by rational Gaussian elimination for both an ordinary coordinate edge and an antipodal edge in dimensions \(3,4,5\). The latter checks do not use the spectral potential.

The program's completed run reported `FOLDED_CUBE_EXACT_OK dimensions=9 spectral_edge_currents=22520 full_grounded_columns=6 full_grounded_currents=304`. The infinite range follows from the proof above, not from these finitely many tests. Run with `python3 verify_folded_cube.py`; it needs only the Python standard library.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582 (first publicly available 2023-05-21), establish the exact endpoint cut-projection norm \((n+1)/2\) for the **ordinary** binary \(n\)-cube in Theorem 45 and analyze its complementary cycle projection in Corollary 60. The folded graph studied here differs by the addition of all antipodal edges. Its degree, quotient character spectrum, edge-coordinate space and projection columns are different. The new central-binomial term is not implied by substituting a dimension in their cube theorem.

Boutin, Cockburn, Keough, Loeb and Rombach, *Symmetry Parameters of Various Hypercube Families*, arXiv:2110.04154 (2021), study folded hypercube automorphisms and distinguishing invariants. They do not calculate endpoint cut–cycle projection norms. The familiar small folded examples are consistent with the formula but are not the novelty claim. The exact unrestricted dimension formula and antipodal-matching excess for \(n\ge5\) are the claims made here. General electrical-network pseudoinverse identities remain relevant background; no assertion of novelty is made for those identities themselves.

## Limitations

The finding determines only canonical orthogonal projections, not optimal projections among all bounded linear projections. It uses real, unweighted, undirected graph edge coordinates and the two endpoint norms; it does not treat intermediate \(\ell_p\) operator norms, arbitrarily weighted matchings or nonuniform cube-edge conductances. Although targeted comparisons with identified literature found no covering formula, literature search cannot establish absolute bibliographic uniqueness. The result has received a self-review, not an independent mathematical audit.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582, v1 posted 2023-05-21; Theorem 45 and Corollary 60, and sections 1.1, 2.6–2.7. https://arxiv.org/abs/2305.12582
2. D. Boutin, S. Cockburn, L. Keough, S. Loeb, P. Rombach, *Symmetry Parameters of Various Hypercube Families*, arXiv:2110.04154, v1 posted 2021-10-08; section 5 and Table 1. https://arxiv.org/abs/2110.04154
