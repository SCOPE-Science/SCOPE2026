---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A functional digraph decomposes into cycles with attached rooted in-trees; bounded height is counted by T_0=z, T_(h+1)=z exp(T_h), with F_(h,d)=exp(∑_(j|d)T_h^j/j). Subtracting adjacent heights and Möbius inversion isolates maximum depth and lcm period. At h=0 the positive powers form an ambient permutation cyclic subgroup, at h=1 their positive powers form a cyclic subgroup of order p with its own local identity, so exactly φ(p) positive powers generate the same ambient-identity submonoid; at h≥2, f is the unique power capable of generating f again. Correcting n^n counts only depth≤1 maps; those are determined by cyclic vertex set, its permutation and arbitrary one-step tails. Positive-coefficient bound of 1/(1−ze^z) at z=1/2 and Stirling yields the stated exponential error. Independent literal monoid equality and multiplicity n=1…5 corroborates.

## originality

PASS

Qualified PASS for exact embedded labeled h,p census and asymptotic uniqueness. Elliott–Levine–Mitchell count abstract monogenic submonoid types, not actual labeled subsets. Published monounary-algebra enumeration treats a different common source-height condition and does not identify cyclic-power generator fibers.

## value

PASS

The explicit sharp h=1/2 generator-rigidity threshold transforms the standard functional-digraph species numerator into a nontrivial embedded-submonoid profile; the exponential rarity law quantifies how often distinct maps collapse to one generated submonoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
