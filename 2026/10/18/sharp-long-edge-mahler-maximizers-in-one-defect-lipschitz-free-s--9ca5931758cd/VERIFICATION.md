---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The finite metric is admissible on 1<=t<=2, with the changed pair distance at most two through any other point. In anchored molecule coordinates, equilateral transportation balls decompose by signs into two simplices in each orthant; Vandermonde gives vol P_{d,1}=choose(2d,d)/d!. Removing the marked edge leaves two opposite exposed facets, because every integer tight spanning-tree Lipschitz potential has |f_a-f_b|<=2 and equality only at the positive/negative distinguished potential. Each exposed facet is a determinant-one (d-1)-crosspolytope, and moving the two molecule apices from +/-v to +/-v/t changes total volume by 2^d(1-1/t)/d!. For the polar, fix core-vertex potentials with range R; the endpoints share an interval of length 2-R, restricted to |f_a-f_b|<=t, yielding area (2-R)^2-((2-R)-t)_+^2; integrate using the exact range distribution of d-1 anchored core values to get d+1+(2/d)(1-(2-t)^d). Differentiating gives F_d(t) with derivative strictly negative on [1,2) for d>=3, and opposite endpoint signs, hence a unique maximum. At d=2 the product is (t+2)(4-t) and decreases beyond 1. C(2d,d)~4^d/sqrt(pi d) gives (2-t_d)^(d-1)=Theta(d^(3/2)2^(-d)), so t_d->3/2 and the relative gain is 1+2/[d(d+1)]+o(d^-2). Independently verified exact planar identity and strict derivative grid in d=3..30 (rational arithmetic), plus stationary tests, not an exhaustive proof.

## originality

PASS

The equilateral volume product (d+1)choose(2d,d)/d! is explicitly published by Alexander et al and not new. That source’s global maximizer structural theorems do not calculate the one-long-edge deformation; the new continuous primal/polar formulas, strict in-family maximum and t_d asymptotics remain after removing covered ingredients. Aliaga gives molecule/extreme-point framework, while Gordon–Petrov generic combinatorics lacks this degenerate one-edge profile.

## value

PASS

The Mahler product is an affine-invariant quantity naturally associated with Lipschitz-free Banach balls, and a single variable metric-edge deformation isolates geometric transition mechanisms not visible in combinatorial counts. Exact primal and polar volume formulas, the change from boundary optimum at d=2 to unique interior optimum for every d>=3, and a universal t_d->3/2 limit give a complete motivated continuous extremal classification. The asymptotic gain of order d^-2 is small but the structural optimizer and phase change are substantive and not merely a tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
