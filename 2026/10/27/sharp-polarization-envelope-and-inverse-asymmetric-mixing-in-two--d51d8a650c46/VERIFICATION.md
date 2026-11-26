---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For Δ=x₂−x₁ the input difference is KΔ. A logistic chord of absolute length s has absolute response difference sinh(s/2)/[cosh(midpoint)+cosh(s/2)], maximized uniquely at midpoint zero for s>0. At λ≤0 its signed contribution opposes Δ so |Δ| decays at least as e^(−t). At λ>0 compare with y′=−y+tanh(Ky/4); at K=4, y decreases to zero and (y^(−2))′→2/3 for y(0)>0, giving the universal constant. At symmetric weights and h=−β/2 the anti-diagonal is invariant and realizes equality, so sharpness is across the allowed family. At equilibrium the chord bound forces |Δ|≤d for K>4. Equality requires centered inputs and hence complementary activities. Writing m=(x₁+x₂)/2, the mean input is h+β[m+(a−b)Δ/2], so the stated h_σ centers it at m=1/2 and actually realizes each extremum. Strict increase of artanh(d)/d on (0,1) gives the unique positive cap, with none at or below K=4. Both logistic derivatives then equal (1−d²)/4; the row-stochastic matrix has eigenvalues 1 and λ. This gives the asserted Jacobian spectrum, with H′=[d−(1+d²)artanh(d)]/d²<0 and H falling from one to zero. The stimulus midpoint and separation yield the stated inverse without sign ambiguity only when orientations are labeled; coincidence of h_+ and h_− correctly means a=b. Replay: chord identity, mean-input formula and Jacobian above or RESULT.md lines 21–41. The frozen verify.py was inspected, not executed. Neither convergence to the maximizing states, nonlinear stability at the zero eigenvalue, nor noisy identifiability is proved.

## originality

PASS

Credit the directed assignment of the optimal contrasts to their stimulus values, and the resulting identification of ordered cross-weights in the exact two-block model. The positive-λ synchronization threshold, critical comparison law, contrast magnitude and symmetric stability transition are covered or directly implied by indexed results and are not credited as new. The signed λ≤0 decay statement is a two-block refinement of the absolute row-difference bound.

## value

PASS

A maximum contrast alone cannot tell which community influences the other more: all allowed pairs with the same a+b have the same contrast bound. Optimizing over the actual controlled input and reporting the field along with the contrast resolves precisely that information loss. The exact oriented field offsets give a usable deterministic test for directed asymmetry, and the saddle/sink distinction limits when the envelope might be observed by passive relaxation. This is structural model information, not a claim of a new scalar decay phenomenon or a statistical estimation guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
