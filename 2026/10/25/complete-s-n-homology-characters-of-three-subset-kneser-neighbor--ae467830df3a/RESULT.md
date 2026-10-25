# Complete \(S_n\)-homology characters of three-subset Kneser neighborhood complexes

## Finding
For each integer \(n\ge 6\), let \(X_n=\mathcal N(\operatorname{KG}(n,3))\), with the usual relabeling action of \(S_n\). The graph \(\operatorname{KG}(n,3)\) has the three-subsets of \([n]\) as its vertices, with edges between disjoint triples; \(\mathcal N\) is the *ordinary open-neighborhood complex*, not the independence complex or the neighborhood complex of a stable Kneser subgraph.

For \(g\in S_n\), let \(a(g)\) be the number of fixed labels and \(b(g)\) the number of two-cycles in its disjoint-cycle decomposition. Define
\[
Q(a,b)=\frac{a^4-10a^3-4a^2b+31a^2+12ab-30a+4b^2-12b+4}{4}.
\]
Then, as an equality of full rational characters,
\[
\operatorname{tr}\!\left(g\mid\widetilde H_{n-6}(X_n;\mathbb Q)\right)
=\operatorname{sgn}(g)\,Q(a(g),b(g)).
\]
All other reduced rational homology groups vanish. Neither the trivial nor sign representation of \(S_n\) occurs; the finite quotients by \(S_n\) **and** \(A_n\) are rationally acyclic (their reduced rational homology vanishes in all degrees). This gives the complete rational equivariant homology character in every dimension parameter, not merely its dimension.

The previously published sphere-wedge theorem yields the homology concentration and rank
\[
\dim\widetilde H_{n-6}(X_n;\mathbb Q)
=\frac{(n-5)(n-3)(n-2)n}{4}+1.
\]
Indeed, evaluating the new character at the identity reproduces that rank, but the rank and the sphere-wedge homotopy type themselves are **not** claimed as new.

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. For a permutation \(g\), the sign character means the ordinary determinant sign of its permutation action on \([n]\). The claim holds for every integer \(n\ge6\), including the base case \(n=6\) where reduced degree-zero homology is allowed. Each face of \(X_n\) is a collection of distinct triples whose union occupies at most \(n-3\) labels: exactly then a disjoint triple exists as a common neighbor. We use *augmented* simplicial chains in the equivariant reduced Lefschetz calculation. The result is rational: no new integral equivariant decomposition is asserted.

## Proof
**1. Homology concentration.** Put \(k=n-6\). Theorem 1.3 of Nilakantan–Singh, arXiv:1807.11732v1, proves that \(\mathcal N(\operatorname{KG}(n,3))\) is a wedge of \(\frac{(k+1)(k+3)(k+4)(k+6)}4+1\) copies of \(S^k\). Thus its reduced rational homology is concentrated in degree \(k\), so the reduced Lefschetz number of any permutation is \((-1)^k\) times its trace on that group. This invokes a published nonequivariant theorem; our calculation of its induced action is independent.

**2. Signed fixed-face count.** Fix \(g\in S_n\) with \(c\) cycles on labels. Regard its cycles as a set \(\mathcal C\). Every \(g\)-fixed face of \(X_n\) is a union of whole \(g\)-orbits of three-subsets. If it contains \(r\) vertices (triples) in \(t\) orbits, its induced orientation sign is \((-1)^{r-t}\). Multiplying by \((-1)^{r-1}\), the alternating chain weight is \((-1)^{t+1}\). The same expression for the augmented empty face is \(-1\). Therefore the reduced Lefschetz number equals the negative of the sum \(S\) of \((-1)^t\) over all invariant faces including the empty face.

For \(B\subseteq\mathcal C\), let \(F(B)\) be the signed sum over *all* \(g\)-invariant families of three-subsets whose union is supported inside the label-cycles \(B\); there is **no** neighborhood restriction in this auxiliary sum. Each orbit of triples present in \(B\) is independently either selected or omitted, and hence \(F(B)\) is \(1\) if the total length \(w(B)\) is smaller than \(3\), and otherwise \(0\). Define \(T(B)\) similarly with union of labels **exactly** equal to the cycles in \(B\). Since \(F(B)=\sum_{D\subseteq B}T(D)\), Boolean Möbius inversion gives
\[
T(B)=(-1)^{|B|}\left(1-a_B-b_B+\binom{a_B}{2}\right),
\]
where \(a_B\) and \(b_B\) count the one- and two-cycles in \(B\). Indeed, the only subsets \(D\) with \(w(D)<3\) are the empty set, one one-cycle, one two-cycle, or two one-cycles.

