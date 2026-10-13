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

The local classification was checked against the exact sextic formula and the published seven strata.

The replay script `artifacts/verify.py` verifies symbolically that the homogenized difference polynomial is cubic, that the local equation at \((0:1:0)\) has a transverse quadratic term and residual order four, and that when \((1:0:0)\) is present its residual term has orders two, four, or six according to the first nonzero one of \(d_2,d_3,d_4\). It also checks the affine rule \(m\mapsto A_{2m-1}\) for \(m=1,2,3\), the seven baskets, and their \(\delta\)-sum \(5\).

The checker does not prove the formal Morse lemma or the published classification of singular-point locations; those are used as mathematical inputs. The proof in `RESULT.md` supplies the local argument and explicitly states the characteristic and disjointness assumptions.
