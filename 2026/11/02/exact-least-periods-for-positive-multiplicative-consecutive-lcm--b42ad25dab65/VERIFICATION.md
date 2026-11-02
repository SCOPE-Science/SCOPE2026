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
# Reproducible computations and boundaries

Run `python verify.py` with Python 3 (standard library only). It computes the original quotient \(G_{k,\sigma_\alpha}(n)\) by independently factoring the values \(n+i\) and their least common multiple. It also computes the independently derived local-count expression, checks periodicity, and rejects every proper divisor of the claimed period.

Validated \(\alpha\in\{0,1,2\}\), every \(1\le k\le10\), and a non-completely-multiplicative function \(f(p^j)=2^{j^2}\) for \(1\le k\le9\). The recorded output was:

`VERIFY_OK: tested 7470 exact sigma_alpha comparisons (alpha=0,1,2), 987 non-geometric prime-power function states; all claimed periods were minimal`

These checks are finite and do not constitute infinite certification. The proof's critical steps are the cancellation of prime powers above \(p^{e_p}\), cyclic-interval asymmetry of the top count, and elimination of possible cross-prime compensations by positivity and finite-translation orbits. All are established symbolically in RESULT.md. No independent mathematical audit has been performed.
