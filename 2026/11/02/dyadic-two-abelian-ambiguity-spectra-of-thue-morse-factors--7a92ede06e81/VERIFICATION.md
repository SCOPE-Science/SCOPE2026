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

# Verification of the dyadic two-Abelian spectrum

The proof is in `RESULT.md`. The only external mathematical input is the established ordinary Thue–Morse factor count \(3N-2\) at lengths \(N=2^k\) (Greinecker, arXiv:1404.3906, introduction). This is needed to show that the full cut-and-join description of the factors has no hidden duplicates.

To reproduce the independent finite corroboration, place `checker.py` and this file in the same directory and run `python checker.py 10` with Python 3. No network, third-party library, or other file is needed. The checker builds the fixed point from the substitution and computes actual overlapping \(00\) and \(11\) counts on each distinct window. Its prefix length \(8N\) is exhaustive, since its eight level-\(k\) substitution blocks contain all four adjacent block types. It independently builds the cut-and-join representation and checks coverage and disjointness.

Checked exactly at all dyadic lengths from \(N=4\) through \(N=1024\). The complete distributions of class sizes (size: number of classes) were:

| \(N\) | Class-size distribution |
|---:|---|
| 4 | 1:6, 2:2 |
| 8 | 1:4, 4:2, 5:2 |
| 16 | 5:6, 8:2 |
| 32 | 5:4, 16:2, 21:2 |
| 64 | 21:6, 32:2 |
| 128 | 21:4, 64:2, 85:2 |
| 256 | 85:6, 128:2 |
| 512 | 85:4, 256:2, 341:2 |
| 1024 | 341:6, 512:2 |

Every literal signature table, factor count, and representation check passed. The full analytic proof includes the unrestricted quantifiers; checking nine finite levels does not establish them. The asymptotic parity split follows algebraically from the exact class sizes, not from numerical fitting. There has been no independent mathematical audit.
