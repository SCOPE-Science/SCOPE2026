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

# Reproducibility

Run `python3 verify.py` from the extracted artifact directory. The program uses only Python's standard library and computes integer partition numbers by the complete product-generating-function dynamic program, not floating-point approximations.

The exact certificate tests all \(2925\) off-diagonal triples \(0\le a\le25,\ 1\le r<s\le26-a\), all \(26\) saturated diagonal caps, and all \(325\) off-diagonal comparisons with \(s=26-a\). It checks all \(562475\) admissible pairs through \(n=150\) and independently reconstructs joint probabilities by enumerating every integer partition for \(2\le n\le14\) (\(506\) distinct partition objects). The results do not constitute an exhaustive check over unbounded sizes. The all-size implication instead follows from the proved cap-propagation lemma and the published strict log-concavity of the integer partition numbers at every index at least \(26\) [2].

The sign table and exceptions are reproducible without external software. The published theorem [2] was verified from the primary paper's text and statement, not reproved independently. Historical novelty is conditional on the compared, accessible literature; it is not certified independently.
