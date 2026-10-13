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

Run `python3 verify.py` beside `certificate.json`.

The verifier treats both minimum-critical-exponent directive initializations \(a_1=1\) and \(a_1=3\). It reconstructs
\[
Q_0=1,\qquad Q_1=a_1+1,\qquad Q_N=2Q_{N-1}+Q_{N-2},
\]
checks the published Binet-type expression through index \(24\), and evaluates the exact specialized recurrence formula
\[
R_v(n+1)=n+3Q_{N+1}+Q_N.
\]

For high Pell scales it checks that the normalized values at the left and right endpoints converge to
\[
5+3\sqrt2
\quad\text{and}\quad
3+\sqrt2,
\]
respectively. It also samples \(101\) normalized positions across one large scale interval and checks the limiting continuous map.

The computations are regression evidence for the algebra and indexing. The complete accumulation interval follows from the proof in `RESULT.md`, using the exact source theorem and a subsequence argument.
