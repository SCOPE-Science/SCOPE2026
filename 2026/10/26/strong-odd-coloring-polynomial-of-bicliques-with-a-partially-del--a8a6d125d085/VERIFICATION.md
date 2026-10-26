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

Run the standalone standard-library Python 3 script using `python verify.py`. It builds matching-deleted bicliques from their adjacency lists and independently checks proper colorings and every color multiplicity in each open neighborhood. It enumerates restricted-growth-word partitions rather than assuming the claimed odd-block characterization, and compares coefficient distributions with an independently coded odd-Stirling recurrence. It additionally enumerates all assignments from palettes of one through four colors on six small graphs. Both methods agree with the theorem; the recorded output is in `verification_output.txt`.

**Actual checks:** 26 valid parameter triples, 945,707 independent set partitions, 24 complete named-palette enumerations, full predicted versus measured coefficients, optimal-color counts, and minimum-partition multiplicities. All checks passed.

**Limits:** The checks cover graphs with at most ten vertices and small named palettes. They cannot prove the theorem for all integers; the universal result is established by the odd-class/maximality argument in `RESULT.md`. No independent audit was performed.
