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

# Reproducibility and mathematical checks

The companion `verify.py` uses Python's standard library and requires no packages or network access. Run `python verify.py` in the directory containing the file. It enumerates all \(2^{\binom d2}\) edge-sign patterns for every integer \(2\le d\le7\), normalizes them by the vertex gauge on the star at vertex one, and checks \(2^{\binom{d-1}{2}}\) distinct classes. It also checks the product of that component number and \(2^{d-1}\), the independent-variable count, the dimension \(d(3d+1)/2\), and the even-binomial Hilbert numerator evaluation. Lastly it verifies all three principal equations and an explicitly nonzero nonprincipal minor and determinant for the given \(3\times3\) matrix.

Expected output includes:

```text
d=2 components=1 component_degree=2 principal_degree=2 ambient=8 dimension=7 hilbert_numerator=[1, 1]
d=3 components=2 component_degree=4 principal_degree=8 ambient=18 dimension=15 hilbert_numerator=[1, 3]
d=4 components=8 component_degree=8 principal_degree=64 ambient=32 dimension=26 hilbert_numerator=[1, 6, 1]
d=5 components=64 component_degree=16 principal_degree=1024 ambient=50 dimension=40 hilbert_numerator=[1, 10, 5]
d=6 components=1024 component_degree=32 principal_degree=32768 ambient=72 dimension=57 hilbert_numerator=[1, 15, 15, 1]
d=7 components=32768 component_degree=64 principal_degree=2097152 ambient=98 dimension=77 hilbert_numerator=[1, 21, 35, 7]
VERIFY_OK d=3 principal_equations=0 nonprincipal_minor=-2 determinant=-4
```

**Proof limits.** All statements for unbounded \(d\) are proved algebraically in `RESULT.md` using invariant rings, pair-straightening of matrix monomials, a complete closed-component decomposition, finite sign-group quotient, and a reduced complete-intersection argument. The script is a separate exact finite consistency test, *not* an infinite certificate, irreducibility test, or independent scientific audit. The only external mathematics relied on is standard Veronese/determinantal geometry and the originating definition of the membrane level-two shuffle relations. The result does not imply claims about arbitrary truncation levels or real positivity.
