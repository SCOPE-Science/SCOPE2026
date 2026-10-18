# Multiplicity-free symmetric-group homology of Johnson flag complexes

## Finding
For every pair of integers \(n,k\) satisfying \(n\ge 2k\) and \(k\ge4\), let \(J(n,k)\) be the graph on the \(k\)-subsets of \([n]\), with an edge when the subsets differ by one element. Let \(X_{n,k}=\operatorname{Cl}(J(n,k))\), equivalently the inclusive graph-metric Vietoris–Rips complex at radius one. The coordinate-permutation action of \(S_n\) on its only nonzero reduced rational homology is exactly
\[
\widetilde H_2(X_{n,k};\mathbb Q)\cong
\bigoplus_{j=1}^{k-1}S^{(n-j-2,j,1,1)}.
\]
Here \(S^\lambda\) is the irreducible rational Specht module for partition \(\lambda\). Every summand occurs with multiplicity one and the summands are pairwise nonisomorphic. All reduced rational homology in other degrees vanishes. Neither \(S_n\) nor \(A_n\) fixes a nonzero rational second-homology class. For the first self-complementary Johnson graph \(J(8,4)\), the module is
\[
S^{(5,1,1,1)}\oplus S^{(4,2,1,1)}\oplus S^{(3,3,1,1)},
\]
with constituent dimensions \(35,90,56\) and total rank \(181\). The integer homotopy type \(X_{n,k}\simeq\bigvee^{\beta(n,k)}S^2\) and the rank formula are already known; the new theorem is the complete equivariant Specht decomposition for \(k\ge4\).

## Assumptions and scope
All simplices are nonempty finite cliques, with the empty simplex included when defining reduced chains. The group \(S_n\) acts simplicially by permutations of the underlying \(n\) coordinates. The coefficient field is \(\mathbb Q\), so finite-group modules are semisimple. The domain \(n\ge2k\ge8\) makes the stated partitions legitimate: for \(1\le j\le k-1\), \(n-j-2\ge j\ge1\). Complementation identifies the excluded half \(k>n/2\) with this range, but no extra cases are claimed. The theorem concerns graph-metric scale one only; no integral module structure, maps between scales, or action of additional graph automorphisms is asserted.

## Proof
**1. Clique decomposition and concentration.** Write \(V=\binom{[n]}k\). For each \((k-1)\)-subset \(A\), the **star** \(F_A\) consists of all \(A\cup\{x\}\) with \(x\notin A\); for each \((k+1)\)-subset \(B\), the **top** \(F_B\) consists of the \(k\)-subsets of \(B\). These are precisely the maximal cliques. Indeed, every third vertex adjacent to two given adjacent \(k\)-subsets belongs either to their common \((k-1)\)-core's star or their common \((k+1)\)-union's top, and a vertex of one kind cannot be adjacent to a vertex of the other kind. Distinct maximal cliques meet in at most two vertices. Each face with at least three vertices consequently belongs to exactly one such simplex.

For completeness, this structure gives an elementary collapse of \(X_{n,k}\) to dimension two: in each maximal simplex choose an apex \(a\); for every face \(\tau\) avoiding \(a\) and having at least three vertices, in decreasing order of size remove the pair \((\tau,\tau\cup\{a\})\). Every pair is an elementary free-face pair because no other maximal clique contains \(\tau\). The collapse preserves the entire one-skeleton. The hypersimplex \(\{x\in[0,1]^n:\sum_i x_i=k\}\) has the Johnson graph as its one-skeleton and only triangles as two-dimensional faces: a two-face fixes all but three coordinates, whose sum is one or two. Since the convex hypersimplex has dimension \(n-1\ge7\), its cellular two-skeleton is simply connected. Its two-skeleton embeds in \(X_{n,k}\) and contains the whole one-skeleton; adding other faces cannot introduce fundamental-group generators. Thus \(X_{n,k}\) is connected, simply connected, and homotopy equivalent to a two-dimensional CW complex. In particular \(\widetilde H_i(X_{n,k};\mathbb Q)=0\) for \(i\ne2\), and the reduced equivariant Euler character equals the actual \(H_2\) character.

**2. Equivariant chain identity.** Let \(P_r=\mathbb Q[\binom{[n]}r]\) be the permutation module on \(r\)-subsets. Let \(E\) be the signed orientation module on the edges of \(J(n,k)\); a symmetry fixing an edge but interchanging its endpoints acts by minus one. Let \(I_-\) be the permutation module on incidence flags \(A\subset U\) with \(|A|=k-1\), \(|U|=k\), and let \(I_+\) be the permutation module on flags \(U\subset B\) with \(|U|=k\), \(|B|=k+1\). Square brackets denote virtual characters. In the augmented simplicial chain complex of each maximal simplex \(F\), the alternating sum of its face-chain modules is zero. Hence its contribution from faces of dimension at least two is \([\mathbf1]-[C_0(F)]+[C_1(F)]\). Sum over all stars and tops. The sum of their vertex modules is \(I_-\oplus I_+\); each graph edge belongs to exactly one star and one top, so the sum of their oriented-edge modules is \(E\oplus E\). Adding the global zero- and one-dimensional chains and subtracting one trivial augmentation line yields
\[
[\widetilde H_2]=[E]+[P_{k-1}]+[P_k]+[P_{k+1}]-[I_-]-[I_+]-[\mathbf1]. \tag{1}
\]
All identities respect orientation signs, including symmetries that swap the endpoints of an edge.

