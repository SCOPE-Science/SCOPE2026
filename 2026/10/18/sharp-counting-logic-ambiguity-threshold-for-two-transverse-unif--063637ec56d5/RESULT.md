# Sharp counting-logic ambiguity threshold for two transverse uniform equivalences

## Finding
Fix an integer \(k\ge3\). Let \(\mathcal T_k\) be the class of finite nonempty structures \((X,E,F)\) in the vocabulary of **two named binary relations**, subject to:

1. \(E\) and \(F\) are equivalence relations.
2. Every \(E\)-class and every \(F\)-class contains exactly \(k\) elements.
3. Every intersection of one \(E\)-class with one \(F\)-class has size at most one.

Write \(C^2\) for first-order logic using only two variable symbols (reused under quantifiers), with equality and arbitrary finite counting quantifiers. Let \(p(t)\) denote the number of integer partitions of \(t\), with \(p(0)=1\).

**Theorem.** For each \(k\ge3\):

(a) For a fixed cardinality, any two members of \(\mathcal T_k\) satisfy the same \(C^2\) sentences. The possible nonzero cardinalities are exactly \(kr\) for integers \(r\ge k\).

(b) At cardinalities \(k^2\) and \(k(k+1)\), the class \(\mathcal T_k\) has exactly one isomorphism type at each cardinality. The first two distinct isomorphism types that cannot be distinguished by \(C^2\) occur at the **sharp cardinality**
\[
 n_{\min}(k)=k(k+2).
\]

(c) At cardinality \(k(k+2)\) the number of isomorphism types is exactly
\[
 a_k=p(k+2)-p(k+1)=\#\{\lambda\vdash k+2:\text{every part of }\lambda\text{ is at least }2\}.
\]
They all belong to the same \(C^2\) class, and all have connected class-incidence graphs. For \(k=3,4,5,6\), respectively, the cardinality thresholds are \(15,24,35,48\), with numbers of types \(2,4,4,7\).

## Assumptions and scope
The names \(E,F\) matter: isomorphisms must preserve each relation, rather than interchanging them. All relations are reflexive, symmetric and transitive; the \(E\)- and \(F\)-classes can be regarded as the two *distinguished* sides of a bipartite incidence graph. Every common intersection has **zero or one** element, so the bipartite graph is simple. Empty structures are excluded. The signature has no further predicates, constants, or designated elements. The logical equivalence is *within* \(\mathcal T_k\); a larger class could have additional structures with the same \(C^2\) theory.

## Proof
**Step 1: Exact incidence correspondence.** Form a bipartite graph whose left vertices are the \(E\)-classes and whose right vertices are the \(F\)-classes. Connect a left and a right vertex if their classes meet. The intersection constraint makes this a simple graph; its edges are in bijection with elements of \(X\). Every graph vertex has degree \(k\), since every equivalence class has size \(k\). Consequently the numbers of left and right vertices are equal to a common integer \(r=|X|/k\), with \(r\ge k\). Conversely, every simple \(k\)-regular bipartite graph with two distinguished sides of size \(r\) gives an object of \(\mathcal T_k\): take the edges as elements, and declare two edges \(E\)-equivalent when they share their left endpoint and \(F\)-equivalent when they share their right endpoint. Isomorphisms of structures are exactly side-preserving graph isomorphisms. Every \(r\ge k\) is realized, for example by a union of \(k\) cyclic perfect matchings of \(K_{r,r}\).

**Step 2: Uniform two-variable counting types.** Fix an element \(x\) of any structure with \(|X|=n=kr\). For a second element \(y\), precisely four mutually exclusive atomic configurations can occur: \(x=y\); \(x\ne y\) and \(E(x,y)\); \(x\ne y\) and \(F(x,y)\); or neither relation holds. The condition on class intersections rules out the case \(x\ne y\) with both relations true. The respective numbers of such \(y\) are exactly
\[
 1,\quad k-1,\quad k-1,\quad n-2k+1.
\]
These four counts are independent of \(x\) and of the incidence graph. We prove by structural induction that, for any \(C^2\) formula with free variables among \(x,y\), its truth under an assignment is determined by the atomic configuration of the assigned pair and the common integers \(n,k\). Atomic formulas obey this immediately. Boolean connectives preserve it. If \(\varphi(x,y)\) satisfies the induction hypothesis, then for a fixed value of \(x\), the number of values of \(y\) satisfying \(\varphi\) is the sum of a fixed subset of the four displayed numbers. Thus each counting quantifier binding \(y\) has truth independent of \(x\) and of the chosen incidence graph; similarly for a counting quantifier binding \(x\). In the case of a formula with just one free variable, interpret an unused second variable arbitrarily: the induction assertion still applies. Hence every \(C^2\) sentence has the same truth value in any two members with the same \(n,k\).

