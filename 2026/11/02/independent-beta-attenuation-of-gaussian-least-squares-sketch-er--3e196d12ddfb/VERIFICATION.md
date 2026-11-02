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

# Reproducible mathematical and numerical checks

Run `python verify.py` with NumPy and SciPy installed. The script was executed successfully on the packaged program and reported `PASS: 845 analytical, matrix, and seeded statistical checks; direct-Haar KS=0.01054, tail ratio=0.484848484848`.

The direct-sketch component uses 26,000 independently generated Haar frames from QR factorizations of standard Gaussian matrices, alongside 26,000 independently generated Gaussian sketches. The comparison distribution is sampled separately from independent beta, chi-square, and Gaussian variables. There are additional exact beta-moment identities checked over a range of dimensions, deterministic CDF integrals for scalar error, and asymptotic tail-ratio checks at three high thresholds. The seed is fixed in the included program. The seeded finite simulations are diagnostics rather than proofs of the infinite-dimensional or limiting statements.

The analytical proof in `RESULT.md` establishes the complete finite-dimensional distributional coupling, all positive moment thresholds, and the sharp far-tail asymptotic. Its essential unproved extensions include higher-rank designs, complex sketches, and non-Haar structured orthonormal transforms. Source priority has not been independently certified.
