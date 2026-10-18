# Exact constant-composition capacity for single adjacent-transposition detection

## Finding
For integers \(q\ge2\) and \(n\ge1\), write \(\Sigma_q=\{0,1,\dots,q-1\}\). A subset \(C\subseteq\Sigma_q^n\) is **single-adjacent-transposition detecting** if distinct codewords never differ by swapping two adjacent *unequal* letters once. Let \(D_q(n)\) be the maximum size of such a code. Then
\[
D_q(n)=\frac{q^n+q^{\lceil n/2\rceil}}2.
\]
The code consisting of all words with an even number of inversions is optimal for every \(q,n\).

The stronger constant-composition statement determines the optimum in every prescribed symbol-content class. For \(\boldsymbol r=(r_0,\ldots,r_{q-1})\in\mathbb Z_{\ge0}^q\) with \(\sum_i r_i=n\), let
\[
M(\boldsymbol r)=\frac{n!}{\prod_i r_i!},\quad m=\lfloor n/2\rfloor,
\]
and define
\[
F(\boldsymbol r)=\begin{cases}
\displaystyle\frac{m!}{\prod_i\lfloor r_i/2\rfloor!},&\text{if at most one }r_i\text{ is odd},\
0,&\text{otherwise}.
\end{cases}
\]
Because the coordinate sum equals \(n\), the permitted case means all counts are even when \(n\) is even, and exactly one count is odd when \(n\) is odd. The maximum size among codes with content \(\boldsymbol r\) is exactly
\[
D(\boldsymbol r)=\frac{M(\boldsymbol r)+F(\boldsymbol r)}2.
\]
In particular, these two formulas hold without a restriction that every alphabet letter occur.

## Assumptions and scope
The alphabet has a fixed total order and contains \(q\) letters. The channel introduces **at most one nontrivial adjacent transposition**: swapping two unequal neighboring symbols produces a changed received word; swapping equal symbols is a null event and is not an error. Detection means that such an erroneous output is never itself a *different* codeword. This is not correction: output neighborhoods of different words may overlap outside the code. The content vector counts occurrences of each letter and is invariant under swaps.

For \(w=(w_1,\ldots,w_n)\), let \(\operatorname{inv}(w)=|\{(i,j):i<j,\ w_i>w_j\}|\). Define the even and odd vertex sets \(E,O\) by inversion parity. The adjacent-swap graph has one vertex for each word and an edge for each one-swap pair of distinct words. Each constant-content class is an induced union of its edges.

## Proof
**Step 1 (two-coloring).** Swapping adjacent unequal symbols changes \(\operatorname{inv}\) by exactly one in absolute value: only their relative order changes. Therefore every graph edge joins \(E\) to \(O\). Taking all even-inversion words gives a detecting code, in total and in each content class.

**Step 2 (explicit matching saturating the odd side).** Set \(m=\lfloor n/2\rfloor\). Designate the disjoint neighboring pairs of positions \((1,2),(3,4),\ldots,(2m-1,2m)\). For each word with at least one designated pair containing two unequal symbols, find the *first* such pair and interchange those two letters. Call the result \(T(w)\). The same pair is still first unequal after this interchange, so \(T(T(w))=w\). Moreover, \(w\) and \(T(w)\) are adjacent in the graph and have opposite inversion parity. As all swaps occur within the designated pair, the matching preserves the content vector.

A word is unmatched precisely when every designated pair consists of identical letters (with one arbitrary final letter if \(n\) is odd). Such a word has even inversion parity: each inversion contributed by two different doubled pairs appears four times, and each inversion between a doubled pair and the optional last letter appears twice. Within a doubled pair there is none. Thus **every odd vertex is matched**, with its partner even. An independent set contains at most one endpoint of each matched edge and at most all remaining even vertices, hence has size at most \(|E|\). The even side attains this bound, both globally and within each content class.

