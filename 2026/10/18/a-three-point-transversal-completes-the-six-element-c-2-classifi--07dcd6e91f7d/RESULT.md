# A three-point transversal completes the six-element \(C^2\) classification for three equivalences

## Finding
Let \(E,F,G\) be three **named** equivalence relations on a common finite nonempty set, with no other relations or constants. For structures of each size from one through six, the numbers of isomorphism classes and of two-variable counting-logic (\(C^2\)) classes are respectively:

| Size | Isomorphism classes | \(C^2\) classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 8 | 8 |
| 3 | 37 | 37 |
| 4 | 285 | 285 |
| 5 | 2,150 | 2,150 |
| 6 | 21,205 | 21,197 |

Every \(C^2\)-class through size five is a singleton. At size six there are exactly **eight doubletons** of nonisomorphic structures and 21,189 singleton classes; there are no larger classes. These eight doubletons form four orbits, of sizes \(1,3,3,1\), under simultaneous permutation of the names \(E,F,G\).

Define a *common transversal triple* to be a three-element subset \(\{x,y,z\}\) for which each pair is inequivalent under each of \(E,F,G\). In every exceptional doubleton, one structure has **zero** common transversal triples and the other has **exactly two**. Consequently, adjoining the single three-variable sentence
\[
\tau:=\exists x\,\exists y\,\exists z\;\bigwedge_{\{u,v\}\in\binom{\{x,y,z\}}2}\bigl(\neg E(u,v)\land\neg F(u,v)\land\neg G(u,v)\bigr)
\]
to the complete \(C^2\)-theory distinguishes **all** nonisomorphic structures of at most six elements in this signature. This last assertion is restricted to the stated cardinality range.

## Assumptions and scope
All structures are finite, nonempty, and carry three labeled (not interchangeable in the isomorphism definition) reflexive, symmetric, transitive binary relations. The entire domain is subject to simultaneous bijective relabeling, while the relation names are held fixed. \(C^2\) permits arbitrarily nested counting quantifiers over at most the variable names \(x,y\), and contains equality. Cardinality itself is \(C^2\)-definable by counting, so different sizes can be considered independently. The count \(21,205\) refers to isomorphism classes, not to labeled objects. No claim is made for structures of seven or more elements or for extra predicates.

## Proof
**1. Complete structural enumeration.** Each equivalence relation on \(n\) labeled elements is uniquely a set partition, encoded by a restricted-growth string \(p_0,\ldots,p_{n-1}\), with \(p_0=0\) and \(0\le p_i\le 1+\max_{j<i}p_j\). Generate all such strings (Bell numbers \(1,2,5,15,52,203\)). Generate one representative \(E\) from each orbit of partitions under \(S_n\). For each such \(E\), generate one representative \(F\) from each orbit of partitions under the stabilizer of \(E\). For each pair \((E,F)\), generate one representative \(G\) from each orbit of partitions under the common stabilizer of \(E,F\). The standard orbit-stabilizer argument proves that this outputs **every** isomorphism type of ordered triples \((E,F,G)\) once and only once. Direct computation gives the first numeric column above.

An independent Burnside check uses
\[
\#\bigl(\mathcal P_n^3/S_n\bigr)=\frac1{n!}\sum_{\pi\in S_n}\bigl|\{P\in\mathcal P_n:\pi P=P\}\bigr|^3,
\]
where \(\mathcal P_n\) denotes the set of partitions of \(n\) points. It reproduces all six isomorphism counts without using the stabilizer-transversal enumeration.

