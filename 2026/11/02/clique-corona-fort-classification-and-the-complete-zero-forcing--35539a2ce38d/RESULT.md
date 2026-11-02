# Clique-corona fort classification and the complete zero-forcing polynomial transform

## Finding

For an arbitrary finite simple graph \(G\), replacing every original vertex by an attached private clique of order at least two admits an exact transfer law for both minimal forts and *every coefficient* of the standard zero-forcing polynomial. The base graph need not be connected and may have isolated vertices.

Let \(V=V(G)\), \(n=|V|\geq1\), and assign integers \(r_v\geq2\) independently to \(v\in V\). Construct \(H\) by adding a private clique \(C_v\cong K_{r_v}\), joining each vertex of \(C_v\) to \(v\), and adding no other edges. The uniform case is the corona \(G\odot K_r\).

A *fort* is a nonempty vertex set \(F\) for which every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Let \(\mathscr{M}(G)\) denote the inclusion-minimal forts of \(G\), and define their cardinality polynomial
\[
\mathcal M_G(z)=\sum_{A\in\mathscr M(G)}z^{|A|}.
\]
**Theorem A (complete classification).** Every inclusion-minimal fort of \(H\) is **exactly one** of the following disjoint kinds: (i) a pair of vertices in one private clique \(C_v\); (ii) a set \(A\cup\{p_v:v\in A\}\), where \(A\in\mathscr M(G)\) and each \(p_v\) is chosen independently from \(C_v\). Conversely every set of either kind is an inclusion-minimal fort. Consequently
\[
\boxed{\mathcal M_H(z)=z^2\sum_{v\in V}\binom{r_v}{2}
+\sum_{A\in\mathscr M(G)}\left(\prod_{v\in A}r_v\right)z^{2|A|}.}
\]
For \(r_v=r\) throughout this becomes
\[
\boxed{\mathcal M_{G\odot K_r}(z)=n\binom r2z^2+\mathcal M_G(rz^2).}
\]

Let \(\mathscr Z(G)\) denote the family of all standard zero-forcing sets of \(G\): a blue vertex forces its unique white neighbor blue, repeated until no further move is possible. Define
\[
\mathcal Z_G(z)=\sum_{T\in\mathscr Z(G)}z^{|T|}.
\]
**Theorem B (complete polynomial transfer).** For arbitrary nonuniform clique orders,
\[
\boxed{\mathcal Z_H(z)=\sum_{T\in\mathscr Z(G)}
\prod_{v\in T}\bigl(z^{r_v}(r_v+1+z)\bigr)
\prod_{v\notin T}\bigl(r_vz^{r_v-1}\bigr).}
\]
In particular, for a common clique order \(r\geq2\),
\[
\boxed{\mathcal Z_{G\odot K_r}(z)
=(rz^{r-1})^n\,\mathcal Z_G\!\left(\frac{z(z+r+1)}r\right).}
\]
Thus the entire size distribution transfers from the arbitrary base graph via one explicit polynomial substitution, not merely the least exponent.

As a corollary, put \(q=\min\{|T|:T\in\mathscr Z(G)\}\). The minimum zero-forcing cardinality of \(H\) is \(\sum_v(r_v-1)+q\), and the *exact number* of minimum-cardinality zero-forcing sets is
\[
\boxed{\sum_{\substack{T\in\mathscr Z(G)\\|T|=q}}
\prod_{v\in T}(r_v+1)\prod_{v\notin T}r_v.}
\]
For uniform \(r\), this count is \(r^{n-q}(r+1)^q[z^q]\mathcal Z_G(z)\). The scalar minimum in the uniform connected case is previously known (see References).

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. The base \(G\) is arbitrary of positive order, without a connectedness or minimum-degree hypothesis. Each private clique is complete and has at least two vertices. A fort is inclusion-minimal, not necessarily minimum-cardinality. Standard zero forcing here uses only the usual unique-white-neighbor rule, not skew or positive-semidefinite variants. Every vertex subset, including the full set, is eligible in the zero-forcing polynomial; the empty set is not zero forcing when \(n\geq1\). Exponents of \(z\) are vertex cardinalities. No normalization by graph automorphisms is used.

