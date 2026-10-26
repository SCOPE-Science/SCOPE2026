# Five two-round theories of finite hyperoctahedral groups

## Finding
For every integer \(n\ge 1\), let \(B_n=(C_2)^n\rtimes S_n\) denote the group of signed permutations of \(n\) coordinates. Work in the first-order relational language \(\{e,R\}\), with a named identity \(e\) and ternary multiplication relation \(R(a,b,c)\) meaning \(ab=c\). Write \(G\equiv_2 H\) when the structures agree on all first-order sentences of quantifier rank at most two, allowing Boolean combinations and both quantifier kinds.

**Theorem.** For all \(m,n\ge1\),
\[
B_m\equiv_2 B_n\quad\Longleftrightarrow\quad\min\{m,5\}=\min\{n,5\}.
\]
There are exactly five two-round theories within this infinite family, with least-degree representatives \(B_1,B_2,B_3,B_4,B_5\). Each member is two-round equivalent to one of at most \(2^5\cdot5!=3840\) group elements, and the bound is sharp **within this family**.

More structurally, for every \(n\ge5\), the rank-one extension profile of a chosen first element \(x\in B_n\) is determined precisely by its order category \(1,2,3,4,\ge5\) and, where nonredundant, whether \(x\) is a square. Eight such profiles occur: the identity; square and nonsquare elements of order two; elements of order three; square and nonsquare elements of order four; and square and nonsquare elements of order at least five. (Every order-three element is a square.)

## Assumptions and scope
All groups are abstract finite groups endowed with **only** the named identity and ternary multiplication relation. No coordinate predicates, distinguished generators, order relation, unary inverse function, or preassigned signed-cycle decomposition is present in the logical language. The sign-cycle argument below is an external analysis of these structures. The quantifier-rank cutoff is exact for the class of signed-permutation groups; it is not an assertion about all finite groups or about unrestricted logical interpretations of sign coordinates.

A signed cycle consists of an underlying permutation cycle of length \(\ell\ge1\) and a sign \(+\) or \(-\) given by the product of its coordinate signs. Its order is \(\ell\) for sign \(+\) and \(2\ell\) for sign \(-\). Independent signed cycles commute.

## Proof
### 1. Exact atomic-extension invariant
For an arbitrary group \(G\), fix a first move \(x\). The second move chooses \(y\). The full atomic diagram on the named identity \(e\), \(x\), and \(y\) is determined by all equalities among these values and the truth of \(R(u,v,w)\) for \(u,v,w\in\{e,x,y\}\). Reduction by the group identities shows that the only variable possibilities beyond the fixed order identities of \(x\) are:

* the special cases \(y=e,x,x^{-1},x^2\), with possible coincidences controlled by \(\operatorname{ord}(x)\in\{1,2,3,4,\ge5\}\);
* a nonspecial element with \(y^2=e\);
* a nonspecial element with \(y^2=x\);
* a nonspecial element with \(y^2\notin\{e,x\}\).

Indeed, any product among \(e,x,y\) outside the evident identity products can equal an element of this same set only if \(y\) is special (or if \(y^2=e\) or \(y^2=x\)); in particular, \(xy=x\) forces \(y=e\), \(xy=y\) forces \(x=e\), \(xy=e\) forces \(y=x^{-1}\), and \(x^2=y\) forces \(y=x^2\). All four special values can be inspected directly, including coincidences at orders one, two and three.

