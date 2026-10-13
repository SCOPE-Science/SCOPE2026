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
The checker performs exact rational arithmetic for
\[
1\le n\le40,
\qquad
1\le k\le n.
\]

It evaluates the Weyl-root product
\[
d!\prod_{\alpha>0,\ \langle\omega_k,\alpha^\vee\rangle>0}
\frac{\langle\omega_k,\alpha^\vee\rangle}
{\langle\rho,\alpha^\vee\rangle}
\]
directly from the type-\(C_n\) positive coroots and verifies that it equals the closed factorial degree formula.

It verifies the Bruhat-cell count
\[
2^k\binom nk,
\]
the complete strict degree-versus-Euler classification, and the absence of equality.

For every fixed \(k\ge2\) in the tested range, it checks the exact adjacent-\(n\) degree quotient and confirms that the normalized degree/Euler ratio increases. It also checks the exact Lagrangian boundary recurrence.

Finite checks are regression evidence only. The infinite classification is established by the symbolic identities and inequalities in the accompanying result.
