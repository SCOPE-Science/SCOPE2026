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

# Reproducibility record

Run `python verify.py` with Python 3 standard library.

The bundled checker enumerates every perfect matching through seven chords (\(135135\) diagrams at seven), computes isolated vertices and crossings by direct endpoint interlacing, checks finite exact moment identities against the closed formula, checks conditional crossing distributions against convolution laws for designated isolated chords, and tests every possible upper-tail threshold of the stochastic domination. It also checks the isolation-size-biased upper tails and algebraic asymptotic estimates at eight larger sizes.

Observed output: `PASS: 1037 exact arithmetic assertions; full matching enumeration n=2..7; all stochastic tails checked.`

The code is a finite reproducibility check. Universal stochastic ordering and the all-size asymptotic statements require the mathematical coupling and counting arguments supplied in RESULT.md. No external or independent audit was performed.
