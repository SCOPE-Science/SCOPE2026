---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

At the pinned RESULT.md, L1=1+P_m p−P_n p and Fourier(P_b f)(k)=Fourier(f)(bk), so the claimed k≠0 equation is exact. For gcd(m,n)=1, extraction of maximal m- and n-powers gives unique r m^a n^b with m∤r,n∤r. Relations at r m^a n^b connect adjacent vertices of every fixed a+b=ell chain, proving identical coefficients; weighted Parseval handles L² and the independent [0,1] a.e. constraint handles positivity. A polynomial coefficient class survives iff its largest frequency r·max(m,n)^ell≤N, yielding exactly 1+2 sum_r(1+floor(log_max(N/r))) real dimensions; p=1/2 is a relative-interior witness. For any stationary L¹ density f, strictly convex integrable phi(t)=sqrt(1+t²), unitality L1=1, and equality of integrals force equality in each positive weighted inverse-branch Jensen inequality, hence f=f∘T_m a.e. Ergodicity of T_m forces f=1. The fixed point 0 yields singular delta_0, so no unrestricted uniqueness is claimed. These are infinite arguments, not extrapolations from finite checks.

## originality

PASS

Best-of-knowledge PASS for the *complete* inverse-policy Fourier classes and all-cutoff real dimension, not novelty of the standard Perron–Frobenius identity or Jensen ergodicity. Fresh Resultary searches and full published RESULT.md comparisons separated fixed iid switching statistics from state-dependent policies. Primary sources materially inspected (Suzuki 2023 PDF; Bahsoun–Bose–Quas 2008 full text) treat stationary densities for exogenous switches or a given policy and do not imply this all-policy arithmetic dimension formula. Important papers by Góra–Boyarsky (2003) and Alshekhi–Ding–Rhee (2024) were abstract-only because full text inaccessible; priority risk explicitly retained; no absent theorem is asserted in unseen text.

## value

PASS

The natural invariant-law inverse-design problem asks for every measurable state-dependent switch probability preserving the uniform law of two expanding maps. Giving all frequency-level degrees of freedom, the exact dimension of every trigonometric degree cutoff, an explicit nonconstant robust interior family, and a precise absolutely-continuous uniqueness/singular counterexample dichotomy is a motivated complete structural classification, not an arbitrary small computation. The number of freely selectable parameters is directly useful for calibrated feedback design. The transfer identity and Jensen argument are standard ingredients and do not independently confer value; the complete all-policy/all-cutoff classification is the substantive exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
