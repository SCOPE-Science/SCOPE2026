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

# Reproduction

Execute `python3 verify.py` in the same directory. Only Python's standard library is used; no network services, external data, randomness, or nondeterministic truncation are involved. The computation enumerates all even permutations of six letters, obtains every conjugacy class, checks all 360 partners for each of seven representatives, and explicitly checks the 30 \(S_4\) subgroups and their generating pairs.

The expected terminal marker is `VERIFY_OK`; all mathematical assertions in the checker must succeed before it is printed. Checked derived-length multiplicities for ordered pairs at lengths 0, 1, 2, 3, and infinity are `1, 2519, 16920, 6480, 103680`. These total 129600, the square of the group order 360. The checker also requires exactly 30 distinct copies of \(S_4\) and 216 ordered generating pairs in each.

The exhaustive finite proof relies on the fact that the breadth-first closure computes *all* products of subgroup generators, and the second closure uses *all* commutators, as documented in RESULT.md. The verification does not assert results for larger alternating groups and does not substitute a numerical sample for a theorem about all finite groups.

Independent audit status: not performed.
