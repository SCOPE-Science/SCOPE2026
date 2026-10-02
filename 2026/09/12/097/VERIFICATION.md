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

The main finite classification was independently recomputed rather than accepted from the saved log. Enumerating all \(16^3\cdot 9^3=2,985,984\) triangle cost instances and minimizing the binary local-polytope objective over the classical half-integral singleton grid reproduces maximum gap exactly \(4/3\) and zero violations. The antiferromagnetic witness has integer optimum four and LP optimum three by a direct feasible half-half coupling and the per-edge lower bound one. The claimed ear-step obstruction was also independently reconstructed over all \(9\cdot16\cdot16\cdot27\cdot4=248,832\) local configurations using exact rational arithmetic: the worst ratio is exactly two and exactly 4,484 configurations exceed \(4/3\), matching the stored log. The package `evaluate.py` implements the same one-dimensional coupling minimization. Thus the finite claims do not depend on the archived success logs alone.

## originality

PASS

Fresh exact-object search found no earlier source giving the complete restricted triangle census, the exact \(4/3\) maximum over these alphabets, or the 4,484-case scalar-ear obstruction. Roof duality/QPBO supplies half-integrality but does not imply the extremal finite classification.

## value

PASS

The triangle is the minimal treewidth-two obstruction core for the stated series-parallel target. A sharp finite gap classification plus a concrete failure of the natural scalar ear induction materially constrains how any global proof must proceed, so this is a motivated boundary result rather than an arbitrary small-instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
