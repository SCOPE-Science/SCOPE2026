---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed balanced connected directed multigraph/Euler-tour equivalence, including active-vertex convention and loop-only singleton. Flow conservation uniquely gives one integer triangle circulation t with three nonnegative opposing pair counts. The mutually exclusive cases one active loop vertex, a connected two-vertex reversible pair, three vertices with nonzero circulation, and three vertices with t=0 and at least two reversible links give exactly the stated formal generating function; no disconnected loop components counted. Positive off-diagonal support thresholds follow from minimum arc lengths. Fresh, separately implemented enumeration of all 3^n words for n=1..9 agrees with symbolic GF by each support type, but unrestricted n relies on the exact Eulerian case decomposition.

## originality

PASS

The Eulerian characterization, balanced 3-by-3 matrix enumerator and general Markov-type counting are established earlier. The assessed additional statement is the all-length support-refined bivariate expression, unattainable support 1, nonmonotone first-occurrence thresholds, and exact profile-code sizes. Neither the inspected full unrefined 2012 source nor the 2021 DNA rank-modulation code source supplies this two-variable support distribution; the absence is limited to inspected material.

## value

PASS

Ordered adjacent-pair multiplicity profiles are natural Markov-type and DNA read channels; number of positive off-diagonal transition types measures sparsity of observed dynamics. An all-length exact distribution and sharp support thresholds are meaningful enumerative refinements, not just a reprint of unrefined known balanced-matrix totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
