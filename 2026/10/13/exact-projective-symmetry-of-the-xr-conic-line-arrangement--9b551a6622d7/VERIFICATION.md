---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Every automorphism preserves component degree and hence stabilizes the six-line set. Dual line vectors yield exactly four collinear triples arranged as the K4 incidence structure. Four-point-frame reconstruction enumerates 72 frames and 24 exact projectivities inducing the full S4 on the four concurrency classes; this is exhaustive over C because any projectivity is determined uniquely by one projective frame and its image, even with rational representative coordinates. Six published conic quadratic forms transported as B Q B^T (B=A^(-T)) cut the 24 maps to exactly six. A wholly independent SymPy rational-matrix reconstruction reproduced all 72 frames, 24 line stabilizers and 6 conic-preserving projectivities, matching the supplied verifier. Direct matrix multiplication checks that listed s,t generate six transformations with s^2=t^3=(st)^2=1 in PGL3. Applying the six maps to added line covectors yields the 3 free-line and 6 plus-one-line orbits. Projectivity preserves the free/plus-one properties and exponent data, subject to originally published examples.

## originality

PASS

The published source supplies the explicit 12-component XR equation, singularity structure, freeness and two single-line additions but not the embedded S3 stabilizer or the S4-to-S3 break. Exact Resultary similarity search returns a projective S3 stabilizer for a distinct small two-conic three-line arrangement, insufficient for this result. The 3 and 6 orbits are new consequences of this distinct group computation, with residual risk of unindexed equivalent calculation.

## value

PASS

The complete embedded automorphism group of a prominent 12-component free conic-line arrangement is naturally motivated by the initiating addition-deletion problem. It reduces repeated testing of distinct source addition lines by grouping projectively equivalent ones, distinguishes S4 combinatorial line symmetry from S3 symmetry of the full curve, and gives explicit orbit decompositions. This is mathematical structure beyond reproducing the source exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
