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
The proof in `RESULT.md` is the verification of the arbitrary-dimensional theorem. The accompanying `verify.py` is only a finite algebraic replay.

It checks the projected coordinate normal
\[
Q_{ij}=
\left(e_i-\frac1m\mathbf1_m\right)
\left(e_j-\frac1n\mathbf1_n\right)^{\mathsf T}
\]
by exact rational arithmetic for a range of dimensions, including zero row and column sums and squared Frobenius norm \((m-1)(n-1)/(mn)\).

It also checks deterministic families of positive integer margins. For each case it forms
\[
t_*=\min\left\{\frac{\min_i r_i}{n},\frac{\min_j c_j}{m}\right\},
\]
constructs the residual product matrix exactly with rational numbers, and verifies the prescribed margins and the common entry lower bound.

Finally, it checks the \(d\times d\) Birkhoff specialization through the symbolic identities \(t_*=1/d\), \(\kappa=(d-1)/d\), and \(\rho=1/(d-1)\).

No finite enumeration is used to infer the general theorem, and no claim is made for sparse transportation supports or non-Frobenius norms.
