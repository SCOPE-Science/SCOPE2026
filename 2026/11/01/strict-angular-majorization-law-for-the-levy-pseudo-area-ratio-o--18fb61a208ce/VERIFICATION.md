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

# Reproducibility notes

Run `python levy_hexagon_checker.py` with Python 3.9 or newer and no third-party packages. It prints `PASS: polynomial identity; 4275 exact sign and numerical diagnostics` on success.

The exact polynomial differentiation identity was checked by symbolic polynomial arithmetic using integer/rational coefficients, not by floating-point sampling. The sign was also tested on 675 exact rational admissible pairs. Geometric formulas and two-angle averaging were checked on 1,200 deterministic nondegenerate random angle triples with an independently evaluated shoelace area and direct side-length pseudo-area.

The proof of the universal derivative sign is the analytic two-case inequality in RESULT.md. The finite checker cannot establish strict inequalities over an uncountable domain or establish literature novelty. Complete primary-text comparison with some historical publications remains unavailable, and there has been no independent mathematical audit.