**3. Convert the identity to symmetric functions.** Write \(h_r\) and \(e_r\) for complete and elementary symmetric functions, with \(h_0=1\). Under the Frobenius characteristic map, the seven terms on the right of (1) give
\[
\begin{aligned}
\mathsf F={}&h_{k-1}e_2h_{n-k-1}+h_{k-1}h_{n-k+1}+h_kh_{n-k}+h_{k+1}h_{n-k-1}\\
&-h_{k-1}h_1h_{n-k}-h_kh_1h_{n-k-1}-h_n.
\end{aligned} \tag{2}
\]
For instance, the stabilizer of an unoriented Johnson edge splits its coordinates into a common \((k-1)\)-set, an exchanged pair, and an \((n-k-1)\)-set. On the exchanged pair it acts by sign, whence \(\operatorname{ch}(E)=h_{k-1}e_2h_{n-k-1}\). The two flag modules have characteristics \(h_{k-1}h_1h_{n-k}\) and \(h_kh_1h_{n-k-1}\).

**4. A telescoping Jacobi–Trudi calculation.** Put \(a=n-j-2\). Expanding the Jacobi–Trudi determinant for \((a,j,1,1)\) gives
\[
\begin{aligned}
s_{(a,j,1,1)}={}&e_2(h_ah_j-h_{a+1}h_{j-1})\\
&+h_1(-h_ah_{j+1}+h_{a+2}h_{j-1})\\
&+h_ah_{j+2}-h_{a+3}h_{j-1}.
\end{aligned} \tag{3}
\]
Sum (3) over \(j=1,\ldots,k-1\). The first group telescopes to \(e_2(h_{n-k-1}h_{k-1}-h_{n-2})\). The second telescopes to \(h_1(h_{n-1}+h_{n-2}h_1-h_{n-k}h_{k-1}-h_{n-k-1}h_k)\). The third telescopes to \(h_{n-k+1}h_{k-1}+h_{n-k}h_k+h_{n-k-1}h_{k+1}-h_n-h_{n-1}h_1-h_{n-2}h_2\). Using \(e_2=h_1^2-h_2\), every extra boundary term cancels, leaving exactly (2). Therefore
\[
\mathsf F=\sum_{j=1}^{k-1}s_{(n-j-2,j,1,1)}.
\]
The Frobenius characteristic is injective on rational characters, and semisimplicity turns this character identity into the asserted direct-sum isomorphism. All constituents are distinct, and none is the trivial or sign representation. Restriction from \(S_n\) to \(A_n\) cannot introduce invariants unless a constituent is trivial or sign, since \(\operatorname{Ind}_{A_n}^{S_n}\mathbf1=\mathbf1\oplus\operatorname{sgn}\). This proves both invariant-vanishing statements.

## Verification
The standalone `verify.py` uses Python's standard library and can be run with `python3 verify.py`. It independently enumerates the full \(J(8,4)\) clique complex (face counts by cardinality: \(70,560,1120,560,112\)); compares signed simplex Lefschetz traces against (1) on all 22 conjugacy classes of \(S_8\); and computes the mod-two ranks of two-dimensional collapsed cores for \((n,k)=(8,4),(9,4)\). The latter have \((V,E,T,\operatorname{rank}\partial_2,\beta_2)=(70,560,672,491,181)\) and \((126,1260,1596,1135,461)\). A separate Pieri-rule character expansion verifies the irreducible lists for \((8,4),(9,4),(10,5),(12,5)\). The complete run prints `VERIFY_OK`. These finite computations check delicate signs, incidence multiplicities, and the decomposition; the unrestricted quantifiers follow from Steps 1–4 rather than extrapolation.

## Relationship to prior work
Rispoli's *The Graph of the Hypersimplex* (arXiv:0811.2981v1, first posted 2008-11-18) describes the relevant Johnson/hypersimplex graph and its combinatorics, but not the asserted simplicial homology representation. Shuldiner and Oldford's *The Clique Structure of Johnson Graphs* (arXiv:2208.12710v1, first posted 2022-08-26) gives the two maximal-clique types used here, not an equivariant top-homology decomposition. A subsequently published *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes* classifies the **nonequivariant** homotopy types for all \(3\le k\le n-3\), and so already implies the rank and concentration used above; those are not presented as new. *Symmetric-group homology character of constant-weight-three Hamming Rips complexes* determines the character for \(k=3\) only; it does not imply the new claim for all \(k\ge4\). Galetto, Montaño and Wellner (arXiv:2606.20784v1) study homology representations of the **entire** Boolean hypercube Rips complex, not the individual constant-weight layers: restriction to an induced layer does not in general recover homology of that layer. None of these inspected results states or implies the all-\(k\) Specht decomposition above.

## Limitations
The theorem treats ordinary rational \(S_n\)-modules of one fixed Johnson Rips scale. It does not classify integral module lattices, additional complement automorphisms when \(n=2k\), persistent transition maps, or other Rips scales. A differently indexed or uninspected equivalent statement may exist; the literature comparison is not independent certification. Computations corroborate selected finite cases and cannot establish all parameters by themselves.

## References
1. F. J. Rispoli, *The Graph of the Hypersimplex*, arXiv:0811.2981v1, first posted 2008-11-18, https://arxiv.org/abs/0811.2981.
2. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710v1, first posted 2022-08-26, https://arxiv.org/abs/2208.12710.
3. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, published-finding corpus research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518.
4. *Symmetric-group homology character of constant-weight-three Hamming Rips complexes*, published-finding corpus research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-symmetric-group-homology-character-of-constant-weight-three-hamm--11db16b6cb70.
5. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1, first posted 2026-06-18, https://arxiv.org/abs/2606.20784.
