---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Theorem 6.3 specializes exactly as claimed: Example 7.5 has radical dimension two, so every shortest LCD embedding is obtained from \(B=U^{-1}[D;E]\) with \(D\in\mathrm{GL}_2(R)\) and arbitrary \(E\in R^{1\times2}\). Reduction modulo \(u\) gives \(|\mathrm{GL}_2(R)|=6\cdot 2^4=96\), and there are \(4^2=16\) choices for \(E\), hence 1536 labeled embeddings. I independently reimplemented the finite enumeration from the actual package formulas: all 1536 distinct matrices were generated, all 64 codewords of each were checked, and the exact census \((3,6):768\), \((4,7):720\), \((4,8):48\) was reproduced. Every binary Gray generator had rank six and nonsingular Gram matrix. The 48 distance-eight images split exactly 32/16 between the two stated weight distributions.

## originality

PASS

The complete An--Kim manuscript was inspected through Theorem 6.3 and Example 7.5. It explicitly says that all shortest embeddings were enumerated with MAGMA and then publishes one embedding having the largest minimum distance; for Example 7.5 it gives one ring-distance-four embedding whose Gray image is optimal \([20,6,8]\). It does not publish the total 1536 count, the full 768/720/48 ring/Gray-distance distribution, the fact that every Gray image in the family is binary LCD, or the two optimal weight-enumerator multiplicities. Those data are not implied by the existence of one maximizer or by the abstract parametrization without carrying out the finite classification.

## value

PASS

This is a natural complete finite classification attached to a source example whose authors themselves optimize by exhaustive enumeration. It quantifies how rare the optimal Gray distance is, separates ring and Gray distance behavior, establishes LCD status uniformly, and proves at least two permutation-inequivalent optimal Gray-image types. Those are motivated exact invariants of the complete shortest-embedding family rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
