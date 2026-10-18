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

The standalone `verify.py` computes open-neighborhood signatures from the adjacency relation of each rook graph, and directly checks uniqueness, total open domination and induced selected degree exactly one. It exhausts all even vertex-subsets on twelve small labeled boards; odd subset sizes cannot satisfy the induced-degree-one condition. It checks examples both with and without solutions, including the nontrivial mixed cases \((3,3)\) and \((4,5)\).

`verification_output.txt` is the output of `python3 verify.py`, ending with `VERIFICATION_OK`. Explicit larger constructions serve as independent positive tests but are **not** complete enumerations at those dimensions. The infinite-family existence, exclusivity and factorial counts depend on the four-step proof in `RESULT.md`, not on numerical extrapolation.

Self-review of the proof and literature comparison was completed. Independent audit is not yet performed.
