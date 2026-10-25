---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For y^5-y=x^4+x²+x over F5 the sole pole at infinity has order 4, so Riemann–Hurwitz gives genus six, Deuring–Shafarevich gives 5-rank zero, and there is exactly one rational point above infinity. Counting trace-zero values independently over F_(5^n), n=1..6, yields N=(6,6,156,646,3501,15576), matching package values; for n=2 N2=N1=6, hence no degree-two closed places. Newton power sums S=(0,20,-30,-20,-375,50), Newton identities and Weil functional equation yield full L=(1,0,-10,10,55,-25,-175,-125,1375,1250,-6250,0,15625). Reduction mod 2 is T^12+T^8+T^7+T^6+T^5+T^4+1; Rabin tests at 2^12, 2^6 and 2^4 certify irreducibility, so Frobenius char polynomial is irreducible and Jacobian is simple over F5. L(1)=11731 and trial division to sqrt(11731) proves this prime, hence J(F5) cyclic of prime order. Direct finite counts are enough for all coefficients only because genus six and functional equation, not by extrapolation; geometric simplicity is not asserted.

## originality

PASS

The identical curve appears in Tafazolian–Kazemifard Lemma 3.3 as a first possible 5-rank-zero genus with no extra geometric automorphisms; that paper supplies the model but not its complete zeta polynomial, simple Frobenius polynomial or prime-order rational Jacobian. Bouw et al and McGuire–Yılmaz study additive-polynomial covers y^p-y=xR(x) or x^(p^k+1)+ax, which over p=5 have degrees 2,6,26,..., unlike x^4+x²+x. No direct exact model match was identified in Resultary. Unread fine-grained abelian-isogeny database coverage remains a caveat.

## value

PASS

A naturally singled-out smallest rigid characteristic-five rank-zero Artin–Schreier example has concrete complete arithmetic: all extension counts from a degree-twelve Weil polynomial, base-field simplicity and a prime-order rational Jacobian. This answers a motivated exact-invariant question arising from the new geometric classification, not an arbitrary small numerical instance, even without a general-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
