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

Use Python 3 and run `python3 checker.py` from the directory containing the embedded standalone files. The checker constructs \(C_8\) literally from the defining morphism and computes the earliest duplicated *string factor* by a dictionary of complete substrings, with no hash-only identity approximation. It checks every \(1\le n\le729\) against the piecewise formula. It separately checks both generic block distinctness statements for 256 combinations of block lengths and endpoint-one binary words, through length eight. The local execution reported:

```
PASS 729 full first-repeat scans; 256 generic block tests; word length 6561
```

For hand verification, the first-repeat indices at \(n=1,2,3,4,7,9,10,27,28,81,82\) are, respectively, \(2,2,5,6,10,15,18,45,54,135,162\). Their matching earlier starts are \(0\) for the first short-block plateau, \(3m\) for the zero-plateau, and \(m\) for the isolated power-of-three endpoint.

The infinite result is proved in `RESULT.md`; these finite computations are only corroboration. No independent audit or formal proof certification is claimed.
