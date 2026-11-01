# Mixed-parity homology forced by the symmetry character of \(\operatorname{Hom}(P,K_4)\)

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), with disjoint pairs adjacent. Let \(X=\operatorname{Hom}(P,K_4)\) be the standard Babson–Kozlov cell complex of proper four-colorings, and let \(\Gamma=\mathfrak S_5\times\mathfrak S_4\) act by source automorphisms and permutation of the four colors. Write \(S^\lambda\) for the rational Specht representation of the symmetric group indexed by partition \(\lambda\), and \(\varepsilon_4\) for the sign character of \(\mathfrak S_4\).

The complete reduced *virtual rational homology character* is the class function \(\widetilde L_X(g)=\sum_{i\geq0}(-1)^i\operatorname{tr}(g\mid\widetilde H_i(X;\mathbb Q))\) displayed below. In particular, its irreducible character inner products satisfy

\[
\left\langle\widetilde L_X,S^{(3,2)}\boxtimes\mathbf1\right\rangle_\Gamma=1,
\qquad
\left\langle\widetilde L_X,S^{(2,2,1)}\boxtimes\varepsilon_4\right\rangle_\Gamma=-1.
\]

**Consequently, \(X\) has nonzero positive-degree rational homology in both even and odd degrees.** At least one even-degree group contains a copy of the five-dimensional \(S^{(3,2)}\boxtimes\mathbf1\) representation; at least one odd-degree group contains a copy of the five-dimensional \(S^{(2,2,1)}\boxtimes\varepsilon_4\) representation. These assertions are existence statements, *not* complete graded homology decompositions.

The entire cellular face vector, from dimensions zero through six, is

\[
(12960,53280,80400,54960,17400,2400,120).
\]

Thus \(X\) is connected and \(\chi(X)=240\), with reduced Euler characteristic \(239\). The full character table below is indexed by cycle types of \(\mathfrak S_5\) (rows) and \(\mathfrak S_4\) (columns). Each entry is the ordinary, unreduced Lefschetz number \(L_X(g)=\widetilde L_X(g)+1\).

| Source cycle lengths | \((1,1,1,1)\) | \((2,1,1)\) | \((2,2)\) | \((3,1)\) | \((4)\) |
|:--|--:|--:|--:|--:|--:|
| \((1,1,1,1,1)\) | 240 | 60 | 0 | 0 | 0 |
| \((2,1,1,1)\) | 12 | -16 | 4 | 0 | 0 |
| \((2,2,1)\) | 0 | 4 | 0 | 0 | 0 |
| \((3,1,1)\) | -12 | 6 | 0 | 0 | 0 |
| \((3,2)\) | 0 | 2 | 4 | 6 | 0 |
| \((4,1)\) | 0 | 0 | 0 | 0 | 4 |
| \((5)\) | 0 | 0 | 0 | 0 | 0 |

## Assumptions and scope

There are no assumptions on unspecified graphs: \(P\) is exactly the ten-vertex Kneser graph above, the target is the loop-free complete graph on four colors, and \(X\) is the *polyhedral* Hom complex, not the graph of colorings by itself. A cell is an ordered tuple \(\eta=(A_v)_{v\in V(P)}\) of nonempty subsets \(A_v\subseteq\{0,1,2,3\}\), subject to \(A_u\cap A_v=\varnothing\) whenever \(uv\) is an edge. Its closed cell is the product \(\prod_{v\in V(P)}\Delta^{|A_v|-1}\), of dimension \(\sum_v(|A_v|-1)\). An automorphism \((\sigma,\tau)\in\Gamma\) permutes the ten vertex coordinates via the induced action of \(\sigma\) on two-subsets and sends every color set to its \(\tau\)-image.

The homology coefficients and representation decompositions are over \(\mathbb Q\). No statement about integral torsion, a particular nonzero homological degree, or a wedge-of-spheres decomposition is inferred from the virtual character.

## Proof

**Exhaustiveness of cells.** Recursion over the ten vertex coordinates lists each proper four-coloring exactly once. There are 12,960 such colorings. Starting with their ten one-element color sets, repeatedly adjoin to any coordinate one new color absent from all neighboring color sets. This yields exactly the legal Hom cells: every generated tuple satisfies the disjointness condition, and every legal tuple admits a singleton choice at each coordinate and can be obtained by adding its other colors in some order. The independent enumeration procedure in `verify.py` generates 221,520 distinct tuples, whose dimension counts are the displayed face vector. The one-skeleton has one edge for each legal single-vertex recoloring; exhaustive breadth-first search reaches all 12,960 coloring vertices from one initial coloring, so \(X\) is connected. The alternating face count gives \(\chi(X)=240\).

**Cellular fixed-cell signs.** Orient each factor simplex by increasing color order and each product cell by the fixed vertex-coordinate order. For \(g=(\sigma,\tau)\), only cells satisfying \(A_{\sigma v}=\tau(A_v)\) can contribute to the trace of its action on cellular chains. Let \(\mathcal O\) be a cycle of length \(\ell\) in the induced permutation of the ten graph vertices, with representative color set \(A\). Fixedness forces \(\tau^\ell(A)=A\). The cyclic permutation of the \(\ell\) oriented simplex factors supplies the Koszul factor \((-1)^{(\ell-1)(|A|-1)}\), while the accumulated color permutation supplies \(\operatorname{sgn}(\tau^\ell\mid_A)\). Multiplication by the Euler sign \((-1)^{\ell(|A|-1)}\) reduces the cycle's contribution to

