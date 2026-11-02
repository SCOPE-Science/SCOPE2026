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

# Reproducible verification
Run `python3 check_borel.py` with the standard Python library. This uses an independent closure-under-Lie-brackets algorithm and checks its output against the rank characterization of all sampled tuples. The expected output is `check_borel_output.txt`; the final line is `VERIFY_OK`.

Exhaustive coverage, rather than sample testing, was achieved only for all tuples with \((q,k)=(2,1),(2,2),(2,3),(3,2)\). Samples for \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_4\) test the criterion but do not certify all tuples over those field/length pairs. The \(\mathbb F_4\) implementation uses the irreducible polynomial \(z^2+z+1\). Finite tests alone are not a proof for all fields; the proof is symbolic and given in `RESULT.md`.

Scientific literature comparisons and residual priority risks are documented in `REVIEW.md` and `AUDIT.json`. Independent audit is not performed.
