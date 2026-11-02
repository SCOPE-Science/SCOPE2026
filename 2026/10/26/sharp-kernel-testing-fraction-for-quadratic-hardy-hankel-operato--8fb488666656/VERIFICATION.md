---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For H_{bar psi} with psi(z)=az+bz² and a,b complex, the Hankel matrix on span{1,z} is [[bar a,bar b],[bar b,0]], giving ||H||=(|a|+sqrt(|a|²+4|b|²))/2. Direct Szego-kernel action gives K(H)²=max_{0<=r<=1}(1-r²)((|a|+|b|r)²+|b|²) with angular alignment. For both coefficients nonzero set t=|a|/|b| and x=(t+sqrt(t²+4))/2; radial derivative t-t²r-3tr²-2r³ is strictly decreasing and has exactly one interior zero. Differentiating the optimized squared ratio yields two branches s=t+r=x or 1/x. Substituting into the radial equation excludes s=x and forces x²=3/2, t=r=1/sqrt6 on s=1/x. Since ratio tends to 1 as t->0 and t->infty, the unique stationary point is global minimum squared 25/27, i.e. 5/(3sqrt3); monomial cases have ratio 1. Equality phases follow triangle equality. Independent symbolic check verified both branch factorizations; numerical one-dimensional search and 301-point logarithmic grid corroborated norm ratio about 0.96225044865, not a continuum proof.

## originality

PASS

Qualitative strict inequality for the SAME quadratic family is already known in Dyakonov 2026, and finite-rank SRKT equality is classified in a published stronger qualitative theorem. The newly assessed piece is the global quantitative minimum 5/(3sqrt3) and its unique magnitude and phase equality conditions. Dyakonov full text and the archival Bonsall source were not independently accessible in this run; only material actually read is characterized as such.

## value

PASS

The first nonmonomial polynomial Hankel family is explicitly natural in the reproducing-kernel-thesis literature. A known qualitative strict inequality does not reveal how badly kernels underestimate norm. The sharp global fraction and full coefficient/kernel extremizer classification provide an exact quantitative diagnostic benchmark for finite-rank Hankel kernels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
