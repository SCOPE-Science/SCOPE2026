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
The source definition and Theorem 9 were read from arXiv:1801.02785v2. The earliest public version was verified as 2018-01-09, and the source lists classification 42C15.

For the failure witness, direct substitution with \(H=\mathbb C\), \(K=I\), \(W_1=H\), \(V_1=\{0\}\), \(w_1=a_1=b_1=1\), \(\lambda_1=\lambda_2=0\), and \(\mu=1\) gives equality in the perturbation hypothesis and zero perturbed frame energy.

For the repaired theorem, the checked proof chain is:
1. \(X^2\geq Aa_-^2\|K^*f\|^2\).
2. The source perturbation hypothesis therefore implies \(D^2\leq pX^2+qY^2\), with \(p=\lambda_1+\mu/(Aa_-^2)\) and \(q=\lambda_2\).
3. Direct-sum triangle inequalities give \(X\leq Y+D\) and \(Y\leq X+D\).
4. Solving \((1-r)^2=p+qr^2\) yields \(r_\pm=(1\pm\sqrt{p+q-pq})/(1-q)\).
5. When \(p<1\), \(r_->0\), and coefficient confinement converts \(r_-X\leq Y\leq r_+X\) into the displayed \(K\)-fusion-frame bounds.
6. At \(p\geq1\), the scalar zero-subspace construction satisfies the perturbation inequality, proving sharpness of the universal threshold.

A random symbolic-numeric stress test of \(100000\) pairs \((p,q)\) with \(0\leq p<1\) and \(0\leq q<1/2\) found no violation of the exact ratio interval. This finite test is auxiliary only; no infinite-dimensional conclusion depends on it.

Scientific limits: the theorem-level claim is tied to the fully inspected arXiv v2 statement. The later journal publication was identified bibliographically but not used as whole-document negative evidence. No independent audit has been performed.
