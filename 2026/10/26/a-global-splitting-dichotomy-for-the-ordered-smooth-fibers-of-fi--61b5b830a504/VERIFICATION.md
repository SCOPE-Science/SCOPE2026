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
# Reproducible checks and proof boundaries

The main proof is symbolic and applies for every integer \(k\ge2\). The diagonal divisors \(\Delta_{ij}\subset(\mathbb P^1)^k\) have divisor classes \(e_i+e_j\), so integer row-column operations on their relation matrix compute \(\operatorname{Pic}(F_k(\mathbb P^1))\). The included `CHECK.py` reconstructs that matrix and computes its exact Smith normal form with SymPy. Execution over \(2\le k\le8\) returned `VERIFY_OK k_range=2..8 exact_integral_smith_forms=true` with free rank one at \(k=2\), and a unique order-two factor for each \(3\le k\le8\). The universal proof for all larger \(k\) reduces the relations directly and uses a nonzero parity homomorphism to show exact order two.

The crucial noncomputational steps are (i) existence of a universal family for indivisible stable \(\delta\) over the punctured projective line, (ii) vanishing of cross-extensions for distinct stable representations with isotropic Euler pairing, (iii) identification of framed-stable quotients with a product of projectivized framing bundles, and (iv) the determinant condition for a trivial projective-line bundle. These are proved in the written result and checked against the actual framing convention of the originating paper. The computation does not certify historical priority, the moduli decomposition, or a statement about the singular-fiber strata. Independent audit is not performed.
