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

# Reproducible checks

From the directory containing this document and `verify_broom.py`, run `python3 verify_broom.py` using Python 3 without external packages. The script directly enumerates all percolation states on every candidate vertex-deleted graph for \(2\le k\le4\), \(2\le L\le7\) and \(p\in\{1/3,2/3\}\), using exact rational arithmetic. It compares the expected outbreak with independently calculated pair connectivity, verifies closed score differences, evaluates the integer switch-existence criterion for \(2\le k\le5\), \(3\le L\le25\), and checks the established eight-vertex switching benchmark at six rational \(p\) values. The tested program returned `PASS 306 independent exact enumerations; 126 difference identities; threshold and benchmark checks PASS`.

The mathematical proof, not numerical enumeration, establishes the infinite parameter theorem. No probabilistic Monte Carlo simulations, external proof-assistant runs, or independent scientific audits are claimed. The source comparisons are bounded by the actually readable material, with the subscription-gated site-bond paper assessed only through its abstract.
