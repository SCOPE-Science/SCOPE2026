---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For ellipsoid E(c,Q) containing the closed ball B_r(0) strictly, let s(u)=u^TQu, y(u)=u·c, D=det Q. Affine hyperplane slicing gives V(u)=κ_{n-1}√D [s(u)-(r-y(u))²]^{(n-1)/2}/s(u)^{n/2}, radicand strictly positive. Raise to 2/(n-1); odd part under u↦-u is 4r D^{1/(n-1)} y/s^{n/(n-1)}. If one center vanishes equality forces both to vanish. For two nonzero centers, homogenize odd equality, raise to n-1 and apply UFD to the positive-definite real quadratic forms in n>=3, irreducible there, to force Q'=λQ; the unpowered odd formula forces c'=c. Even part then forces λ=1. For centered nonspherical Q, homogeneity and irreducibility of s and s-r²||x||² likewise force Q'=λQ and λ=1; for Q scalar the transformed data are constant and the only way Q' can have constant t↦(t-r²)t^{-n/(n-1)} on its Rayleigh interval is Q' scalar, with identical radius. These exhaust all centers and shapes. Dimension n>=3 is essential to irreducibility; no n=2 claim. Finite numerical checks do not replace polynomial factorization.

## originality

PASS

Yaskin--Zhang's noncentral-section question and Makai--Martini's local smooth determination do not imply global all-center ellipsoid rigidity. Polygonal determination is a different object class. Published later planar ellipse results apply n=2 only, and cannot be used to predate this n>=3 theorem. The original Barker--Larman 2001 article was not obtained in full; an institutional request returned a different paper in the same journal issue, not the desired one. This is a real older-overlap risk but not, without evidence, a reason to reject best-of-knowledge originality.

## value

PASS

Determination of a general ellipsoid from noncentral supporting-ball sections is a natural exact inverse problem inside the longstanding Barker--Larman question. Unlike centered or perturbative cases it simultaneously identifies arbitrary translation, orientations and principal semiaxes, proving a sharp global injectivity benchmark for geometric tomography.

The dated certificate retains the supplied scientific assessment, sources and limitations.
