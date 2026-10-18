---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The four orthogonal H spectral blocks have energies (a+b)(n-1), a(n-1)-b, -a+b(n-1), -a-b; positivity of a,b rules out collisions except the two middle blocks at a=b. Projecting site-diagonal detectors to P⊗P gives n-by-n Gram G=((n-2)/n)I+J/n², eigenvalues (n-1)/n and (n-2)/n, hence rank n for n≥4. Middle blocks contribute 2(n-1) off resonance but only n-1 on resonance; E⊗E contributes one. The H-eigenvector in ker Γ argument identifies this visible spectral space with the entire eventual-loss subspace for every κ_j>0, without requiring equal rates. Independent direct projector construction in scope05_independent_checks.py checked n=4,5,6,7, every diagonal/off-diagonal localized pair and normalized symmetric/antisymmetric pairs, ranks 3n-1 and 2n. Derived v*G^{-1}v and exchange cross terms agree with all printed probabilities. Finite test corroboration is not the n-uniform proof.

## originality

PASS

The closest original complete-graph two-particle study is a discrete-time unitary coined model with phase interaction, and general continuous-time trapping work introduces the spectral-projector method but no full diagonal-collision projector evaluated on the weighted K_n □ K_n product. None of the primary statements inspected implies the rank resonance or exchange-probability transition. Distinguishable walkers and κ_j>0 are essential hypotheses. This is a best-of-knowledge exact-specialization judgment, not a proof that all literature is exhausted.

## value

PASS

An exact all-n detector-subspace dimension and rate-independent capture profile for an elementary but physically motivated reaction geometry reveals an abrupt equal-speed resonance and a symmetry-selective dark channel. This structural phenomenon is not merely rephrasing the general spectral-method lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
