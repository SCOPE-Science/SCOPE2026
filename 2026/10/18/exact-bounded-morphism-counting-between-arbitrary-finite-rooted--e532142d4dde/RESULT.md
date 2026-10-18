# Exact bounded-morphism counting between arbitrary finite rooted tree frames

## Finding

For every pair of finite nonempty rooted trees \(T,U\), equip the vertices with the **reflexive descendant** accessibility relation. The number \(N(T,U)\) of surjective bounded morphisms (\(p\)-morphisms) \(T\to U\) is given by a finite, explicit subtree inclusion–exclusion recurrence. If \(n=|V(T)|\), \(m=|V(U)|\), and \(\Delta\) is the maximum number of children of a target vertex, it can be evaluated with \(O(nm\max\{1,\Delta\}2^\Delta)\) integer arithmetic operations and \(O(nm+2^\Delta)\) working integer cells. In particular **exact bounded-morphism counting is fixed-parameter tractable in target branching** (with respect to arithmetic-operation complexity), without a height bound or planarity/order on either tree.

The recurrence distinguishes *the number of maps* from the mere existence of a map. It counts functions between the actual vertex sets, not isomorphism classes of functions. No input or output vertex labels or valuations are assumed beyond the distinguished roots.

Write \(C_T(s)\) and \(C_U(t)\) for child sets, and \(T_s,U_t\) for the corresponding inclusive rooted descendant subtrees. Define \(F_s(t)\) as the number of maps \(f:T_s\to U_t\) that send \(s\) to \(t\) and satisfy the bounded-morphism equation at every source vertex. Put
\[
 A_c(t)=\sum_{u\in U_t}F_c(u),\qquad
 B_c(t,J)=\begin{cases}
 A_c(t),&J=\varnothing,\\
 A_c(t)-F_c(t)-\sum_{v\in J}F_c(v),&\varnothing\ne J\subseteq C_U(t).
 \end{cases}
\]
Then the *exact* recurrence is
\[
 \boxed{F_s(t)=\sum_{J\subseteq C_U(t)}(-1)^{|J|}
        \prod_{c\in C_T(s)}B_c(t,J),\qquad N(T,U)=F_{r_T}(r_U).}
\]
The empty product is \(1\). This single formula handles all leaves and arbitrary branching; no separate base cases are imposed.

## Assumptions and scope

All trees are finite, nonempty, rooted, unordered, and simple as underlying graphs. The accessibility relations are \(xR_Ty\iff y\in T_x\) and \(uR_Uv\iff v\in U_u\), including reflexive pairs. A map is a bounded morphism precisely when
\[
 f(T_x)=U_{f(x)}\quad\text{for every source vertex }x.
\]
This is the ordinary forth/back condition for one accessibility relation, not the stronger notion of a bounded morphism simultaneously preserving inverse accessibility. A *surjective* bounded morphism necessarily sends the source root to the target root. Conversely, any bounded morphism that sends root to root is surjective, because the image of the source root's cone is the entire target cone.

The recursion uses the concrete child sets and target descendant sets. Thus if two target vertices are isomorphic or two branches of the source are isomorphic they nevertheless remain distinct possible function values or source argument positions. The count is a nonnegative integer despite the alternating formula.

## Proof

**Local decomposition.** Fix source and target vertices \(s,t\) and a map with \(f(s)=t\). For each source child \(c\in C_T(s)\), the bounded-morphism condition restricted to the cone \(T_c\) implies \(f(T_c)=U_{f(c)}\). Forth preservation gives \(f(c)\in U_t\). Conversely, assigning independently to every child \(c\) one target vertex \(u\in U_t\) and one of the \(F_c(u)\) bounded maps \(T_c\to U_u\), then setting \(f(s)=t\), produces a map satisfying the condition at all proper descendants of \(s\). Its image on \(T_s\) is
\[
 \{t\}\cup\bigcup_{c\in C_T(s)}U_{f(c)}.
\]
This equals \(U_t\) exactly when it contains every *immediate child* \(v\in C_U(t)\); all descendants of \(v\) then occur automatically if \(v\) is contained in one of the images \(U_{f(c)}\).

**Coverage lemma.** For any immediate target child \(v\) and source child \(c\), \(v\in U_{f(c)}\) holds precisely when \(f(c)=t\) or \(f(c)=v\). Indeed \(f(c)\) is a descendant of \(t\), while \(v\) covers \(t\); the only target ancestors of \(v\) within \(U_t\) are \(t,v\). In particular, an assignment misses all vertices of a nonempty set \(J\subseteq C_U(t)\) if and only if each source child \(c\) chooses an image root in \(U_t\setminus(\{t\}\cup J)\). There are exactly
\[
 \sum_{u\in U_t\setminus(\{t\}\cup J)}F_c(u)
 =A_c(t)-F_c(t)-\sum_{v\in J}F_c(v)=B_c(t,J)
\]
ways for that child's subtree. For the empty forbidden set there is no restriction, giving \(B_c(t,\varnothing)=A_c(t)\).

**Inclusion–exclusion and induction.** The product over source children of \(B_c(t,J)\) counts assignments missing all target children in \(J\). Inclusion–exclusion over \(C_U(t)\) counts precisely those covering every target child, proving the boxed recurrence. Induction from leaves to the source root defines every \(F_s(t)\), because each term uses only states \(F_c(u)\) with strictly smaller source cone \(T_c\). For a source leaf and nonleaf target the alternating sum is \((1-1)^{|C_U(t)|}=0\); for a leaf target it is \(1\), so the formula also establishes the correct initial states. The root observation proves \(N(T,U)=F_{r_T}(r_U)\).

