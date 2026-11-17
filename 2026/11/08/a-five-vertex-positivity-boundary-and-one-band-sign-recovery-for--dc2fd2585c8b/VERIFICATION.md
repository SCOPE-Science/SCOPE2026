---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Complete-multipartite spectral projector formula gives diagonal d=1/N+(1/p−1/N)F(Nh)+(1−1/p)F((N−p)h), distinct-vertex offdiagonal from strict chord-slope inequality. F has exact minimum (1−sqrt2)/2 at 4+3sqrt2, which bounds every N<=5 diagonal positive. For N>=7 the H(p,N−p) inequality yields a negative witness, N=6 p=3,4 have zero at witness with positive derivative and hence nearby negative. Quartic positive constant/linear/leading, negative cubic gives at most two positive roots by Descartes; positive endpoints plus negative witness force exactly two simple roots. Independently checked algebra/numeric sample boundary cases; not extrapolating experiments.

## originality

PASS

Standard SSP and absolute-monotonicity results concern arbitrary positive systems, while adjacent graph positivity classifications concern Radau IIA or Padé/RK4 stability functions. The exact unmodified TR-BDF2 threshold N=5 and single negative self-transition interval for each part are not implied by these sources.

## value

PASS

Graph heat positivity of a common L-stable integrator has a universal sharp order threshold and per-vertex reentrant sign band, pertinent to deciding timestep admissibility and distinguishing endpoint positivity from internal stages; not just a stability-function restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
