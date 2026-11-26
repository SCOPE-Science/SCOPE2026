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

A feasible nonempty pattern with maximum letter count h shares a constant-letter subsequence of length h with every host of the specified content and has length at most T=min(k, sum_i min(c_i,h)). Conversely one can realize every admissible h with total T and maximum count h by reserving one coordinate of capacity h, then filling the remaining capacities. Placing those counts in reverse block order from the host forces every common subsequence to use one letter and attains T−h. The empty host and pattern give zero. Globally the deficit of a feasible length-m pattern is at most m−ceil(m/q), a nondecreasing function of m. Pure-letter patterns detect the capped count of every letter at any nonnegative budget. Opposite block orders with balanced counts and total length k attain the bound k−ceil(k/q); the reverse host distinguishes itself from the forward host at every lower budget without changing the capped counts. This also covers q=1 and k=1, when no lower nonnegative budget exists, and q>k, when the witness uses k distinct letters.

## originality

PASS

The definition, finite-index framework, capped-count result at budget k−1, and the pigeonhole sufficient condition are not credited as new. The supported distinct claims are the exact worst-order envelope at every content and the matching necessity at the alphabet-dependent collapse threshold. Inspected more precise subthreshold counts apply to one binary parameter triple, not the general sharp statement.

## value

PASS

The exact envelope determines how much order can cost at a prescribed content, including highly unbalanced contents where the worst-case alphabet bound is far from attained. The sharp collapse theorem answers exactly when all order information disappears from this established equivalence model, rather than giving another nonoptimal sufficient budget. The two statements are useful despite not classifying the subthreshold quotient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
