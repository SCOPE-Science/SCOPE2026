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

# Verification of the bidirected cube result

Run `python3 verify.py`. Only the Python 3 standard library is required. The script uses exact integer arithmetic throughout. It builds the directed 24-arc cube twice: by extension of admissible arc sets and by all partial functions from the eight source vertices to cube neighbors with distinct targets and no directed cycles. The enumerations agree on 6,496 nonempty simplices and give face vector `(24,216,928,2016,2160,1008,144)`.

The script then constructs all 29,136 signed codimension-one incidences, applies 3,196 deterministic elementary Morse pairs in the explicitly declared 24-arc order, and topologically sorts every cell of the reversed-matching Hasse digraph to establish acyclicity. Exactly 104 critical cells survive, with counts `(1,0,0,7,47,37,12)` by dimension. The signed gradient reduction computes the integral Morse differentials. Every nonzero entry of the fourth and fifth differentials is checked against a rank-one factorization through a unit pivot; the sixth differential is identically zero. No torsion-producing Smith factor is possible. Consecutive differentials compose to zero. Direct Gaussian elimination on the original, unreduced simplicial boundaries over the field with two elements independently confirms their ranks.

Expected final marker: `VERIFY_OK`, with integer Betti counts `{0:1,1:0,2:0,3:6,4:45,5:36,6:12}`. The zero- and high-degree boundary conventions are explicit in the proof. The checker establishes the integral homology and the existence of an acyclic matching; it does not determine higher attaching maps or the full homotopy type. Independent audit is not performed.
