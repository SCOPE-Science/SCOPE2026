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

Run `python3 verify.py` with a recent Python 3 interpreter. The verifier has no external dependencies. It checks the explicit finite-field arithmetic for \(\mathbb F_4\), and directly enumerates every possible one-insertion parent for each tested received word, deduplicating equal parents by storing tuples in a set. For every tested nonzero check vector it compares the maximum directly enumerated list size to the separately computed rank formula.

The recorded run checked \(1{,}574\) check vectors and \(131{,}395\) received-word cases. All length-\(4\) quaternary and quinary check vectors are included; the length-\(4\) septenary cases are a fixed pseudorandom sample of size \(45\). The boundary counterexample for a binary alphabet below the hypothesis is checked separately. See `verification_output.txt` for the complete standard output ending in `HYPERPLANE_LIST_VERIFY_OK`.

These finite computations cannot certify the theorem for all field orders. The theorem is instead established by the insertion-gap count, the strict inactive-gap bound, and the finite-field hyperplane-union argument in `RESULT.md`. No independent audit or independent validation is claimed.
