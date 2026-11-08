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

Width W(u)=a|u1|+b|u2|+c|u3|. Each Haar column is spherical: E|Oij|=1/2, E Oij²=1/3, same row/column absolute cross moment 2/(3pi). For distinct row and column, condition on the first column u and circle perpendicular to it to get E|O11 O22|=(4/pi²)E(1-u2²)=8/(3pi²). Sum weighted entries and subtract (s/2)² to obtain exact V and covariance C. Exchangeability gives Var(orth mean)=(V+2C)/3 and Var(iid mean)=V/3. R(r)=1+2(Ar-B)/(C0+D0 r), r=s²/q in (1,3]; numerator of derivative 2(AC0+BD0)>0, giving sharp upper at cube r=3 and unattained needle infimum r→1. Threshold B/A lies in (1,3); for (1,1,t), two stated positive roots. Verified pinned mathematical derivation and code; independently checked derivative symbolically and covariance for three seeded Haar samples of 80k matrices, finite simulation not general proof.

## originality

PASS

Joint orthogonal-Haar box-width covariance and sharp three-view estimator phase diagram are distinguished from single-direction cube widths and same-direction width-brightness or other cubature. Closely related broad 2026 weighted-width manuscripts inaccessible in full; best-of-knowledge original with explicit risk rather than automatic failure.

## value

PASS

A natural directional measurement design has a surprising shape-dependent efficiency reversal, quantitatively sharp for all positive 3D orthotope dimensions; determines exact best/worst shape classes and transition. Nontrivial Haar mixed-coordinate moment and universal monotone quotient provide a self-contained useful design invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
