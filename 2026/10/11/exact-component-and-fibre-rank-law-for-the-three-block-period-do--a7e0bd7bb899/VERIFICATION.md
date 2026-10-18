---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Over clopen substitution phase Y0=Γ(Ypd), square shift lift is G=(Z/κ)^2 additive cocycle c(z)=(1,1−z0). Return cylinders of u_n=Γ^n(1) minus last char have two return words τ_(n−1),τ_n by parity-recognizable induction; increments v_n=(2^{n−1},2^{n−1}−s_(n−1)), w_n=(2^n,2^n−s_n), s_n=(2^{n+1}+(-1)^n)/3. Exact determinant ±2^{n−1}, entries gcd1, Smith diag(1,2^{n−1}); modular generated subgroup index gcd(κ,2^{n−1}) eventually q=2^{ν2κ}. Kang–Jäger finite clopen minimal-component theorem gives almost-periodic skew extension; future-cylinder/return-recurrence proof equates component stabilizer H with Hn for large n, then coset count [G:H]=q, fibre size |H|=κ²/q. Independently recalculated Smith determinant and modular indices for n2..5 and κ2..20, and inspected bundled check_components.py n2..9 κ2..17; these finite examples supplement, not replace, the infinite return-induction/continuity proof.

## originality

PASS

Kang–Jäger 2026 Theorem1.7 has prior odd-modulus minimality, while Theorem4.1/Cor4.2/Lemma4.11 provide finite clopen components and within-piece fibre-rank constancy. The exact number and uniform rank for every even modulus are not implications of their stated criterion; this claim adds an explicit 2-adic stabilizer/SNF law. Resultary failed; unknown older odometer-extension formula remains a risk.

## value

PASS

Classifying precisely all minimal components and common fibre ranks of a natural nonminimal finite group extension, including every even modulus, fills a concrete dynamical invariant omitted from prior minimality-only results; the 2-adic law is structural and reusable, rather than mere parity restatement or one finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
