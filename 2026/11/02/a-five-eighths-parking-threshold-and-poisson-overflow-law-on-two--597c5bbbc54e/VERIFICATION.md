---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the deterministic complete b-ary height-two tree (N=b^2+b+1), the order-independent upward flux recurrence R_v=(A_v+sum_child R_child-1)_+ is exact; independent direct-versus-sequential enumeration matched all 50,549 preference sequences in the declared b=2,3 small cases. Under Poisson arrivals with per-vertex mean mu=t*b^(5/4)/N ~ t*b^(-3/4), leaf double occupancy probability q=e^-mu*mu^2/2. For each parent B_i~Binomial(b,q), and b*P(B_i>=2) -> t^4/8. The b independent rare-parent events converge in total variation to Poisson(t^4/8); higher leaf occupancies, parent direct-arrival intersections and triple-leaf collisions are bounded by O_t(b^-1/4). On the good event each crowded parent emits one car, the root absorbs one, so F=(Z-1)_+. Monotone coupling of fixed car count with two Poisson counts proves full fixed-m distribution and sharp sub/supercritical zero-failure threshold at m~b^(5/4)~N^(5/8). The Poissonized rate O_t(b^-1/4) is not asserted for fixed-m. Finite enumeration validates recurrence but does not replace the asymptotic estimates.

## originality

PASS

Best-of-knowledge PASS for the complete shifted-Poisson escape-count law and 5/8 critical load exponent on a deterministic height-two high-degree tree. Existing rooted-tree parking enumeration and random Cayley-tree/constant-degree Galton–Watson results have different graph sequences/load regimes, and generic Poisson approximation/Abelian recursion is credited. No same-parameter exact limiting law found in Resultary or inspected literature; historical priority remains qualified.

## value

PASS

A canonical two-level hierarchy yields a sparse-arrival parking phase transition through a double-collision cascade, with a nontrivial exponent 5/8 and an exact nondegenerate law for the number escaping, not only a success probability. This natural exact benchmark can inform parking and load-balancing investigations in shallow networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
