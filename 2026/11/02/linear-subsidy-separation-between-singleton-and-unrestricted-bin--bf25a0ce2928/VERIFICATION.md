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

If g0 goes to B, every A-agent needs at least one unit, since the subsidy at the recipient is nonnegative. If g0 goes to a0 in A with subsidy t, equal utilities within A force each of the other r−1 agents to receive 1+t. A total below r leaves less than one for all B subsidies and rt combined. Equality of utilities within B and the integer number of approved goods then force all B bundle sizes to be identical: the sizes cannot differ by an integer while subsidies differ by less than one. The common size is at most one by the total 2r−1, and cannot be zero because B would envy a subsidized A-agent. With size one, B has utility strictly below two, so none of the remaining r−1 approved goods can go to any A-agent other than a0. Giving them all to a0 violates the same bound since r−1≥2. For attainment, put g0 alone with a0, split the other goods among B with sizes 2,...,2,1, and pay one to the r−1 empty A-agents and the last B-agent. Own utility is one in A and two in B and no other bundle plus payment exceeds it for that type. Under singletons, assigning g0 to B creates bilateral envy with an A-agent holding an ordinary good whose two inequalities sum to 0≥2. Thus g0 goes to A, and comparing any B outcome with an ordinary good and subsidy 1+t held in A forces every B payment to be at least 1+t. Zero for a0 and one for everyone else attains 2r−1. The lower bounds apply to real payments. At r=2, g0 and one ordinary good can go to a0 and B can receive one each, with just the other A-agent paid one; this confirms why the unrestricted formula excludes the boundary. I inspected the finite allocation and difference-constraint check without executing it; the direct argument establishes the infinite result.

## originality

PASS

The supported distinct claim is the exact deterministic comparison on the same two-type square valuation matrix. Neither subsidy feasibility, prior worst-case n−1 bounds, nor the fact that the singleton problem is algorithmically solvable is new here.

## value

PASS

On the same square binary input with only two types, constraining bundle size nearly doubles the minimum budget, with an exact unbounded additive gap. The example isolates a concrete obstruction to generalizing continuous-random coincidence, and shows how allowing empty and doubled bundles lowers the budget. It is not a claim of a universal factor-two ceiling or a maximum gap across binary instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
