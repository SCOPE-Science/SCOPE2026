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

# Verification and limitations

Compile `checker.cpp` with C++17: `g++ -O3 -std=c++17 checker.cpp -o checker && ./checker`. It uses only the standard library, integer arithmetic and modular arithmetic with `unsigned __int128` intermediates. It tests primality of both reduction moduli using exhaustive trial division, checks primitive ninth roots, computes the rank of every Fourier submatrix for all row/column masks under both moduli, and takes the maximum rank. It then tests exact-support existence for all \(261{,}121\) nonempty support-set pairs by column-deletion and row-addition rank tests. Finally it partitions the accepted pairs under the prescribed affine generators and again with Fourier duality.

The first output block must report a total of \(92{,}236\) accepted pairs and the stated complete \(9\)-by-\(9\) matrix; the subsequent orbit count lines must report \(302\) and \(158\), and execution must finish with `CHECK_PASS`. Both orbit weighted sums equal the support-pair total and the incidence matrix is checked symmetric. The certificate is exact because the product of its two prime moduli exceeds \(9^{27}\), an upper bound on the absolute norm of every nonzero cyclotomic Fourier minor. The formal mathematical implications of this bound are established in `RESULT.md`.

The finite enumeration is exhaustive for the order-nine cyclic DFT, not an asymptotic proof about other group orders. The result is not an independent mathematical certification; independent audit remains unperformed. Residual novelty risk concerns older specialized positional-support datasets.
