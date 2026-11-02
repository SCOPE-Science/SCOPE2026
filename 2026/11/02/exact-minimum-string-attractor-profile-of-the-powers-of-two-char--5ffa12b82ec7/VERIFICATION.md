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

# Verification of the exact powers-of-two attractor profile

The theorem is proved for all positive prefix lengths in `RESULT.md`; the following finite checks are reproducibility tests, not substitutes for the proof.

Run `python3 verify.py` using Python 3 and only the standard library. The program constructs the characteristic word directly from the power-of-two index condition, computes explicit proposed attractor sets and the exact proposed size, and independently enumerates every distinct substring to confirm that a chosen position is crossed by some occurrence. It performs this factor coverage test for all lengths from 1 through 184 and further lengths 191, 192, 223, 256, 383, 384 and 512.

For each of those lengths, it separately constructs disjoint sets of factor occurrence regions corresponding to the lower-bound proof. At odd dyadic depth it checks this certificate on the dyadic prefix, which is the case used in the projection lemma; at even depth it checks the pertinent dyadic or high-block certificate on the actual prefix. Every occurrence of each witness factor must be confined to its designated region, and the regions must be pairwise disjoint. A third test exhausts all possible selected-position sets for lengths 1 through 14 to confirm the claimed minimum directly, without assuming the proposed attractor.

Expected and observed output:

`VERIFY_OK: factor coverage, disjoint-occurrence witnesses, and exhaustive small-prefix minima`

**Limits.** The test uses exact finite enumeration; it does not establish coverage for all lengths, certify the projection lemma for all integers, or verify publication novelty. Those matters rely respectively on the symbolic proof and on source comparisons.
