---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

On (0,∞)^2 with positive parameters and e>0, the printed F1=x[r/(1+s1y)−a(1+s2s1y/(1+s1y))−bx−(c+ey)y], F2=y[−n+ε(c+ey)x] has exact Dulac multiplier B=1/(xy). Independent symbolic differentiation confirms ∂x(BF1)+∂y(BF2)=εe−b/y, no omitted x-dependent terms. A nonconstant positive periodic trajectory is a simple closed curve and its Jordan interior remains in the positive quadrant (convex positivity); BF has zero outward flux along Γ. Green gives εe|D|=b∬_D y^(−1), hence harmonic mean b/(εe). A continuous strictly increasing divergence integrand with a sole zero y_H forces minΓ y<y_H<maxΓ y. At any positive equilibrium, substituting both equilibrium equations into the trace reduces it to xbar(εe ybar−b), independently verified symbolically. No finite simulation proves cycle existence; statement is necessary only.

## originality

PASS

The source model paper computes the same e=0 Dulac weight and the local e>0 Jacobian trace but does not state the e>0 enclosed-area harmonic-mean identity in the materially inspected full text. Green integration gives a finite-amplitude necessary invariant not equivalent to the local trace or no-cycle case. Other cooperative models use different vector fields, so the strong global identity is best-of-knowledge original for this exact model.

## value

PASS

The source explicitly exhibits finite-amplitude oscillations and possible stable/unstable cycles. The identity turns the sign-changing cooperative Dulac divergence into an exact cycle-wide geometric observable, locating *every* positive periodic orbit on both sides of the same parameter-only level at which local Hopf trace vanishes. This bridges local and global dynamics across amplitudes and potentially across distinct cycles; it is substantively motivated beyond a routine no-cycle sign test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
