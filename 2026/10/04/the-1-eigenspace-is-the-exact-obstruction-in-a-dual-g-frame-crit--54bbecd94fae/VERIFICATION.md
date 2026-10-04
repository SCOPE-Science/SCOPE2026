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
The primary source definitions, Theorem 3.1, and its proof were read directly. The core identity was independently reconstructed:
\[
\sum_i(\Lambda_i-\Lambda_iS^{-1})^*(\Gamma_i-\Omega_i)
=(I-S^{-1})T_\Lambda T_{\Gamma-\Omega}^*.
\]
Thus the published orthogonality condition is equivalent to placing the mixed duality defect in \(\ker(S-I)\).

The explicit \(\mathbb C^2\) example was checked symbolically. Its frame operators and bounds follow from diagonal quadratic forms; the orthogonality operator is exactly zero; and the reconstruction operator is exactly \(\operatorname{diag}(2,1)\), not the identity.

For the sharp general boundary, the synthesis operator of a \(g\)-frame is surjective and \(T_\Lambda^*S^{-1}\) is an explicit bounded right inverse. Therefore any nonzero operator with range in \(\ker(S-I)\) can be realized as the mixed defect of a \(g\)-Bessel perturbation of a fixed dual. This proves necessity of excluding eigenvalue \(1\) when the criterion is required to work for every \(g\)-Bessel candidate.

No numerical computation, finite enumeration, or unproved extrapolation is used. The literature comparison did not find an indexed erratum or an equivalent spectral correction; unindexed overlap remains possible.
