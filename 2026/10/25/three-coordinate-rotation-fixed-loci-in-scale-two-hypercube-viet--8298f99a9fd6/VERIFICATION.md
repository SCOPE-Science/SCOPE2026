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

# Computational verification and mathematical scope

Run `python3 verify_fixed_c3.py` in the containing directory. The code uses only Python's standard library and verifies the four exact three-bit cyclic orbits and their complete maximum-Hamming-distance matrix. The checker independently verifies all 43,434 distinct orbit-vertex pairs over \(3\leq n\leq9\), compares every computed orbit edge with the explicit rule, builds full orbit-complex face sets for \(3\leq n\leq7\), and verifies 620 free-face pairs by checking the exact remaining coface set at each elementary collapse. For \(3\leq n\leq6\), independent mod-two simplicial boundary ranks reproduce the expected reduced Betti vectors. The final face sets exactly match two copies of the smaller Rips complex plus two edge-paths per remaining cube vertex. The supplied `verify.log` contains actual output from the complete run ending `VERIFY_OK`.

The general PL correspondence, orbit distance identity, local link and free-collapse proof in RESULT.md apply for every integer \(n\geq3\), with integral homotopy conclusions. Numerical tests alone cannot prove that unlimited statement or determine integral attaching maps. Independent scientific audit has not been performed.
