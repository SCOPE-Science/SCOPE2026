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

The state set is exactly \(3^{10}=59049\) labelled ternary colorings for each of \(GP(5,1)\) and \(GP(5,2)\). The recorded complete transition tables have 59049 32-bit little-endian destination indices each. From the package root, execute `python3 verification/check.py` to check every transition, reconstruct all directed cycles and basins, verify the exact JSON result certificate, and enumerate the full graph-automorphism groups by adjacency-constrained backtracking. This uses Python's standard library only.

A second, independently implemented method is compiled with `g++ -std=c++17 -O2 verification/check_independent.cpp -o independent_check` and run with `./independent_check`. Its output must match `verification/independent_results.txt` exactly. Unlike the first program, it classifies recurrent components by exploring entire trajectories and marking active paths rather than by indegree peeling. Both code paths were actually executed and gave identical period-by-basin-by-entrance cells on all 118098 total labelled graph states.

The certificate gives primitive periods \(\{1,3,4,5,7\}\) and \(\{1,3,4,5,8\}\) respectively, with longest initial transient eight and six. It also supplies exact sharp-transient and exceptional-period witnesses. The symmetry checker verifies every adjacency-preserving bijection and computes the orbit partition under its action. This is an exhaustive finite proof, not a statistical test or a proof for all generalized Petersen parameters.
