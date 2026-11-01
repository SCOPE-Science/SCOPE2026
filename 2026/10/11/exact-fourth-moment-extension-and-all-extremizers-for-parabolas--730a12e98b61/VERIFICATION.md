---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For q=p^k with odd p, two-dimensional character orthogonality gives Σ|E_qf|^4=q^{-2}Σ_{s,t}|F(s,t)|², and division by (S/q)² reduces the quotient to Σ|F|²/S². Fiberwise Cauchy then gives B=Σ_{x,y} w(x−y)μ_xμ_y, with w=2p^r for 2r<k and w=p^{floor(k/2)} otherwise; the congruence z²=z0² has exactly the claimed roots for odd p. Even k=2m: all weights are ≤p^m, strict outside one coset modulo p^m, so equality forces a single coset; equality of all fiber products then forces full support and an additive character on its affine graph. Odd k=2m+1,m>=1: parent and daughter masses satisfy B≤2p^{m-1}(1−ΣU²)+p^mΣ(2U²−ΣV²)≤(2−1/p)p^m, with strict equality requiring one parent of mass one and equal masses in its p daughters. Fiberwise product constancy forces a common additive character on the fine digits and arbitrary unimodular daughter phases. At k=1, all off-diagonal root multiplicities equal two and diagonal multiplicity one, giving B≤2−1/p with equality for constant modulus. Direct independent reconstruction enumerated every pair fiber and exact coset-indicator quotient in q=3,9,27,81,243,25,125,49; five further complex phase-family witnesses at p=3,k=2..5 and p=5,k=3 matched sharp constants to numerical tolerance. The finite checks corroborate the source analytic proof and do not establish the infinite theorem alone. No characteristic-two or mixed-modulus conclusion is asserted.

## originality

PASS

Best-of-knowledge PASS for the genuinely unrestricted odd-prime-power depth classification. The all-k exact norm and necessary-and-sufficient phase structure survive comparison with published prime-square and prime-cube cases: those fully imply k=2 and k=3 specializations and are not claimed as new. Hickman–Wright addresses ring restriction exponent ranges and uniform estimates, González-Riquelme–Oliveira e Silva sharp finite-field endpoints in different ambient dimensions/exponents, and Kingsbury-Neuschotz squarefree moduli; none of the inspected claims implies every k>=4 together with all equality cases. The general p-adic wave-packet/fiber idea is established prior methodology; exact all-depth sharpness and rigidity are the surviving contribution. The identically titled public copy of the assigned package is the same result, not independent priority evidence. Possible historical equivalent results under p-adic Strichartz terminology remain a disclosed risk.

## value

PASS

The sharp L2-to-L4 norm and all complex equality cases are natural invariants of Fourier extension on cyclic local rings. The first two nilpotent depths have published exact theorems, but a complete arbitrary-depth classification was not established by them; the present all-k formula exposes a genuine even/odd valuation transition and the exact coset/character and daughter-phase geometry. Higher depth k>=4 is a motivated structural extension rather than an arbitrary small instance or numerical table; it supplies sharp test functions for ring restriction questions. This assessment does not claim quantitative stability, other moments, even-characteristic rings, mixed moduli, or a general Fourier restriction theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
