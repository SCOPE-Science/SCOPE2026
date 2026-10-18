---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For each n>=3 polygon, its boundary radius in a direction δ from nearest vertex is r/cos(α−δ), α=π/n,r=Rcosα. A circle t∈(r,R) is covered by vertex-angle arcs of half-width η=α−arccos(r/t). With m cyclic phase gaps g_j summing 2α, angular measure exactly nΣ min(g_j,2η), valid also for zero gaps. The sharp sum inequality Σmin(g,c)≤min(2α,mc) has all-level equality for equal gaps; unequal gaps are strictly inferior on an open interval near c=2α/m, so positive-a.e. radial weights strictly prefer equal gaps. The polar angular integration per gap equals r²[tanα−tan(α−g/2)], giving area/inradius and the stated 1/m disk deficit. Independent Shapely computations for (n,m)=(3,3),(4,3) with coincident phases,(5,5),(7,2) agree with the exact formula <1e−10. These finite cases are diagnostics, not the all-n,m proof.

## originality

PASS

Best-of-knowledge statement-level comparison of original claim, aliases and stronger coverage: Existing named facts do not logically imply the sharp coverage and rigidity without additional phase-gap analysis; all known preexisting parts explicitly excluded from novelty.

## value

PASS

The universal every-radius coverage order is stronger and more reusable than single area or perimeter optimization. It determines all positive radial-weight optimizers, rigidity including coincidence, exact area/inradius, and the disk deficit for a natural congruent-polygon union construction. The known basic configuration and perimeter/area ratio are explicitly NOT the novel portion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
