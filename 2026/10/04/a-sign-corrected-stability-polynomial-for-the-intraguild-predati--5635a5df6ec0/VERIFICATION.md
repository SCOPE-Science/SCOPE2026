---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For any \(3\times3\) matrix, \(\det(\lambda I-J)=\lambda^3-(\operatorname{tr}J)\lambda^2+P_2(J)\lambda-\det J\). The source’s displayed definitions are \(\sigma_2=\operatorname{tr}J\), \(\sigma_1=-P_2(J)\), and \(\sigma_0=\det J\), so all three nonleading signs in its printed polynomial are reversed. Direct substitution of the stated positive parameter witness makes all three equilibrium residuals zero and yields the displayed rational Jacobian. Independent exact arithmetic reproduced coefficients \((23/36,139/216,4/27)\) and the strict Hurwitz margin, so the equilibrium is locally asymptotically stable while the printed source criterion rejects it.

## originality

PASS

The inspected current arXiv supplement/published record retains the sign convention that produces the inconsistency: the Jacobian definitions give \(\sigma_2=\operatorname{tr}J\), \(\sigma_1=-P_2(J)\), and \(\sigma_0=\det J\), while the printed characteristic polynomial uses plus signs. Targeted Resultary and web searches by arXiv id, DOI, title, coefficients, and correction/erratum found no source-specific prior correction. The publisher record dated 2026-06-01 shows the article remains current without a surfaced erratum.

## value

PASS

A sign correction that reverses the local stability classification of an admissible positive coexistence equilibrium is scientifically consequential. The exact rational witness makes the effect concrete and reproducible rather than merely editorial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
