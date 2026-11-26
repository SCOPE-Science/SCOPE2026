---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On the symmetric rank-k idempotent orbit, differentiating along [Omega,P] and using the nondegenerate trace pairing on skew-symmetric matrices makes [P,Q]=0 the critical equation. A simple-spectrum symmetric Q has mutually orthogonal nonisotropic eigenlines, so commuting projectors give exactly the claimed values. On repeated spectra F is the specified formal continuation, not an actual critical-point census. Each unordered pair I,J is uniquely the disjoint oriented differences up to exchange plus their intersection C, giving binom(n-2r,k-r) repetitions of its squared difference and a factor 4 for every value pair. This includes the r=1 Vandermonde orbit and the empty resonance product at k=1 or n-1. In the root ring each r>=2 unsquared product transforms by a character; the sign character would force every eigenvalue difference to divide it, impossible by the supports. Transitivity and unique factorization then prove irreducibility in the invariant coefficient ring, and for the Vandermonde square the only proper feasible invariant exponent would be one, ruled out by sign. Distinct orbits have distinct hyperplanes. Away from the other hyperplanes on one lift of a resonance component the only repeated values are the indicated disjoint pairs; a third member would require another equality hyperplane. The ordered gaps on (0,1,2,3) and the lexicographic sign of the three-factor cubic check out. The degree in the Finding is the degree in the spectral roots as computed in Proof §3, equivalently the weighted coefficient degree with wt(e_j)=j, not the ordinary degree in e-coordinates. For example, T_{5,2} has root degree 15 but vanishes when e_2 through e_5 are zero, since then only one root can be nonzero and some factors omit it. Thus it cannot have ordinary coefficient degree 15. Read VERIFICATION.md and verify.py; the latter was not run and its integer examples do not establish the universal factorization or a matrix-entry factorization.

## originality

PASS

The supported distinct result is the full irreducible resonance-orbit decomposition with exponents and the generic coincident-value portrait for projection Grassmannians in the universal spectral ring. The Grassmannian ED critical-point description, the distinction between critical-point and critical-value degeneration, and the subset-sum resolvent construction are antecedents, not novelty. The inspected known results do not state or cover the orbit-factor census and its generic geometric interpretation. The isolated four-root example is illustrative, not a separate novelty assertion.

## value

PASS

An explicit irreducible discriminant is useful for separating degeneracy of the critical equations from collisions of values. The exponents and generic counts say exactly how a simple real or complex spectrum can produce several unrelated ties on a single component, uniformly over n,k. This is not a rebranding of the ED-degree theorem, does not assume factorization after pullback to matrix-entry space, and does not claim that these ties are global minima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
