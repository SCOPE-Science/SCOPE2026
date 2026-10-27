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

The supplied `verify.py` is a standalone Python 3 checker that uses only the standard library. Run `python3 verify.py` to enumerate all invertible \(2\times2\) matrices over fields of sizes \(2,3,4,5,7,8,9,11\). Polynomial models use \(t^2+t+1\) over \(\mathbb F_2\), \(t^3+t+1\) over \(\mathbb F_2\), and \(t^2+1\) over \(\mathbb F_3\) for sizes \(4,8,9\), respectively.

The checker validates the finite-field multiplication, counts fixed projective points using the displayed cubic equation, and compares all four histogram proportions to exact rational expressions. In the cases \(q\le5\), it independently enumerates every nonzero algebra vector and verifies \(Mx^{[2]}=x\) directly for each matrix, cross-checking the projective bijection. The outputs (for \(N=0,1,2,3\)) are:

- \(q=2\): \((2,3,0,1)\), among \(6\) invertible matrices.
- \(q=3\): \((16,20,8,4)\), among \(48\).
- \(q=4\): \((60,90,0,30)\), among \(180\).
- \(q=5\): \((160,208,64,48)\), among \(480\).
- \(q=7\): \((672,900,216,228)\), among \(2016\).
- \(q=8\): \((1176,1764,0,588)\), among \(3528\).
- \(q=9\): \((1920,2624,512,704)\), among \(5760\).
- \(q=11\): \((4400,6100,1000,1700)\), among \(13200\).

Observed final marker: `VERIFY_OK`. These finite checks neither substitute for the projective counting proof over arbitrary finite fields nor provide an independent mathematical audit.
