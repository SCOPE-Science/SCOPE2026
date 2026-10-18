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

# Verification record

The executable `verify_sparse_complement.py` is a dependency-free Python 3 script. Run it from the directory containing this file and the Python script using `python3 verify_sparse_complement.py`. It rederives formal concepts using Galois derivations and maximal independent sets by brute force; it does not reuse the analytic tree expression for these checks. Every incidence matrix on bipartitions of sizes from 1 through 4 with product at most 9 is examined (1,226 instances). The same script independently enumerates small colored bipartite trees and compares direct MIS enumeration with the three-state tree dynamic program; size-2/3/4 coefficient sums are checked. Expected output begins `VERIFY_OK: exact FCA/MIS identities 1226`.

The asymptotic component-frequency concentration and exponential-tail control are proved in RESULT.md and are **not** certified by the finite computations. No external independent audit has been performed. Literature and previous-claim comparisons are scientific overlap checks, not mathematical certification.
