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

# Reproduction

Run `python3 verify.py` in the same directory using Python 3 standard library. The program independently enumerates all indexed binary source words of length \(n\) with exactly three ones and generates actual cyclic length-\(k\) windows for each source. It checks correspondence between measured profiles and the four gap classes, full fiber cardinalities and the two stabilization counts for every \(2\le k\le10\) and \(n\in\{3k-1,3k,3k+1,3k+3\}\). This performs 36 complete source-domain cases with 53,325 words.

A separate analytic arithmetic loop for \(2\le k\le124\) and four source lengths per \(k\) checks 492 profile counts and that predicted source fiber sizes sum to \(\binom n3\). Expected success message: `VERIFY_OK 36 direct cases, 53325 indexed source words, 492 large-parameter combinatorial identities`.

# Interpretation and limits

These are exact finite enumeration and integer identities for the tested parameters, not an exhaustive infinite search. The infinite theorem rests on the correlation-inversion, long-gap, classification and placement arguments in RESULT.md. There is no independent scientific audit.
