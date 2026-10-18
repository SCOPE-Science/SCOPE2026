# Eight pointed types and twelve minimal extremizers for two equivalences

## Finding
Let \(X\) be a nonempty finite set equipped with **two named equivalence relations** \(E\) and \(F\), in the first-order language consisting of \(E,F\) and equality only. Let \(t(X)\) be the number of distinct complete one-free-variable first-order types of quantifier rank at most one realized by elements of \(X\), with no parameters and no counting quantifiers.

**Theorem.** Every such structure has \(t(X)\leq 8\). Equality is attained if and only if all eight possible witness patterns with an element outside both its \(E\)-class and its \(F\)-class occur. Equality is impossible on fewer than \(12\) elements, is possible on \(12\), and is possible on every larger finite cardinality. Up to isomorphism preserving the names \(E\) and \(F\), **exactly twelve** twelve-element structures satisfy \(t(X)=8\). These twelve are classified by three support configurations, each with four weight assignments, as proved below.

**Corollary.** All structures satisfying \(t(X)=8\) have the same first-order sentence theory through quantifier rank two (though they need not be isomorphic). This follows because a rank-two sentence is a Boolean combination of existence claims about pointed rank-one types in this purely relational language.

## Assumptions and scope
There is no restriction on sizes or on interactions between the two equivalence partitions; their names are retained by isomorphisms. The universe is finite and nonempty. Quantifier rank counts nested ordinary first-order quantifiers, not distinct variable names; one free variable is permitted in the pointed types. No unary predicates, parameters, constants or counting quantifiers are used.

For \(x\in X\), define four bits by existence of witnesses \(y\in X\) **distinct** from \(x\):

\[
\begin{aligned}
a(x)&=[\exists y\ne x:\ E(x,y)\wedge F(x,y)],\\
b(x)&=[\exists y:\ E(x,y)\wedge\neg F(x,y)],\\
c(x)&=[\exists y:\ \neg E(x,y)\wedge F(x,y)],\\
d(x)&=[\exists y:\ \neg E(x,y)\wedge\neg F(x,y)].
\end{aligned}
\]

The last three predicates automatically force \(y\ne x\), since the equivalences are reflexive. Brackets denote truth values in \(\{0,1\}\). The pointed rank-one type of \(x\) is exactly the four-bit vector \((a(x),b(x),c(x),d(x))\).

## Proof
**Step 1: completeness of the witness pattern.** For fixed \(x\), every quantifier-free formula in \(x,y\) is a Boolean combination of equality and the four possibilities for \((E(x,y),F(x,y))\). The case \(y=x\) is always present and fixed. The other four disjoint possibilities with \(y\ne x\) are precisely those recorded by \(a,b,c,d\). Therefore every one-free-variable formula of rank at most one is determined by the four bits. Conversely each bit is expressed by a rank-one formula. Hence \(t(X)\) equals the number of distinct four-bit vectors realized.

**Step 2: the intersection multigraph.** Make a bipartite graph whose left vertices are \(E\)-classes, right vertices are \(F\)-classes, and occupied intersections are edges, weighted by the positive number of elements in that intersection. Write \(m(e)\) for the weight of an edge and \(\deg_E(e)\), \(\deg_F(e)\) for the degrees in the *simple support graph* (number of other intersection cells is relevant, not population). Every element in the cell \(e\) has

\[
a=[m(e)\ge2],\qquad
b=[\deg_E(e)\ge2],\qquad
c=[\deg_F(e)\ge2],
\]

and \(d=1\) exactly when some other occupied cell shares neither endpoint with \(e\).

**Step 3: universal bound.** If an edge \(e\) has \(d=0\), all occupied edges lie in the union of its left-endpoint star and right-endpoint star. The central intersection gives only one pointed type. Each left-only arm edge necessarily has \((b,c)=(1,0)\), and each right-only arm edge has \((b,c)=(0,1)\). Within each arm group, only the bit \(a\) can vary; \(d\) is constant there, determined by the presence or absence of the opposite arm group. Thus there are at most \(1+2+2=5\) types. Otherwise every realized vector has \(d=1\), so there are at most the eight possibilities indexed by \((a,b,c)\in\{0,1\}^3\). Consequently \(t(X)\le8\), with equality precisely when all eight \((a,b,c,1)\) occur.

**Step 4: sharp twelve-point threshold.** Realizing all eight patterns requires four occupied cells with \(a=0\), each containing at least one element, and four distinct occupied cells with \(a=1\), each containing at least two. Thus \(|X|\ge4+2\cdot4=12\). Equality forces *exactly* eight occupied cells, one of each \((a,b,c,1)\), with weights \(1\) when \(a=0\) and \(2\) when \(a=1\).

For an explicit twelve-element witness, take \(X=\{1,\ldots,12\}\), with the two partitions

\[
\begin{aligned}
X/E&=\{\{1\},\{2\},\{3,4\},\{5,6\},\{7,8\},\{9,10,11,12\}\},\\
X/F&=\{\{1,3,4,5,9,10\},\{2\},\{6\},\{7,8\},\{11,12\}\}.
\end{aligned}
\]

