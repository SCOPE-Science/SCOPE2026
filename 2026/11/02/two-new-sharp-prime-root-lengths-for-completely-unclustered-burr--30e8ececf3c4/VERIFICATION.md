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

# Verification performed
The included exact-arithmetic Python script evaluates the claimed construction for eligible primes up to \(2000\). For each length it checks the complete last-to-first permutation, predicted spliced arrows, single-cycle property, unequal neighboring last-column symbols, exact blockwise sorted matches, and sharp Hamming distance. For eligible primes up to \(181\), it reconstructs the primitive necklace, independently regenerates its full cyclic BWT by sorting all cyclic rotations, and recomputes cyclic input runs. Results appear in `verification_output.txt`.

The symbolic infinite proof is in `RESULT.md` and does not depend on the number of cases tested. The calculation relies on the published cyclic-run/Hamming identity and on the universal \(\lceil n/2\rceil\) bound. The condition that \(2\) has order \(p-1\) is checked for the tested primes but remains an explicit hypothesis in the theorem. No exhaustive literature-priority guarantee or external validation is claimed.
