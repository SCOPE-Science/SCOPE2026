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

Independent calculation for A≥1,B≥0: iterated Euler-totient tail H(2^A3^B)=2^(A−1)(3^(B+1)+1)−1, since φ(2^A3^B)=2^A3^(B−1) for B>0 followed by 2^A,2^(A−1),…,1. For n=3^k p with p−1=2^a3^b, φ(n)=2^(a+1)3^(b+k−1), so S(n)=2^a(3^(k+b)+1)−1 and n=2^a3^(k+b)+3^k. Equality iff 2^a−1=3^k. Mod 8: even k yields 2^a≡2 mod8 forcing a=1 and impossible; odd k yields 2^a≡4 mod8 forcing a=2 and k=1. Independent exact totient trajectory comparison for 156 prime/exponent instances confirms the formula; not a proof beyond grid.

## originality

PASS

Best-of-knowledge PASS for the exact empty k≥2 endpoint p−1=2^a3^b of the classical 3^k p perfect-totient problem. The 2003 and 2009 complete/principal references genuinely involve extra nested predecessor primes; neither directly covers the endpoint with no extra prime. Classical k=1 positive family is acknowledged, not claimed original. Thesis full-text access is a residual risk.

## value

PASS

The prime predecessor p−1=2^a3^b is the natural zero-extra-prime endpoint of established nested-prime trees in the open classification of perfect totients 3^k p. Uniformly ruling out ALL higher k here closes a structurally motivated infinite subclass and cleanly delineates the known positive k=1 family; it is not an arbitrary numerical slice. Although the final modulo-eight obstruction is short, the explicit tail normalization and rigorous endpoint boundary are needed to compare with published longer-chain results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
