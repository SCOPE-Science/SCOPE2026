# The 143 rank-three theories of finite permutation digraphs and a sharp 19-point kernel

## Finding
In the relational vocabulary consisting of equality and one directed binary relation \(R\), consider all **nonempty finite bijection structures**: \(R(x,y)\) holds precisely when a permutation sends \(x\) to \(y\). Fixed points are represented by loops. Two structures are rank-three equivalent when they agree on all first-order sentences of quantifier rank at most three.

**Theorem.** This class has exactly **143** rank-three equivalence classes. Every such structure is rank-three equivalent to one containing at most **19** points, and 19 is the least universal bound. Exactly one equivalence class has minimum representative order 19. Its cycle-type is
\[
1^3\,2^2\,3\,4\,5,
\]
meaning three fixed points, two 2-cycles, and one cycle of each length 3, 4, and 5. This notation specifies cycle multiplicities, not a product in the structure language.

## Assumptions and scope
Every model is a nonempty finite set equipped with one *binary relation* that is the graph of a bijection. No built-in ordering, numeric labels, counting quantifiers, or unary function symbol is available to formulas. In particular, a unary function syntax with arbitrary iterated terms would give a different quantifier-rank hierarchy. The result concerns the ordinary quantifier rank \(3\), not three-variable logic of unrestricted rank. A directed \(j\)-cycle may have \(j=1\) (a loop) or \(j=2\) (both directed edges between two vertices).

## Proof
**1. An exact three-round signature.** For any structure \(G\), a chosen ordered pair \((x,y)\) has a quantifier-free atomic description
\[
A_G(x,y)=([x=y],[R(x,x)],[R(y,y)],[R(x,y)],[R(y,x)]).
\]
For each \(z\notin\{x,y\}\), record the five-bit pattern
\[
P_G(x,y;z)=([R(x,z)],[R(z,x)],[R(y,z)],[R(z,y)],[R(z,z)]).
\]
Let \(M_G(x,y)\) be the *set* of patterns realized by such \(z\). The rank-one type of the pair is determined exactly by \((A_G(x,y),M_G(x,y))\): the cases \(z=x\) and \(z=y\) are already determined by \(A_G\), and the distinct cases give precisely the quantifier-free three-variable types needed for one additional move. Consequently, the complete rank-three theory of \(G\) is determined exactly by the nested set signature
\[
\Sigma_3(G)=\left\{\left\{(A_G(x,y),M_G(x,y)):y\in G\right\}:x\in G\right\}.
\]
Two finite relational structures are rank-three equivalent if and only if these signatures agree. This is the depth-three Hintikka-type recursion, equivalently the three-move Ehrenfeucht–Fraïssé game, including repeated choices of vertices.

**2. Infinite-to-finite reduction.** A bijection structure is a disjoint union of directed cycles. Fix a root \(x\). For a second point \(y\) in the same cycle, the possible third-vertex patterns are determined by whether \(y=x\), \(y\) is a predecessor or successor, \(y\) is two directed steps away in either direction, or both directed distances are at least three. The only possibly nonzero incidences with a distinct third vertex are at predecessors and successors of \(x\) and \(y\). When a cycle has length at least seven, these local cases are all realized, and in the final case at least one further vertex has no incidence with either chosen vertex. The set of pair signatures is therefore unchanged when that component's length is replaced by seven, irrespective of other components. The same statement follows for pair signatures with the second vertex in another component: a long component always supplies vertices beyond the at most four nearby candidates.

For a fixed cycle length, replacing any multiplicity greater than three by three likewise preserves \(\Sigma_3\). A pair \((x,y)\) occupies at most two components, and a third copy, if needed, already supplies every pattern that additional copies could supply. Other component lengths remain unaffected. Both reductions can also be checked case-by-case in the explicit pattern formula in `verify.py`; the argument applies to all finite lengths and multiplicities, not only to sampled orders.

Thus every nonempty structure is rank-three equivalent to a canonical union specified by one vector \((c_1,\ldots,c_7)\in\{0,1,2,3\}^7\setminus\{(0,\ldots,0)\}\), where \(c_j\) copies have length \(j\). The reduction never increases the number of vertices.

**3. Exhaustive exact classification.** There are \(4^7-1=16,383\) canonical vectors. `verify.py` calculates \(\Sigma_3\) without enumerating all triples: for each cycle length that occurs it chooses one rooted vertex, considers each possible second vertex in its component or another component, and constructs the third-vertex set from the predecessor/successor candidates plus the two possible generic types (a distant loop or a distant nonloop). It computes the rank-three signature literally as nested immutable sets of atomic descriptions and five-bit masks. A dictionary keyed by these exact signatures has **143** entries. The program finds a representative with at most 19 points in every class, and its minimum-order representative manifest is `minimal_representatives.csv` (143 data rows). It also finds only 142 types among canonical vectors of order at most 18, with exactly one additional type first occurring at order 19, represented by multiplicities \((3,2,1,1,1,0,0)\).

By step 2, a noncanonical structure of order at most 18 would reduce to a canonical structure of no greater order, so the missing type cannot have a smaller noncanonical representative. This proves sharpness. The entire finite computation is inspectable and reproducible using Python's standard library; the exact program and finite manifest are constituent parts of the proof.

## Verification
Run `python verify.py` in a directory containing this program. It generates `minimal_representatives.csv` and reports the complete 16,383-vector classification. An independently implemented *direct* type calculation builds every edge of a graph and enumerates every possible third vertex, not relying on the local predecessor/successor shortcut. The two methods agree on all 731 canonical representatives of order at most 19 and on 509 additional selected samples. The direct method checks additional long-cycle and multiplicity instances. See `verification_output.txt`. These finite tests corroborate the unlimited reductions; those reductions are proved in step 2 and are not extrapolated from tests.

## Relationship to prior work
Libkin's *Elements of Finite Model Theory* (2004), Chapter 3, gives the Ehrenfeucht–Fraïssé and Hintikka-type machinery and disjoint-union composition principles, but does not tabulate rank-three permutation-digraph theories. Otto's 2016 lecture notes study finite successor **strings**, not bijective successor structures with cycles. Albert, Bouvel and Féray (arXiv:1808.05459, 2018; published 2020) explicitly develop the same permutation-as-one-bijection binary relational language, distinguishing it from the two-orders language; inspection of its relevant definitions and results finds no 143-type or 19-point rank-three census. The literature on individual directed cycles gives component-level logical thresholds but not the simultaneous multiplicity interactions counted here.

## Limitations
The classification is solely for nonempty finite bijection structures in the binary-relation language and rank exactly at most three. It does not classify partial functions, nonbijective functions, infinite models, ordered permutations, counting logic, or larger ranks. Novelty claims remain qualified by the possibility of an unindexed equivalent enumeration. The exact finite calculation needs execution of the supplied standard-library program; the table is not asserted to be a human-hand enumeration.

## References
- L. Libkin, *Elements of Finite Model Theory*, Springer, 2004, Chapter 3, doi:10.1007/978-3-662-07003-1. An author-hosted full-text manuscript is at https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf .
- M. Otto, *Finite Model Theory*, lecture notes, 2016, Section 2.3.1 (successor strings), https://www2.mathematik.tu-darmstadt.de/~otto/LEHRE/FMT16.pdf .
- M. Albert, M. Bouvel, V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459 (first posted 2018), especially Sections 2 and 6, https://arxiv.org/pdf/1808.05459 .
