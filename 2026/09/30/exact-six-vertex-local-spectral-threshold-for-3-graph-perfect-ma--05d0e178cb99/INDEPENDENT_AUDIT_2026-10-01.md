# Independent mathematical audit — Exact six-vertex local spectral threshold for 3-graph perfect matchings

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** On six vertices, a perfect matching is exactly a complementary pair of triples, so matching-free families are parameterized by 59,049 independent complementary-pair choices. The inspected exact verifier compares every five-vertex link spectral radius with two by testing positive semidefiniteness of two times the identity minus the adjacency matrix using exact principal minors and Bareiss elimination. The independent replay covered all 59,049 families, found none above the threshold, and found exactly 78 labeled equality cases. The inspected repository classifier canonicalizes those cases under all vertex permutations and asserts exactly five isomorphism types.

Checked sources: Assigned RESULT.md; artifacts/verify_psd.py; Independent replay of the exact threshold enumeration; Liu--O 2026.

Residual correctness risks: The repository also contains a separately implemented characteristic-polynomial check; it was not rerun in this audit..

## Originality

**PASS.** Liu and O prove the same threshold formula for sufficiently large orders divisible by three, with space-barrier extremals. The inspected main theorem does not assert the exact order-six result or its five equality types. No earlier six-vertex spectral classification was located.

### Equivalent formulations

Searches/sources: Published-record search for six-vertex triple-system perfect matching local link spectral threshold two; arXiv:2609.26832; Polcyn--Rucinski maximal intersecting triple systems.

Evidence: The exact archive match was the audited finite theorem. Liu--O Theorem 1.1 explicitly assumes sufficiently large order. Maximal intersecting classifications concern inclusion structure rather than this spectral statistic.

No equivalent order-six spectral result was found.

### Broader coverage

Searches/sources: Liu--O large-order exact threshold theorem; Maximal-intersecting six-vertex classifications.

Evidence: The Liu--O theorem leaves small orders outside its stated range. Maximal-family classification does not by itself determine the minimum link spectral radius over all subfamilies.

Neither inspected source dominates the finite threshold and equality classification.

### Exact database or table

Searches/sources: Published archive search for threshold two and five equality types; Search for six-vertex intersecting-hypergraph spectral tables.

Evidence: No earlier exact spectral table was located.

The audited computation evaluates a distinct spectral invariant rather than reproducing a known catalog value.

### Claim versus prior implication

Searches/sources: Substitute order six into the sufficiently-large Liu--O theorem; Infer equality types from maximal-intersecting classifications.

Evidence: An unspecified sufficiently-large hypothesis cannot be specialized to six. Spectral equality is not determined solely by maximality.

The exact enumeration is needed.

### Source inspections

- **Exact local spectral thresholds for perfect matchings in 3-graphs and 3-partite 3-graphs** — PRIMARY_PARTIAL_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2609.26832
  Trigger: Same parameter, matching problem and threshold formula.
  Material read: Pages 1 through 12 of the 39-page primary paper, including the abstract, Theorem 1.1, barriers, and initial stability lemmas.
  Method: authorized institutional full-text extraction after open-access text retrieval failed
  Evidence: The inspected theorem states the non-partite result only for sufficiently large order; later pages were not inspected.

Residual originality risks:
- Only pages 1 through 12 of the 39-page Liu--O paper were inspected, so a later remark could mention order six even though Theorem 1.1 itself is large-order.

## Scientific value

**PASS.** Order six is the first nontrivial order divisible by three. Determining the exact local-spectral threshold and every equality obstruction is a natural complete base case for the new large-order matching theory.

Residual value risks: No order-nine or stability theorem is claimed..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
