---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. Cauchy projection formula for the solid cone gives B_k(z)=pi*z/2+(1/4) integral_0^{2pi}|k sqrt(1-z^2) cos(phi)+z|dphi and the axial branch pi*z. Setting x=z/(k sqrt(1-z^2))=sin(a) reduces the nonaxial branch to G_k(a)=k[cos a+(pi/2+a)sin a]/sqrt(1+k^2 sin^2 a). The derivative sign is D(a)-k^2 sin a cos a. H(a) has a unique minimum at tan(2a_s)=pi+2a_s, giving at most one nonaxial local maximum. The maximum of the G_k branch is strictly increasing from 0 to infinity and crosses pi exactly once, after H-minimum. The equality stationary equation D(a)[D(a)+cot a]=pi^2 singles out the transition. Independently solving it gave k_c=2.6414025520640956, |u_z|=0.5889810763491234 and saddle k_s=2.145539290889752; independent one-dimensional optimization checked k=1.5,k_c,3,5. The proof classifies all directions including axial/oblique ties, not merely stationarity.

## originality

PASS

PASS, best knowledge: exact global maximizer transition and coexistence latitude is finer than a projected-area formula and lower stationary bifurcation. Pennell–Deignan 1989 is the strongest plausible coverage risk: it treats the identical projected-area problem, but its full mathematical article could not be inspected, so priority must remain explicitly qualified.

## value

PASS

PASS. Maximal directional projected area is the cone brightness/visible-shadow extremal problem with a genuine global phase transition distinct from local stationary-point birth. Uniqueness of maximizing latitude and coexistence at a sharp aspect answer an intrinsic geometric optimization question; no arbitrary slice or tiny gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
