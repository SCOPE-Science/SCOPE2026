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

Execute `python3 verify.py` from the directory containing this document and the script. No external Python packages are required.

Expected terminal result:

```
VERIFY_OK sampled_lengths=14 valuations=12 prefix=393216 widths=1..5 published_first_failures=11,43 arithmetic_triples=343
```

The checker enumerates all length-\(n\) factors *within a specific finite 393216-symbol prefix* for fourteen selected \(n\)'s, compares their Parikh spectra with the predicted parity rule, and checks representative valuations. It confirms the initial five extremal-width recurrences for the sampled factors and the first failure lengths reported in the 2024 source for two valuations. It also checks the collision criterion on 343 short-range integer triples using a deliberately synthetic parity spectrum, without treating that model as an actual factor census. It does not establish that finite-prefix factors exhaust the infinite word's factor language; that infinite characterization comes from the cited 2014 theorem. The closed-form classification and unbounded deficits are deduced in `RESULT.md` from that theorem, not inferred from finite enumeration.

Public scientific review is same-model only; no independent audit has occurred.
