# Exact abelian-complexity trichotomy for binary Parikh-constant three-uniform morphisms

## Finding

Let \(\sigma\) be a morphism on \(\{0,1\}\) whose two images have length three and the same Parikh vector, each containing both letters. Suppose \(\sigma(0)\) starts with \(0\), so the infinite fixed point \(x=\sigma^\omega(0)=x_0x_1\cdots\) exists. For \(n\ge1\), let \(a_x(n)\) count the distinct Parikh vectors of contiguous length-\(n\) factors. Because the alphabet is binary, it is also one plus the difference between their maximum and minimum counts of \(1\).

**Theorem (complete nine-morphism classification).** With all pairs written in the order \((\sigma(0),\sigma(1))\), there are exactly three profiles:

| Morphisms | Exact abelian complexity for all positive lengths |
| --- | --- |
| `001/001`, `010/010`, `011/011` | \(a_x(n)=1\) for \(3\mid n\), and \(2\) otherwise. |
| `001/010`, `010/001`, `010/100`, `011/101` | \(a_x(n)=3\) for \(3\mid n\), and \(2\) otherwise. |
| `001/100`, `011/110` | \(a_x(1)=2\); \(a_x(n)=3\) for every \(n\ge2\). |

Thus this complete natural binary three-uniform Parikh-constant family has abelian complexity periodic from length two, with period dividing three. The claimed formulas include all finite boundary cases.

## Assumptions and scope

The fixed point is one-sided and indexed from zero. Factors are contiguous, not scattered. For a finite word \(w\), its Parikh vector is \((|w|_0,|w|_1)\); no other equivalence relation is used. The full-support hypothesis excludes the trivial single-symbol images, and prolongability on \(0\) excludes a fixed-point convention ambiguity. Complementation exchanges fixed-point seeds and preserves abelian complexity. No classification beyond binary length-three image pairs is asserted.

There are exactly nine admissible morphisms: if each image has one \(1\), then \(\sigma(0)\in\{001,010\}\) and \(\sigma(1)\in\{001,010,100\}\); if each image has two \(1\)'s, then \(\sigma(0)=011\) and \(\sigma(1)\in\{011,101,110\}\).

## Proof

**1. Periodic instances.** If the images coincide, iteration gives \(x=\sigma(0)^\omega\). This period-three word contains one or two ones in each complete period. Every factor of length divisible by three has the same number of ones, while a factor of either other residue has exactly two possible counts. This establishes the first row.

**2. All ordered letter pairs at every sufficiently long displacement.** Consider the other six morphisms. For every integer \(d\ge1\), put
\[
 P_d=\{(x_i,x_{i+d}):i\ge0\}\subseteq\{0,1\}^2.
\]
The following **full-lag lemma** holds for each of these six fixed points:
\[
 P_d=\{00,01,10,11\}\qquad(d\ge3).
\]
For the finite base \(3\le d\le8\), each of the four ordered pairs is witnessed directly inside the prefix \(\sigma^8(0)\), by the complete deterministic search in `verify.py`. This supplies \(6\cdot6\cdot4\) finite witness assertions, not statistical sampling.

For the infinite induction, define the letter maps \(f_j(t)=\sigma(t)_j\), for \(j=0,1,2\). The fixed-point identity \(x_{3i+j}=f_j(x_i)\) implies, for every \(s\in\{0,1,2\}\) and \(k\ge1\),
\[
 P_{3k+s}=\bigcup_{j=0}^{2}
 \{(f_j(u),f_{(j+s)\bmod3}(v)):
 (u,v)\in P_{k+\lfloor(j+s)/3\rfloor}\}.
\]
For each of the six substitutions, and separately for each of the three values of \(s\), replacing both input pair sets by the full four-element set makes this union the full four-element set. All eighteen explicit finite-map identities are checked in `verify.py` without reference to long sequence prefixes. If \(d=3k+s\ge9\), then \(3\le k,k+1<d\). Strong induction from the finite base therefore proves the lemma for every \(d\ge3\).

