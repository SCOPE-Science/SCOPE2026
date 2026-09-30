# Independent Audit — 2026-09-29

**Record:** `2026/09/19/acyclic-signatures-complete-graphs-minus-matching--c164cb9690e5`  
**Title:** Factorial acyclic signatures for complete graphs minus a matching  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The signed orientation algebra and coefficient extraction are correct. For complete multipartite graphs, topological-order monomials are well-defined because incomparable adjacent swaps occur only within a part. Sink-layer inclusion–exclusion gives F·C=1. The even/odd decomposition reduces the full coefficient for K_{2r+s}−M_r to ordered perfect matchings among the r doubleton parts, giving (−1)^k(2k)! and hence exactly the displayed factorial cases. An independent brute-force enumeration for all tested r≤3, s≤2 reproduced every sign and zero case.
- **Originality — PASS:** Mühlherr–Poullot introduced the acyclic polynomial/signature and the nonzero-signature Hamiltonicity obstruction; indexed v2 material and exact searches for complete multipartite graphs, matching complements, and cocktail-party graphs did not reveal this factorial formula. Carballosa–Khera–Reyes treat unsigned enumeration of complete multipartite acyclic orientations. The current 58-page v2 PDF could not be obtained by the available arXiv/OA routes, and an authorized retrieval attempt returned no verified PDF, so full-text noncoverage is not claimed; this remains an explicit residual originality risk.
- **Scientific value — PASS:** The result gives an exact factorial parity imbalance for every cocktail-party graph and a parity-sensitive near-perfect-matching extension, producing an infinite dense family of explicit non-Hamiltonicity certificates. The cancellation identity is also a reusable signed-enumeration device for multipartite orientation problems.

## Independent checks

- Rechecked the F·C=1 sink-subset cancellation coefficientwise.
- Re-derived the hyperbolic even/odd simplification and the coefficient of Q^k as (2k)!/2^k.
- Independently enumerated acyclic orientations induced by all vertex permutations for r≤3 and s≤2; every signature matched the theorem.
- Searched the current v2 indexing and multipartite-orientation literature for matching-complement/cocktail-party coverage.

## Literature and evidence

- Mühlherr–Poullot, Hamiltonicity of graphs of acyclic orientations and acyclic polynomials — Primary 2026 source introduces the acyclic polynomial/signature and its Hamiltonicity obstruction; current indexing shows v2.
- Carballosa–Khera–Reyes, Encoding and Enumerating Acyclic Orientations of Graphs — 2025 full-text-indexed source gives complete multipartite orientation encodings and unsigned counts, not the signed matching-complement formula.
- Savage–Squire–West, Gray Code Results for Acyclic Orientations — Classical parity/Gray-code background for acyclic-orientation graphs.

## Limitations

- Only Ψ(D;−1) is determined, not the full acyclic polynomial.
- Zero signature is merely absence of this parity obstruction and does not imply Hamiltonicity.
- The full current arXiv v2 PDF could not be obtained through the available OA/arXiv tooling; authorized fallback found no verified PDF. No claim is made that its inaccessible pages were read.
- Older trace-monoid or hyperplane-arrangement literature under different terminology remains a residual originality risk.

**Independent-audit disposition:** passed.
