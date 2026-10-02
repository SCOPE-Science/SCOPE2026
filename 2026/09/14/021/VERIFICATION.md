---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The next-generation reduction was independently reconstructed from the block triangular transition matrix: \(H=D_\beta V_I^{-1}D_\sigma V_E^{-1}\). With the stated parameters and movement matrices, exact arithmetic gives isolated values \(1/5\) and \(2/9\), \(\operatorname{tr}H(1)=14/45\), \(\det H(1)=1/90\), discriminant \(106/2025\), and Perron root approximately \(0.2699514460>2/9\). This is an exact finite counterexample, not a simulation-only conclusion.

## originality

PASS

Prior multipatch epidemic literature demonstrates that travel can overturn isolated-patch disease outcomes, but no searched source was found that directly implies this exact simple SEIR stage-specific-movement counterexample or its matrix.

## value

PASS

A two-patch exact counterexample to a natural universal bracketing heuristic is mathematically informative: it isolates the mechanism to opposite stage-specific movement and gives a transparent rational next-generation matrix. This is a motivated boundary/counterexample rather than an arbitrary parameter-only gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