**2. Complete counting-logic comparison.** Apply a *single synchronized* color refinement to all the representative structures of fixed size \(n\), not separate local color labels. Initially all vertices have color zero. Given color \(c_t(x)\), the next color records, injectively,
\[
\left(c_t(x),\left\{\!\left\{\left(b(x,y),c_t(y)\right):y\ne x\right\}\!\right\}\right),
\qquad b(x,y)=\mathbf1_{E(x,y)}+2\mathbf1_{F(x,y)}+4\mathbf1_{G(x,y)}.
\]
The diagonal \(y=x\) is excluded because equality already specifies its atomic type. Importantly, **all eight joint atomic masks** are retained, not merely separate block-size totals. Two structures have the same \(C^2\)-theory exactly if their multisets of stable global vertex colors agree, by the standard counting-logic/color-refinement correspondence for finite binary relational signatures. Refinement is monotone, and the global number of color classes is unchanged after the third iteration at sizes five and six (earlier at smaller sizes); subsequent iterations through seven confirm stability. The resulting histogram classes have exactly the sizes in the table and exactly eight doubletons at six points.

**3. A uniform three-variable separator.** All eight doubletons, including the exact restricted-growth strings of their members, are listed in `COLLISIONS.json`. For each member, exhaust the \(\binom63=20\) unordered vertex triples and count those whose three pair masks are zero. In every doubleton the ordered counts are \((0,2)\). The formula \(\tau\) expresses existence of such a triple, so it separates the two structures in each doubleton. All other classes were singletons already; therefore \(C^2\) together with this single sentence separates all isomorphism types through six points. The named-relation symmetry orbits of the eight doubletons, computed by explicitly permuting the three relation names and canonically relabeling their vertices, have sizes \(1,3,3,1\).

An explicit representative doubleton has \(E\) encoded by `001122`, \(F\) by `010212`, and its two \(G\)-relations by `011220` and `012120`, respectively. The full certificate is in the standalone file rather than relying on this one example.

## Verification
Run `python3 verify_triple_equivalences.py 6` from the directory containing the artifacts to regenerate the full orbit and \(C^2\) partition census. Run `python3 crosscheck_triple_equivalences.py` for an independent Burnside orbit count, exhaustive permutation tests of nonisomorphism for each doubleton, independently recomputed pairwise color refinement, and the relation-name symmetry orbit check. Run `python3 triangle_witnesses.py` to regenerate `COLLISIONS.json`, including each changed three-vertex atomic-mask motif. All scripts use the Python standard library. These computations were executed against the files supplied with this result; they reproduced the stated counts and every \((0,2)\) transversal discrepancy.

## Relationship to prior work
Kiefer, Schweitzer, and Selman's 2015 preprint provides a **much broader structural characterization** of finite relational structures identified by \(C^2\), including unusual small edge-coloured regular cases (especially their Theorems 24 and 27). Their discussion already exhibits a six-point colour-regular ambiguity of the sort that motivates this question, so the mere existence of an early ambiguity is **not** claimed as new. The exact eight-doubleton census in the restricted signature of **three named equivalences**, the four name-symmetry orbits, and the **one common-transversal sentence resolving all eight** are the claims here. Pratt-Hartmann's 2015 paper concerns satisfiability and undecidability boundaries with equivalence predicates; it does not furnish this explicit six-point ambiguity table. A full prior derivation of these exact numbers from the general classification has not been located; the general classification makes priority assessment nontrivial.

## Limitations
This is a complete **finite cutoff** theorem, not an all-size characterization. Computer-assisted exhaustive enumeration is part of the proof: its correctness depends on the short, supplied and executable enumeration algorithms, not solely on the reported output. The companion Burnside identity independently checks isomorphism totals, while the second implementation checks the ambiguous pairs rather than independently reproducing the entire global colour partition. Exhaustive finite verification cannot establish claims beyond six elements. Published general classification theorems may admit an alternative derivation, and an unlocated earlier finite tabulation remains a priority risk. Independent human review has not yet been performed.

## References
1. Sandra Kiefer, Pascal Schweitzer, Erkal Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, first posted 2015-03-30; especially the introduction, Section 5, Theorems 24 and 27. https://arxiv.org/abs/1503.08792
2. Ian Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, Mathematical Logic Quarterly **61** (2015), 474–515, published 2015-11-25; DOI:10.1002/malq.201400102, especially Sections 1 and 7. https://doi.org/10.1002/malq.201400102
