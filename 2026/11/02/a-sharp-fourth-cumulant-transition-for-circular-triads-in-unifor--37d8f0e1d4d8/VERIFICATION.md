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

# Reproducibility and limits

Run `python3 VERIFY.py` with a standard Python 3 interpreter; no external packages or external data are required. The script was executed successfully, passing **156 exact assertions**. It independently enumerated all \(2^{\binom n2}\) equally likely tournaments for each \(3\le n\le6\); it also constructed signed incidence matrices and directly counted signed simple four-cycles for \(3\le n\le9\), checking the spectral fourth-trace and cumulant identities. The predicted polynomial sign was independently checked at integers through 100.

Finite checks are corroborative. The infinite claim is proved in `RESULT.md` by Rademacher-moment expansion and the exact spectrum of the signed line-graph adjacency. No Lean proof, independent external certification, or third-party audit was performed. Older paired-comparison priority remains uncertain where historical full text was inaccessible.
