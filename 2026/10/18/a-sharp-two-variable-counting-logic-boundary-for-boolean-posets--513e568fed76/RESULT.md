# A sharp two-variable counting-logic boundary for Boolean posets

## Finding
Let \(B_n\) be the Boolean lattice of subsets of an \(n\)-element set, considered **only as a finite partial order** in the signature containing a single reflexive order relation \(\leq\). For every integer \(n\geq0\), the following are equivalent:

1. Every finite partial order satisfying exactly the same two-variable first-order sentences with counting quantifiers (\(C^2\)) as \(B_n\) is isomorphic to \(B_n\).
2. \(n\leq3\).

For each \(n\geq4\), the proof explicitly constructs a nonlattice partial order \(Q_n\) on exactly \(2^n\) points with \(Q_n\equiv_{C^2}B_n\). Thus failure first occurs at the natural four-atom Boolean lattice, with sixteen points. Equivalence is relative to **finite partial orders**, not to arbitrary one-binary-relation structures; no Boolean operations, constants, rank predicates, or named atoms occur in the language.

## Assumptions and scope
A partial order is reflexive, antisymmetric and transitive. For elements \(x,y\), write \(x<y\) for \(x\leq y\) and \(x\ne y\). The logic \(C^2\) permits equality, the order predicate, arbitrary Boolean connectives and counting quantifiers but at most two reusable variable symbols. For a finite structure, \(C^2\)-identification **within posets** means no nonisomorphic finite poset satisfies the same \(C^2\) sentences.

The zero-atom case \(B_0\) is the singleton. We always count elements, not atoms, in the cardinality \(2^n\). These are order reducts of Boolean algebras, and the result is not asserted in the richer Boolean-algebra functional language or among lattices alone.

## Proof
**1. The counting criterion.** Suppose two finite posets \(P,P'\) have corresponding partitions \(P=\bigsqcup_{i\in I}C_i\) and \(P'=\bigsqcup_{i\in I}C_i'\) with equal block sizes. Assume that for every \(i,j\), every point in \(C_i\) has the same numbers of points in \(C_j\) related by each of the four ordered atomic types: equality, strict below, strict above and incomparability; the same numbers occur for every point in \(C_i'\) relative to \(C_j'\). Then \(P\equiv_{C^2}P'\).

Indeed, atomic two-variable formulas depend only on the ordered atomic type. Every formula with at most two free variables is built, after bound-variable scoping, from such atomic tests and subformulas with at most one free variable. Inductively, a one-free-variable \(C^2\) formula has constant truth value on corresponding blocks. Each counting quantifier over the second variable reduces to a sum of the corresponding atomic-type counts into blocks satisfying its one-variable subconditions. Therefore the truth value of every sentence agrees. This is the edge-coloured counting-refinement characterization specialized to the order language.

**2. The identified cases.** In \(B_n\), an element of subset size \(r\) has exactly \(2^r-1\) strict predecessors and \(2^{n-r}-1\) strict successors. These pairs of counts determine \(r\). Both counts and the number of elements of each such unary counting type are \(C^2\)-invariants. A poset \(C^2\)-equivalent to \(B_n\) thus has \(\binom nr\) elements in the corresponding type \(r\), no within-type strict comparisons, and the same numbers of comparisons to every other type.

For \(n\leq2\) this forces the singleton, two-element chain, or four-element diamond, respectively. At \(n=3\), the four type sizes are \(1,3,3,1\). The extreme singleton types are a bottom and a top, and every one of the three type-one elements lies below exactly two of the three type-two elements; conversely each type-two element lies above exactly two type-one elements. The resulting simple bipartite graph is a two-regular graph on \(3+3\) vertices, hence necessarily a single six-cycle, equivalently the complement of a perfect matching in \(K_{3,3}\). All other comparisons are forced. Therefore the poset is isomorphic to \(B_3\).

**3. A sixteen-point witness.** Let \(A=\{1,2,3,4\}\) and define \(T\) to have five strata \(T_0,\dots,T_4\) of sizes \(1,4,6,4,1\). Give the points in these strata the following subset supports of \(A\): respectively \(\varnothing\); all four singleton subsets; three distinct copies of \(\{1,2\}\) and three distinct copies of \(\{3,4\}\); all four triple subsets; and \(A\). For points in distinct strata, declare \(x<y\) precisely when the support of \(x\) is a proper subset of the support of \(y\). For points in the same stratum, only equality holds. Set \(x\leq y\) when \(x=y\) or \(x<y\). Support inclusion proves transitivity, and increasing stratum index proves antisymmetry; hence \(T\) is a poset.

