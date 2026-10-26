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

# Verification of the mathematical claim

The general proof uses a tamely ramified \((\mathbb Z/2\mathbb Z)^4\)-cover, five elliptic quotients, and norm/pullback correspondences satisfying \(\Phi\Psi=[8]\). The integer \(8\) is invertible in characteristic \(7\), so the decomposition is compatible with the \(7\)-divisible group. The Legendre Hasse polynomial is verified as \((\lambda+1)(\lambda-2)(\lambda-4)\). The geometric heart is the pairwise intersection of two four-subsets in three points and sharp triple transitivity of \(\mathrm{PGL}_2(\mathbb F_7)\); it yields the allowed multiplicities \(\{0,1,3\}\). The marked counting proof is an exact incidence double count, valid for every \(7\)-power field.

A standalone checker, `check.py`, performs independent exact arithmetic in \(\mathbb F_7\) and \(\mathbb F_{49}\) without external libraries. Its verified output is:

```
HASSE_POLYNOMIAL_OK 7
STRATA_COUNTS_OK 7 {3: 20}
INCIDENCE_COUNTS_OK [12, 12, 12, 12, 12]
RANK_COUNTS_OK {2: 20}
HASSE_POLYNOMIAL_OK 49
STRATA_COUNTS_OK 49 {0: 1512, 1: 630, 3: 20}
INCIDENCE_COUNTS_OK [138, 138, 138, 138, 138]
RANK_COUNTS_OK {5: 1512, 4: 630, 2: 20}
CHECK_OK
```

The checker exhausts two finite base fields, not all extensions or all algebraically closed parameters. The proof rather than this enumeration supplies the universal conclusion. Independent scientific audit is not performed.
