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

The finite search space is justified symbolically before enumeration. For odd \(n\) with \(\Omega(n)=5\) and \(\sigma(n)\ge2n\), support has size \(3,4\), or \(5\). Exact Euler-factor bounds reduce these cases respectively to support \(\{3,5,7\}\), to largest prime at most \(103\), and to squarefree support beginning \(3,5,7\) with largest prime at most \(383\).

`verify.py` regenerates every candidate from those finite ranges and retains exactly \(121\) nondeficient integers. For each one it computes \(H(n)=(\sigma(n)-2n)/2\). A \(\{-1,1\}\)-presentation with exactly \(k\) negative coefficients is equivalent to a set of \(k\) distinct nontrivial proper divisors summing to \(H(n)\). The checker reads `spectrum.csv`, verifies the stored size-\(k\) witness, and exhaustively tests every subset of smaller size. It then asserts the histogram \(17,1,88,0,15\) and the exact fifteen cases with minimum five.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK boundary=121 spectrum=17,1,88,0,15 max_negative=5 extremals=15`

No floating-point arithmetic, probabilistic primality test, timeout inference, or unbounded computation is used. The checker establishes only the stated \(\Omega(n)=5\) theorem.
