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

# Direct verification and scope

The certificate is finite, exact and reproducible. Compile the two different C++17 implementations from `certificates/`, run each with arguments `12 13 124`, compare all length/count pairs against `certificates/counts.csv`, and run `python3 certificates/check_witness.py` from the package root. `certificates/replay_output.txt` contains recorded outputs that have already been regenerated from these exact source files. A run of the search with maximum depth \(124\) enumerates all normalized candidates through depth \(124\); no valid candidate at that length was found because every valid parent and every permitted next symbol is tested.

**Proof-to-computation linkage.** The normalized length-\(123\) leaf, all \(76{,}864\) search nodes and every depth count are calculated by two LCS implementations, one scalar and one bit-parallel. Alphabet orbit normalization accounts for the six distinct actual maximizers. The Python program checks every interval triple on the explicit word independently and verifies exact maximum ratio \(58/63\) (ten maximizing triples) and reversal-complement symmetry. The search excludes longer strings by prefix closure, not by a time limit or probabilistic sampling.

**Limits.** The computation establishes only a fixed finite parameter and a fixed three-symbol alphabet. The historical \(12/13\) numerical obstruction is already published. Publication-priority and independent external audit have not been performed.
