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

# Verification and reproducibility

The proof constructs independent undirected Poisson edge-contact processes of rate \(1/a+1/b\), verifies both first-jump decompositions into the common \((1,1)\) residual law, and separates the fixed-width limit into rapid small-part saturation and a residual maximum of order \(a\) independent exponential waiting times. The proof's exponential-probability bounds and second-moment domination establish mean convergence, not only weak convergence.

Execute `python check.py` using a Python 3 standard-library interpreter. The program checks exact state-recursion identities, exact rational Laplace-transform decompositions and mean ordering, and fixed-seed numerical asymptotic diagnostics using a deterministic random seed. During this review it passed 526 assertions/diagnostics. The program is independent of private files and external services. Code and numerical checks cannot replace proofs of the infinite-width statements.

**Scientific limits:** \(b\ge2\) and \(k\ge1\) are fixed in the asymptotic classification, while \(a\to\infty\). The all-deadline source-optimality theorem holds for a single initial seed only. Complete historical novelty cannot be guaranteed by finite searching. Mathematical audit by an independent reviewer has not been performed.
