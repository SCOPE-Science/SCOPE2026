---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Forward confluence is equivalent to a suffix of nonempty rows whose maxima are nondecreasing: once a row is nonempty the maximum in any later row must dominate its maximum, and choosing that later maximum suffices for confluence. The diamond truth table on thresholds recovers both the active suffix and each maximum. The future-quantifying box truth table recovers each suffix-union minimum; for empty prefix rows the box sees the same suffix as at the first active row. These minima are nondecreasing and no larger than the respective row maxima. The rows {u_i,m_i} therefore realize every legal signature without changing either table. The empty relation has a separate signature. Matching tables yield matching formula interpretations by induction, and an operator disagreement is already visible with one atom. Reversing the columns and ordering the maximum row above the minimum row gives exactly a boxed plane partition. The MacMahon product telescopes to the claimed factorial ratio; its product recurrence reproduces all ten listed numbers. A partial-functional representative exists exactly on the diagonal u_i=m_i, giving the hockey-stick sum binom(2n,n). For every n>=2, even a suffix of length one permits u_1=0<m_1=1, proving sharpness.

## originality

PASS

The Boolean row data for confluence and the plane-partition formula are prior results. The independently supported contribution is the exact pointwise FIK quotient, including the suffix-minimum invariant, simultaneous bounded-branching realization and exact class counts. No inspected comparison covers that combination or supplies it by direct restriction.

## value

PASS

On the same labeled chain, this result tells one exactly which relation edges are dispensable to every formula, supplies a sharp uniform branching bound, and counts the observable structures rather than their encodings. The separation between raw and observable counts and between one- and two-successor realizations is substantive for finite-frame enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