**Step 3 (count unmatched words at a fixed content).** The number of vertices of content \(\boldsymbol r\) is \(M(\boldsymbol r)\). Unmatched words require each designated pair to be monochromatic. For even \(n=2m\), this is possible exactly when every count is even, in which case assigning the \(m\) doubled symbols in sequence produces \(m!/\prod_i(r_i/2)!\) words. For odd \(n=2m+1\), the final single letter must be the sole symbol with odd count; then the remaining \(m\) pairs may be filled in \(m!/\prod_i\lfloor r_i/2\rfloor!\) ways. In all other cases there are no unmatched words. Thus there are exactly \(F(\boldsymbol r)\) unmatched words.

Every non-fixed orbit of \(T\) consists of one even and one odd vertex. As all fixed words are even, \(|E|=(M+F)/2\) on each content class, proving the constant-composition formula.

**Step 4 (sum over compositions).** There are \(q^n\) words total. Each of the \(m\) designated pair-values may be chosen independently from \(q\) letters, and the final single letter (if present) independently as well; hence exactly \(q^{\lceil n/2\rceil}\) words are unmatched. Applying the same orbit count yields the claimed formula for \(D_q(n)\). This covers the boundary \(n=1\), where there are no nontrivial swaps and all \(q\) words are valid.

## Verification
The included standalone standard-library program `checker.py` independently constructs the adjacent-swap graph in each content class. It computes a maximum bipartite matching by an augmenting-path algorithm **without using the theorem's designated-pair involution**, and uses the equality \(\alpha=|V|-\nu\) for bipartite graphs as a finite graph-theoretic check. The checker directly enumerates inversion parity and compares the predicted counts with graph optima for all cases \(q=2\), \(1\le n\le9\); \(q=3\), \(1\le n\le7\); and \(q=4\), \(1\le n\le5\). It also verifies that the displayed even code contains no adjacent pair. The finite tests corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
The prior literature on adjacent transpositions emphasizes **correcting** one or more errors, sometimes jointly with deletion, insertion, or substitution. Wang–Vu–Tan's publicly released 2023 preprint explicitly corrects adjacent transpositions jointly with asymmetric deletions; its theorem statements do not determine detection-only maximal code sizes. Khuat–Kim's 2023 q-ary construction corrects one edit or adjacent transposition and does not report the detection-only exact optimum. Earlier work by Abdel-Ghaffar considers **joint detection** of substitutions and transpositions, a strictly more restrictive admissibility condition. Its accessible abstract states bounds for that joint model, which neither imply nor refute this optimum for transpositions alone; full-text overlap with the present statement remains an outstanding source-access uncertainty.

The signed enumeration of multiset permutations by inversion number is classical; the q-multinomial polynomial already encodes the parity split (NIST DLMF §26.16). The claim here is the **independent-set optimum for the single-swap detection channel** and its exact type-wise formula, justified by a saturating explicit matching; no novelty is claimed for inversion parity or Gaussian multinomial enumeration in isolation.

## Limitations
The result concerns **detection** of exactly one possible adjacent swap of unequal symbols. It does not give correction of one transposition; it does not handle a simultaneous set of disjoint swaps, a nonadjacent transposition, substitution, deletion, or insertion. Every bound is exact for the stated model, not for broader error channels. The literature comparison was limited by unavailable full text of an older plausible source; an unindexed or unretrieved equivalent detection-only statement cannot be excluded. No independent validation has been conducted.

## References
1. S. Wang, V. K. Vu, V. Y. F. Tan, *Codes for Correcting Asymmetric Adjacent Transpositions and Deletions*, arXiv:2301.11680, first publicly submitted 27 January 2023; https://arxiv.org/abs/2301.11680 .
2. T.-H. Khuat and S. Kim, *Novel q-ary Code Design for One Edit or Adjacent Transposition Error*, IEEE Open Journal of the Communications Society 4 (2023), 2830–2837, doi:10.1109/OJCOMS.2023.3327435.
3. K. A. S. Abdel-Ghaffar, *Detecting Substitutions and Transpositions of Characters*, The Computer Journal 41 (1998), 270–277, doi:10.1093/comjnl/41.4.270 (abstract inspected; complete text unavailable).
4. NIST Digital Library of Mathematical Functions, §26.16, *Multiset Permutations*, https://dlmf.nist.gov/26.16 .
