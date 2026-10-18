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

# Reproducible checks

Run `python3 CHECK.py` from the package directory with Python 3.9 or later. The standalone script uses the standard library and prints `OK 8260 exact checks` when successful. It executes:

1. Exact principal-minor checks for every integer \(2\le K\le14\), \(2\le b\le11\), and \(1\le m<Kb\), using fractions rather than floating-point comparisons.
2. Independent permutation enumeration and exact closed-form risk evaluation for \(2\le K\le5\), \(2\le b\le5\), three deterministic vector arrays of dimension three, and every nontrivial prefix, including partial blocks.
3. Exact matched-sample bounds for those tests, and equality at every complete-block prefix on a block-constant contrast construction for \(2\le K\le11\), \(2\le b\le11\).

The package's analytic proof also reconstructs the finite-population risk identity and the sharp eigenvalue envelope. Finite enumeration does not establish the theorem for arbitrary block counts, dimensions or data; that universal claim relies on the proof. A separate numerical check, not required for replay, compared the top eigenvalue of the directly assembled permutation-mask covariance with the two-dimensional expression for small block sizes and counts. No independent scientific audit has been performed.
