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
The universal statement is proved analytically. The decisive checks are:

1. Character orthogonality gives \(\mathcal M_A(c)=\sum_d|R_d|^2\), with \(R_0=4\) and \(R_{-d}=\overline{R_d}\).
2. For four points and prime \(p\ge11\), a difference multiplicity \(3\) forces an affine four-term arithmetic progression, while the only otherwise possible three-doubled-class pattern would force \(p=7\).
3. One doubled class can be canceled without affecting the singleton lower bound; two doubled classes can be canceled simultaneously in both possible support geometries.
4. On a four-term progression, after phase normalization the only variable lower bound is
\[
(r-1)^2+r^2=2\left(r-\frac12\right)^2+\frac12,
\]
so the exact minimum fourth moment is \(19\).
5. `artifacts/verify.py` exhaustively checks the support-profile classification for several primes and replays explicit phase witnesses. These finite checks corroborate the formulas but do not replace the all-prime proof.
