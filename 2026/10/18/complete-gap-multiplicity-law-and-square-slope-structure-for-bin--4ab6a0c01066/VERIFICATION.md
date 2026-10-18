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

# Reproducing the arithmetic tests

Run `python3 verify_gaps.py` with a standard Python 3 interpreter. The script needs no third-party dependencies or outside data. It computes \(Q_{a,b}\) coefficients from the truncated product of two geometric series, then reads consecutive nonzero exponent differences. Separately it constructs the predicted histogram from modular inverses and floor sums, and verifies equality on 3,256 coprime pairs. It also cross-checks the nonstandard triangular insertion lemma directly for all coprime remainders, distances and intermediate residue subsets at \(2\le a\le27\). Four small explicitly stated cases are also checked. Expected terminal line: `VERIFIED: 3256 coprime pairs; exact coefficient gaps and square-slope formula`.

# What is, and is not, certified

The proof is in `RESULT.md`; finite checks do not establish its infinite claim by themselves. In particular, the key reflection and triangular insertion lemma require the mathematical argument there, not brute-force evidence. All counted pairs are exact, deterministic arithmetic tests. The checked parameter range is explicitly coded, not all possible \(a,b\). Prior-work priority and the theorem remain subject to independent scrutiny. No independent audit has been performed.
