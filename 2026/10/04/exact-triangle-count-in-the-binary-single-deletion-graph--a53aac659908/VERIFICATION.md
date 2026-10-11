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

The actual package constructs an exact finite-state recognizer for deletion distance at most one, determinizes it to 11 states, and takes the three-pair product with 287 reachable states. The inspected verifier does not infer from a finite table: it certifies invariant Krylov spaces of dimensions 5 and 14 and annihilating polynomials \((t-2)^3(t-1)\) and \((t-2)^4(t-1)^3\), thereby proving the pair and ordered-triple recurrences for all lengths. Inclusion--exclusion removes coordinate equalities and division by six converts ordered distinct triples to triangles. Independently, I rebuilt the literal deletion graph for every \(1\le n\le7\); the triangle counts \(0,2,18,100,432,1592,5268\) exactly match the formula.

## originality

PASS

Alon et al. define the same deletion graph and use triangle sparsity, but their result is a general-radius asymptotic upper bound rather than an exact radius-one enumeration. Their fixed-pair LCS/SCS multiplicity estimates and the older insertion-reconstruction literature do not determine the number of global three-vertex cliques. A fresh Resultary search found no earlier exact formula for \(T_n\).

## value

PASS

Triangle sparsity is an explicit structural input in current deletion-code lower-bound work. At the first nontrivial deletion radius the theorem replaces a general asymptotic control by an exact all-length clustering invariant, including every lower-order term; that is a natural reusable graph statistic rather than an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
