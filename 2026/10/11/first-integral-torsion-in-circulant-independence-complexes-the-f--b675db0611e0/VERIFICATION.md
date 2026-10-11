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
# Reproduction and limits

Run `python verify_census.py census.json` with Python 3 and SymPy. It enumerates all nonempty connected circulant graph step sets of orders three to fourteen; there are 338. It constructs every independent face, oriented integral simplicial boundary, and Smith normal form, then compares complete machine-generated case records with `census.json`. Successful output includes `CENSUS_PASS`. The empty-step graphs are simplices; disconnected circulants decompose as disjoint graph unions, hence their independence complexes are joins, covered by the torsion-free join argument in `RESULT.md`.

Run `python verify_surface.py surface_certificate.json` with Python 3 alone. This verifier uses a second, direct-subset face enumeration, checks the fourteen ordered elementary collapse pairs at the moment of removal, and verifies each resulting closed surface by triangle incidence, connected vertex links, Euler characteristic and contradictory orientation propagation. It verifies both step-set unit orbits and that the triangles of the earlier \(Q_{7,2}\) model map to the pure example under multiplication by three. Successful output includes `SURFACE_PASS`.

Both programs were executed successfully after checking their complete embedded source files. Exact Smith forms, not finite experiments over selected fields, establish the torsion statement for every enumerated complex. This is an **exhaustive bounded theorem for \(1\leq n\leq14\)**; neither checker proves any claim for larger circulants. Homotopy type is established only for the six exceptional step sets. No independent audit or outside certification was performed.
