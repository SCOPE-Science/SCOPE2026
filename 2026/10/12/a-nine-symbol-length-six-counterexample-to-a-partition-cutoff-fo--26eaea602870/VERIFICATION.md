---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read Construction 6 and Conjecture 1 in Stanovnik–Moškon–Mraz arXiv:2307.12593v2. For q=9,n=6 the strict cutoff i>1+6/10 forces R2=R3=R4=R5=empty, and recurrence forces code L1 R1^5, size a(9-a)^5, maximum 33,614 over all integers 1<=a<=8 (at a=2). Independently built the unrestricted explicit partition with L1={0,1}, R1={2,...,8}, R2={(0,2),(0,3)}, later Ri empty, obtained |Li|=(2,12,88,640,4656) and a literal set of exactly 33,872 distinct length-six words. For each proper length k=1..5 computed all prefixes and suffixes and confirmed disjoint sets (includes self-overlap). Thus some non-overlapping code exceeds every cutoff-representable code by 258; every maximum code also exceeds the cutoff and the conjecture is false. No exact optimum S(9,6) or smallest counterexample is claimed.

## originality

PASS

The original 2024 primary paper states the universal cutoff as Conjecture 1 and its tabulated exact cases concern q<=6; the counterexample at q=9,n=6 uses the paper’s own representation but violates the claimed existence of a cutoff-compatible maximum. An examined 2025 dissertation still states that conjecture rather than this refutation; a 2024 constrained-code paper addresses different restrictions. Resultary search returned no covered same q=9 cutoff refutation. Priority could nevertheless be affected by unindexed numerical datasets or subsequent work.

## value

PASS

This is a motivated, explicit refutation of a universal published conjecture about structure of maximum non-overlapping codes, not an arbitrary finite instance. The exact 258-word gap independently separates a concrete admissible code from every cutoff-compatible representation. It changes the status of a proposed algorithmic restriction in synchronization/DNA address coding even without computing S(9,6).

The dated certificate retains the supplied scientific assessment, sources and limitations.
