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

# Verification details

The proof is analytic and reproducible from the normalized Legendre integral and Euler beta identity, with absolute Fubini justified by split-torus integrability. The nonstandard step is the transfer to arbitrary spectral mixtures: use the standard spherical Bochner decomposition, bound all principal contributions by the integrable parameter-zero spherical function, eliminate a trivial mass using the L1 hypothesis, and apply Tonelli to the positive complementary part. No finite computation is used to certify the all-parameter theorem.

For an independent numerical normalization cross-check, evaluate
\[
2\int_0^{90}P_{-\nu}(\cosh t)\cos(\xi t)\,dt
\]
with mpmath's high-precision Legendre integrator and compare to the displayed two-beta expression in RESULT.md. At 25 decimal digits the absolute differences were approximately \(2.31\times10^{-12}\) for \((\nu,\xi)=(0.3,0.7)\), \(2.99\times10^{-18}\) for \((0.5,1)\), and \(1.80\times10^{-20}\) for \((0.5+0.8i,0.4)\). The first discrepancy is dominated by the finite cutoff; the analytic proof treats the whole real line.

The numerical check is not an exhaustive parameter test; strict positivity for all real frequencies and arbitrary mixtures follows from the gamma product and the spherical-Bochner/Fubini proof. Sources checked include the complete relevant introductory and principal-series coverage in arXiv:2606.07286, a classical Legendre integral representation and accessible special-function references. Earlier unindexed transform tables and a potential future sequel are residual originality risks.
