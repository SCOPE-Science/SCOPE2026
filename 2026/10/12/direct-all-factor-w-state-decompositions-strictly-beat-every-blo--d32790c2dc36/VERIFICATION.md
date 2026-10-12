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

For each nonempty block \(B\), set
\[
A_B=\sum_{i\in B}(d_i-2).
\]
The cited theorem gives the certified length
\[
U(B)=2^{|B|-1}(A_B+2)
\]
for \(|B|\ge2\), while for a singleton the same expression is \(d_i\), the exact rank of \(W_{d_i}\).

For disjoint nonempty \(I,J\), exact expansion yields
\[
\begin{aligned}
U(I)U(J)-U(I\cup J)
&=2^{|I|+|J|-2}\bigl((A_I+2)(A_J+2)-2(A_I+A_J+2)\bigr)\\
&=2^{|I|+|J|-2}A_IA_J.
\end{aligned}
\]
Because every \(d_i\ge3\), both sums \(A_I\) and \(A_J\) are positive. This proves strict improvement at every merge. Repeating merges proves the arbitrary-partition statement.

The initiating 18-page source was inspected at the definition of \(W_d\), the statement \(\operatorname{rk}(W_d)=d\), Theorem 1.1, Corollary 1.2, the comparison with earlier bounds, and the final remarks. The 2019 predecessor was inspected at Theorems 3.3 and 3.6. A finite randomized integer replay checked the displayed algebraic identity for thousands of sample degree tuples and splits; this was only a consistency check and is not part of the universal proof.

The proof makes no claim about exact nonsingleton tensor ranks or global optimality of the direct decomposition.
