# A one-factor certificate and exact count for minimum attractors of injective periodic prefixes

## Finding
Let \(q\ge 2\) and \(k\ge 1\) be integers, and let \(0\le r<q\). Over an alphabet of \(q\) distinct letters \(a_0,\ldots,a_{q-1}\), put
\[
W_{q,k,r}=(a_0a_1\cdots a_{q-1})^k a_0a_1\cdots a_{r-1},
\]
where the final suffix is empty for \(r=0\). A *string attractor* is a set of positions intersecting at least one occurrence of every nonempty contiguous factor. Every smallest attractor of \(W_{q,k,r}\) has cardinality exactly \(q\) and selects exactly one occurrence of each letter.

Use zero-based indexing. Specify such a set by indices \(t_i\) with \(0\le t_i<k+\mathbf{1}_{i<r}\), selecting position \(qt_i+i\) for letter \(a_i\).

If \(k=1\) or \(r=q-1\), *every* choice of these indices is a smallest attractor. Otherwise (\(k\ge2\), \(r\le q-2\)), the choice is a smallest attractor **if and only if** it intersects at least one occurrence of the single factor
\[
C_r=a_{q-1}a_0a_1\cdots a_r.
\]
Equivalently, precisely the selections satisfying all three conditions
\[
t_{q-1}=k-1,\qquad t_r=0,\qquad t_i\in\{0,k\}\quad(0\le i<r)
\]
are *not* attractors. (When \(r=0\), the last condition is vacuous.) Consequently the number of distinct smallest attractors is exactly
\[
A(q,k,r)=\begin{cases}
(k+1)^r k^{q-r},& k=1\ \text{or}\ r=q-1,\\
(k+1)^r k^{q-r}-2^r k^{q-r-2},&k\ge2,\ 0\le r\le q-2.
\end{cases}
\]
In particular, at complete periods (\(r=0\), \(k\ge2\)) the count \(k^q-k^{q-2}\) gives the exact fraction \(1-k^{-2}\) of one-occurrence-per-letter selections, independently of the alphabet size. The special binary complete-period count \(k^2-1\) was reported separately before; the theorem here treats arbitrary alphabets and *all* truncated prefixes, and identifies the unique distinguishing factor.

## Assumptions and scope
Letters \(a_0,\ldots,a_{q-1}\) are pairwise distinct and positions run from \(0\) to \(qk+r-1\). A factor is contiguous, not a scattered subsequence. A factor's occurrence is an interval, and a set attracts the factor if at least one occurrence interval meets the set. The theorem concerns every integer \(q\ge2\), \(k\ge1\), and \(0\le r<q\). It makes no assertion for period blocks with repeated letters or for arbitrary nonperiodic words.

## Proof
**1. Size and normalization.** Each singleton letter \(a_i\) is a factor, so an attractor needs at least one position carrying each of the \(q\) letters. A size-\(q\) set therefore selects exactly one occurrence per letter, with position \(qt_i+i\) and the stated range. We prove which of these selections work; at least one always works (choose all \(t_i=0\), except that the forbidden condition cannot hold for \(k\ge2\)).

**2. A missing-factor lemma.** Fix any factor \(U\) of length \(L\), and let its first occurrence start at \(s\) with \(0\le s<q\). This follows from the injectivity of the period block: distinct first letters fix the starting residue. All occurrences of \(U\) start at \(s+qj\) for consecutive integers \(0\le j\le h\), where \(h=\lfloor(qk+r-s-L)/q\rfloor\ge0\). Suppose a size-\(q\) selection fails to intersect *every* occurrence of \(U\). We show that necessarily \(k\ge2\), \(r\le q-2\) and that its indices satisfy the three displayed forbidden conditions.

First take \(L<q\). If \(s+L\le q\), the factor does not wrap around a period boundary. Its last letter \(a_{s+L-1}\) is present in every complete occurrence of the period block; if it also occurs in the truncated final suffix, then either the entire factor occurs there or its index is at least \(r\) and so has no additional occurrence. Thus the selected occurrence of that last letter belongs to an occurrence of \(U\), contradiction. More explicitly, if \(s+L\le r\) the factor also occurs in the final suffix; if \(s+L>r\), its last letter has no final-suffix occurrence.

Otherwise \(s+L>q\). Write \(t=s+L-q\), with \(1\le t<q\). If \(t\le r\), \(U\) occurs starting in *every* one of the \(k\) full cycles, so every occurrence of letter \(a_{q-1}\) lies inside some occurrence of \(U\), contradiction. Hence \(t>r\). In this case exactly \(k-1\) occurrences start at \(s,s+q,\ldots,s+q(k-2)\); because \(U\) exists, \(k\ge2\). Their intervals cover positions of \(a_{q-1}\) in cycles \(0,\ldots,k-2\), so avoiding them forces \(t_{q-1}=k-1\). They also cover positions of each \(a_i\) with \(0\le i<t\) in cycles \(1,\ldots,k-1\). Since \(r<t\), the choice for \(a_r\), which has no extra copy, is forced to cycle zero: \(t_r=0\). For every \(0\le i<r\), only cycles zero and \(k\) lie outside all these intervals, hence \(t_i\in\{0,k\}\).

