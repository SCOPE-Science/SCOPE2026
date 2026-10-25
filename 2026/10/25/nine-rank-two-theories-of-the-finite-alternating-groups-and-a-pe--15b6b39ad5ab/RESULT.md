# Nine rank-two theories of the finite alternating groups and a persistent parity oscillation

## Finding
Let \(A_n\) be the alternating group on \(n\) letters, \(n\ge3\). In the one-sorted first-order language consisting of equality, a named identity \(e\), and a ternary **relational** multiplication symbol \(R(x,y,z)\), interpreted as \(xy=z\), the complete classification at quantifier rank two is:

\[
A_m\equiv_2 A_n \iff
\begin{cases}
 m=n\in\{3,4,5,6,8,10\},&\text{or}\\
 \{m,n\}\subseteq\{7,9\},&\text{or}\\
 m,n\ge11\text{ and }[m\bmod8\in\{4,5\}]\Leftrightarrow[n\bmod8\in\{4,5\}].
\end{cases}
\]

Consequently the family has exactly **nine** rank-two theories, with smallest group-degree representatives \(3,4,5,6,7,8,10,11,12\). Unlike the symmetric-group family, the alternating-group theories do **not** eventually stabilize: two distinct classes recur infinitely often. The sharp largest size of a representative **within the alternating-group family** is \(|A_{12}|=12!/2=239500800\).

More specifically, the rank-two sentence
\[
\exists x\bigl(x\ne e\land R(x,x,e)\land\forall y\,\neg R(y,y,x)\bigr)
\]
is true in \(A_n\) precisely when \(n\ge4\) and \(n\equiv4\) or \(5\pmod8\). It states that there is an involution having no square root **inside** \(A_n\).

## Assumptions and scope
Quantifier rank is nesting depth; distinct top-level quantifiers joined by a Boolean connective do not add their ranks. The symbol \(R\) is **not** a function, and expressions such as an iterated product are not atomic. The equivalence \(\equiv_2\) refers to *all* closed formulas of quantifier rank at most two, with arbitrarily many Boolean connectives, no counting quantifiers, and only the specified language. The classification ranges over every integer \(n\ge3\), including groups with exceptional low degrees.

## Proof
**1. Complete two-round atomic reduction.** Once one element \(x\) has been chosen, all atomic formulas on the two chosen elements \(x,y\) and the named element \(e\) are determined by equalities among \(e,x,y\) and the equalities expressing \(x^2\), \(y^2\), \(xy\), and \(yx\) as one of \(e,x,y\). Associativity and cancellation imply that when neither of \(x,y\) is the identity, \(xy=e\) (equivalently \(yx=e\)) holds precisely for \(y=x^{-1}\), whereas \(xy=x\), \(yx=x\), \(xy=y\), and \(yx=y\) cannot hold unless an element is the identity. Also \(x^2=y\) forces \(y\) to be the single specified element \(x^2\); \(y^2=e\) specifies identity or an involution; and \(y^2=x\) specifies a square root of \(x\). An idempotent is necessarily \(e\).

For \(n\ge4\), the complete set of two-variable atomic diagrams extending a given \(x\) is therefore determined by one of the following nine categories:

* \(E\): \(x=e\).
* \(I_+\), \(I_-\): \(x\) has order \(2\), and does, respectively does not, have a square root in \(A_n\).
* \(T_+\), \(T_-\): \(x\) has order \(3\), and does, respectively does not, have a square root different from its already existing root \(x^{-1}=x^2\).
* \(Q_+\), \(Q_-\): \(x\) has order \(4\), and does, respectively does not, have a square root in \(A_n\).
* \(H_+\), \(H_-\): \(x\) has order at least \(5\), and does, respectively does not, have a square root in \(A_n\).

