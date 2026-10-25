---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

From the actual Cayley generators on Z4², independent shortest-path enumeration gives 16 vertices, degree6, distance distribution (1,6,9), and 12 linear generators fixing 0, yielding 192 affine graph automorphisms, matching the published full order. The four displacement orbits have sizes 1,6,3,6. For each representative, independently generated every length4 magnitude-chain basis and signed d3,d4, checked d3d4=0, and computed full integer SNF: for distance0 dims C2,C3,C4=(9,54,96), ranks d3,d4=(9,45), H3=0; distance1 (6,54,80), ranks(6,48), H3=0; both distance2 orbit reps (4,66,80), ranks(4,61), H3=Z. All nonzero SNF factors of d3/d4 equal 1, proving torsion-freeness, 144 localized Z copies in total. Independent rational cohomology cocycle action verifies signs on every representative stabilizer: H_(0,2): two + two -, H_(1,2): one + one -. Integral rank-one fiber action has same ± signs. Endpoints induce full 192-group lattice modules; invariant zero and each nontrivial stabilizer coinvariants Z/2, total (Z/2)².

## originality

PASS

Best-of-knowledge original only for the precise additional integral/equivariant/multiplicative result; explicit known portions carved out. Two targeted indexed semantic searches plus specified primary comparisons do not show a stronger implying theorem; absence of hits is not a proof of novelty. See each named mathematical implication check and named residual risks.

## value

PASS

The Shrikhande graph is the canonical counterexample partner of the 4x4 rook graph among strongly regular (16,6,2,2) graphs. Published rational MH3,4 rank144 does not determine integral torsion, which endpoint orbit supports homology, or the full signed 192-group module. Complete local Smith and sign classification is a natural exact invariant useful for equivariant magnitude homology comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
