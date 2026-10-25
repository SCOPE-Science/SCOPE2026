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

# Verification of cherry/root-split moment localization

Run `python3 verify.py` using only the Python standard library. It checks the exact YHK cherry law propagated from the leaf-splitting transition, all conditional first and second moments for each \(10\le n\le65\) and \(1\le k<n\), and the mean/variance identities for the extreme-root event. It separately enumerates every possible uniform leaf-selection history on a rooted binary tree through eight leaves and confirms uniform root-split counts. The script prints 4,228 exact arithmetic/history assertions when successful.

The finite computations do not establish the all-size theorem or historical priority. The proof uses the Pólya-urn split law, conditional independent YHK subtrees, and the published marginal cherry-moment formulas, with all small-subtree corrections displayed in RESULT.md. Independent external audit is not performed.
