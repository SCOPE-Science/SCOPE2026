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

Run `python3 artifacts/verify.py` using a standard Python 3 interpreter. The script relies only on the standard library and makes no network calls. Its expected terminal marker is `VERIFY_OK`.

Checks performed: exact eight-by-eight signed transfer multiplication; the six-step all-state recurrence; exact even/odd half-turn boundary-vector identities; 478 instances of the twelve-column character and module-increment formulas; direct enumeration of invariant independent sets with permutation parity for all four automorphisms and each length \(2\le n\le7\) (24 cases); and independent mod-two augmented boundary ranks at lengths \(n=2,3,4,5\). The enumerated independent-set counts in these four homology checks are \(41,227,1234,6743\), respectively.

The matrix identities and the published homological-concentration theorem give the uniform proof. Finite enumerations are error checks and do not provide an infinite search certificate. No external audit, computer-assisted formal proof, or integral-module splitting has been performed.
