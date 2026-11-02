# Sharp two-marker systematic permutation-invariant single-deletion codes for three and four information symbols

## Finding

A full-systematic permutation encoder with \(n\) information symbols and \(r\) distinct redundancy markers is an injective map \(E:S_n\to S_{n+r}\) such that deleting the symbols \(n+1,\ldots,n+r\) from \(E(\pi)\) recovers \(\pi\) in its original order. A permutation-invariant deletion (PID) deletes one coordinate and standardizes the surviving symbols to their ranks. Define \(r_{\mathrm{PID}}(n)\) as the least \(r\) for which the PID-deletion sets of the \(n!\) encoded words are pairwise disjoint.

Then
\[
\boxed{r_{\mathrm{PID}}(2)=1,\qquad r_{\mathrm{PID}}(3)=r_{\mathrm{PID}}(4)=2,\qquad r_{\mathrm{PID}}(n)\ge 2\ \text{for every }n\ge3.}
\]
In particular, six length-five and twenty-four length-six codewords suffice to encode every permutation of three and four data symbols, respectively, and correct any single PID. Explicit complete codebooks are in `codebooks.json`.

## Assumptions and scope

The alphabet labels are \(1,\ldots,n+r\). Redundancy markers have fixed labels \(n+1,\ldots,n+r\), may be interleaved with the data symbols, and each label occurs exactly once. The receiver sees the standardized length-\(n+r-1\) permutation after exactly one deletion; allowing zero or one deletion makes no difference because output lengths distinguish the cases. This is not the symbol-invariant deletion channel, which retains surviving labels. The result gives an all-length lower bound and exact minimum marker counts only for \(n=2,3,4\).

## Proof

For a permutation \(w=(w_1,\ldots,w_m)\), let
\[
D(w)=\left\{\operatorname{std}(w_1\cdots w_{j-1}w_{j+1}\cdots w_m):1\le j\le m\right\},
\]
where \(\operatorname{std}\) replaces each entry by its rank among the remaining entries. If the outputs after deleting adjacent positions \(j\) and \(j+1\) agree, their shared positions except one have identical entries, while that position contains respectively \(w_{j+1}\) and \(w_j\). Their standardized patterns agree if and only if there is no other entry strictly between these values. As every value in \([m]\) appears, this is equivalent to \(|w_j-w_{j+1}|=1\).

Consequently, if \(|D(w)|=1\), the preceding condition holds at every adjacent pair. The sequence \(w\) is a Hamiltonian path in the path graph \(1-2-\cdots-m\), and hence \(w\) must be the increasing or decreasing permutation. Conversely, both monotone permutations have a singleton PID-deletion set. Thus precisely two length-\(m\) permutations have singleton deletion sets, for every \(m\ge2\).

If \(r=1\), the full-systematic code contains \(n!\) words of length \(n+1\), all with nonempty deletion sets in \(S_n\), which has only \(n!\) elements. Pairwise disjointness forces every encoded word to have a singleton deletion set; only two candidate codewords exist. When \(n\ge3\), \(n!>2\), contradiction. For \(r=0\), there are \(n!\) information words but only \((n-1)!\) possible standardized one-deletion outputs, so correction is impossible for every \(n\ge2\).

For \(n=2\), the encoder \(12\mapsto123\), \(21\mapsto321\) has disjoint PID-deletion sets; the \(r=0\) lower bound makes it optimal. For \(n=3\), use the six words `14532`, `21345`, `23154`, `43251`, `45123`, `53142`; after removing markers `4`, `5`, they yield all six messages once each. Their eighteen distinct standardized one-deletion outputs are mutually disjoint across codewords. For \(n=4\), the twenty-four words in `codebooks.json` yield each of the twenty-four messages once upon removal of markers `5`, `6`. Their PID-deletion sets have total union size ninety, with no output shared by distinct codewords. The explicit exhaustive checker independently computes these ranks in two ways and tests disjointness. These codebooks establish \(r=2\) for \(n=3,4\), matching the universal lower bound.

## Verification

Run `python3 verify.py` in the directory containing `codebooks.json`. It uses only the Python standard library, checks full systematicity, all permutations and messages, two independent standardization algorithms, and all distinct PID outputs. The saved `verification_output.txt` reports six and twenty-four codewords, eighteen and ninety distinct outputs, and `VERIFY_OK`. The same program directly corroborates the singleton-deletion lemma and the adjacent-deletion equivalence for every permutation of lengths three through seven; the general assertion is established by the preceding graph argument, not by this finite test.

## Relationship to prior work

Wu, Bui, Niu, Vu and Wang (2026) formulate full-systematic permutation deletion codes and provide an asymptotic construction with four markers for one PID. Their stated sufficiently-large-length results do not give the exact minimum at information lengths three or four or the present two-marker codebooks. Gao and Shum (2024), following Levenshtein, establish perfect single-deletion codes in the label-preserving SID model; they do not imply PID correction because standardization identifies different surviving-label sequences. Gabrys and collaborators (2016) establish the deletion channel models and general constructions without the stated exact full-systematic short-length optimization in the material accessible for comparison.

## Limitations

The exact two-marker upper bound is certified only for information lengths three and four. No two-marker construction for arbitrary information length, efficient large-length encoder, full enumeration of all optimal encoders, or independent publication-priority certification is claimed. The lower bound applies to every information length at least three. The 2016 journal article was not available in full for comparison, so unindexed or inaccessible equivalent finite constructions remain a residual priority risk.

## References

1. B. Wu, Q. D. Bui, K. Niu, V. K. Vu and S. Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, arXiv:2609.37578v1, first submitted September 29, 2026. https://arxiv.org/html/2609.37578v1
2. M. Gao and K. W. Shum, *Efficient encoding and decoding algorithm for a class of perfect single-deletion-correcting permutation codes*, arXiv:2411.08258, first submitted November 13, 2024. https://arxiv.org/abs/2411.08258
3. R. Gabrys et al., *Codes Correcting Erasures and Deletions for Rank Modulation*, IEEE Transactions on Information Theory 62 (2016), 136–150. https://doi.org/10.1109/TIT.2015.2493147
