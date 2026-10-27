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

# Verification

Run `python3 verify.py` from the extracted package directory. The program independently constructs the \(37\)-state transition system using all four output labels, enumerates direct pair sums for \(1\le m\le8\), and verifies the initial counts \(2,7,27,95,345,1259,4629,17019\).

The decisive certificate tests \(vM^kQ(M)w=0\) for every integer \(0\le k<37\), using the characteristic polynomial degrees and coefficients stated in RESULT.md. Since \(M\) is a \(37\times37\) integer matrix, Cayley–Hamilton extends the checked zero interval to all \(k\ge0\). Thus it is a complete finite proof component, not an extrapolation from initial terms.

The verifier checks only the binary-palindrome sumset and does not test originality against the literature. The recognition proof in RESULT.md explains why the finite-state machine represents the exact intended set of integer sums.
