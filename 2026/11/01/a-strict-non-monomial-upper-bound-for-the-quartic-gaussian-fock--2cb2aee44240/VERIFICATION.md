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

# Verification of the polynomial witness
Run `python3 verify.py` using the ordinary Python standard library. The script recomputes the fourth norms of the two quadratic polynomials from their squared-coefficient Gaussian moments; its exact expected difference is
\[
-\frac{23857292957391399561}{18757812500000000000000000}.
\]
It also checks \(r^4<1/2\), \(r^2>1/2\), and \(1-a^2>0\) with exact fractions. The exterior modulus domination is separately proved by a symbolic identity in the proof, without numerical point sampling. The lower bound depends on the cited established Gaussian Hilbert-space sharp-radius theorem, not on this code. This is not an independent mathematical audit.
