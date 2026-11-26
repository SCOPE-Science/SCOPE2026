---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the frozen symmetric model (RESULT.md lines 7–43, 47–68), B=I−hA is real symmetric with spectral radius <1. The stationary Gaussian innovation series has covariance 2qh(I−B²)^−1, so the precision is A/q−hA²/(2q). At known q the symmetric roots of I−2hqC^−1 exist exactly at C≽2qhI; their eigenvalues are in (−1,1), so all produce stable SPD drifts. Each positive spectral block of the squared matrix splits by an arbitrary orthogonal projector, giving two signs on a simple block and Grassmannians on repeated blocks; a zero block has only the zero symmetric root. At two distinct steps the affine intercept and twice negative slope are U=A/q and V=A²/q. Hence VU^−1=A and VU^−2=qI; conversely U positive definite, V=qU² and the stated strict stability give exactly the two input precisions. The known-q perturbation bound is sharp for opposite scalar precision errors (small enough to preserve positive definiteness if required); it is a bound for the displayed estimator, not a lower bound for every constrained estimator. In continuous time C*=qA^−1 has a common scaling ambiguity. In the nonsymmetric witness the two transitions are scaled orthogonal matrices with identical scalar B B^T=(1−hκ)²+h²ω², giving (6) for precisely its stated stable range. The known-q one-grid fiber is not a claim to classify unknown-q data without allowing q to vary. VERIFICATION.md and check_stationary_ou.py supply recorded finite checks only and were not executed.

## originality

PASS

The complete known-noise one-grid fiber and known-noise two-step recovery have exact overlap in another indexed record, including for arbitrary specified q by rescaling C. The distinct central result here is identification and data consistency for jointly unknown (A,q) from two stationary numerical marginals, with the contrast to exact-time sampling and a nonreversible boundary. Neither fixed-noise result nor the inspected steady-state and trajectory inference literature gives this joint identification as stated. This is not a claim of priority for the overlapping parts.

## value

PASS

A plausible identification failure from stationary data is resolved by changing a controlled numerical resolution rather than observing trajectories. The theorem specifies when this works, gives an exact consistency test and unique joint recovery, and exhibits both continuous-time and rotational failures outside the informative model. The known-noise root classification is useful context; the substantial increment is the unknown-scale inverse result and its limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
