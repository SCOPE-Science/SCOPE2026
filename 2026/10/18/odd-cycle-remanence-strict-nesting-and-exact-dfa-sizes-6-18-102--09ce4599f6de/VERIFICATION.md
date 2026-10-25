---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Definition uses all vertices both initial and accepting, + follows each edge orientation and - reverses. The displayed mapping C_{n+2}->C_n sends the cyclic image walk 0,1,...,n-1,0,1,0 along actual C_n edges; pullback of orientations proves Rem(C_{n+2}) subset Rem(C_n) for all n>=3. Strictness uses concrete three signed words and all lower masks/one higher rejecting mask. For exact finite sizes, enumerating 2^n masks, reachable subsets per mask, synchronous product and absorbing dead state is complete by BFS induction; deterministic Moore refinement ending in acceptance-respecting congruence counts distinct Myhill–Nerode classes. An independent reimplementation, not just stored checks.txt, recomputed (reachable,minimized)=(6,6),(24,18),(230,102),(8936,1098) for n=3,5,7,9 with respectively 3,8,25,88 refinement rounds, and confirmed the meaning of no extrapolation to other n. Source verify.py separately provides direct witness checks.

## originality

PASS

The originating work defines remanent languages and preexisting triangle/five-cycle observations. Novel assessment is exact Myhill–Nerode minima at 5,7,9 and strict C5>C7>C9 witnesses along with all-n two-step monotonicity. Full original Pujol manuscript inaccessible, so priority is best-of-knowledge with a material uninspected-source risk.

## value

PASS

The first contiguous four odd cycle orders are canonical test cases for remanent languages, especially beyond the triangle and five-cycle obstruction. Exact complete-DFA sizes escalate 6,18,102,1098 while language inclusions are strict; reproducible exhaustive minimization gives natural finite structural benchmarks, not an arbitrary instance or a false general formula. The all-n homomorphism gives a separate explanation of monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
