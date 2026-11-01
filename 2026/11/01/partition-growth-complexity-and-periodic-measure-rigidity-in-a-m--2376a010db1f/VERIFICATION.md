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

# Verification record

The proof in RESULT.md is analytical: finite words are counted by increasing positive compositions, periodic gaps by cyclic monotonicity, the invariant measures by a complete recurrent-point classification, and the asymptotic constant by the Hardy--Ramanujan partition formula and a controlled Riemann-sum limit.

The standalone `verify.py` was executed with Python, with all checks passing. It independently enumerated all binary finite words of lengths 1--14 and all circular binary states of lengths 1--12, compared the exact formulas for language size and periodic points, verified the Euler-zeta first-difference identity, and checked numerical leading ratios at lengths 200, 400 and 800 (approximately 0.995564305, 0.996996428 and 0.997943726). The script has no third-party dependencies.

Finite enumeration and leading-ratio samples do not prove universal or asymptotic statements; those statements rely on the symbolic-dynamical and classical analytic-number-theoretic arguments in RESULT.md. The analysis does not claim independent verification or historical priority certification.