\[
(-1)^{|A|-1}\operatorname{sgn}(\tau^\ell\mid_A).
\]

The product of these factors over cycles of the source permutation is the signed Lefschetz contribution of the fixed cell. The verifier enumerates every cell for representative permutations of the seven source and five color conjugacy classes, checks fixedness, and sums these products as integers. This yields all 35 entries of the table. The cellular Hopf trace formula identifies their alternating cellular traces with alternating homology traces; the connected zero-dimensional homology is the trivial representation, so \(\widetilde L_X=L_X-1\).

**Character projection and parity.** For a permutation \(\sigma\in\mathfrak S_5\), let \(f\) be its number of fixed letters and \(t\) its number of two-cycles. The character of the five-dimensional \(S^{(3,2)}\) is

\[
\chi_{32}(\sigma)=\binom f2+t-f,
\]

because the permutation representation on two-subsets decomposes as \(\mathbf1\oplus S^{(4,1)}\oplus S^{(3,2)}\), whereas the permutation representation on letters is \(\mathbf1\oplus S^{(4,1)}\). The conjugate Specht representation is \(S^{(2,2,1)}=S^{(3,2)}\otimes\operatorname{sgn}_5\). Therefore the two claimed signed multiplicities are calculated, for \(\rho=\chi_{32}\) and \(\rho=\chi_{32}\operatorname{sgn}_5\), respectively, by the exact finite sum

\[
\frac1{120\cdot24}
\sum_{\lambda\vdash5}\sum_{\mu\vdash4}
|C_\lambda|\,|C_\mu|\,[L_X(\lambda,\mu)-1]
\rho(\lambda)\,\kappa(\mu),
\]

where \(\kappa\equiv1\) in the first case and \(\kappa=\operatorname{sgn}_4\) in the second. The class size for partition \(\lambda\) is \(n!/\prod_j j^{m_j}m_j!\), with \(m_j\) parts of size \(j\). Direct substitution into the 35-entry integer table gives precisely \(+1\) and \(-1\); both are independently recomputed by `verify.py`. Since finite-group rational representations are semisimple, an irreducible occurring with signed multiplicity \(+1\) must occur in even reduced homology, and one with signed multiplicity \(-1\) must occur in odd reduced homology. Neither representation is the trivial source representation; both occur in positive degrees. This proves the finding.

## Verification

Run `python3 verify.py` from the directory containing `class_character.json`. It uses Python's standard library only. It performs proper-coloring recursion, upward closure of all allowable multicolor cells, a complete connectivity search on the coloring graph, signed fixed-cell Lefschetz sums for 35 conjugacy classes, and two independent Specht projections using the fixed-point/two-cycle formula. It checks the supplied table byte-for-byte at the data level rather than trusting recorded traces. Its successful result is reproduced in `verify_output.txt`, ending with `VERIFY_OK`.

The character-table data file records the complete 35 class traces, class sizes, and fixed-cell counts. The proof of exactness uses the finite exhaustiveness argument above; the verification output alone is not substituted for that argument.

## Relationship to prior work

Babson and Kozlov introduced the polyhedral Hom complex and proved homotopy classifications when the source is a complete graph, a forest, or the complement of a forest. The Petersen graph is neither a forest nor a complement of a forest, and these statements do not imply the two explicit \(\mathfrak S_5\times\mathfrak S_4\) virtual-character projections. Čukić and Kozlov proved \((n-d-2)\)-connectivity for \(\operatorname{Hom}(G,K_n)\) when \(G\) has maximum degree \(d\); for \(G=P\), \(d=3\), \(n=4\), it yields only nonemptiness, not the homological parity assertion. Previously recorded calculations of graph configurations, cutting complexes, and five-cycle Hom complexes involve different topological objects or graph/target pairs.

The present claim is solely the *computed complete equivariant virtual character and its two forced homological-parity consequences*. It does not claim to invent Hom complexes, Specht character theory, or the cellular Lefschetz method. A formally equivalent unindexed published calculation remains possible.

## Limitations

The individual graded Betti numbers, integral homology groups, and full homotopy type of \(X\) are not determined here. The two Fourier coefficients concern the alternating sum of graded representations; they do not locate the degrees or determine multiplicities in any one degree. The calculation applies to this particular Petersen graph and four-color target. No independent external mathematical audit has been performed.

## References

1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first public version 2003-10-05. https://arxiv.org/abs/math/0310056
2. S. Lj. Čukić and D. N. Kozlov, *Higher connectivity of graph coloring complexes*, arXiv:math/0410335, first public version 2004-10-14. https://arxiv.org/abs/math/0410335
3. D. A. Holton and J. Sheehan, *The Petersen Graph*, Cambridge University Press, 1993. The graph is identified here with \(\operatorname{KG}(5,2)\), and its full automorphism group with \(\mathfrak S_5\).
