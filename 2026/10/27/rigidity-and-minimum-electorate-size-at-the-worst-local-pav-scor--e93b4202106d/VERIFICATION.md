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
# Verification details

The packaged `verify.py` was run using Python 3's standard-library `fractions.Fraction`. It completed 57,627 exact rational pointwise inequality/equality tests; it generated smallest extremal electorates for each committee size \(2\) through \(14\); all swaps were checked, and all committees were enumerated through size \(6\). The mathematical proof, rather than these finite calculations, supports all integers \(k\ge2\).

For \(k=3\), there are six voters approving one member of each of two three-candidate blocs (one voter per pair involving each of two designated outside candidates) and two voters approving the third outside candidate only. The baseline PAV score is \(6\), while the optimal alternative is \(8\), giving \(3/4\), and every one-candidate swap preserves score \(6\).

No independent scientific audit or independent mathematical validation has been performed. The result depends on the mathematically explicit assumptions and the cited harmonic inequality; historical priority beyond the inspected literature remains uncertain.
