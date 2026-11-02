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

# Verification and reproducibility

Run `python3 verify.py` using Python 3.10 or later, with no external packages or network. The script builds Boolean-cube adjacency and Walsh restriction matrices from definitions, and uses exact modular elimination over the prime field with 1000003 elements. It checks 280 frequency-sector ranks for dimensions two through eight, 25 directly formed full-Hamiltonian Krylov ranks for dimensions two through six, and 454 exact integer Catalan and threshold identities in the tested range. The observed output is:

```
EXACT_WALSH_SECTORS 280
EXACT_KRYLOV_CASES 25
VERIFY_OK checks=759
```

The low-radius controls are retained to test boundary behavior; the reviewed new result is limited to \(d\ge6\), \(2\le r\le d\). Small finite-field cases independently test the formulas but cannot establish all characteristic-zero ranks. The analytic proof in `RESULT.md` uses the cited characteristic-zero maximal-rank theorem for subset-inclusion matrices. No independent scientific audit has been performed.
