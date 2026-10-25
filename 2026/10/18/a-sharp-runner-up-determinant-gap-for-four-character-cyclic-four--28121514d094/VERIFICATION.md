---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For N=4m≥8 and four consecutive Fourier rows E={0,1,2,3}, the determinant is the Vandermonde six-chord product 64 sin(αa)sin(αb)sin(αc)sin(αd)sin(α(a+b))sin(α(b+c)), α=π/N. The gap change p=(a+c)/2,u=(a−c)/2,v=(b−d)/2 gives exactly D=64(T−X)(1−T−Y)(1−X−Y) with T=sin²(αp), X=sin²(αu), Y=sin²(αv). Positive integer gaps have either all integral p,u,v or all half-integral: no third parity class. For u=v=0 in the integral branch nonsquares bound by 16cos²(2α); all other integral cases use X+Y≥sin²α and AM–GM to bound by 16cos^6α, below 16cosαcos2α for 0<α≤π/8. In the half-integral branch |u|,|v|≥1/2 and strict factor monotonicity force X=Y=sin²(α/2); grid quantization forces p=m±1/2 and the bound 16cosαcos2α. Equality gap tuples arise by moving one square node one grid step; m≥2 gives uniqueness of source square and exactly 2N distinct sets. A separately coded finite enumeration computed exact gap sine products for all four-subsets N=8,12,16,20,24,28 and reproduced 2N runner-up ties each N; this is finite corroboration and does not replace the all-N trigonometric proof. The frozen package code implements a separate complex chord-length check (not executed as an opaque verifier).

## originality

PASS

Best-of-knowledge PASS: the exact maximum 16 and all square translates were already established by the published general four-row optimum theorem; likewise continuous-circle four-point Fekete squares and Fourier determinant tightness are established. The claim is the sharp second-best determinant upon excluding every optimum, a strict loss and complete equality multiplicity 2N for all N divisible by four. The prior theorem does not impose exclusion of maximizers and does not determine this runner-up layer.

## value

PASS

Second-best Fourier sampling determinant supplies a stability gap quantifying the volume cost of one-grid-step perturbation away from orthogonal four-node sampling, together with exact near-extremizer geometry and O(N^-2) loss. This is a natural discrete-Fekete extremal refinement, not an arbitrary small parameter value or restatement of the first optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
