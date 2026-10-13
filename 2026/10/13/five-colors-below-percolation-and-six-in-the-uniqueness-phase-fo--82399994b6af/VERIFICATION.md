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

The proof uses the following checked source implications.

For amenable \(G\), the Bernoulli graphing \(\mathcal B(G)\) is hyperfinite. If all percolation clusters are finite, the quotient relation is smooth with finite classes, so the quotient graphing \(\mathcal B(\widetilde G_p)\) is hyperfinite. Proposition 3.5 makes it pmp, and the source explicitly observes that planarity of \(G\) gives Borel planarity of \(\mathcal B(\widetilde G_p)\). Finite clusters in a locally finite graph yield a locally finite quotient.

Theorem 6.4 therefore gives a measurable \(5\)-coloring, and Corollary 3.6 transfers it to a factor-of-iid coloring:
\[
\chi_{\mathrm{fiid}}(\widetilde G_p)\le5.
\]

When there is a unique infinite cluster, Definition 3.4 restricts the quotient graphing to finite components and Proposition 3.5(3) converts a measurable coloring there into a partial factor whose domain contains all finite percolation components. The same hyperfinite-pmp-planar argument supplies five colors on that domain.

The event that a vertex belongs to an infinite percolation component is measurable and equivariant. Assigning one fresh sixth color to the unique infinite component completes the partial factor. Since no finite component uses that color, every quotient edge incident to the infinite component is proper. Hence
\[
\chi_{\mathrm{fiid}}(\widetilde G_p)\le6.
\]

## Limits

The proof supplies upper bounds only. It does not establish sharpness.

The unique-infinite-cluster argument does not extend as written to a phase with infinitely many infinite clusters.

No finite computation, simulation, or asymptotic approximation is used.
