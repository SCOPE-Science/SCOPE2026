---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The spectral projectors of the unweighted K_(1,n-1) star at 0,1,n give exact Rademacher sign-count weights w0=(n-2K)^2/n^2, w1=4K(n-1-K)/[n(n-1)], wn=4K^2/[n^2(n-1)], K~Bin(n-1,1/2). The first three moments give the two-node Jacobi matrix and exact nonnegative residual Q_n-T2=(n-2K)^2*d0/[t(t+1)(t+n)*dt], with d0=4K^2(n-1-K)/[n+(n-4)K]. k=0 is early Krylov termination, treated exactly. It is strictly positive at k=1 for n>=3, hence strict negative expected bias. Fixed t>0 and binomial CLT plus subGaussian moment bounds give (T1-tau)/n -> -1/[(t+1)(t+2)] and (T2-tau) => Z^2/(t+1)^2-1/[t(t+1)] with all fixed absolute moments; bias limit -1/[t(t+1)^2], variance limit 2/(t+1)^4. Independent direct-rational star action and resolvent checks for n=3..13 and t=1/3,2,7/2 reproduced residual; file scope_worker08_checks_20261106.py emits ONE_STAR_EXACT_PASS. Finite checks do not prove the CLT.

## originality

PASS

The inspected prior primary mathematics supplies the classical framework, but none of the materially compared statements implies the full claimed specialization; best-of-knowledge priority, with explicit risks. Equivalent form is the two-node Gauss-Stieltjes formula for a random three-atom spectral measure. General three-node/moment quadrature is classical, but it does not by itself state this binomial-measure exact law and high-degree shifted chi-square limit. The general error and stochastic matrix-free theory covers the algorithm and Stieltjes sign behavior, but the inspected results do not provide this exact star/Rademacher binomial residual or limit distribution. A specialized theorem for arbitrary growing outliers could dominate it; that remains a priority risk.

## value

PASS

The high-degree star is a natural stress-test for stochastic Lanczos trace estimation, as the vanishing mass of the growing outlier produces extensive single-step underestimation but a nondegenerate shifted chi-square residual after two steps. The exact all-sign error and limiting variance give interpretable finite-step performance benchmarks that neither a general Gauss error sign nor a routine numerical test alone supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
