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

The proof is analytic and does not depend on computation. The executable check `verify_forced_biclique.py` independently implements the three-colour forcing rule on \(K_{m,n}\), compares forcing success against the claimed structural classification, and compares domain-size counts against the stated generating polynomial.

The checked range is \(1\le m,n\le5\). The exhaustive run covers \(25\) biclique types and \(1,860,496\) partial assignments. Its exact output is recorded in `verification_output.txt` and is:

`ALL CHECKS PASSED; biclique_types=25; partial_assignments=1860496; forcing_assignments=19494`

The finite range is a stress test only. It is not used to infer the theorem for larger parameters. The unrestricted result is justified by the structural proof in `RESULT.md`.
