---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible finite checks

Run `python verify.py` with Python 3 (no third-party packages required). The separately implemented evaluator constructs the upset lattice of each complete two-level frame and computes each nucleus from upper cones, without using the theorem's Boolean compatibility formula. It then checks nucleus identities, composes every ordered pair on every upset, and compares those outcomes with the criterion and closed-form pair count. A separate standard Bron–Kerbosch implementation enumerates maximal commuting cliques and checks the claimed two unique extremizers.

For the case with two points on each level, the program also enumerates all meet-closed possible fixed-point families on the seven-element Heyting lattice, reconstructs closure maps, and tests meet preservation. It finds exactly the 16 subset-generated nuclei, providing a second finite check of exhaustiveness.

The expected per-case totals for \((r,s)=(2,2),(2,3),(3,2),(3,3)\) are respectively \(162,542,542,1682\) ordered commuting pairs and \(7,11,11,15\) for the maximum commuting-family sizes. The expected final output line is `VERIFY_OK`.

Limits: exhaustive computation only covers these four finite parameter pairs; the upper bound, unique-extremizer classification, and exact all-size formulas require the general mathematical proof in `RESULT.md`. No independent external audit was carried out.
