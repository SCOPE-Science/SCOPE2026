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

For m≥2, d=m−1, substituting n=1 into exact Edholm–Mathew Theorem 1.3 gives L(j)=1,kappa(j)=j, hence Q_{m,1}(s)=Σ_{k=0}^{2d}a_k s^k with a_k=1+(d+3)k for 0≤k<d, a_d=d²+4d+1, and a_{2d−k}=a_k. Independent coefficient derivation checked the five numerator contributions against Fourier coefficients of d+(d+2)F_d+F_{d+1}, including endpoints and middle, for arbitrary d. Their equality establishes ζ^{−d}Q(ζ)=d+(d+2)|Σ_{j<d}ζ^j|²+|Σ_{j≤d}ζ^j|²>d on the unit circle (consecutive geometric sums cannot both vanish). Reciprocity, a_0=a_{2d}=1 and no unit roots yield exactly d inner and d outer roots. Explicit z,w∈H_m realize each inner s=t root while denominator nonzero. Fresh independent direct five-term integer coefficient script verified d=1..100 as a cross-check; infinite proof is symbolic.

## originality

PASS

Full primary Edholm–Mathew article states Conjecture 4.20 for all coprime slopes and proves only differences m−n=1,2 in Theorem1.7, with additional bounded gap 3,4,6 computations. The axis n=1,m→∞ has unbounded gap and is not covered. Its general reciprocal symmetry only guarantees reciprocal pairing, not absence of unit-circle roots; earlier Edholm zero existence on another section does not imply this exact restricted-root census. New exact Fejér-square identity is strong structural proof; no equivalent prior full-axis theorem was identified.

## value

PASS

Infinite exact theorem resolves a natural unbounded axis of an explicit published conjecture, gives a positive-squares certificate for every integer d and exact interior-zero census on a canonical Bergman-kernel diagonal; meaningful beyond preexisting mere kernel-zero existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
