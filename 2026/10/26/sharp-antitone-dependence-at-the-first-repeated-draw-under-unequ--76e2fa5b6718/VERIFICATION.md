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

For collision at time K=k and match index S=s, fixing repeated category i and enumerating the (k−1) other distinct prefix labels gives q_k=(k−1)! Σ_i p_i² e_(k−1)(p_-i), independent of s; kq_k sums to unity. With P(z)=Π(1+p_i z), B(z)/P(z)=Σ p_i/(z+1/p_i) is a Stieltjes sum with strictly negative derivative between distinct negative poles, yielding real negative zeros with repeated-weight factors by continuity. Newton’s inequalities for degree m−1 with factorial conversion give q_k²≥[(m−k+1)/(m−k)] q_(k−1)q_(k+1), uniform-sharp and strict for nonuniform weights. Strict q log-concavity implies all reverse-TP2 2×2 minors on triangular support (off-support zero cases included), and the rearranged covariance identity is negative for strictly increasing functions, including m=2. Independent rational exact collision path enumeration and all small rectangles corroborated finite cases.

## originality

PASS

Camarri–Pitman original full 2000 paper gives P(K=k)=k! Σ_A Π_A p_A, algebraically equal to k q_k, and analyzes repeat times and tree structures. Its inspected full original formulas do not supply this two-variable S/R reverse-TP2 order or real-rooted sharp Newton equality theorem, though the joint mass can be recovered by marking the match index. Rathie–Zörnig 2003 addresses unimodality and uniform birthday-law extensions, not the full arbitrary-weight two-variable order. Stein 1990 explicitly concerns Newton identities for generalized birthdays and remains a real priority uncertainty (full report inaccessible). No negative novelty claim based only on search absence.

## value

PASS

Reverse-TP2 is a strong distribution-wide dependence ordering under every unequal positive categorical law, not just a covariance at one parameter. The full joint law, sharp coefficient inequality and rigid equality case provide useful natural structure for sampling/collision processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
