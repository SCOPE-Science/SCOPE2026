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

The exact computations are self-contained in the two accompanying Python 3 scripts, using only the standard library. Execute `python3 verify_symbolic.py` and `python3 verify_point_counts.py` from a directory containing the programs; no external data or CAS is required.

`verify_symbolic.py` directly reconstructs all nonzero coefficients of the \(3\times3\) Cartier block from the multinomial expansion of \((x^5+a x^2+1)^4\), verifies the determinant and constant minor, and checks the twisted-product minor \(3a^4(a^{10}-1)\). On the quotient ring \(\mathbb F_7[a]/(a^5-1)\) it calculates the full four-step product, verifies rank-one minors, trace \(2\) and \(P_4^2=2P_4\). At \(a=0\), it confirms cube-zero behavior. Expected marker: `SYMBOLIC_CERTIFICATE_OK`.

`verify_point_counts.py` enumerates exact extensions \(\mathbb F_{7^n}\) with \(n=1,2,3,4\), tests their defining moduli irreducible, and counts points on all six smooth prime-field parameter curves. Newton identities give mod-seven numerator coefficients and independent ranks \(0,1,2,2,2,2\). Expected marker: `INDEPENDENT_POINT_COUNTS_OK`.

These computations substantiate polynomial certificates and six finite-field examples; infinite-field correctness rests on the proof in `RESULT.md`. No independent human or external audit has occurred.
