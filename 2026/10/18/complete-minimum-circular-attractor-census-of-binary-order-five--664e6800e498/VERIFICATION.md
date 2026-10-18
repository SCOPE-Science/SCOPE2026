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

Run `python3 verify.py` with Python 3 in a writable directory. It exhaustively generates the binary order-five de Bruijn cycles by directed Hamiltonian walk, enumerates every seven-position cyclic-gap-bounded candidate, verifies all length-one through length-four factor incidences, and writes the complete `census.csv`. It cross-checks all 32 circular-factor lengths by direct substring enumeration on every seven-position candidate for each of the six extremal cycles. All asserted totals and boundary cases must pass before `ALL CHECKS PASS` is printed.

The observed outputs are recorded in `verify_output.txt`. Expected `census.csv` SHA-256 is `8bb608eb66f3bfac0152475146822a21df2a5ecb9665f2f9193ef22ec4291ea2`; the file includes exactly 2048 data rows plus one header. The finite proof also relies on the paper-level combinatorial reductions explained in RESULT.md: one-to-one enumeration of all rooted de Bruijn cycles, equivalence of circular gap bounds and hitting all length-five windows, and exact occurrence-incidence coverage. The program verifies no general claim about other de Bruijn orders.

These are reproducible finite checks; no external independent scientific audit has been performed.
