---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The primary construction applies: α_j=cj^{−p} has finite sum below 2(1−b), decreases strictly with adjacent ratio tending to one, and α_1<2b. Its normalized Lebesgue restriction is invariant, physical, and fair Bernoulli in the measure-theoretic coding. Centered children of a length-I_j cylinder have center offsets ±(I_j+g_j)/4. The cylinder length is 2^{−j}(L+∑_{k≥j}β_k); its centers converge to the coded coordinate, giving a uniformly absolutely convergent sum of independent fair signs. Pairing the only matching sign indices after n shifts gives C_n=∑d_jd_{j+n}>0 including n=0. Set B_j=4·2^j d_j and P(t)=∑β_j t^j. Summing the β tails gives ∑B_jt^j=[2+(1−2t)P(t)]/(1−t), whose value and t-weighted derivative at 1/4 give the stated W_0,W_1 (independent check: python /workspace/branches/independent_checks.py). The inclusive Euler–Maclaurin tail starts with m^{1−p}/(p−1)+(1/2)m^{−p}, with error O(m^{−p−1}); the added β_m raises 1/2 to 3/2. Taylor expansion at m=n+j for j≤n/2 gives the coefficient 3/2−j and error O((1+j)^2 n^{−p−1}); exponential 4^{−j} weights control that error and the remaining tail. Normalizing by LW_0/16 gives the claimed A and J, and B_j>L proves approach from above. The differences I_j−I_{j+1}=2d_j telescope to ∑d_j=1, and d_0=(1+b)/2 implies |D|≥b on the closed unit disk. Thus the positive variance spectrum is |D|² with a zero-free normalized analytic factor. The positive Fourier coefficients of log|D|² are the Taylor coefficients of log D and the constant is twice log D(0), giving the stated inverse. Then I_j=2−2∑_{k<j}d_k and g_j=4d_j−I_j recover gap sizes and, by centering, locations. The claim about shift conjugacy is read on the recovered cut-interval model explicitly specified in the Finding. On the circle one must identify the two endpoint codes; full one-to-one conjugacy there is measure-theoretic (modulo the countable null set of boundary itineraries), not pointwise on the quotient. This distinction does not affect the signed-position integrals or geometry recovery, and nothing determines the map on the open deleted gaps.

## originality

PASS

The map construction, invariant physical measure, fair coding, and the general minimum-phase inverse are prior. The distinct supported contribution is the evaluated signed-position covariance, its explicit two-term correction, and the centered-gap realization of spectral identifiability via the zero-free bound and reconstruction; the compared primary and indexed exact statements do not cover these conclusions together or supply the specific missing calculations.

## value

PASS

All these maps have the same fair symbolic law, yet the embedded signed observable records precise geometric information. The explicit algebraic correction to exponential covariance distinguishes the gap decay, and the full spectrum is a complete observable invariant for the centered geometry. This is a quantitative and inverse result for a natural existing family, not a novelty claim for a standard Fourier algorithm or a recovery claim about the dynamics in the gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
