# Complete list-decoding capacity spectrum for the eight-bit three-deletion channel

## Finding
For every integer \(L\ge0\), define \(A_2(8,3;L)\) as the largest possible cardinality of a set \(C\subseteq\{0,1\}^{8}\) with the following property: every binary word of length five can be obtained by deleting exactly three symbols from at most \(L\) distinct codewords of \(C\). The full exact answer is

\[
A_{2}(8,3;L)=\left\lfloor\min\left\{256,\frac{10L+2}{3},\frac{13L+4}{4},3L+4,\frac{14L+50}{5},\frac{8L+44}{3},\frac{5L+47}{2}\right\}\right\rfloor.
\]

The six affine bounds in the formula change which one is smallest at \(L=4,12,30,35,53\). For example, the optimal cardinalities at \(L=1,2,3,4,8,12,30,35,53,93\) are respectively \(4,7,10,14,27,40,94,108,156,256\). All \(256\) eight-bit words can be selected if and only if \(L\ge93\).

## Assumptions and scope
Only finite binary strings of length exactly eight, exactly three coordinate deletions, distinct received subsequences, and a nonnegative integral list size \(L\) are considered. Deleting different triples of positions that produce the same five-bit received word counts only one compatibility relation between that received word and that codeword. There are \(256\) possible transmitted words and \(32\) possible received words.

Let \(a_{u,w}=1\) when the five-bit word \(u\) is an order-preserving subsequence of the eight-bit word \(w\), and zero otherwise. The model imposes \(\sum_{w\in C}a_{u,w}\le L\) for every received word \(u\).

## Proof
**Upper bounds.** The certificate file `three_deletion_capacity_cert.json` supplies six vectors \(y^{(j)}\in\mathbb Q_{\ge0}^{32}\). For each vector set
\[
z^{(j)}_w=\max\left\{0,1-\sum_{u}a_{u,w}y^{(j)}_u\right\}
\qquad(w\in\{0,1\}^{8}).
\]
Then \(\sum_u a_{u,w}y^{(j)}_u+z^{(j)}_w\ge1\). For any feasible code \(C\), summing over its codewords gives
\[
|C|\le L\sum_u y^{(j)}_u+\sum_w z^{(j)}_w.
\]
Exact rational arithmetic gives the six slope/intercept pairs
\[
\left(\frac{10}{3},\frac23\right),\quad
\left(\frac{13}{4},1\right),\quad(3,4),\quad
\left(\frac{14}{5},10\right),\quad
\left(\frac83,\frac{44}{3}\right),\quad
\left(\frac52,\frac{47}{2}\right).
\]
The trivial cardinality bound \(|C|\le256\), together with integrality, gives the asserted upper envelope. Every dual inequality and exact coefficient sum is checked by the standalone verifier without optimization software.

**Matching constructions for every finite intermediate list size.** For each integer \(1\le L\le93\), `three_deletion_capacity_cert.json` contains the full selected set of length-eight codewords as lexicographic integers from \(0\) to \(255\). The standalone verifier constructs the entire incidence matrix from the definition, computes the number of selected codewords compatible with each of the \(32\) five-bit outputs, verifies that none exceeds \(L\), and checks that the number selected equals the integer part of the upper envelope. These are explicit finite witnesses, not claims inferred from a black-box optimization log. Thus the upper bound is attained for all \(93\) intermediate allowances.

**Endpoints.** For \(L=0\), any nonempty code would have a deletion output, so the empty code is optimal. Direct enumeration of the same \(32\times256\) incidence matrix gives exactly \(93\) compatible length-eight supersequences for each received five-bit word. Therefore for \(L\ge93\), all \(256\) length-eight words form a permissible code. This covers every integer \(L\ge0\).

## Verification
With Python 3 (standard library only), run

`python3 verify_three_deletion_profile.py three_deletion_capacity_cert.json`

The verifier reconstructs all distinct order-preserving length-five subsequences of all \(256\) eight-bit words, recomputes every dual slack as a nonnegative exact rational, checks the six rational slope/intercept identities, verifies all \(93\) explicit codebooks, and checks the endpoints. Expected terminal line:

`VERIFY_OK n=8 deletions=3 dual_lines=6 explicit_witnesses=93; exact capacity for every integer list size L>=0`

The certificate records six complete \(32\)-coordinate dual vectors and \(93\) separate codeword lists; no external optimizer is required to verify any claim.

## Relationship to prior work
Lin's 2026 treatment of all list-decodable deletion codes defines precisely the same \(k\)-deletion and list-size model and gives general asymptotic lower bounds, using deletion hypergraphs and common-supersequence estimates [1]. Its inspected full text gives no exact all-list-size profile for the eight-bit, three-deletion instance. Kiah, Wei, and Zeng [2] give nonasymptotic finite-length list-deletion upper bounds, notably their Theorem 23, as well as asymptotic estimates; the relevant full-text sections do not state or imply this complete exact eight-bit capacity profile. An unindexed finite enumeration nevertheless remains a residual risk. Yasunaga [3] develops general bounds for insertion/deletion correcting codes; those results are not an exact finite \(32\times256\) three-deletion list-capacity table. This theorem is a certificate-supported finite-block classification, not an improvement to any asymptotic capacity bound.

## Limitations
Only block length eight and exactly three deletions are covered. The theorem gives no formula for other block lengths, other deletion budgets, or nonbinary alphabets. The result includes exact primal/dual witnesses that can be independently checked, but independent scientific review has not been performed. Earlier unindexed enumerations or finite tables could overlap with the claimed novelty.

## References
[1] Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first public September 22, 2026. https://arxiv.org/abs/2609.26650

[2] Han Mao Kiah, Hengjia Wei, and Ruixiao Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395v1, first public September 18, 2026. https://arxiv.org/abs/2609.21395

[3] Kenji Yasunaga, *Improved bounds for codes correcting insertions and deletions*, *Designs, Codes and Cryptography* 92 (2024), 1267--1278. https://doi.org/10.1007/s10623-023-01342-1
