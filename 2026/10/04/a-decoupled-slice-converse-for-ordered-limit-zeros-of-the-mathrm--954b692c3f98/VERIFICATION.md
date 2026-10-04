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

The universal proof uses no finite computation. It relies on two exact formulas from arXiv:2609.28354v1 and the classical identity for negative integer zeta values.

For \(a,c\in\mathbb N_0\), the two detector values are
\[
P(a,c)=\zeta(-a)\zeta(-c),
\]
\[
R(a,c)=P(a,c)+\frac{(-1)^{c+1}}{c+1}\zeta(-a-c-1).
\]
Thus \(P(a,c)=R(a,c)=0\) is equivalent to \(a,c\ge1\) with \(a+c\) odd. If every ordered limit vanishes, then these two do, so the source conjecture's necessary condition follows on \(\ell_{12}=0\). No claim is made here that the condition forces all six ordered limits to vanish.

`verify.py` recomputes Bernoulli numbers with exact rational arithmetic and checks the two-detector equivalence for all \(0\le a,c\le40\). The recorded output is in `verification_output.txt`. This finite check is only corroborative; it does not certify the infinite theorem.

Limits: no claim is made for \(\ell_{12}>0\), for the all-six sufficient direction, or for rank greater than two.
