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
# Verification

The universal argument is analytic. The following checks were used as supporting consistency tests:

1. The weak-barrier normalization was matched to the source identity \(S^*(B,S^{n-1})=2S(B)\) and to the projection formula \(\frac12\int |\langle u,v\rangle|\,S^*(B,\mathrm dv)\).
2. For the unit cube, Cauchy's projection formula gives \(\mathcal H^{n-1}(Q_n|u^\perp)=\sum_i|u_i|\), so every normalized sign diagonal yields the exact lower bound used in the proof.
3. `artifacts/verify.py` exhaustively enumerates signs for many integer coefficient vectors and checks \(\mathbb E X^2=\sum_i a_i^2\) and \(\mathbb E X^4=3(\sum_i a_i^2)^2-2\sum_i a_i^4\) exactly.
4. The same script checks the normalized pointwise inequality \(1-\mathbb E|X|\ge(1-\sum_i v_i^4)/(\sqrt n+1)^2\) and the angular fourth-mass bound on a deterministic grid.

The script is a consistency check, not an exhaustive proof over the sphere. The proof in `RESULT.md` establishes the quantified statement for all allowed dimensions, weak barriers, and angles. No claim of an optimal coefficient is made.
