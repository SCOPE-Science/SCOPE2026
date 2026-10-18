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

# Verification

Execute `python3 verify_binary_chords.py` using Python 3 standard library. The script independently rebuilds the cycle with chords \(\{n,2^j\}\) for \(2^j\le n-2\), computes a target-specific witness, checks its label sum, and checks induced connectivity by breadth-first search. Every target is checked for \(3\le n\le80\); additional reproducible sampled targets reach \(n=65{,}537\). The exact one-line expected output appears in `verifier_output.txt`.

The mathematical proof establishes the infinite statement, not the sampled testing. The verifier does not establish minimality of the chord set, and no external audit has been performed.
