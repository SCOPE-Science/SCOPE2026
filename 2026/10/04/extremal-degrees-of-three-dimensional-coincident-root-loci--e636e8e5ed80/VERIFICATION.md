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

Hilbert's formula specializes for a three-part partition to 6abc divided by the factorials of repeated multiplicities. The proof correctly separates distinct, double, and triple multiplicity patterns. For maxima, repeated triples are bounded below the explicit distinct candidate for d>=6, and strict balancing moves among distinct triples force the unique residue-class patterns shown in the claim. For minima, the repeated-part cases and distinct case all exceed 3(d-2) for d>=7 except (1,1,d-2), with d=3,4,5,6 checked separately. A fresh exhaustive integer replay through d=120 independently matched every maximum, minimum, uniqueness claim, and small exception; the package verifier separately checks through d=500.

## originality

PASS

Feher--Nemethi--Rimanyi give the pointwise Hilbert degree formula and identify dimension with the number of parts, and Brambilla--Stagliano reuse this family for dual/rank-boundary questions. The primary 2003 paper was inspected at the actual formula page; no fixed-three-part maximum/minimum classification was located. The audited theorem requires an all-d integer optimization across symmetry classes, not merely reading a table. Resultary and targeted searches found no prior statement of the residue-class maximizers or the unique minimizer.

## value

PASS

Projective degree is the exact generic intersection count for a coincident-root stratum, so ranking three-dimensional strata by degree is geometrically meaningful. The theorem gives a complete all-degree maximum/minimum classification and exposes a non-obvious symmetry-factor effect that moves the maximum away from equal multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
