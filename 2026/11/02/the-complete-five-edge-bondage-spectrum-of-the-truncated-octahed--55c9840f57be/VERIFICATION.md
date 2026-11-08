---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: The standard 24-permutation adjacent-swap graph has 36 edges. All 7-vertex dominating sets are absent and exactly 1767 eight-vertex dominating sets exist. For each such D and v outside D, define Q(D,v) as selected incident edges; D ceases dominating after edge deletion F iff at least one Q(D,v)⊆F. Therefore gamma(T−F)>8 iff every D is destroyed, a finite exact criterion. An independently written C++ exhaustive enumeration over all 0..5-edge F gave bondage counts 0,0,0,0,0,276, with examined k5 count C(36,5)=376992; under 48 value-permutation/position-reversal actions it gave eight orbits of sizes 12,24,24,24,48,48,48,48. Source independent Python alternative inspected. This is a complete finite proof rather than extrapolation.

## originality

PASS

PASS (qualified): Srivastava 2026 arXiv:2609.02477 already proves gamma=8 and bondage number b=5, so neither invariant is claimed original. The accessible abstract describes four-edge exhaustive nonexistence and existence of a five-edge witness, not the 276 count and eight automorphism classes. The full primary manuscript could not be read; an identical census in its body or appendix would be decisive prior coverage. That inaccessible plausible source alone leaves priority qualified, not a scientific failure.

## value

PASS

PASS: Refining the just-established minimal bondage number of a classic 24-vertex convex-polyhedron/permutohedron graph into the full 276-witness and eight-orbit spectrum is a motivated finite extremal graph invariant, revealing how edge deletion actually raises domination; a precise count of all minimum obstruction sets can be used in resilience and symmetry studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
