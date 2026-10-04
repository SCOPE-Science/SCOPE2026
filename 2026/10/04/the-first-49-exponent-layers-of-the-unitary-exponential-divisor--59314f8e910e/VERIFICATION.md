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

Run `python verify.py` in the package directory. It uses only the Python standard library.

The script rebuilds \(R_a(X)=\sum_{d\mid a,d<a}X^d-1\) and the exact remainder \(B_a(X)\) of \(X^a+1\) modulo \(R_a(X)\) for every \(2\le a\le49\). It checks with the rational-root theorem that no \(B_a\) has an integer root \(p\ge2\), proves \(p\le C_a+1\), verifies \(\max C_a=1082\), and exhausts every prime inside the resulting exact bounds.

The 34 divisibility pairs are recorded in `candidates.tsv`. Every rejected quotient has a proper factor witness; the four surviving quotients are proven prime by direct trial division through their square roots. Finally both divisor-sum formulas are evaluated on each surviving triple.

Expected output:

`VERIFY_OK exponents=2..49 max_C=1082 divisibility_pairs=34 solutions=[(2, 2, 5), (2, 3, 5), (6, 2, 5), (49, 2, 4363953127297)]`

The verification is complete only for the stated exponent range and singleton-cofactor family.
