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

The proof was checked symbolically at the following points.

For fixed \(\alpha>0\), the implication \(p>\alpha n\Rightarrow p>\sqrt n\) holds for all \(n>\alpha^{-2}\), so every higher term in Legendre's formula vanishes. The equivalence \(\lfloor n/p\rfloor=j\iff n/(j+1)<p\le n/j\) fixes the interval boundaries exactly. Intersecting those cells with the target window gives the coefficient in `RESULT.md`, and the prime number theorem applies to only finitely many fixed scaled endpoints.

The embedded `verify.py` was replayed from the decoded package. It independently computes Legendre valuations, checks the exact cell regrouping in \(250\) finite cases, and evaluates the parity profile for \(h=2\), \(K=2\) through \(n=2{,}000{,}000\). The machine output is stored in `verification_output.txt`.

The finite checks do not prove the asymptotic and are not presented as exhaustive evidence for all parameters. The asymptotic proof depends on the classical prime number theorem in the form \(\vartheta(x)=x+o(x)\). No claim is made about a uniform error when the fixed parameters vary with \(n\).
