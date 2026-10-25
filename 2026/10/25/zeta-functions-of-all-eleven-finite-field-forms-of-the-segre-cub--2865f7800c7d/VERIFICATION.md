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

Install the dependency listed in `requirements.txt`, then run `python verify_segre.py` and `python verify_finitefield.py` from the extracted directory. The first program reconstructs the 15 perfect matchings, ten nodes, and 20 parity-ordered ruling labels, computes the eleven coefficient pairs without reading them from the proof, and independently checks the 25-generator/nine-relation rational boundary divisor presentation together with rank-16 generation. The second program constructs actual field extensions of \(\mathbb F_5\) of degrees one through six and counts projectivized trace-zero/cube-trace-zero solutions for every degree-six étale algebra partition, reproducing all eleven \(q=5\) counts.

The finite-field check is exhaustive **only** for the eleven models over \(\mathbb F_5\). Arbitrary-characteristic and arbitrary-extension assertions are deduced by the geometric resolution, algebraic cohomology, and Grothendieck–Lefschetz trace argument in `RESULT.md`; the program alone does not constitute such a proof. The geometric ingredients are sourced in the references. Independent mathematical auditing has not been performed.
