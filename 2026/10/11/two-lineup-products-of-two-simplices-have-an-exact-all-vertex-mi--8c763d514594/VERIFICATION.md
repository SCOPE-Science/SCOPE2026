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
The theorem is proved symbolically in `RESULT.md`.

Critical checks:
- every generic product-simplex functional has scores \(p_i+q_j\);
- its top two entries share a row or column;
- every ordered row-sharing or column-sharing pair can be realized as the top two entries;
- the source vertex criterion converts exactly those lineups into lineup-polytope vertices;
- every resulting occupation vector has squared norm \(1+\alpha^2+\beta^2\);
- every resulting occupation vector has row-block and column-block sums equal to \(1\);
- the row-column uniform point therefore has the displayed common squared vertex distance;
- the \(de\) cyclic same-row lineup vertices have that point as their equal-weight barycenter;
- the barycentric squared-distance identity proves exact minimum-enclosing radius and uniqueness.

`verify.py` checks all parameter pairs \(2\le d,e\le8\) for several admissible rational weight pairs. It enumerates the classified vertex set, checks the exact vertex count, verifies the common squared radius and cyclic barycenter, and constructs additive-score witnesses for every ordered row-sharing and column-sharing pair. Finite computation is corroborative only and does not assess originality.
