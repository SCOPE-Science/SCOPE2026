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

# Reproduction and limitations

Run `python3 verify.py` with a standard Python 3 installation, without third-party dependencies. The script independently generates every bijection from each domain subset to each image subset and tests pairwise adjacency preservation and reflection; it then compares every rank coefficient with the exact circular-run partition formula for all \(3\le n\le9\). The resulting totals are \(34,97,286,955,3396,12753,50482\). A successful run prints `VERIFY_OK`.

The proof in `RESULT.md` supplies the unrestricted combinatorial bijections, Stirling estimates, and fixed-deficiency argument. The finite checker is a sanity check, not a general theorem prover. The mathematical review status describes only the current internal consistency review; independent review remains unperformed. Publication-priority uniqueness is not independently certified.
