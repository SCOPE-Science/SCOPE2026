# Independent mathematical audit — Exact small-order 3-union-free triple systems through nine vertices

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The fixed-pair construction is union-free because the union records exactly which outside vertices were selected. Heredity reduces the upper bound to excluding a family with one more edge after fixing a first edge by symmetry. The inspected verifier stores exactly every union created by one-, two-, or three-edge subfamilies, so its pruning criterion is logically equivalent to preserving the required injectivity. An independent replay for orders four through nine found no fixed-edge family of size n minus one and exactly three fixed-edge extremals of size n minus two at every order. Incidence double counting then yields exactly one pair-star type and the stated labeled counts.

Checked sources: Assigned RESULT.md; artifacts/verify_unionfree.py; Independent exact replay for all six orders; Liu--Shangguan--Zhang 2024 and 2026.

Residual correctness risks: The upper bound is computer-assisted finite mathematics; this audit reran the Python implementation but not the repository's independent C++ implementation..

## Originality

**PASS.** Current uniform union-free work explicitly leaves the parameter regime containing this invariant outside its general asymptotic theorem and records superlinear eventual growth. Targeted searches found no earlier exact table or equality classification for orders four through nine.

### Equivalent formulations

Searches/sources: Published-record search for three-union-free triples through order nine; Search under three-separable constant-weight codes; arXiv:2411.07908 and arXiv:2605.11949.

Evidence: The exact archive match was the audited theorem. The union-free papers use the same union-injectivity condition. The nearby weight-three two-cover-free theorem concerns a weaker predicate.

The cover-free packing number is not equivalent to the stricter union-free invariant.

### Broader coverage

Searches/sources: Liu--Shangguan--Zhang uniform union-free theorem; Published exact weight-three two-cover-free theorem.

Evidence: The 2026 theorem lists the relevant three-uniform, three-union regime as exceptional. Two-cover-free does not imply three-union-free; the Fano-plane example separates them.

No inspected broader theorem covers these six exact values.

### Exact database or table

Searches/sources: Published archive exact search for the first six values; Search under separable-code and uniquely-decodable union terminology.

Evidence: No earlier finite table was located in the searched corpus.

The exact census is not tied to an identified pre-existing table.

### Claim versus prior implication

Searches/sources: Can asymptotic lower bounds determine small exact values?; Can the weaker cover-free maximum determine the stricter union-free maximum?.

Evidence: The superlinear asymptotic lower bound gives no exact small-order value. A family may be two-cover-free and still fail three-union-freeness.

The finite search addresses a distinct unresolved exceptional regime.

### Source inspections

- **Asymptotically sharp bounds for cancellative and union-free hypergraphs** — CONTEXT_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2411.07908
  Trigger: Same definitions and asymptotic context.
  Material read: Primary HTML introduction, union-free subsection, facts and theorem ranges.
  Method: lawful open-access primary text
  Evidence: The paper supplies general context, not the six exact finite values.
- **Sharp bounds for uniform union-free hypergraphs** — EXCEPTIONAL_REGIME.
  Identifier: https://arxiv.org/abs/2605.11949
  Trigger: Current stronger theorem with possible broader coverage.
  Material read: Primary HTML introduction and exceptional-regime discussion.
  Method: lawful open-access primary text
  Evidence: The theorem explicitly leaves the regime containing this invariant outside its general result.

Residual originality risks:
- An older separable-code or superimposed-code table could encode these small exact values under different terminology.

## Scientific value

**PASS.** The theorem gives a complete six-order initial segment and unique equality type in a natural regime explicitly exceptional in current asymptotic theory. Because the eventual scale is superlinear, the transition away from the pair-star construction is mathematically meaningful, making these exact initial conditions useful benchmarks.

Residual value risks: The result stops at order nine and does not locate the first later transition..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
