---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Bell overlaps of the Gibbs state define a Pauli channel. Applying two independent copies to the source input gives C_out=max{C_in lambda_perp^2-(1-lambda_z^2)/2,0}, which simplifies to the package's prefactor-4 formula. Independent direct Hamiltonian diagonalization, Bell probabilities, two-copy channel application and Wootters concurrence agreed across both signs of J and several D,T,theta values. Expanding at large |D| gives C_in/(1+D^2)+O(exp(-|J|sqrt(1+D^2)/T)), proving eventual positivity. A bibliographic detail is wrong but non-mathematical: arXiv v1 labels the printed formula Eq. (8), not Eq. (14).

## originality

PASS

Best-of-knowledge originality passes. The primary arXiv PDF was read directly: it prints the same two-copy Pauli-channel construction and the concurrence bracket with prefactor 2, then says the output reaches zero for large DM coupling. Direct reconstruction gives prefactor 4 and shows that for fixed nonzero J, positive T and nonzero input concurrence the zero limit is approached through a positive algebraic tail. No checked later source or Resultary result supplied the correction or asymptotic.

## value

PASS

Concurrence is the source's primary teleportation measure. A factor-two normalization error changes every positive output value, while the asymptotic analysis changes the qualitative strong-coupling picture by proving finite-D revival with an algebraic tail. This is a substantive source correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
