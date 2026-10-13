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

# Verification and reproducibility

The standalone checker is `checker.py`. Run `python checker.py` in Python 3 without third-party dependencies. It constructs the 2-state Markov law by exact-rational recursion for lengths 4 through 36, compares the adjacent-center difference against the independent binomial coefficient expression for 680 parameter/length combinations, verifies normalization and strict finite-threshold inequalities, and checks the explicit size-reversal example. The run reported: `PASS 680 exact-rational parameter and chain-length comparisons; reversal example PASS`.

The universal theorem is analytical. Its nontrivial steps are: enumeration of switched runs, three exact binomial identities, preservation of symmetric unimodality under convolution, a strict coefficient-difference recurrence, and an aperiodic lattice local central limit theorem. Finite testing cannot establish the general statement or historical priority.

No independent audit or independent validation is asserted.
