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

Run `python3 verify.py` and `python3 verify_general.py` using only Python's standard library. Both reconstruct the defining physical tandem-duplication channel, the derivative and the root signature for each tested word. `verify.py` checks all shorter blocklengths and the first boundary for two alphabets at duplication length two. `verify_general.py` also checks duplication lengths three and four for binary alphabets, with independent exact per-fiber subset optimization.

Expected terminal messages:

`VERIFY_OK q2_n7_maximum=84 q2_n7_maxima=2176782336 q3_n7_maximum=1719 first_strict_length=7 direct_signature_conflicts_agree=true`

`GENERAL_VERIFY_OK q2_k2 q3_k2 q2_k3 q2_k4 checked`

The two direct-output and signature distance predicates agree on all tested word pairs within every root fiber. The tested first-onset size pairs are \((84,80)\), \((1719,1701)\), \((776,768)\) and \((6928,6912)\). Every possible local subset is checked in each tested fiber; the huge global equality counts are obtained by multiplication of the independent local choices and independently checked against the proved product expression.

This finite validation does not prove the all-alphabet, all-duplication-length claim by itself. The universal proof is the complete symbolic classification of the only root-signature fiber types possible before and at length \(3k+1\), as presented in RESULT.md. No formal or independent validation has been performed.
