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

Run `python verify.py` with a Python 3 standard-library interpreter. The observed result was:

```
VERIFY_OK checks=75521
```

The checker enumerated all time permutations for each pair of positive leaf counts at most four and total leaf count at most six, checking the combinatorial schedule law, exact moments, and optimizer characterizations. It independently executed the infection event process, averaging over every initial infected vertex and every transmission-outcome mask for small cases at rational probabilities. It also checked reproducible selected calendars at larger parameters. Those checks are finite and supplement, rather than replace, the written universal combinatorial proof. No formal or independent verification was conducted.

The variance shown in the finding refers exclusively to variation of \(R(\pi)=\mathbb E[Z\mid\pi]\) under random calendars; it is not \(\operatorname{Var}(Z)\). The theorem assumes one encounter per edge and permanent infection during the calendar.
