# Complete counting-logic, lattice, and orbit stratification of rank-three Eulerian posets

## Finding

Consider finite bounded Eulerian posets of rank three in the language of **one strict binary order relation** \(\lt\). Such a poset has ranks \(0,1,2,3\), with a unique bottom and top. Write \(r\) for its number of atoms. Then \(r\ge 2\), there are also \(r\) coatoms, and it has \(2r+2\) elements.

**Classification theorem.** The isomorphism classes for fixed \(r\) are indexed by integer partitions \(\lambda\vdash r\) whose parts are at least two. The incidence graph between rank-one and rank-two elements is the disjoint union of the bipartite cycles \(C_{2k}\), one for every part \(k\) of \(\lambda\). Let \(s(\lambda)\) be the number of distinct part sizes.

1. **Counting-logic width.** All such posets with the same \(r\) satisfy exactly the same sentences of two-variable first-order logic with counting quantifiers, \(C^2\), regardless of \(\lambda\). Different values of \(r\) have different \(C^2\) theories. Directed counting colour refinement stabilizes at the four rank levels, of sizes \(1,r,r,1\). Conversely, every individual poset in this class is identified up to isomorphism **within the class** by a \(C^3\) sentence of quantifier rank at most \(\lceil\log_2 r\rceil+3\). Thus three counting-variable names are necessary and sufficient for isomorphism identification throughout every fixed-size layer with \(r\ge4\), while two suffice for the singleton layers \(r=2,3\).
2. **Lattice boundary.** The poset is a lattice if and only if \(\lambda\) has no part equal to two. Consequently, latticehood is not definable by any \(C^2\) sentence even within this restricted Eulerian class. Its first failure of invariance is exactly at ten elements: the unique two isomorphism types for \(r=4\), indexed by \((4)\) and \((2,2)\), are \(C^2\)-equivalent, but only the former is a lattice. In contrast, latticehood within the class is definable by a single \(C^3\) sentence, so three is the exact required number of counting-variable names.
3. **Hidden automorphism orbits.** The automorphism-orbit partition has \(2+2s(\lambda)\) classes: the two extremal singletons and, for each distinct part size \(k\), one atom orbit and one coatom orbit, each of size \(k\) times the multiplicity of \(k\). Directed counting refinement recovers these orbits precisely if all parts of \(\lambda\) are equal. Its first failure within this Eulerian class is exactly at twelve elements, for \(\lambda=(3,2)\); the orbit sizes are \(1,1,2,2,3,3\) versus the four refinement-cell sizes \(1,1,5,5\). For fixed \(r\), the maximum number of automorphism orbits among the single \(C^2\) equivalence class is
   \[
   2+2\left\lfloor\frac{\sqrt{8r+9}-3}{2}\right\rfloor.
   \]
4. **Exact census.** With \(p_{\ge k}(n)\) the number of integer partitions of \(n\) with every part at least \(k\), and with the empty partition counted at \(n=0\), the numbers of isomorphism types, lattices, nonlattices, and orbit-refinable types at fixed \(r\ge2\) are, respectively,
   \[
   T_r=p_{\ge2}(r),\qquad L_r=p_{\ge3}(r),\qquad N_r=p_{\ge2}(r-2),\qquad F_r=\tau(r)-1.
   \]
   Here \(\tau(r)\) is the number of positive divisors of \(r\), and \(p_{\ge2}(n)=0\) for \(n<0\). The generating functions, including the formal empty partition at \(r=0\), are
   \[
   \sum_{r\ge0}T_r z^r=\prod_{k\ge2}(1-z^k)^{-1},\qquad
   \sum_{r\ge0}L_r z^r=\prod_{k\ge3}(1-z^k)^{-1},\qquad
   \sum_{r\ge0}N_r z^r=z^2\prod_{k\ge2}(1-z^k)^{-1}.
   \]

The structural cycle decomposition itself is established background; the finding here is its joint complete counting-logic, lattice-definability, and orbit-refinement stratification, including the sharp boundaries and counts.

## Assumptions and scope

A finite bounded graded poset has a unique least element \(\hat 0\), a unique greatest element \(\hat 1\), and an integer rank function increasing by one along cover edges. Rank three means \(\rho(\hat1)=3\). Eulerian means that in every nontrivial interval, the number of elements of even relative rank equals the number of elements of odd relative rank. The vocabulary consists solely of a strict order predicate, with equality built into logic. Neither rank colours, cover edges, lattice operations, nor any constants are named.

