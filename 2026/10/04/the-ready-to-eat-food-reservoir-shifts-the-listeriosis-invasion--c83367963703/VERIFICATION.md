---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The primary equations impose \(F_u+F_c=F\), and substituting the published zero-food state gives \(F_u'=p_fF>0\). Eliminating \(F_u=F-F_c\) at the clean-food equilibrium yields the displayed \(3\times3\) infected/environmental block. Its characteristic cubic has constant term \(kd_Bq(1-\mathcal R_F)\). For \(q>0\), \(\mathcal R_F<1\) implies \(a\xi_l<kd_B\); the remaining Routh--Hurwitz inequalities are strictly positive. A fresh symbolic check confirmed the package identity for \(A_1A_2-A_3\). The exact witness gives published \(1/3\), corrected \(4/3\), and cubic \(\lambda^3+5\lambda^2+6\lambda-1\).

## originality

PASS

The inspected primary paper prints the listeriosis-only equations, the food-total constraint, a disease-free point with both food compartments zero, and a threshold omitting the contaminated-food return path. The corrected equilibrium and factor are not in that source. Resultary and source-specific searches found no published correction.

## value

PASS

The correction changes both the existence of the printed disease-free equilibrium and the invasion threshold. An exact positive-parameter witness reverses the source's stability prediction, so this is a substantive model correction rather than a cosmetic normalization issue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
