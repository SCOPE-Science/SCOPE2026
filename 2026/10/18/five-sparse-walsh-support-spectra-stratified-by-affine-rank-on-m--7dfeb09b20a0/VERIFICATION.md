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
# Reproducible verification

Execute `python3 verify_five_walsh.py` using Python 3.8 or later. No external modules or downloaded data are required. The script enumerates every Walsh-row-generated proper subspace on each canonical five-point support, tests containment of each coordinate functional, and counts all frequency rows belonging to each eligible subspace. It separately checks explicit nonzero integer coefficient vectors for every admissible support size and asserts the expected complete histograms. The reproduced terminal output is embedded as `verification_output.txt`.

All rational ranks equal ranks in the prime field of order 101: for any minor of dimension at most five, Hadamard's inequality bounds its integer determinant in absolute value below 101. Hence modular vanishing is equivalent to integer vanishing. Closure of row spans and the finite-union-of-hyperplanes argument prove that this finite check covers *all complex coefficients*, not only integer test samples. Repetition by annihilator cosets is proved for all dimensions. Verification does not establish any result about source sparsities other than five and does not constitute an independent audit.
