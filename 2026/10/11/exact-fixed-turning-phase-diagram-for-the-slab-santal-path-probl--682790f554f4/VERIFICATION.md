---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For p>=p_a=0.5 sqrt[a(1+a)^n], S_p(w)=sqrt(4p²+w(1-w)^n) remains real for -a<=w<=1. Differentiating the separated Hamilton–Jacobi generating function gives 4 Phi_t Phi_s=(1-ts)^n with admissible nonnegative partial derivatives, hence a calibration upper bound H_n(a)<=F_n(a,p). Under the integral sign, derivative Fp=2Psi; kernel (1-w)^n/[S_p(S_p+2p)] is strictly decreasing p, making Psi strictly increasing and F strictly convex. The source established Psi(a,p_a) sign transition at a_n: boundary p_a below, unique root p*>p_a above. At Psi=0 reflected characteristic contact coordinates match at (sqrt a,-sqrt a), yielding a calibrated attaining causal path. At a=1 any path goes through opposite corner via axis-parallel lines and H=0. As a->1, uniform large-p expansion Psi=log(1/a)-C_a/(8p²)+O(p^-4), C_a=(1+a)^(n+1)/(n+1), gives p*sqrt(1-a)->2^((n-2)/2)/sqrt(n+1), H/sqrt(1-a)->2^((n+2)/2)/sqrt(n+1). Independently computed adaptive quadrature/root of Psi for n=2,3,5 and a=.92,.93,.97, consistent with signs/asymptotic; numeric checks do not replace calibration proof.

## originality

PASS

The very recent original Artstein–Avidan arXiv:2609.38041v1 introduces the global slab Santaló variational setup and its Remark 6.5 qualitatively proposes varying momentum at fixed a. That qualitative direction is pre-existing; the audited new content is the evaluated scalar strictly convex phase, uniqueness and sharp boundary constants. Full source manuscript could not be retrieved during this execution; only arXiv abstract and source-equation excerpts in frozen RESULT/AUDIT were available. No Resultary search matched exact endpoint constants except this own record. Best-of-knowledge O PASS with substantial documented source-access priority risk, not a whole-text noncoverage assertion.

## value

PASS

Completes a clearly identified natural fixed-turning auxiliary variational problem left open in quantitative form by the sharp global inequality source. Unique momentum, attaining corner curve and endpoint square-root law are independent mathematically useful structural facts; no change to the global Santaló constant is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
