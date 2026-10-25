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

The proof in `RESULT.md` covers all positive integers \(k\), including \(k=1\). A pure-standard-library Python verifier checks all configurations modulo independent flips of paired leaf vertices and permutations of the triangles for \(1\le k\le4\). Memoized depth-first recursion terminates because each move decreases the total pebble count. It separately checks hub-only reachability for all configurations with \(4k\) pebbles and nonstackability of the asserted \(4k-1\) witness. The actual run from the included `verify.py` yields `VERIFICATION_OK`; details are in `verification_output.txt`.

The computation is exhaustive only for the listed finite orders and does not by itself certify the theorem for arbitrary \(k\). There has been no independent audit.
