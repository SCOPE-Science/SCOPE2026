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

Let a_j=b^j+c with integers b>=2,c>=−1. Each support diagonal is a matching. Union of first two matchings contains no alternating cycle because a two-step left-vertex move shifts by a fixed signed gap b−1. If c<b(b−2), for j>=1, a_(j+1)−2a_j=(b−2)b^j−c>0; every new matching edge has at most one previously incident endpoint, so attaching it cannot create a cycle. A finite cycle would be contained in a finite prefix. If c>=b(b−2), with q=b−1, a=c+1, the b+1 left vertices iq, b right vertices a−iq (i<b), and the final right vertex a+q are distinct and nonnegative, and four specified edge families assemble a 2(b+1)-cycle on first three support levels. At equality nonnegativity holds exactly, so cutoff is sharp. Published Theorem E of Zeng–Xue–Zeng transfers forestness to Abelian pattern Sturmian characteristic words. Independently checked 435 (b,c) pairs using exact union-find on first four support diagonals, bases 2..11 and offsets around thresholds; these checks are not the universal proof.

## originality

PASS

Full 2026 Zeng–Xue–Zeng original paper Theorem E characterizes the class by incidence-forest graphs. Its Proposition 7.12 in accessible version v3 supplies strict doubling as a sufficient criterion, with {3^j} example and {2^j} cycle, but does not establish the full iff translation cutoff or the new explicit cycles for all (b,c). The published Resultary note proves an overall logarithmic occurrence bound and the {2^j−1} extremizer; those inequalities do not classify all integer translations. Best-of-knowledge PASS with older incidence-graph terminology risk.

## value

PASS

A natural two-parameter deformation of geometric sparse supports undergoes an exact sharp quadratic-in-base transition from acyclic to cyclic sum-incidence. Complete classification and explicit small finite obstructions sharpen prior sufficient growth and density results, not mere renaming of the forest criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