**Arithmetic complexity.** Process source vertices bottom-up. For every computed source state \(c\), the values \(A_c(t)\) for all target vertices are subtree sums and can be computed bottom-up in \(O(m)\) arithmetic operations. At each \((s,t)\), enumerate subsets of \(C_U(t)\), and use subset sums of \(F_c(v)\) for individual source children \(c\). A direct implementation costs at most \(O(|C_T(s)|\max\{1,|C_U(t)|\}2^{|C_U(t)|})\) operations for that pair. Summing over states and using \(\sum_s|C_T(s)|=n-1\) yields the claimed \(O(nm\max\{1,\Delta\}2^\Delta)\) bound. Streaming the subsets keeps working memory \(O(nm+2^\Delta)\). As counts may be exponentially large, these bounds count arbitrary-precision integer arithmetic operations; bit complexity also depends on output length.

**Two exact specializations.** If \(T\) and \(U\) are stars with respectively \(a\) and \(b\) leaves and \(b\ge1\), every source leaf must map to a target leaf, and all target leaves must be hit. Thus
\[
 N(T,U)=\sum_{j=0}^{b}(-1)^j\binom bj(b-j)^a=b!\,S(a,b).
\]
Here \(S(a,b)\) is a Stirling number of the second kind, and the formula also gives \(0\) when \(a<b\). When \(U\) is the two-point rooted chain and \(T\) is a full binary tree of height \(h\), the counts satisfy \(q_0=0\), \(q_{h+1}=(q_h+1)^2\). Therefore the successive counts for heights \(0,1,2,3,4\) are \(0,1,4,25,676\). This illustrates that *enumeration* retains multiplicity information invisible to the existence predicate.

**Equal-size boundary.** If \(|T|=|U|\), every surjective bounded morphism is bijective. The cone equality then makes it an order isomorphism, and therefore a rooted tree isomorphism. Consequently \(N(T,U)=0\) for nonisomorphic equal-order trees and \(N(T,T)=|\operatorname{Aut}(T)|\).

## Verification

The standalone standard-library program `count_pmorphisms_dp.py` implements both the inclusion–exclusion recurrence and an independent **positive-coverage-state** recurrence that explicitly accumulates which immediate target children are covered. They agree on all \(28{,}016\) pairs of nonisomorphic rooted tree shapes with source order at most eight and target order no greater than source order (rooted-tree counts \(1,1,2,4,9,20,48,115\)). It also checks \(100\) star-pair identities against the classical onto-function formula.

`verify_pmorphisms_bruteforce.py` independently inspects the forward/back equation for **all** \(22{,}132{,}644\) set-functions across \(936\) rooted shape pairs with source order at most six and target order no greater than the source order; root preservation and surjectivity are checked separately. Every result equals the recurrence.

`verify_rooted_automorphisms.py` independently counts actual root-preserving graph isomorphisms by bijection enumeration for \(2{,}807\) pairs of rooted tree types of equal order at most seven. All counts equal the recurrence. These finite tests are reproducibility checks, not substitutes for the universal induction above.

Run using Python 3.10 or later from a directory containing the three files:

```sh
python count_pmorphisms_dp.py
python verify_pmorphisms_bruteforce.py
python verify_rooted_automorphisms.py
```

## Relationship to prior work

Bounded morphisms are a classical truth-preserving construction in modal model theory. Endriss (2003, §§3.5–3.6) studies bounded morphisms for ordered-tree modal frames; his tree-image lemma concerns surjective *bidirectional* morphisms with an immediate-successor relation. Goranko–Otto (2006, §2.2) give the standard forth/back semantics and preservation theorems. Neither inspected treatment provides an exact count of bounded morphisms for the single reflexive-descendant relation between arbitrary finite rooted trees.

Bodirsky–Piguet (arXiv:1002.1557v1, 2010) concern a Ramsey theorem for *plane binary* rooted trees with leaf-preserving topological embeddings, not enumeration of modal frame morphisms. A separate topological-minor criterion decides whether at least one map exists, but a yes/no test does not supply the number of vertex-set maps. The present contribution is the explicit all-shapes multiplicity formula and its target-branching complexity guarantee, not a new proof of the classical semantics or of topological-minor well-quasi-ordering.

## Limitations

No claim is made for infinite trees, multiple accessibility relations, valuations not constant on fibers, general directed acyclic graphs, or the irreflexive immediate-successor relation. The parameterized complexity statement is for the number of arithmetic operations and explicitly allows an exponential dependence on target maximum branching. No polynomial-time counting result for unrestricted target branching or complexity lower bound is asserted. Independent scientific audit and publication-priority certification have not been performed; specialized earlier enumerative literature may exist outside the inspected sources.

## References

1. U. Endriss, *Modal Logics of Ordered Trees* (revised thesis, March 2003), §§3.5–3.6, particularly Definition 3.20 and Lemma 3.32. https://staff.science.uva.nl/u.endriss/pubs/files/otl.pdf
2. V. Goranko and M. Otto, *Model Theory of Modal Logic* (2006), §2.2, Definition 15 and Corollary 16. https://www.mathematik.tu-darmstadt.de/~otto/papers/Chapter5_02_05_06.pdf
3. M. Bodirsky and D. Piguet, *Finite trees are Ramsey under topological embeddings*, arXiv:1002.1557v1 (first posted 2010-02-08). https://arxiv.org/abs/1002.1557
