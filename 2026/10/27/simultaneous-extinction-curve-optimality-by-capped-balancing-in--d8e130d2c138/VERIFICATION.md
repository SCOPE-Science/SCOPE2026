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

# Reproducibility and checks

Run `python verify.py` from this directory using Python 3 standard library only. Compare standard output parsed as JSON with `certificate.json`, ignoring whitespace and key formatting. The checker enumerates all group-label removal words for eight small parameter vectors and compares their maximum area to the capped-balancing schedule. It enumerates all \(2^{\binom n2}\) simple labeled graphs for \(1\le n\le5\) and all \(2^n\) removal subsets per graph, testing both unrestricted optimal orders and every degree-descending order with arbitrary tie breaking. The first strong degree-ranking failure is ten labeled copies of \(K_{2,3}\) at five pollinators. All comparisons are exact integers.

The all-size theorem is established by the balancing proof in `RESULT.md`, not by finite checks. The finite classification is an exhaustive computation proved correct by the specified recurrence and executable complete enumeration. No independent scientific or external verification has been performed.
