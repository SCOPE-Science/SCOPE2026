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
The theorem is proved analytically in `RESULT.md`; the finite checker is corroborative.

Source-dependent checks:
- The middle-period source was inspected at the Hansen-polytope section and its primary MSC metadata.
- The open-access 2013 full text was inspected at Definition 4 and Lemma 5. A visual page check confirmed the exact vertex set and the irredundant inequalities
  \[
  -1\le -t+2x(C)\le1
  \]
  for every clique \(C\) of a perfect graph.
- The historical 1977 source was identified from its publisher record, but the encountered PDF access path required authentication, so no noncoverage conclusion is based on that unread text.

Mathematical checks:
- Each clique facet normal has squared norm \(4|C|+1\), making maximum cliques exactly the closest centered facets.
- Every signed stable-set vertex has squared norm \(|S|+1\), making maximum stable sets exactly the farthest vertices.
- Opposite facets prove the global inradius upper bound for arbitrary ball centers.
- An antipodal maximum-stable-set vertex pair proves the global circumradius lower bound and forces the circumcenter to be the origin.

`verify.py` enumerates representative small perfect graphs, reconstructs all cliques and stable sets, verifies every declared facet inequality on every vertex, checks exact affine facet rank, and confirms the two radius formulas. It is not used to prove the theorem for arbitrary graphs.
