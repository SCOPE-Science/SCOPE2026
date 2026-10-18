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

# Verification protocol

Run `python3 verify_core.py` and `python3 verify_alt.py` with standard Python 3. Compare their stdout with `output_core.txt` and `output_alt.txt`, respectively. Every assertion is executed on the fully enumerated state graph, not on a supplied sample. The first program constructs the Clebsch graph by XOR differences, searches partial colorings by saturation, computes connected components and all eccentricities, and checks symmetry actions. The second program independently constructs the antipodal five-cube quotient, enumerates partial colorings lexicographically, constructs recoloring edges using state-dictionary membership, and independently recomputes the full component and diameter distribution.

The first program additionally examines all vertex subsets to verify maximum independent-set size five, proving that four colors are optimal. Results claimed beyond the executable checks are limited to the finite completeness argument given in `RESULT.md` and direct consequences of checked automorphisms. The programs do not verify a priority claim or certify unrelated cases. External scientific audit has not been performed.
