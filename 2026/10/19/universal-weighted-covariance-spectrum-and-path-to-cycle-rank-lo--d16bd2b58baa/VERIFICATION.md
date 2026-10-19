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

# Reproducibility of the finite checks

The analytical proof in RESULT.md covers all \(q\ge2\), all full-support \(p\), and every allowed sample size; exhaustive numerical checks are supporting checks, not an infinite-domain proof.

Run `python3 verify_bigram.py` with Python 3 and standard library only. The script enumerates **25** exact-rational iid probability laws (alphabet sizes two, three, four; selected sequence lengths two through six), each in its admissible open and cyclic configuration. For every case it enumerates every sequence with its rational probability, forms all directed bigram counts, recomputes means and every covariance entry directly, and checks each against the independent closed formula. It also verifies all symmetric and antisymmetric alphabet-potential eigenvector equations, every independent interaction-basis eigenvector equation, the scaled covariance trace and constant null direction. The script printed:

`PASS 25 exhaustively enumerated laws with q in {2,3,4}, n in {2,...,6}, exact rational nonuniform probabilities, path/cycle configurations.`

The two central exact variance identities are reconstructed directly from the row/column Hoeffding decomposition and endpoint telescoping. The central limit theorem used for the Pearson corollary is the usual one-dependent bounded-vector CLT; the code does not establish that asymptotic theorem by experiment. Its claim of historical priority also remains subject to the disclosed older-paper access limits.
