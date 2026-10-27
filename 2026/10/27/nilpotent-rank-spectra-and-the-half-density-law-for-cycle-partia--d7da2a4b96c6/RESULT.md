# Nilpotent rank spectra and the half-density law for cycle partial-isometry monoids

## Finding
For each integer \(n\ge3\), the complete nilpotent rank-generating polynomial of the cycle-graph partial-isometry monoid has an explicit divisor-sum formula. With the definitions below,
\[
N_n(z)=\sum_{d\mid n}\varphi(d)\big((1+z)^d-z^d\big)^{n/d}+R_n(z)-(2n-1)-n(n-1)z-\mathbf 1_{2\mid n}\frac{n(n-2)}2z^2,
\]
where the reflection contribution is
\[
R_n(z)=\begin{cases}
n(1+2z)^{(n-1)/2},&n\text{ odd},\\
\frac n2\big((1+2z)^{(n-2)/2}+(1+2z)^{n/2}\big),&n\text{ even}.
\end{cases}
\]
The coefficient at the maximum nilpotent rank is \([z^{n-1}]N_n(z)=n\varphi(n)\). The nilpotent proportion tends to one half, quantitatively
\[
\frac{N_n(1)}{|\mathcal{DPC}_n|}=\frac12+O\!\left(\frac{(\log n)^2}{n}\right).
\]
For example, the coefficient of \(z^2\) is \(n(n-1)(n-2)\) for odd \(n\) and \(n(n-2)(2n-3)/2\) for even \(n\).

## Assumptions and scope
Let \(n\ge3\) be an integer. The vertices of the ordinary undirected cycle \(C_n\) are \(\mathbb Z/n\mathbb Z\), and distance means shortest-path distance. The inverse monoid \(\mathcal{DPC}_n\) consists of every partial bijection preserving that distance, including the empty map \(0\). Multiplication is composition of partial maps. The **rank** of a partial map is the size of its domain. A map is **nilpotent** if one positive power is the empty map; equivalently its directed functional graph contains no directed cycle. We include the rank-zero map in \(N_n(z)\). The symbol \(\varphi\) is Euler's totient function, and \(\mathbf1_{2\mid n}\) is one when \(n\) is even and zero otherwise. No primality assumption is placed on \(n\). There are no field hypotheses.

## Proof
**Dihedral reduction.** As proved by Fernandes and Paulista (Lemma 1.1), every partial isometry of a cycle is the restriction \(g|_S\) of an element of its dihedral isometry group \(D_{2n}\) to some domain \(S\). All rank-at-least-three maps have a unique extending dihedral permutation. Every rank-one map has exactly two dihedral extensions. In even cycle length, and only then, there is an additional double extension at rank two precisely for maps with antipodal domain and antipodal image.

**Nilpotency of restrictions.** Suppose \(g\) is a permutation of the vertex set and \(\alpha=g|_S\). The directed cycles of \(\alpha\) are precisely those full cycles of \(g\) lying entirely in \(S\). Indeed, each partial orbit advances by \(g\) until leaving the domain, unless it visits a full \(g\)-cycle. Hence \(\alpha\) is nilpotent if and only if \(S\) contains no entire \(g\)-cycle. The generating polynomial for choices from one \(g\)-cycle of length \(d\) is \((1+z)^d-z^d\).

**Counting rotation-restriction pairs.** A rotation of order \(d\mid n\) comprises \(n/d\) disjoint cycles of length \(d\); there are exactly \(\varphi(d)\) such rotations. Summing permissible domain choices gives
\[
\sum_{d\mid n}\varphi(d)\big((1+z)^d-z^d\big)^{n/d}.
\]
In odd size, every reflection has one fixed vertex and \((n-1)/2\) transpositions; the forbidden fixed vertex contributes factor one, and each transposition contributes \(1+2z\). There are \(n\) reflections. In even size, \(n/2\) reflections have two fixed vertices and \((n-2)/2\) transpositions, while the other \(n/2\) have \(n/2\) transpositions. This proves the displayed \(R_n(z)\). Thus \(F_n(z)\) enumerates all pairs \((g,S)\) with nilpotent \(g|_S\), **not yet distinct partial maps**.

**Correction for multiple extensions.** The empty map is counted once for every element of \(D_{2n}\), namely \(2n\) times, and so contributes an overcount of \(2n-1\). Every nonzero rank-one map with source different from target is nilpotent; there are \(n(n-1)\) of these and each is counted twice. For even \(n\), antipodal two-point domains are \(n/2\) in number. The image of such a domain must also be an antipodal pair; among the \(n/2\) such pairs, the one identical to the domain gives the two nonnilpotent bijections, and the remaining \(n/2-1\) pairs each give two nilpotent bijections. Consequently the number of *nilpotent* rank-two maps with two dihedral extensions is \((n/2)\cdot(n/2-1)\cdot2=n(n-2)/2\). There are no further multiple extensions. Subtracting precisely these overcounts proves the polynomial formula.

