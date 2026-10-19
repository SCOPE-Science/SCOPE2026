# A three-level minimal-absent-factor law for four-run binary words

## Finding

For positive integers \(a,b,c,d\), write
\[
W=0^a1^b0^c1^d.
\]
All factors are **contiguous**, the source word is **linear**, and the ambient alphabet is precisely \(\{0,1\}\). A minimal absent factor is an absent nonempty word every proper contiguous factor of which occurs in \(W\). Let \(\mathcal M(W)\) be the set of all such factors. The exact cardinality is
\[
\boxed{|\mathcal M(W)|=b+c+2^{\mathbf{1}_{a>c}+\mathbf{1}_{d>b}}.}
\]
Thus the excess over \(b+c\) is always \(1\), \(2\), or \(4\), never \(3\). All three possibilities occur, and the value is determined solely by the two strict comparisons \(a>c\) and \(d>b\).

More strongly, the following ten disjoint families give the **complete set** \(\mathcal M(W)\). A family with a condition is empty unless its stated condition holds.

1. \(\{0^{\max(a,c)+1},\ 1^{\max(b,d)+1}\}\).
2. \(\{01^j0:1\le j<b\}\).
3. \(\{10^j1:1\le j<c\}\).
4. \(\{1^{b+1}0\}\) if \(d>b\).
5. \(\{10^{c+1}\}\) if \(a>c\).
6. \(\{0^{a+1}1^b0\}\) if \(c>a\) and \(d\ge b\).
7. \(\{10^c1^b0\}\) if \(a\ge c\) and \(d\ge b\).
8. \(\{0^{c+1}1^{b+1}\}\) if \(a>c\) and \(d>b\).
9. \(\{0^{a+1}1^{d+1}\}\) if \(c>a\) and \(b>d\).
10. \(\{10^c1^{d+1}\}\) if \(a\ge c\) and \(b>d\).

## Assumptions and scope

The parameters \(a,b,c,d\) range independently over all positive integers. Occurrences cannot wrap from the last letter to the first. Repetition exponents are counts of contiguous equal symbols. The source contains both alphabet symbols, so no absent one-letter words arise. The theorem is not about scattered subsequences or the periodic factor language of a circular word. No parameter-size cutoff is imposed.

## Proof

**Factor criterion.** An absent word of length at least two is minimal precisely when both its prefix and suffix of length one less are factors of \(W\). Indeed those two factors contain all its proper contiguous factors. Every factor of \(W\) has at most four runs. A factor with four runs necessarily has shape \(0^i1^b0^c1^j\), with \(1\le i\le a\) and \(1\le j\le d\). The three-run factors have shapes \(0^i1^b0^j\), where \(1\le i\le a,1\le j\le c\), or \(1^i0^c1^j\), where \(1\le i\le b,1\le j\le d\).

**One and two runs.** The only minimal absent single-run words are the two words in family 1, by the maximal run lengths. A factor of shape \(1^i0^j\) occurs exactly when \(i\le b\) and \(j\le c\). The prefix/suffix criterion therefore gives \(1^{b+1}0\) only if \(1^{b+1}\) occurs in the final run (\(d>b\)), and \(10^{c+1}\) only if \(0^{c+1}\) occurs in the initial run (\(a>c\)). These are families 4 and 5.

A factor of shape \(0^i1^j\) occurs exactly when
\[
(i\le a\ \text{and}\ j\le b)\quad\text{or}\quad(i\le c\ \text{and}\ j\le d).
\]
Its possible minimal absent words are the missing interior corners of the union of these two integer rectangles. A corner exists only when neither rectangle dominates the other: it is \(0^{c+1}1^{b+1}\) if \(a>c,d>b\), or \(0^{a+1}1^{d+1}\) if \(c>a,b>d\). These are families 8 and 9. No boundary corner with one exponent equal to one is absent and minimal, since both adjacent mixed pairs occur in \(W\).

**Three runs.** For \(0^i1^j0^k\), the middle run must be bridged across the unique first-to-second zero-run transition. If \(1\le j<b\), the word is absent but its length-one deletions at the ends are factors exactly when \(i=k=1\); this gives family 2. If \(j>b\), its suffix containing \(1^j0\) is absent. If \(j=b\), the word occurs for \(i\le a,k\le c\). A missing left extension is minimal exactly when \(i=a+1,k=1,c>a,d\ge b\), giving family 6; a missing right extension cannot be minimal because \(1^b0^{c+1}\) is itself absent. Hence no other three-run word of this orientation is minimal absent.

