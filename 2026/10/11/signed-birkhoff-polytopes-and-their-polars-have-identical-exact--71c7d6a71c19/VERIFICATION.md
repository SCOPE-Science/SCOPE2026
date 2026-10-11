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
The arbitrary-\(n\) proof is given in `RESULT.md`.

Critical checks:
- every signed permutation matrix has Frobenius norm \(\sqrt n\);
- signed permutation vertices occur in antipodal pairs;
- every source facet normal \(\varepsilon\otimes e_i\) or \(e_i\otimes\varepsilon\) has norm \(\sqrt n\);
- every source facet has support constant \(1\);
- opposite source facets force inradius at most \(1/\sqrt n\);
- the row/column sign normals span all of \(\mathbb R^{n\times n}\), forcing the unique incenter \(0\);
- polarity makes those source facet normals the vertices of \(\mathcal C(n)\);
- polarity makes signed permutation matrices the facet normals of \(\mathcal C(n)\);
- signed permutation matrices span all of \(\mathbb R^{n\times n}\), forcing the polar's unique incenter \(0\);
- antipodal vertices force unique minimum-enclosing center \(0\) for both polytopes.

`verify.py` exhaustively checks \(1\le n\le5\). It enumerates all signed permutation matrices and all row/column sign normals, verifies norms, source inequalities, antipodal closure, spanning rank, and the polar contact relations with exact integer arithmetic. Finite computation is corroborative only and does not assess originality.
