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

# Verification and limits

The analytical result is fully stated with explicit hypotheses, frequency, transversality, multilinear Taylor tensors, cubic resolvent, algebraic reduction, and Hopf theorem application in RESULT.md.

Executable check: run \(\texttt{python verify.py}\) in the directory containing this file and verify.py. It requires the standard Python environment plus SymPy, NumPy, and SciPy. The script performs symbolic rational-function simplification and verifies the six-site coefficient exactly; it also checks the spectral inequalities and coefficient signs in 612 finite parameter cases and checks three nonlinear small-amplitude drift trajectories. These finite tests are diagnostics only, not exhaustive verification of the infinite family.

Mathematical caveats: the quotient Hopf theorem is local; the lifted full system may exhibit quasi-periodicity because of phase drift. The claimed bifurcating orbits are radially unstable, not asserted to be attracting. At the onset the critical pair has nonzero imaginary part; no statement about far-from-threshold behavior is made. The comparison literature does not establish an independent priority certificate.