These categories are pairwise distinguishable by their two-variable atomic-extension sets. To establish sufficiency constructively, the only special possible second choices are \(y=e\), \(y=x\), \(y=x^{-1}\), and \(y=x^2\); if these overlap, the overlap is already fixed by whether \(x\) has order \(1,2,3,4\) or at least \(5\). Beyond them, a second element \(y\) can contribute only the relation \(y^2=e\) (an involution), the relation \(y^2=x\) (a root), or neither (a generic element). For nonidentity \(x\), a root can equal a special element only when \(x\) has order three, in which case \(x^{-1}=x^2\) is the canonical root. Each \(A_n\) for \(n\ge4\) has at least three involutions, so an involution outside the special set exists whenever needed: if \(x\) has order four, \(x^2\) is at most one of them; otherwise at most \(x\) is an involution. Also every \(A_n\) for \(n\ge4\) has at least eight distinct \(3\)-cycles; one outside \(e,x,x^{-1},x^2\) is a generic element, since the square of a \(3\)-cycle cannot equal \(x\) unless \(x\) itself has order three and the root is exactly \(x^{-1}\). Thus **every** allowed atomic diagram is realized whenever its defining square-root condition holds, without any large-degree assumption. The order categories themselves are detected by the atomic relations: \(x=e\), \(x^2=e\), whether some \(y\) has simultaneously \(x^2=y\) and \(xy=e\) (order three), or whether some \(y\) has simultaneously \(x^2=y\) and \(y^2=e\) (order four). The existence of the indicated special or additional root determines the sign. Hence two alternating groups of degree at least four agree at rank two exactly when they realize the same categories. In \(A_3\), there are no nonidentity involutions; its two pointed types are computed directly.

For clarity: a group of order \(3\) lacks an involution, whereas \(A_4\) and larger alternating groups have one. This does not presume that the generic-choice argument holds at \(A_3\).

**2. Even-permutation square-root criterion.** Suppose a permutation \(x\in A_n\) has \(c_j\) cycles of length \(j\), counting fixed points. There exists \(y\in A_n\) with \(y^2=x\) if and only if (i) \(c_j\) is even for every even \(j\), and (ii)
\[
\sum_{j\text{ even}}\frac{c_j}{2}\equiv0\pmod2
\quad\text{or}\quad
c_j\ge2\text{ for some odd }j.
\]
Indeed every two cycles of the same even length must be glued into one root cycle of doubled length, an odd permutation. Each odd-length cycle has its unique odd-length individual square root (an even permutation). One may alternatively glue two equal odd-length cycles into an even-length root cycle, changing root parity. Hence the forced parity of the even-length pairings may be corrected exactly when two equal odd cycles are available. This also proves the converse, because squaring a root cycle yields either one odd cycle or two cycles of the same length.

**3. Occurrence of each category.** The identity category \(E\) occurs always. A nontrivial involution in \(A_n\) is a product of \(2t\) transpositions with \(t\ge1\), leaving \(f=n-4t\) fixed points. The criterion in step 2 shows that it has no alternating square root precisely when \(t\) is odd and \(f\le1\); such an involution exists exactly for \(n\ge4\) with \(n\equiv4,5\pmod8\). An involution *with* a root exists whenever \(n\ge6\), witnessed by \((12)(34)\) with two spare fixed points and root \((1324)(56)\).

An element of order three is composed of \(k\ge1\) disjoint \(3\)-cycles and \(f=n-3k\) fixed points. Its canonical root \(x^{-1}\) is always alternating. A second alternating root exists precisely when at least two odd-cycle pairings can be made, i.e.
\[
\left\lfloor\frac{k}{2}\right\rfloor+\left\lfloor\frac{f}{2}\right\rfloor\ge2.
\]
It follows that \(T_+\) occurs exactly when \(n\ge7\), while \(T_-\) occurs exactly for \(n\in\{3,4,5,6,7,9,10\}\). (If the displayed sum is below two, then \(k\le3\); examining \(k=1,2,3\) gives exactly those degrees.)

The element \((1234)(56)\) gives \(Q_-\) for every \(n\ge6\), since its two even-length cycles cannot separately be paired. The category \(Q_+\) appears precisely when \(n\ge10\): a square root of order-four \(x\) must have order eight, and the least support of an **even** permutation of order eight is ten (an eight-cycle together with a transposition). Conversely \((12345678)(9\,10)\) is even, and its square has order four.

