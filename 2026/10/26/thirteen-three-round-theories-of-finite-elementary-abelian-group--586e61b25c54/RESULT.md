# Thirteen three-round theories of finite elementary abelian groups in addition-only relational language

## Finding
For every prime \(p\) and integer \(d\geq1\), let \(A_{p,d}\) have universe \(\mathbf F_p^d\) and the single nonlogical relation \(R(a,b,c)\) iff \(a+b=c\). **There is no named zero, scalar multiplication, or group-operation function symbol.** Equality is logical.

Exactly **13** equivalence classes occur among these finite structures for all first-order sentences of quantifier rank at most three. The complete classification is:

| Class | Prime \(p\) | Dimension \(d\) | Smallest representative size |
|---|---|---|---:|
| 1 | 2 | 1 | 2 |
| 2 | 2 | 2 | 4 |
| 3 | 2 | \(d\ge3\) | 8 |
| 4 | 3 | 1 | 3 |
| 5 | 3 | \(d\ge2\) | 9 |
| 6 | 5 | 1 | 5 |
| 7 | 5 | \(d\ge2\) | 25 |
| 8 | 7 | 1 | 7 |
| 9 | 7 | \(d\ge2\) | 49 |
| 10 | 11 | 1 | 11 |
| 11 | 11 | \(d\ge2\) | 121 |
| 12 | 13 | 1 | 13 |
| 13 | 13 with \(d\ge2\), or any \(p\ge17\) with \(d\ge1\) | as stated | 17 |

Different rows are inequivalent. Consequently every member has a three-round-equivalent representative with at most **121 elements**, and 121 is the least possible universal bound. The class of \(A_{11,2}\) requires a representative of at least 121 elements within this family.

## Assumptions and scope
Only finite nontrivial elementary abelian groups \(\mathbf F_p^d\), prime \(p\), positive \(d\), are included. The signature has exactly one ternary relation \(R\). The rank bound is **quantifier rank**, not number of quantifiers in a prenex normal form, variable width, counting rank, or elementary equivalence without a rank bound. The equivalence is agreement on *all* sentences of rank at most three.

