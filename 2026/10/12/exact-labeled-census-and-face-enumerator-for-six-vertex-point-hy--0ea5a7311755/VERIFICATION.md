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

`verify.py` exhausts all \(2^{20}\) labeled 3-uniform hypergraphs on six vertices. For each mask it checks the tetrahedron condition on all \(15\) four-vertex subsets. It then constructs every relabeling of the seven-face octahedral obstruction under all \(720\) permutations, verifies that the orbit has \(120\) distinct members, removes that orbit, and checks the exact face distribution.

A second stage partitions the surviving masks into full \(S_6\)-orbits. It verifies that there are \(174\) orbits, checks every orbit size against the reported profile, and checks that the weighted orbit sum is \(50{,}214\). The final output is stored in `verification_output.txt` and ends with `VERIFY_OK`.

The finite verifier establishes only the census conditional on the six-vertex iff criterion. It does not reprove Theorem 5.16 of arXiv:2610.05311v1, and no conclusion is asserted outside its characteristic-zero algebraically closed scope.
