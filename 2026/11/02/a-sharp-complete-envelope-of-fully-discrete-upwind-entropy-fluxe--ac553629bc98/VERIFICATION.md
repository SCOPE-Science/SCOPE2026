---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For periodic N>=3 upwind forward Euler v_i=(1-nu)u_i+nu u_{i-1} and consistent shared H(a,a)=U(a)=a^2/2, choose neighboring states (left,center,right)=(a,a,b) to force H(a,b)<=U(a), and (a,b,b) to force H(a,b)>=U(a)-(1-nu)(a-b)^2/2. At nu>1 these inequalities contradict each other for any a!=b. For 0<nu<=1 let J=U-H; the pointwise envelope is exactly 0<=J(a,b)<=(1-nu)(a-b)^2/2. Direct identity for any neighboring triple gives cell dissipation nu[(1-nu)(a-left)^2/2 +J(a,right)-J(left,a)]>=0, proving necessity and sufficiency without smoothness of H or bounded-state assumptions. Consistent quadratic polynomial H are exactly U(a)-k(a-b)^2 with 0<=k<=(1-nu)/2. Substituting the source half-cell bounds yields k<=1/2-nu, strictly narrower and void for nonconstant interfaces when nu>1/2. Independent rational counterexamples/witnesses check bounds; finite checks are not the universal proof.

## originality

PASS

Best-of-knowledge PASS subject to particularly significant coverage risk: the motivating 2026 source supplies a sufficient half-cell inequality, not an advertised complete classification in material accessible here. It was not possible to inspect its full text; therefore no whole-paper noncoverage is asserted. Classical entropy-flux theory may contain an equivalent necessary-and-sufficient specialization.

## value

PASS

The complete exact necessary-and-sufficient interval for every consistent shared 2-point entropy flux, including nonsmooth functions, identifies a genuine conservatism and empty-but-feasible regime in a natural numerical entropy stability construction. The classification is useful in designing/validating entropy-flux limiters despite its deliberately simple scalar model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
