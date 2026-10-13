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

# Verification details

The mathematical theorem is analytic and not based on finite enumeration. The proof explicitly resolves all spectral projectors of an arbitrary \(K_{a_1,\ldots,a_k}\), derives every matrix-entry type, and constructs three infinite-family tests proving the scalar conditions are necessary. The Gauss multiplier is evaluated symbolically for all \(s>0\), so no numerical approximation is used to establish the universal positivity conclusion.

Run the standalone script with `python3 artifacts/verify.py` from the containing directory. It uses only Python's standard-library `fractions` and `itertools` modules. It constructs each graph Laplacian directly, squares it, forms both fourth-order Padé polynomials, inverts the denominator by rational Gaussian elimination, and compares the resulting matrix against an independently assembled spectral-projector expression. For each case it tests every entry for strict positivity and each row sum for exact equality to one.

Actual execution returned:

`VERIFY_OK 993 exact rational graph-step cases, spectral projections, row sums, strictly positive entries, sharp independent obstructions`

The cases comprise every ordered composition of total size \(2\le n\le8\) with at least two parts, each evaluated at four rational steps, plus five heterogeneous larger graphs. Separate exact checks examine nonnegativity and monotonicity of the specific multiplier and the independence of the scalar restrictions. The examples are arithmetic cross-checks; an infinite mathematical assertion cannot be certified by enumerating those cases. External independent audit has not been performed.
