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

With n=2^(k+2) product_{i=1}^r p_i (distinct odd primes) multiplicativity yields exactly 2^k (P-2Q)=2^r(k+3), where P=product p_i, Q=product(p_i-1), B=P-2Q odd. Therefore k=r+nu_2(k+3), B=(k+3)/2^(k-r) must be a positive odd integer. For r<=2 B<0; for r=3 and 5 no admissible k; r=4 forces (k,B)=(4,7), prime-product bounds force p1=3,p2=5; then (p3-16)(p4-16)=233 forces p3=17,p4=249 composite, contradiction. For r=6 only (k,B)=(6,9) or (7,5); Euler-ratio monotonicity forces p1=3,p2 in {5,7,11}; modulo-3 and prefix recurrence in (7,5) force p2=5,p3>=17. Independent exact integer checks reproduced these signatures and the alleged 2023 example n=4096320, phi=1024000, tau=112, phi+tau-n/4=32. No bounded search is used as an infinite nonexistence proof.

## originality

PASS

Sándor 2023 treats the identical quarter equation and proves only unrestricted omega(n)>=4. Its closing odd-squarefree reduction uses a k+1 divisor term and an example with error 32; correcting the factor to k+3 changes the possible support signatures and excludes five-odd-prime layers. The 2022 half-equation is a different target. No searched Resultary record supplies an implication-equivalent support obstruction.

## value

PASS

The squarefree odd part is a canonical multiplicative stratum of a published equation, not an arbitrary cutoff. The theorem eliminates all support sizes up to five odd prime factors for every 2-adic exponent and isolates exact first admissible support constraints; the demonstrated numerical correction prevents invalid examples from propagating.

The dated certificate retains the supplied scientific assessment, sources and limitations.
