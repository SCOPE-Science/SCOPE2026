# Scientific assessment

## Correctness — PASS

The mathematical claim is one complete antichain classification for \(w=0^a1^b0^c1^d0^e\) and its exact enumeration. The proof establishes a complete run-count cutoff: every word with at least six runs contains the absent proper subsequence \(10101\); the five-run candidates are exhausted by their starting symbol; one- through four-run candidates are classified by explicit embeddability rectangles or coordinate boxes and deletion tests. This proves exactly seven unconditional and six conditional, distinct elements for all positive parameters. Enumerating the three interior threshold statuses gives the rational generating function and exact fixed-length distribution. The standalone direct-subsequence checker confirms all 3125 positive tuples up to five per run, 79 selected larger tuples, and histograms for 26 total lengths; no finite experiment is used as the infinite proof.

## Originality — PASS with stated risk

The relevant sections of Kosche–Koß–Manea–Siemer, *Absent Subsequences in Words* (arXiv:2108.13968), describe general MAS structure and enumeration but do not state the exact symbolic five-run antichain, its 13-element threshold, or its rational length distribution. Adamson et al. (arXiv:2407.18599) count all absent subsequences at given lengths, not the minimal antichain in a fixed-run family. Manea et al. (arXiv:2504.21471) focus on efficient enumeration of MAS/SAS on generic inputs. A generic enumerator's ability to compute each specialized case is not itself the closed structural formula. This evidence supports best-knowledge originality, not proof of absence from all literature; equivalent unindexed specialized work remains possible.

## Mathematical value — PASS

Minimal absent scattered subsequences form a finite obstruction basis for the downward-closed subsequence language of a string. Run-length encoding is a standard compressed representation, and five runs are the first configuration in this line of analysis with two separated one-runs flanked on both sides by zeros. The complete parameter-uniform obstruction list, exact sharp cardinality 13, interior-threshold phenomenon and closed length distribution are mathematically motivated finite-structure results rather than an arbitrary small census, routine reformulation, or unsupported numerical improvement.

## Residual limitations

No theorem is asserted for larger run counts. The exact family depends on the initial symbol being zero (complementation gives the other orientation); all five lengths are positive. The literature inspection was restricted to accessible relevant full-text sections and cited near results, so unknown equivalent specializations cannot be excluded. General all-parameter correctness rests on the written proof, not solely on tests.

Self-review: passed. Independent audit: not yet performed.
