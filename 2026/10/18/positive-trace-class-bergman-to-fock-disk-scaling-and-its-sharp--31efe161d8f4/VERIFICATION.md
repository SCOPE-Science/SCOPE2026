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

The normalized radial integrals diagonalize in the specified common monomial basis with total-degree multiplicity binom(k+d-1,d-1). With m=k+d, the density ratio of scaled Beta(m,s+1) to Gamma(m,1) strictly decreases on (0,s) and is zero beyond s; normalization forces one crossing and hence strictly positive CDF difference for 0<t<s. Kernel integration gives the exact trace, using the primitive (v/(1-v))^d/d; positivity turns it into the trace norm. At each fixed degree the first variation is m(m+1)/2 times the difference of the Gamma(m,1) and Gamma(m+2,1) CDFs, giving the stated eigenvalue. Multiplicity cancels the factorial to 1/[k!(d-1)!]; summing recovers the first variation of the exact trace. Pointwise positive diagonal convergence plus convergence of these total masses gives trace-norm convergence without an unjustified uniform Taylor estimate. The adjacent-eigenvalue comparison reduces to t(t+2) versus (k+d)(k+d+1), proving the claimed staircase for the limiting error operator, including ties. Independently checked 12 numerical quadratures including nonintegral weights and 20 adjacent ties.

## originality

PASS

The radial spectra, weak convergence and sharp limit of individual disk-localizer operator norms are established inputs. The exact positive defect, its first-order trace-class limit in all dimensions, and the limiting defect's maximizing-degree transitions are distinct from the strongest available comparisons. The judgment is confined to those claims and the inspected sources.

## value

PASS

This gives exact error control and a complete first variation for a naturally scaled approximation of localization operators, rather than a rephrased eigenvalue limit. Trace norm controls all modes; the staircase describes which degree governs the sharp approximation error, with d=t=1 witnessing that the error need not be largest on constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
