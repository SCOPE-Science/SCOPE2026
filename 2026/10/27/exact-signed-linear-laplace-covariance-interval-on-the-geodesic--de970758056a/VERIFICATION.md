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

For the intrinsic circle of circumference 2pi, even Fourier integration gives F_n=a(1-(-1)^n exp(-pi*a))/(a^2+n^2)>0 and coefficient (F_n-b F'_n)/pi. Separately in each parity class F'_n/F_n strictly increases; the even limit is the unattained global supremum. The difference between the least odd and even values is 2/[a(a^2+1)]-pi/sinh(pi*a)>0 by the cubic lower bound for sinh and pi^2>3. Thus the lower bound is the reciprocal of the negative zero-mode derivative ratio and the upper bound is the reciprocal of the positive even limit. Strict positivity at the lower endpoint follows because an atomic measure with no nonzero Fourier modes would equal a multiple of Haar measure; for distinct sites this forces every weight to vanish. The even coefficients at the upper endpoint have a positive (a^2+n^2)^-2 tail; negativity outside is detected by mode zero or sufficiently large even modes, respectively. Taylor expansion and the difference a-b_+ give the stated limits and deficit. Fresh bounded replay: python3 /workspace/review_replay.py circle; direct 45-digit quadrature at a=.002,.4,1,1.7 and an independent 256-site circulant at a=1 confirmed selected endpoint and exterior signs, not the all-mode statement. At a=1 it reproduced endpoints -1.1653548145454739 and .87573937173774468. This is not a result for chordal distance or a periodized Euclidean Matérn.

## originality

PASS

Best of current evidence: the specific interval with its two different endpoint mechanisms and sharp deficit is distinct. The general Fourier characterization, the uncorrected exponential kernel and the failure of the uncorrected geodesic Matérn-3/2 profile are prior and receive no novelty credit. The closest indexed prior modulation uses cos(theta), not theta; neither its spectral inequalities nor the general positivity theorem supplies the required all-mode extremal derivative comparison.

## value

PASS

The affine term is a motivated correction to a standard invalid intrinsic covariance; the interval gives an exact design rule for every range parameter. The signed lower boundary and strict finite-site positivity despite losing the mean mode are useful distinctions not provided by the known Matérn exclusion. The exact exponentially small short-range deficit and fourth-order even-mode tail also explain why a finite spectral scan may miss failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
