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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and its standard library; there are no third-party packages or downloaded data. The verifier rebuilds every graph by explicit equality-of-row-or-column adjacency, computes closed neighborhoods and the maximum residual degree by bitset enumeration, and independently evaluates the inclusion–exclusion coefficients. It checks all subsets for \(2\le m\le n\le4\) and \(1\le\ell\le m+n-1\), totaling 487472 graph-subset decisions across 30 parameter triples. It also checks the exact minimum-count formulas from the distribution, and on larger boards compares 13400 deterministic pseudorandom adjacency tests against the support threshold while checking further exact polynomial minima.

Expected final line: `VERIFICATION_OK 30 487472 13400`. The recorded `verify_output.txt` was produced by execution of the packaged code. Only finitely many examples are computationally checked; the proof of the infinite claim is the structural argument in `RESULT.md`. No independent audit has been performed.
