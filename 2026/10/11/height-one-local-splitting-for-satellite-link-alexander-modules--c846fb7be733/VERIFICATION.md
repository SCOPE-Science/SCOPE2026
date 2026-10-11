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

The proof was checked from the following chain of source statements in arXiv:2609.36040v1:

1. Proposition 4.10 identifies the first homology of the lifted companion and pattern pieces with the corresponding Alexander modules after extension of scalars to the satellite ring \(R\).
2. Equation (4.13) gives
\[
0\to M_C^R\oplus M_P^R\to M_L\to\mathfrak K\to0.
\]
3. The proof of Proposition 4.13 places \(\mathfrak K\) inside \(R/\langle T_1-1,A_1-1\rangle\) and proves
\[
\gcd(T_1-1,A_1-1)=1.
\]
4. For a height-one prime \(\mathfrak p\), at least one of these two annihilators lies outside \(\mathfrak p\), hence becomes invertible in \(R_{\mathfrak p}\). Therefore \(\mathfrak K_{\mathfrak p}=0\).
5. Exactness of localization turns (4.13) into the claimed direct-sum isomorphism.

The consistency check against Theorem 1.11 is exact: taking Fitting orders of the local direct sum yields the source's gcd-convolution formula at every height-one valuation. No computational enumeration, numerical approximation, or unproved extrapolation is used.

Limits checked explicitly: the argument depends on both nonvanishing vectors; it does not prove global splitting; it does not classify codimension-two support or pairings.
