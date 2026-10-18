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

Fix L>0, ε>0. The source axial volume Gini constant equals 246/875, and normalized boundary masses satisfy α=a/D>0, β=b/(2D), γ=ε/(3D)=α/(3S), S=sqrt(L²+1)>1. Hence β=1−α(1+1/(3S)), α<3S/(2S+1)<3/2. Substitution in g=α+(2/3)β−(2/3)α²−αβ−(2/5)β² yields g−4/15=α[6S²+2S−α(3S²−3S+2)]/(45S²). The bracket is strictly > (3S²+13S−6)/2>0. As ε→0, α→0, β→1 so g→4/15 and transverse penalty 2sqrt(1+ε²)/L→2/L, giving unattained inf_U=4/15+2/L. Exact rational difference 246/875−4/15=38/2625 means the projection-diameter proof works for some positive ε iff L>2/(38/2625)=2625/19. For L at/below threshold no ε satisfies these TWO inequalities, not an impossibility theorem for the true geometric distance sign. Independent rational-symbolic checker reconfirmed the polynomial identity, positivity reduction and threshold. Presentation caution: assigned RESULT.md has literal doubled backslashes in mathematical command strings (e.g. before varepsilon, Delta, frac); proof was interpreted after decoding its intended formula, and source rendering requires authorized fix before publication.

## originality

PASS

Compared the exact final theorem and quantifiers against all materially relevant inspected same-object and related published statements. Actual source readings and residual priority risks below; no negative search is treated as novelty proof.

## value

PASS

A finite SHARP stretch threshold for the established elementary mean-distance certificate of a natural six-vertex convex-body counterexample is a meaningful exact boundary. It replaces an ad hoc numerical stretch L=1000 by the complete iff L>2625/19 range for that proof mechanism; does not pretend to find the true least geometric stretch or solve the unrestricted mean-distance conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
