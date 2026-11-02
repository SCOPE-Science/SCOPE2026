---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Radial covariance gives E[y_i y_j]=q_d delta_ij, making the reproducing kernel exactly K(x,y)=1+x dot y/q_d. Symmetry and radial convexity of integral |K| put the sharp output at outer |x|=1; sign of K gives extremizing input and symmetric kernel gives matching L1 norm. Kernel has unit signed mass, so endpoint norm is one plus twice the negative cap moment, outer ball minus inner ball, with correct volume normalization. A uniform-shell radius coupling proves 0<=q_d’(r)<=r/d<1, so r-q_d(r) has exactly one zero in (1/(d+2),1/d). At inner-ball contact, h=r-q_d(r)>0 small and the cap beta integral has order h^((d+3)/2) with coefficient 4 omega_{d-1} 2^((d-1)/2) r_d^((d-3)/2)/((d+1)(d+3)). Multiplication by 2/(omega_d(1-r_d^d)) and h’=1-q_d’ yields claimed C_d>0. This term is one-sided, so its derivative order is ceil((d+3)/2). Planar q2=(1+r²)/4 yields r2=2-sqrt3; independently checked numerical cap moments and elementary circular formula at five radii. Computations do not substitute for all-d proof.

## originality

PASS

Degree-one projection covariance is elementary and pre-existing filled-ball polynomial projection/weighted hyperinterpolation is established. The inspected primary treatments do not give sharp punctured-shell endpoint norm, unique inner-hole contact, or universal one-sided fractional cusp as dimension varies. These specific shape parameters are essential, not a mere renaming of filled-ball asymptotics.

## value

PASS

Sharp endpoint stability under a concentric drilled hole is a natural geometric perturbation of an elementary polynomial projection. A unique contact point changes exactly which kernel-negative cap is removed, producing a dimension-universal first nonsmooth derivative and explicit threshold, a meaningful shape-sensitivity invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
