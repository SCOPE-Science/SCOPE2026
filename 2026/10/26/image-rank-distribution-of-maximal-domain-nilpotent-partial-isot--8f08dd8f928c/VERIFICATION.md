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

# Reproduction

Run `python verify.py` with Python 3 and only the standard library. The program enumerates every weakly increasing image vector for each domain obtained by deleting one point from \([n]\), independently tests nilpotence by trajectory traversal, checks fixed-point-freeness, computes actual image ranks, and compares them with two separately evaluated theoretical expressions for \(2\le n\le9\). It separately compares Narayana convolutions, exact formula values, and Catalan totals for \(2\le n\le150\). A successful run prints `VERIFY_OK_MAXIMAL_DOMAIN_NILPOTENT_RANK_NARAYANA`.

The checks do not enumerate all partial transformations with arbitrary domains or establish bibliographic priority. The general formula follows from the explicit bijections and Lagrange inversion in `RESULT.md`, not from this finite check.
