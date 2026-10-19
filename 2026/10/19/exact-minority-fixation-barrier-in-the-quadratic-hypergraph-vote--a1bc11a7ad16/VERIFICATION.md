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

# Reproduction and verification

Run `python verify.py` with Python 3 (standard library only). The code reconstructs each interior transition probability by summing the original hypergeometric sample events, using `fractions.Fraction`, rather than relying on the derived closed quotient. It compares these probabilities to the proposed exact quotient and checks the harmonic first-step identity and symmetry for every state at \(3\le N\le12\), \(2\le d\le N-1\). It also checks monotonicity in \(d\) and the exact \(d=N-1\) binomial endpoint. The completed run reported **440 exact finite-state harmonic/reversibility checks**.

The supplemental large-population code evaluates log-Gamma ratios and compares them with the formula at \(N=300,1000\) for \(d=2,3,5,11\): **8 numerical comparisons passed** with logarithmic error below \(0.02\). These sampled large-\(N\) comparisons are not a proof of the asymptotic. The expansion, strict inequality, and monotonicity are proved in the accompanying mathematical argument by Stirling expansion, discrete Laplace's method, and an integral representation of the rate.

Reproduction assumptions: each update draws a focal agent uniformly and \(d\) *distinct* other agents uniformly, then uses the squared fraction holding the opposite opinion. The invariant state count lies in \(\{0,1,\ldots,N\}\). Only the two unanimous states absorb; there is no neutral/biased mutation and no growing-degree asymptotic asserted.
