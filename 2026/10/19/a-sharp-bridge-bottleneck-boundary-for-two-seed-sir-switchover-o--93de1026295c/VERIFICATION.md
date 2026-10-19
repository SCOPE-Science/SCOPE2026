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

# Verification

The mathematical argument is fully contained in `RESULT.md`. It uses the bond-percolation representation of a deterministic-one-step SIR epidemic, conditional sampling of two distinct seeds, independent binomial leaf-edge counts, and exact third-order binomial moments. The sign proof covers every integer \(n\ge1\) and every transmission probability \(0\le p\le1\), including the boundary equalities and the single interior crossing. The macroscopic limit is obtained algebraically from the exact finite-network identity.

Run `python verification/bistar_verify.py` in a Python environment with SymPy installed. The checker independently constructs graph edge sets, iterates all subsets of retained edges, reconstructs connected components using graph search, sums outbreak sizes over every unordered pair of seeds, forms the exact symbolic probability polynomial, and subtracts the theorem's expression. It checks \(n=1,2,3,4,5,6\), covering \(10{,}920\) percolation realizations and \(907{,}792\) graph/seed-pair cases. Every polynomial difference simplifies exactly to zero. No simulation or approximate numerical sampling is needed.

This finite computation does not certify the infinite-family claim by itself; the component-moment proof does. No independent external scientific audit or independent validation has been performed. Scope excludes different infection durations, unequal transmission probabilities, more than two seeds, and arbitrary graph families.
