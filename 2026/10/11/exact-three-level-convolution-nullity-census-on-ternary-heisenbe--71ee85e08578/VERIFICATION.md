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

# Verification of the three-level convolution nullity theorem

The proof's critical group-theoretic facts were reconstructed explicitly: the quotient symplectic form, the full irreducible degree count \(Q+2(3^n)^2=3Q\), the regular-block nullity weighting, and trace-zero eigenvalue multiplicities for noncentral elements. Scalar cancellation holds only for a permutation of the two nontrivial cube roots. Joint diagonalization for isotropic-independent vectors gives two vanishing eigenpairs, whereas the primitive quantum commutator implies \((U+W)^3=2I\) and hence an inverse for \(I+U+W\).

The support-census calculation distinguishes central cosets, noncentral cyclic cosets, two-fiber supports, the remaining affine lines, and isotropic or nonisotropic quotient triangles. All counts sum to \(\binom{3Q}{3}\) for every \(Q=3^{2n}\), and each count is nonnegative in the stipulated range.

The attached `heisenberg_check.cpp` is standalone C++17 source. Build and execute it with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic heisenberg_check.cpp -o heisenberg_check` followed by `./heisenberg_check`. It generates the group operation from the stated symplectic formula, constructs the complete left-convolution matrix of each tested support, and independently computes its rank modulo \(1009\). At \(n=1\), it exhausts all 2925 supports and verifies the exact distribution: 117 at nullity 18, 864 at nullity 6, and 1944 at nullity 2, with zero mismatches. At \(n=2\), it examines twelve supports, including representatives of all three predicted classes. A successful execution prints `VERIFY_OK`; failures cause nonzero exit codes.

The computation takes place in characteristic \(1009\) to make exact integer elimination efficient. It is a finite consistency check, not proof of complex ranks or of the classification for all \(n\). The unrestricted complex result rests on the self-contained representation-theoretic and counting proof in `RESULT.md`. Independent mathematical validation has not been conducted.
