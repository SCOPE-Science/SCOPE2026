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

The exact standalone checker is `artifacts/verify_radau_cycle.py` (Python 3 with SymPy). Running the script reconstructs the stability function from its Runge–Kutta tableau, expands its Taylor series, verifies the modular inverse coefficients for dimensions two through six, checks rational matrix inverses at explicit rational step sizes, and reproduces all coefficient-sign and root-isolation statements used in the proof. The recorded run reports 158 successful assertions; the result is also supported by a self-contained analytic shortest-path argument, polynomial inequalities, and a Fourier-limit argument.

The rational root interval uses integer arithmetic. The checker does not prove that no unsearched earlier article contains an equivalent statement. Independent audit has not been performed.
