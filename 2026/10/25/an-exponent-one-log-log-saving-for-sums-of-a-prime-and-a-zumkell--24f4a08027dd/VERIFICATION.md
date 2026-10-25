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

The proof is analytical, using established results about consecutive-prime Zumkeller blocks, Mertens products, Linnik bounds, and CRT. The supplied Python program `verify.py` uses exact rational arithmetic for the six finite prime blocks, verifies the inequalities \(2\le B_k<2(1+1/Q)\) and \(0<\varphi(A_k)/A_k<1/2\), and confirms four CRT forbidden-residue counts by exhaustive enumeration of one complete modulus. It also checks the divisor/totient inequality for four familiar Zumkeller integers. Run: `python3 verify.py`. Expected terminal marker: `VERIFY_OK`.

These computations are finite only. They neither establish the existence of an effective universal Zumkeller-block threshold nor certify the claimed infinite asymptotic without the displayed proof and cited results. Independent auditing and validation have not been performed.