## Proof
**1. Exact finite extension recurrence.** In a three-round Ehrenfeucht–Fraïssé game, a chosen ordered tuple \((a_1,\ldots,a_k)\) for \(0\le k\le3\) has an atomic diagram determined by equalities and by the vanishing of the linear forms \(e_i+e_j-e_h\) for indices from 1 to \(k\). For \(A_{p,d}\), the orbit of this tuple under \(\mathrm{GL}_d(\mathbf F_p)\) is determined exactly by the kernel \(K\subseteq\mathbf F_p^k\) of the linear map carrying \(e_i\) to \(a_i\). This kernel has codimension at most \(d\). A one-point extension has some kernel \(K'\subseteq\mathbf F_p^{k+1}\) satisfying \(K'\cap\mathbf F_p^k=K\) and \(\mathrm{codim}(K')\le d\); conversely every such \(K'\) is realized by some extension, by extending an isomorphism on the span of the first \(k\) vectors.

Define recursively the atomic type \(H_0(K)\), and \(H_{r+1}(K)\) to be its atomic type together with the **set** of all \(H_r(K')\) over permissible one-point extensions. At the empty tuple, \(H_3(\{0\})\) is precisely the rank-three theory. This is the usual characteristic-formula/EF recursion: equality of these recursively specified objects is equivalent, by induction on remaining rounds, to a Duplicator win. The procedure uses every subspace of \(\mathbf F_p^k\) for \(k\le3\); it is not a sample of individual group elements or a partial search. Since no tuple of three vectors spans more than three dimensions, all groups with \(d\ge3\) have the same rank-three theory as \(d=3\), for a fixed \(p\).

**2. Exact small-field computation.** The standalone `verify.py` enumerates every subspace of \(\mathbf F_p^k\) for \(0\le k\le3\) by its unique reduced row-echelon basis. It computes atomic diagrams directly from the defining linear forms, restriction kernels by row reduction, and the complete recurrence above. The primes \(2,3,5,7,11,13,17,19,23,29,31\) and dimensions 1, 2, 3 produce exactly the classes in the table, with the first 12 classes confined to primes at most 13 and class 13 already shared by \(A_{13,2}\) and \(A_{17,1}\). Because the enumeration exhausts all possible kernels and their extensions, it is an exact finite proof for these characteristics, not an empirical enumeration of chosen games. A separate direct implementation evaluates all three-round Hintikka types on ten actual small groups, including \(A_{2,3}\) and \(A_{3,2}\), and agrees on all 100 ordered comparisons.

**3. Uniform characteristic stabilization.** It remains to cover *every* prime \(p\ge17\), not just computed primes. For a selected pair \((x,y)\), every atomic relation involving a third point \(z\) either is fixed already by the pair or tests whether \(z\) equals one of the following ten vectors:
\[
0,\ x,\ y,\ 2x,\ 2y,\ x+y,\ x-y,\ y-x,\ x/2,\ y/2.
\]
Here division by two is legitimate for odd \(p\). All \(z\) outside this set have the same atomic extension diagram. For every \(p\ge11\) and positive \(d\), such an outside point exists because the entire group contains at least eleven elements, whereas the displayed set has at most ten. Thus the *complete set* of third-round atomic responses to \((x,y)\) is determined by the equality partition of these ten expressions and the pair atomic type.

For \(x\ne0\), every equality between two nonidentical expressions in the display, if it is not universally valid, forces \(y=tx\), where the rational slope \(t\) belongs to exactly the following list:
\[
-2,\ -1,\ -\tfrac12,\ 0,\ \tfrac14,\ \tfrac13,\ \tfrac12,\ \tfrac23,\ 1,\ \tfrac32,\ 2,\ 3,\ 4.
\]
This follows by subtracting each of the 45 pairs of the ten expressions; `verify.py` independently regenerates the list. For two different rational slopes on this list, the absolute value of their cross-multiplied numerator difference is at most 15. Therefore all thirteen are well-defined and pairwise distinct modulo every prime \(p\ge17\); their equality partitions also agree with the rational ones. Since \(p>13\), at least one scalar \(t\in\mathbf F_p\) avoids these thirteen slopes. A vector \(y=tx\) at such a generic slope has all the same third-round atomic diagrams as a linearly independent \(y\) in a larger-dimensional space: no nonuniversal equality among the ten displayed expressions holds. Hence the **set of all possible rank-one types of pairs extending each nonzero** \(x\) is identical for every prime \(p\ge17\) and every positive dimension. If \(x=0\), the alternatives \(y=0\) or \(y\ne0\) likewise yield a uniform set of pair types. The initial one-point atomic diagrams only distinguish zero and nonzero, which occur in all these groups. Two further applications of the extension recurrence prove that every \(A_{p,d}\) with \(p\ge17,d\ge1\) is rank-three equivalent.

For \(p=13,d\ge2\), all thirteen exceptional scalar slopes occur and a linearly independent \(y\) supplies the generic pair pattern; every ten-expression third-round pattern has an outside \(z\) because the group has at least \(169\) elements. Thus its rank-three type is the same universal type. For \(p=13,d=1\), every scalar is one of the thirteen exceptional slopes, so the generic pattern is absent, as the exact recurrence also confirms.

**4. Distinctness and sharpness.** The exact recurrence yields thirteen pairwise different top-level characteristic types. In a finite signature, unequal characteristic types are separated by a first-order sentence of the indicated quantifier rank, by the same induction underlying the EF theorem. The smallest element count in each class is given in the table, because each row's prime and dimension restrictions were exhaustively classified (and the large-prime row starts at prime 17). The maximum minimum is \(11^2=121\), completing the sharp bound.

## Verification
Run `python3 verify.py` using Python 3. The program uses only the standard library; it creates no external files. The included `verification_output.txt` records `VERIFY_OK classes=13 maximal_minimum_representative=121 exceptional_slopes=13` and `DIRECT_ORACLE_OK cases=10 ordered_comparisons=100`. The mathematical characteristic-stabilization proof above, not testing finitely many primes, covers the infinite prime range.

## Relationship to prior work
Gomaa's *Descriptive Complexity of Finite Abelian Groups* (International Journal of Algebra and Computation 20 (2010), 1087–1116; DOI 10.1142/S0218196710006047) studies Ehrenfeucht–Fraïssé complexity for finite abelian groups with ternary multiplication **and a named identity constant**. Its Sections 3–4 develop binders and asymptotic bounds, including prime cyclic groups; it does not provide the thirteen-class three-round classification in the identity-free relational reduct, nor the sharp 121-element representative. The absence of the constant changes the finite-depth problem: the identity is definable but defining it consumes quantifier depth. General EF/characteristic-formula methods are classical and are not claimed as new.

Other nearby work on vector-space EF games in field or scalar-multiplication signatures uses a richer language. Those results do not directly imply the rank-three classification for the one-relation additive reduct. The contribution claimed here is the exact joint prime/dimension classification and its sharp representative bound, not the underlying linear-algebra facts or the general EF recursion.

## Limitations
Only prime exponent elementary abelian groups are considered; arbitrary finite abelian groups, richer group signatures, counting logics, and quantifier rank four are not classified. The 13-class statement has undergone self-review and explicit finite verification, but not independent external audit. Relevant inaccessible or unindexed publications may affect an originality determination.

## References
- W. Gomaa, *Model Theory and Complexity Theory*, PhD thesis, University of Maryland (2007), institutional record https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 (record dated 2007-07-06).
- W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation **20** (2010), 1087–1116, DOI https://doi.org/10.1142/S0218196710006047. Sections 2–4 inspected in author-posted full text.
- L. Libkin, *Elements of Finite Model Theory*, Springer (2004), foundational background on Ehrenfeucht–Fraïssé games and characteristic types.