**Step 3: Uniqueness for the first two sizes.** At \(r=k\), every row and column of the \(r\)-by-\(r\) incidence matrix has \(k=r\) ones, so the graph is \(K_{r,r}\). At \(r=k+1\), each row and column has a unique zero; the complement in \(K_{r,r}\) is a perfect matching. All perfect matchings are related by side-preserving permutations. Thus there is exactly one type at both sizes, and no smaller nonzero size is possible.

**Step 4: Classification at the next size.** At \(r=k+2\), every row and column of the complement in \(K_{r,r}\) has exactly two ones. This complementary graph is a simple \(2\)-regular bipartite graph: a disjoint union of cycles of lengths \(2\ell\), where \(\ell\ge2\), with exactly \(\ell\) vertices from each side on each cycle. Hence its complete side-preserving isomorphism invariant is the multiset of half-cycle lengths, equivalently an integer partition \(\lambda\vdash r\) with every part at least two. Conversely any such partition determines the complementary graph, hence determines a valid member of \(\mathcal T_k\). Nonidentical partitions give nonisomorphic structures, as isomorphisms preserve the complement and its cycle-component sizes.

The number of partitions of \(r\) with no part one equals \(p(r)-p(r-1)\): deleting one occurrence of a part one bijects partitions of \(r\) containing one with *all* partitions of \(r-1\). For every \(r=k+2\ge5\), there are at least two different partitions with no part one, namely \((r)\) and \((r-2,2)\). Combined with Steps 2 and 3, this proves both the sharp threshold and the exact number of nonisomorphic structures sharing the counting theory.

**Step 5: Connectivity of the incidence graph.** For \(r=k+2\) and \(k\ge3\), \(k>r/2\). If a \(k\)-regular bipartite graph were disconnected, each component would contain at least \(k\) vertices on each side; two distinct components would demand at least \(2k>r\) vertices on either side. Thus each graph under consideration is connected.

**Explicit first witnesses.** For \(k=3\) take \(r=5\). Label both vertex sides by \(0,1,2,3,4\), and for a permutation \(\sigma\) without fixed points join left \(i\) to right \(j\) exactly when \(j\notin\{i,\sigma(i)\}\). Two choices are \(\sigma=(0\ 1\ 2\ 3\ 4)\) and \(\sigma=(0\ 1\ 2)(3\ 4)\). Their complements are respectively a single ten-cycle and a disjoint union of a six-cycle and a four-cycle, so the corresponding 15-element two-equivalence structures are not isomorphic; Step 2 proves they are \(C^2\)-equivalent.

## Verification
The included Python 3 script `verify_uniform_pairs.py` uses standard-library functions only. It enumerates derangements through eight left-side vertices and recovers the exact cycle-partition classification for \(k=2,\ldots,6\); explicitly constructs every corresponding incidence graph, checks both \(k\)-regularity and cardinality, tests connectivity for \(k\ge3\), and directly computes the four possible pair-type counts. An independent exhaustive row-by-row enumeration of all labeled \(k\)-regular incidence matrices for \((k,r)=(2,2),(2,3),(2,4),(3,3),(3,4),(3,5)\) checks the claimed isomorphism-type numbers. Reproduce with `python3 verify_uniform_pairs.py`; compare to `verification_output.txt`, ending in `VERIFICATION_OK`. All proofs for unrestricted \(k\) and \(r\) are given above; finite checks alone would not establish them.

## Relationship to prior work
J. P. James (2006) treats the same incidence correspondence between pairs of uniform partitions and regular bipartite graphs, with a different principal aim: existence of graphs with trivial side-preserving automorphism group. Its accessible abstract states a sharp asymmetric-graph threshold at \(r\ge\max\{k+3,8\}\), not the counting-logic identification threshold and the exact size of its first fibre. The full article was not accessible for a decisive appendix-level exclusion, leaving residual coverage risk.

I. Pratt-Hartmann (2015) studies the satisfiability and expressive behaviour of two-variable counting logic with equivalence relations. The inspected full text develops logical complexity and local configurations, not the sharp minimum-size two-partition collision or the partition-number spectrum here. General facts about regular bipartite graphs and partitions of an integer are used as ingredients rather than claimed as new.

## Limitations
This result is a **relative** \(C^2\) identification boundary for the stated transverse, equal-class-size family. It does not determine all collisions at larger sizes, and it says nothing about arbitrary nonuniform or nontransverse equivalence structures. Logical equivalence is proved directly without classifying automorphisms of every incidence graph. The accessible abstract rather than full body of James (2006) was inspected; possible specialized coverage there remains a publication-priority risk.

## References
1. J. P. James, *Partition Actions of Symmetric Groups and Regular Bipartite Graphs*, Bulletin of the London Mathematical Society **38** (2006), 224–232. DOI: 10.1112/S0024609306018285. First available public online date verified as 2006-03-16.
2. I. Pratt-Hartmann, *The Two-Variable Fragment with Counting and Equivalence*, Mathematical Logic Quarterly **61** (2015), 474–515. DOI: 10.1002/malq.201400102.
