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

The proof in `RESULT.md` is an integer-presentation proof valid for all \(n\ge3\), \(1\le t<n\), including the one-unmatched-vertex endpoint. Its pivotal claims are the redundant sink row, the eliminated matched relation \(n(U+V)=0\), and the final \(2\times2\) Smith form with gcd \(1\).

Run `python3 verify.py` using Python 3.9 or newer. The packaged code uses only the Python standard library, builds each reduced Laplacian from graph edges, performs exact integer unimodular Smith reduction, and compares all nontrivial invariant factors for \(3\le n\le10\). Its observed output is:

```
VERIFY_OK full_smith_cases=44 orders=3..10 intermediate_matching_deletions
```

A SymPy-based Smith calculation separately checked \(65\) instances for \(3\le n\le12\); that separate calculation is supporting evidence, not a packaged dependency. Neither finite experiment certifies all parameter values or establishes originality; the mathematical proof supplies the universal result. Independent mathematical audit remains not performed.
