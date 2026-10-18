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
# Verification of the finite claim

Run `python verification.py` with Python \(\ge3.9\). Standard-library modules alone suffice. Its output must agree with `verification_output.txt`, including the terminal `VERIFY_OK`. The program reconstructs the Petersen graph as the disjointness graph of the two-element subsets of a five-set. It first proves four colors are necessary by exhausting the six perfect matchings and checking that each complementary two-factor consists of two odd cycles. It then enumerates colorings directly and independently as four matching classes.

For all \(49{,}920\) assignments, it checks legal one-edge recolorings by two formulations, reciprocal graph edges, complete connected components by flood-fill and disjoint-set union, frozen-state characterization, the \(S_5\times S_4\) orbit and parity behavior of the large components. All equalities are assertions; the run is exhaustive, not sampled. Its code is supplied alongside the scientific statement rather than inferred from an unverified output log.

Only the finite enumerated claim is established. The code does not certify novelty, imply generalization to arbitrary cubic graphs, or replace independent validation. The count of all edge colorings agrees with the already known OEIS entry A159233.
