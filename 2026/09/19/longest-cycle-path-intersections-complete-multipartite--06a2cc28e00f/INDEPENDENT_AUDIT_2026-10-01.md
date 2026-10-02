# Independent mathematical audit — Exact intersections of longest cycles and paths in complete multipartite graphs

Audited on 2026-10-01 UTC.

**Disposition:** PASSED

## Correctness — PASS

If \(B\) is a largest part and \(O=V\setminus B\), every cycle satisfies \(|C\cap B|\le|C\cap O|\) and every path satisfies \(|P\cap B|\le|P\cap O|+1\). In the nonspanning regimes these bounds are attained by alternating constructions using every vertex of \(O\), so the longest-object vertex sets are exactly \(O\cup A\) with \(|A|=q\) for cycles or \(q+1\) for paths. In the complementary regimes Dirac's theorem or the alternating path gives spanning objects. The pairwise spectra then follow from the exact intersection range of two fixed-size subsets of an \(M\)-set. A fresh independent dynamic-programming enumeration through order \(8\) reproduced all predicted longest orders and intersection spectra.

## Originality — PASS

The ingredients (Hamiltonicity criteria, alternation bounds, subset intersections) are elementary and not claimed new. The final contribution is the complete longest-cycle/longest-path vertex-set classification, full pairwise intersection spectra, common connectivity-sized core, and exact equality cases for Smith/Hippchen inside all complete multipartite graphs. Resultary and literature searches did not locate that classification. Residual access risk remains for Wu (2026), Hippchen's thesis, and Kains's dissertation.

### Equivalent formulations

Standard circumference/traceability facts are equivalent to only the maximum size, not to the full family, common core, and pairwise intersection spectrum.

Evidence: Resultary returned only this record for the exact class/result combination. Searches located general longest-intersection work but no complete-multipartite vertex-set spectrum theorem.

### Broader coverage

The new theorem is narrower in graph class but substantially stronger within that class; the general lower-bound literature does not imply the exact set-family description.

Evidence: Ma--Ning--Zhao proves a general \(k/600\) lower bound and discusses sharpness examples, not the class-wide exact spectrum. No inspected accessible source supplied a theorem dominating the complete-multipartite classification.

### Exact database or table

The theorem is structural, not a known-table recomputation.

Evidence: No exact database/table of complete-multipartite longest-object intersection spectra was found.

### Claim versus prior implication

Although the proof is short, the result is a natural complete classification addressing active conjectures; it is not a mere substitution into a known intersection theorem.

Evidence: Classical alternation/Hamiltonicity facts mechanically determine longest order, but not an already-stated prior theorem containing the complete vertex-set families and intersection spectra was located. The final spectrum follows by an additional exact classification of which extremal vertex sets occur.

### Source inspections

- **Longest cycles intersect linearly in highly connected graphs** — NOT_COVERING for the complete-multipartite exact classification.. Material read: Abstract and indexed context of the conjecture/general \(k/600\) theorem; the package's quoted complete-bipartite sharpness context was cross-checked against the paper's subject. Evidence: The paper's advertised theorem is a general linear lower bound, not an exact class classification.
- **On two conjectures about the intersection of longest paths and cycles** — No complete-multipartite classification located.. Material read: Bibliographic/abstract-level material and the package's prior full-text search result. Evidence: No indexed or package full-text search hit for multipartite treatment.
- **Intersection of cycles and paths in k-connected graphs** — INACCESSIBLE_RISK, not evidence for or against coverage.. Material read: Bibliographic metadata only; full text was not obtained. Evidence: No full theorem text was available for inspection.

### Checked sources

- arXiv:2609.20724
- arXiv:2310.03849
- 2013 survey DOI:10.5614/ejgta.2013.1.1.6
- Wu 2026 DOI:10.1016/j.dam.2025.07.013
- Resultary published findings

### Residual risks

- Wu (2026), Hippchen (2008), and Kains (2023) were not fully inspected in this run.
- Older class-specific graph literature may use different terminology; no concrete covering result was found.

## Scientific value — PASS

This is a natural complete classification for a major graph class directly tied to active Smith and Hippchen intersection conjectures. Exact common cores, all pairwise intersection sizes, and equality cases are meaningful structural information even though the proof uses elementary extremal arguments.

## Limitations

- The classification is only for complete multipartite graphs and the cycle statement requires \(q\ge 2\).
- Finite enumeration through small orders corroborates but does not replace the direct proof.
- Wu (2026) could not be retrieved through the authorized route in this audit and remains a residual originality risk.
