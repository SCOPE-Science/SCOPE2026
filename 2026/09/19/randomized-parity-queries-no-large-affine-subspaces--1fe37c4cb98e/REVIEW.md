# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** Wang--Wu's definition depends only on the bitwise XOR of the complete two-party inputs. Their address stage samples coordinates of that XOR, so singleton parity queries simulate it. Each of the four queries in their fully linear \(\mathbb F_{2^{4k}}\) test contributes four-\(k\) binary linear coordinates, yielding \(O(k\log k)=O(\log N\log\log N)\) parity queries with the same error. If \(a+H\) is monochromatic of codimension \(r\), then \(H\times(a+H)\) is a monochromatic XOR rectangle of density \(2^{-2r}\); their rectangle bound forces \(r\ge m/(16k)\), which is polynomial in \(N\) up to logarithmic factors under their parameters. Deterministic parity-tree leaves are affine subspaces of codimension at most the depth, giving the deterministic lower bound.
- Originality: **PASS.** Best-of-knowledge originality passes for the parity-query consequence. The communication construction and rectangle lower bound are prior; the new mathematical step is the XOR quotient plus protocol descent and the affine-subspace transfer.
- Scientific value: **PASS.** The result gives a quantitative negative answer to an explicit structural question in randomized parity-query complexity: polylogarithmic randomized parity queries coexist with polynomial codimension for every monochromatic affine subspace. A short reduction can still be valuable when it settles a named open implication.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
The earlier same-model scientific assessment remains preserved in `AUDIT.json` and is not relabeled as independent evidence.
