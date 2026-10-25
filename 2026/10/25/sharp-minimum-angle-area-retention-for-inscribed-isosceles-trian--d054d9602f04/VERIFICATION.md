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

# Verification and boundaries

The analytical result reduces to three candidate area fractions (cited theorem and direct similarity/cosine-law computations), then to a monotone one-variable minimax and one polynomial factorization. Each angular threshold from \(0<\vartheta\le\pi/3\) is treated; at the endpoints the degenerate limiting triangle is excluded and the equilateral case is included.

`CHECK.py` is a self-contained Python standard-library diagnostic. Execute `python CHECK.py` in the directory containing this file. It uses bisection to find the sharp branch threshold, checks 600 positive minimum angles, over 70,000 feasible normalized side configurations and monotonic perturbations, and compares the left and right one-sided derivatives. The output is numerical corroboration, not infinite certification.

The published prerequisite is Ambrus et al., arXiv:2205.11637v1, Theorem 1.2(ii) and Corollary 2.4, with detailed proof in Section 3. Their original source was read in open HTML. No independent replication of that multi-case published proof is asserted. The new minimax proof is self-contained once that published theorem is accepted. There is no expert, third-party or independent validation claim.
