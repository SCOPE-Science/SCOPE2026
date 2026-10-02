# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. Exact arithmetic on the six printed rows gives \(a=r_2+r_3=100112202000102002022001\) and \(b=r_1+r_4=211221201011101002221122\), with \(\operatorname{Supp}(a)\) a strict subset of \(\operatorname{Supp}(b)\). Hence the printed row space is not minimal. The source paper proves that a ternary linear code is trifferent exactly when it is minimal, so this already invalidates the claimed witness. Independently, the triple \(a,b,-a\) has no coordinate containing all three field symbols. The first six columns have determinant \(2\) modulo \(3\), verifying that the printed matrix still has rank six. An independent calculation reproduced every certificate datum.
- Originality: **PASS**. The 2024 paper itself prints the exact matrix and uses it as the inner \([24,6]_3\) trifferent code in the proof of its explicit rate theorem, while also proving the minimal-code/trifferent equivalence that makes support containment decisive. Targeted searches for the exact certificate strings, errata, corrections, and later blocking-set work found no public correction or prior statement of this defect. Resultary likewise returned only the audited correction.
- Scientific value: **PASS**. The matrix is the explicit inner code used in a published asymptotic concatenation proof. A short exact certificate that the printed witness fails its required property is a motivated reproducibility correction with direct consequences for that proof, while the claim carefully avoids overstating what it disproves.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in
`AUDIT.json` and is not relabeled as independent evidence.
