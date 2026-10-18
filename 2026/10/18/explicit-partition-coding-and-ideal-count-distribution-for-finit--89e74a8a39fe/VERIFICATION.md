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
# Reproducibility and proof checks

Run `python3 verify.py` using Python 3's standard library. It prints `VERIFY_OK` only after the following tests complete:

- All partitions of sets with zero through seven labels are decoded into operations satisfying the unit, separation, order, and cycloid identities; the decoder-to-encoder round trip and injectivity are checked for every partition.
- The number of non-unit invariant elements equals the number of blocks, and the counts by block number agree with independent Stirling-number dynamic programming for each input size from one through eight.
- For each input size at most five, a separate brute-force search of the raw L identities enumerates every permitted multiplication matrix and checks setwise equality with the partition images.
- For each input size at most six, every nonempty proper subset is tested against all four defining ideal axioms; the number of ideals matches the partition block count.

These exhaustive checks are finite and do not substitute for the proof on every size. For arbitrary size, the crucial scientific premises are the unique-extension lemma and the finite-chain decomposition in Dietzel–Menchón–Vendramin, Proposition 4.4 and Theorem 4.5, and the invariant/ideal bijection of Properzi–Qin, Theorem 4.3. All three were inspected in the primary source text. The code includes the decoder, encoder, direct operation enumeration, invariant check, and independent ideal test. No external verification or independence certification is asserted.