A part \(k\ge2\) of \(\lambda\) encodes an incidence component with \(k\) atoms and \(k\) coatoms in an alternating simple cycle. This includes \(k=2\), whose incidence graph is \(K_{2,2}=C_4\). For \(r=2\) the poset is not a lattice; for \(r=3\) its sole type is the Boolean lattice on three atoms. Every statement about definability is restricted to the class of finite bounded Eulerian rank-three posets, not to all finite posets.

## Proof

**Step 1: exact structure.** A rank-two nontrivial interval in an Eulerian poset has equally many even- and odd-rank elements. Its two endpoints have even relative rank, so exactly two rank-one elements lie strictly between them. Apply this to \([\hat0,c]\) for every coatom \(c\), and to \([a,\hat1]\) for every atom \(a\). Every coatom covers exactly two atoms and every atom is covered by exactly two coatoms. Applying the Eulerian condition to \([\hat0,\hat1]\) yields equality of the atom and coatom numbers. The middle-rank incidence graph is therefore a simple two-regular bipartite graph, hence a disjoint union of even simple cycles of lengths at least four. Since rank is intrinsic, poset isomorphisms preserve its two bipartition sides. The multiset of half-cycle lengths, a partition \(\lambda\) of \(r\) into parts at least two, determines the poset up to isomorphism. Conversely every such multiset yields a bounded Eulerian rank-three poset: the length-two intervals contain exactly two intermediate elements, the full interval has equal parity counts, and length-one intervals are automatically Eulerian. This also proves \(r\ge2\).

**Step 2: full \(C^2\) collapse.** In these structures the order-theoretic ranks are characterized by strict predecessor and successor counts: the bottom has none below, the top none above, an atom has exactly one strict predecessor, and a coatom exactly one strict successor. Thus one counting-refinement round distinguishes the four levels. Their sizes are \(1,r,r,1\). Between levels, the numbers of smaller, larger, equal, and incomparable elements relative to a vertex are determined only by \(r\): each atom lies above the bottom, below exactly two coatoms and the top, and is incomparable with the other \(r-1\) atoms and remaining \(r-2\) coatoms; the dual statement holds for a coatom. The bottom and top are comparable with everyone. Hence the four-level partition is equitable for all strict-order atomic binary types and cannot refine further.

For completeness this proves equivalence of full \(C^2\) theories, not merely equality of a chosen refinement transcript. Induct on formulas using at most the two variable names \(x,y\). Every atomic formula depends solely on the two ranks and their atomic relationship (equality, strict order in either direction, or incomparability). This property persists under Boolean operations. Quantifying one of \(x,y\), including exact or threshold counting quantifiers, sums truth values over atomic relationship types to the remaining variable; their multiplicities depend only on that variable's rank and on \(r\), as just calculated. Thus every formula's value depends only on \(r\), the ranks of its free variables, and their atomic relationship. In particular every sentence depends only on \(r\). Conversely \(\exists^{=2r+2}x\,(x=x)\) separates distinct sizes.

**Step 2b: logarithmic-depth identification in three variables.** Define the rank-one predicate \(A(u)\) and the rank-two predicate \(C(u)\) by one strict predecessor and one strict successor, respectively (as made explicit below). Set \(M(u)=A(u)\lor C(u)\). Using three variable names, define a binary formula \(D_0(x,y)\) saying that \(x,y\) are middle-rank vertices and are equal or comparable. Recursively define
\[
D_{j+1}(x,y):=\exists z\,\bigl(D_j(x,z)\land D_j(z,y)\bigr).
\]
In the two occurrences of \(D_j\), rename the internally bound variable to the third available symbol; shadowing is harmless because the two subformulas have disjoint scopes. Thus each \(D_j\) is a three-variable counting formula, and its quantifier rank is at most \(j+1\). By induction it expresses incidence-graph distance at most \(2^j\) between middle-rank vertices. Every cycle component \(C_{2k}\) has diameter \(k\le r\). With \(t=\lceil\log_2 r\rceil\), \(D_t(x,y)\) therefore expresses membership of \(x,y\) in the same middle-incidence component.

