---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For every n>=5, objective ||P-J/n||₂ is convex and dihedral-invariant, so averaging arbitrary spatially varying admissible symmetric Markov matrices proves a global lower bound from invariant weights without claiming global uniqueness. For n>=6 the spectrum is a quadratic f(cos(2πk/n)) anchored at f(1)=1. For h=floor(n/2), j=floor((n+2)/4), u=cos(2π/n), ell=cos(2πh/n), v=cos(2πj/n), the grid maximum of (x-ell)(u-x) is at v. Equioscillation f(ell)=f(u)=t,f(v)=-t determines t=Δ/[Δ+2(1-ell)(1-u)], Δ=(v-ell)(u-v), and the sign-change plus root at 1 proves optimality and unique invariant polynomial. Coefficients p1=-(u+ell)/T,p2=1/(2T),p0=(Δ+1+2u ell)/T satisfy strict positivity by the even/odd factorizations, so relaxed optimum is feasible. n=5 is complete and J/5 unique. Taylor expansion yields gap 8π²/n² and n²p1 even/odd 2π²/3π²/2. The proof does not claim uniqueness of all inhomogeneous minimizers.

## originality

PASS

PASS, qualified. Boyd–Ghosh–Prabhakar–Shah (2005) Section 3.1 already treats k-nearest-neighbor rings including k=2 and obtains lower bounds and asymptotically good weights, while Boyd–Diaconis–Parrilo–Xiao (2009) proves symmetrization and the one-step cycle example. The assessed exact all-finite-n C_n² three-weight minimizer and mod-four active frequency are not stated in the inspected relevant sections. A historical exact Chebyshev/minimax equivalent could exist.

## value

PASS

PASS. The exact minimizer solves a standard design problem for a natural k-nearest ring graph at every finite n. The active frequency/parity structure and strictly positive yet vanishing one-hop weight characterize stability that near-optimal asymptotics cannot determine; the fourfold limiting gap gain is a useful sharp comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