**High-rank boundary.** No nilpotent partial injection on \(n\) points can have full rank, since a full-rank injection is a permutation. A nilpotent map with rank \(n-1\) has a directed Hamiltonian path (the partial-injection functional graph consists entirely of directed paths; with just one missing domain point a nilpotent map has one path). Its dihedral extension closes that path to an \(n\)-cycle. Conversely, restricting any dihedral \(n\)-cycle by omitting any one point gives such a path. The dihedral \(n\)-cycles for \(n\ge3\) are precisely the primitive rotations, of which there are \(\varphi(n)\). Each admits \(n\) distinct one-point omissions. Therefore \([z^{n-1}]N_n(z)=n\varphi(n)\).

**Half-density law.** Evaluate the pair-polynomial at \(z=1\). For any rotation of order \(d\), the nilpotent-restriction fraction among its \(2^n\) domains equals \((1-2^{-d})^{n/d}\). Put \(L=\lceil2\log_2 n\rceil\). There are at most \(\sum_{1\le d\le L}\varphi(d)=O(L^2)\) rotations of order at most \(L\), so all their deficits from \(2^n\) cost at most \(O(2^n(\log n)^2)\). For each larger-order rotation, Bernoulli's inequality gives a deficit bounded by \(2^n(n/d)2^{-d}\le2^n/n\). Summed over at most \(n\) such rotations, this is \(O(2^n)\). Every reflection contributes at most \(3^{n/2}\) nilpotent restrictions, giving \(O(n3^{n/2})\) in total. Thus \(F_n(1)=n2^n+O(2^n(\log n)^2)\). The polynomial corrections are \(O(n^2)\). The known cardinality formula of Fernandes–Paulista gives \(|\mathcal{DPC}_n|=n2^{n+1}+O(n^2)\), so division yields the claimed \(\frac12+O((\log n)^2/n)\) limit. All bounds hold over both parities.

**Rank-two illustration.** There are \(n\) unordered vertex pairs of a given nonantipodal cyclic distance, and, for even \(n\), \(n/2\) antipodal pairs. Counting the two bijections between each ordered pair of equal-distance two-point sets, then excluding any maps with fixed points or directed two-cycles, yields \([z^2]N_n(z)=n(n-1)(n-2)\) when \(n\) is odd and \(n(n-2)(2n-3)/2\) when \(n\) is even. These agree with direct coefficient extraction from the main formula.

## Verification
The accompanying standalone Python-3 program `verify.py` enumerates **all** restrictions of the \(2n\) dihedral permutations for \(3\le n\le10\), deduplicates partial bijections, detects directed cycles by independent orbit traversal, and checks every coefficient of the formula. It also independently checks the known cardinality of the full monoid and the top-rank count. Run `python3 verify.py` from the extracted file directory. Successful execution prints `VERIFY_OK cycle partial-isometry nilpotent rank polynomial`. The full-range proof is symbolic, not extrapolated from these finite examples.

## Relationship to prior work
Fernandes–Paulista, *On the monoid of partial isometries of a cycle graph* (2022), establishes the extension criterion, rank-dependent multiplicity of dihedral extensions, and exact overall size; these are used as cited lemmas. Its examined principal results concern the size, Green relations, generators, and rank; they do not state this nilpotent rank spectrum or half-density law. Gomes–Howie, *Nilpotents in finite symmetric inverse semigroups* (1987), classifies nilpotents in the unrestricted symmetric inverse monoid by acyclic partial-orbit paths, providing the general nilpotency criterion but not the restriction count in the dihedral cycle monoid. The 1990 Mills work on the semigroup of partial symmetries of a convex polygon is a closely related source; only its bibliographic abstract could be inspected, so overlap with its uninspected full text remains a priority risk.

## Limitations
The formula counts labelled partial maps, not conjugacy classes or nilpotent generated subsemigroups. It uses the **graph metric of a cycle**, not arbitrary cycle-graph endomorphisms or partial automorphisms of induced subgraphs. The error term is an upper bound, not a claim of a sharp secondary asymptotic. A bibliography search and inspected primary full texts do not establish absolute publication priority. No independent mathematical audit has been performed.

## References
1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (initial public submission 2022-05-04), especially Lemma 1.1 and the cardinality formula, https://arxiv.org/abs/2205.02196 .
2. G. M. S. Gomes and J. M. Howie, *Nilpotents in finite symmetric inverse semigroups*, Proceedings of the Edinburgh Mathematical Society (1987), DOI:10.1017/S0013091500026778, especially the directed-path characterization.
3. J. E. Mills, *The inverse semigroup of partial symmetries of a convex polygon*, Semigroup Forum (1990), DOI:10.1007/BF02573384 (bibliographic/abstract information only, complete text not inspected).
