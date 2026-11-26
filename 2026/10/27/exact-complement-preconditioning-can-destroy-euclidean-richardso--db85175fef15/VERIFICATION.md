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

The fine diagonal block is SPD and its Schur complement is 1−2ε²>0. The largest absolute row sum of A is bounded by 1+2ε<2, so all eigenvalues are in (0,2) and the symmetric Type-II error map at β=1 has norm <1. For Type III the applied inverse is diag(1,α,α/δ); its first and second coordinate test gains are at least αε/√δ and exactly √(ε²+(1−α)²), respectively. Norm ≤1 would force α≤√δ/ε≤ε²/2 and thus squared gain at least 1+ε⁴/4, impossible. At α=δ, F^(1/2)AF^(1/2) is SPD with row sums <2, so the similar FA gives spectral radius <1 for I−FA. The same α gives a norm limit √(1+ε²); every sequence of bounded near-minimizers as δ→0 has α=O(√δ), so the second coordinate test proves the matching lower limit. The rational example has exact gains bounded below by max(64α,√(1/16+(1−α)²)); at α≤1/64 the latter is at least 65/64. With a one-dimensional complement, compression of T⁻¹ is a positive scalar, so the two scaling families coincide after reparameterization. The obstruction range is sufficient, not claimed to be a sharp transition for fixed δ. The checks in check.py are finite corroboration; the uploaded program was inspected, not run, and the universal bounds were independently derived.

## originality

PASS

The inspected close literature and catalogue statements do not cover the combined Type-II-safe, exact-complement Type-III-unsafe example and sharp limiting infimum in the same original Euclidean norm. This is a bounded judgment about that specific separation, not a claim that nonnormal transient amplification or spectral-versus-Euclidean distinctions are new.

## value

PASS

This example answers a concrete tuning question: even an exact inverse of the fine block with an optimally chosen positive scalar may be strictly worse than leaving that block unpreconditioned for Euclidean one-step Richardson safety. The sharp limiting gap and the minimum dimension distinguish it from a generic example of nonnormal growth and give an explicit benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
