---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With the specified target norm, the images of the Hardy monomials are orthogonal and have lengths (k+1)^(-alpha)|sum_j a_j rho_j^k|, tending to zero. At L=t^(-1/alpha), count those with (k+1)/L below the 1/alpha power of the modulus. On a bounded window containing all such indices, character tests against continuous functions of (k+1)/L converge to the Lebesgue-Haar product: geometric partial sums are bounded for every nontrivial character and summation by parts handles the slow factor. The threshold graph has product measure zero by its singleton x-sections, even when the orbit distribution has atoms or exact cancellations. Integrating the subgraph gives M_alpha; the squared modulus has Haar mean sum_j |a_j|^2 by distinctness, so M_alpha>0. Inversion of the strict count yields s_n~M_alpha^alpha n^(-alpha) and harmonic summation gives the critical residue. For the equal two-term example the finite cosine sum is 1+2 sum_{k=1}^{floor((b-1)/2)} cos(pi k/b); the Dirichlet kernel formula yields the two parity values, including b=1 (coincident rotations combined) and b=2 (zeros on odd indices). On irrational orbits the mean is 4/pi. Rational denominators tending to infinity give that same limit, with strict finite-denominator inequalities in opposite directions. The diagonal difference bound k|theta-phi|/(k+1) independently gives norm Lipschitz continuity. No numerical premise is needed.

## originality

PASS

Best-of-knowledge pass for the finite-superposition sharp residue and its explicit arithmetic discontinuity, not for the one-rotation diagonal, the summation identities, or the general equidistribution mechanism. No inspected antecedent gives or implies the full claim as a stated general theorem.

## value

PASS

An exact tail constant for a natural class of compact superpositions quantifies cancellations that individual ideal memberships do not detect. The two-term example gives sharp rational values and demonstrates a genuine instability of the critical residue in an operator-norm Lipschitz family, not an instability of operator norm itself. The elementary ingredients do not make the combined spectral and arithmetic conclusion vacuous.

The dated certificate retains the supplied scientific assessment, sources and limitations.
