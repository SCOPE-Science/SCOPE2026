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

Run the standalone standard-library Python 3 script `python3 artifacts/verify.py` from the package root. It constructs the windmill graph from labeled vertices and edges and independently enumerates stable simplicial faces through graph-edge orbits. It evaluates their signed reduced Lefschetz numbers for every tested group element; compare with the predicted characters in RESULT.md. It also constructs all matching faces, computes exact reduced boundary ranks over \(\mathbb F_2\), and tests 120 group-average rational quotient predictions. Expected final markers are `WINDMILL_QUOTIENT_PREDICTIONS_VERIFIED 120` and `WINDMILL_FULL_WREATH_CHARACTER_VERIFIED 1128`.

The verifier covers 1,128 automorphisms, 13 boundary-rank computations including a 43,658-face complex, and 120 predicted quotient parameters. Its finite success does not establish the infinite theorem or integral lattice; those follow from the homotopy recurrence and integral relative exact sequence. No external or independent mathematical audit has been performed.
