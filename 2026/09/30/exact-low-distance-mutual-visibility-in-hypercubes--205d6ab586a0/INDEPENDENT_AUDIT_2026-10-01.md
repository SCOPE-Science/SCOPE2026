# Mathematical audit — 2026-10-01

Record: `SCOPE-20260930-205d6ab586a0`

## Correctness — PASS

For any feasible set in \(Q_n\), the Hamming diameter is at most the allowed visibility distance. Kleitman's diameter theorem therefore gives the sharp anticode upper bounds \(n+1\) for diameter two and \(2n\) for diameter three. The radius-one ball realizes the first bound. For diameter three and \(n\ge5\), Frankl's equality characterization says every size-\(2n\) family is, up to translation, \(\{A:|A\setminus\{y\}|\le1\}\); the pair \(\varnothing,\{y,i\}\) has both possible middle vertices selected, so such a family is not mutually visible. The explicit singleton-plus-\(y\)-pair construction has size \(2n-1\) and its required geodesics check by pair type. The parity family on \(Q_4\) gives eight, and the direct omitted-pair orbit argument gives five on \(Q_3\) and three on \(Q_2\). The assigned verifier exhausts all subsets through dimension four and checks the constructions through dimension twelve.

### Correctness sources

- assigned RESULT.md and verify.py
- Frankl 2017 fixed-diameter theorem/full primary PDF
- Cera et al. 2024 k-distance mutual visibility full arXiv HTML

### Correctness risks

- Only \(k=2,3\) are determined.

## Originality — PASS

The primary k-distance mutual-visibility paper was inspected in full searchable HTML. It introduces the parameter and proves exact results for several classes, but a full-text search finds hypercubes only among references to prior ordinary mutual-visibility work and does not state these hypercube formulas. Frankl's theorem supplies only the bounded-diameter extremal families, not the geodesic-avoidance exclusion or lower constructions. Resultary searches for the exact hypercube parameter returned only the audited record. Thus the combination, including the strict one-point drop from the diameter-three anticode maximum and the \(Q_4\) parity exception, is not covered by the inspected sources.

### equivalent_formulations

Searches:
- Resultary: hypercube k-distance mutual visibility mu_2 mu_3 exact values Hamming diameter
- Cera et al. arXiv:2408.03976 full HTML search for hypercube
- Frankl fixed-diameter theorem

Evidence:
- The 2024 paper's searchable text mentions hypercubes only in surrounding ordinary-visibility references and contains no exact \(\mu_2(Q_n)\) or \(\mu_3(Q_n)\) theorem.
- Frankl gives the anticode extremal structure, not visibility.

Reasoning:
Bounded Hamming diameter is only a necessary condition; the audited theorem additionally solves the internal-geodesic avoidance condition.

### broader_coverage

Searches:
- Cera et al. 2024 full text
- Frankl 2017 full primary PDF
- ordinary hypercube mutual-visibility literature
- current Resultary hypercube findings

Evidence:
- No broader inspected visibility theorem specializes to the exact low-distance formulas.

Reasoning:
Classical mutual visibility at unrestricted distance and anticode extremal theory do not mechanically supply the distance-limited lower constructions or the exclusion of the diameter-three equality family.

### exact_database_or_table

Searches:
- current Resultary exact hypercube search
- web searches for low-distance mutual visibility hypercubes

Evidence:
- No exact database or table with the claimed sequence was found.

Reasoning:
The formulas hold uniformly in dimension and are theorem-level claims.

### claim_vs_prior_implication

Searches:
- claim-versus-Frankl implication comparison

Evidence:
- Frankl permits \(2n\) vertices at diameter three; the audited visibility condition rules all equality families out and constructs \(2n-1\).
- The \(Q_4\) parity construction reaches eight despite the different equality behavior at the threshold dimension.

Reasoning:
The final values require additional graph-geodesic arguments not present in the set-family theorem.

### source_inspections

- **The k-distance mutual-visibility problem in graphs** — https://arxiv.org/abs/2408.03976. Trigger: Primary source introducing the exact parameter. Material read: Full searchable arXiv HTML, including definition, general results, complexity section, and exact-class section; searched specifically for hypercubes. Method: Primary full-text statement search and scope comparison. Assessment: NOT COVERING the hypercube formulas. Evidence: Hypercubes appear in the introduction as ordinary mutual-visibility related work, not as an exact k-distance class.
- **A Stability Result for Families with Fixed Diameter** — https://www.renyi.hu/~pfrankl/2016-6.pdf. Trigger: Critical equality classification used for the \(2n\) upper bound. Material read: Primary PDF text and rendered theorem pages, including the Kleitman diameter statement and Frankl equality classification for odd diameter. Method: Primary theorem verification. Assessment: SUPPLIES the anticode equality structure but not mutual visibility. Evidence: For odd diameter three the extremal family is the translate of the standard \(K_y\) family.
- **Assigned hypercube verifier** — verify.py. Trigger: Small-dimensional exceptional cases and construction checks. Material read: Complete source. Method: Line-by-line inspection. Assessment: Correct corroboration. Evidence: It exhausts all subsets of \(Q_2,Q_3,Q_4\) and checks the stated families through dimension twelve.

### checked_sources

- https://arxiv.org/abs/2408.03976
- https://www.renyi.hu/~pfrankl/2016-6.pdf
- ordinary mutual-visibility hypercube literature
- current Resultary exact search
- assigned RESULT.md and verify.py

### residual_risks

- A later or poorly indexed hypercube-specific k-distance result could exist, but no plausible covering source was located.

## Scientific value — PASS

The result determines the first two nontrivial distance-limited levels on a central graph family, identifies a genuine one-point obstruction beyond the classical diameter extremum, and isolates the exceptional parity construction in dimension four. It creates a concrete bridge between a recent visibility invariant and classical anticode structure, which is a natural motivated gap.

### Value sources

- Cera et al. parameter introduction
- Kleitman–Frankl diameter theory
- assigned constructions

### Value risks

- No claim is made for larger visibility radii.

## Limitations

- Only \(k=2\) and \(k=3\).
- Frankl/Kleitman provide the anticode input but not the visibility formulas.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
