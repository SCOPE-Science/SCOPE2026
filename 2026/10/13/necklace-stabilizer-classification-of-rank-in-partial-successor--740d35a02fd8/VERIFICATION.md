---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For a cycle letter a(i)=i+1 and partial successor b_A(i)=i+1 on A, i otherwise, shifts H(A) commute with both, forcing every image to have size at least h=|H|. On cyclic quotient of order m=n/h, B=A/H has trivial stabilizer. For every nonzero directed pair separation d choose u∈B, u+d∉B; applying a^t b decreases d by exactly one, so any pair merges within m(m−1) letters. At most m−1 merge rounds compress quotient to one; lifted image has exactly h states and bound m(m−1)². Primitive binary necklace Möbius inversion supplies N_{n,d}=Σ_{e|n/d}μ(e)2^{n/(de)} and fixed-weight N_{n,d,k}=Σ_{e|gcd(n/d,k/d)}μ(e)binom(n/(de),k/(de)), zero if d∤k. Direct independent reachable-subset BFS verified every 1020 active masks n=2..9, including periodic/all/empty boundary patterns. Infinite result follows from pair-merging proof, not enumeration.

## originality

PASS

General primitive automaton synchronization theorems and semiconstant/unitary-letter criteria cannot handle every composite-size periodic pattern or derive exact nonunit minimum rank. Kari–Ryzhikov–Varonka treat word length/rank bounds in broad circular automata but do not in inspected summary establish stabilizer equality and exact necklace counts. Möbius primitive necklace count is classical; new assertion is equality of machine rank and stabilizer for all A with induced classification.

## value

PASS

It determines the minimum transformation rank for an entire natural two-letter circular automaton family without a powerset search, identifies exactly when synchronizing, provides a constructive cubic reset bound in quotient size and exact rank/fixed-weight distributions. In particular, it handles nonprimitive periodic masks and composite cycles, a real structural gap beyond simple small-automaton examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
