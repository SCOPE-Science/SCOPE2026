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

# Reproducibility

Run the included standalone Python file with a standard Python 3 interpreter:

```sh
python verify_star_idempotents.py
```

The verifier enumerates every partial transformation, including the empty map, for \(S_{m+1}\) with \(1\le m\le6\). It independently evaluates \(f^2=f\), checks graph edges against the definition of each monoid, records exact image-rank histograms, and compares them to the polynomial formulas. It printed `ALL SIX RANK SPECTRA VERIFIED THROUGH SIX LEAVES` and the six total-idempotent vectors given in `RESULT.md` when run on the accompanying source.

The exact formulas and the asymptotic limits are proved mathematically for every \(m\ge1\) in `RESULT.md`; exhaustive enumeration through six leaves alone cannot verify statements for all \(m\). No independent audit or third-party verification is asserted.
