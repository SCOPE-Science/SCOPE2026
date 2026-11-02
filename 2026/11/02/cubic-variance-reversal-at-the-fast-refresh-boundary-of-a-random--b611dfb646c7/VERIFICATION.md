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

# Reproducible analytical and computational checks

The proof is in `RESULT.md`, with the renewal-reward identity, explicit path-weight formula and fully uniform bound on omitted geometric-block contributions. The standalone `checker.py` requires only standard Python libraries; invoke `python checker.py` in the same folder. It exhaustively enumerates two-sided paths through length four and computes all assertions using exact rational fractions; no enumeration of finite paths purports to prove an infinite-domain theorem.

Eight rational environment laws (symmetric, asymmetric, multi-atom and deterministic) confirm four first moments, four second moments, four velocity coefficients and four diffusivity coefficients each. A separate symmetric two-atom example with retention failure `q=1/10` is checked with exact moments through block length twelve and a provable geometric remainder estimate; the accepted signs follow from the analytic Taylor theorem, not that example. The actual results in `checker-output.txt` include 129 passed exact rational assertions and the numerical values of the rational quantities.

Not established: independent verification, historical uniqueness, general refresh mechanisms or the sign exactly at the critical triangular scaling boundary.
