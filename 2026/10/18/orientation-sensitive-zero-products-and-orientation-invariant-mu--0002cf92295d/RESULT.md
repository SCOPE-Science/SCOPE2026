# Orientation-sensitive zero products and orientation-invariant mutual annihilation in truncated cycle algebras

## Finding

Let \(q\) be any prime power and let \(Q_s\) be a quiver whose underlying undirected graph is a simple cycle \(C_n\) with \(n\ge3\). Orient edge \(\{i,i+1\}\), read modulo \(n\), forward if \(s_i=+\) and backward if \(s_i=-\). In the finite associative algebra \(A_s=\mathbb F_q Q_s/J^2\), write
\[
Z_s(q)=|\{(x,y)\in A_s^2:xy=0\}|,\qquad H_s(q)=|\{(x,y)\in A_s^2:xy=yx=0\}|.
\]
Define the integer matrices
\[
D=\operatorname{diag}(1,q-1,q-1),\quad
W=\begin{pmatrix}q^2&q^2&q\\q&q&q\\q^2&q^2&q\end{pmatrix},\quad
M_+=WD,\quad M_-=W^{\mathsf T}D,
\]
\[
B=\begin{pmatrix}
q^2&q(q-1)&q(q-1)\\
q&q(q-1)&q(q-1)\\
q&q(q-1)&q(q-1)
\end{pmatrix}.
\]
**Theorem.** For every such \(q,n,s\),
\[
Z_s(q)=\operatorname{tr}(M_{s_1}\cdots M_{s_n}),\qquad
H_s(q)=\operatorname{tr}(B^n).
\]
The second count is therefore independent of the orientation. Indeed, for any finite simple graph \(G=(V,E)\), with \(Q\) any orientation of \(G\), the same mutual-annihilation count is
\[
H_G(q)=\sum_{S\subseteq V}\bigl(2(q-1)\bigr)^{|S|}
q^{\,|E|+|E(G[V\setminus S])|}.
\]
For a coherently directed cycle, set \(a=q(3q-2)\), \(b=q^2(q-1)^3\) and \(c=2q^2(q-1)^2\). Let \(\lambda_\pm\) be the roots of \(t^2-at-b=0\), and \(\theta_\pm\) the roots of \(t^2-at+c=0\). Then
\[
Z_{(+^n)}(q)=\lambda_+^n+\lambda_-^n,\qquad
H_s(q)=\theta_+^n+\theta_-^n.
\]
These algebraic-number expressions are integers; the roots are taken over the real numbers, not inside \(\mathbb F_q\). At length four, the exact orientation gap is
\[
Z_{+-+-}(q)-Z_{++++}(q)=
q^4(q-1)^3\bigl(q^5+3q^4+8q^3-8q^2-q+1\bigr)>0
\]
for every prime power \(q\ge2\). For \(q=2\), the respective counts are \(6928\) and \(5152\), while \(H_{+-+-}(2)=H_{++++}(2)=2176\). Each algebra has \(2^8=256\) elements in that example, so the ordered-pair sample size is \(2^{16}\).

## Assumptions and scope

The directed graph \(Q\) has precisely one arrow over each edge of a loopless simple graph \(G\); all paths of length at least two are killed by the ideal \(J^2\). The resulting algebra is unital, with basis \(\{e_v:v\in V\}\cup\{a_e:e\in E\}\) and \(\dim_{\mathbb F_q}A_Q=|V|+|E|\). We adopt the path multiplication convention \(e_u a_e=a_e=a_e e_v\) for an arrow \(e:u\to v\); all other vertex-arrow products vanish. Multiplying pairs \((x,y)\) is ordered: \(xy=0\) alone is not interchangeable with the simultaneous condition \(xy=yx=0\). No characteristic restriction beyond the existence of the field is needed. The cycle transfer expressions require \(n\ge3\); the general-graph mutual-annihilation sum allows isolated vertices.

## Proof

Write \(x=\sum_v d_ve_v+\sum_e b_ea_e\) and \(y=\sum_v h_ve_v+\sum_e c_ea_e\). For an arrow \(e:u\to v\), multiplication modulo \(J^2\) gives
\[
(xy)_{e_w}=d_wh_w,\quad (xy)_{a_e}=d_uc_e+b_eh_v,\quad
(yx)_{a_e}=h_ub_e+c_ed_v.
\]
Thus \(xy=0\) forces \(d_wh_w=0\) independently at every vertex. Each pair \((d_w,h_w)\) belongs to one of three types: \(0=(0,0)\), \(L=(d_w\ne0,h_w=0)\), or \(R=(d_w=0,h_w\ne0)\), with multiplicities \(1,q-1,q-1\), respectively. Given endpoint types \(\alpha\) at \(u\) and \(\beta\) at \(v\), the arrow equation for \(xy=0\) is a homogeneous linear equation in the two independent variables \((b_e,c_e)\). It has rank zero exactly when \(d_u=h_v=0\), and rank one otherwise. Consequently the counts of arrow-variable solutions, indexed by tail-row and head-column types in the order \((0,L,R)\), form the matrix \(W\) displayed above. All arrows decouple because products of two arrows are zero. For a cyclic orientation, the edge transfer is \(WD\) when forward and \(W^{\mathsf T}D\) when backward. The weight of every vertex is inserted once in the cyclic matrix product, so summing over the types proves the trace formula for \(Z_s\).

