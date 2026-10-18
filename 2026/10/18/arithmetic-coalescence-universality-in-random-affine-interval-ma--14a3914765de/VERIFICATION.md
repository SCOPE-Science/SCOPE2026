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

# Verification and reproducibility

The proof is entirely analytical. The arithmetic reduction follows from the identities \(d\mapsto bd-m\) under expansion and \(d\mapsto d/b\) under every contraction, where \(m\) is an integer. It yields exact absorption of a nearest-neighbor walk at denominator depth zero. The ballot theorem yields the full law; the smallest quadratic generating-function root yields meeting probabilities and moments; reflection yields the critical heavy tail; and a first-order expansion at \(p=(1+\theta\varepsilon)/2\) with Laplace argument \(z=e^{-u\varepsilon^2}\) yields the Brownian first-passage crossover. The accompanying script `verify.py` uses `fractions.Fraction` and separately follows every selected affine branch on two trajectories, aggregating exact rational probabilities before comparison with the closed formula.

Reproduction: execute `python verify.py` in the same directory as `RESULT.md`. Successful execution prints `PASS: 511 exact rational comparisons across bases 2, 3, 4, and 6.` The verifier compares four integer bases, including the composite base \(6\), three expansion probabilities, multiple denominator depths and starting locations, a gap of denominator \(2\) in base \(6\), and finite-horizon nonmeeting of non-base-adic gaps. All tests passed when the package was prepared.

Finite checks do not prove the absence of collisions at arbitrary times, the drift-dependent hitting probability, the infinite critical tail, or the scaling limit; those conclusions rely on the independently stated mathematical arguments in `RESULT.md`. No independent mathematical audit or external formal certification has been performed.