This construction preserves all ordered atomic-type counts between corresponding strata of \(B_4\). The only nontrivial comparisons to check are: every singleton is below three of the six middle points and three of the four triple points; every middle point is above two singletons and below two triples; and every triple is above exactly three middle points. The last assertion uses the fact that every triple of \(A\) contains exactly one of the two complementary pairs \(\{1,2\}\), \(\{3,4\}\), and each pair has multiplicity three. These are exactly the binomial comparison counts in \(B_4\). Equal-stratum elements are incomparable unless equal in both posets. Step 1 yields \(T\equiv_{C^2}B_4\).

But the atoms supported on \(\{1\}\) and \(\{2\}\) have three distinct incomparable minimal common upper bounds: the three copies of \(\{1,2\}\). Their join does not exist. Therefore \(T\) is not a lattice and in particular is not isomorphic to \(B_4\).

**4. Persistence in every higher dimension.** Cartesian products of posets have the componentwise order. If \(P,P'\) satisfy the partition criterion of Step 1, then so do \(P\times R\) and \(P'\times R\) for any finite poset \(R\): use the blocks \(C_i\times\{r\}\) and \(C_i'\times\{r\}\), for every \(i\) and every \(r\in R\). For fixed \(r,s\), the comparison type between \((x,r)\) and \((y,s)\) is determined entirely by the comparison types of \(x,y\) and of the fixed pair \(r,s\); summing matching counts proves the criterion. Hence \(P\times R\equiv_{C^2}P'\times R\).

For every \(n\geq4\), set \(Q_n=T\times B_{n-4}\). Since \(B_4\times B_{n-4}\cong B_n\), Step 3 and the product observation prove \(Q_n\equiv_{C^2}B_n\). If \(a,b\) are the two atoms of \(T\) lacking a join, then \((a,\varnothing),(b,\varnothing)\) lack a join in \(Q_n\): any least upper bound would project to a least upper bound for \(a,b\) in \(T\). Thus \(Q_n\) is not a lattice, proving nonisomorphism for every \(n\geq4\). This completes the proof.

## Verification
Run `python3 verify_boolean_c2.py` using Python's standard library. The program independently constructs both base posets, tests reflexivity/antisymmetry/transitivity of the sixteen-point witness, checks its full rank-pair atomic-type count table, and confirms the missing join. It also enumerates all six labelled three-by-three degree-two incidence matrices, verifies that they are perfect-matching complements, and compares exact shared colour-refinement signatures of \(B_n\) and \(Q_n\) for \(4\leq n\leq8\), with up to 256 points per poset.

The exhaustive finite tests corroborate the construction and the small-case combinatorics. The **all-dimension assertion comes from the preceding proof and product lemma**, not from extrapolating those tests.

## Relationship to prior work
Kiefer, Schweitzer and Selman (arXiv:1503.08792v1, first public 2015-03-30) characterize finite relational structures identifiable by \(C^2\) among arbitrary structures and establish the coloured-degree framework. This is a general logical framework, not the explicit sharp Boolean-poset identification boundary relative to the class of posets; the latter requires the transitivity restriction for its positive cases and the order-preserving sixteen-point construction for its negative cases. Bova, Ganian and Szeider (arXiv:1408.4263v1) address quantified conjunctive-query model checking on finite posets, rather than \(C^2\)-isomorphism identification. Otto's 1995 canonization work provides foundational context for two-variable counting logic.

An earlier exhaustive eight-point poset classification settles the positive eight-point case as a special consequence; no novelty is claimed for that isolated classification. The present contribution is the explicit sixteen-point obstruction, the sharp Boolean-family threshold, and its all-dimension product propagation. Searches did not establish priority; an unlocated specialized treatment remains possible.

## Limitations
The identification result is restricted to finite posets in the order-only language. The negative examples are not lattices (nor necessarily graded), so they do not settle \(C^2\)-identifiability among lattices, distributive lattices, or Boolean-algebra expansions. The verification checks finite parameters through \(n=8\), not all dimensions. The priority assessment is based on inspected sources and recorded searches, not a proof of novelty.

## References
1. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1 (2015), especially Sections 2 and 5. https://arxiv.org/abs/1503.08792
2. S. Bova, R. Ganian and S. Szeider, *Quantified Conjunctive Queries on Partially Ordered Sets*, arXiv:1408.4263v1 (2014). https://arxiv.org/abs/1408.4263
3. M. Otto, *PTime Canonization for Two Variables with Counting*, LICS (1995), 342–352. DOI:10.1109/LICS.1995.523269.
