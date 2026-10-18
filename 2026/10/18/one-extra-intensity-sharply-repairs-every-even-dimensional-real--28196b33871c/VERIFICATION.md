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

The exact theorem is established in `RESULT.md` by (1) a two-part finite geometric series, (2) Weyl-basis Fourier diagonalization of full Gabor intensities, (3) antipodal Hermitian block rank, and (4) the rank-two kernel test for all vector pairs. These checks establish every even order \(N\ge2\) and every real \(0<r<1\); no finite enumeration is treated as an infinite proof.

The standalone `verify.py` uses NumPy to construct each Gabor projector with \(r=1/2\), compute its matrix-space rank, and test the added probe \(w=(1,\ldots,1,i,\ldots,i)\). It checks even orders \(2,4,6,8,10,12\), odd orders \(3,5,7,9,11\), and one explicitly indistinguishable antipodal signal pair per antipodal location. The saved output is `verify_output.txt`. Numerical rank tolerances do not certify the universal claims; the independent analytical proof controls all orders.

No independent mathematical audit has been performed, and no experimental noise-stability guarantee is claimed.
