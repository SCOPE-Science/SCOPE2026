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

The included `checker.py` runs without dependencies outside the Python standard library. Execute `python3 checker.py` from the artifact directory. The final line for the completed check was `ALL_CHECKS_OK`.

The orientation check covers all \(2^n\) orientations of predetermined distinct local minima for each \(n=1,\ldots,11\). It compares directly evaluated Gödel modalities against the one-greater/one-equal/remaining-less trichotomy, including the \(n=1\) boundary. Additional seeded simulations use 160,000 independent-uniform samples for each of five row lengths and check three joint probabilities per length against the analytic formula with explicit numerical tolerance.

A direct analytic proof, including conditional fair orientation, the joint survival–CDF integration, singular measure decomposition and limit calculation, is in RESULT.md. The checker is finite and does not independently establish infinite-size convergence, originality or mathematical value. No external validation has been performed.
