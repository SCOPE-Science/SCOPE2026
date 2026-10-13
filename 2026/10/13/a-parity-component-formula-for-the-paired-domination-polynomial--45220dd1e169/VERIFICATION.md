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

# Reproducibility and verification

Run `python3 verify_rook_pair.py` in the same directory as this document; it requires only Python 3's standard library. Its two pathways are independently implemented: (a) bitset domination and recursive perfect-matching testing of every vertex subset of the rook graph, and (b) exact rational-polynomial bivariate-series coefficient extraction. They agree on every board with \(1\le m,n\le4\), i.e. sixteen boards. The largest graph has sixteen vertices and all \(65,536\) cell subsets are enumerated. The total number of paired-dominating sets counted over all test boards is \(30,118\). Output is preserved in `verification_output.txt`.

The formal argument is independent of the finite verification. Critical infinite steps are: equivalence of even edge-component sizes with a perfect matching of a line graph; equivalence of domination with exclusion of simultaneous isolated rows and columns; parity projection via the logarithm of the bipartite graph EGF; and isolated-vertex inclusion-exclusion. The proof holds for all dimensions; enumeration cannot establish that infinite quantifier. The verifier does not test any dimensions above four, audit external literature in its entirety, or constitute independent validation.
