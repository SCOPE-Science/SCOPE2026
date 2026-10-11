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
For the complete all-parameter proof see `RESULT.md`.

Critical steps checked independently:
- every stable-set vertex is \(\mathbf1_S\), with \(S\subseteq V_i\) for one class;
- the scalar defining function decreases from \(k>2\) to zero, giving exactly one threshold \(h\);
- setting \(p_i=(1-h/a_i)_+/2\) yields \(\sum_i p_i=1\);
- the squared vertex distances are
  \[\|\mathbf1_S-c\|^2=B+|S|(1-2p_i);\]
- \(a_i(1-2p_i)=\min\{a_i,h\}\), so precisely the claimed full-class vertices are contacts;
- the positive-weight contacts average to \(c\), and the variance identity produces the strict lower bound \(R^2+\|y-c\|^2\) for every competing center \(y\ne c\);
- the active-set root is \(h=(m-2)/(\sum_{i\in I}1/a_i)\), giving exact rational squared radius;
- adjoining any class of size no larger than \(h\) preserves the root and radius.

`verify.py` exhaustively enumerates integer part-size profiles with bounded total order and all their stable-set indicator vertices using `fractions.Fraction`. It checks the active-set formulas, contact equality cases, the weighted-average certificate, and sample exact-radius plateaus. These finite tests are corroborative and are not an exhaustive infinite-parameter proof.
