---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Take H=R², C=C′=I, I={1,2,3,4}, v_i=1/2, W_i=H. Then E_W(f)=4(1/4)||f||²=||f||² so A=B=1. Replace all four subspaces by Z_i=span(e_2). Each difference D_i=P_{W_i}-P_{Z_i}=P_{e_1} is positive and the *per-index* theorem condition ||v_i D_i^{1/2}f|| <=(1/2)||f|| holds with eps=1/2<sqrt(A). Yet E_Z(e_1)=0, contradicting the printed positive lower A-eps²=3/4. The proof in the primary article treats an indexed difference as if it controlled the full sum. For a correct repair assume sum_i v_i²||D_i^{1/2}f||² <= eps²||f||² for all f and D_i>=0. Since E_W-E_Z equals this sum exactly, one has (A-eps²)||f||²<=E_Z(f)<=B||f||². With finitely many N indices only the per-index bound gives A-N eps². The N factor is sharp for N repeated copies of H weighted 1/sqrt(N) all compressed to a codimension-one subspace: eps=1/sqrt(N), A=1, E_Z vanishes on the missing direction. The source’s square-root positivity is explicitly retained.

## originality

PASS

The source’s Theorem 4.9 erroneously promotes a pointwise error bound to a global frame perturbation constant. A checked related controlled-K-fusion theorem uses an actual sum over all indices; its sufficient hypothesis does not make Shakoory’s pointwise theorem correct and does not contain this four-block counterexample or the sharp N amplification. Resultary retrieved various independent K-fusion perturbation defects but no matching correction of this specific theorem. The computation is adapted to precise hypotheses, not a general rebranding of the triangle inequality.

## value

PASS

A frame perturbation theorem is mathematically meaningful only if its hypothesis controls the total coefficient energy. This published result predicts a strictly positive lower frame bound for a collapsed one-dimensional family. The explicit minimal finite witness, plus sharp amplification factor N and a clean direct-sum correction, identify the actual stability requirement. This is substantive theory repair despite elementary linear algebra; the source statement concerns robustness of an entire indexed system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
