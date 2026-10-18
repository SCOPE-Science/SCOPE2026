---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For Ω=Δ^k×B^m, k,m≥1, d=k+m, the balanced Minkowski functional is max(‖z‖∞,‖w‖2). Restricting every origin-preserving holomorphic Ω→B^d map to complex lines gives derivative contraction A. Writing A=[u1…uk B], exact independent-unit-phase averaging of the squared Euclidean norm of ∑ε_j u_j+η Bv (unit v∈C^m) yields ∑‖u_j‖²+‖Bv‖²≤1, hence ‖B‖op²≤1−s. Hadamard and AM-GM prove |det A|²≤(s/k)^k(1−s)^m with unique maximizer s=k/(k+m) and value m^m/(k+m)^(k+m). The explicit diagonal linear map L(z,w)=(z,√m w)/√(k+m) is a valid strict map and attains equality. Since B^d⊂Ω⊂Δ^d, Kobayashi–Eisenman monotonicity and the normalized endpoint values both 1 imply kΩ(0)=1. Independently checked k=m=1→1/4 and k=1,m=2→4/27, and exact asymptotics e^(−k)m^(−k) for fixed k. All quantifiers and endpoint domain cases are as stated.

## originality

PASS

Read the complete full-text primary localization paper by Jaiswal–Kar (arXiv:2606.01773), including its product model and exact k_{Δ×B^n}(0)=1 plus pure-polydisc q=d^{-d}. It does not state or imply an exact mixed-product c/q determinant optimum; product inclusions alone bound k but not c. General convex-domain estimates of Kar 2024 do not provide the sharp parameterized mixed-product formula in the material checked. Resultary searches exposed the current claim and unrelated volume/model constants, no dominating exact q formula. Acceptance remains best-of-knowledge with older invariant-volume literature risk.

## value

PASS

The mixed polydisc–ball is the precise scaling model used in contemporary Eisenman localization. Its exact Carathéodory quotient is a natural invariant missing from the source model analysis; the formula gives all k,m and sharp asymptotics, not just a restatement of known K factor. Although finite-dimensional determinant inequalities yield an elementary proof, the independently useful exact benchmark is motivated and not a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
