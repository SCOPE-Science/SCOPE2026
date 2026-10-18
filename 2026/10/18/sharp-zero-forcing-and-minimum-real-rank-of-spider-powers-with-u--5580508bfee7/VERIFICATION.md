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

The accompanying `verify_spider_powers.py` is a standard-library Python 3 program. Run `python3 verify_spider_powers.py` from a folder containing that file. Its recorded output is in `verification_output.txt`.

The independent graph builder first creates the original tree and computes adjacency in the ordinary \(k\)-th graph power by repeated neighbourhood expansion. For each test instance, the script independently constructs the specified symmetric integer matrix and tests its complete off-diagonal support against the computed power graph. It also checks \((m-1)k\) explicit kernel vectors by exact integer multiplication, verifies their prescribed independent initial-coordinate structure, and computes the *actual* rational matrix rank using fraction arithmetic rather than floating point.

It then follows the proposed chronological forcing list and checks every force against the current blue set and white neighbours. Across 53 instances, with \(2\le m\le5\) and \(1\le k\le4\) and both equal and unequal arm lengths, all matrix and force checks passed. For five smaller instances, an independent closure implementation checked 10,981 initial seed sets of sizes strictly below \((m-1)k\); none forced the graph. The output file preserves the actual printed test summary.

These finite checks do not prove the general theorem, enumerate every graph, verify positive semidefiniteness, or establish publication priority. The universal lower bound follows from the dimension of the exact matrix kernel; the universal upper bound follows from the explicit forcing schedule. No independent audit has been performed.
