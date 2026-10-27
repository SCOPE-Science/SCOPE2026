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

# Verification methods and limits

The standalone `verify.py` constructs each graph from original adjacency data, tests the super domination condition without using the symbolic proof, independently enumerates all three-state configurations, and computes the induced-component polynomial. All three complete coefficient dictionaries are asserted equal. The test spans every labeled simple graph with one through four vertices (75 graphs) and 108 fixed-seed base graphs of orders five, six and seven (183 total).

Run `python3 verify.py`. Its success line is `PASS: 183 base graphs, direct graph definition, induced-component expansion and 3-state homomorphism count agree`. It additionally checks the minimum coefficient and, for connected bases, the exact near-minimum coefficient and its equivalence to absence of a cut vertex.

The general polynomial is proved by a direct bijection, not inferred from these finite experiments. The counting-hardness theorem invokes published results of Dyer and Greenhill and does not offer a new independent complexity certificate. An inaccessible 2024 publication and potentially unindexed papers leave priority uncertainty. Independent audit has not been performed.
