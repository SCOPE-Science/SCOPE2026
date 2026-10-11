---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The finite-dimensional trace classification follows directly from the presentation. In any finite-dimensional representation, central Z decomposes the space into eigenspaces with Z=μI; on an r-dimensional block UV=μVU, so determinants give μ^r=1. If t is not a root-of-unity trace μ+μ^{-1}, the last relation forces U+V=2I, and the standard positive identity then forces U=V=I; the commutation relation forces μ=1. Conversely, at every cyclotomic t one gets a distinct finite-dimensional trace from clock-shift matrices (or a distinct character at t=2). For |t|>2, z+z*−t is invertible, forcing u=v=z=1. For noncyclotomic t in (−2,2), choosing the corresponding non-root-of-unity ζ gives a quotient onto the irrational rotation algebra and hence a distinct amenable trace. The density assertions are elementary consequences of roots of unity being countable dense on the unit circle. The bundled checker only verifies support counts and finite clock-shift identities; none of these finite checks substitutes for the analytic argument.

## originality

PASS

The accessible Chen–Zhao primary abstract gives a general construction and says it is applied to an algebra having a unique finite-dimensional trace and a distinct amenable trace, but it does not expose a one-parameter cyclotomic classification. Resultary searches for the parameterized rotation-algebra trace criterion found no matching published finding, while Lawton provides general rational-rotation background rather than this presentation-dependent phase diagram. The Chen–Zhao full text could not be obtained through the open-access route in this run, and the authorized institutional fallback returned no usable text; this is recorded as the principal residual risk rather than used as novelty evidence. With that access limitation, the exact iff cyclotomic resonance theorem remains original to the best of the material actually inspected.

## value

PASS

The coefficient t is a natural parameter in the focal presentation, and the theorem identifies a sharp dense arithmetic resonance boundary separating finite-dimensional trace uniqueness from rational-rotation obstructions, while also distinguishing interior irrational-rotation quotients from exterior collapse. This is a structural phase diagram rather than an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
