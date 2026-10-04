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

The proof was checked at its two nontrivial interfaces.

First, the current author manuscript for arXiv:2608.01277 was inspected at the fixed-combinatorics chamber estimate and the ordinary-link upper-bound remark. It gives a uniform \((AN)^{3N}\) bound for each fixed labeled cyclic decomposition and then multiplies by at most \(N!\) such decompositions.

Second, the relabeling quotient was reconstructed directly. A cyclic decomposition of \(N\) labeled vertex slots is represented by a permutation. Renaming the slots by \(\tau\) sends the decomposition permutation \(\sigma\) to \(\tau\sigma\tau^{-1}\). Two permutations are conjugate exactly when they have the same cycle type. Thus every ordinary unoriented unordered polygonal link can be represented in a canonical model determined only by its multiset of component stick counts. Since every component uses at least \(3\) sticks, the number of canonical models is \(p_{\ge3}(N)\).

The bundled program `artifacts/verify_partition_quotient.py` exhaustively checks the cycle-type reduction for \(3\le N\le9\), including the conjugacy-class size formula and an independent restricted-partition count. Those finite checks are regression tests and are not used to justify the general theorem.

The asymptotic step uses the classical Hardy--Ramanujan formula \(p(N)=\exp(O(\sqrt N))\), so the restricted-partition factor contributes only \(N^{o(N)}\).

The independent-audit channel has not been performed.
