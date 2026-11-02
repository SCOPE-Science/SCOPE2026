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

Run `python VERIFY.py` with a standard Python 3 interpreter. This independently recomputes the \(r\)-Stirling coefficients from their recurrence, checks each normalized conditional law against inclusion-exclusion, checks the deletion identity and log-concavity, and checks reverse-TP2. Every mapping \([n]\to[n]\) is also enumerated independently for \(n\le6\) to verify the joint \((C,Z)\) count table. The verifier executed successfully with **114389 exact integer assertions**. Adjacent minors were checked through \(n=38\), all separated minors through \(n=17\), and exhaustive maps through \(n=6\). The all-size proof rests on the recurrences and inequalities in `RESULT.md`, not on finite enumeration.

No external independent audit or formal proof certification has been performed. Known residual scientific risks are possible historical priority and the restriction to uniform self-mappings.