For simultaneous zero products, the arrow equations in the order \((b_e,c_e)\) have coefficient matrix
\[
\begin{pmatrix}h_v&d_u\\ h_u&d_v\end{pmatrix}.
\]
Its determinant is \(h_vd_v-d_uh_u=0\), since the already-imposed vertex constraints are \(d_wh_w=0\). This coefficient matrix has rank zero if and only if both endpoint types are \(0\), and rank one otherwise. Thus each edge contributes \(q^2\) when both endpoints are of type \(0\), and \(q\) otherwise, *independently of the direction of the edge*. For any finite simple underlying graph, collapse types \(L,R\) into a single active type, with combined multiplicity \(2(q-1)\). If \(S\subseteq V\) is the set of active vertices, exactly \(|E(G[V\setminus S])|\) edges have both endpoints inactive. The arrow-variable contribution is therefore \(q^{|E|+|E(G[V\setminus S])|}\), giving the graph sum. On a cycle, the three-state transfer matrix is the displayed \(B\), and hence \(H_s=\operatorname{tr}(B^n)\), independent of \(s\).

Direct determinants give
\[
\det(tI-M_+)=t\bigl(t^2-at-b\bigr),\qquad
\det(tI-B)=t\bigl(t^2-at+c\bigr).
\]
Since \(n\ge3\), taking traces of the respective powers gives the stated spectral expressions. Finally, multiply \(M_+\) and \(M_-\) in the two length-four words: expanding \(\operatorname{tr}(M_+M_-M_+M_-) - \operatorname{tr}(M_+^4)\) yields the displayed factored polynomial. For \(q\ge2\), the bracket equals \(q^2(q^3-8)+3q^4+8q^3-q+1\), which is strictly positive. This proves the strict orientation contrast for every finite field.

## Verification

Run the bundled standard-library program with \(\texttt{python3 checker.py}\). It directly enumerates the full multiplication table in small prime fields, and separately evaluates the transfer matrices; the two independently computed counts agree for \(q=2,3\) and several cycle orientations of lengths \(3,4,5\). Its final output is \(\texttt{VERIFY_OK}\). In particular, the exact ordered-pair counts for \(\mathbb F_2\) are \((Z,H)=(608,320)\) on the directed triangle, \((5152,2176)\) on the directed square and \((6928,2176)\) on the alternating square. Symbolic multiplication and factorization of the displayed matrices yield the characteristic equations and orientation-gap polynomial. The finite enumeration is a consistency check, not the proof for arbitrary \(q,n\); the proof is the local linear-algebra count and cyclic contraction above.

## Relationship to prior work

Shumyatsky and Vannacci (arXiv:2307.12633v1, 24 July 2023) introduce and study the zero-product probability of finite rings and give structural theorems in terms of large ideals and their products. Their Theorem 1.3 and Section 3 concern uniform bounds, not an enumeration of radical-square-zero cycle algebras or orientation effects. The probability studied here is the same invariant, \(Z_s(q)/q^{4n}\) on a cycle, but its exact orientation dependence is an additional question. Dolžan (2022) studies general finite-ring zero-product probabilities and reports exact semisimple values and general bounds; no claim that this full work lacks cycle formulas is made without its complete text. Green and Schroll (arXiv:2302.08169) study quotients of quiver path algebras defined by parallel-path differences, rather than zero-product pair counts. Earlier finite-ring zero-product studies for commutative rings and rings of matrices give context, but their ring families are different. Counts of commuting pairs (vanishing commutators) do not imply the more restrictive condition \(xy=0\), and certainly do not determine the simultaneous condition \(xy=yx=0\).

## Limitations

This is a theorem for finite fields and radical-square-zero path algebras of loopless quivers; it does not supply zero-product counts for untruncated path algebras or looped quivers. The general-graph closed sum applies only to mutual annihilation, whereas the explicit one-sided trace formula applies to oriented cycles. The orientation gap proved here is for the coherent and alternating orientations of \(C_4\), not a complete ordering of all orientations for every \(n\). The literature search cannot prove historical uniqueness; in particular the full text of Dolžan's closely themed 2022 paper was not available for a complete comparison.

## References

1. P. Shumyatsky and M. Vannacci, *Commuting and product-zero probability in finite rings*, arXiv:2307.12633v1 (first submitted 24 July 2023), https://arxiv.org/abs/2307.12633 .
2. D. Dolžan, *The probability of zero multiplication in finite rings*, Bull. Aust. Math. Soc. 106 (2022), 83–88, https://doi.org/10.1017/S0004972721001246 .
3. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169 (2023), https://arxiv.org/abs/2302.08169 .
4. S. M. S. Khasraw, *What is the probability that two elements of a finite ring have product zero?*, arXiv:1810.13312 (2018), https://arxiv.org/abs/1810.13312 .
