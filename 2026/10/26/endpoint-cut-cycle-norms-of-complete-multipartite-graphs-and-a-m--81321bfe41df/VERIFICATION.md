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

# Verification of the complete multipartite endpoint formulas

The proof in `RESULT.md` is an all-parameter analytical calculation. The supplementary `verify_multipartite.py` program uses the Python 3 standard library and does not read external files. Execute `python verify_multipartite.py` next to the other files.

The checker enumerates every unordered integer partition of every order \(N\in\{3,4,5,6,7,8,9\}\) with at least two nonempty parts. For each graph it constructs the incidence-induced Laplacian, chooses one grounded vertex, solves every unit edge divergence by an exactly inverted rational grounded Laplacian, and evaluates every projection column directly. It checks both independent column formulas, both maximization formulas, and, whenever there are three or more parts, the largest-two-parts cut rule. This covers 86 graphs and 1,572 columns. It separately checks the claimed strict rankings and rational formulas for \(K_{k,2,1}\) at each integer \(3\le k\le40\) (38 cases).

Observed execution output:

`COMPLETE_MULTIPARTITE_CERTIFICATE_OK partitions=86 columns=1572 family_cases=38`

The finite checker does not establish the general all-size claims; those rest on the explicit potential, exhaustive edge-type algebra and parameter comparisons in the written proof. No independent external audit has been conducted.
