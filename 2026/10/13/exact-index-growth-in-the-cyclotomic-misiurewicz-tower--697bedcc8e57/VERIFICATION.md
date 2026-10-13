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

The proof establishes the universal index formula by local algebra and a regular Newton-polygon computation. The accompanying `verify.py` is a finite replay aid only.

It checks, for \(1\le k\le10\) and \(0\le s\le k+4\), the identity
\[
\nu_2\!\left(\binom{2^k}{m}\right)=k-\nu_2(m),
\]
constructs the lower Newton hull using exact rational slopes, checks every floor ordinate against
\[
\min\{\min(s,k),\,k-\lceil\log_2 m\rceil\},
\]
checks the resulting index sum \(2^k-2^{k-\min(s,k)}\), and verifies the midpoint valuation used in the residual-separability argument.

The stored output is:
`VERIFY_OK newton_cases=105 k_max=10 index_formula=OK residual_midpoints=OK`.

Finite replay does not establish irreducibility, local maximality, or the universal quantifiers; those are supplied by the proof in `RESULT.md`.
