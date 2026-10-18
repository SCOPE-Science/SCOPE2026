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

# Reproduction and limits

From a directory containing the standalone `verify.py` and a Python 3 interpreter, run:

```sh
python3 verify.py
```

The script has no external package requirements. It constructs the entire lattice order, meet and join on \(M_n\), then tests independently every top-preserving meet-preserving box and every top-preserving monotone diamond. For all pairs of maps, it checks the complete Dunn inequality on every ordered input pair, rather than using the proof's reduced tests. It compares all surviving pairs with the closed counting formula. It then enumerates the entire atom-permutation group and records fixed modal-expansion pairs, yielding the Burnside orbit counts. The exhaustive domain is \(n=3,4\) only.

Expected exact output:

```text
n 3 B 50 D 150 valid 574
Burnside Counter({52: 3, 13: 2, 574: 1}) isomorphism 126
n 4 B 234 D 1361 valid 5054
Burnside Counter({62: 8, 316: 6, 16: 6, 86: 3, 5054: 1}) isomorphism 325
n5 and n6 closed census 70834 1332432
```

The verifier tests finite instances and arithmetic; the all-width proof in `RESULT.md` is necessary for the universal result. For widths \(n\ge5\), no exhaustive relation enumeration or orbit enumeration is asserted. Code agreement is not an independent mathematical audit.
