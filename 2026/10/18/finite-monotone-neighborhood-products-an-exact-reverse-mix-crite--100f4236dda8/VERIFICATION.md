---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The complete proof is in `RESULT.md`. The auxiliary `CHECK.py` uses Python's standard library and requires no external inputs. Execute `python3 CHECK.py` in the directory containing the checker. Its terminating success line is `EXACT_FINITE_T_PRODUCT_OK; 2x3 and 3x3 witnesses confirmed`.

For each ordered factor-size pair from one through three, the checker constructs **every** nonempty upward-closed family of subsets containing the distinguished zero. It evaluates **every** subset of the product carrier as the valuation of the sole propositional atom. It compares the directly evaluated rectangle modality with both directional iterated modalities. The output verifies the exact characterization for every considered neighborhood-family pair and verifies that the first failing carrier sizes are two by three, three by two, and (for a shared failure valuation) three by three.

The respective complete family-and-valuation configuration counts at factor sizes two by three and three by three are 640 and 12800. The checker also evaluates the two displayed example valuations independently, including a single shared valuation for the simultaneous obstruction.

Finite exhaustive computation here is not evidence of the theorem for larger finite carriers. The unrestricted implication uses an inclusion-minimal neighborhood and the finite intersection of all relevant vertical sections. The lower bounds use the fact that a nonempty reflexive monotone neighborhood family over at most two points is automatically intersection-closed. Neither fact depends on the enumerator. No external or independent audit was performed.
