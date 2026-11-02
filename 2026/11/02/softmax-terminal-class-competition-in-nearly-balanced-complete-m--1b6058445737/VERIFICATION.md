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

The accompanying `check.py` is standard-library Python 3. Run `python3 check.py` in a directory containing this file and the checker. It checks exact finite-state last-part probabilities for small complete multipartite graphs; cross-validates those by direct walk simulations with a fixed random seed; checks rational detailed balance in diverse graphs; and evaluates critical-window normalization at three rapidly increasing graph sizes. All checks completed without assertion failures. The exact finite values include \(K_{2,2,2}\) probabilities \((23/105,41/105,41/105)\) from part one.

These calculations independently exercise finite definitions and normalization identities; the infinite-dimensional probability claims are established by the written finite-state mixing and coupon-collector proof, not by the finite checks. No independent audit was performed. No external computational data or symbolic-library dependencies are required.
