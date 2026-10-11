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

The recursive block sampler is exactly uniform because a prescribed first block/order and recursively prescribed remainder have product probability 1/R!. Conditional on prior blocks, each block is a uniform critical-size subset of the residual system, so the source theorem applies with its polynomial failure bound. A prefix through N/2 meets at most 1+2^(2/p)mN^(-2/p) blocks; Minkowski and coefficient Cauchy–Schwarz give the required K_p scale, and a union bound over O(N^(1-2/p)) blocks makes all such prefixes good simultaneously. For later prefixes, L2/Linfinity interpolation gives K_p(T)<=|T|^((1-2/p)/2), which is on the same scale when m>N/2. The Fourier near-origin interval supplies the matching lower bound. The complete corrected RESULT.md preserves this proof and changes only malformed escape/control characters.

## originality

PASS

The primary 2026 theorem is an exact-cardinality result at one critical size ceil(N^(2/p)) with arbitrary polynomial failure probability. It does not give one random permutation whose every prefix simultaneously has the sharp two-parameter profile. The audited recursive critical-block construction, prefix block count and deterministic large-prefix regime supply that new nested statement. Resultary returned no independent all-cardinality predecessor.

## value

PASS

The critical Bourgain cardinality is naturally the transition point of a full selection profile. Producing one nested random family with sharp order at every cardinality is useful for applications that need compatible restrictions across scales, not merely a separate good set at one size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
