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

The standard-library program `checker.py` was executed on the exact bytes supplied here. Its recorded stdout is embedded as `checker_output.txt`, and the final line is `CERTIFICATE_OK: no circular string attractor of size 4096`.

The checker reconstructs the binary cycle two ways, verifies every length-sixteen cyclic factor is different, exhaustively locates every occurrence of the six certificate factors, and computes the cyclic residues not intersecting those occurrences. Their union equals the entire residue set \(\{0,1,\ldots,15\}\). This certifies exclusion of all the only possible density-bound sets, by the gap lemma proved in RESULT.md. Smaller dyadic cases are checked by complete factor-residue incidences. These are finite exhaustive checks, not evidence for further orders.

**Limits.** Neither an attractor of size \(4097\) nor exact optimality at order sixteen has been established. The result is a strict lower bound, and the manuscript does not supply an independent external audit.