Symmetrically, a \(1^i0^j1^k\) word with \(j<c\) contributes precisely \(10^j1\) (family 3), while \(j>c\) cannot be minimal absent. At \(j=c\), a missing right extension is minimal exactly when \(i=1,k=d+1,a\ge c,b>d\), giving family 10. A missing left extension cannot be minimal, because \(1^{b+1}0^c\) is absent. These exhaust three-run possibilities.

**Four and more runs.** Consider a four-run word beginning with zero and ending with one, of shape \(0^i1^j0^k1^l\). Whenever its length-one-shorter prefix retains four runs, its occurrence forces the middle exponents \(j=b,k=c\) and the permitted initial exponent; whenever its suffix retains four runs it likewise forces the middle exponents and the permitted final exponent. If \(i=1\) or \(l=1\), the corresponding shortened word has three runs, whose occurrence forces \(j=b\) or \(k=c\), respectively. Combining both shortened-factor conditions in all four endpoint cases yields \(i\le a,j=b,k=c,l\le d\): the entire candidate already occurs. Thus no four-run word in the \(0\)-to-\(1\) orientation is minimal absent.

For \(1^i0^j1^k0^l\), no four-run occurrence exists. Minimality forces \(i=l=1\), or else one of its shortened factors would also have an impossible four-run orientation. Its prefix \(10^j1^k\) occurs precisely when \(j=c,k\le d\); its suffix \(0^j1^k0\) occurs precisely when \(j\le a,k=b\). Consequently the unique possible four-run minimal absent word is \(10^c1^b0\), present as family 7 exactly when \(a\ge c,d\ge b\).

A word with five runs would need singleton first and last runs for both shortened words to have at most four runs. One of those shortened words would then have four runs beginning with one and ending with zero, impossible in \(W\). With six or more runs at least one shortened word retains five or more runs, also impossible. Hence families 1–10 are exhaustive. Their defining conditions are the precise conditions for the two shortened factors to occur, so every listed word is indeed minimal absent. The families are disjoint by run orientation, exponent, or mutually exclusive parameter inequalities.

**Counting.** Families 1–3 contribute \(2+(b-1)+(c-1)=b+c\). The seven remaining singleton conditions contribute, respectively, \(4\) if both \(a>c\) and \(d>b\), \(2\) if exactly one holds, and \(1\) if neither holds. This is exactly \(2^{\mathbf{1}_{a>c}+\mathbf{1}_{d>b}}\), proving the formula and the missing-excess-three phenomenon. For example, parameters \((a,b,c,d)=(1,1,1,1),(2,1,1,1),(2,1,1,2)\) realize excess \(1,2,4\), respectively.

## Verification

A standalone Python 3 checker enumerates the complete minimal absent factor set independently from intersecting factor contexts, for all \(7^4=2401\) parameter quadruples with entries between one and seven. It separately scans all binary candidate words directly for 310 quadruples of total source length at most eleven, and examines 200 additional reproducibly sampled quadruples with entries between one and fifteen. It compares sets (not just cardinalities) and checks the closed formula. All checks passed. These finite checks are corroboration; the preceding proof applies to all positive integer parameters.

To replay, run `python3 verify.py` in the directory containing the accompanying file. Only the Python standard library is required.

## Relationship to prior work

Akagi, Okabe, Mieno, Nakashima, and Inenaga established a general output-sensitive minimal-absent-word data structure for run-length encoded strings and divided minimal absent words into five structural types. That general algorithm can enumerate the words for any fixed instance, but the inspected results do not state a symbolic four-run classification or the exact three-level cardinality law. The present theorem concerns a special but naturally parameterized family and supplies both closed-form membership and an explicit structural phase diagram without running a general-purpose enumeration algorithm.

Fici, Restivo, and Rizzo study minimal forbidden factors of circular languages (factors of arbitrary powers). Their boundary convention and principal results differ from minimal absence for one fixed linear word. Subsequent CDAWG-space work provides more general enumeration algorithms without the four-run symbolic law. None of the cited general algorithms is claimed as new here.

## Limitations

The formula is limited to two symbols, four positive runs, and linear contiguous factors. It does not characterize words with five or more runs, circular words, or scattered subsequences. The available literature comparison did not identify this particular closed-form classification, but unindexed prior derivations or implicit specializations in later work remain possible; independent assessment has not been performed.

## References

1. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591, first public version February 28, 2022; CPM 2022, DOI: 10.4230/LIPIcs.CPM.2022.27.
2. G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (2017); Theoretical Computer Science 792 (2019), 144–153.
3. S. Inenaga, T. Mieno, H. Arimura, M. Funakoshi, Y. Fujishige, *Computing Minimal Absent Words and Extended Bispecial Factors with CDAWG Space*, arXiv:2402.18090 (2024).
