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

The proof was checked symbolically at the level of its decisive implications.

For membership, Bézout gives \(d=\sum_i a_i f_i\), whence \(\operatorname{rank}d(X)\le\sum_i\operatorname{rank}f_i(X)\); multiplication by the quotient \(g/d\) cannot increase rank. This proves \(C=\ell\).

For nonmembership, select a root \(\lambda\) at which \(d\) has multiplicity \(a\) and \(g\) has multiplicity \(b<a\). On \(J_a(\lambda)\), every generator vanishes. The residual factor of \(g\) is invertible and \((J_a(\lambda)-\lambda I)^b\ne0\), so \(g\) does not vanish. This is a direct contradiction to any finite domination coefficient.

For sharpness, distinct \(\lambda_i\) with \(f_i(x)=\prod_{j\ne i}(x-\lambda_j)\), \(g=1\), and \(X=\operatorname{diag}(\lambda_1,\ldots,\lambda_\ell)\) give generator ranks \(1\) and target rank \(\ell\).

`verify.py` independently executes these finite symbolic sanity checks for several sizes and obstruction examples. `VERIFY_OUTPUT.txt` records its successful output. The computation does not certify the infinite statement; the written proof does.
