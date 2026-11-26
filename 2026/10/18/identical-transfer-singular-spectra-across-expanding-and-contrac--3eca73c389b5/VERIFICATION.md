---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A stronger direct check is P_{A_m}^n−Π = P_{U^{mn}}(P_R^n−Π): commutation gives the factorization at every n, and the outer transfer is unitary on the output L² and fixes constants, so the input Gram operator is literally the same. Its diagonal on e_k/ρ(k) is ρ(k)^{-2} for nonzero k in (Rᵀ)^n Z^d and zero otherwise. Thus in the compact case the list is the ordinary singular-value multiset, also for n=0. For general bounded-below weights the list is the positive diagonal eigenvalues of the modulus with multiplicities, not a claim that a noncompact operator has a decreasing compact-type singular sequence or that the list includes spectral limit points. Unitary invariance holds for approximation numbers too. R²=2I and Rᵀ(x,y)=(y,2x) give 2^j times Z² or Z×2Z, both with shortest nonzero length 2^j. The eigenvalue moduli are √2 times (1+√2)^{±m}; at |m|=1 already √2/(1+√2)<1. Degree two means a two-sheeted covering (signed determinant is 2(−1)^{m+1}). Dyadic shells give the precise sp>2 test, and after removing 4^{-jsp/2} from the p-power sums the summable majorants are Q^{-sp/2}; the odd terms are strictly smaller for b≠0. Inspected check.py: the 51,623 reported tests count 11×13×19² exact finite membership cases plus separate label checks; not executed or used for the proof.

## originality

PASS

The Fourier action, unitary invariance and lattice identities are standard mechanisms, not priority claims. The supported distinction is the explicit infinite mixed/expanding comparison with full all-iterate Sobolev singular data and exact parity profiles; the closest inspected results do not supply that construction or an implying example. This is a bounded comparison, not a claim of unique priority.

## value

PASS

For a natural inverse question about what precise transfer smoothing reveals about expansion, the family gives a concrete negative answer even with every singular value at every time and arbitrarily disparate hyperbolic rates. The two computable Schatten phase constants add information absent from the top singular value, whose shortest-length formula cannot distinguish the two parity lattices at fixed j. The significance is the witness, not an isolated application of unitary invariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
