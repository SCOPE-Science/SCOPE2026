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
# Reproduction and verification

Run `python verify.py` with SymPy (version 1.10 or later). This verifies the quadratic-residue edge orientation, the full directed flag face vector, the complete binary induced-homology census of 462 five-element subsets, the 55-member affine orbit, and the integer six-triangle sphere cycles.

Exact integral Smith normal forms certify the nonzero factors of the third boundary as 54 copies of one and one copy of two, and the concatenated third boundary plus sphere-cycle matrix as 65 copies of one. The rational second-boundary rank is 45. The latter 65 ones, together with the kernel rank, prove integral spanning. For the torsion cycle, the verifier computes all 110 coefficients of the summed tetrahedral boundary as 55 copies of plus two and 55 copies of minus two. It verifies that the halved chain is an integral cycle. Full column rank of the third boundary proves nontriviality of the order-two class.

Successful direct execution returned:

`VERIFY_OK 11_VERTICES 55_SPHERE_CARRIERS 55_AFFINE_ORBIT`

`CHAIN_FVECTOR 11_55_110_55 RANK_D2_45 RANK_D3_55`

`SMITH_D3 54_ONES_AND_2; SMITH_D3_PLUS_SPHERES 65_ONES`

`CANONICAL_TORSION 110_TRIANGLES 55_PLUS_55_MINUS`

No finite-sample inference for a larger graph family is used. Published background supplies the pre-existing ambient homotopy classification; the new spanning and minimal-support statements follow from the exact computations in this package. Independent external audit has not been performed.
