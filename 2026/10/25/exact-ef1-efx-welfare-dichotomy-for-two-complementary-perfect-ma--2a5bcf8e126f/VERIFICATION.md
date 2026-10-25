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

# Reproduction and verification

Run `python3 check_spoc_cycles.py` using Python 3 standard library only. The included `spoc_cycles_check_output.txt` records output from the executed check. The checker enumerates all labeled ordered pairs of perfect matchings on 2, 4, 6, and 8 goods and, for each input, all complete two-agent allocations. It separately evaluates the EF-X predicate for every good, computes the true constrained optimum, reconstructs a cycle-balanced-or-one-gap solution and checks its welfare, coverage and all EFX inequalities.

The verified input counts by goods are 1, 9, 225, 11025, totaling 11260, with all four domains passing. Exact enumeration does not establish universal correctness; the arbitrary-size result rests on the alternating-cycle proof in RESULT.md. The code verifies the **strong** EFX convention requiring the envy inequality after deletion of every good in the other bundle, even when the deleted good has zero marginal value to the observer.

The proof's critical checks are: (1) welfare T forces perfect coverage by selected red/blue pairs; (2) an alternating cycle admits only its two monochromatic perfect-matchings, including common double-edge cases; (3) after excluding a largest half-length L, greedy whole-component assignment leaves count difference at most L; (4) x+y=L−1 admits a near-balancing choice; (5) selected red/blue arcs leave exactly two unassigned goods; (6) the final goods-count bounds make both EFX inequalities hold for each possible deletion. The four-good extremal obstruction is known prior work.

Independent audit: not performed. No external formal proof or independent certificate is asserted.
