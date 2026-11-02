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

# Reproducibility and limits

Run `python3 verify_local_profiles.py` with Python 3. The deterministic program creates two finite degree-three bipartite cyclic covers from independently chosen voltage assignments, checks the base's complete set of 133 short cycles, checks every voltage sum is nonzero, checks connectedness and degrees, computes exact rank-one triple extension diagrams with finite bitsets, and compares the resulting rank-two ordered-pair types across both covers. It also checks rank-three singleton-type agreement with the separately constructed symplectic quadrangle of order \((2,2)\).

The expected last line is `VERIFY_OK`; `verification_output.txt` records an actual successful execution. The algorithm computes extensions from adjacency matrices, without assuming the proposed fourteen-class theorem when calculating the logical signatures. Its inference from absence of all projected short cycles to absence of short cycles in the covers is a standard voltage-cover argument.

These are finite nonisomorphic test structures, **not** hexagon or octagon certification examples. They do not prove an infinite statement. The general theorem is established by the direct no-short-cycles extension analysis in `RESULT.md`. Independent scientific validation: not performed. The rank-five theory and all stronger logics remain outside the verified scope.