The category \(H_+\) appears for \(n\ge5\), witnessed by a five-cycle. At degree \(n=7\), the element \((123)(45)(67)\) is even and has no alternating square root; for every \(n\ge8\), the element \((123456)(78)\) is even and has no square root even in the full symmetric group because its unique even-length cycles have distinct lengths. Thus \(H_-\) occurs for every \(n\ge7\); no element of order at least five without an alternating square root exists in \(A_n\) for \(n\le6\). These arguments give the complete occurrence table:

| Category | Precisely the degrees where it occurs |
| --- | --- |
| \(E\) | \(n\ge3\) |
| \(I_-\) | \(n\ge4\), \(n\bmod8\in\{4,5\}\) |
| \(I_+\) | \(n\ge6\) |
| \(T_-\) | \(n\in\{3,4,5,6,7,9,10\}\) |
| \(T_+\) | \(n\ge7\) |
| \(Q_-\) | \(n\ge6\) |
| \(Q_+\) | \(n\ge10\) |
| \(H_+\) | \(n\ge5\) |
| \(H_-\) | \(n\ge7\) |

**4. Class count and sharpness.** Comparing category sets shows that the only coincidence among \(n\le10\) is \(n=7\) versus \(n=9\). Starting at \(n=11\), every category except \(I_-\) occurs uniformly, and that remaining category occurs exactly in the two residue classes stated above. There are therefore nine distinct theories, and their least degree representatives are precisely \(3,4,5,6,7,8,10,11,12\). The last class is first attained at degree 12; since \(|A_n|=n!/2\) increases strictly for \(n\ge3\), the sharp largest least-representative order is \(|A_{12}|=239500800\). Finally the displayed rank-two formula expresses the presence of \(I_-\) and proves the infinite oscillation.

## Verification
Run `python3 check_alt.py`. The standalone program (i) computes permutation cycle partitions and the exact category sets for every degree \(3\le n\le40\); (ii) independently constructs *every even permutation* in degrees \(3\) through \(9\), checks the parity-sensitive square-root criterion against the actual squares, and enumerates the full ternary-multiplication atomic diagrams of each pair; (iii) checks that these concrete atomic profiles agree with category predictions. It confirms nine symbolic category sets and the independent low-degree logical-type signatures. The infinite degrees are proved by steps 1–4, **not** by extrapolation from the finite tests.

## Relationship to prior work
Gomaa's dissertation (2007) formulates bounded-round Ehrenfeucht–Fraïssé equivalence in the *same relational group language* and studies cyclic, abelian and dihedral groups; its examined sections do not classify the alternating family. Macpherson (2016) discusses model theory and ultraproducts of finite simple/alternating groups, not the exact rank-two theories of \(A_n\). Grochow–Levet (2022) use substantially stronger group-isomorphism logics with generalized quantifiers and more pebbles; their results do not entail this fixed rank-two equivalence in the plain relational language. Larsen–Tiep (2023) study products of conjugacy classes in alternating groups, rather than the elementwise square-map predicate controlling the rank-two oscillation. The present exact nine-class classification and mod-eight persistence were not located in the examined results. Structural square-root facts are classical; novelty is asserted only for their complete bounded-rank logical consequence.

## Limitations
This statement uses precisely the *ternary relational* multiplication language. It is **not** a classification for first-order logic with multiplication as a binary function, for logics with counting/group quantifiers, or for higher quantifier ranks. The maximum representative size is optimal only among the alternating-group family, not among all finite structures. Direct computational verification ends at degree nine; higher degrees use the written mathematical argument. A prior equivalent formulation could exist in unindexed or inaccessible literature. This is a self-review; independent mathematical validation has not been performed.

## References
1. Walid Gomaa, *Model Theory and Complexity Theory* (doctoral dissertation, University of Maryland, 2007), public repository record dated 2007-07-06. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. Dugald Macpherson, *Model theory of finite and pseudofinite groups* (2016), arXiv:1607.06714. https://arxiv.org/abs/1607.06714
3. Joshua A. Grochow and Michael Levet, *On the Descriptive Complexity of Groups without Abelian Normal Subgroups* (2022), arXiv:2209.13725. https://arxiv.org/abs/2209.13725
4. Michael Larsen and Pham Huu Tiep, *Squares of Conjugacy Classes in Alternating Groups* (2023), arXiv:2305.04806. https://arxiv.org/abs/2305.04806
