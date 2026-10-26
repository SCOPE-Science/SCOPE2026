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

# Reproducibility and verification

Run `python3 verify.py` (Python standard library only) from the directory containing this document and `verify.py`. The program constructs \(\mathbb F_5\) and \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\), checks squarefreeness by polynomial gcd independently of the symbolic discriminant, expands the cubic power of the defining quintic independently of the claimed Cartier formulas, and computes the semilinear fourth and fifth powers of the Cartier matrix (fifth power is sufficient for stabilization in dimension four). It checks all \(125\) coefficient triples over \(\mathbb F_5\), including exact Cartier ranks for every smooth triple. It also checks gcd/discriminant agreement and the full census on all \(15625\) triples over \(\mathbb F_{25}\), and verifies semilinear matrix ranks for forty representatives of each smooth type there.

Expected output:

```
F_5: {'singular': 25, (0, 4): 20, (2, 2): 64, (0, 2): 16} verified Cartier sample sizes {'(0, 4)': 20, '(2, 2)': 64, '(0, 2)': 16}
F_25: {'singular': 625, (0, 4): 600, (2, 2): 13824, (0, 2): 576} verified Cartier sample sizes {'(0, 4)': 40, '(2, 2)': 40, '(0, 2)': 40}
VERIFY_OK
```

The finite checks are exact but do not certify the identities over *all* field extensions; the proof in `RESULT.md` establishes the universal statements from elementary algebra, Riemann–Hurwitz and Cartier semilinearity. The source-overlap comparison has a specifically noted access limitation for one relevant 2025 paper. Independent external audit has not been performed.
