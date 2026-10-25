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

# Reproduction and analytical scope

Run `python3 checker.py` with a standard Python 3 installation. Its recorded standard output is in `check_output.txt` and reads `PASS: 119 finite consistency assertions.` The script independently constructs truncated complex Gram systems for degree-four through degree-thirteen Fock monomials, tests the exact conditional-moment projection, and checks illustrative larger-degree two-shell values and stationary locations. Every truncated Gram approximation uses a tail well beyond the Poisson bulk for its chosen test cases.

The checker is a finite verification of formulas and selected regimes only; it does not establish uniform asymptotics for arbitrary integer sequences. The proof in `RESULT.md` contains the analytical uniform Fourier filtering, small-radius exclusion, and exact scalar optimization. No independent audit has been performed.
