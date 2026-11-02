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

# Verification record

The mathematical proof is given in `RESULT.md`. The critical steps are (i) observing all subset-absence events from the complete binary-history law, (ii) an exponential-polynomial zero bound, (iii) the dimension obstruction when there are too few distinct subset sums, and (iv) explicit binary-weighted duration designs. Each holds for all positive admissible parameters and all integers \(k\geq1\).

Run `python verify.py` with Python 3 and no external dependencies. It checks exact rational binary histories, Hankel–Prony reconstruction for \(k=1,2,3,4\), an exact same-history/different-occupancy example at three equal visits, separation under unequal efforts, and subset-sum cardinalities for \(k=1,\ldots,10\). These checks test representative finite identities; they neither certify the general theorem independently nor replace its proof.

An independently conducted mathematical review has not been performed. Historical priority is provisional. The result concerns structural identification from an exact population law, not accuracy in finite samples.
