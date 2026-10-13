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

# Verification and limits

`verify_matching_transition.py` independently constructs each \(2n\)-vertex graph adjacency matrix for \(3\le n\le8\) and \(0\le t\le n\), tests every labeled subset for domination and outside-neighbor capacity \(k=n-2\), and computes its minimum and number of minimizers. Both are compared with the proposed formulas and recorded in `matching_output.txt`. The executed verifier reports **39 profiles and 757248 labeled subsets**, with all comparisons passing. Run `python3 verify_matching_transition.py` using Python 3's standard library only.

The proof applies to every integer \(n\ge3\) and all \(0\le t\le n\) through direct case arguments. Finite test coverage is not a universal proof or claim of global priority. The baseline complete-bipartite value comes from Božović et al., arXiv:2606.22422, Proposition 1(iv). Independent audit has not been performed.
