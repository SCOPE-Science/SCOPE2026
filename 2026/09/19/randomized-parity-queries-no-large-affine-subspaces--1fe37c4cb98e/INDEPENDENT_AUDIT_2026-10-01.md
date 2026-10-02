# Independent audit — Efficient randomized parity queries without large monochromatic affine subspaces

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** Wang--Wu's definition depends only on the bitwise XOR of the complete two-party inputs. Their address stage samples coordinates of that XOR, so singleton parity queries simulate it. Each of the four queries in their fully linear \(\mathbb F_{2^{4k}}\) test contributes four-\(k\) binary linear coordinates, yielding \(O(k\log k)=O(\log N\log\log N)\) parity queries with the same error. If \(a+H\) is monochromatic of codimension \(r\), then \(H\times(a+H)\) is a monochromatic XOR rectangle of density \(2^{-2r}\); their rectangle bound forces \(r\ge m/(16k)\), which is polynomial in \(N\) up to logarithmic factors under their parameters. Deterministic parity-tree leaves are affine subspaces of codimension at most the depth, giving the deterministic lower bound.

## Originality

**PASS.** Best-of-knowledge originality passes for the parity-query consequence. The communication construction and rectangle lower bound are prior; the new mathematical step is the XOR quotient plus protocol descent and the affine-subspace transfer.

### Equivalent formulations

No earlier equivalent negative answer to the stated parity-query question was located.

Evidence: The archive search returned this record as the exact match; nearby Wang--Wu records address communication refinements rather than the parity-query consequence. Gavinsky's Question 14 is explicitly stated in affine-subspace language, so synonymous formulations were checked directly.

### Broader coverage

No inspected broader theorem already resolves the randomized affine-subspace question.

Evidence: Wang--Wu prove the total communication separation, fully linear verification protocol, and rectangle density bound, but do not formulate the parity-query quotient consequence in the inspected paper. Gavinsky poses the efficient-randomized-parity-query versus large-affine-subspace question as open. The deterministic XOR communication/parity correspondence does not itself give the randomized simulation used here.

### Exact database or table

This is a qualitative complexity separation rather than a tabulated quantity; the exact archive search is the applicable database check.

Evidence: No earlier archive entry states a negative answer to that question via this construction.

### Claim versus prior implication

The claim is a concise but genuine source-specific reduction, not a generic corollary of randomized communication complexity.

Evidence: The descent is not automatic for an arbitrary randomized communication protocol; it works because this protocol samples XOR coordinates and then uses fully linear field queries. The affine-subspace rectangle embedding gives the exact factor-two codimension conversion. The known deterministic equivalence does not imply the randomized upper bound.

### Source inspections

- **Efficient Randomized Communication Without Large Monochromatic Rectangles** — ESSENTIAL_PRIOR_NOT_COVERING.
  Identifier: https://eccc.weizmann.ac.il/report/2026/190/
  Material read: complete 19-page ECCC paper, including Theorem 3.7, the public-coin protocol, Definition 3.8, and the monochromatic-rectangle theorem.
  Evidence: The paper supplies four fully linear field queries, the sampled address protocol, and rectangle density at most \(2^{-m/(8k)}\), but does not state the one-variable parity-query theorem.
- **Unambiguous Parity-Query Complexity** — OPEN_QUESTION_SOURCE.
  Identifier: https://doi.org/10.1002/rsa.70010
  Material read: accessible full article around the parity-query definitions and Question 14.
  Evidence: Question 14 asks whether efficient randomized parity-query computation forces a large monochromatic affine subspace.

### Checked sources

- https://eccc.weizmann.ac.il/report/2026/190/
- https://arxiv.org/abs/2609.20763
- https://doi.org/10.1002/rsa.70010
- https://doi.org/10.1137/17M1136869
- Resultary published-finding semantic search

### Residual risks

- The motivating communication result is extremely recent and the quotient deduction is concise, so near-simultaneous or folklore priority risk is material.

## Scientific value

**PASS.** The result gives a quantitative negative answer to an explicit structural question in randomized parity-query complexity: polylogarithmic randomized parity queries coexist with polynomial codimension for every monochromatic affine subspace. A short reduction can still be valuable when it settles a named open implication.

## Final assessment

The unchanged final claim passes correctness, originality, and scientific value. No research claim or slogan change is required.

This assessment is not formal verification or expert attestation and does not guarantee that no undiscovered prior art exists.