## Proof

**1. Rigid local fort structure.** A pair \(\{p,q\}\subset C_v\) is a fort of \(H\): the corresponding original vertex \(v\) sees two vertices of the pair, every remaining vertex in \(C_v\) sees two, and every other outside vertex sees none. Hence any inclusion-minimal fort containing at least two vertices of some \(C_v\) is that pair alone.

Consider now a fort \(F\) with at most one member of each \(C_v\). If \(v\in F\) but \(F\cap C_v=\varnothing\), each outside vertex of \(C_v\) has exactly one neighbor in \(F\) (namely \(v\)), a contradiction. If \(v\notin F\) but \(F\cap C_v\) is a singleton, there is another vertex of \(C_v\) outside \(F\) since \(r_v\geq2\); it has exactly one neighbor in \(F\), again a contradiction. Thus \(v\in F\) if and only if \(F\cap C_v\) is a singleton. Writing \(A=F\cap V\), the fort must have the lifted form \(A\cup\{p_v:v\in A\}\). Every peripheral vertex outside \(F\) sees either zero or two vertices in \(F\). For each original vertex \(u\notin A\), the number of neighbors inside \(F\) is precisely \(|N_G(u)\cap A|\). Hence this lifted set is a fort of \(H\) if and only if \(A\) is a fort of \(G\). In particular \(A\ne\varnothing\).

Moreover a proper fort subset of such a lifted \(F\) cannot contain two vertices of a private clique, so it too must be lifted from a nonempty fort subset of \(A\). Consequently the lifted set is inclusion-minimal exactly when \(A\) is inclusion-minimal in \(G\). This proves the classification and both minimal-fort formulas, including the mixed-clique weights.

**2. From forts to zero forcing.** For any finite graph, a blue set \(S\) is zero forcing if and only if it intersects every fort. To see this directly, if \(S\) misses a fort then no sequence of valid forces can enter that fort: the first supposed force into it would come from an outside blue vertex with exactly one neighbor in the fort. Conversely, if the forcing process stalls with white vertices remaining, the nonempty final white set is a fort disjoint from the initial blue set. This gives the equivalence without an external assumption.

The peripheral-pair forts from part 1 imply that a zero-forcing set \(S\subseteq V(H)\) omits at most one vertex of every \(C_v\). Define
\[
B(S)=\{v\in V:\ v\notin S,\ |C_v\setminus S|=1\},
\qquad T(S)=V\setminus B(S).
\]
A lifted minimal fort \(A\cup\{p_v:v\in A\}\) can be completely disjoint from \(S\) precisely when \(A\subseteq B(S)\): for each \(v\in A\), the omitted core and omitted private vertex give the required pair. Therefore the lifted-fort intersection condition is equivalent to \(B(S)\) containing no fort of \(G\), which by the same equivalence holds precisely when \(T(S)\) is zero forcing in \(G\).

**3. Exact local weights and bijection.** Fix \(T\in\mathscr Z(G)\). At \(v\notin T\), both the core \(v\) and exactly one private vertex are white. The other \(r_v-1\) private vertices are blue, giving \(r_v\) possibilities and weight \(r_vz^{r_v-1}\). At \(v\in T\), either all private vertices are blue with the core white (weight \(z^{r_v}\)), all private vertices and the core are blue (weight \(z^{r_v+1}\)), or the core is blue and exactly one private vertex is white (\(r_v\) choices, weight \(r_vz^{r_v}\)). Their sum is \(z^{r_v}(r_v+1+z)\). Choices at different original vertices are independent, and every zero-forcing subset appears in exactly one such decomposition according to its uniquely determined \(T(S)\). Multiplication gives the mixed polynomial. When all sizes equal \(r\), taking out \(r^nz^{n(r-1)}\) and recognizing the definition of \(\mathcal Z_G\) yields the substitution formula.

