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

# Reproducible finite verification

Run `python3 checker.py` with Python 3.10 or newer. The checker uses only the Python standard library; no external tables, internet resources, numerical approximations, or other files are needed. It enumerates the signed permutation vectors \(D_p\), constructs each normalized compatibility graph, and enumerates every maximal clique with the recursive Bron--Kerbosch algorithm. Its expected exact output is:

```text
p=5 |D|=8 |V|=3 edges=3 maximal_cliques={3: 1} directions=2 affine_spectra=10
p=7 |D|=48 |V|=5 edges=10 maximal_cliques={5: 1} directions=8 affine_spectra=392
p=11 |D|=3840 |V|=69 edges=156 maximal_cliques={2: 120, 9: 1} directions=384 affine_spectra=5622144
p=13 |D|=46080 |V|=319 edges=926 maximal_cliques={1: 24, 2: 324, 3: 225, 5: 42, 11: 1} directions=3840 affine_spectra=1425765120
CHECK_PASS
```

The checker explicitly verifies the unique maximum clique, every pairwise edge among its radial vertices, the modular symmetries, exact spectrum counts, and the thirteen-field noncollinear local example. These certificates close the finite enumeration for the four listed primes only. The proof's cyclotomic lemma and reduction from spectra to cliques are mathematical arguments in `RESULT.md`, not empirical assertions. A failed checker or incomplete execution would not prove or disprove the classification. Independent audit is not performed.
