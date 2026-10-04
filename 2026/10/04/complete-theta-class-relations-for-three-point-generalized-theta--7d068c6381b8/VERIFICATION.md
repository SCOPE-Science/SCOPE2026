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

The proof was checked by reconstructing the reduced Świątkowski complex after vertex explosion and identifying the relevant weight-two and weight-three syzygies with the Koszul complex on the edge differences. The key unbounded step is exactness of that Koszul complex; the finite computation is not used to infer the theorem for all \(m\).

`verify_theta_relations.py` builds the theta-to-exterior coordinate map for \(4\le m\le10\), checks the exact five-edge boundary relations over the integers, verifies reduction of every non-fixed-edge theta class to the fixed-edge basis, and checks the expected ranks modulo \(2,3,5,7,101\). Its recorded run ended with `VERIFY_OK`.

The literature checks separately identified that prior work already controls the numerical rank through first-homology and Euler-characteristic information. Verification therefore concerns the stronger equivariant module and complete relation claim, not novelty of the rank formula.
