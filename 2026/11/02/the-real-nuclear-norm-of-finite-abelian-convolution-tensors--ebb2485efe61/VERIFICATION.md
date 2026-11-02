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

# Verification record

The mathematical proof provides two matching finite-dimensional certificates in real Fourier coordinates: an explicit rank-one expansion whose total projective cost is \(\sqrt n[r+\sqrt2(n-r)]\), and a norm-one injective trilinear functional pairing with the tensor to the same value. The complex-field comparator has matching Fourier-decomposition upper and normalized-self-duality lower bounds. All statements quantify over every finite abelian group; no general conclusion relies on enumeration.

`verify.py` (Python 3, NumPy) was executed. It passed the 13 listed abelian-group instances, checking the original convolution coefficient array, orthogonality of real and complex Fourier bases, all cross-block zeros, block coefficients and magnitudes, the equality of dual pairing and primal projective decomposition cost, and numerical unit-vector tests of the block dual witness. The independent complex Fourier decomposition was also checked for each group, with exactly the predicted character-coordinate support and coefficient amplitudes.

The sampled injective inequalities are not certificates for all vectors; their validity for all vectors is established by the complex multiplication modulus inequality and the block Hölder estimate in the analytical proof. The numerical checks cover only group orders at most nine and do not establish the general formula. No independent external mathematical audit or publication-priority certificate has been performed.
