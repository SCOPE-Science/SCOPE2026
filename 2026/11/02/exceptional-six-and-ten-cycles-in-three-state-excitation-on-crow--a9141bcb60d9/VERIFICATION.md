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

# Reproduction and boundaries

Run `python3 verify_crown_gh3.py` in a directory containing that file. Only the Python 3 standard library is required. The code exhausts all 19,683 clipped matched-pair signatures, computes recurrent signature cycles and lifts them by transporting all occupied pair types. It confirms the exceptional six- and ten-cycle classes, maximal transient six and the sharp size-dependent boundary cases.

An independent direct vertex-level update computes the dynamics of every one of 597,870 labelled colourings for shore sizes one through six. At size five, it also computes all 59,049 colourings under the distinct cyclic-contact rule and confirms identical period-ten basin membership for the two rules. The successful completion marker is `CROWN_GHM3_VERIFY_OK` ; the successful check prints the indicated marker.

Finite small-size enumeration is not a proof for unbounded shore sizes. The unbounded conclusion relies on the separately stated proof that the clipped nine-trit model is an exact factor and that recurrent occupied-type maps are permutations. Source/log replay checks that finite computational lemma, not any external certification. Independent audit remains unperformed.
