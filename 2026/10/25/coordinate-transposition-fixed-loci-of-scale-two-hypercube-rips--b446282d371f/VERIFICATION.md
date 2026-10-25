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

# Reproducible checks and their limits

The standalone `verify.py` uses only Python's standard library. Execute `python3 verify.py` from this extracted directory and compare against `verify_output.txt`. All file contents are embedded with this result.

For each \(m=1,2,3,4\), the program independently builds all orbits of the coordinate swap on \(Q_{m+2}\), checks actual binary Hamming distances against the explicit orbit adjacency formula, enumerates every resulting simplex, and computes reduced mod-two Betti numbers from boundary matrices. It checks the predicted multiplicities separately for dimensions two and three and the vanishing of every other reduced Betti number. The expected vectors are \((\beta_2,\beta_3)=(1,0),(5,0),(17,2),(49,18)\).

For \(m=1,2,3\) it independently enumerates ambient Rips faces and computes the signed trace of the transposition on each simplicial chain degree. The alternating Lefschetz sums are respectively \(2,6,16\), as required by the fixed-space Euler characteristics. The total counted orbit faces are 2,468, and the output terminates in `VERIFY_OK`.

These tests are finite and mod-two (except for the signed integer Lefschetz sums). They cannot by themselves rule out integral torsion or higher attaching maps; those are resolved by the cone-link and spanning-tree cancellation proof in `RESULT.md`. No independent audit has been performed.
