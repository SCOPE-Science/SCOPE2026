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

Decompose L2 over the affine intervals. A diagonal block is a restricted unnormalized Hilbert transform times the n-th power of the local slope, so its norm is at most pi times L to the n. Between two distinct ordered intervals, Lipschitz control majorizes the kernel by L to the n divided by distance; after choosing a separator this is a restricted Carleman kernel, whose L2 norm is pi by the standard weighted Schur calculation. The finite block matrix contributes at most the factor N.

## originality

PASS

The recent primary source publicly states a general linear-in-order bound and square-root-order refinements under extra regularity; no finite-corner order-uniform theorem was located. Muhly–Xia assumes VMO derivatives, excluding generic slope jumps. Full same-paper comparison remained access-limited and is retained as a residual risk.

## value

PASS

The motivating work explicitly raises sharpness of polynomial order growth. This theorem rules out every fixed polygonal profile as a source of such growth and identifies unbounded slope complexity as necessary for any finite-corner mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
