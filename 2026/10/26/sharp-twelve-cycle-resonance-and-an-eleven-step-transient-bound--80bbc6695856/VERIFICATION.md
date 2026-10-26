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

The result follows from an exact finite abstraction, not from numerical extrapolation. For each of the three parts and each of its three states, truncate the exact count at two. The excitation threshold is preserved, so the complete deterministic quotient has 19,683 states. The tagged-vertex product has 177,147 states, sufficient to recover the evolution of every labelled vertex for arbitrary part sizes.

`verify.py` reconstructs this quotient directly from the update rule, verifies \(T^{23}=T^{11}\) for **every** tagged state, and finds 108 nonmatching states at the preceding bound \(T^{22}\ne T^{10}\). The separately checked labelled configuration on \(K_{5,2,3}\) shows that the eleven-step bound is also sharp for an actual graph. The script checks the period-two and period-six exclusions for every capped occupancy profile and verifies by exact set equality that there are precisely 42 primitive-twelve capped population patterns, all of the two-large-one-small form.

A separate direct vertex-level implementation (no capped profile used to generate its transitions) checks nine graph sizes, including \(K_{4,4,1}\), \(K_{4,4,2}\), \(K_{4,4,3}\) and \(K_{4,4,4}\). Exact multinomial profile sums are compared with the corresponding direct periodic-state totals. The precise command to rerun is `python3 verify.py`, from a directory containing the file. The output is embedded as `verify_output.txt`.

The finite quotient lemma and the deterministic dynamics prove the all-size theorem; the direct small-graph checks are additional corroboration only. The proof and program do not claim a result for other thresholds, more than three independent parts, stochastic rules, or independent external validation.
