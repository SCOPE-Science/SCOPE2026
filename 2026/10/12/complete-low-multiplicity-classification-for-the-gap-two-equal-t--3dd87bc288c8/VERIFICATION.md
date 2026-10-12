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

The proof in `RESULT.md` is symbolic and unbounded. The accompanying `verify.py` is an independent finite regression check, not a substitute for the proof.

It performs the following checks.

1. It verifies the algebraic identities
\[
rs=pq+2,\qquad r+s=p+q+2
\]
for a grid of odd parameter pairs \(3\le A<B\).

2. It constructs exact smallest-prime-factor data through \(10^6+2\), evaluates \(\Omega\) and \(\varphi\) from factorizations, and exhaustively finds all \(n\le10^6\) satisfying
\[
\Omega(n),\Omega(n+2)\le2,\qquad \varphi(n)=\varphi(n+2).
\]

3. Every nonexceptional hit is required to be a product of two distinct odd primes at both endpoints and to invert to a unique pair \((A,B)\) that regenerates all four factors.

The resulting output is stored in `verification_output.txt`. The finite cutoff establishes no statement beyond the scanned range; all unbounded exhaustiveness comes from the proof.
