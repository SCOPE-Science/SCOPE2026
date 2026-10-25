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

# Verification scope
The accompanying `verify.py` can be run with NumPy and SciPy using `python verify.py`. It checks the exact support optimization by an independently formulated linear program for dimensions \(2\) through \(8\), the root identity and active-support count, half-normal moment formulas by direct quadrature, and the finite moment relation \(d\mathbb E(Y-t_d)_+^2=d\Pr(Y>t_d)-t_d^2\). It also prints seeded finite-dimensional simulation diagnostics for the claimed joint weak limit. The independent LP has explicit auxiliary variables for all absolute values and the maximum-coordinate constraint.

The initial replay completed 105 linear-program comparisons, 105 threshold-root and exposed-rank comparisons each, ten independent numerical quadratures, and five deterministic threshold-moment identities. For \(d=10000\), 1000 reproducible simulated directions gave empirical centered covariance approximately \(\begin{pmatrix}1.006&-0.505\\-0.505&0.818\end{pmatrix}\), whose slow convergence toward \(\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\) is expected from Gaussian-tail corrections. These finite calculations neither prove the infinite-dimensional limit nor independently assess originality or mathematical importance.

# Analytical checks and limits
The proof derives the limiting covariance from a two-coordinate triangular-array central limit theorem and the stochastic implicit-root mapping. In particular, one must retain the randomness of the active coordinate count in converting the threshold functional into rank fluctuations: the limiting second coordinate is the count fluctuation **minus** the width fluctuation. The Gaussian radial factor is negligible after multiplying by \(t_d^2\). No verification of every possible equivalent theorem in the broader literature is asserted. No independent mathematical audit has been performed.
