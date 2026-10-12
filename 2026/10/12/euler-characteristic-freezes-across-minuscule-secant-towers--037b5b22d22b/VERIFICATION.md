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
The critical abstract facts are
\[
V_\lambda=\bigoplus_{\mu\in W\lambda}V_\mu,
\qquad
\dim V_\mu=1,
\]
and that a generic cocharacter separates the finitely many weights.

The checker replays this separation mechanism in three standard classical minuscule families.

For type \(A\),
\[
V_\lambda=\bigwedge^k\mathbb C^n,
\]
the weights are indexed by \(k\)-subsets and their count is
\[
\binom nk.
\]

For a half-spin representation of type \(D_n\), the weights are parity-constrained sign vectors and their count is
\[
2^{n-1}.
\]

For the vector representation of type \(D_n\), the weights are
\[
\pm e_i,
\]
with count
\[
2n.
\]

In each tested family the checker chooses an explicit integer cocharacter and verifies that all weight pairings are distinct.

Finite checks are regression evidence only. The theorem for every minuscule representation follows from the abstract Weyl-orbit and multiplicity-one properties plus Euler localization.
