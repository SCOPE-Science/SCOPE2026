---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the exact scalar annulus

The proof is symbolic and applies to *all* bounded operators on nonzero complex Banach spaces; no script, numeric experiment, or unavailable external certificate is required.

1. Directly inspect the uniform quantifier in [1, Definition 3.3]: at one common time \(N\), the continuous function \(x\mapsto\|T^Nx\|\) maps the connected unit sphere into \([0,1/2)\cup(2,\infty)\); its image must lie in exactly one component. This establishes the global-power dichotomy without assuming a spectral splitting.
2. Check \(\|AB\|\le\|A\|\|B\|\), \(m(AB)\ge m(A)m(B)\), and \(m(T^n)\le\|T\|^{n-1}m(T)\) (the last uses \(T^n=T^{n-1}T\)). These yield the two uniform asymptotics and handle \(m(T)=0\).
3. Check the usual spectral-radius formula and the superadditive-limit formula for \(\log m(T^n)\) when \(m(T)>0\). Multiplication by \(c\) scales both radii by \(|c|\), establishing exactly the strict parameter thresholds.
4. Boundary stress-test: \(T=\operatorname{diag}(1/2,2)\) gives excluded \(1/2\le|c|\le2\). For \(T=2S\) with \(S\) the unilateral Hilbert-space isometry, \(\|T^n x\|=2^n\|x\|\) exactly, so \(cT\) qualifies iff \(|c|\ne1/2\); at the boundary it is an isometry. This also rules out identifying lower growth radius with the minimum spectral modulus.

Limits: the checked theorem does not assert results about other expansivity definitions, describe nonlinear dynamics, or provide independent peer validation. The supporting 2016 comparison was inspected at its Introduction, Section 2, Definitions 1–2, and Proposition 5; the 2026 source was examined at its definition, core claims, shift examples, proof, and scalar proposition.
