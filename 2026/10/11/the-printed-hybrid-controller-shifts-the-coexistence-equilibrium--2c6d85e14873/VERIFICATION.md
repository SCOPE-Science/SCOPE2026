---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. At a constant state the delay-difference feedback is exactly zero, while alpha1=.6 multiplies prey growth, so subtracting controlled and uncontrolled balance equations proves no common positive equilibrium. Independently derived the positive controlled root of 12x^3+237x^2+1186x-200=0 and y=1/4+9x/[10(10+x)], obtaining (0.16326353132240665,0.26445767668400183), versus the printed old point near (0.19755,0.267435). Independently reconstructed the characteristic matrix and solved for |e^{-i omega delta}|=1, giving controlled first omega=0.5308877025, delay=2.9635539089 and uncontrolled omega=0.5392046766, delay=2.9241528123. Inspected source VERIFY.py quartic frequency equation with one positive root by Descartes signs -,-,+,+,+, no earlier crossings, and positive crossing speed about 0.080834. The corrected threshold direction is opposite to paper Example 7.2, with scope limited to local linear stability and printed equations.

## originality

PASS

PASS, best-of-knowledge for concrete correction of the specific published hybrid-controlled predator–prey example and reversed threshold comparison. Ou et al. AIMS Mathematics 9(1), 2024, eqs (4.1),(7.2), Example 7.2 explicitly use alpha1=.6 and claim same equilibrium and controlled threshold ≈2.85; the full lawful OA PDF’s relevant equations were inspected and contradict the paper’s own numerical conclusions. No published correction with actual (xc,yc) and first delay 2.9635539 was located by DOI, title, coefficient and Resultary comparison. General delay-Hopf theory supplies characteristic-equation machinery but does not automatically imply this corrected model-specific equilibrium and root; a later unindexed erratum remains risk.

## value

PASS

PASS. The exact positive coexistence equilibrium and first imaginary-root crossing determine whether the published controller shrinks or enlarges the stable-delay region. Correcting the central comparison reverses its conclusion, a substantial mathematical correction to a natural predator-prey delay model rather than just a residual-at-old-point check. Scope is precisely the printed Example 7.2 and local linear stability, no unsupported nonlinear Hopf branch claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
