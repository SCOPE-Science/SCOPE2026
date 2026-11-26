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

Fix the phase at the smallest point to zero. With the time-zero bit removed, each next row is a translate of the previous prefix, so the candidate phases are either empty or a coset of the prefix stabilizer, of order at most gcd(n,i) for a prefix of size i. In prime-power length, digit reversal makes each aligned block of p^r indices a coset of the subgroup of size p^r, giving exactly the maximal stabilizer at each prefix. Translating the suffix by a stabilizer element preserves distinctness and every signature row. Each later required subgroup either lies inside the current subgroup, so both pieces of the later prefix remain invariant, or contains it, so the later prefix itself is unchanged. Successive phase differences recover the chosen shifts; the product is attained. At mixed-prime length, attaining the product forces every branching bound to be met, in particular at prefix sizes p<q for two distinct prime divisors. Those prefixes would be the corresponding subgroups because they contain zero; the required inclusion is impossible. Summing valuations gives the stated exponent and the numerical examples, including the prime boundary k=1.

## originality

PASS

Prime rigidity, composite nonuniqueness, and prime-case cyclic shift reconstruction have clear predecessors. The checked evidence did not cover the universal extremal product together with its exact prime-power saturation classification. A later exact composite-fiber family counts particular fibers, not the worst case.

## value

PASS

Prior work made the extent of ambiguity a natural continuation of prime rigidity. A sharp universal bound and an arithmetic criterion for attaining it quantify how much reconstruction can fail, rather than giving another ambiguous pair. The distinction between simultaneously attainable prime-power stabilizers and incompatible mixed-prime stabilizers explains the phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
