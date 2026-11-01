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
# Verification and mathematical limits

The standalone Python 3 script `check.py` was executed against the files in this package. Its actual output is embedded in `verification_output.txt`. The program reconstructs the \(m\)-state Markov matrix, tests the invariant cell density with exact rational fractions, verifies affine first-return branches and their slope \(-m\) with exact rational samples, and checks the Perron root, both entropies and maximal-entropy cell occupations at \(m=2,\ldots,12,32,128,512\).

The infinite family claims, uniqueness of the two invariant statistical laws, the almost-everywhere basin statement, the topological entropy identification and the large-\(m\) limits require the written proof; finite experiments are not substituted for them. The source statements were examined in the cited material. An independent audit was not performed.
