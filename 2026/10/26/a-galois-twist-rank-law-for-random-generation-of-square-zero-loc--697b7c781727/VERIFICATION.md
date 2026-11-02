---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Separable Wedderburn–Malcev splitting and K⊗FqK≅∏σK decompose J into K^{kσ} with σ-twisted right action. For a residue-generating r-tuple, N=B∩J is a K-bimodule; an algebra section modulo N defines σ-derivations. Ordinary derivations of finite separable fields vanish; for nonidentity σ, every σ-derivation is t(σ(a)−a). Therefore N_id is spanned by r independent uniform radical vectors, while N_σ for σ≠id is spanned by r−1 adjusted vectors b_i−(σ(a_i)−a_i)/(σ(a_j)−a_j)b_j. This linear transformation is invertible, separately by σ, making all ranks independent conditional on residues; the law is independent of the particular generating residue tuple. Gaussian-binomial rank counts give the displayed distribution. Möbius inversion over subfields gives the exact residue-generation probability and product full-generation formula; positivity iff nσ≥kσ yields the minimal positive r, including kσ=0 and m=1 boundaries. Independent brute-force F2 algebra closure verified all r≤3 and k_id≤3; examined original F4 closure checker for twisted examples.

## originality

PASS

The 2024 Sercombe–Shalev paper provides broad random-generation bounds and maximal-subalgebra structure; Iovanov–Sistko study maximal subalgebras. The complete conditional product of independent Galois-twist rank distributions and the precise full-generation probability for every r/multiplicity were not explicitly identified in the relevant inspected statements. General rank counting and finite-field separability are standard components; the coupled algebra-generated-subspace characterization is the added theorem.

## value

PASS

The result exactly classifies all conditional generated radical dimensions and full-generation probabilities for a natural complete algebra class, including all Galois twists and multiplicities. These distributions matter beyond the known minimal generator count and are not a vacuous local check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
