# Independent audit — 2026/09/12/064
Assigned/current tree: `4d700058345d314a145efc768cb9b2ee24ee5720`  
Disposition: **repaired**

## Correctness

Both printed rotation systems have 13 faces with lengths eleven 4s and two 6s, hence genus 3, the Ringel minimum. Independent brute force over all 24·5040 bipartition-preserving relabellings finds no orientation-preserving isomorphism between E1 and E2. Exhaustive single-row replacement tests reproduce exactly 45 genus-3 replacements per witness after excluding the identical row, and all 45 are nontrivial cyclic shifts of the same row; there are zero genus-3 non-shift replacements. Therefore both isomorphism classes are isolated under the record’s explicitly defined move, so that reconfiguration graph is disconnected.

## Originality

Grannell–Knor already enumerated nonisomorphic minimum-genus embeddings of K(4,7), so the existence of many K(4,7) minimum-genus classes is not new. Focused search did not locate the specific graph whose move is arbitrary reordering of one vertex rotation while preserving minimum genus. The novelty, if any, is therefore only the isolation/reconfiguration property under this custom move.

## Scientific value

Two exact isolated vertices give a clean disconnectedness certificate for the stated reconfiguration graph. The broader sampled-census claims in the original record are unnecessary and were not reproducible from the committed package, so they are removed.

## Independent checks

- Independent face tracing: both E1 and E2 have 13 faces with lengths 4^11,6^2.
- Brute force over all 120960 bipartition-preserving relabellings found E1 and E2 non-isomorphic.
- For each witness, exhaustive 20317 single-row replacements found 45 genus-3 replacements, all cyclic shifts, and zero non-shift neighbours.

## Limitations

- The move called a flip here is a custom single-vertex cyclic-order reordering, not the standard diagonal flip of a surface triangulation.
- The referenced output/artifacts/witnesses.json and verify_final.py are absent from the audited Git tree.
- The audit independently recomputed the witness properties from the rotations printed in RESULT.md; the original approximate wider census is removed.
- No exact component count for the full reconfiguration graph is claimed.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/064
- https://grannell.net/Papers/kmn.pdf
- https://doi.org/10.37236/10292
