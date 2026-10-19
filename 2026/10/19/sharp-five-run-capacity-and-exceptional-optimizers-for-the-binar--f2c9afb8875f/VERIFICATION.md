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

# Reproducibility checks

Use Python 3 standard library and run `python3 verify.py` in the folder containing the files. The script uses no network, third-party packages, or external data.

It enumerates **every** binary host of length \(n\in\{4,5,6,7,8\}\) and evaluates \(c_{0101}(w)\) twice, once by a standard backwards dynamic program and once directly by all four-position subsets. The exact unrestricted maxima are \(1,2,5,9,16\). It also exhaustively checks the low-run optimum for every length from \(4\) through \(12\), checks the six-run count identity through length \(512\), and checks the signed residue expression through length \(4096\).

The all-length proof requires no extrapolation: the four-run balanced-product bound, the unused endpoint block for five-run hosts, the explicit six-run count identity, and four elementary positive polynomials establish the universal part. Only the three exceptional global comparisons require finite exhaustive enumeration. Python integer arithmetic is exact; no randomized samples, timeouts, or approximate certificates are used.

Originality was compared with the cited primary source, which already covers the length-six failure, and other pattern-packing literature. No independent literature or proof audit was performed; an unknown equivalent published result remains a residual risk.
