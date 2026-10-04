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

The proof was reconstructed from the definitions of entropy minimality, left/right balance, factorial avoidance language, and invariant Gibbs measure. The key inequalities were checked symbolically: the empty word supplies the lower combinatorial bound, the balance constant supplies the upper combinatorial bound, and Gibbs cylinder estimates supply the two conditional-probability bounds.

The entropy step uses only submultiplicativity of \(|D_n(v)|\) and the standard entropy identity for a factorial language and its associated shift. The case in which the survivor shift is empty is handled separately by compactness, which forces \(D_n(v)\) to be empty for all sufficiently large \(n\).

Primary-source comparison confirms that Hong--Kim Lemma 4.9 proves only an eventual one-hit statement. The global entropy-difference escape formula in finite-type/Parry settings is prior work and is not treated as novel here. The accepted scope is the exact worst follower/predecessor exponent and its arbitrary-cylinder Gibbs conditional counterpart.

No numerical computation is needed. No claim is made about boundary-straddling occurrences, universal prefactors, mixing, or hitting-time limit laws.
