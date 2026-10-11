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

The scientific premises checked in the primary source are:

- the handle map is \(A=QR^{-1}\) on a genus-\(19\) fiber;
- \(S=A_*\) has characteristic polynomial \((t^2+1)^2h(t)h^*(t)\);
- the printed degree-\(17\) polynomial \(h\) is irreducible over \(\mathbb Q\);
- \(K=\ker(S^2+I)\) has dimension \(2\);
- the displayed integral basis spans \(L=K\cap H_1(\Sigma_{19};\mathbb Z)\), and \(L\) is isotropic.

The bundled `artifacts/verify_spectral_reduction.py` was executed from its packaged path with the system Python interpreter. It uses only the standard library and exact rational polynomial arithmetic. It checks the printed coefficient vector, the reciprocal factor, exact coprimality of \(h\) and \(h^*\), coprimality with \(t^2+1\), total degree and reciprocity of the characteristic polynomial, and the dimension bookkeeping for the primary sector and quotient.

Successful replay output:

`VERIFY_OK deg_h=17 gcd_h_hstar=1 gcd_h_cyclotomic=1 char_degree=38 reciprocal=true primary_dim=4 kernel_dim=2 quotient_rank=34 stable_dim=17 unstable_dim=17`

The no-unit-circle theorem is symbolic: a unit-circle root of the real polynomial \(h\) would also be its inverse-conjugate and therefore a root of \(h^*\), contradicting exact coprimality. The \(17+17\) split then follows from reciprocal pairing in the rank-\(34\) symplectic quotient. The nonsplit primary-module statement follows from the degree-four \((t^2+1)\)-primary characteristic factor together with the source value \(\dim\ker(S^2+I)=2\).

No numerical root sampling, truncated enumeration, timeout inference, or external certification is used in the proof. The verification does not establish a pseudo-Anosov stretch factor or any statement beyond the homological action described in the result.
