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

The construction is checked directly from the coordinate formula. For every nonzero \(\lambda\in\ell_p\) and every \(x\in\ell_p\), disjoint supports give
\[
\|T_\lambda x\|_p^p=\|\lambda\|_p^p\|x\|_p^p.
\]
This proves injectivity and closed range.

For each input coordinate \(i\), the output coordinates \(M_i=\{n_i^{(k)}:k\ge1\}\) carry exactly the one-dimensional pattern \(x_i\lambda\). Choosing a basis vector \(e_r\notin\operatorname{span}\{\lambda\}\) produces quotient witnesses \(e_{n_i^{(r)}}+\operatorname{ran}T_\lambda\), and the block restrictions prove these witnesses are linearly independent. Therefore the quotient is infinite-dimensional.

If \(W\) has finite dimension \(N\), then all positive iterates \(T_\lambda^m(W)\) lie in \(\operatorname{ran}T_\lambda\). The quotient image of the complete orbit is therefore only \(q(W)\), which is finite-dimensional and closed. It cannot be dense in the infinite-dimensional quotient, so \(T_\lambda\) is not \(N\)-supercyclic.

The proof uses no computation beyond exact series identities and no unproved limiting assertion. It does not address maximality of the embedded subspace or Feldman's distinct infinite-supercyclicity notion.
