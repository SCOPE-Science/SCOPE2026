---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The valuation identity follows directly from factoring out the common minimum \(p\)-valuation. On the primitive layer, goodness is the union of nonzero coordinate sum and the all-nonzero zero-sum configurations; the latter count is the standard additive-character value \(((p-1)^k+(p-1)(-1)^k)/p\). Common-divisibility layers contribute \((p-1)/(p(p^k-1))\). CRT gives the finite-prime product, while the large-prime obstruction is bounded by \(\sum_{p>Y}p^{-k}\) plus a union bound of order \(1/Y\) for primitive tuples. Thus the cutoff can be removed. The local bad mass is \(O_k(p^{-2})\), giving a positive convergent Euler product. Fresh counts for \(k=2,3,4\) and \(p=2,3,5\) reproduced the character count and local factors.

## originality

PASS

The primary Fan--Tóth abstract establishes the two-variable density and indicates related higher-variable questions; the exact \(k\)-variable local factor was not found in Resultary or other indexed material. The complete primary body could not be obtained through the available open routes, and the single authorized institutional fallback was unavailable, so no whole-document noncoverage claim is made. Best-of-knowledge originality passes with that explicit residual access risk because no stronger implication was identified.

## value

PASS

The theorem answers the natural fixed-dimension extension of an explicit recent gcd-density problem. The higher-variable primitive layer introduces a genuinely new finite-field obstruction absent from the pair case, and the exact Euler factor is the natural invariant needed for any further distributional or quantitative study.

The dated certificate retains the supplied scientific assessment, sources and limitations.
