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

Run `python verify_star.py` and `python verify_exact.py` after installing NumPy, SciPy and SymPy. The first program constructs the complete physical matrix generator from the defining Hamiltonian, local Lindblad jumps, and hub sink; it evaluates an integrated matrix resolvent and compares to the theorem for 84 fixed-seed parameter sets and six strict-optimality examples. The second program uses exact rational matrix arithmetic for six small cases. Both programs passed against the source files embedded with this result.

The proof establishes results for all integer star sizes at least two and the continuous parameter domain; finite experiments do not replace the proof. None of the calculations constitute independent scientific validation.
