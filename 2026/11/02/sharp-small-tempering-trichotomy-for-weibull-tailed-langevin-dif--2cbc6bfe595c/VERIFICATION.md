---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Scale density e^((1−2ℓ)V) and speed e^(−V) yield exact E_xτ0=∫_0^|x|H(y)e^(−2ℓV(y))dy, H=e^V∫_y^∞e^(−V), with supremum the full integral. Under V′~ηx^(η−1), V″/V′²→0, l’Hôpital gives H~1/(ηx^(η−1)). Regular-variation scaling u=2ℓx^η yields for η<2 gamma coefficient Γ(2/η−1)/η² times (2ℓ)^(1−2/η); critical η=2 logarithmic (1/4)log(1/ℓ); η>2 finite M0 and difference coefficient Γ(2/η)/[η(η−2)] times (2ℓ)^(1−2/η). Strict decreasing/convex follows integral differentiation. Infinite scale endpoints for ℓ≤1/2 give nonexplosion, uniformly bounded hitting time implies Doeblin minorization via 0 and positive compact heat kernels; when ℓ=0 and η≤2, nonuniform fixed-time return from x→∞ prevents uniform TV ergodicity. Independent exact Gaussian η=2 hypergeometric identity checks at ℓ=.01,.1,.3,.5. Numerics support the constants and normalization but not uniformity for all V.

## originality

PASS

Best-knowledge PASS, qualified: Mijatović–Xie 2026 motivating paper treats polynomial-tailed π and includes general tempering ideas, but its displayed hypotheses exclude these Weibull tails and do not compute the sharp three small-tempering constants. Pinsky/coming-down-from-infinity and general Cattiaux–Guillin provide Green/hitting criteria; the new sharp evaluated parameter-response trichotomy is additional (though may be derivable from a broader general Tauberian theorem).

## value

PASS

The critical exponent η=2 separates finite uniform entrance-time behavior from infinite at zero tempering, with a nonanalytic cusp for η>2. Exact constants quantify a natural parameter sensitivity not captured by general binary ergodicity criteria; useful to understand how weak tempering changes diffusion times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
