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

# Finite verification

Run `python3 verify.py` in the directory containing the code. No third-party packages are needed. The program checks the complete \(2^{16}\)-choice successor-pairing space of the binary order-five de Bruijn graph and independently traverses all edge-simple Euler circuits fixed at the unique zero edge. These procedures give equal sets of \(2048\) cyclic rotation classes. All classes pass the direct check that each length-five circular factor is unique.

For every class, direct circular-window discrepancy is compared with the prefix-walk range; distinct Parikh-vector enumeration is compared with an independent sliding-window min–max calculation. Each of the eight claimed cells is checked exactly, including the absence of other cells. The symmetry-orbit decomposition under reversal and complementation is also checked. The program verifies known cycle counts at binary orders one to five.

Recorded successful execution: `VERIFY_OK independent_euler_and_pairing_generators=2048 pairings_tested=65536 independent_discrepancy_algorithms=2 independent_abelian_peak_algorithms=2 rooted_windows_tested=2031616 joint_cells=8 symmetry_orbits=528 histogram=5-6:224,6-6:304,6-7:384,7-6:48,7-7:640,7-8:224,8-8:192,8-9:32`.

These finite computations, together with the completeness proofs in `RESULT.md`, prove the stated finite claim. They do not prove an analogous formula at larger orders or establish historical priority; no independent external review is represented.
