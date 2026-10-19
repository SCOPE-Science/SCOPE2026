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

The exact Fourier-Gram identity, three-by-three eigenvalue calculation, and strict extremal comparisons for \(N\ge8\), \(N=7\), and \(N=6\) are written out in `RESULT.md`. Positivity uses the ordinary three-node Vandermonde determinant. Taylor expansions establish the large-order law.

Run `python3 checker.py` in the same directory. This checker uses Python 3 standard library only, enumerates every three-element erasure set of \(\mathbb Z_N\) for \(6\le N\le36\), independently evaluates real Gram spectral radii from a trigonometric cubic root formula, and checks the sharp bound and exact equality masks. Additional large-order samples and all three \(N=6\) gap types are checked. Finite computations corroborate but do not establish the universal theorem. No independent external audit has been performed.
