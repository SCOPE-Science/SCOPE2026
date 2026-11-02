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

# Verification record

## Reproducibility

Run `python verify.py` with Python 3 and the standard library. The recorded execution prints the deterministic comparison of the renewal formula with 30,000 simulated independent search trajectories per target and terminates with `PASS: 95 independent deterministic and probabilistic assertions`. The simulation samples Brownian first-hit attempts by the exact Lévy-law representation and compares against the independently computed renewal expectation.

## Analytical checks

1. The Brownian hitting-time Laplace transform is \(e^{-s|x-c|}\); competing exponentials and the renewal equation yield the forward MFPT without finiteness requirements on moments of the source position.
2. Folded source transforms are holomorphic for \(\Re s>0\); inverse Laplace transform uniqueness is used for each target.
3. Vanishing two folded signed measures imply oddness under two reflections. Their composition yields a nonzero translation; finite total variation excludes a nonzero invariant measure.
4. The Fourier reconstruction determinant is \(\sin(k(b-a))\). Resonant frequencies are recovered by continuity, not by dividing by zero.
5. The arbitrary finite-data counterexample is a normalized kernel nullspace; the four-atom specialization uses the vector \((-1,e^{-1},-e^{-1},1)\).
6. Oscillatory sine-density sources yield exact Laplace-transform differences proportional to \((2\pi n)/((2\pi n)^2+s^2)\) while total variation remains \(2\varepsilon/\pi\).

## Limits

The probabilistic simulation and finite assertions only test examples, not the all-measure proof. Inverse Laplace continuation can be ill-conditioned. No noisy-data statistical accuracy claim and no external independent audit are made.
