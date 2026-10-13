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

# Verification instructions and limits

Execute `python verify.py` in an environment with Python 3.8+ and no third-party dependencies. It enumerates the explicit \(m\)-bit item masks, computes every cyclic adjacent-pair Boolean OR, compares their multiset against the complete nonzero output set, and checks the fixed pool cardinality, absence of adjacent pooled items, and exact total incidence for every \(2\le m\le13\). The expected last line is `VERIFY_OK`.

For a symbolic reconstruction, count the \(2^{m-1}\) output vectors carrying each fixed bit; each selected vertex is incident to exactly two tested edges, forcing \(|P_j|\ge2^{m-2}\). Equality requires that a pool contain no neighboring vertices. Inspect the four-step OR sequence from the explicit masks and the final wraparound edge to verify all outputs are unique and nonzero. Count the low bit's indices modulo four and higher bits' even indices to see every pool attain the lower bound.

The finite verifier is a reproducibility check for the explicit formulas, not exhaustive enumeration of arbitrary matrices and not a proof of the all-parameter theorem. The written covering lower bound and constructive identity provide that proof. No independent audit has been performed.
