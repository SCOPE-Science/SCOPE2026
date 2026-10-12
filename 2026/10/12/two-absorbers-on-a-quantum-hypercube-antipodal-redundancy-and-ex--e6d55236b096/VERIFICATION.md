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
# Verification of the two-absorber hypercube theorem

**Analytic checks.** The dark subspace is the direct sum of the eigenspace kernels of both site functionals. Positive loss rates make the complementary restriction strictly decaying. For every nonantipodal separation and every interior spectral weight, both Walsh phases occur; hence all denominators \(\binom dk^2-K_k(r)^2\) are positive. Both endpoint eigenspaces have rank one. The rank sums and the degree-one Walsh sign argument prove the dimension and exact-zero statements in every finite dimension.

**Standalone exact checker.** Execute `python artifacts/verify.py` from the directory containing the package. The exact standard-library checker evaluates all 640 combinations of \(d\in\{2,3,4,5,6\}\), nonzero separation \(r\), and initial vertex \(x\), comparing rational Krawtchouk evaluations against independent character-by-character Fourier projections. It also checks the summed ranks and zero-survival loci in all configurations. Output: `VERIFY_OK exact_walsh_states= 640 rank_formula=passed zero_survival_sites=passed`.

**Optional dynamics cross-check.** With NumPy 2.3.5 and SciPy 1.17.0, five finite non-Hermitian matrix exponentials in dimensions two through four, each at unequal positive absorber strengths, yielded maximum absolute difference approximately \(1.2513\times10^{-13}\) from the exact limit. Output: `NUMERIC_TIME_CHECK cases= 5 maximum_absolute_difference= 1.2512213487525514e-13`. These are illustrative finite-time checks, not uniform convergence bounds.

**Limits.** No check at finitely many dimensions certifies the infinite dimension range; the analytic proof does. No claims of independent auditing or certification are made.
