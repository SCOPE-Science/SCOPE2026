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

The proof was replayed symbolically from the cited source statements. No numerical experiment or finite exhaustion is used.

For an unbounded curve away from the fundamental rays of \(Q\), Lemma 3.2 gives \(|\Re Q(z)|\ge c|z|^m\). Since \(R(z)=O(|z|^k)\) with \(k<m\), one of \(\exp(Q)\) and \(\exp(-Q+R)\) dominates exponentially and cannot be cancelled by the polynomial term.

On an asymptotic fundamental ray, the noncoincidence of the fundamental rays of \(Q\) and \(R\) gives a fixed sign and \(|\Re R(z)|\ge c|z|^k\). If the sign is positive, boundedness of \(F\) would give a polynomial-size sum of two exponentials whose product is at least \(\exp(c|z|^k)\). Hence the terms have asymptotically equal moduli and opposite phases, so \(\exp(2Q-R)\to-1\). Lemma 3.4 forbids this on the asymptotic ray because \(\deg R<\deg(2Q)\).

If the sign is negative, the product of the two exponential moduli is at most \(\exp(-c|z|^k)\). Boundedness of \(F\) requires their sum to have the polynomial scale of \(P\), so one exponential is polynomially large while the other tends to zero. Equal modulus is impossible outside a sufficiently large disk. The connected asymptotic-ray construction therefore yields an unbounded connected branch family with fixed dominance. Removing the vanishing exponential would make either \(\exp(Q)+P\) or \(\exp(\widetilde Q)+P\) bounded on an unbounded curve, contradicting Theorem 1.1.

The proof does not cover the resonant case in which a fundamental ray of \(R\) coincides with one of \(Q\); there the leading sign separation for \(\Re R\) disappears.
