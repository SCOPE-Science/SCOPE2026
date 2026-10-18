# The complete two-matching counting-logic fibre and its sharp first orbit split

## Finding

Let \(A=(X,E,F)\) be finite, with \(E\) and \(F\) named equivalence relations on the same nonempty domain. Assume every class of each equivalence has size exactly two and the two classes containing any \(x\in X\) intersect only in \(x\). Let \(n=|X|\), and write \(t=n/2\).

**Theorem.** Such structures exist exactly for even \(n\ge4\). For each allowed \(n\), they form precisely one equivalence class under the complete two-variable first-order counting logic \(C^2\), even when compared with arbitrary finite structures interpreting \(E,F\) as equivalence relations. The isomorphism types in this logical class are indexed by the partitions of \(t\) into parts at least two; thus their number is \(p(t)-p(t-1)\), with \(p(0)=1\).

Every element has the same stable one-dimensional counting-refinement colour. If \(\lambda\vdash t\) is the indexing partition, the exact number of automorphism orbits on \(X\) is the number \(d(\lambda)\) of distinct part sizes. Consequently the first failure of the stable-colour partition to recover automorphism orbits occurs at \(n=10\), uniquely at \(\lambda=(3,2)\), with orbit sizes \(6,4\). For every allowed even \(n\), the maximum orbit count over this entire logical class is
\[
D(n)=\left\lfloor\frac{\sqrt{4n+9}-3}{2}\right\rfloor.
\]
The bound is attained by partitions with successive distinct small parts and any remaining weight added to the largest part.

## Assumptions and scope

All domains are finite and nonempty. The vocabulary contains exactly the two binary relation symbols \(E\) and \(F\). They are required to be reflexive, symmetric and transitive, but comparisons for the logical-equivalence assertion allow *all* such pairs of equivalences, not just those satisfying the class-size hypotheses. The equivalence \(C^2\) permits arbitrarily nested first-order quantification with only two reusable variables and exact counting quantifiers. Stable refinement records, for each current vertex colour, the numbers of points in all four atomic relation categories \((E(x,y),F(x,y))\); equality \(x=y\) is separately available.

Associate to \(A\) a two-sided incidence multigraph: the left vertices are the \(E\)-classes, the right vertices are the \(F\)-classes, and every \(x\in X\) contributes one edge joining its two classes. Side labels are part of the data and must be preserved by isomorphisms. The intersection hypothesis excludes parallel edges.

## Proof

**1. Structural decomposition.** Every incidence vertex has degree two. Since the graph is finite, bipartite, simple and 2-regular, every connected component is an even simple cycle of length at least four, say \(2k\) with \(k\ge2\). Its edges represent \(2k\) elements of \(X\); hence \(n=2\sum k\). Conversely, every multiset of such even cycles yields two equivalences satisfying the assumptions: elements are cycle edges, while the two equivalences group edges incident at a common left or right vertex. Any two side-coloured even cycles of the same length are isomorphic, and cycles of different lengths cannot be interchanged. Hence the complete incidence structure up to isomorphism is encoded exactly by a partition \(\lambda\) of \(t=n/2\) into parts \(k\ge2\). This also proves nonexistence when \(n\) is odd or \(n=2\).

**2. The full \(C^2\)-equivalence fibre.** In every admissible structure and at every point \(x\), the four joint relation types of a variable \(y\), arranged as \((E\wedge F,E\wedge\neg F,\neg E\wedge F,\neg E\wedge\neg F)\), have counts \((1,1,1,n-3)\). Thus uniform-start counting refinement does not split the single vertex colour at the first round or at any later round. Since \(n\) is fixed, all admissible structures have equal complete refinement histograms and hence agree in \(C^2\) by the standard finite-structure colour-refinement correspondence.

Conversely, let \(B\) be any pair of finite equivalence relations agreeing in \(C^2\) with such an \(A\). The logic expresses the cardinality \(n\) by \(\exists^{=n}x\,(x=x)\), and it expresses the three conditions
\[
\forall x\,\exists^{=2}y\,E(x,y),\qquad
\forall x\,\exists^{=2}y\,F(x,y),\qquad
\forall x\,\exists^{=1}y\,(E(x,y)\wedge F(x,y)).
\]
These formulas use only the variables \(x,y\). They hold in \(A\), so they also hold in \(B\). Therefore \(B\) belongs to the same degree-two, no-parallel-edge family. This proves that the claimed fibre is exact *relative to all finite two-equivalence structures*, not merely relative to the family.

