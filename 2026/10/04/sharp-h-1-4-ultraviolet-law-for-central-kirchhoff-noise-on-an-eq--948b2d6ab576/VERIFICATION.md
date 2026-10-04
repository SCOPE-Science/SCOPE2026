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
# Verification

The claim is checked analytically by the following chain.

1. The equilateral Kirchhoff star decomposes into a permutation-symmetric sector and antisymmetric sectors. Only the symmetric modes have nonzero central value.
2. The published Kirchhoff-noise identity \(B^*=-L\) makes the central mode value the exact scalar noise coefficient when the covariance is supported at the center.
3. Itô isometry gives the displayed modal variances and therefore the exact projected \(\mathcal H_\alpha\) second moment.
4. The large-mode summand is asymptotic to a constant times \(n^{4\alpha-2}\). At \(\alpha=1/4\) the leading term is exactly \(1/(N\pi n)\), with a summable remainder; above the endpoint the power-sum asymptotic gives the stated coefficient.
5. An \(\mathcal H_\alpha\)-valued centered Gaussian random variable must have finite second moment, so divergence of the projected trace excludes such a version at \(\alpha\ge1/4\).

The included `verify.py` independently evaluates the exact finite sums for representative parameters. It checks critical slope and renormalized stabilization, one supercritical coefficient, and one subcritical convergent tail. It uses only the Python standard library and prints `VERIFY_OK`.

Limits: the numerical checks are finite and do not prove the asymptotic theorem; the proof above does. No independent audit has been performed.
