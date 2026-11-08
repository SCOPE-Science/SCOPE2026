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

Uniform convergence of H(x)=sum_j (-1)^j x^{underline j} follows from j! divisibility, while divided differences converge since deleting one of j consecutive factors retains factorial divisibility. Odd H' is 1 mod 2; even H' is 2 mod 4, giving exact 2-adic distance laws on odd inputs and even inputs within a mod-4 class. Rescaled branches F_odd, F_0, F_2 are isometric bijections of Z_2; this yields each even residue once, each 1 mod 8 four times and no other fibers. Difference valuation also proves least period 2^k and closure support has measure 5/8. Independent full-fiber recurrence checks k=1..10 passed, distinct from the global proof.

## originality

PASS

Best-of-knowledge PASS for exact all-residue fiber multiplicities, with prior 2-adic continuity and weighted-derangement period results properly excluded from the novelty claim. O'Desky-Richman Theorem 1.2/1.5 establishes p-adic regularity for larger classes, not the derivative-induced precise 1/4 fiber law. Hidden implications of general interpolation are a residual risk.

## value

PASS

Classifies the 2-adic value distribution and support of a classical combinatorial sequence exactly rather than only congruences, index periods, or continuity; a natural and reusable arithmetic-statistical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
