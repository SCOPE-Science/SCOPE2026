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

A direct event argument avoids assuming generator-domain regularity or a finite mean in advance. Set S=α+β. From the reset site while inactive, the time to go active has rate α+rηπ₁: all other reset outcomes leave the searcher at that same state. Its mean is Δ=S/[α(S+rη)]. Starting active, measure time only while active. A direct reset occurs at rate r; an off excursion begins at rate β, lasts an independent Exp(α+r), and ends in a position reset with probability r/(α+r). If it ends in reactivation, the active Markov motion continues from the same state. Thus in active time the first disruptive reset has rate q=r+βr/(α+r), is independent of the active path, and competes with τ. A cycle succeeds with probability F(q) and uses mean active time d=(1−F(q))/q. The expected wall-clock time including all off waits until reset or success is d[1+β/(α+r)]. After a direct reset the inactive probability is ηπ₀; after a reset during an off period it is 1−ηπ₁. Including the time to return to active at x_* adds d[rηπ₀+βr(1−ηπ₁)/(α+r)]Δ to the cycle cost. The combined multiplier of d is exactly S/α. By regeneration at active x_* and F(q)>0 the mean is finite and equals Sd/[αF(q)], independent of η. Stationary initialization adds π₀Δ, giving the formula and strict improvement for η'>η. This is a mean identity only, and geometry independence concerns the penalty at a common starting and reset site, not arbitrary initial sites or the full mean itself. The finite-state script and recorded comparisons were inspected, not executed.

## originality

PASS

The supported distinct result is the complete partial-refresh mean law for a strictly immobile off state, including active-start invariance and cancellation of all active-search dependence from the stationary-start difference. The nearest verified comparisons treat moving internal states or a switching target that does not stop the searcher's interior motion. A generic two-state renewal system is antecedent methodology, not a demonstration of this scalar cancellation for the frozen model.

## value

PASS

This answers a natural protocol-design question: when does the mean benefit of forgetting an internal mode depend on the search geometry? It identifies all geometry dependence in one active first-passage transform and shows why the benefit at the reset point comes solely from stationary initialization into the frozen state. The exact penalty and active-start invariance apply without solving the spatial process, even when its original mean first-passage time is infinite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
