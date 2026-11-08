---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For K_{r,s} with r,s>=3, a subset of shore occupancies (a,b) double-dominates iff a,b>=1, (a=r or b>=2), and (b=s or a>=2). An optimal partition has excess e=r+s-k=min(r-1,4). The proof bounds e using available nonsingleton vertices and two necessary partner types; for r>=6, e=4 forces exactly two distinct (1,2)/(2,1) bridge triples. For r<=5 and sufficiently large s, a B singleton forces a whole-A or split A hub, except the r=5 bridge pair. Nine remaining finite (r,s) are exhaustively decided by all multisets of occupied block types totaling exact excess, with forced singleton residues; they are not extrapolated. Labeled selection yields 1_{r<=5}(1+s sum_{a=2}^{r-1}binom(r,a)) + 1_{r=s<=5}(1+r sum_{b=2}^{s-1}binom(s,b)) +1_{r>=5}9 binom(r,3)binom(s,3). Independent profile enumeration and orbit-count arithmetic confirmed K_{3,3}=20, K_{3,5}=16, K_{4,4}=82, K_{5,5}=1152, K_{5,8}=5241, K_{6,6}=3600, K_{6,8}=10080.

## originality

PASS

Henning–Mojdeh 2025 Theorem 6 established the optimal number of blocks, and exhibits hub/bridge witnesses; that scalar result and those examples are genuine prior coverage, not new. The present exact **all** maximizing partition classification and vertex-labeled counts do not follow from knowing one sharp construction or the scalar maximum. Golmohammadi 2024 precursor makes a contradictory overgeneralized scalar statement that the later theorem corrects; it is not coverage of a valid equality census.

## value

PASS

An exact equality-case and multiplicity classification refines a known extremal graph partition invariant: all optimal structures, not just one example, and combinatorially meaningful labeled counts for each bipartite shore size. The r=5 bridge/hub coexistence and r=6 transition explain a structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
