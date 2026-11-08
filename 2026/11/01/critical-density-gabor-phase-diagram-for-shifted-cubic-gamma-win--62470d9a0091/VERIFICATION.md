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

Reconstructed Zak transform as e^{-λx}F_{c+x}(r e^{2πiω}), F_u rational from cubic geometric moments. Verified symbolic numerator identity F_u(-r)=P_r(u)/(1+r)^4, exact Cayley transform F_u=(1+w)H_u(y), cubic discriminant −12E(u), and Routh–Hurwitz determinant 6u(u−1)(2u−1). Root signs show any zero inside unit disc must lie on negative real z, so only ω=1/2 can vanish. P_r derivative and values at 0,1 give the r0=2−√3 root-count transition; shifted-series identity shows u_+−u_-<1, covering the parameter intervals. At c=u_+, the sole boundary Zak zero has nonzero real and frequency derivatives, with local minimum in ω and monotonic increase away from c boundary, while compactness rules out other global minima. Squaring P_r/(1+r)^4 gives exact boundary lower bound and leading 9(v_+²−r)²/(1+r)^6 δ². Independent sympy exact identities plus source finite checker inspection corroborate; no finite Zak grid is used as a universal proof.

## originality

PASS

Classical Zak multiplier criterion is not new; cited totally-positive-window uniqueness and B-spline/exponential frame-bound studies do not contain the causal shifted cubic-gamma polynomial root diagram or damping-dependent two-zero regime. Published related sharp quadratic onset for a tent spline concerns a different window and noncritical lattice. Best-of-knowledge priority subject to further polynomial-exponential window literature.

## value

PASS

Exact critical sampling stability for a natural shifted causal cubic-gamma family requires nontrivial control of complex Zak zeros and a delicate two-root phase, not merely plugging into the generic Zak criterion. The explicit threshold and quadratic optimal lower-bound coefficient identify a precise robustness/ill-conditioning phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
