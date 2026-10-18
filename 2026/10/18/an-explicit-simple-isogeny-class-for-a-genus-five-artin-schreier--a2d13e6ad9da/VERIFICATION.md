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
# Reproducibility and limits

Run `python3 verify.py` with Python 3.9 or newer. No third-party packages or network connections are needed. The script uses explicit irreducible monic moduli for \(\mathbb F_{3^m}\), \(1\le m\le5\), certifies their irreducibility by complete monic trial division, then enumerates all finite-field inputs for both absolute-trace and direct \(y^3-y\) methods. It verifies point counts \((6,18,24,66,291)\), derives all zeta-numerator coefficients by Newton identities and the genus-five functional equation, checks \(P_C(1)=711\), and proves irreducibility modulo \(5\) with exact gcd and Frobenius-power tests. The script's output includes `VERIFY_OK` on success.

The mathematical proof also uses standard Artin–Schreier genus and \(p\)-rank formulas, the curve zeta functional equation, and simplicity consequences of a rationally irreducible Frobenius characteristic polynomial. Computation is exhaustive for \(m\le5\), not for infinitely many extensions. The functional equation is essential to the complete degree-ten reconstruction. Arithmetic simplicity does not establish geometric simplicity.
