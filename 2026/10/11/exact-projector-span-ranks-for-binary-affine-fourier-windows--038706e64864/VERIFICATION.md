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
# Mathematical verification record

The algebraic proof derives the rank in every binary finite field of order at least four. It uses the nondegeneracy of the field trace pairing, Fourier orthogonality in the translation variable, the diagonal matrix rank of \(J+(|z|^2-1)I\), and an exact symmetric/antisymmetric column decomposition of the remaining Fourier blocks.

Run `python verification/check_affine_binary.py` with Python 3.9 or later and no external packages. The test uses explicit irreducible binary polynomials to construct \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\), reduces Gaussian integer coefficients modulo prime \(1009\) using the root \(i\mapsto469\), and performs modular elimination on each *full* affine projector measurement matrix, as well as on its separated Fourier blocks. The tested parameters are \(z=2+i\), \(2\), \(1+i\), \(i\), and \(1\). Every one of the fifteen calculations satisfies the symbolic rank identity. Expected full ranks at \(z=2+i\) are \(9\), \(49\), and \(225\), respectively.

The modular tests do not themselves certify any general statement over \(\mathbb C\) and do not establish reconstruction stability or uniqueness beyond the proved rank identity. Independent audit has not been performed.
