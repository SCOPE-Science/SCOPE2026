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

# Verification

The standalone `VERIFY_SPARSE.py` checker uses Python's standard library and passed 12,007 exact assertions. It enumerates all binary \(N\times N\) matrices with exactly \(N+1\) entries equal to one for \(N\in\{2,3,4\}\), retains strongly connected matrices, forms characteristic determinant polynomials by permutation expansion, and compares primitive zeta denominators to the proposed parameter family. It constructs the shared-path witness graph for every admissible primitive pair through \(N=7\), checking connectivity and exact determinant polynomials. It compares the exact period counts to the totient formula for every integer \(2\le N\le150\).

These are **finite consistency checks** only. The proof for every \(N\ge2\) is the deterministic-path graph decomposition, directed cycle determinant expansion, continuous-orbit-equivalence invariant calculation and totient pairing identity. The classical totient summatory error estimate is an established analytic-number-theory fact, not numerically certified here.

The standard-library execution command is `python3 VERIFY_SPARSE.py` from a directory containing the extracted standalone verifier. No external data files, network connection or nonstandard packages are required.
