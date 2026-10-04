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

The unrestricted proof is in `RESULT.md`.

The checker verifies the exact rational maxima for every exponent partition
used to prove \(\Omega(n)\ge5\), the odd-part maxima in the \(a=1\) case, and
the finite factor equations in the \(a=2\) and \(a=3\) branches.

It also computes \(\sigma(n)\) and \(\Omega(n)\) for every
\(1\le n\le10^6\) using a smallest-prime-factor sieve. Among triperfect
numbers in that range, the only value satisfying \(\Omega(n)\le5\) is
\(120\).

The finite sweep is corroborative only. The infinite theorem follows from the
symbolic inequalities and exhaustive exponent-pattern case split.
