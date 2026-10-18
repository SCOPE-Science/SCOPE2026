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

# Reproducibility

The analytic proof in RESULT.md covers every nonzero real quartic chirp and all real delay-frequency pairs. The Airy reduction follows by a heat-equation identity and remains valid for either sign of the cubic Fourier phase. No claim that finite tests establish infinitely many folds is made.

Execute `python checker.py` using the specified Python dependencies. The accompanying `checker_output.txt` is a transcript of its successful execution. It evaluates six original oscillatory Gaussian integrals separately from their Airy expressions, tests 75 fold minima, samples nodal branch signs, and probes the asymptotic constants at the thousandth Airy zero. These tests validate normalizations and provide finite corroboration, not a computer-assisted proof of the global assertions.

The bibliographic comparison consulted the actual accessible primary texts of Babusci–Dattoli–Sacchetti (2010), Balazs–Bayer–Jaillet–Søndergaard (2011) and Moore–Filip (2025), as well as the DLMF Airy-zero formulas. Publication-priority completeness is not independently established.
