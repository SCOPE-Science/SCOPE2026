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
# Exact reproducibility

Execute `python3 verify.py` using Python 3 and its standard library. The program checks the 30-state complete carry transducer; every zero-tail fixed-point equation; the exact correlation at unit spacing; all 16 possible low-five-bit odd prefixes; both exceptional affine branches (including both parity phases); all stable-sign identities on the unrestricted parameter half-line \(t\geq7\); and supplementary exact binary-prefix comparisons at 14 lags.

Expected result begins with `VERIFY_OK` and prints the sample odd correlations \(C(3)=-1/8\), \(C(5)=-1/8\), \(C(7)=3/16\), \(C(9)=-1/16\), \(C(11)=-1/32\), \(C(13)=-7/32\), \(C(15)=7/32\), and \(C(17)=3/32\).

The claimed infinitely many spacings are covered by exactly checked finite-state closure and the symbolic induction; 14 finite comparisons are only supplementary. The original Rudin–Shapiro sequence, normalization, Cesàro convention and dependence shape are specified in `RESULT.md`. No independent audit has been performed.
