# Independent mathematical audit — Projective nonincidence graphs realize every even total-uniformity

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — In the point-hyperplane nonincidence graph, earlier hyperplane choices cannot affect freshness of a new point vertex. A point \(P_i\) has a fresh hyperplane neighbor exactly when it is outside the span of the earlier selected points, so every legal point increases the span dimension by one; total domination of all hyperplanes occurs exactly when the selected points span the whole \(d\)-dimensional space. Dually, every legal hyperplane drops the intersection dimension by one and total domination of all points occurs exactly at zero intersection. Hence every total dominating sequence contains exactly \(d\) vertices from each part. The regularity, connectedness, false-twin-freeness, and recursive deletion statement follow from elementary projective linear algebra. An independent small-field replay reproduced the degrees and span criterion.

Checked sources: Assigned RESULT.md and inspected verifier source; Brešar--Henning--Rall 2016; Dravec--Jakovac--Kos--Marc 2022; Bahadır--Gözüpek--Doğan 2021; Independent small-field linear-algebra replay.

Residual correctness risks: The finite artifact and replay cover only small fields; the proof, not computation, establishes all prime powers and dimensions..

## Originality

**PASS** — Prior work covers total \(4\)-uniform crown graphs, projective-plane-linked regular bipartite total \(6\)-uniform graphs, nonexistence for odd parameters, and one connected total \(8\)-uniform example. The 2021 paper explicitly left connected examples for all larger even parameters as an open direction. The inspected literature and Resultary search did not contain the arbitrary-dimensional projective nonincidence construction or the resulting complete connected existence spectrum.

### Equivalent formulations

Searches/sources: Resultary query: total k-uniform projective point hyperplane nonincidence every even k Grundy total domination; Brešar--Henning--Rall, Total Dominating Sequences in Graphs; Dravec--Jakovac--Kos--Marc 2022; Bahadır--Gözüpek--Doğan 2021.

Evidence: The Resultary exact match was the audited theorem. Dravec et al. characterize the total \(4\) case and regular bipartite total \(6\) case, tied to finite projective planes. Bahadır et al. prove odd nonexistence and exhibit a connected total \(8\)-uniform graph.

No equivalent all-dimension nonincidence statement was found.

### Broader coverage

Searches/sources: Hypergraph edge-covering formulation of Grundy total domination; finite projective geometry nonincidence graph literature; 2021 total-uniform graph existence paper.

Evidence: The point-hyperplane nonincidence graphs themselves are classical, but the searched finite-geometry sources do not state their total \(2d\)-uniformity. The 2021 graph-theory paper explicitly treats larger even connected examples as ongoing/open.

No inspected broader graph or hypergraph theorem implies total \(2d\)-uniformity for these graphs.

### Exact database or table

Searches/sources: Resultary exact theorem search for projective nonincidence total uniformity; published small-k total-uniform classifications.

Evidence: No pre-existing exact record was found; the small-k literature covers \(4,6,8\) separately.

The result is an infinite structural family, not a finite table.

### Claim versus prior implication

Searches/sources: Does the total \(6\)-uniform projective-plane result extend formally to arbitrary dimension?; Does odd nonexistence plus one \(8\)-uniform example imply all even cases?.

Evidence: The dimension-\(3\) projective-plane classification does not imply the span/intersection argument in arbitrary dimension. The earlier existence results leave even \(k\ge10\) open rather than implying them.

The arbitrary-dimensional rank-growth proof supplies genuinely new coverage.

### Source inspections

- **On graphs all of whose total dominating sequences have the same length** — PRIMARY_OPEN_PROBLEM.
  Identifier: https://doi.org/10.1016/j.disc.2021.112492
  Trigger: Closest prior existence-spectrum paper.
  Material read: Complete accessible article material, including the odd nonexistence theorem, connected total \(8\)-uniform construction, and concluding open direction.
  Method: lawful full text
  Evidence: The paper does not give connected constructions for all larger even parameters.
- **On graphs with equal total domination and Grundy total domination numbers** — LOW_DIMENSION_PRIOR.
  Identifier: https://doi.org/10.1007/s00010-021-00776-z
  Trigger: Closest prior projective-geometry-linked classification.
  Material read: Accessible full preprint/article text covering the total \(4\) and regular bipartite total \(6\) cases.
  Method: lawful open-access full text
  Evidence: It links the \(6\)-uniform case to finite projective planes but does not state the arbitrary-dimensional nonincidence theorem.

Residual originality risks:
- A differently indexed finite-geometry or hypergraph-covering source could contain the same rank-growth observation, though none was located.

## Scientific value

**PASS** — The theorem closes a published existence question exactly, supplies one uniform finite-geometric mechanism for every even parameter, and yields infinitely many connected regular false-twin-free examples for each fixed even parameter at least four. This is a natural structural construction rather than a small-case extension.

Residual value risks: It does not classify all total-uniform graphs or prove minimum order/degree..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier review evidence remains separately identified and is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
