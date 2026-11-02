---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The morphism satisfies W_k=W_{k-1}W_{k-2}W_{k-2} and an alternating final-letter recurrence. The source proves by parity-aligned desubstitution that W_{k-2} occurs in W_k only at positions 0, 2^{k-1} and 3·2^{k-2}, for all k>=3. This supports absence and both proper-factor occurrences for the two boundary obstructions. The global forbidden families arise by iterating Psi(v)=mu(v) with first symbol removed, starting from 0000 and 1001; a hereditary inverse-morphism/parity argument proves absence while separate induction tracks positions of the truncated prefix/suffix occurrences at each level. Two initial-letter towers, distinct lengths, and the k=3 exceptional collision check establish pairwise distinct 2k-1 witnesses. Independently constructed W_k and tested the three-position lemma and all specified witness absences/prefix/suffix inclusions for k=3..10, giving 5,7,9,11,13,15,17,19 witnesses. These tests do not prove the all-k lower bound; the substitution induction is the proof. No general upper bound or full antidictionary enumeration is asserted.

## originality

PASS

Currie (2023) classifies good words avoiding the infinite period-doubling factor-language patterns by a desubstitution theorem. That covers global prohibited patterns but not the two finite-prefix boundary obstructions or the quantitative at-least-2k-1 count. Pinho et al. 2009 and Barton et al. 2014 define and compute minimal absent factors for arbitrary strings, not an all-level symbolic list for the period-doubling dyadic prefixes. Nearest published result on period-doubling prefix attractors evaluates a different statistic. Best-of-knowledge original constructive bound; equivalent finite-prefix formulas in unindexed automatic-word literature remain a risk.

## value

PASS

Minimal absent factors are the finite word’s antidictionary and are a standard measure of negative substring information. Showing at least logarithmically many explicit and structurally different obstructions in highly ordered dyadic prefixes, separated into hereditary global and endpoint-generated families, is a motivated all-scale structural result. It is not a claim of complete census and not merely a finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