**3. Complementary small supports.** The sum over all invariant families without support restriction is \(0\), because the graph has at least one three-subset orbit and \(w(\mathcal C)=n\ge6\). The neighborhood condition is that at least three labels are missing. Therefore \(S\) equals minus the sum of \(T(B)\) with at most two labels omitted. Put \(a=a(g)\), \(b=b(g)\), and
\[P(a,b)=1-a-b+\binom a2.\]
The omitted cycle families can only be the empty family, one one-cycle, one two-cycle, or two one-cycles. Thus
\[
S=-(-1)^c\left[P(a,b)-aP(a-1,b)-bP(a,b-1)
+\binom a2P(a-2,b)\right].
\]
When a coefficient vanishes, its corresponding term is omitted, so no evaluation at negative counts is needed. Direct expansion of the bracket gives exactly \(Q(a,b)\). Therefore \(\widetilde L(g)=-S=(-1)^cQ(a,b)\). Since the only nonzero reduced homology lies in degree \(n-6\), its trace is
\[
(-1)^{n-6}\widetilde L(g)=(-1)^{n+c}Q(a,b)
=\operatorname{sgn}(g)Q(a,b),
\]
using \(\operatorname{sgn}(g)=(-1)^{n-c}\). This proves the full character formula for *all* \(n\ge6\).

**4. Absence of invariant and alternating lines.** Write the quartic polynomial in the binomial/falling-factorial character basis:
\[
\begin{aligned}
Q(a,b)={}&1-2\binom a1+4\binom a2-6\binom a3+6\binom a4
-2\binom b1\\
&+2\binom a1\binom b1-2\binom a2\binom b1+2\binom b2.
\end{aligned}
\]
Under uniform \(g\in S_n\), each \(\binom a j\binom b t\) has mean \(1/(j!2^tt!)\) for \(j+2t\le n\); substitution in this expansion yields \(\mathbb E[Q(a(g),b(g))]=0\). Moreover, the signed mean of each such basis function vanishes because specifying \(j\) fixed labels and \(t\) disjoint two-cycles leaves at least \(n-j-2t\ge2\) free labels, whose symmetric group has zero sign sum. Thus \(\mathbb E[\operatorname{sgn}(g)Q(a(g),b(g))]=0\). These are the multiplicities of the sign and trivial representations respectively. Restriction to \(A_n\) has no invariant line because its fixed subspace is precisely the sum of the trivial and sign isotypic spaces of \(S_n\). For finite group actions on finite simplicial complexes, passing to barycentric subdivision and averaging over \(\mathbb Q\) identifies quotient-space rational homology with invariant homology. The asserted rational acyclicity follows.

## Verification
The accompanying `check_kg3.py` constructs the orbits of *all* triples under a representative of each cycle type, forms an independent signed support-mask dynamic program, computes the augmented chain Lefschetz number, and compares it to the quartic character. It checks all **253** conjugacy-class representatives for \(n=6,7,8,9,10,11,12\); identity values agree with the published sphere-wedge ranks in the same range. Exact class-size-weighted sign and trivial multiplicity sums also vanish for each such \(n\). Run `python3 check_kg3.py` using only the Python standard library. This finite test supplements, and does not replace, the all-\(n\) combinatorial proof.

## Relationship to prior work
Nilakantan and Singh (arXiv:1807.11732v1, Theorem 1.3, including its proof) determined the *nonequivariant* wedge-of-spheres homotopy type for three-subset Kneser graphs. The article's theorem, definitions, relevant Morse construction, final proof, and references were inspected: no complete natural \(S_n\) homology character is supplied there. Their earlier arXiv:1802.05848v1 concerns **two-subset** Kneser graphs, which have a different underlying complex and a different character. The new theorem specifies the entire rational \(S_n\)-module through its character and both natural symmetry-quotient homology consequences. Targeted searches of homology-character/equivariant aliases did not reveal a stronger covering formula. Lack of a search hit is not proof of publication priority.

## Limitations
Only the rational character and its derived rational quotient consequences are new claims; homology concentration and Betti ranks are imported from the cited 2018 theorem. This does not determine an integral \(\mathbb Z[S_n]\)-lattice or any torsion in symmetry quotients, and it does not identify an explicit rational Specht basis. Existing unindexed equivariant computations could affect priority; no independent external validation has been performed.

## References
Nilakantan, N., and Singh, A. (2018), *Neighborhood Complexes of Kneser Graphs, KG3,k*, arXiv:1807.11732v1 (first public 2018-07-31), especially Theorem 1.3 and Section 4.2. https://arxiv.org/pdf/1807.11732

Nilakantan, N., and Singh, A. (2018), *Homotopy Type of Neighborhood Complexes of Kneser Graphs, KG2,k*, arXiv:1802.05848v1 (first public 2018-02-16), Theorem 1.3. https://arxiv.org/pdf/1802.05848
