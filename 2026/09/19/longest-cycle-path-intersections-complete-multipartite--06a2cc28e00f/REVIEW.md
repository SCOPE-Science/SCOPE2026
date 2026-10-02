# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

**Disposition:** PASSED

## Correctness — PASS

If \(B\) is a largest part and \(O=V\setminus B\), every cycle satisfies \(|C\cap B|\le|C\cap O|\) and every path satisfies \(|P\cap B|\le|P\cap O|+1\). In the nonspanning regimes these bounds are attained by alternating constructions using every vertex of \(O\), so the longest-object vertex sets are exactly \(O\cup A\) with \(|A|=q\) for cycles or \(q+1\) for paths. In the complementary regimes Dirac's theorem or the alternating path gives spanning objects. The pairwise spectra then follow from the exact intersection range of two fixed-size subsets of an \(M\)-set. A fresh independent dynamic-programming enumeration through order \(8\) reproduced all predicted longest orders and intersection spectra.

## Originality — PASS

The ingredients (Hamiltonicity criteria, alternation bounds, subset intersections) are elementary and not claimed new. The final contribution is the complete longest-cycle/longest-path vertex-set classification, full pairwise intersection spectra, common connectivity-sized core, and exact equality cases for Smith/Hippchen inside all complete multipartite graphs. Resultary and literature searches did not locate that classification. Residual access risk remains for Wu (2026), Hippchen's thesis, and Kains's dissertation.

The structured originality comparison, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.json`.

## Scientific value — PASS

This is a natural complete classification for a major graph class directly tied to active Smith and Hippchen intersection conjectures. Exact common cores, all pairwise intersection sizes, and equality cases are meaningful structural information even though the proof uses elementary extremal arguments.

## Limitations

- The classification is only for complete multipartite graphs and the cycle statement requires \(q\ge 2\).
- Finite enumeration through small orders corroborates but does not replace the direct proof.
- Wu (2026) could not be retrieved through the authorized route in this audit and remains a residual originality risk.
