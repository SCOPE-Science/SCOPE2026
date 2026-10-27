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

The claim is \(\|J_\mu\|_{\mathrm{ess}}=\mu_{\mathrm{c}}(K)^{1/p}\) for compact metric \(K\), finite positive Radon \(\mu\), and \(1\le p<\infty\).

- **Atomic component:** enumerate the point masses and truncate after \(N\) atoms. The operator-norm tail is at most \((\sum_{j>N}a_j)^{1/p}\to0\), so this component is compact.
- **Nonatomic upper bound:** the zero operator gives essential norm at most \(\|J_{\mathrm{c}}\|=\mu_{\mathrm{c}}(K)^{1/p}\).
- **Nonatomic lower bound:** use an independent generating Rademacher sequence \((r_n)\) and continuous approximants \((f_n)\) bounded by one. For any compact operator, a subsequence of its images converges in norm; independence from finite-coordinate approximants to any fixed target vector forces the limiting distance to be at least \(\mu_{\mathrm{c}}(K)^{1/p}\).
- **Mixed measure:** the atomic and nonatomic \(L^p\) components form an \(\ell_p\)-direct sum, and the atomic component is compact, so it does not change essential norm.

No computation or finite experiment is used to infer an infinite statement. The proof relies on the standard fact that a finite nonatomic Borel probability measure on a compact metric space is a standard nonatomic probability space, and on density of continuous functions in \(L^p\) for finite Radon measures. Independent validation and independent audit have not been performed.
