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

The claimed law applies to all \(n\ge1\) and \(q=2^e\), with uniformly distributed **invertible** structure matrices, and does not sample unweighted isomorphism classes. The proof reduces the nonassociative idempotent equation to semilinear fixed points, performs Frobenius descent, matches twisted-conjugacy orbit sizes to conjugacy-class weights in \(\mathrm{GL}_n(\mathbb F_2)\), then performs exact subspace Möbius inversion. Lang's theorem is cited rather than reproved.

The standalone checker `evolution_idempotent_checker.py` enumerates all invertible matrices and all their rational idempotent vectors in eight configurations: \((2,1),(4,1),(8,1),(2,2),(4,2),(8,2),(2,3),(2,4)\). Exact tested-matrix total: \(24{,}053\). It compares **whole rank distributions** rather than only expectations. Final successful output: `ALL_CHARACTERISTIC_TWO_EVOLUTION_CHECKS_PASSED 24053`.

Finite exhaustive tests cannot justify untested dimensions and field orders; the general result is established mathematically by the proof in RESULT.md. Idempotent count is always at least one because zero is idempotent. No claim is made in odd characteristic or for singular structure matrices. Historical uniqueness is not independently certified. Independent audit: not performed.