The set \(P_G(x)\) of atomic diagrams achievable by a second choice \(y\) is a complete rank-one pointed invariant in this purely relational language. The two-round Ehrenfeucht--Fraïssé criterion states that \(G\equiv_2 H\) exactly when the collections \(\{P_G(x):x\in G\}\) and \(\{P_H(x'):x'\in H\}\) are equal. This follows by matching the first move's set of possible second-move atomic diagrams in both directions; the reverse implication is the usual two-round game strategy.

### 2. The square-root criterion for signed permutations
**Lemma.** A signed permutation is a square in \(B_n\) exactly when, for every signed cycle type \((\ell,\epsilon)\) with either \(\epsilon=-\) or even \(\ell\), the multiplicity of that exact signed type is even. Positive odd-length cycles have unrestricted multiplicity.

**Proof.** Squaring a signed cycle of odd length \(\ell\) gives one positive cycle of length \(\ell\); for any desired positive odd cycle one can invert doubling modulo \(\ell\) to obtain a positive same-length square root. Squaring a signed cycle of even length \(2\ell\) splits it into two cycles of length \(\ell\) carrying the same sign (equal to the product of all original signs). Therefore the positive cycles of even length and all negative cycles in a square occur in even numbers at each signed length. Conversely, pair those exceptional cycles of equal signed length and interlace each pair into a signed cycle of double length with the designated sign product; root each remaining positive odd cycle individually. The factors are disjoint, so their product supplies a signed-permutation square root. \(\square\)

### 3. Uniform realization of the atomic extensions for \(n\ge5\)
For any chosen \(x\in B_n\), at most three nonidentity candidates occur among \(x,x^{-1},x^2\). The \(n\) coordinate sign flips are distinct involutions, so at least two flips lie outside the special set for \(n\ge5\). Thus the nonspecial case \(y^2=e\) always occurs. There are \(2\binom n3\ge20\) unsigned positive three-cycles in \(B_n\). Their squares run bijectively through the positive three-cycles; at most three of them are special and at most one squares to \(x\). Consequently a nonspecial \(y\) with \(y^2\notin\{e,x\}\) always exists.

If \(x\ne e\) is a square and has order different from three, every square root \(y\) of \(x\) is nonspecial: \(e^2\ne x\), \(x^2=x\) would imply \(x=e\), while \((x^{-1})^2=x\) or \((x^2)^2=x\) would imply that \(x\) has order three. If \(x\) has order three, \(x^{-1}\) is a special square root, but a nonspecial one still exists: multiply \(x^{-1}\) by the central sign reversal \(-I\), which is a nontrivial involution for every \(n\ge1\). The result squares to \(x\) and lies outside the order-three cyclic subgroup.

For \(x=e\), the only pointed special case is \(y=e\), and the remaining types are nonidentity involutions and noninvolutions, both available for \(n\ge2\), hence for \(n\ge5\). Altogether the possibilities in section 1 show that, for all \(n\ge5\), \(P_{B_n}(x)\) depends **only** on the indicated order category and square-root existence; no length, multiplicity or coordinate-support detail can be detected by a second move.

All eight categories occur in \(B_5\), with additional unused coordinates fixed positively:

| Pointed category | Witness signed-cycle structure | Least degree needed |
| --- | --- | ---: |
| identity | all positive fixed cycles | 1 |
| order two, nonsquare | one negative fixed cycle | 1 |
| order two, square | two negative fixed cycles | 2 |
| order three | one positive 3-cycle | 3 |
| order four, nonsquare | one negative 2-cycle | 2 |
| order four, square | two negative 2-cycles | 4 |
| order at least five, nonsquare | one negative 3-cycle (order six) | 3 |
| order at least five, square | one positive 5-cycle | 5 |

The signed-square criterion establishes the claimed square status of each witness. The least-degree column only asserts existence in the stated degree; it does not presuppose the theorem. Every witness continues to realize the same square status under the natural embeddings obtained by adding positive fixed coordinates. Since exactly these eight categories can occur for all \(n\ge5\), their pointed-profile collections coincide. Hence all such \(B_n\) have the same rank-two theory.

### 4. Four sharp separating thresholds
To show that none of \(B_1,B_2,B_3,B_4\) belongs to the stabilized class or to each other, use the following witnesses, each a sentence of quantifier rank **at most two**. Write \(Q(x,y)\) for \(R(x,x,y)\) and \(E(y)\) for \(R(y,y,e)\) **only as explanatory abbreviations**, not extra relation symbols. Explicitly:

1. The existence of order four is expressed by
\[\exists x\exists y\,[R(x,x,y)\land y\ne e\land R(y,y,e)].\]
It first holds at degree two.
2. The existence of order three is expressed by
\[\exists x\exists y\,[x\ne e\land R(x,x,y)\land R(x,y,e)].\]
It first holds at degree three.
3. The existence of a **square element of order four** is expressed by
\[\exists x\,\bigl[(\exists y\,[R(x,x,y)\land y\ne e\land R(y,y,e)])\land(\exists z\,R(z,z,x))\bigr].\]
It first holds at degree four, through two negative 2-cycles.
4. The existence of a **square element of order at least five** is expressed by
\[\exists x\,\bigl[(\exists y\,[R(x,x,y)\land y\ne e\land\neg R(y,y,e)\land\neg R(x,y,e)])\land(\exists z\,R(z,z,x))\bigr].\]
The first conjunct forces \(\operatorname{ord}(x)\ge5\): the three restrictions exclude precisely orders two, four and three after the equation \(y=x^2\), and order one also fails. This first holds at degree five, through a positive 5-cycle.

These properties are monotone under standard embeddings and are absent from smaller degrees by the exhaustive signed-cycle lengths and square criterion above. Therefore five different rank-two theories occur, exactly as claimed. The sharp internal representative size is \(|B_5|=2^5\cdot5!=3840\). \(\square\)

## Verification
The accompanying standalone program `verify_hyperoctahedral.cpp` independently enumerates signed permutations of degrees one through six (up to 46,080 group elements), computes exact atomic second-move profiles for every signed-cycle conjugacy representative, and checks the signed-cycle square criterion against exhaustive square-root search. Compile with `g++ -O3 -std=c++17 verify_hyperoctahedral.cpp -o verify_hyperoctahedral` and run `./verify_hyperoctahedral`. Expected terminal output is provided in `verify_hyperoctahedral.out`, ending in `VERIFY_OK`. It finds pointed profile counts \(2,4,6,7,8,8\) for degrees one through six, with eight universal order-and-square categories in degrees five and six. These finite experiments corroborate but do not replace the universal reasoning in the proof.

## Relationship to prior work
Chen's FPSAC'92 paper (available in full) develops signed-cycle double partitions and induced cube-vertex/cube-edge cycle indices. That foundational algebraic object description provides a natural starting point, but its propositions concern cycle enumeration, not two-round first-order indistinguishability of the abstract groups. Gomaa's 2007 dissertation studies descriptive complexity, including quantifier-depth bounds for finite abelian groups and examples involving dihedral groups; the inspected relevant sections do not give the present signed-permutation classification. Ram's 2012 exposition describes signed permutations and Weyl type \(B\), without claiming a bounded-rank logical classification. These comparisons concern their actual statements, not merely their titles.

Related finite-group rank-two classifications in the research record concern symmetric, alternating, cyclic or dihedral groups; the signed-cycle square obstruction and exactly five classes proved here do not follow from results for those different abstract group families. Searching the indexed literature does not establish uniqueness, and an equivalent unindexed characterization remains possible.

## Limitations
The five-class statement applies only to the group family \(B_n\) in the specified ternary relational multiplication language. It is not a classification of elementary equivalence at unbounded quantifier rank. The structural argument is non-computational; brute force covers only degrees one through six. No independent audit or external formal proof certification has occurred. The earliest archival source is associated with the FPSAC'92 meeting of June 15--19; June 19 is used as a conservative documented public-by boundary, **not** as an asserted day of first manuscript release. Literature coverage is nonexhaustive.

## References
1. William Y. C. Chen, “Induced Cycle Structures of the Hyperoctahedral Group,” FPSAC'92 proceedings/poster, pp. 45--58, University of Montréal conference June 15--19, 1992. Full text: https://fpsac-archive.github.io/FPSAC92/POSTERS/Chen_proc.pdf ; meeting chronology: https://fpsac.org/confs/fpsac-1992/ .
2. Walid Gomaa, “Model Theory and Complexity Theory,” Ph.D. dissertation, University of Maryland, publicly archived July 6, 2007, especially the finite-group quantifier-depth discussion: https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 .
3. Arun Ram, “The Hyperoctahedral Group,” mathematical exposition, updated March 31, 2012: https://math.soimeme.org/~arunram/Notes/hyperoctahedral.html .
