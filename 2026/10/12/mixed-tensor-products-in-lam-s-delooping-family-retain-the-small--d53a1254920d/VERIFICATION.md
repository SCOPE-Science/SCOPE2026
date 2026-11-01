---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The package defines A_r as a radical-square-zero quiver algebra with loop at 1 and endpoint T_r, and makes the bound for every m,n≥2. Lam’s Ext profile (degrees 1,r), combined with the tensor Künneth spectral-free decomposition, yields possible degrees 2,m+1,n+1,m+n; hence Ext_R^j(S,R)=0 for 3≤j≤q with q=min(m,n). Dimension shifting gives left projective approximation inclusions at j=3,…,q and Σ^{q+1}Ω^qS≅Σ³Ω²S. The crucial local three-approximation support inclusion W={(1,1),(1,2),(2,1),(2,2)} was independently modeled via actual quiver module matrices and Hom maps for both equal and unequal low parameters, supporting the tail-independence argument. V={i≤m+1,j≤n+1} is successor-closed. In the minimal total tensor resolution the (0,q) component has a unique degree-q carrier of v=(m+2,q+1) and nonzero vertical differential, so Ω^qS has a nonprojective summand outside V. Such a summand cannot stably retract into Ω^{q+1}Σ³Ω²S, contradicting the Gélinas criterion for dell_R(S)≤q. For q=2 the Ext-vanishing interval is vacuous, and the local calculation still applies; m=n is the source diagonal case. The result is a lower bound, not an exact delooping value.

## originality

PASS

Best-of-knowledge new two-parameter ordinary-delooping lower bound. Lam establishes the same obstruction for diagonal self-tensors A_r⊗A_r, but a diagonal statement does not imply the rectangular one for A_m⊗A_n; Guo’s related general results involve the derived invariant with finite-global-dimension hypotheses violated here. The new argument checks mixed Ext-degree vanishing and endpoint support for unequal factors; it does not merely rename a parameter. No covering same-invariant rectangular statement was found, but searches alone do not prove priority.

## value

PASS

Ordinary delooping under tensor products is a natural homological invariant problem; Lam established its sharp qualitative nonadditivity only in self-tensor examples. The mixed result separates the two factors and controls the obstruction by min(m,n), producing unbounded defects along genuinely nonisomorphic rectangular pairs (r,2r). Its proof needs mixed projective resolution and support analysis, so the precise all-parameter lower bound is a motivated structural extension rather than an arbitrary substitution or isolated computation. Value is incremental and focused; it neither establishes an exact level nor introduces a new delooping method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
