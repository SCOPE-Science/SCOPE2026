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

The proof checks the universal restricted-\(p\)-map as a morphism of sheaves, then determines its zero scheme on an exhaustive standard affine cover. The exact chart rings are given in `RESULT.md` and determine all nilpotents and ordinary reduced points. The projection module decomposition supplies the full Hilbert polynomial; neither a numerical fit nor finite enumeration is substituted for it.

Run `python3 verify.py` with Python 3.8 or later; it has no nonstandard dependencies. It enumerates projective \(\mathbf F_p\)-points of the ordinary summand, counts monomials in truncated polynomial rings, and compares with the signed binomial expansion of \((1-t^p)^r/(1-t)^{r+s}\). The tested cases are \(p=2,3,5\), \(1\le r,s\le3\), and finitely many degrees. Expected output begins with `VERIFY_OK`.

The checker does not prove absence of extra components over every algebraically closed field, scheme-theoretic decomposition for all dimensions, or historical originality. Those questions are addressed by the algebraic chart proof and source comparison, respectively. This is not an independently audited result.
