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

# Finite computation and proof boundary

Execute `python3 verify.py` using Python 3 and standard library only. The program independently constructs all nonempty state subsets for the explicit binary automata at state counts \(3\) through \(10\), enumerates all Bob responses of lengths zero through \(k-1\) as their reachable subset images, and obtains winning regions and least worst-case Alice turn counts by attractor iteration. It compares all 60 pairs \((n,k)\) with \(1\leq k\leq n+1\) against the asserted threshold; `B` means Bob has a strategy to prevent synchronization, not an execution timeout. The program additionally checks the explicit two-token invariant, all short response branches of the three-turn winning strategy, the absence of length-one and length-two reset words, and the existence of the length-three reset word.

Recorded execution output is in `verification_output.txt`. These are finite checks for small automata, not an exhaustive verification of all state counts. The infinite statement rests on the universal direct argument in `RESULT.md`. No external independent audit or validation has been performed.