**4. Minimum and its multiplicity.** The least exponent in the summand indexed by \(T\) is \(\sum_v(r_v-1)+|T|\). All coefficients are nonnegative, so the smallest contributing \(|T|\) is \(q\), and each such \(T\) contributes exactly \(\prod_{v\in T}(r_v+1)\prod_{v\notin T}r_v\) terms at that degree. This proves the stated minimum and exact labeled count. No monotonicity or unproved enumerative assertion is used.

## Verification

The accompanying standalone `VERIFY.py` independently constructs graph adjacencies from edge masks, directly simulates the standard forcing process, tests the fort condition, extracts all inclusion-minimal forts by subset comparisons, and compares entire coefficient dictionaries against the two formulas. It includes *all* labeled base graphs of orders \(1\) through \(4\), uniform private-clique orders \(2\) and \(3\) where computationally feasible, nonuniform sizes \(2\) and \(3\), and seven further base graphs of order \(5\). Command: `python3 VERIFY.py`. Observed result: `VERIFY_OK: 104 graph-corona instances, 537504 direct vertex subsets; uniform and mixed clique sizes; all zero-forcing coefficients and all minimal-fort coefficients`. These finite tests corroborate but do not replace the proof for all graph orders.

For a concrete small instance, the base \(G=K_2\) with \(r=2\) gives \(\mathcal Z_H(z)=12z^3+13z^4+6z^5+z^6\) and \(\mathcal M_H(z)=2z^2+4z^4\); both follow directly and are independently counted by the checker.

## Relationship to prior work

Becker, Cameron, Hanely, Ong, and Previte (arXiv:2404.05963v1, first public 2024-04-09) establish a general peripheral-clique minimal-fort construction in Proposition 22 and a lifted minimal-fort construction for **cycle** bases in Proposition 23. Their accompanying warning identifies failure of that lifting for certain arbitrary bases when the attached clique has size one. Those results neither classify every minimal fort for arbitrary base graphs with attached cliques of order at least two nor give an all-graph zero-forcing polynomial transform. The classification here distinguishes the local pair obstructions from all lifted forts and exploits the assumption \(r_v\geq2\) in the converse.

Boyer and collaborators (arXiv:1801.08910v1, first public 2018-01-26) introduce and study the full zero-forcing polynomial but do not state this clique-corona substitution. Javaid, Irshad, Batool, and Raza (arXiv:1607.04071v1, first public 2016-07-14, Theorem 2.3) establish the **scalar** zero-forcing number for coronas of connected graphs, implying the uniform minimum above; that scalar fact is not claimed as new. Abara and Pelayo (arXiv:2202.04997v1) study maximal failed zero-forcing sets of graph products, including coronas of complete graphs, rather than the exact polynomial transfer for arbitrary bases.

## Limitations

The hypothesis \(r_v\geq2\) is essential: at size one, an outside private vertex is unavailable to rule out a lone selected private vertex with unselected core, and the stated classification and polynomial transform need not hold. The general base graph's own zero-forcing polynomial or minimal forts may still be difficult to compute; this result is a complete symbolic reduction, not a polynomial-time algorithm for arbitrary \(G\). It does not address arbitrary attached nonclique graphs, other forcing rules, orbit counts, or independent verification of publication priority. Some later journal-version material was not fully inspected; an unindexed or later equivalent result remains possible.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1, 2024-04-09, Sections 2 and 5.2, Propositions 22–23. https://arxiv.org/pdf/2404.05963
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, 2018-01-26. https://arxiv.org/pdf/1801.08910
3. I. Javaid, I. Irshad, M. Batool, Z. Raza, *On the zero forcing number of corona and lexicographic product of graphs*, arXiv:1607.04071v1, 2016-07-14, Theorem 2.3. https://arxiv.org/pdf/1607.04071
4. M. N. M. Abara, P. A. B. Pelayo, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1, 2022-02-10. https://arxiv.org/pdf/2202.04997
