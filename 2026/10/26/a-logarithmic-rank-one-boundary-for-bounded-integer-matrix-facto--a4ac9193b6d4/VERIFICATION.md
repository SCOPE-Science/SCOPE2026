---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For w the first column of B, Aw=e_1 forces w primitive. The two families 'second column of B zero' and 'second row of A zero' cover all solutions: any nonzero second column lies in ker A, so rank A=1 and im A=span(e_1). Transposition and factor reversal exchange the families without changing E_11 or the box. The first has size S=Σ_w U_T(w)R_T(w); the overlap has size C=Σ_w U_T(w). In the Bézout fiber, centers of the two parameter intervals are separated by 1/|uv| when uv≠0, so their intersection has length 2T/h+O(1) uniformly, and rounding changes the count by O(1). Axis vectors have h=1 and satisfy the same bound directly. For the zero fiber R_T=2 floor(T/h)+1. Thus S=32T² Σ_{h≤T}φ(h)/h²+O(T²), since the shell is exactly 8φ(h), also at h=1, and the sum of O(T/h+1) shellwise errors over primitive vectors is O(T²). Möbius inversion gives Σφ(h)/h²=log(T)/ζ(2)+O(1) and C=O(T²). Inclusion–exclusion yields 2S−C=(384/π²)T² log T+O(T²) with absolute error constant. Independent exhaustive products give 100, 404, 996 at T=1,2,3; replay: python /workspace/reproductions/2/independent_direct_count.py. This only corroborates finite counts. Frozen VERIFICATION.md and verify.py were inspected, not executed; the asymptotic is established analytically.

## originality

PASS

The exact count is the same ordered height-capped divisor function studied by the closest primary sources, but their nonzero-singular estimates do not determine the logarithm, constant, or remainder for the primitive 2×2 rank-one target. No equivalent asymptotic was identified in the sources compared.

## value

PASS

E_11 is the canonical primitive rank-one test target in the first nontrivial matrix size, where the existing divisor-function lower bound and upper bounds leave the scale open. The exact logarithm and leading constant distinguish this singular fiber from both the unimodular and zero fibers and provide a concrete benchmark for future nonzero-singular counts. The gain is an entire scale and leading term, not a minor improvement to an already known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
