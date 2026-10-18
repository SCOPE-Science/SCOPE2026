---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For real Day–James norm Euclidean on st≥0 and ℓ1 on st<0, normalized unit x ranges over same-sign Euclidean arcs, opposite-sign taxicab facets and four nonsmooth axes. At Euclidean x=(c,s), c²+s²=1, 0<s≤c, its unique BJ partner y=(−s,c)/(s+c), and ||x+y||²=1+1/(s+c)²≥3/2 with equality only c=s. At taxicab x=(.5+u,−.5+u), 0≤u<.5, partner y=(1/√2,1/√2), giving ||x+y||²=3/2+2√2u+2u²≥3/2, equality only u=0. At axis x=(1,0), norming-functional segment fτ=(1,−τ), 0≤τ≤1, y=(τ,1)/√(1+τ²) and ||x+y||²=2+2τ/√(1+τ²)≥2. All symmetry images exhausted; the balanced pair has both symmetric chord norms sqrt(3/2) and is BJ orthogonal in both orders. Thus the complete equality classification and exact infimum follow.

## originality

PASS

PASS with bounded caveat: Baronti–Papini 2022 Example5.4 already gives classical g=sqrt(3/2), while computing only J_perp≈1.626 for this mixed Euclidean/taxicab norm. Their adjacent examples compute g_perp expressly, but this same-object Example5.4 omits it and does not classify Birkhoff-constrained minimizing ordered pairs. General inequality g≤g_perp and one balanced orthogonal pair make the NUMBER easy, but do not classify all minimizers. The assessed final result includes that natural complete classification and comparison g_perp=g though J_perp<J. Searches find same-object nearby records on other parameters or ℓ3−ℓ1, not a covering ℓ2−ℓ1 g_perp equality classification.

## value

PASS

The exact constraint-minimizer classification completes a canonical counterexample in the defining orthogonal-constant paper and explains why the two orthogonality restrictions behave differently. The mere numerical equality follows cheaply from classical g and one witness; value rests primarily on exhaustiveness of all BJ minimizers across smooth arcs and nonsmooth axes, not on falsely claiming new classical g.

The dated certificate retains the supplied scientific assessment, sources and limitations.
