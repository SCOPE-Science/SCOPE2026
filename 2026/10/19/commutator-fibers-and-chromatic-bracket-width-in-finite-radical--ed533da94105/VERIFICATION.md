---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For fixed diagonal pairs c(i)=(a_i,b_i), the bracket on an arrow corner is (a_i−a_j)v_ij−(b_i−b_j)u_ij. Diagonal and loop output vanish; each off-diagonal corner is in the bracket span by [e_i,u]=u. Unequal colors give a surjective linear map with q^dimension preimages per target; equal colors give q^(2 dimension) for zero only. Multiplying gives the claimed q^(2h+M) normalization and support-conditioned weights. Exact support F gives product over its edges of (q^μ−1) possible targets, subject to q²-colorability for a single bracket. For r brackets, the tuple of r diagonal pairs must separate every edge supporting the sum. Conversely use a proper q^(2r)-coloring, route each nonzero edge vector entirely to one separating coordinate pair, and solve the independent corner equations. The argument includes r=0, the zero target, no off-diagonal arrows, both orientations and characteristic two. A full-support target attains the maximum.

## originality

PASS

The supported distinct content relative to inspected earlier sources is the general support-resolved bracket result, in particular the exact additive length threshold for every target and every number of brackets together with the uniform fiber formula. The zero fiber in the simple-graph scope and the two-vertex case are not new. Two later distinct indexed results materially reproduce the loopless result in both fibers and width; this is equivalent coverage, not a historical-priority conclusion.

## value

PASS

A support graph gives an exact length for each bracket target and sharp worst cases that are unbounded at fixed field size. This also identifies all unattainable single brackets, with precise fiber multiplicities for the remaining targets, substantially beyond an average commutativity statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
