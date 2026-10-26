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

# Reproducible finite checks and proof boundary

Execute `python3 verify.py` with the standard Python 3 library in this directory. The script checks the complete integer matrix identity \(P_n(B_n^2)=J_n\) for every odd \(n\) from \(3\) through \(41\), using direct matrix multiplication and exact binomial coefficients. It also computes digit-parity sums directly and checks the original scalar identity for \(n=3\), \(1\le x\le120\); \(n=5\), \(1\le x\le40\); and \(n=7\), \(1\le x\le12\). Its largest direct digit-enumeration endpoint is \(559872\).

Expected success output:

`VERIFY_OK: all odd transfer matrices n=3..41; direct digit tests: [(3, 120, 480), (5, 40, 10240), (7, 12, 559872)]`

The finite computations are reproducibility checks, not an exhaustive proof for all \(n\) or \(x\). The unrestricted theorem follows from exact digit concatenation, Fourier diagonalization, the binomial-root identity, and cancellation of consecutive parity contributions, as written in `RESULT.md`. No external proof checker or independent auditor was involved.
