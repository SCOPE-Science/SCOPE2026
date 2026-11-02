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

For positive weights the norming-functional formula and triangle inequality give exactly the finite-simplex maximum Phi_epsilon(u)=sum_j(1+epsilon*h_j)u_j^alpha*u_(j+1)^beta, alpha=(p-1)/p, beta=1/p; nonnegative real x realizes equality over both real and complex fields. Weighted Young/AM-GM shows Phi_0<=1 with equality iff all u_j equal, including n=2 with two parallel directed edges. Compactness localizes every perturbed global maximizer in an interior neighborhood. The simplex-tangent Hessian at u*=1/n is -n*alpha*beta*L, negative definite because connected L has kernel constants. Analytic implicit function plus uniqueness of near critical point establishes a unique positive analytic maximizing mass branch for sufficiently small epsilon. Its first displacement solves n*alpha*beta*L xi=b^circ, b_j=alpha*h_j+beta*h_(j-1). Maximizing the second-order Taylor functional gives <b^circ,L+ b^circ>/(2n alpha beta). The exact operator identity (alpha I+beta S)(alpha I+beta S^-1)=I-alpha beta L yields coefficient [p^2/(p-1)*<h^circ,L+ h^circ>-||h^circ||^2]/(2n), with O(|epsilon|^3). Fourier eigenvalues 4sin^2(pi k/n)<=4 and p^2/(p-1)>=4 prove nonnegativity, and equality for nonconstant h precisely p=2, even n, pure alternating mode. Independent Green-object reconstruction from seven observed blobs, 15 independently implemented finite-difference comparisons (n=2,3,4,6,9; p=1.3,2,3.7), and separate four-cycle Green-energy computations (1/2 and 1/4) corroborated the proof. The grouped-minus-alternating coefficient equals p^2/[32(p-1)] as stated. Finite checks do not prove all quantifiers.

## originality

PASS

Best-of-knowledge PASS for the full all-n, all-1<p<infinity local numerical-radius Hessian with cycle Green pseudoinverse and exact null-mode classification. Directly inspected 2012-2025 Hilbert cyclic-shift permutation papers establish global arrangements or Hilbert eigenvalue formulae; those are real prior coverage for the p=2 specialization. The distinct published all-p four-cycle rearrangement theorem strongly covers the displayed local grouped-versus-alternating ordering for that special two-weight family, so that example is not claimed independently new. It does NOT give an arbitrary-dimension, arbitrary-weight-direction coefficient, analytic profile, or complete Fourier Hessian spectrum. Distinct published non-Hilbert nilpotent-shift and exponent-derivative results study different operators/limits. Targeted semantic Resultary searches and public literature searches did not identify the complete assertion outside the assigned finding; absence is not proof of originality. Key priority risk remains a possible older nonlinear-Perron/Banach numerical-range sensitivity theorem and the uninspected portion of Chang-Wang 2012; lawful OA/preprint attempts failed and authorized Oxford retrieval returned vpn_disconnected, so no false whole-paper coverage judgment is made.

## value

PASS

The spatial numerical radius is a canonical nonlinear Banach operator invariant, and finite positive weighted cyclic shifts are the natural family underlying classical numerical-radius permutation problems. The theorem computes its complete second variation on the n-dimensional positive weight space for every n>=2 and 1<p<infinity, in terms of the meaningful graph Green inverse. The formula resolves mode-by-mode perturbation sensitivity, identifies the unique Hilbert alternating flat direction, and yields an arrangement comparison from the full quadratic law. Although the two-weight four-cycle strict ordering is covered globally by a separate theorem, the arbitrary-n all-direction spectral Hessian and sharp zero-mode characterization are neither a mere table lookup nor an arbitrary unmotivated slice; they are standalone natural exact facts usable for local sensitivity/stability studies. The proof uses standard perturbation methods but the computed Green-energy coefficient and zero-mode classification are structurally informative and not established in the inspected prior Banach weighted-cycle statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
