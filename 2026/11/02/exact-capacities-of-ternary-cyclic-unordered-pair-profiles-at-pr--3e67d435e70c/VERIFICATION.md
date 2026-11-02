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

# Verification of the exact ternary unordered-pair profile capacity

The logical proof uses the undirected Eulerian circuit criterion, a parity decomposition of the three cross-edge counts, and exact enumeration of all disconnected possibilities for positive content. No infinite-domain claim depends on the finite verifier.

Run `python3 verify.py` from the directory containing this note. The program uses only the Python standard library. It directly enumerates every ternary word at lengths 3–11 and groups outputs by positive composition, totaling 165 compositions. It compares the exact histogram sets with the parity-parameterized graph enumeration and the coefficient formula. It also builds explicit Euler circuits for 2,427 eligible profiles with symbol counts 1–5 and verifies both the histogram and the prescribed content. For every integer composition \(m,m,m\) with \(1\le m\le150\), it compares the finite-sum coefficient formula with the stated cubic closed form.

Observed execution:
```
brute length 3 composition classes 1
brute length 4 composition classes 3
brute length 5 composition classes 6
brute length 6 composition classes 10
brute length 7 composition classes 15
brute length 8 composition classes 21
brute length 9 composition classes 28
brute length 10 composition classes 36
brute length 11 composition classes 45
PASS: direct exhaustive words length 3..11; compositions 165
PASS: Eulerian witnesses 2427
PASS: balanced formula m=1..150
```
All tests passed. Bounds are explicitly finite and do not certify absence of an equivalent older theorem. No independent scientific audit has been performed.
