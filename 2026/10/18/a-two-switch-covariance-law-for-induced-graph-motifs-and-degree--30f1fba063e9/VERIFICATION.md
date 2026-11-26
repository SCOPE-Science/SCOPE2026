---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reassessed the corrected RESULT.md in repairs/1. Summing over an induced h-set and degree indicators, outside vertices contribute no covariance by edge independence; the h internal vertices contribute the degree-role sum of Bin(n-h,p) masses at k-d_v, less h times the unconditional mass. There is no need for joint independence among those internal degrees. Dividing by the positive unconditional mass yields (1) including zero-binomial roles. The second derivative of log R is the positive weighted mean of d_v/p^2+e_v/(1-p)^2 plus the variance of the log-term derivatives. Endpoint divergence and positive second derivative give exactly the stated crossing and tangency alternatives. Criterion (2) is now explicitly limited to compatible k; at incompatible regular k, A=0 and the covariance is strictly negative, not a two-switch case. At the eventual compatible interior scaling the 1/N correction to log A is r/(2N); the log monomial has second derivative -r^3/(de) at its maximum d/r. The assumed 1/sqrt(N) perturbation gives (3), with no assertion at equality. Three cycle labelings per four-set and degree-two probability (1-p)^(n-4) give (4); the cubic maximum 4/27 yields the exact six-vertex onset and p=c/n gives (5). Independent replay `python3 /workspace/audit_recompute.py 1` used a degree-sequence test for C4 and P4 inside four-sets and exact rational moment sums: 90 comparisons at n=4,5,6 across all degree classes and three densities, including incompatible degrees and the C4 specialization. The replay does not prove the convexity or infinite limits.

## originality

PASS

Pass for the repaired contribution only. Equation (1) as a distinct claim of originality is not supportable: the earlier arbitrary-motif non-induced result directly determines it by signed supergraph inclusion–exclusion and covariance linearity. The original did not identify that specific prior implication or the close same-day induced two-switch example. The repaired finding expressly treats the exact identity and its direct substitutions as supporting material and reclaims only the compatible-role sign classification, the regular sqrt(N) window, and the sharp transition for the named induced C4 and N2 pair. These quantitative sign conclusions are not present in, or direct specializations of, the matched sign laws; summing non-induced covariances of either sign does not preserve their one-switch structure.

## value

PASS

The surviving statement is not a recomputation of an already computable covariance. It gives a structural bound on the number and direction of density-driven sign changes, separates tangency from crossings, and quantifies a sharp regular-motif window where both roots disappear. The induced C4 example locates the exact first feasible size for that specified pair and gives a sparse parameter boundary. Those address natural joint observables and complement rather than repeat the earlier one-switch non-induced law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