**3. Exact factor-weight envelopes.** Write \(c=|\sigma(0)|_1=|\sigma(1)|_1\), and for \(t\in\{0,1\}\) define the prefix counts \(\pi_j(t)=|\sigma(t)_{[0,j)}|_1\), for \(j=0,1,2,3\). A length \(n=3k+r\) factor starting at offset \(j\) in an image block, with \(0\le r,j<3\), has \(1\)-count \(kc+\Delta\), where
\[
 \Delta=\begin{cases}
 -\pi_j(x_i)+\pi_{j+r}(x_{i+k}),&j+r<3,\\
 c-\pi_j(x_i)+\pi_{j+r-3}(x_{i+k+1}),&j+r\ge3.
 \end{cases}
\]
This is an exact cut into the initial partial image, full middle images (each of weight \(c\)), and final partial image. For \(k\ge3\), the full-lag lemma implies that *every ordered boundary-letter pair* occurs in each of the needed displacements \(k\) and \(k+1\). Thus taking the minimum and maximum over \(j=0,1,2\) and both possible boundary letters computes the **attained** minimum and maximum of \(\Delta\), not merely an upper bound. Direct substitution gives the following complete table, in which columns are \(r=0,1,2\) and each entry is \((\min\Delta,\max\Delta)\):

| \((\sigma(0),\sigma(1))\) | \(r=0\) | \(r=1\) | \(r=2\) |
| --- | --- | --- | --- |
| `001/010` | \((-1,1)\) | \((0,1)\) | \((0,1)\) |
| `001/100` | \((-1,1)\) | \((-1,1)\) | \((0,2)\) |
| `010/001` | \((-1,1)\) | \((0,1)\) | \((0,1)\) |
| `010/100` | \((-1,1)\) | \((0,1)\) | \((0,1)\) |
| `011/101` | \((-1,1)\) | \((0,1)\) | \((1,2)\) |
| `011/110` | \((-1,1)\) | \((0,2)\) | \((0,2)\) |

For lengths \(3\le n\le8\), evaluating the same formula over all four pairs still gives a universal enclosing interval; an explicit factor of \(\sigma^8(0)\) realizes each extreme. The checker verifies these twelve-plus cases symbolically against the envelope. At length \(1\), both letters appear. At length \(2\), the possible counts have range \(0\) to \(2\) precisely for `001/100` and `011/110`; for the other four nonconstant image pairs the range width is one. Both claims are directly exhibited and checked inside \(\sigma^8(0)\).

**4. From extrema to the number of Parikh classes.** The number of ones in a length-\(n\) sliding window changes by at most one when the starting position increases by one. Every integer between any attained minimum and maximum therefore occurs. Hence \(a_x(n)=1+\max|w|_1-\min|w|_1\) exactly. Applying this to the table and the finite boundary lengths yields the other two rows of the theorem. \(\square\)

## Verification

Run `python3 verify.py` using only the standard Python library. The checker enumerates the nine morphisms, proves the six-by-six finite ordered-pair bases using genuine factors of \(\sigma^8(0)\), tests the eighteen finite maps in the induction step, independently recalculates all residue envelopes, verifies the small boundary lengths, and compares all theorem values for lengths \(1\le n\le1024\) for all nine morphisms. The recorded output is:

`VERIFY_OK morphisms=9 nonconstant=6 pair_base_and_step=54 boundary=66 prefix_checks=9216 direct_class_checks=576`

The infinite argument is the explicit displacement induction and the block-boundary identity; finite testing alone is not an infinite proof. The checker supplies the small exhaustive pieces on which those arguments depend.

## Relationship to prior work

Rigo, Stipulanti, and Whiteland prove computable automaticity for abelian complexity of fixed points of arbitrary Parikh-collinear morphisms and explicitly ask whether Parikh-constant morphisms have ultimately periodic abelian complexity. The present result establishes that property, with exact values, for **all** full-support binary three-uniform Parikh-constant morphisms prolongable on a letter. Automaticity alone does not imply ultimate periodicity, and the cited work does not give the nine-case trichotomy. This small complete class is motivated by the stated general question, not selected by an arbitrary numeric invariant. Classical periodic words and specific automatic-word formulas are acknowledged as earlier cases; the new assertion is the complete family classification and uniform full-lag mechanism.

## Limitations

This establishes only the stated binary image-length-three family. No deduction is made about all binary image lengths, larger alphabets, all Parikh-collinear substitutions, or any stronger general conjecture. Direct factor enumeration is used only to certify finite witnesses and boundary cases, and publication priority beyond the inspected references remains subject to independent literature review. There is no independent mathematical audit attached to this result.

## References

1. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032 (first public May 28, 2024), https://arxiv.org/abs/2405.18032 ; DOI: 10.1007/s00224-024-10197-5. In particular Theorem 3 and Section 6 (Concluding Remarks).
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Automaticity and Parikh-collinear Morphisms*, Combinatorics on Words 2023, LNCS 13899, 247–260, DOI: 10.1007/978-3-031-33180-0_19.
