---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The primary definitions confirm that incomparable averages may have size one and that a very-fast-growing family satisfies \(s(\beta_{j+1}^*)>2^{h_j}\). Proposition 3.1 gives the needed pointwise bound \(|\alpha_i^*(x_s)|\le1/s(\beta_i^*)\). From a first hit of size at least one, the next size is at least three; the size-three case must be incomparable, and labels \(2,3,4\) cannot support three pairwise incomparable nodes, so its support maximum is at least five. Hence the third size is at least \(33\), its support maximum at least \(38\), and the later squared tail is bounded by \(4^{-37}/3\). The lower witness was independently checked: \(3,4,5\) are pairwise incomparable, \(64,\ldots,96\) are 33 nodes on one level, and the size jumps \(3>2^1\), \(33>2^5\) hold. High-precision recomputation gives width \(8.3670225\ldots\times10^{-24}\).

## originality

PASS

Best-of-knowledge originality passes. The complete primary Proposition 3.1 proves only \(1\le\|x_s\|_\alpha\le2\), using a coarse tail estimate. The audited bracket needs the first two forced support-size jumps, retention of the evaluation vector in \(\ell_2\), and a separate near-extremal witness. Resultary returned no older same-object bound.

## value

PASS

Uniform segment-sum boundedness is a central design feature of the new tree norm. Pinning its optimal constant to a width below \(8.368\times10^{-24}\) and furnishing a concrete near-extremal segment determines a natural exact-scale invariant rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
