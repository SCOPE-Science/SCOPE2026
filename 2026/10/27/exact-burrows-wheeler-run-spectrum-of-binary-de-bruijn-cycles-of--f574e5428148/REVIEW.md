# Review of order-five de Bruijn BWT run spectrum

## Correctness — PASS

Every order-five de Bruijn word has exactly one prefix occurrence of each five-bit word. Splitting the sorted rotations into pairs sharing the first four bits forces each BWT pair to be `01` or `10`. The explicit inverse-permutation formula accounts for all 65,536 choices, with a one-cycle condition equivalent to one de Bruijn necklace. The 32-edge Euler-circuit recursion is a second, independent complete enumeration and produces precisely the same 2,048 canonical strings and run values. The run identity \(17+\sum_{i=0}^{14}[\epsilon_i=\epsilon_{i+1}]\) is checked algebraically and computationally. Smaller orders are exhausted separately, proving the first strict failure of the lower bound. The verifier and all dependencies are included.

## Originality — PASS, subject to a documented priority risk

Higgins' 2012 work derives the transform's binary pair-block structure and inverse-cycle correspondence: this **does** cover the structural lemmas, which are not claimed new. Neither the inspected presentation nor the inspected primary texts of Kucherov–Tóthmérész–Vialette (2012) and Fici–Gabory (2025) supply this precise order-five run-frequency polynomial or first-bound-failure assertion. Searches for aliases such as *BWT run count*, *run-length encoding*, *cyclic BWT*, and *de Bruijn transform spectrum* did not reveal a dominating exact table; search absence is not proof of priority. Reproducing the six coefficients is therefore the specific claimed addition. An unpublished, unindexed, or indirectly encoded preexisting run table remains a residual risk.

## Value — PASS

The number of runs is a natural compression statistic of the Burrows–Wheeler transform. De Bruijn cycles are maximally factor-diverse, making their BWT runs a direct measure of residual run-length compressibility. Order five is the first nontrivial obstruction to the elementary all-orders lower bound after orders two, three and four attain it. The complete six-value spectrum, exact multiplicities, and 38 extremizers are a finite, reproducible natural classification rather than a freely chosen numerical slice.

## Scope and status

The claim does not address larger orders, different alphabets, or whether another historical source already tabulated the result. Computational exhaustiveness follows from the mathematically justified finite representation, not from statistical sampling. The examination is not independent validation.

Self-review: passed. Independent audit: not yet performed.
