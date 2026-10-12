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

The verification reconstructs the data directly from arXiv:2610.01276v1.

Burek defines
\[
A(z)=z^8+14z^4+1,\qquad
B(z)=z(z^4-1),\qquad
C(z)=z^{12}-33z^8-33z^4+1
\]
and uses
\[
A(2)=481,\qquad B(2)=30,\qquad C(2)=-4879.
\]
Proposition 7.1 describes each ordinary double point by
\[
J(v_0)=0,\qquad
t^4=\frac{C(v_0)}{-4879},\qquad
y=0,\qquad
x=\frac{3\cdot481^2C(v_0)}{-4879A(v_0)}t^2.
\]

Appendix A gives the section formulas \(P_j(u)\); the six resolution sections are
\[
P_1(2),\ P_2(2),\ P_6(2),\ P_1(2i),\ P_2(2i),\ P_6(2i).
\]
Appendix B lists the \(24\) values \(v_0\), one fourth root \(\tau\) for each, and one witnessing section for each of the four nodes over \(v_0\).

`artifacts/verify.py` uses only exact rational arithmetic in \(\mathbf Q(i)\). It first checks all \(24\) values satisfy \(J(v_0)=0\) and every displayed \(\tau\) satisfies
\[
\tau^4=C(v_0)/(-4879).
\]
It then forms all \(96\) pairs
\[
(v_0,i^k\tau),\qquad 0\le k\le3,
\]
reconstructs their node coordinates, and evaluates all six section coordinate formulas at every node.

The replay obtains
\[
N_1=44,\quad N_2=24,\quad N_3=16,\quad N_4=8,\quad N_5=4,\quad N_6=0.
\]
Every section contains \(32\) nodes. The nodes lying on exactly one section are distributed
\[
6,\ 6,\ 10,\ 6,\ 6,\ 10
\]
for
\[
P_1,\ P_2,\ P_6,\ P'_1,\ P'_2,\ P'_6.
\]
Thus each section has private nodes. The script also checks every subset of size at most \(5\) and confirms that none covers all \(96\) nodes, while all six do. The saved replay terminates with `VERIFY_OK`.

No floating-point computation is used. No conclusion is drawn about centers outside these six explicit section images.
