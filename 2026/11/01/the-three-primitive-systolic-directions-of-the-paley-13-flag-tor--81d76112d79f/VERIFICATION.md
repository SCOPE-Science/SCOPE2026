---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For Paley P13, edges have differences ±1,±3,±4. Its clique triangles are exactly translates of {0,1,4} and {0,3,4}, with 13 vertices, 39 edges, 26 triangles, six-cycle links and no four-cliques. These identify its flag complex as the universal triangular lattice divided by L={(a,b):a+3b≡0 mod13}. The triangular edge generators ±e1,±e2,±(e1+e2) give the exact all-class edge-walk length max(|a|,|b|,|a-b|); this follows from both 1-Lipschitz coordinate bounds and explicit axial/diagonal paths, not finite testing. L has no nonzero vector of norm≤3 and exactly ±(3,-1), ±(1,4), ±(4,3) at norm4, all primitive, first two determinant13. Every minimal vector forces three steps of one type plus one of another, yielding 13 distinct simple cycle carriers for each of three unoriented types. Independent enumeration gave 78 total 4-cycles, 39 zero-class and 39 nonzero with counts 13 each; translations and multiplier4 transitively permute them. Distinction between shortest closed walks for any w and census of simple essential 4-cycles is respected.

## originality

PASS

Qualified best-of-knowledge originality of the exceptional 13-vertex three-direction integral systolic shell, exact carrier counts and transitive orbit; triangular-lattice structure and flagness are known and explicitly separated.

## value

PASS

The Paley(13) graph is a canonical small flag torus; exact marked length norm and three distinct primitive shortest directions with 13 carriers each give meaningful finite geometry and a sharp contrast with the previously determined one-direction n≥17 cyclic torus family. The class multiplicities and affine orbit are not routine graph f-vector computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
