# An exact cyclic Burrows–Wheeler recursion for period-doubling words

## Finding

Write \(\operatorname{BWT}(w)\) for the last column obtained by sorting all cyclic rotations of a nonempty binary word \(w\) in lexicographic order \(0<1\). Let \(\mu(0)=01\), \(\mu(1)=00\). If \(w\) is any circular binary word containing both symbols and avoiding the cyclic factor \(11\), set \(z=|w|_0\), \(k=|w|_1\), and let \(C(w)\) be the first \(z\) characters of \(\operatorname{BWT}(w)\). Then the **entire transform** satisfies

\[
\operatorname{BWT}(\mu(w))
 =1^{k}0^{k}\,\overline{C(w)^{\mathrm R}}\,0^{z}.
\tag{1}
\]

Here reversal \((\cdot)^{\mathrm R}\) reverses character order, and an overline complements every bit. In particular, for \(W_m=\mu^m(0)\) and every integer \(m\ge2\),

\[
\boxed{r(\operatorname{BWT}(W_m))=2m-2
=2\log_2 |W_m|-2,}
\tag{2}
\]

where \(r\) counts the maximal constant-letter runs in a **linear** transform, including its two ends separately. These formulas use the cyclic-rotation transform, with no appended endmarker. They hold for indexed rotations even if the word is imprimitive.

## Assumptions and scope

The alphabet is exactly the ordered alphabet \(\{0,1\}\). A cyclic factor may cross the last-to-first boundary. In (1), \(w\) has length at least two, contains at least one of each symbol, and has no adjacent ones cyclically. Reversal and complementation apply to finite words, and juxtaposition denotes concatenation. Equal cyclic rotations may be ordered arbitrarily: they have identical preceding letters, so the transform itself is well-defined.

In (2), \(m\) ranges over all integers at least two; the initial word \(W_0=0\) and the first iterate \(W_1=01\) are not covered by the displayed linear law. In fact, \(\operatorname{BWT}(W_1)=10\) has two runs.

## Proof

**Lexicographic four-block lemma.** Index \(w\) cyclically, and call a rotation of \(\mu(w)\) *even* or *odd* according to whether its starting position is the first or second character of some image \(\mu(w_i)\). Since every image begins with \(0\) and since a \(1\) in \(w\) has a following \(0\), the cyclic rotations of \(\mu(w)\) fall into the following four disjoint consecutive lexicographic blocks, determined by their first characters:

| Block | Starting position | Condition | Required prefix | Preceding bit |
|---|---|---|---|---|
| A | Even | \(w_i=1\) | `000` | `1` |
| B | Odd | \(w_i=1\) | `001` | `0` |
| C | Even | \(w_i=0\) | `01` | \(1-w_{i-1}\) |
| D | Odd | \(w_i=0\) | `1` | `0` |

All four classes are nonempty because both symbols occur. The preceding bit in A is \(1\), since a cyclic \(1\) is preceded by \(0\) and the last bit of \(\mu(0)=01\) is \(1\). An odd start is always preceded by the first bit, \(0\), of its own image. Thus blocks A, B, and D contribute, respectively, \(1^k\), \(0^k\), and \(0^z\) to the transform.

Within C, comparing two even-start rotations is equivalent to comparing their original rotations after substitution by \(\mu\). At the first differing original bit, \(\mu(0)=01>00=\mu(1)\) lexicographically, so substitution **reverses** strict lexicographic order. The original rotations beginning with \(0\) form the first \(z\) rows of the original sorted rotation matrix, and their preceding characters spell \(C(w)\). The preceding characters of the corresponding even-start rotations are the complementary bits \(1-w_{i-1}\). Therefore C contributes \(\overline{C(w)^{\mathrm R}}\). This proves (1), including any repeated-rotation case: equal rotations have equal predecessors.

**Iteration.** Each image of \(\mu\) starts with \(0\), so avoidance of cyclic \(11\) is preserved. Every \(W_m\) for \(m\ge1\) contains both symbols. All rotations beginning with \(1\) are preceded by \(0\), hence

\[
\operatorname{BWT}(W_m)=C_m0^{k_m},\qquad
C_m=C(W_m),\quad k_m=|W_m|_1>0.
\]

The number of zeros in \(\mu(W_m)\) is \(|W_m|+k_m\), so removing its final \(|W_m|_0\) zeros from (1) yields the exact prefix recursion

\[
C_{m+1}=1^{k_m}0^{k_m}\,\overline{C_m^{\mathrm R}}.
\tag{3}
\]

