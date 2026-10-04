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

The exact checker `verify.py` uses a two-component rational representation of \(\mathbb Q(\sqrt5)\). It checks the normalized order-four signature matrices, obtaining one all-positive class, one all-negative class, and six mixed sign triples. It verifies the canonical matrices by \(G G^\dagger G=G\) and \(Gz=0\).

For the arbitrary-dual obstruction, the proof reduces a one-angle Gram matrix to
\[
H=G^\dagger+za^{\mathsf T}+az^{\mathsf T},
\qquad
H_{ij}=\beta\varepsilon_{ij}\quad(i<j).
\]
Fixing \(\varepsilon_{12}=1\) leaves thirty-two complete sign patterns. Exact row reduction finds twenty inconsistent systems. The twelve consistent patterns and their exact determinants are:

| signs | \(\det H\) |
|---|---|
| `++++++` | \(-175/16-(25/8)\sqrt5\) |
| `++++--` | \(175/144\) |
| `+++-++` | \(-35/16-(5/8)\sqrt5\) |
| `+++---` | \(-225/16-(25/4)\sqrt5\) |
| `++-+++` | \(-35/16-(5/8)\sqrt5\) |
| `++-+--` | \(-225/16+(25/4)\sqrt5\) |
| `++--++` | \(-175/16-(25/8)\sqrt5\) |
| `++----` | \(-225/16\) |
| `+-++-+` | \(-175/16+(25/8)\sqrt5\) |
| `+-+--+` | \(-35/16+(5/8)\sqrt5\) |
| `+--+-+` | \(-35/16+(5/8)\sqrt5\) |
| `+----+` | \(-175/16+(25/8)\sqrt5\) |

Every determinant is nonzero in \(\mathbb Q(\sqrt5)\), so every consistent one-angle generalized inverse has rank four and cannot be the Gram matrix of four vectors in \(\mathbb R^3\).

Replay with:

`python3 verify.py`

Expected terminal success line:

`VERIFY_OK signature_classes=1,1,6 one_angle_patterns=32 inconsistent=20 full_rank_candidates=12`

The checker certifies only the finite algebraic reduction used in the proof. The literature comparison and significance assessment are not computational claims.