For each \(k\in\{2,\ldots,r\}\), the one-variable formula
\[
H_k(x):=A(x)\land\exists^{=2k}y\,D_t(x,y)
\]
selects precisely the atoms belonging to components of length \(2k\). An atom in such a component is counted \(k\) times across that component's atoms, so if \(m_k\) is the multiplicity of part \(k\) in \(\lambda\), the sentence \(\exists^{=k m_k}x\,H_k(x)\) fixes \(m_k\). The conjunction of these sentences for all \(2\le k\le r\), together with a cardinality clause when desired, identifies the entire partition and hence the poset among rank-three Eulerian posets. Its quantifier rank is at most \(t+3\). For \(r\ge4\), at least two different allowed partitions exist, so Step 2 shows that no \(C^2\) sentence identifies either of them in the class. For \(r=2,3\), the class has only one isomorphism type per cardinality. This proves the sharp variable-width assertion and the logarithmic quantifier-rank upper bound; no optimal quantifier-rank lower bound is claimed.

**Step 3: lattice and variable width.** A pair of distinct atoms has the top as an upper bound, together with their common coatoms. It has a join precisely if it has at most one common coatom. Dually, a pair of distinct coatoms has a meet precisely if it has at most one common atom. All cross-rank pairs have meets and joins: comparable pairs use their smaller and larger elements, while incomparable atom-coatom pairs use the bottom and top. Hence the whole poset is a lattice if and only if its middle incidence graph contains no \(K_{2,2}\). In a two-regular bipartite graph a \(K_{2,2}\) is necessarily an entire \(C_4\) component. This proves the criterion \(2\notin\lambda\).

Using only three variable names, let the formulas \(A(u)\) and \(C(u)\) abbreviate “\(u\) has exactly one strict predecessor” and “\(u\) has exactly one strict successor,” respectively; their bound variables may reuse any of \(x,y,z\) by ordinary variable shadowing. The sentence
\[
\exists x\,\exists y\,\bigl(x\ne y\land A(x)\land A(y)\land
\exists^{\ge2}z\,(C(z)\land x<z\land y<z)\bigr)
\]
uses only \(x,y,z\) and expresses **nonlatticehood** within the stated class. Its negation expresses latticehood. In contrast, the two structures \(\lambda=(4)\) and \(\lambda=(2,2)\), each having ten elements, share all \(C^2\) sentences by Step 2 while differing in latticehood. At \(r=2\) and \(r=3\) there is just one type per size, and the class has no other cardinalities below ten; therefore ten is the sharp first mixed order. No assertion is made that ten is the minimum over unrestricted finite posets.

**Step 4: exact orbits.** Any automorphism fixes the bottom and top and permutes the connected components of the middle incidence graph preserving their cycle lengths. On each cycle \(C_{2k}\), the side-preserving dihedral automorphisms act transitively on its \(k\) atoms and on its \(k\) coatoms. Equal-sized cycle components may also be permuted. Components of different sizes cannot be interchanged. Thus the orbits consist of two extremal singletons and two orbits for each distinct half-cycle length, of the sizes stated in the finding. Step 2 gives only four stable refinement classes, so these equal the orbit partition if and only if \(\lambda\) has one distinct part size. For \(r\le4\), all partitions into parts at least two have this property; at \(r=5\), \((3,2)\) is the unique partition with two distinct part sizes. This proves the sharp twelve-element orbit threshold.

If \(s\) distinct part sizes occur, their least possible sum is \(2+3+\cdots+(s+1)=s(s+3)/2\). Conversely, whenever this sum is at most \(r\), increasing the largest part by the surplus realizes exactly \(s\) distinct allowed sizes. Therefore \(s\) attains every value up to \(\left\lfloor(\sqrt{8r+9}-3)/2\right\rfloor\), proving the maximum orbit-class formula. In particular the orbit/refinement class-count discrepancy is unbounded as \(r\) grows despite complete \(C^2\) equivalence at each cardinality.

**Step 5: exact census.** Cycle decomposition gives \(T_r=p_{\ge2}(r)\). Excluding \(C_4\) components gives \(L_r=p_{\ge3}(r)\). Removing one part equal to two bijects partitions containing a two with all partitions of \(r-2\) into parts at least two, so \(N_r=p_{\ge2}(r-2)\). Orbit-refinability requires every part to have one common size \(k\), which is equivalent to a divisor \(k\mid r\) with \(k\ge2\), giving \(F_r=\tau(r)-1\). Standard integer-partition product series yield the displayed generating functions.

## Verification

Two standalone Python programs requiring only the standard library are included: `verify_eulerian.py` and `verify_incidence_enum.py`. Their captured outputs are included as `eulerian_output.txt` and `incidence_output.txt`.

