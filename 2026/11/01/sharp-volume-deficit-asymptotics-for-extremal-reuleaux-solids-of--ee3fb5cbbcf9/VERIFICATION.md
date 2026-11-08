---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: For each odd n>=3, the support of the revolved width-one regular Reuleaux n-gon has h=1/2+f, f(π−θ)=−f(θ), and the meridional and azimuthal principal radii yield by integration by parts the exact identity π/6−V=(π/2)∫_0^π((f′)^2−2f²)sinθ dθ. The alternating radius equation f″+f=g(nθ) with g=±1/2 square wave, after F_n(t)=n²f(t/n), has uniformly C¹-convergent zero-mean even periodic solutions to F″=g. Its triangular derivative F′ has mean squared energy π²/48, weighted rapid-period averaging contributes 2, f² is lower order, giving the universal odd-sequence limit π³/48. The missing translation modes are fixed by dihedral symmetry, and the smoothness/endpoint conditions justify the Jacobian and parity. Hynd extremality is a cited prior theorem, not inferred from the volume computation. Independent symbolic integration reproduced energy π²/48; two independent disk-section and support Fourier numerical integrations for n=3,5,7,11,19,35 agree within 1.2e−7 and approach 0.6459640975. Numerical samples are corroboration, not proof of the infinite asymptotic.

## originality

PASS

PASS on best available primary comparison: the volume-deficit coefficient of the explicit extremal revolution sequence is not supplied by Hynd’s extremality theorem, known planar Reuleaux area and Estermann asymptotics, or one-mode Legendre volume families. Older solid-volume identities could encode the coefficient; no exhaustive historical priority claim is made.

## value

PASS

PASS: Gives an exact n^−2 geometric approach-to-ball rate for a canonical sequence of genuinely extreme width-one 3D convex bodies. The constant distinguishes extrinsic 3D volume loss from known planar area/inertia rates and is a reusable sharp quantitative geometric datum; neither arbitrary sampling nor a restatement of extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
