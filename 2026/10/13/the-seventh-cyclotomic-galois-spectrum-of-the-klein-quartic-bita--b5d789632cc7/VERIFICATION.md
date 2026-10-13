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

# Reproducibility record
Execute `python verify_klein.py` with Python 3 and SymPy installed. The program stores exact representatives of \(\mathbb Q[\zeta_7]\) in the integral power basis and reduces modulo \(\Phi_7\). It checks the three invariant-pullback equations, completes the entire 28-line orbit, computes the full Galois action, and uses resultant norms plus common polynomial gcd tests to rule out pair coalescence at every odd prime except seven. The 378 pairwise norm-gcd histogram is asserted, as are the six fixed counts and Galois-orbit decomposition.

The program also enumerates all \(p^2+p+1\) rational lines independently at \(p=3,5,11,13,17,19,23,29\) and detects whether the restricted quartic is a square over the prime field. The corresponding output counts are \(1,1,1,4,1,1,1,28\). The eight finite enumerations alone cannot establish the infinite-prime statement: the proof uses exact cyclotomic Galois action, resultant divisibility and residue-field coprimality for that step. No assertion in characteristics two or seven is tested or inferred by extrapolation.

The verifier is an ordinary symbolic checker, not a formal theorem prover or an independently certified mathematical artifact. No independent audit has been performed.
