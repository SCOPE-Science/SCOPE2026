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

For all N≥3, a∈Z and t>0, g(j)=ω^{aj²}+tδ_0 has directly expanded ambiguity A_g(u,v): diagonal N+t(t+2), zero-lag offdiagonal t(t+2), chirp line (N+2t)ω^{au²}, and off-line tω^{au²}(1+ω^{u(v−2au)}). Weyl-basis Fourier diagonalization makes lifted N²×N² singular values √N|A_g|. For odd N no roots of unity equal −1; minimum is 2√Nt sin(π/(2N)), maximum √N(N+2t+t²). The exact condition number is minimized uniquely at t=√N via N/t+t≥2√N. For even N zeros solve u(v−2au)=N/2 mod N; grouping by d=gcd(u,N) gives Σ_{d|N/2}dφ(N/d), the stated factorized nullity. The least positive singular value is 2√Nt sin(π/N), N even≥4. Independently reconstructed direct complex sums and divisor nullities for orders 3..19 with several a,t, not as a substitute for the symbolic proof. Even nullity concerns LINEAR lifting only, not impossibility of nonlinear phase retrieval.

## originality

PASS

Bojarovska–Flinth 2015 Theorems 2.2–2.3 establish the general nonvanishing-ambiguity phase-retrieval criterion and generic exact frame bounds, so these portions are prior tools, not new. Casazza–Fickus 2006 treats finite chirp Fourier transforms without the real single-impulse arithmetic lifting nullity and optimal conditioning family found here. Resultary Gabor findings on constant-plus-complex-one-site, two holes and quadratic exponential windows treat different seeds/constraints; prime dimension general complex-impulse results may overlap special a=0 prime cases but do not determine full all-N arithmetic nullity. Li 2026 provides stronger general window constructions with better margins, but not the stated family-specific full spectrum in accessible abstract; full text uninspected.

## value

PASS

Exact all-N singular spectrum and totient kernel dimension of a natural chirp-plus-one-spike experiment is a useful design/obstruction fact for finite Gabor tomography. It identifies a sharp odd/even arithmetic change and the unique optimal impulse within a precisely scoped physically motivated one-parameter seed, without unsupported global-optimum claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
