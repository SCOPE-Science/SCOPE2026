---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Orthogonality and the squared norms (n+1)^σ/2 give the reciprocal weights and factor two; polynomial coefficient growth ensures continuous interior evaluations. The moment measure in the proof is a probability with moments (n+1)^(−σ) for σ>0, so the positive Poisson kernels give strict positivity, also directly at σ=0. DLMF 25.12.12 applies to every negative order. For w=1−z, write −log(1−w)=w A(w) with A analytic, A(0)=1, A′(0)=1/2. On the right-half sector the principal factorization gives Li_σ(z)/z=Γ(μ)w^(−μ)B(w)+C(w), where B and C are analytic at zero, B(0)=1 and B′(0)=1−μ/2. Thus the scaled real part has uniform C¹ angular remainder O(ρ²+ρ^μ), including at the sector endpoints (an angular derivative on an analytic factor is iw times its derivative). The leading cosine takes both signs at fixed admissible angles for every μ>1. Away from odd μ≥3, all leading zeros are simple and separated from the two endpoints; monotonicity on small neighborhoods and a compact nonzero gap on the complement prove exact root exhaustion inside |θ|<arccos(ρ/2). The derivative remains nonzero and the analytic implicit function theorem applies for ρ>0. The mean value theorem first gives shift O(ρ), then dividing the root equation by ρ gives the stated coefficient, using cos((μ−1)θ_j)=sin(μθ_j)sin θ_j. Conjugation doubles the count. No census is required at the grazing orders; realizability of all disk z makes the sign result an assertion about the actual kernel.

## originality

PASS

The distinct contribution supported by the comparison is the complete order-dependent boundary-local nodal census together with its first angle correction for the specified shifted harmonic kernel. The kernel construction, moment mixture and local polylogarithm expansion are not credited as original. The sign threshold by itself also admits a standard positive-real-part coefficient argument. Available closest texts did not show equivalent coverage of the complete nodal result; limits of access are explicit below.

## value

PASS

For a natural harmonic Sobolev scale, the census identifies where and how new boundary-local nodal branches appear as regularity changes. It establishes exhaustion and branch nonsingularity, not just example sign changes or a heuristic count from asymptotic rays. The first correction quantifies the geometry of each branch in the actual disk coordinate, and the theorem identifies the parameters where that stable analysis has a boundary-ray obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
