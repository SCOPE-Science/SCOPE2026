---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The formal integral substitution y=e^t−1 gives G(y)=Σ g_k y^k with g0..3=(1,1,2,7); Stirling expansion yields a(n)=Σ g_k k! S(n,k). Mod 2^e, factorial divisibility truncates this to a finite sum Σ c_j j^n. Odd j are Carmichael-periodic; even j^n vanish by n≥e, proving period L_e from onset e. At n=e−1 only j≡2(mod4) contribute to the Carmichael-shift discrepancy; finite binomial inversion and mod-2 fourth-difference show their coefficient sum ≡g2+g3≡1, giving exact 2^(e−1). If some earlier tail had arbitrary period Q, its least period on the tail beginning e divides both Q and L_e; this forces equality at the obstructed n=e−1, contradiction. A separate e=1 parity check gives s1=0. Independent Stirling/arithmetic checks confirmed e=2..12; universality is proved by the finite-spectrum parity argument.

## originality

PASS

Kallat arXiv:2609.07238 Proposition 2.1 proves the upper onset n≥e with Carmichael period, and Remark 2.2 expressly leaves sharpness open. A previously established least-eventual-period theorem is separately credited. The submitted result supplies the missing lower bound against every arbitrary possible period, not a restatement of upper periodicity or a finite OEIS example. Danesh preprint abstract overlaps general eventual periodicity but full text was inaccessible, leaving priority risk.

## value

PASS

This settles a natural sharp-onset question in an actively studied OEIS sequence and separates first eventual periodic index from eventual period length; the explicit boundary discrepancy has independent use in exact modular sequence dynamics. A genuine all-e impossibility statement is not inferable from a known upper onset bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
