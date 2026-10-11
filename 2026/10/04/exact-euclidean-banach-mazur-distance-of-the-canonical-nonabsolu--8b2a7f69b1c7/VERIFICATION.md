---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The 2006 primary source defines exactly the piecewise function used in the record and states that the corresponding generalized Day--James unit sphere is an octagon. For an arbitrary positive-definite quadratic pullback \(q\), the matrix certificate in the package expresses a convex combination of \(q\) at two unit-ball vertices as \(13/9\) times the average at two unit-sphere edge points. Therefore \(M(q)\ge(13/9)m(q)\) for every pullback. Fresh exact rational replay of the assigned verifier reproduced the certificate, the candidate maximum \(16/13\), the boundary minimum \(144/169\), and the ratio \(13/9\). Thus the claimed distance \(\sqrt{13}/3\) and the displayed optimal quadratic form are correct.

## originality

PASS

The exact primary source was read at Proposition 2.4: it supplies the same piecewise function and octagonal sphere, but its topic is the James constant and uniform nonsquareness, not Banach--Mazur distance. The PDF contains no Banach--Mazur discussion. Current Resultary searches returned the assigned record and nearby exact Euclidean-distance records for different polygonal or Day--James families, but no stronger theorem whose parameter specialization gives this irregular octagon. The current general distance-ellipsoid literature supplies an optimality framework rather than this octagon's numerical invariant.

## value

PASS

The object is a canonical published example designed to separate generalized Day--James geometry from absolute norms, and Euclidean Banach--Mazur distance is a standard affine invariant. An exact sharp value with a universal matrix certificate and optimal ellipse is therefore a natural reference fact rather than an arbitrary coordinate computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