Directly, \(W_1=01\), \(\operatorname{BWT}(W_1)=10\), and \(C_1=1\). Equation (3) gives \(C_2=100\), whose first and last bits are \(1,0\) and which has two runs. Inductively, if \(C_m\) begins with \(1\) and ends with \(0\), then \(\overline{C_m^{\mathrm R}}\) also begins with \(1\) and ends with \(0\). Concatenating the two initial nonempty blocks \(1^{k_m}0^{k_m}\) therefore introduces **exactly two** runs, so

\[
r(C_{m+1})=r(C_m)+2 \quad (m\ge2).
\]

Finally the trailing \(0^{k_m}\) in \(\operatorname{BWT}(W_m)=C_m0^{k_m}\) merges with the last run of \(C_m\), so \(r(\operatorname{BWT}(W_m))=r(C_m)=2+2(m-2)\). Since each iteration doubles length, \(|W_m|=2^m\), establishing (2) with its exact boundary \(m=2\).

## Verification

The accompanying standalone `verify.py` implements two different cyclic-rotation sorting algorithms: direct lexicographic sorting and cyclic rank-doubling. It checks (1) for **all 828** mixed binary circular words avoiding \(11\) of lengths 2 through 12, including nonprimitive words, and independently compares the two transforms. It checks (2) by actual cyclic sorting through \(m=13\), with direct independent sorting through \(m=10\), and checks the complete transform recursion through \(m=20\), where length is \(2^{20}\). Its successful output is `VERIFY_OK cyclic_words=828 sorted_iterates=12 max_round=20`. The infinite claims follow from the four-block proof, not from those finite checks.

To replay: `python3 verify.py` (Python 3 standard library only).

## Relationship to prior work

Brlek, Frosini, Mancini, Pergola and Rinaldi (2019) calculated BWT behavior for Thue–Morse iterates, generalized Fibonacci words and related compositions; those substitutions are different from period doubling. Frosini, Mancini, Rinaldi, Romana and Sciortino (2022, preprint first public February 5) proved general logarithmic bounds for binary purely morphic words and some other exact examples; an \(O(m)\) result cannot specify the present coefficient, constant term, or complete BWT word. Fici, Romana, Sciortino and Urbina (2023) analyzed the effect of **one application** of period doubling on selected arbitrary words, proving an unbounded worst-case additive sensitivity, not the fixed-point iteration in (2) nor (1). Their 2025 sequel characterizes morphisms with bounded sensitivity, again a different quantifier and invariant. A 2026 survey recapitulates these sensitivity results. None of the inspected theorem statements or relevant full-text sections supplies (1) or (2); this comparison does not assert a proof of uniqueness across all literature.

## Limitations

The identity is specific to the cyclic, unsentinelled BWT, the indicated substitution, binary alphabet order, and the cyclic absence of \(11\). It does not describe the endmarker-suffixed BWT, arbitrary substitutions, or arbitrary binary words that contain cyclic \(11\). The count in (2) is for the finite substitution iterates, not all finite prefixes of the infinite fixed point. The scientific novelty assessment is based on inspected sources and search results, not an exhaustive bibliographic uniqueness certificate. No independent scientific audit has been performed.

## References

1. A. Frosini, I. Mancini, S. Rinaldi, G. Romana, M. Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, arXiv:2202.02609, first public 2022-02-05. https://arxiv.org/abs/2202.02609
2. S. Brlek, A. Frosini, I. Mancini, E. Pergola, S. Rinaldi, *Burrows–Wheeler Transform of Words Defined by Morphisms*, IWOCA 2019, DOI:10.1007/978-3-030-25005-8_32. https://flore.unifi.it/handle/2158/1171602
3. A. Frosini, I. Mancini, S. Rinaldi, G. Romana, M. Sciortino, *Burrows-Wheeler Transform on Purely Morphic Words*, DCC 2022, DOI:10.1109/DCC52660.2022.00063. https://doi.org/10.1109/DCC52660.2022.00063
4. G. Fici, G. Romana, M. Sciortino, C. Urbina, *On the Impact of Morphisms on BWT-Runs*, CPM 2023, DOI:10.4230/LIPIcs.CPM.2023.10. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2023.10
5. G. Fici, G. Romana, M. Sciortino, C. Urbina, *Morphisms and BWT-Run Sensitivity*, MFCS 2025, DOI:10.4230/LIPIcs.MFCS.2025.49. https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.49/LIPIcs.MFCS.2025.49.html
6. G. Fici et al., *BWT and Combinatorics on Words*, 2026 survey. https://drops.dagstuhl.de/storage/01oasics/oasics-vol131-manzinis-festschrift/OASIcs.Manzini.1/OASIcs.Manzini.1.pdf
