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

The exact prime-local argument in `RESULT.md` is the universal proof. Its two binomial coefficient identities for each of \(k+1\) and \(k+2\) are integer equations and apply also at the low boundaries \(n=k\) and \(n=k+1\), with \(\nu_p(0)=+\infty\).

The standalone `verify.py` uses separately constructed Pascal coefficients and factorial binomial coefficients for each \(1\le k\le100\) and every \(k\le n\le5k+25\). For each \(k\), it also recomputes the first two witness values, their exact gcd, and the universal normalization denominator. For \(k\le20\) it independently computes the gcd of all Newton coefficients from the degree-\(2k\) forward-difference table; unlike a finite sample, that gcd equals the polynomial's fixed divisor over the entire integer domain. The recorded successful verifier output was obtained by running the actual standalone script.

No finite sample proves the prime-local assertions for all \(k\) and \(n\); those assertions require the argument in the proof. Literature coverage beyond the inspected references has not been certified, and no independent mathematical audit has been performed.
