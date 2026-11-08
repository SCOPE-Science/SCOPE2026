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

Congruence transforms B^T diag(p)B>=gamma I to diag(p)>=gamma (BB^T)^-1. Therefore maximize gamma by minimum-trace diagonal PSD majorant of C; its standard elliptope dual has diag X=1. In the weak branch, the proposed slack quadratic form is an explicit sum of nonnegative squares and its all-ones kernel gives a matching rank-one dual. In the strong branch, slack/w=t vv^T+(1+1/t)L_complete, with v=e_1+e_n-t^-1 sum interiors; matching rank-two correlation X=aa^T+(1-r²)ff^T yields equality. Complementary slackness forces each q uniquely even allowing nonsymmetric competitors; rank of factors proves nullity and t=m/2 boundary. An implicit-function argument starting at C=I establishes feasible unit-row systems for sufficiently small w at every t. Independently checked rational PSD/dual/rank certificates in 64 cases; finite coverage does not replace the symbolic factorization.

## originality

PASS

Dai–Soltanalian–Pelckmans establish the general diagonal-majorant SDP, which is prior. The claim evaluates it explicitly for a dense signed complete graph with exactly one negative edge, including unique optimizer, rational strong branch and sharp nullity transition, which were not found in inspected relevant sources. The published inverse-positive-coordinate model assumes nonnegative inverse and is not applicable to negative signed triangles. O=PASS qualified by partially inaccessible 2014 exact-MSE article and possible spin/elliptope literature.

## value

PASS

A dense interaction network with one antagonistic coupling is a natural robustness model. The optimizer undergoes a genuine sign-induced structural transition and has explicit probabilities and spectral rate throughout an infinite dimension family, removing a generic semidefinite optimization for this class. The one-step objective is explicitly bounded and avoids unsupported multistep claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
