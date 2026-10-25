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
# Reproducible exact checks

Install `sympy` from `requirements.txt`, then run `python verify_wiman_char5.py` in the directory containing the two files. The script checks identities in exact polynomial rings of characteristic \(5\), not floating-point approximations.

The verified identities include the reduction of the original sextic to \(2(a+b+c)^3+abc\), the node-projection factorization, branch resultants and derivative resultants, the four relevant coefficients of \((B_t(B_t-A))^2\), and the symbolic Cartier determinant \(t^8\). The geometric consequences use ordinary nodes, Kummer-cover Riemann–Hurwitz, the tame group decomposition of Jacobians, and the standard hyperelliptic Cartier formula as proved in `RESULT.md`.

For a secondary independent check, the script evaluates all \(31\) projective plane points over \(\mathbb F_5\) for each parameter \(t=1,2,3,4\), and separately enumerates the genus-two double-cover points. The plane image has four nonsplit rational nodes and no other rational points in those examples, while each genus-two quotient has four rational points; their point counts satisfy the expected trace identity. Such finite checks cannot by themselves establish the theorem for arbitrary algebraically closed parameters.

The provided code is a reproducible exact symbolic certificate, not external independent scientific validation. Later scholarly priority review is still warranted.
