# Review: exact weight-three nonadjacent pair decks

## Correctness

PASS. Every admissible profile determines the numbers of linear zero-runs and one-runs via its two diagonal pair counts. The proof enumerates the eight possible run-type signatures for exactly three ones and proves the complete support set of the remaining ordered \(01\) count for each type. The only missing interior values are an explicitly identified parity progression when both run counts equal two. The cardinality sum proves the exact two-branch formula for every \(n\ge8\), and finite enumeration establishes the shorter initial values. The supplied independently implemented `VERIFY.py` checked 1,663,740 source words across lengths through 80 and compared a literal-pair implementation through length 14. Finite computation corroborates but does not replace the symbolic proof.

## Originality

PASS, with priority risk. The original gapped-deck work of Golm–Nahvi–Gabrys–Milenkovic (https://arxiv.org/abs/2201.12671) gives the channel and shortest-collision bounds. Rigo–Stipulanti–Whiteland (https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf) characterize the general one-gap two-binomial equivalence and study factor-complexity functions for infinite words, but do not state the exact full fixed-weight-three image or parity-dependent run-type support. Chrisnata et al. (https://www.aimsciences.org/article/doi/10.3934/amc.2021032) study ungapped \(k\)-decks. A previously documented exact weight-two result addresses the same observation with only two markers, not the eight-state enumeration here. The existing general characterization is closely related, and independently unindexed equivalent enumeration remains possible.

## Mathematical value

PASS. The object is the full, naturally specified weight-three layer of a recognized gapped read channel. Its exact zero-error capacity changes linear coefficient by parity, and the complete run-type classification pinpoints which observational profiles are impossible. This supplies a sharp, reproducible finite-length benchmark: \(\Theta(n^3)\) sparse sources collapse to only \(\Theta(n)\) distinct measurement outputs, quantifying the information loss.

## Limitations

The theorem covers linear indexed binary words with exactly three ones and the full ordered nonadjacent pair multiset only. It does not cover circular words, other weights or larger gaps. No independent external proof or publication-priority audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
