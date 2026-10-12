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
# Reproducibility and verification

The standard-library script \(\texttt{check_zeta.py}\) represents each degree-\(n\) extension using a binary irreducible modulus, checks irreducibility algorithmically, enumerates the \(2^n\)-element field, and performs two different enumerations: affine point fibers for the displayed plane equation plus the geometrically justified ramified-point correction, and the elliptic base points plus Artin–Schreier trace solvability. For \(n=1,\ldots,9\), both methods return the complete vector
\[
(4,8,4,24,44,8,116,312,508).
\]
It then generates the first ten zeta coefficients with Newton identities, imposes the established genus-nine Hasse–Weil functional equation, verifies the factor product and the numerical value \(1024\), and emits \(\texttt{NAKAJIMA_GENUS_NINE_ZETA_EXACT_OK}\). The nine finite-field counts are individually exhaustive; the functional equation is the separate theorem that upgrades these finite computations to an exact all-extension result. The proof of the requisite genus, birational equality, and eight simple poles is in the cited article, Proposition 7.2.

The numerical factorization and counts are self-review only. No independent audit, external formal proof certification, or verification of the full Jacobian rational-point group structure has been performed.
