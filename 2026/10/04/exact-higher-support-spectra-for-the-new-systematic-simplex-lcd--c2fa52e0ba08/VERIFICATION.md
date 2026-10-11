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

For an \(r\)-dimensional message subspace \(U\), a nonzero simplex-block column vanishes on the whole subcode exactly when it lies in \(U^\perp\). Thus that block has fixed support \(q^m-q^{m-r}\). The systematic block contributes exactly the ordinary coordinate support size \(s(U)\ge r\), with equality on coordinate \(r\)-spaces, proving the hierarchy. For a fixed coordinate set of size \(s\), inclusion-exclusion over its coordinate hyperplanes counts the \(r\)-subspaces having full support there and gives the displayed Gaussian-binomial sum; summing over \(s\) recovers the total Gaussian binomial \({m\brack r}_q\). The inspected verifier independently enumerates reduced-row-echelon subspaces for \((q,m)=(2,3),(2,4),(3,2),(3,3)\) and agrees with the certificate; the proof itself is exact for all parameters.

## originality

PASS

Mondal--Lee's full open article defines exactly the two identity-augmented simplex families and determines ordinary weight distributions and LCD optimality. Full-text search found no generalized-Hamming-weight discussion. Classical simplex higher weights determine the fixed non-systematic contribution, but not the coordinate-support contribution or its full multiplicity spectrum after adjoining \(I_m\).

## value

PASS

Generalized weights and complete subcode-support spectra are standard structural invariants of a code family. For these newly introduced optimal LCD families, the result determines the full hierarchy and every support multiplicity rather than merely recomputing the minimum distance, providing a natural exact classification useful for higher-support applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