Now take \(L\ge q\). Consecutive occurrences of \(U\) overlap or touch, so their union is the interval \([s,E]\), with \(E=s+qh+L-1\). By maximality of \(h\), the number \(b=qk+r-1-E\) of excluded positions at the right satisfies \(0\le b<q\). Thus every selected position would have to belong either to the initial segment \([0,s-1]\) or to the terminal segment of length \(b\). The initial segment contains no \(a_{q-1}\). If \(b\le r\), the terminal segment consists solely of the final partial-cycle letters among \(a_0,\ldots,a_{r-1}\), so also contains no \(a_{q-1}\), impossible. Therefore \(b>r\), implying \(r\le q-2\). The terminal segment then consists of all \(r\) extra letters followed backwards by \(b-r\) letters from the last complete block; these latter letters have indices at least \(q-(b-r)>r\). Hence the only occurrence of \(a_{q-1}\) in the complement is its last full-cycle occurrence and \(t_{q-1}=k-1\). The letter \(a_r\) cannot appear in that terminal segment; it must come from the initial segment, so \(s>r\) and \(t_r=0\). For \(i<r\), positions in the complement can come only from the first cycle or the final partial cycle, yielding \(t_i\in\{0,k\}\). Again these restrictions entail \(k\ge2\): when \(k=1\), any factor of length \(L\ge q\) has \(b=q+r-s-L\le r\), contrary to \(b>r\).

Thus any non-attractor among the one-per-letter selections must satisfy the three forbidden restrictions. When \(k=1\) or \(r=q-1\), they cannot occur, proving that all choices work.

**3. The single certificate and enumeration.** Suppose \(k\ge2\) and \(r\le q-2\). The factor \(C_r=a_{q-1}a_0\cdots a_r\) has exactly \(k-1\) occurrences, beginning at positions \(q-1+qj\) for \(0\le j\le k-2\). They cover the \(a_{q-1}\) positions in cycles \(0,\ldots,k-2\), every \(a_r\) position except its first, and every \(a_i\), \(i<r\), except its first and extra-final occurrences. The other letters do not occur in \(C_r\). Consequently \(C_r\) is not attracted exactly under the three forbidden restrictions. Together with Step 2, this shows that attracting \(C_r\) is necessary and sufficient for attracting *every* factor among size-\(q\) selections.

There are \((k+1)^r k^{q-r}\) possible selections. Under the forbidden restrictions, the last letter and letter \(a_r\) each have one choice, the first \(r\) letters each have two choices, and the remaining \(q-2-r\) letters each have \(k\) choices. The subtraction \(2^r k^{q-r-2}\) follows. This proves the exact count and the statement on minimum size. \(\square\)

## Verification
The accompanying standalone program `attractor_certificate.py` independently constructs the occurrence-coverage mask of *every distinct nonempty factor* and compares direct attractor truth values with the closed-form exceptional-condition test, for every possible selection in 108 parameter triples. It checks \(117132\) candidate sets across alphabets of \(2\) to \(6\) symbols, full-cycle counts \(1\) to \(4\), plus extended cases for \(3\) and \(4\) symbols up to \(8\) cycles. It independently compares enumerated counts with the formula. This finite experiment is corroboration, not a substitute for the quantifier-uniform proof above.

Run with Python 3: `python3 attractor_certificate.py`. No third-party packages are required.

## Relationship to prior work
The concept of string attractors and the alphabet-size lower bound are established in the foundational literature. Gheeraert, Romana, and Stipulanti's 2023 work constructs small attractors for families of morphic fixed points, and a 2022 study of episturmian sequences establishes minimum size for their factors. Banbara and collaborators (2026) explicitly study *all* minimum attractors for Fibonacci and period-doubling words rather than only their size. Their inspected statements address different word families. The previously published count of \(k^2-1\) minimum attractors for the complete-period binary word \((01)^k\) is exactly the \(q=2,r=0\) instance here; neither that special case nor minimum size \(q\) is asserted as independently new. The asserted contribution is the universal-prefix classification for arbitrary \(q\), the explicit one-factor test, and the partial-period count.

## Limitations
The theorem is for injectively labeled period blocks and ordinary finite-word attractors. No characterization is claimed for arbitrary periodic blocks with repeated symbols. The independent mathematical assessment has not been carried out; novelty remains subject to possible unindexed equivalent literature. Finite checks do not establish the infinite theorem on their own.

## References
1. F. Gheeraert, G. Romana, M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647 (first posted 2023-02-27), especially §§2, 4, 6; primary MSC2020 68R15. https://arxiv.org/abs/2302.13647
2. L. Dvořáková, *String attractors of episturmian sequences*, arXiv:2211.01660 (2022). https://arxiv.org/abs/2211.01660
3. M. Banbara et al., *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33. https://doi.org/10.4230/LIPIcs.CPM.2026.33
4. N. Prezza, *String Attractors*, arXiv:1709.05314 (2017), and D. Kempa, N. Prezza, *At the Roots of Dictionary Compression: String Attractors* (STOC 2018). https://arxiv.org/abs/1709.05314