The first constructs every allowed cycle-type partition for \(2\le r\le16\) (230 nonisomorphic test structures). It checks the full strict-order interval parity condition, all pairwise meets and joins, a direct three-variable witness predicate, the stabilizing refinement partition and its equivalence across cycle types, complete middle-incidence connectivity recovery using \(\lceil\log_2 r\rceil\) Boolean adjacency squarings, every lattice and nonlattice partition count, the divisor criterion for orbit-refinability, and the extremal distinct-part bound. For \(r\le5\) it additionally computes the complete automorphism orbit partition by enumerating all rank-preserving atom/coatom permutations; this is a separate exact check of the group-action argument.

The second enumerates every labeled simple bipartite incidence matrix with row and column sums two for \(2\le r\le5\), without using the partition-based poset builder. There are respectively \(1,6,90,2040\) such matrices. It reconstructs their connected cycle components, independently tests the \(C_4\) lattice criterion, and checks uniform atomic-type profiles. These are finite validation checks of the construction, not substitutes for the all-order proof.

The ten-element representatives can be reconstructed with `poset((4,))` and `poset((2,2))`; both have stable rank-class sizes \((1,4,4,1)\), while the former is a lattice and the latter is not. The twelve-element non-refinable representative is `poset((2,3))`.

## Relationship to prior work

The small-rank structural classification of Eulerian posets as alternating cycle components is already described in the mathematical literature and is **not** claimed as new. The public exposition “Eulerian poset” (created 2013-03-22, drawing on Stanley) gives this description for rank three. The finite-model-theoretic connection of colour refinement with two-variable counting logic and the general concept of refinability are likewise established background; see the references below.

An earlier finite-poset result identifies the unbounded-rank-free eight-element counting-logic collision between two four-cycles and one eight-cycle in a height-two incidence order. Its underlying pair is related to the ten-element witness here by adjoining global extrema; that witness by itself is therefore not the central novelty claim. What is asserted here is the **all-order, exact four-way classification** of counting-logic theories, latticehood, automorphism orbits and orbit-refinability within Eulerian rank-three posets, including the variable-width boundary and exact enumerators. No inspected source directly states that combined result. General equitable-partition and inversion theorems supply ingredients but do not by themselves give the poset-specific census, logarithmic-depth three-variable identification bound, and structural cross-classification without the argument above. In particular, Kiefer–Schweitzer–Selman (2015) give general classifications of \(C^2\)-identified finite relational structures and graph orbit representatives; those conclusions neither assert within-class \(C^3\) identification for Eulerian rank-three posets nor determine which members of the one fixed-size Eulerian \(C^2\) theory are lattices or orbit-refinable.

## Limitations

The conclusion concerns finite bounded Eulerian posets of **rank exactly three**, presented as a strict binary relation. It does not characterize latticehood on all finite posets, arbitrary Eulerian ranks, or languages enriched with join and meet operations or named cycle-component predicates. The three-variable identification sentence distinguishes structures only **within** the finite bounded Eulerian rank-three class; it is not claimed to characterize that class in an unrestricted binary-relation universe. The \(C^3\) bound is a number of variable names with counting; no lower bound is claimed for ordinary three-variable logic without counting, and no minimal quantifier rank is claimed. The computations cover only the finite ranges stated; the proofs cover all allowed \(r\).

The comparison of accessible published literature and indexed mathematical research did not identify an equivalent complete theorem. Uninspected specialized work on low-rank Eulerian structures or finite-variable logic could contain related or dominating statements. The cycle decomposition, integer-partition identities, and equitable-partition observations are standard ingredients; the contribution is their exact logical and orbit-theoretic synthesis, not independent discovery of those ingredients. The scientific review is not an independent audit.

## References

- “Eulerian poset,” PlanetMath, created 2013-03-22; section “Eulerian posets of small rank.” https://planetmath.org/eulerianposet
- M. Grohe, K. Kersting, M. Mladenov, and E. Selman, “Dimension Reduction via Colour Refinement,” arXiv:1307.5697, originally submitted 2013-07-22. https://arxiv.org/abs/1307.5697
- V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” arXiv:1502.01255, originally submitted 2015-02-04. https://arxiv.org/abs/1502.01255
- S. Kiefer, P. Schweitzer, and E. Selman, “Graphs Identified by Logics with Counting,” arXiv:1503.08792, originally submitted 2015-03-30. https://arxiv.org/abs/1503.08792
