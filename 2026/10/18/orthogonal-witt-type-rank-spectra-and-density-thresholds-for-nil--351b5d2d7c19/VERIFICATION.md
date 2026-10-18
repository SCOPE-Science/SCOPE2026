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

# Reproducibility and mathematical verification

The claim is proved for every odd prime-power field and every nondegenerate symmetric space of dimension at least two. The proof reduces algebra endomorphisms to triples satisfying \(A^{\mathsf T}BA=\lambda B\), partitions them at zero versus nonzero multiplier, counts isotropic-image maps and free central functionals, and derives the polar-space products from isotropic flags. It separately checks multiplier surjectivity for even forms, square multiplier restriction for odd forms, and all exponent comparisons in the automorphism-density limit.

The provided scripts directly test these independent instances using ordinary multiplication equations, not by enumerating the closed-form counting summands:

- `verify_evolution_orthogonal.py`: full matrix enumeration over \(\mathbb F_3\) and \(\mathbb F_5\) in dimension two, and over \(\mathbb F_3\) in dimension three; independent reduced-row-echelon isotropic-subspace counts in dimensions four and five.
- `verify_orthogonal_gf9.py`: exhaustive matrix enumeration over the genuine extension field \(\mathbb F_9\), including each two-dimensional form type.

The expected success markers are `VERIFY_OK_ORTHOGONAL_EVOLUTION_RANK_SPECTRA` and `VERIFY_OK_ORTHOGONAL_EVOLUTION_GF9`. Both scripts use the standard-library Python interpreter only. These computations are finite examples, not proofs of the theorem in unbounded dimension. Published mathematical priority and independent assessment remain unverified.
