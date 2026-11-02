# Twelve automorphism types of Schur rings on the three-by-three rectangular band

## Finding
Let \(B=[3]\times[3]\), with semigroup multiplication
\[
(i,j)(k,\ell)=(i,\ell).
\]
A *semigroup Schur ring* here means the rational linear span of the class sums of a set partition of \(B\), closed under multiplication in \(\mathbb Q[B]\); the semigroup need not have an identity and no group-style inverse condition is imposed.

**Theorem.** Exactly **42** partitions of the nine labeled cells give semigroup Schur rings. Every one is the orbit partition of a subgroup of \(\operatorname{Aut}(B)\cong S_3\times S_3\). Up to the action of this automorphism group there are exactly **12** types. Of the 42 labeled partitions, exactly 25 are direct-product partitions and 17 are not. The counts by number of partition classes are
\[
\begin{array}{c|rrrrrrr}
\text{classes}&1&2&3&4&5&6&9\\\hline
\text{partitions}&1&12&4&9&9&6&1
\end{array}.
\]

Here is a complete set of orbit representatives. In a nine-digit encoding the cells are read row by row in the order \((1,1),(1,2),(1,3),(2,1),\ldots,(3,3)\); cells with the same digit belong to the same partition class. The third column counts labeled partitions in the corresponding \(S_3\times S_3\)-orbit.

| Representative | Classes | Orbit size |
|:--|--:|--:|
| `000000000` | 1 | 1 |
| `000000111` | 2 | 3 |
| `001001001` | 2 | 3 |
| `001010100` | 2 | 6 |
| `000111222` | 3 | 1 |
| `012012012` | 3 | 1 |
| `012120201` | 3 | 2 |
| `001001223` | 4 | 9 |
| `001234324` | 5 | 9 |
| `001223445` | 6 | 3 |
| `012012345` | 6 | 3 |
| `012345678` | 9 | 1 |

## Assumptions and scope
The two factors each have exactly three labeled elements. Rational group-algebra coefficients are not required; the objects are subrings of the semigroup algebra \(\mathbb Q[B]\) arising from partitions, with the multiplication-only semigroup definition. Two partitions are identified up to isomorphism only under an actual automorphism of \(B\), which permutes the three rows and three columns independently. Swapping row and column coordinates is an anti-automorphism, not an automorphism, and is not included.

## Proof
**1. A complete algebraic acceptance criterion.** For a class \(C\subseteq B\), set
\[
r_C(i)=|C\cap(\{i\}\times[3])|,\qquad
c_C(j)=|C\cap([3]\times\{j\})|.
\]
For any two partition classes \(C,D\), the coefficient of \((i,j)\) in their product of class sums is exactly
\[
[\,(i,j)\,](\underline C\,\underline D)=r_C(i)c_D(j).
\]
Thus closure holds if and only if, for all class pairs \(C,D\), this coefficient is constant on each class \(E\).

Equivalently, cells \((i,j)\) and \((i',j')\) in the same class must have identical *complete row and column profiles*:
\[
\bigl(r_C(i)\bigr)_{C\in\mathcal P}
=\bigl(r_C(i')\bigr)_{C\in\mathcal P},\qquad
\bigl(c_C(j)\bigr)_{C\in\mathcal P}
=\bigl(c_C(j')\bigr)_{C\in\mathcal P}.
\]
Sufficiency follows by multiplying equal entries of these two profiles. For necessity, sum \(r_C(i)c_D(j)=r_C(i')c_D(j')\) over all \(D\), using \(\sum_Dc_D(j)=\sum_Dc_D(j')=3\); then sum over all \(C\), using \(\sum_Cr_C(i)=\sum_Cr_C(i')=3\). Division by 3 is legitimate over \(\mathbb Q\). This proves the criterion without any computational assumption.

**2. Exhaustive finite classification.** Every partition of nine labeled cells has a unique restricted-growth string \(a_0\ldots a_8\) with \(a_0=0\) and
\[
0\le a_t\le1+\max_{0\le s<t}a_s\quad (1\le t\le8).
\]
Enumerating all choices recursively visits every partition once. Both supplied programs independently enumerate all \(\operatorname{Bell}(9)=21{,}147\) such strings: `CHECK_DIRECT.py` tests literal class-sum structure constants; `CHECK_PROFILE.py` applies the proved row/column criterion. Each returns exactly 42 passing partitions and identical class-count distributions. This is an **exhaustive finite certificate**, not statistical sampling or extrapolation.

**3. Automorphic realization and isomorphism classes.** The full automorphism group acts as \((\sigma,\tau)(i,j)=(\sigma(i),\tau(j))\), so it has order 36. The direct checker independently constructs all 60 subgroups of this group by finite closure, computes their orbit partitions, and obtains exactly 42 distinct partitions. Each orbit partition is a Schur partition because multiplication is equivariant under semigroup automorphisms. Combined with the 42 exhaustive upper bound, this proves **every** Schur ring is automorphic. As a separate check, the profile verifier directly computes the entire setwise class stabilizer of each accepted partition and verifies that this group acts transitively on every class.

Canonicalizing the 42 accepted partitions under the 36 automorphisms gives the 12 explicit representatives in the table. Their orbit sizes sum to 42, independently reconfirmed by both programs. Finally, the product of a partition of the three rows with a partition of the three columns always yields a Schur ring. There are exactly \(\operatorname{Bell}(3)^2=25\) such distinct direct-product partitions, leaving \(42-25=17\) genuinely non-product examples.

## Verification
Run `python3 CHECK_DIRECT.py` and `python3 CHECK_PROFILE.py` with Python 3 standard libraries only. The included `CHECK_DIRECT_OUTPUT.txt` and `CHECK_PROFILE_OUTPUT.txt` record the exact expected outputs. Both checks were executed on the supplied standalone programs and terminated with `VERIFY_OK`. The programs independently verify the full 21,147-partition coverage, the counts, the automorphic realization, the 12 orbit representatives, and the rank distributions. The proof of the row/column criterion is mathematical; the finite census is completed by the exhaustive algorithms.

## Relationship to prior work
Marrow and Misseldine [1] introduced the semigroup version of Schur rings used here. They established direct-product constructions, recognized automorphic constructions, and tabulated semigroups through order seven. They also noted that rectangular bands can possess additional Schur rings beyond direct-product ones. These observations give 25 direct-product examples for the order-nine band but do not state the 42 total or the twelve-type classification here. The explicit converse that all 42 partitions are automorphic is specific to the three-by-three case; it does not follow merely from the existence of automorphic examples. The nine-element square case is not implied by a separate classification confined to rectangular bands with two rows.

## Limitations
The classification is specific to the nine-element rectangular band and does **not** claim that every Schur ring on every rectangular band is automorphic. The automorphism types are with respect to \(S_3\times S_3\), not anti-isomorphism or arbitrary algebra isomorphism. Completeness of the numerical case split is verified by the included exhaustive Python 3 checkers. No independent external mathematical audit has been performed, and an undiscovered broader result or exact enumeration could affect historical priority.

## References
[1] Joseph E. Marrow and Andrew Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940, first publicly posted 2026-01-14. https://arxiv.org/abs/2601.09940 ; open HTML https://arxiv.org/html/2601.09940v1 . See definitions in Section 1, automorphic and direct-product constructions in Sections 2.1–2.2, and small-semigroup enumeration in Section 5.
