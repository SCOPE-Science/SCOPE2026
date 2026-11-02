---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The actual BP5_MATCHING.json (SHA 5cd35d303d6de4fb61fe53d9eb57d3d6e8c8763c) was read. An independent standalone check enumerated all 196 nonempty admissible directed path faces with counts (12,48,76,48,12), validated all 96 disjoint matching pairs and critical masks 3904,47,2624,512; directed Hasse topological sort visited all 196 cells, with 576 incidence edges. Verified the listed eight-mask 2-cocycle has zero integral coboundary on all 48 three-simplices and pairs -1 with the explicit integral 2-cycle, making it primitive. The Alexander–Whitney square vanishes on every one of the 12 four-simplices. Forman reduces to one 0-, one 2- and two 4-cells; π3(S²)=Z and the two cup-square coefficients are their integral Hopf invariants, both zero, giving the asserted wedge. These finite checks are exhaustive for this fixed graph; logs alone did not supply proof.

## originality

PASS

Caputi–Collari–Smith 2026 establishes the integral homology of exactly this BP5 complex and expressly leaves wedge homotopy/open attaching problems. The new finite integral cup-square proof addresses the unsolved Hopf invariant not implied by Betti numbers or dihedral characters. Residual unindexed exact six-cycle work possible.

## value

PASS

BP5 is the smallest homologically mixed bidirected polygon case with two dimension-four attaching maps to an S² where homology does not decide the homotopy type. Evaluating the primitive cup square and integral Hopf obstruction is a substantive, motivated structural computation explicitly tied to an open example in the literature. Exact finite certificates can benchmark more general multipath-homotopy methods; no paper-sized family theorem is demanded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
