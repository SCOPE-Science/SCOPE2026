# Scientific review of the order-five CR-discrepancy classification

## Correctness: PASS
All sixteen-bit Boolean feedback tables are enumerated, and a short bijection establishes that the accepted tables correspond one-to-one to binary order-five de Bruijn rotation classes. The circular discrepancy equals the range of prefix sums because every de Bruijn period is symbol-balanced. Canonical rotation comparisons measure the action of complement and reversal exactly. The resulting 2,048 cycles split into 64 reverse-complement-fixed and 1,984 other classes; the orbit count follows by exact group-size division. A separate enumeration through anti-palindromic half-words independently reproduces all four CR-fixed discrepancy cells, providing corroboration of the central classification.

## Originality: PASS with priority risk
Chang--Wang's original full-text CR characterization and divisibility result contain no discrepancy-by-symmetry spectrum; Gabric--Sawada's discrepancy paper and the minimum-discrepancy work of Álvarez and colleagues do not state these CR-conditioned frequencies. Earlier calculations already contained the marginal order-five histogram and the minimal-discrepancy group-orbit split; both are credited. The additional joint cells at discrepancy six through eight and the complete group-orbit distribution are not consequences of those previously known marginals, and exact comparisons yielded no matching statement. Unindexed equivalent numerical enumerations remain a genuine priority risk.

## Mathematical value: PASS
Two separately motivated properties of de Bruijn cycles—low cyclic symbol imbalance and reverse-complement symmetry—are classified jointly at the first nontrivial odd order supporting a mixed discrepancy spectrum. The exact result reveals that 16 of the 64 symmetry-constrained cycles attain the optimum, while the unrestricted optimum comprises 224 of 2,048 cycles. The complete table also determines all orbit types at nonoptimal values, supporting precise selection and benchmarking of balanced symmetry-constrained sequences. It is a naturally specified finite complete classification, not a sample, a renamed bound, or an arbitrarily chosen witness count. No extension to arbitrary orders is claimed.

## Boundary and literature
The theorem applies only to binary order-five cycles up to rotation, with circular absolute symbol discrepancy and the complement/reversal symmetry group. It does not subsume earlier work on existence, minimum discrepancy, or feedback constructions, and it does not establish larger-order distributions. Sources: Chang--Wang arXiv:2408.01794; Gabric--Sawada arXiv:2005.01638; Álvarez et al. arXiv:2407.17367. Exact programs `verify_fsr.py` and `verify_halfwords.py` provide reproducible finite certificates.

Self-review: passed. Independent audit: not yet performed.
