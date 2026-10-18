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

Run `python verify_friendship.py` in the directory containing that file. It requires only the Python standard library. The checker independently enumerates all configurations of sizes \(1\) through \(4k\) for \(k=1,2,3,4\), follows every legal move recursively by decreasing total count, and compares actual stackability both at the hub and anywhere against the formula. Totals by \(k\) are 34, 1,286, 50,387 and 2,042,974, summing to 2,094,681. The last layer has no nonstackable configurations in each graph. It separately checks all 3,721 ordered outer-coordinate pairs up to \(60\) for the local inequalities and verifies the explicit size-\(4k-1\) witnesses. A successful execution prints `PASS`.

These checks were executed directly from the standalone file. They are finite consistency tests and cannot independently prove universal quantification over \(k\) and arbitrary pebble counts; the detailed symbolic argument is given in `RESULT.md`. The proof assumes undirected ordinary pebbling moves and nonnegative integer counts. No external independent audit has been performed.