Representatives for the eight vectors \((a,b,c,d)\) are respectively \(2,1,6,5,7,3,11,9\), in lexicographic vector order
\[
(0001),(0011),(0101),(0111),(1001),(1011),(1101),(1111).
\]
Adding any number of new elements, each a singleton in a new \(E\)-class and a new \(F\)-class, preserves all eight patterns. Thus equality is attainable at every cardinality at least twelve.

**Step 5: exactly twelve minimal isomorphism types.** In a twelve-element extremizer, label the eight support edges by their unique triples \((a,b,c)\). The two edges with \((b,c)=(0,0)\), one of weight one and one of weight two, are isolated single-edge components of the support graph. They ensure \(d=1\) for every edge. The other six edges are: two core edges with \((b,c)=(1,1)\), of weights one and two; two left-star leaves with \((b,c)=(1,0)\), of weights one and two; and two right-star leaves with \((b,c)=(0,1)\), of weights one and two.

The two core edges are distinct and either (i) have disjoint endpoints, (ii) share their left endpoint, or (iii) share their right endpoint. They cannot share both endpoints, as the support is a simple bipartite graph. For case (i), each of the four core endpoints needs exactly one suitable leaf, yielding two independent choices for assigning the two left-leaf weights and two choices for the right-leaf weights: four configurations. In case (ii), the two right leaves must attach one at each of the two distinct core-right endpoints (two assignments of weights). The two left leaves must either both attach at the shared core-left endpoint or together form a separate two-edge left star (two possibilities): again four. Case (iii) is the left/right mirror and also gives four. No other incidence is possible: a left-star leaf has a degree-one right endpoint, a right-star leaf has a degree-one left endpoint, and all degree-at-least-two endpoints must be supplied as described.

Every listed configuration satisfies all eight profiles, because the two isolated support edges guarantee \(d=1\) and the other endpoint degrees give their required \(b,c\). The configurations are pairwise nonisomorphic under named-side-preserving isomorphism: the unique triple \((a,b,c)\) labels each occupied cell invariantly; hence its left- and right-endpoint equality patterns reconstruct the graph. The three core incidences differ, and the four remaining choices in each case differ in their weighted edge endpoint equality patterns. The total is \(4+4+4=12\).

**Step 6: rank-two corollary.** Every rank-two sentence is a Boolean combination of formulas obtained by quantifying one variable over a pointed rank-one formula; any smaller-rank sentence is covered as well. Existence or nonexistence of each pointed type therefore determines the rank-two sentence theory. The extremizers all realize the same eight types, proving the corollary.

## Verification
The self-contained program `verify_templates.py` generates exactly the twelve support templates from Step 5, verifies all required edge weights and the eight realized profiles, checks distinctness using canonical cell-endpoint equality matrices, and replays the explicit twelve-element witness. Its output is recorded in `verification_output.txt`.

A separately implemented program `verify_exhaustive.cpp` checks all pairs of partitions through twelve elements. For each possible block-size pattern it fixes one canonical \(E\)-partition and enumerates every \(F\)-partition in restricted-growth encoding, covering every pair up to relabelling (with possible repetitions). At size twelve it examines \(324{,}446{,}969\) such representatives and finds \(2{,}448\) instances with all eight types. These are **not** claimed as distinct isomorphism types; the analytical classification in Step 5 gives twelve. The finite computation checks the sharp threshold but is not used to prove the all-size bound.

Reproduce with `python3 verify_templates.py` and `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive` from the extracted file directory.

## Relationship to prior work
Kieroński and Otto (LICS 2005; journal version 2012) investigate two-variable logic with equivalence relations, including model and substructure properties. Pratt-Hartmann (2015) investigates two-variable counting logic with equivalences, develops local configurations and proves undecidability with two equivalence predicates. These broader decidability and model-construction results motivate a sharp *local type-diversity* question but do not state the present universal eight-type bound, the twelve-point threshold, or the twelve-template classification in the material inspected. The present result is not a decidability or complexity improvement, nor a statement about arbitrary counting quantifiers.

The exact extremal question differs from classification of \(C^2\)-equivalence among small structures with two named equivalences: that logic records numerical neighbourhood data, whereas here one asks how many **ordinary rank-one pointed** types can coexist *inside one structure*. It also differs from the analogous extremal problem for two total orders, whose incidence constraints are incompatible with arbitrary equivalence intersections.

## Limitations
The theorem is only about a purely two-equivalence signature and rank-one pointed types, with the stated rank-two sentence corollary. It does not classify every rank-two theory, every smallest model of every theory, or structures with unary colours or more equivalences. The minimal twelve-isomorphism-type classification is proved by the support template analysis, with independent finite code as a check. Previously unindexed specialized treatments of the local extremal problem remain a priority risk.

## References
1. E. Kieroński and M. Otto, *Small Substructures and Decidability Issues for First-Order Logic with Two Variables*, LICS 2005, pp. 448–457; journal version, *Journal of Symbolic Logic* 77 (2012), 729–765. DOI: 10.1109/LICS.2005.49; DOI: 10.2178/jsl/1344862160.
2. I. Pratt-Hartmann, *The Two-Variable Fragment with Counting and Equivalence*, *Mathematical Logic Quarterly* 61 (2015), 474–515. DOI: 10.1002/malq.201400102. First published online November 25, 2015.
