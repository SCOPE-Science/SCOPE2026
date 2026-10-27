# Scientific review

## Correctness — PASS

For arbitrary \(n\ge2\), the only possible weight-one deletion outputs of a word with ones at \(i<j\) are the singleton outputs at \(i\) and \(j-1\). The first and second cases coincide exactly when \(j=i+1\), proving the resource inequality \(L+2S\le n-1\). Consecutive starts of adjacent-one source words produce an identical weight-two deletion output, forcing \(L\le\lceil(n-1)/2\rceil\). These two inequalities imply the stated sharp bound. The explicit construction has disjoint singleton outputs by parity and disjoint weight-two outputs by gap and separated first-one positions. All boundaries including \(n=2\) are covered. The packaged `check.py` directly checks finite instances through length \(200\) and exhaustively optimizes lengths \(2\)–\(8\). These finite tests corroborate but do not establish the universal claim.

## Originality — PASS, with residual risk

Sloane (arXiv:math/0207197, §§1–2) treats unrestricted binary single-deletion codes and their graph representation; his optimum for an unrestricted graph cannot determine its weight-two induced subgraph's independence number. Cullina–Kulkarni–Kiyavash (arXiv:1211.4056, §§III–IV, especially Lemmas 8–9 and Theorem 5) obtain optimal proper colorings of constant-weight induced graphs, not their exact maximum independent sets. Their paper expressly distinguishes coloring optima from independent-set optima. The inspected statements neither state nor imply the claimed sharp all-length weight-two optimum. No close equivalent emerged from targeted semantic and public-literature searches. An unindexed earlier equivalent formula remains a real residual priority risk; this review does not establish historical uniqueness.

## Value — PASS

Exact maximum sizes of codes protecting against deletion are fundamental finite-length parameters. Weight one is degenerate because every source has the same all-zero deletion output; weight two is the first nontrivial constant-weight slice. The theorem replaces a general graph optimization problem by a sharp all-length formula and an explicit optimum with a constant-size local pattern, showing a linear rather than quadratic packing capacity. It is a natural infinite classification, not a numerical table or a routine specialization of an unrestricted bound.

## Scope

The result does not assert an optimum for unrestricted words, alternative error models, multiple deletions, or all optimal codebooks. It includes no independent external certification.

Self-review: passed. Independent audit: not yet performed.
