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

# Reproduction and limitations

From the directory containing `VERIFY.py`, run:

```text
python3 VERIFY.py
```

Actual successful replay:

```text
VERIFY_OK: 4765 exact algebraic checks and 36 full-matrix cases; all offdiagonals strictly positive in checked cases
```

The standalone script requires only the Python standard library. It represents \(\mathbb Q(\sqrt2)\) exactly by pairs of rational numbers. Its sign test compares integer/rational squares rather than using floating-point tolerances. For \(2\le N<36\) and every \(1\le p<N\), it checks the key quartic coefficients, exact negative-witness identity and equality cases, and verifies strict negative witnesses for the stated ranges. The 36 independent full-matrix cases use exact inversion of \(I+ahL\), followed by \(T=(1+\sqrt2)B^2-\sqrt2B\), comparing every entry to the projector-derived formula and checking row sums.

The finite loops do not establish uniqueness of roots, an inequality for every integer order, or a proof of nonnegativity over every real timestep. Those assertions follow from the symbolic rational identities, the continuous minimum calculation, and Descartes' rule in `RESULT.md`. There is no external audit or independent validation in this package.
