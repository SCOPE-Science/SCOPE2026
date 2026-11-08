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

# Finite mathematical verification

Run `python3 verify.py` using only the standard library. The companion `verification_output.txt` is the observed stdout from that execution.

The script constructs the fifteen nonempty subsets of \(\mathbb Z/4\mathbb Z\), validates every familywise multiplication identity, and forms the entire sumset multiplication table. By the symbolic proof in `RESULT.md`, any automorphism fixing the singleton unit group must commute with translations and preserve the five intrinsic orbit types. Exactly \(4\cdot2\cdot4=32\) permutations meet those necessary conditions while fixing the units. The checker enumerates all 32 and verifies that precisely four preserve all 225 ordered products. Composing those with the two group automorphisms gives eight distinct automorphisms; exactly two preserve subsets containing zero. It checks the explicit counterexample on \(\{0,1\}\).

The program does not enumerate all \(15!\) permutations; its exhaustive conclusion depends on the independently written symbolic argument showing that every automorphism belongs to the candidate class. It is finite corroboration, not independent audit or formal verification.
