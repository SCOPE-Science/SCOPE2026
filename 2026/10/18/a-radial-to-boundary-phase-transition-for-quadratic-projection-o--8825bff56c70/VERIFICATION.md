---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The 2nd and 4th isotropic weighted-ball moments produce the displayed exact degree-two reproducing kernel: constants + D<x,y> + D(D+2)/2[(x·y)^2-||x||^2||y||^2/d] + D^2(D+2)/(4dk)(||x||^2-d/D)(||y||^2-d/D), D=d+2k. Radial squared norm has Beta(d/2,k) law; d(1-R_d^2)/2→Gamma(k) in L1 and normalized angular coordinate→N(0,1) independently. Uniform in radius, the kernel divided by d tends in L1 to one-half the absolute value of (1-r²)(G/k-1)+r²(Z²-1). The limiting profile is strictly convex on interior: its maximum is at r=0 or 1 only, even at the tie. Endpoints integrate to k^k e^-k/Gamma(k+1) and sqrt(2/(pi e)), equal at k=1/2; the gamma centered absolute deviation decreases strictly with k by gamma/Beta conditional Jensen. Independent symbolic moment-reproduction and representative finite-weight checks supported normalization. Limit is only for fixed k>0; no finite-d exact maximizer is claimed.

## originality

PASS

The Li–Xu and Figueroa primary papers study ball orthogonal polynomials and projection approximation with fixed d and polynomial degree varying; a separate 2024 sphere minimal projection result supplies a related Gaussian constant but not the weighted ball fixed-degree high-d Gamma radial profile. The all-dimension asymptotic norm and exact weight transition are not implied by their inspected theorems. Originality passes with possible obscure Christoffel/Lebesgue-function literature overlap.

## value

PASS

The canonical degree-two projector has a natural endpoint stability norm; the theorem gives its sharp high-dimensional coefficient and a discontinuous change of extremizer region with the radial weight. This phase transition is a motivated precise invariant, not a numerical fit or a general-fact relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
