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

For every integer N in 2..65536 and grid j/N, exact stochastic rounding of 4j(N-j)/N has support on integer indices floor and ceil with strictly positive weights whenever distinct. The supplied integer C++ verifier builds all directed edges for each N, reverse-BFS from 0 and checks that the only vertices not reaching 0 are empty when 4 does not divide N or precisely j=N/4,3N/4 when 4 divides N. Independently reconstructed and executed all four disjoint exhaustive blocks, covering every one of 65,535 denominators and 2,147,581,950 states without discrepancies. The extra two vertices are a feeder 1/4 to absorbing 3/4; all others reach 0, eliminating any other closed class. In any finite chain transient states absorb almost surely, and invariant probabilities are convex combinations of 0/3/4 point masses. Separately nearest-support transport from arcsine density at split 3/8 gives exact Wasserstein minimum about .15568790319968789436 and W1(delta0,rho)=1/2. This is a complete FINITE classification only through N=65536, not an all-N proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison: the inspected classical tools, records, and primary material do not establish this complete new specific claim. Originality is qualified by explicit risks and limited full text; a failed search is not itself novelty proof.

## value

PASS

An exhaustive two-byte/16-bit grid range provides an exact phase diagram for a natural unbiased stochastic-rounding model: stationary simplex dimension jumps between adjacent denominators 65535 and 65536 and asymptotic distributions remain far from continuum chaos. The full classification and exact discrepancy offer reusable numerical-dynamics benchmarks, not a random tiny slice or finite sample extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
