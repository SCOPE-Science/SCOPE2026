---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Self-adjoint conjugate-linear A is represented by complex symmetric M, Takagi-unitarily congruent to diag(s_i). For normalized frame pair with <x,y>=t=|q| under first-variable-linear convention, the complex symmetric rank-two matrix K=(xy^T+yx^T)/2 equals ((1+t)/2)uu^T-((1-t)/2)vv^T for orthonormal complex u=(x+y)/sqrt(2(1+t)),v=(x-y)/sqrt(2(1-t)) (limit t=1 separately), so K has singular values (1+t)/2,(1-t)/2. Von Neumann trace majorization bounds |tr(MK)| by the proposed affine combination of s1,s2. Witness x=alpha e1+i beta e2,y=alpha e1-i beta e2, alpha²=(1+t)/2, beta²=(1-t)/2 attains equality. For any q, an isotropic x for the complex quadratic form x^T M x exists; since n>=3 take a unit z orthogonal to both x and Ax, giving a valid y with zero numerical value. The constrained two-frame manifold is connected and compact, and simultaneous rotation yields full circular symmetry, so all moduli from zero to maximal are attained: a closed disk. Independently checked 105 top-two equality cases, 2,625 randomized admissible upper-bound frames and spectral extraction. Finite numeric checks corroborate the all-dimensional matrix argument.

## originality

PASS

Full text comparison to the same q-numerical range theorem reveals direct coverage of the disk shape but not its radius. The substantive surviving sharp top-two-Takagi law is supported by standard-but-nontrivially-combined spectral arguments.

## value

PASS

The constrained q-numerical disk is a natural operator-theoretic invariant. An exact affine spectral response identifies precisely which singular values survive q-variation and provides a complete reconstruction/invisibility theorem for self-adjoint antilinear operators, beyond the known qualitative disk geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
