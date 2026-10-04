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

The final claim is analytic and all-dimensional. The following checks were performed on the mathematical dependencies and edge cases.

- The recent primary source arXiv:2609.09335v2 was read at Theorem 1.1 and the intrinsic-volume preliminaries. It states that every monotone \(\mathrm{SO}(d)\)-invariant valuation on all closed convex cones for \(d\ge2\) has a unique expansion \(\sum a_kv_k\) with nondecreasing coefficients, and it records \(v_k(L_j)=\delta_{kj}\) and \(\sum_kv_k=1\). Orthogonal invariance assumed here is stronger than the source's rotational hypothesis.
- The one-dimensional case does not invoke that theorem. The four closed cones are handled directly; the two rays have equal value by \(\mathrm O(1)\)-invariance, and the valuation identity for their union determines the ray value from the zero and full-line values.
- The intrinsic-volume product rule \(v_m(C\times D)=\sum_{i+j=m}v_i(C)v_j(D)\) and the formula \(\delta(C)=\sum_k k v_k(C)\) were checked in arXiv:1303.6672v2, Sections 5.2 and 5.5. These identities give \(\delta(C\times D)=\delta(C)+\delta(D)\) exactly.
- The coefficient formula is obtained on an arbitrary \(k\)-plane by orthogonal congruence with \(\mathbb R^k\times\{0\}^{d-k}\). This covers \(k=0\), \(k=d\), and all intermediate dimensions.
- Monotonicity forces \(\gamma\ge0\) already in dimension one from \(\{0\}\subset\mathbb R\). Conversely, \(\gamma\ge0\) makes the fixed-dimensional coefficient sequence \(\alpha d+\gamma k\) nondecreasing, so the source theorem supplies monotonicity.

No numerical experiment, truncated search, or finite enumeration is used to prove the universal statement. The remaining uncertainty is bibliographic rather than mathematical: targeted searches found no equivalent published cross-dimensional classification, but the literature search is not exhaustive.
