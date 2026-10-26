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

# Verification notes
The file `check_local.py`, executed with the Python standard library, returned `VERIFY_OK 16 moduli delta 0.086071332055934`. It tested every prime \(r\equiv1\pmod4\) up to \(151\) and all nonzero residues modulo each test prime, with integer arithmetic, and checked the equality of the two exponential rate formulas. This finite run tests the local counting formula only; the proof of the assertion for every admissible prime is by the two square roots of \(-1\) and the Chinese remainder theorem. Neither finite experimentation nor a successful script constitutes proof of the claimed asymptotic bound.

For analytic verification, reconstruct in order the two moment-generating functions, their Markov thresholds, the identity \(t\log 2=1\), the modulus estimate \(Q\ll X^{1/4}\), the uniform Brun--Titchmarsh bound, the early-shift bound, and the exceptional primes dividing \(Q\). Then combine the cases. The quoted Mertens theorem for arithmetic progressions is used only for the displayed specialization to the full progression \(1\pmod4\).

No independent audit or external certification has been performed. The Dai--Pan paper's full text was unavailable; its public abstract was inspected. The related Yan--Xu full text was read and compared for scope.
