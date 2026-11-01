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

The reversible 3-site mode generators have equal stationary mode masses 1/2 because switching is site-independent and symmetric. Restrict each phase to the 2D zero-sum space; the resulting 4×4 stationary H(r) is H0+rK with rank(K)=2, hence det H=det(B0 B1+r(B0+B1)) is quadratic, with positive constant and leading terms. Generator irreducibility ensures det H>0 on all r≥0. Every 3×3 adjugate minor is at most quadratic since K has rank two. Because each frozen mode is detailed-balanced, the numerator N(r)=d(r)J(r) vanishes at r=0, yielding J(r)=r(A+Br)/d(r), so at most one positive current sign reversal. An independently built exact six-state rational stationary solver verified the published witness J(r)=r(r−2)/[2(103r²+339r+252)] and its stationary populations at r=2; the positive entropy lower bound (5/61)log(17/12) follows from unequal mode-flip fluxes and nonnegative edge contributions. The rank argument, rather than checked instances, proves the arbitrary strictly positive phase parameters.

## originality

PASS

Explicit ratchet reversals occur in earlier special models, especially Lee et al. 2003, and are not claimed new. The assessed theorem instead has universal quantifiers over every pair of strictly reversible positive 3-state generators under homogeneous symmetric Poisson switching and bounds all positive-axis switching-rate zeros. The full accessible 2003 primary PDF describes a discrete-time noisy 3-state model with a single transition matrix and different parameterization; it does not supply the six-state reversible-pair uniform rank bound. Jarzynski–Mazonka and Levien–Bressloff study special physical ratchets or asymptotic reductions. A broader finite-motor theorem remains possible.

## value

PASS

An exact global bound on direction changes as a physical switching rate varies for all two-mode reversible three-site ratchets is a nontrivial dynamical rigidity principle. The attained single reversal and stall with nonzero entropy production make the bound sharp and distinguish visible current from thermodynamic equilibrium. It identifies a structural barrier to repeated reversals that motivates adding sites, irreversibility, or nonhomogeneous switching.

The dated certificate retains the supplied scientific assessment, sources and limitations.
