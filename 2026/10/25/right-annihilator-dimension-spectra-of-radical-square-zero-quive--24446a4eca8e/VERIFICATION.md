---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS. Direct path multiplication (ab)_v=λ_v μ_v, (ab)_e=λ_tail(e) y_e+x_e μ_head(e) is valid with loops and parallel arrows. For S of zero λ, each arrow from tail outside S determines y_e, each arrow from S leaves y_e free; each μ_v for v∈S remains free iff all x_e with tail∈S,head v vanish. Thus d(a)=m_S+number of eligible v∈S, and disjoint coefficient groups by head give factors (q^{r_S(v)}−1+t) or q^{r_S(v)}. Summation over λ,x proves spectrum for any prime power. Evaluating t=q counts zero-product ordered pairs. Independent height-two zero-product equations give q^m Σ_S q^{|S|+e(S)}(q−1)^{v−|S|}; star/path polynomial subtraction q^6(q−1)^3 and opposite-star difference follow. Finite rank checks supplement, not replace, this proof.

## originality

PASS

PASS best of knowledge. Dolžan 2022 introduces finite-ring zero-product/nullity probability and Dolžan 2025 generic identity P(0)=|A|^{-2}Σ_a |Ann_r(a)|. These are established and explicitly credited; they do not specify all quiver coefficient strata in inspected material. Incidence monoid work and familiar lattice-gas subset graph polynomial are not claimed newly invented. Full Dolžan 2022 article inaccessible, so possible broader formula remains a residual risk; no all-quiver distribution found in Resultary queries.

## value

PASS

PASS. Right-annihilator dimensions are intrinsic algebraic invariants that control zero-product counts but retain strictly more orientation information; the formula evaluates every dimension stratum for all finite fields/quivers, including loops, without enumerating q^(n+m) elements. Explicit orientation-reversing and star/path boundaries demonstrate mathematically meaningful discrimination beyond ring dimension and radical size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
