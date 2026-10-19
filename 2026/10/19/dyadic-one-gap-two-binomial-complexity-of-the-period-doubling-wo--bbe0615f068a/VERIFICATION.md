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

Run `python3 verify_pd_gap.py` with a standard Python 3 installation. For each exponent \(2\le m\le9\), the script enumerates both exact cyclic word families, computes all six gapped statistics by subtracting adjacent pairs from unrestricted scattered-pair counts, verifies the claimed number of distinct classes and class multiplicities, and counts cyclic `10101` patterns in the primitive family. For \(2\le m\le6\), a second quadratic implementation directly enumerates permitted index pairs and compares all six statistics word-by-word. For \(2\le m\le7\), an independently iterated substitution prefix is used to check the full factor set.

Expected totals for \(n=4,8,16,32,64,128,256,512\) are \(6,11,24,45,96,181,384,725\). The infinite theorem is established by the proof, not by the finite verification. No independent audit is claimed.
