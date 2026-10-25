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

- Reconstructed the 11 square-free supports in Proposition 7.3 for \(n=4\).
- Enumerated all \(2^{20}\) vertex subsets and checked the vertex-cover and minimality predicates exactly.
- Obtained 50 minimal vertex covers, all of size 4; their complements are 50 facets, all of size 16.
- Verified the pure shelling criterion for every ordered pair in the listed facet order.
- Re-ran the included Python program and compared its output with `nested_hilbert_n4_shelling.expected.txt`.
- Limitation: the verification is for this finite complex only. It does not certify a general-\(n\) statement or the positive-characteristic singularities of the original nested Hilbert scheme.
