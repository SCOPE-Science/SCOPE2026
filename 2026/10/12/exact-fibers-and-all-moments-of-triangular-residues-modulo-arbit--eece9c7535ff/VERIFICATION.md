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

Identity (2n+1)^2=1+8T(n) bijectively maps odd prime-power triangular fibers to square roots; valuations and Hensel lifting give zero case p^floor(a/2), square even valuation case 2p^j, otherwise zero. Dyadic congruence T(u)≡T(v) mod 2^alpha forces v=u or −u−1 mod 2^(alpha+1), exactly two distinct preimages per output, including m=1 boundary. CRT multiplies local fibers. Summing fiber k powers over discriminant valuation classes gives local C_(p,a)(k) for every integer k>=1; k=2 simplifies to 4m product(1+a(1−1/p)). Independent exact enumeration confirmed all residues/fibers for m=1..250 and moments k=1..4 and collision totals for every m. This finite replay is supplementary; general proof is symbolic.

## originality

PASS

Best-of-knowledge extension from classical discriminant criterion and local square-root counting to explicit full-period fiber multiplicities, every positive power moment and composite collision formula; also proves Ulness Conjectures 1/2 explicitly still posed in original available material. O remains qualified due publisher full-text access restriction and classical quadratic-root literature.

## value

PASS

Resolves two explicitly published saturation conjectures and supplies all full-period multiplicities, collision counts and arbitrary power moments of a natural modular polynomial map. Broader composite-modulus formulas are motivated by additive/arithmetic distribution questions; more than a lone small or arbitrary constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
