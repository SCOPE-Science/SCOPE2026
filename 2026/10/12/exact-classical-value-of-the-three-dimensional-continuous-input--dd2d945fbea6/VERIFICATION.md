---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For arbitrary measurable a,b:S^2 -> {±1}, the classical bias is B=-∬sgn(x·y)a(x)b(y), optimized in b to ∫|h_a(y)|. Independently verified the oddness h_a(-y)=-h_a(y), and spherical-lune measure gives sharp geodesic Lipschitz 2/π. For any odd L-Lipschitz function, antipodal superlevel sets A_t and -A_t are 2t/L-separated. Lévy isoperimetry for cap metric neighborhoods implies σ(|h|>t)≤1−sin(t/L) for 0≤t≤Lπ/2; integration gives ∫|h|≤L(π/2−1). At L=2/π this yields maximum bias 1−2/π, reached exactly by opposite hemispherical responses. Therefore P_cl=1−1/π; uniform dot product and singlet correlation give P_singlet=3/4 and positive gap 1/π−1/4. No assumption of antipodal response functions was used. Sympy verified exact integral and gap, separate from source verifier Monte Carlo. This proves classical optimality but not globally optimal quantum value.

## originality

PASS

At claim/implication level, no inspected prior source states or entails the precise final result; closest frameworks, partial results and source gaps are explicitly distinguished. No failed search is treated as proof of absolute priority.

## value

PASS

The original continuous-input nonlocal-game paper calculates hemispherical performance but leaves its global classical optimality and exact quantum advantage conjectural. A sharp infinite-dimensional geometric optimization over all measurable local responses resolves that natural missing comparison with an exact constant and rigorous quantum/classical separation. The spherical-isoperimetric bound is independently motivated, not a finite numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
