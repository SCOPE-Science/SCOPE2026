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

The reproducible program `verify.py` is a dependency-free Python 3 script that constructs all arc subsets for bidirected length-two stars with arm counts one through seven. It compares actual and predicted complete face enumerators; confirms the local degree and opposite-arrow constraints; pairs every face outside the outer-edge cross-polytope complex and no face inside it; directs all face-poset Hasse covers and checks an acyclic topological sort; and checks the explicit signed integral fundamental cycle and permutation/reversal actions. Its reference output is embedded in `verify_output.txt`.

The program exhaustively verifies the 63,423 faces and 381,024 covers of the seven-arm instance. Reproducing finite certificates does not prove the result for arbitrary arm count; the general proof is the explicit symbolic matching and monotone-cover acyclicity argument in `RESULT.md`. No independent audit has been undertaken. No claim about general bidirected trees or a symmetry-equivariant collapse is included.
