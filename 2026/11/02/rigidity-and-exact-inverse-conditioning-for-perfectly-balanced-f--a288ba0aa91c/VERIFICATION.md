---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Off-diagonal Gram entries vanish iff first k-1 normalized Fourier moments vanish. Endpoint integration identifies differences of k endpoint power sums; Newton identities show r<k would force identical start/end endpoint multisets. For r=k, self-inversive coefficients of unit-circle-root polynomials with equal nonconstant terms and different constants imply all intermediate coefficients vanish; both endpoint sets are regular k-gons, cyclic alternation then imposes equal arcs length 2pi rho/k. Differentiated moments yield delta c_m=(sqrt(k)/(2pi))e^(-im phi)(e^(-im ell) vhat_m-uhat_m). Conjugate real Fourier blocks and even-k Nyquist case give exactly the two squared singular levels with k-1 multiplicities; rho strictly between 0 and 1 gives positive inverse. Analytic Taylor remainder justifies sharp first-order local inverse but not global inversion. Independently assembled 40 real Jacobian matrices and compared full spectra.

## originality

PASS

Endpoint reconstruction and general Prony conditioning are established. Courtney gives recovery using mean plus Fourier moments THROUGH k, whereas zero moments THROUGH k-1 and a fixed-area tangent Jacobian on balanced k arcs constitute a narrower inverse-geometry question. The exact real two-level singular spectrum and k-independent condition number are not found in inspected primary results; the basic rigidity via Newton/self-inversive identities should not be overclaimed as independently deep.

## value

PASS

Determines the minimal number and geometric rigidity of perfectly conditioned sampling windows and supplies the sharp infinitesimal inverse error amplification for the natural endpoint coordinates. The occupancy-only condition number and optimal half-occupancy value address a real inverse sampling problem beyond standard reconstruction existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
