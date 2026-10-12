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
The proof was reconstructed from the stated normalization \(u'=-Lu\) and the exact identity \(C_h=2(I+\tfrac h2L)^{-1}-I\). The key nonstandard step is the complete-bipartite diagonal-resolvent calculation. It was checked in two ways: by direct spectral-projector algebra in the proof and by exact-rational matrix inversion in `verify.py`.

`verify.py` checks, for exact rational step sizes and many small \(p,q\), that the inverse matrix has exactly the two claimed diagonal values, that their difference and the threshold numerator factor as stated, that every Crank–Nicolson row sums to one, and that all off-diagonal entries are positive. It also reconstructs the exact \(K_{2,3}\), \(h=1\) witness with diagonal \((-1/35,-1/35,1/7,1/7,1/7)\).

These finite replays do not prove the theorem for infinitely many \(p,q\); that quantifier is discharged by the symbolic spectral decomposition and factorizations in `RESULT.md`. No claim is made for directed or weighted nonsymmetric generators.
