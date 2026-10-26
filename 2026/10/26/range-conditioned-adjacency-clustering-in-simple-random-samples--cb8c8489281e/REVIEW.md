# Review: range-conditioned adjacency clustering

## Correctness — PASS

Conditional sample counting is exact, because the \(n-r\) admissible sample locations each contribute every interior binary word exactly once. Compositions of positive one- and zero-block lengths yield the complete conditional mass function. Every output word has the same \(z+1\) zero-deletion preimages, proving the insertion coupling preserves uniformity. Inserting a zero cannot create adjacent ones. Conditional means strictly decrease for \(k\ge3\); the \(k=2\) endpoint case is explicit. The double-copy covariance identity proves the asserted strict and weak signs. Exact exhaustive checks cover sizes up to 12; these checks do not replace the universal proof.

## Originality — PASS with residual priority risk

published-finding corpus searches for sample range, runs, conditioned adjacency counts, stochastic order and inserted zeros did not return a covering claim. The nearest related record, `SCOPE-exact-dependence-phases-of-fixed-composition-run-transitions-c6b28ad6d93d`, concerns covariances *between transition indicators* at fixed composition, not the global sample range or its conditional distribution. Smeeton and Cox (2003), inspected in full primary text, address shuffling-based fixed-composition runs tests, not conditioning on span. Stepanov (2011) studies runs from discrete order statistics; only its abstract was accessible, making it a continuing potential source of earlier implications. The finite law and monotone simultaneous coupling are not identified in the material actually reviewed. Absence from searches is not proof of worldwide priority.

## Mathematical value — PASS

The sample span is a natural measure of how far a simple random sample is spread, whereas adjacent selected pairs quantify clustering and are a primitive runs-test statistic. The result gives a complete distributional comparison, not just a sign of a single covariance, and enables monotone-tail calibration when sample range is observed. The independence of the ambient population size and the explicit pathwise zero-insertion construction provide reusable structural information. The theorem is confined to a motivated, fully specified finite sampling model.

## Literature and limitations

The potentially closest incomplete comparison is the full text of Stepanov (2011), inaccessible during this review. The exact run-count enumeration underlying classical binary runs tests is not claimed as new by itself; the additional span conditioning and first-order stochastic coupling are the asserted contribution. Independent historical-priority review is outstanding.

Self-review: passed. Independent audit: not yet performed.
