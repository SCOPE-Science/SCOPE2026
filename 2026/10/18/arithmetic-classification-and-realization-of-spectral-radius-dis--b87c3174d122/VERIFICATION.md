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

For W_α on C(T), W_(p/q)^q is multiplication by exp(qG_q), so log spectral radius equals max G_q; root-of-unity filtering gives G_q=sum_j ĝ(jq)e^{ijqθ}, with mean m. Strict max>m exactly when some positive Fourier mode divisible by q is nonzero. For irrational α, uniform unique ergodicity via uniform trig polynomial approximation gives log r=m. Analytic Fourier decay |ĝ(k)|<=Mρ exp(-ρ|k|) yields jump <=2Mρ e^{-ρq}/(1-e^{-ρq}), ensuring continuity at all irrationals, and the rational spike criterion; denominators are divisor-downward closed. Conversely any divisor ideal D has entire g_D=2η sum_{k∈D}e^{-k²}cos kθ, and positive-coefficient Fourier maximum occurs θ=0: exact rational log spike 2η sum_{ℓq∈D}e^{-(ℓq)²}, positive precisely q∈D; its first term has relative O(e^{-3q²}), while ||e^g-1||∞->0 as η->0. D empty, q=1, and infinitely many D all covered. Independent finite D={1,2,3,6} Fourier checks confirm allowed spike denominators; not a proof of general arbitrary sets.

## originality

PASS

Best-of-knowledge originality is for the precisely new contribution, excluding acknowledged prior-covered premises/corollaries. The four structured implication comparisons and genuine source inspections support noncoverage within a bounded search, not an absolute proof of novelty.

## value

PASS

Classifies exactly which rational rotation parameters are discontinuities for one positive analytic weighted composition family and gives an inverse construction realizing every permitted arithmetic ideal, even with arbitrarily small entire weight perturbation. It connects Fourier sparsity, unique ergodicity, spectral radius and instability of operator spectrum—an explicit natural structural dichotomy with sharp exponential bounds, beyond a routine restatement of fixed-operator variational principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
