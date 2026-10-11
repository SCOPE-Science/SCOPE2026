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
# Verification

The family statement is verified symbolically by the free-face proof in `RESULT.md`. The computational checks are intentionally finite and independent of the published \(\Delta_2\) homotopy theorem.

Running `python3 verify.py` performs two checks. First, it exhausts every labeled simple graph on five and six vertices, selects exactly those that are connected, triangle-free, \(C_4\)-free, and of diameter at most \(2\), and verifies from the definitions that each proposed elementary-collapse pair is free and that the exact remainder is \(\Delta_3\). It finds \(17\) qualifying labeled graphs on five vertices and \(6\) on six vertices.

Second, it reconstructs the Petersen graph. The nonempty face vectors are \((10,45,120,210,252,210,120,30)\) for \(\Delta_2\) and \((10,45,120,210,252,210,90)\) for \(\Delta_3\); the difference is exactly \(30\) elementary collapse pairs. As a separate topology check on \(\Delta_3\), the program constructs a deterministic discrete-Morse matching with \(465\) pairs, checks all \(4440\) Hasse covers, proves acyclicity by topological sorting, and leaves one critical \(0\)-cell and six critical \(6\)-cells.

The replay terminates with `VERIFY_OK`. This finite replay does not prove the universal quantifier; the universal statement is proved by the explicit free-face argument.