**3. Counting nonisomorphic structures.** The usual partition function \(p(t)\) counts all integer partitions of \(t\); those having at least one part equal to one correspond bijectively, by deleting a single one, to all partitions of \(t-1\). Thus exactly \(p(t)-p(t-1)\) partitions have every part at least two. By Step 1 this is the isomorphism-type count.

**4. Automorphism orbits.** The automorphism group of the equivalence structure is the side-preserving automorphism group of its incidence graph, acting on graph edges. On any even cycle, rotation by two vertices and a side-preserving reflection act transitively on edges. Components of the same length may be permuted, while components of unequal lengths cannot be permuted. Consequently two domain elements are automorphic exactly when their incidence components have equal length, so the orbit count equals \(d(\lambda)\). The stable partition has just one class by Step 2.

There cannot be two distinct part sizes before \(t=2+3=5\). At \(t=5\) the only partition with distinct parts at least two is \((3,2)\). It yields the indicated cycle lengths \(6,4\) and orbit sizes \(6,4\), establishing the unique first orbit failure at \(n=10\).

**5. Sharp extremal count.** If \(d\) distinct integers are each at least two, their sum is at least \(2+3+\dots+(d+1)=d(d+3)/2\). Hence \(d(d+3)\le 2t=n\) and
\[
d\le\left\lfloor\frac{\sqrt{4n+9}-3}{2}\right\rfloor.
\]
For any allowed \(n\), let \(d\) be the integer on the right. The partition whose smallest \(d-1\) parts are \(2,3,\dots,d\) and whose last part is \(d+1+[t-d(d+3)/2]\) has exactly \(d\) distinct parts and total \(t\); for \(d=1\) take the single part \(t\). Equality is attained.

## Verification

Two reproducible Python programs are supplied. `verify_matching_cycles.py` generates all perfect matchings in the small orders \(n=4,6,8\) with one matching fixed, excludes shared matched pairs, builds the side-coloured incidence graphs and independently tests isomorphism with a graph-isomorphism algorithm. It recovers respectively \(1,1,2\) isomorphism types, agrees with the restricted-partition formula, and verifies that all domain elements have identical first-round joint atomic counts. `verify_first_orbit_gap.py` constructs the ten-element witness, calculates the connected-component lengths and explicitly enumerates side-preserving automorphisms; it finds one refinement colour and two orbits of sizes \(4,6\). The extremal inequality and rounding identity are also checked arithmetically through \(n=200\). These finite checks corroborate the proof but do not establish its infinite quantifiers.

Run with Python 3 and NetworkX 3 using `python verify_matching_cycles.py` and `python verify_first_orbit_gap.py` from the same directory. No random seeds are used.

## Relationship to prior work

Foundational work of Arvind, Köbler, Rattan and Verbitsky and of Kiefer, Schweitzer and Selman establishes colour refinement and its relation to \(C^2\); the latter gives general identification criteria for finite relational structures, including exceptional cases where logical identification need not recover automorphism orbits. Pratt-Hartmann studies the two-variable counting fragment with designated equivalence predicates. The theorem here determines a particular natural logical equivalence fibre *explicitly for every order* and resolves its entire orbit profile; general identification criteria do not themselves state the restricted-partition census or the first orbit split. The small \(n=8\) indistinguishable pair of alternating cycles is an established boundary and is not claimed as a new example. The all-order fibre count, orbit stratification, and sharp first orbit-failure size are the asserted contribution.

## Limitations

No claim is made about structures with equivalence classes larger than two, non-equivalence interpretations, initial vertex individualization, three-variable logic, or uniqueness of publication priority. The numerical verification is finite and the abstract partition and orbit arguments carry the infinite assertion. A general prior classification may yield this theorem as a corollary after additional analysis, and specialized literature outside inspected material could have an equivalent enumeration; independent audit has not been performed.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public 2015-02-04, especially introductory discussion of refinement and amenability.
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first public 2015-03-30, especially Sections 1 and 5 and Theorem 27 for general relational structures.
3. I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, Mathematical Logic Quarterly 61 (2015), 474–515, DOI:10.1002/malq.201400102, especially the introduction and Section 7.
