---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For a smooth homogeneous degree d>1 GAS field, a C² positive-Hessian Lyapunov L has leading gradient λHz along rays and gives zᵀHf(z)≤0. Conversely a positive definite weak quadratic Q plus an existing smooth proper strict GAS converse Lyapunov W is smooth, proper, strict and has positive Hessian; the converse theorem is explicitly assumed. For the cubic family the quartic W=(x⁴+y⁴)/4 has derivative −x⁶−y⁶<0 for all κ, proving GAS. C4 equivariance averages an arbitrary admissible H to a positive scalar I. The exact identity (x⁴+y⁴)²−8x²y²(y²−x²)²=(x⁴−4x²y²+y⁴)² shows the sharp radial ratio 1/(2sqrt(2)); extremal rays attain it. Hence |κ|≤2sqrt(2) precisely, including endpoint via x²+y²+εW; outside no local even weak C² Morse certificate. I independently checked the polynomial and rotational identities symbolically; no unverified numerical inference supplies the universal necessity.

## originality

PASS

Jongeneel 2026 establishes hyperbolic Morse sufficiency and linear semisimplicity necessity, including non-Morse examples, not the global-if-and-only-if for homogeneous GAS fields or this sharp explicit C4 family. Liu–Fitzsimmons give a distinct cubic GAS field lacking any homogeneous polynomial/analytic Lyapunov certificate, whereas this family always has a quartic polynomial certificate and changes only Morse regularity at |κ|=2sqrt(2). The polynomial and matrix averaging ingredients are conventional; the combined sharp all-parameter certificate existence law was not directly implied by examined sources.

## value

PASS

The homogeneous criterion converts a smooth-function existence problem into a concrete weak quadratic feasibility test; the planar family has a sharp Morse-certificate transition while global stability and a strict quartic certificate remain unchanged. This separates certificate regularity from dynamical bifurcation and addresses a nonhyperbolic case the motivating prior work leaves open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
