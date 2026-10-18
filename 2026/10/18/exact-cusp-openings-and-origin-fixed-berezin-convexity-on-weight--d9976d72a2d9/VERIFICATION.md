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

The analytic proof uses a normalized reproducing-kernel identity, Schwarz–Pick to isolate the origin, a uniform small-radius expansion, a monotone radial inverse with continuously varying angle, and the exact range of one angular Fourier mode. This proves both section endpoints and the convexity obstruction for every eligible bounded composition operator.

The standalone standard-library checker was executed as \(\texttt{python3 check_berezin_cusp.py}\) from the package directory. It passed 48 normalized one-sided section-extremum checks over 12 explicit polynomial families and two scales each; these finite checks are not proofs of an infinite asymptotic or a uniqueness claim.

Primary source dated 2026-02-10; the fractional-kernel range is \(0<s<1\), the symbol fixes zero, and the operator is assumed bounded. The existing Hardy-space analogue supplies related qualitative background but is not independently re-proved by numerical experiments. Independent audit has not been performed.
