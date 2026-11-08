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

From the finite irreducible birth–death rates, detailed balance yields pi(k) proportional to binom(S,k)[(Z)_k(Z)_(S-k)]^q, a known Mobilia formula. The adjacent ratio of the quotient pi2/pi1 on the left half has logarithm q1*ln[(a1+d)/(a1-d)] - q2*ln[(a2+d)/(a2-d)], where a_i=(S-1)/2+Z_i and d=(S-1)/2-k. Each log equals integral_0^d 2a/(a^2-t^2)dt; the kernel ratio is strictly increasing, making F(d) a strictly increasing weighted mean for 0<d<=m<a1<a2. Allowed d run from m down to d_min (1/2 even S, 1 odd S), so the sign pattern yields exact two endpoint thresholds and a unique possible interior likelihood maximum. Reflection matches radial masses; monotone likelihood ratios imply strict tail comparisons; averaging convex test functions over symmetric K pairs gives convex orders. Independent exact integer sign grid and S=20 q2=6,7,8 regimes corroborate, but do not establish the universal integral monotonicity.

## originality

PASS

Mobilia (2015) supplies exactly the same birth–death mechanism and stationary distribution (Eq. 10) and discusses modality as parameters vary. The original formula is not claimed new. Its inspected Sections II/IV do not state the two-control sharp likelihood-ratio thresholds, nonmonotone relative-likelihood middle interval, or strict convex-order consequences. Mellor–Mobilia–Zia (2016) treat heterogeneous consultation classes with different state space, not this same S across two models. Priority remains qualified for generic monotone likelihood ratio comparative-statics theorems.

## value

PASS

The complete stationary polarization distribution, rather than its mean/mode alone, has a sharp and natural comparative-statics order under competing conformity and balanced commitment. The two noncoincident thresholds and intermediate neither-LR-order regime give a useful exact phase diagram for finite reversible opinion models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
