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

# Verification and reproducibility

Run `python verify.py` with Python 3.11+ and `networkx==3.6.1`, `sympy==1.14.0` as specified in `requirements.txt`. No network access or private inputs are needed. The graph is constructed from the 28 noncollinear Fano triples; all order conventions are coded and the verifier prints exact row and column indices of its integral basis certificate.

The verified output begins with `VERIFY_OK_COXETER_HEPTAGON_TORI_INDEX_THREE`. It checks exactly 28 graph vertices, 42 graph edges, girth seven, 336 automorphisms, 24 shortest heptagons and 108 disjoint heptagon pairs. The unordered deleted-product cell vector is \((378,1092,777)\), and every \(\partial_1\partial_2\) column is identically zero over the integers. Each signed heptagon-pair torus is explicitly checked to have zero integer second boundary.

A complete modulo-101 boundary elimination finds rank 700, while a 77-cycle integral minor has determinant \(-1\), establishing the integral basis. The graph automorphism actions certify orbit sizes 84 and 24 and bridge counts two and zero. The 84-orbit matrix has modulo-three rank 76; its two maximal integral determinants \(-273\) and \(5427\) have gcd three. Exact Smith computations confirm one nonunit factor three. The 24-orbit matrix has 23 unit factors and rank 23. The any-one augmentation follows from the transitive group action and the index-three quotient.

Verification is exhaustive for this specified finite graph, with no random scientific sampling: the fixed pseudo-random shuffle seed used to select one minor changes only the choice of certificate, not the underlying exhaustive lists. The assertions do not prove global novelty, any extension to other graphs, or independent scientific certification.
