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
# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library. The output starts `VERIFY_OK` when all assertions pass. The program checks the six-edge four-vertex boundary, all 24 induced orientation permutations, 21,412 simplicial-map/four-subset image checks in small cases, four-color rainbow evaluation ranks in dimensions \(m=4,5,6,7,8\) (respectively \(1,5,15,35,70\) independent columns modulo 101), and exact Fourier coefficients in \(4\le m\le7\). The rank computations over a finite field alone do not prove rational independence for every \(m\); the complete proof uses the exact Fourier orthogonality identity and the published integral dimension theorem.

This verification does not check an integral basis, all other graded representations, or an equivariant homotopy decomposition. Independent audit has not been performed.
