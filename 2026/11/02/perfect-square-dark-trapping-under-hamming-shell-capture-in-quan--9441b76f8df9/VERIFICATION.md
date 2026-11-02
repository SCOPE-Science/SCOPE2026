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
# Reproducibility and limits

Run `python verify.py` from the folder containing the included file. The program requires Python 3, NumPy and SciPy; it has no network access requirement. It checks integer Krawtchouk zeros for \(2\le d\le300\), first-and-second-shell incompatibility, eigenvalues and shell overlaps of the exact radial tridiagonal matrix for \(2\le d\le30\), and full-hypercube versus radial wavefunction norms for \(2\le d\le7\), two positive capture strengths and three times. It separately checks the exact fractions in square dimensions \(4,9,16\). On execution, the program reported `PASS diagnostic groups: 1130`.

The mathematical proof in RESULT.md, rather than finite verification, establishes the results for every integer dimension and every positive capture strength. The full-space dark eigenspace is not classified, no speed of decay or finite-time absorption distribution is claimed, and no independent audit has been performed.
