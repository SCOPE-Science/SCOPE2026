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

The finite-dimensional proof is in `RESULT.md`. To reproduce independent exact-rational checks, install `requirements.txt` and execute `python verify.py` in this directory.

The program explicitly enumerates full canonical occupancy configurations for small graphs, constructs the joint ON/OFF Markov generator, and independently constructs the reduced one-particle gate-modulated generator. It solves their Poisson equations by exact rational linear algebra and compares the resulting long-time variances, including the stationary susceptibility factor.

The executed checks cover a four-vertex complete graph with several gate speeds, a five-vertex cycle with disconnected OFF components at four speeds, component-orthogonal fields with no slow divergence, a connected OFF graph, and all three nontrivial particle counts on a four-vertex complete graph. Every final exact-rational comparison passed. For a two-plus-two complete-graph cut with \(k=2\), \(p=2/5\) and exchange rate \(r=3/2\), the output agrees with \(\mathcal V_\kappa=1/\kappa+5/18\). A five-cycle test has the exact rational expression printed in `RESULT.md`.

The code is a finite-instance cross-check, not a proof for infinitely many graphs or all parameter values. The general argument instead uses exact generator closure, canonical covariance, a variational lower bound, and a finite-dimensional singular Schur complement. No independent external validation is claimed.
