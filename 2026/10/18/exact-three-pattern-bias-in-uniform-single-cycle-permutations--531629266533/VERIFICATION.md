---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For n>=4, specify an n-cycle as a permutation with one group-theoretic cycle and use non-wrapping triples of values at positions i,i+1,i+2. An injective prescribed three-edge partial map extends to an n-cycle iff it is acyclic, then uniquely by cyclically arranging n-3 path components in (n-4)! ways. Removing the only possible partial directed cycles (loops, 2-cycles, 3-cycles) by inclusion-exclusion yields the six explicit integer Q_tau(i,n) polynomials; summing i and dividing by (n-1)(n-2)(n-3) gives zero shift for 123/321, -1/[2(n-1)] for 132/213 and +1/[2(n-1)] for 231/312. Multiplying shifts by P(one n-cycle)=1/n gives the indicated covariance. Direct independent enumeration of n-cycles at n=4..8 gave 30 exact rational mean checks; source verify_cycles.py and symbolic derive_table.py were read, and their algorithms agree with the proof. Finite checks corroborate but do not prove all n.

## originality

PASS

PASS best-of-knowledge for the four nonmonotone n-cycle-conditioned means and their complete six-pattern balance, not for descent-set/monotone entries alone. Prior cycle-type/descent-set results are stronger for 123/321 and credited. Generalized k-descent codes do encode these patterns but no inspected theorem evaluates their n-cycle-conditioned nonmonotone means; unconditional pattern Poisson approximation does not imply them. Older higher-order cycle-pattern identities remain a genuine priority risk.

## value

PASS

The uniform n-cycle is a canonical random permutation class; consecutive 3-patterns are the smallest complete local order-sensitive motifs beyond descents. The exact all-n six-way bias and paired cancellation reveal subtle global-to-local dependence not visible under the unrestricted uniform measure, with natural applications to cycle-conditioned local-pattern statistics, even though the shifts vanish asymptotically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
