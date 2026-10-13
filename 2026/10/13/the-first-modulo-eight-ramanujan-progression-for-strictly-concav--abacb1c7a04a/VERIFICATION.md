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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 standard library. The verifier performs the following exact operations:

1. Computes all \(501\) residues \(s_1(n)\bmod8\), for \(0\le n\le500\), by truncated multiplication of the defining infinite product (all omitted terms have degree greater than \(500\)).
2. Independently computes these coefficients from the published identities for the parity of \(T_o\) and the signed triangular terms, checking exact equality for all \(501\) indices.
3. Checks that each of the \(18\) obstruction indices is exactly \(4\bmod8\).
4. Exhausts all \((m,r)\) with \(1\le m\le24\) and \(0\le r<m\), using the complete triangular residue period and obstruction indices; separately checks all \(21\) excluded residues at \(m=25\).

The infinite positive congruences are consequences of the published Liu–Xia Theorem 1.4, not experimentally extrapolated from the \(501\) values. The verifier does not certify bibliographic novelty or independent validation.
