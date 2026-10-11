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

The analytic proof establishes the infinite family. `verifier.py` replays the algebraic components without external packages: the Newton identity is checked exactly on \(729\) integer triples; every two-value multiplicity is checked exactly for \(2\le m\le200\); equality and Fourier scaling are checked in \(1185\) cases; and \(5700\) random complex zero-sum vectors are used as regression tests. The recorded output is in `verification_output.txt`.

The random checks do not certify the theorem and are not used to infer an infinite statement. The proof's substantive limits are that it treats exponent \(6\) and subgroup-complement spectra only. Independent validation has not been performed.
