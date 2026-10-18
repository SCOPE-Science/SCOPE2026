---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py > check.json` after installing the open-source SymPy Python library. Compare `check.json` to the accompanying `certificate.json` as parsed JSON objects; both should say `VERIFIED`.

The computation enumerates all \(65{,}536\) vertex masks separately for each of the three component bounds, with independent flood-fill and union-find membership checks. It reconstructs every admissible simplex and every incidence of its nonempty face boundary, builds the same explicitly defined vertex-toggle matching, and topologically sorts every reversed-gradient face-poset incidence to verify acyclicity.

Signed integral algebraic-Morse boundary matrices are computed from the original orientations. Their Smith factors are all units; the reduced integral homology is supported only in degree six (rank three at each of the first two stages) or degree seven (rank twenty-one at the third). Each of three source integral six-cycles has its full original simplicial boundary checked as zero before it is transferred into the next complex. Their integral Morse projections, together with target seven-boundaries, form six columns with a determinant-one six-row minor. The certificate lists the matrices and their exact minor.

The finite computations are exhaustive for the specified sixteen-vertex graph and three stages. They do not enumerate other graphs or higher component bounds, and they do not constitute an independent external mathematical audit.
