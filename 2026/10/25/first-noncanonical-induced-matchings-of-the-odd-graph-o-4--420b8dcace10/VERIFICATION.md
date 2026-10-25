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
# Reproduction of finite checks

Execute `python3 verify.py` with standard Python 3. No external packages, network, unpublished tables, or precomputed archives are required. This program creates exactly \(35\) vertices and \(70\) edges, checks that the seven omitted-point labels each contain \(10\) edges, independently enumerates induced matchings with a fixed edge for sizes seven and eight, then exhaustively traverses all size-seven and size-eight matchings. It independently applies all \(5{,}040\) permutations of the ground points and confirms all seven symmetry orbits. The successful run prints `VERIFY_OK`.

Observed output includes `anchored 7 642`, `anchored 8 36`, `total size 7 6420 mixed size 7 5580`, `total size 8 315 mixed size 8 0`, and `VERIFY_OK`. The mathematical meaning of the exhaustive search and the only safe pruning criterion are explained in RESULT.md. Code execution verifies a finite statement, not any infinite generalization.

No independent audit has been conducted. The 2012 almost-intersecting-family paper was not read in full; possible overlap is a limitation of the literature comparison.
