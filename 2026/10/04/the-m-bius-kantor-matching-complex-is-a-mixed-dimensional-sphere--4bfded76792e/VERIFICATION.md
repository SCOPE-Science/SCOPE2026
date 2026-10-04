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

Run `python3 verify_mobius_kantor_matching.py` with the Python standard library.

The verifier reconstructs the generalized Petersen graph \(G(8,3)\) and checks: all \(11{,}068\) graph matchings; face vector \((24,228,1096,2826,3816,2444,600,33)\); the fixed \(5{,}525\)-pair staged face-poset matching; all \(53{,}256\) nonempty face-poset covers; global directed acyclicity; critical profile \((1,10,6)\) in dimensions \((0,4,5)\); the signed degree-\(5\)-to-degree-\(4\) Morse boundary with Smith form \(\operatorname{diag}(1,1,0,0,0,0)\); and independent \(\mathbb{F}_2\) Betti vector \((1,0,0,0,8,4,0,0)\).

The verifier prints `VERIFY_OK` only after all assertions pass.

Limits: this is a complete finite certificate for this graph. It does not certify an infinite family or originality. The homotopy conclusion also uses the standard identification \(\pi_4(\bigvee^{10}S^4)\cong\mathbb{Z}^{10}\), so the degree matrix classifies the \(5\)-cell attaching maps.
