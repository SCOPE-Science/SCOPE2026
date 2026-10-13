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
For an admissible transition/transversion signature \((t,v)\) of length \(L\), define
\[
F_L(t,v)=(L-2t-v)^2(L-2v).
\]
Then
\[
K=-\frac14\log\left(\frac{F_L(t,v)}{L^3}\right),
\]
so K2P ordering is the reverse of exact integer \(F_L\)-ordering.

The embedded `verify_k2p_pdistance_boundary.py` enumerates every admissible signature and every unordered pair for
\[
1\le L\le9.
\]
It verifies no weak-order difference through length \(2\), the first tie split at length \(3\), no strict reversal through length \(8\), and exactly one strict reversing pair at length \(9\):
\[
(2,3)
\quad\text{versus}\quad
(4,0).
\]

It also checks the explicit common-reference sequences and exact integers
\[
F_9(2,3)=12,
\qquad
F_9(4,0)=9.
\]

Run:

`python3 verify_k2p_pdistance_boundary.py`

The first output line must be:

`VERIFY_OK`
