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

The primary endpoint construction was checked in arXiv:2609.24520v1 at Definition 2.1 and Theorem 5.1, including the explicit disjoint bumps, summability of their Sobolev energies, admissibility of the shrinking ball families, and the harmonic-series lower bound that forces failure of the modified compactly Hölder condition.

For the new closed-subspace step, choose pairwise separated translates of the compact support. Disjointness gives the exact \(\ell_p\) norm identity for both the function and its weak gradient, so the image of \(\ell_p\) is closed. The translations escape to infinity, hence the supports are locally finite and every image function is continuous. Given a nonzero coefficient, select one nonzero coordinate. The source's bad balls shrink to the corresponding translated accumulation point; from some scale onward they miss every other translated support. On those balls the linear combination is exactly the selected scalar multiple of one source counterexample, and the divergent lower bound is unchanged up to the positive factor given by that coefficient.

The conclusion is limited to the Euclidean scalar-valued endpoint \(\alpha=1-n/p\) for \(p>n\). No complementedness, metric-space extension, or classification of the entire endpoint complement is asserted.
