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

Every H(n,5) is cubic, so a radius-r ball has at most 3*2^r-2 vertices for r≥1. Four rounds can therefore cover at most 22+10+4+1=37 vertices, excluding n≥19, while three rounds cover at most 15, excluding b≤3 for n≥8. The displayed source sequences were checked by exact BFS and satisfy both coverage and source-validity for n=7,...,15. Exhaustive center enumeration, even without source-validity restrictions, shows radii 3,2,1 leave minimum 2,4,5 vertices uncovered for n=16,17,18, so the last radius-zero source cannot finish. For n=7, radii 2,1 leave at least two vertices, excluding three rounds. An independent replay reproduced the boundary uncovered minima and witness validity. Thus the finite enumeration is exhaustive only for four explicitly bounded orders and the infinite tail is analytic.

## originality

PASS

Sim--Wong's 2026 paper is the decisive same-family source. Its accessible publisher abstract states exact burning numbers for all girth-four generalized Heawood graphs and for the girth-six subfamily H(2k,k), which intersects the fixed-k=5 family only at H(10,5). Targeted Resultary searches found no fixed-5 cutoff theorem. Open-access retrieval did not yield the full article; an authorized institutional attempt for the same DOI also returned no verified PDF, so a bounded access risk is recorded rather than treated as failure.

## value

PASS

The theorem gives an exact finite-to-infinite burning cutoff along a natural fixed-diagonal subfamily of generalized Heawood graphs studied in the current literature. The proof combines explicit positive schedules, exhaustive treatment of the three unresolved boundary orders, and a clean degree-growth tail, making it a meaningful family classification rather than a collection of isolated computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
