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

The scientific argument is given in `RESULT.md`. Run `python verify.py` in this directory to reproduce the independent finite checks with Python 3 standard libraries; stdout from an actual run is embedded as `verification_output.txt`.

The checker evaluates \(\sigma(m^2)\) by factorization for every integer \(1\le m\le100000\) and compares the gcd-equality counts to the values in Dris, Section 5. It checks all simple roots and their Hensel lifts modulo \(p^B\) for \(p\in\{7,13,19,31\}\), \(1\le B\le3\); verifies the exact CRT avoidance probability for \(q=7,13\) by examining all \(8281\) residue classes; and finds small-prime witnesses in relevant progressions. All comparisons use exact integers and rational arithmetic.

The finite regression does not establish the theorem for unbounded \(m\), \(p\), or \(B\). Completeness of the asymptotic result follows from the finite-CRT limiting argument, the divergence of prime reciprocal sums in the prescribed arithmetic progressions, and multiplicativity of the divisor sum. No external audit has been performed.
