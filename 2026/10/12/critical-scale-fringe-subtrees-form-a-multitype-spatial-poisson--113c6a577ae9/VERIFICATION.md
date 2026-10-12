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
# Verification notes

Run `python3 VERIFY.py` from the same directory as the scientific files. This script needs only the Python standard library and does not import any external certificate or data file. On completion it prints a line beginning `VERIFY_OK`.

The first check inserts every uniform permutation of keys of sizes two through seven (\(5,912\) permutations) into a separately implemented binary-search-tree data structure. It compares every possible contiguous key-interval fringe-subtree event with the timestamp inequality and checks exact expected subtree counts by rational arithmetic.

The second check enumerates all \(9!=362,880\) timestamp orders on nine keys and checks exact joint probabilities in six cases: one nested interval sharing a left endpoint, one strictly interior nested interval, one sharing a right endpoint, disjoint touching intervals, separated by one key, and disjoint independent augmented intervals. The one-gap probability is independently integrated as a rational polynomial. All assertions must succeed for `VERIFY_OK`.

These tests verify the model representation and the delicate finite local-event identities. They are not an exhaustive proof for arbitrary sizes or an automatic verification of the Chen--Stein theorem; the mathematical proof derives the uniform estimates and invokes the published process-level bound of Arratia, Goldstein and Gordon (1989, Theorem 2). The continuous marked Poisson limit is weak convergence, not total-variation convergence to a nonatomic location law.
