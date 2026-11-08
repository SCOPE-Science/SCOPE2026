---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For lambda,mu>0 normalize the larger to one and r=m/M in (0,1]. The hexagon N(s,t)=max(|s|,|t|,|s-t|) has exactly six displayed vertices and six signed facets. By convexity of the square of a norm on the product of any two boundary edges, for each radial pair (a,b) the maximum of N(au+rbv)^2+N(rau-bv)^2 occurs at a vertex pair. The two facet maxima can be interchanged with the finite maximum; all 36 ordered vertex pairs times 36 ordered facet pairs give exactly 18 distinct symmetric 2x2 coefficient matrices. For E=(2+r²+r sqrt(r²+4))/2, every diagonal Q_ii<=1+r²<=E. An independent SymPy polynomial-remainder calculation in S²=r²+4 verified that all 18 determinants det(EI-Q) equal seven explicitly nonnegative types, with multiplicities 4,1,6,1,1,1,4; all are >=0 on 0<=r<=1. Hence all E I-Q are PSD and the quotient <=E/(1+r²). For u=(1,1), v=(1,0), tau=(r+sqrt(r²+4))/2, x=u,y=tau v, the norms are 1+r tau and tau, and (1,tau) is an eigenvector of [[1,r],[r,1+r²]] with eigenvalue E; this attains equality. The parameter inequality <=4/3 follows by squaring nonnegative sides 3r sqrt(r²+4)<=2+5r²; the difference is exactly 4(2r²-1)², with equality only r=1/sqrt2. At r=1 the value is (3+sqrt5)/4; the excluded r=0 gives only the limiting value 1, not an asserted parameter case.

## originality

PASS

Statement/implication comparison of the exact two-parameter unrestricted Liu–Li L_YJ on the canonical affine-regular hexagon. The balanced C_NJ=(3+sqrt(5))/4 is known; no novelty claimed for that slice. The 2024 exact L_YJ octagon theorem treats a different eight-vertex norm, while the 2024 James comparison and the published universal L_YJ envelope provide upper bounds, not the sharp hexagonal equality. The 2024/2025 Banas–Fraczek exact result concerns max(lambda|a|,sqrt(a^2+b^2)), a nonpolyhedral Euclidean-arc norm, so is not a linearly isometric presentation of the six-facet target. Published same-hexagon indexed records on generalized von Neumann–Jordan exponent p and Liu–Yang parameter concern different quotients. Primary full-text access to the defining 2021 article was blocked after OA and arXiv attempts, with Oxford VPN disconnected; this remains a named residual priority risk rather than an automatic scientific failure.

## value

PASS

L_YJ quantifies the failure of the Euler–Lagrange/Hilbert identity, and the affine-regular Day–James hexagon is a canonical non-Hilbert two-dimensional norm. Its exact unrestricted two-parameter distortion is a natural invariant not fixed by the known balanced C_NJ value or published universal inequalities. The rigorous continuum profile exhibits a non-obvious off-balanced maximum 4/3 at lambda/mu=sqrt2 or its inverse, strictly exceeding the classical balanced (3+sqrt5)/4. A finite-facet semidefinite proof supplies a reusable exact method for other polyhedral Banach norms. This is a meaningful complete natural-object profile without claiming broader classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
