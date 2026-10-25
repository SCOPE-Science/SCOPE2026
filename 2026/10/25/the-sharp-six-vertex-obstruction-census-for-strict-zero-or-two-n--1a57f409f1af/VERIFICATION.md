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

# Reproducibility

Run `python3 verify.py` from the directory containing this file. It requires only the Python standard library and uses exhaustive integer arithmetic.

The script enumerates every possible simple labeled graph at orders one through six, evaluates all possible binary strategy states for each, and prints the failure counts (respectively 0, 0, 0, 0, 0, 300). At order six, all 300 graph masks without equilibrium must equal the disjoint union of the permutation orbits of the eight-edge and nine-edge witnesses. It verifies orbit sizes 180 and 120, all corresponding edge counts, and automorphism-group sizes four and six. A separate edge-iteration implementation checks 10,816 selected graph-state pairs against the main bit-mask rule. The expected final line is `CERTIFICATE_OK`.

The finite enumeration is exhaustive for these specified sizes, and no conclusion about seven or more vertices is implied. The nine-edge 3-sun obstruction is already published. The certificate supports the new minimality, second witness and completeness claims; it is not an external scientific audit.
