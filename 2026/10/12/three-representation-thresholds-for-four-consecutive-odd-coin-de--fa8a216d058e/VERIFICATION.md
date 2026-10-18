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

For odd a>=9 and A={a,a+2,a+4,a+6}, representations N=aT+2j have disjoint unique layers t=T−2k,J=j+ka, k>=0, with Q(t,J) digit-multiset counts. Direct partition counting (with 0/3-padding induction) gives Q(t,J)>=3 iff t>=3 and 3<=J<=3t−3; Q>=2 iff t>=2 and 2<=J<=3t−2. Analyze j=0,1,2 separately, and j>=3 via first Q>=3 within k=0: M0=a(2+ceil((a+2)/3)), M1=a(2+ceil((a+3)/3))+2, M2=M0+4, Mj=a max(3,ceil((j+3)/3))+2j. Higher layers cannot change these first thresholds because onset in k>=1 is strictly delayed. Mj<M2 for all j>=3, and M0=M2−4. Thus unique maximizing j=1 iff a≡1 mod3, else j=2; adding a denomination a injects representation sets so g2=max Mj−a exactly. Independently computed capped denumerants and all predicted Apéry thresholds for odd a=9..101; no finite experiment used to prove the all-odd-a theorem.

## originality

PASS

The Cardiff Mohammed thesis studies threshold for at least TWO representations (often F2) for four-term arithmetic progressions, not the at least THREE (g2 or F3) level here. Komatsu–Ying 2023 handles three generators. Komatsu–Hyun–Song 2026 covers odd blocks whose lengths increase with first denomination: for a>=9 its parameter h>=4 gives at least five coins, not the fixed four-coin family. A general p-Apéry-max identity is prior and explicitly credited; the new result is the next fixed-four-coin Apéry layer and unique extremal residue, not this generic identity. Cardiff thesis full text was not inspected end to end in this run; risk named.

## value

PASS

Computes an exact hitherto unresolved next-layer representation threshold and complete residue-level Apéry structure for a natural coprime arithmetic-progression coin family, with a unique maximizing residue. This can serve exact denumerant/semigroup computations; it is not a sweeping general p-Frobenius theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
