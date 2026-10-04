# Rank formula for Ramanujan matrices with square-zero radical

## Finding
Let \(R\) be a finite commutative ring and let \(C_R\) denote the generalized Ramanujan matrix defined by Nguyen–Tân–Treviño. Assume that its Jacobson radical satisfies \(J(R)^2=0\). Decompose
\[
R\cong\prod_{{i=1}}^s R_i
\]
into finite local rings. Let \(f\) be the number of factors that are fields and \(e=s-f\) the number of nonfield factors. Then
\[
\operatorname{{rank}}_{{\mathbb Q}} C_R=2^f3^e.
\]
The same rank holds over \(\mathbb C\).

For a nonfield local factor \(A\) with maximal ideal \(\mathfrak m\), residue field \(k=A/\mathfrak m\) of order \(q\), and \(d=\dim_k\mathfrak m\), set
\[
P=\frac{{q^d-1}}{{q-1}}.
\]
Then \(C_A\) has dimension \(P+2\), rank \(3\), and nullity \(P-1\). With the columns ordered as the unit orbit, the \(P\) nonzero \(\mathfrak m\)-orbits, and the zero orbit, its kernel is
\[
\left\{{(0,v_1,\ldots,v_P,0):\sum_{{j=1}}^P v_j=0}}\right\}.
\]

## Assumptions and scope
The ring is finite and commutative. Rank is taken over \(\mathbb Q\), equivalently over \(\mathbb C\), because the matrix has integer entries. The matrix \(C_R\) is the matrix in Theorem 3.1 of Nguyen–Tân–Treviño, indexed by associate classes under multiplication by units. The hypothesis is exactly \(J(R)^2=0\); no assertion is made for higher Loewy length.

For a local nonfield factor, \(\mathfrak m\ne0\) and \(\mathfrak m^2=0\). The action of \(A^\times\) on \(\mathfrak m\) factors through \(k^\times\), so the nonzero orbits are exactly the one-dimensional \(k\)-subspaces of \(\mathfrak m\). Thus there are \(P\) such orbits.

## Proof
For a finite local nonfield ring \(A\) with \(\mathfrak m^2=0\), write \(h=q^d=|\mathfrak m|\). The unit orbit is one class, the nonzero elements of \(\mathfrak m\) give \(P\) projective-direction classes, and zero gives one class. Hence the matrix has size \(P+2\).

For every nonzero \(x\in\mathfrak m\), one has \(\operatorname{{Ann}}_A(x)=\mathfrak m\): inclusion of \(\mathfrak m\) follows from \(\mathfrak m^2=0\), while no unit can annihilate a nonzero element. The generalized Möbius values used in the source are
\[
\mu(A)=0,\qquad \mu(A/\mathfrak m)=-1,\qquad \mu(A/A)=1,
\]
and
\[
\varphi(A)=h(q-1),\qquad \varphi(A/\mathfrak m)=q-1,\qquad \varphi(A/A)=1.
\]
Substitution into the entry formula of Theorem 3.1 gives
\[
C_A=
\begin{{pmatrix}}
0 & -h\mathbf 1_P^\top & h(q-1)\\
-\mathbf 1_P & (q-1)J_P & (q-1)\mathbf 1_P\\
1 & \mathbf 1_P^\top & 1
\end{{pmatrix}}.
\]
All \(P\) projective-direction columns are therefore identical, so \(\operatorname{{rank}} C_A\le3\). The submatrix formed by the unit column, one projective-direction column, and the zero column, and by one row of each of the three row types, is
\[
\begin{{pmatrix}}
0&-h&h(q-1)\\
-1&q-1&q-1\\
1&1&1
\end{{pmatrix}},
\]
whose determinant is \(-hq^2\ne0\). Hence \(\operatorname{{rank}} C_A=3\). Since the only repeated columns are the \(P\) projective-direction columns and the displayed three columns are independent, the kernel is exactly the stated sum-zero space and has dimension \(P-1\).

If \(F\) is a field of order \(q\), the same source formula gives
\[
C_F=\begin{{pmatrix}}-1&q-1\\1&1\end{{pmatrix}},
\]
which has rank \(2\). Every finite commutative ring is a product of finite local rings, and the source proves that under such a product decomposition the Ramanujan matrix is, up to ordering, the Kronecker product of the local matrices. Since matrix rank is multiplicative under Kronecker products, the global rank is \(2^f3^e\).

## Verification
The proof above is symbolic and covers every finite commutative ring satisfying the stated radical hypothesis. A separate exact-rational checker reconstructs the displayed local matrices for residue-field orders \(2,3,4,5,7\) and dimensions \(1,2,3\), verifies rank \(3\), repeated projective-direction columns, and independence of the three distinguished columns. It also checks four small Kronecker-product cases and the rank multiplication predicted by the theorem. The checker output begins `VERIFY_OK`; these finite checks are corroborative and are not used to replace the universal proof.

## Relationship to prior work
Nguyen–Tân–Treviño prove that \(C_R\) is nonsingular exactly when \(R\) is Frobenius and then explicitly ask what can be said about the rank of \(C_R\) in Question 3.4. Their nonsingularity criterion does not determine the rank in the singular cases. The theorem here answers that rank question on the natural first radical layer \(J(R)^2=0\), including arbitrary finite products of local factors.

The formula is consistent with their Frobenius criterion. A nonfield local square-zero factor is Frobenius exactly in the one-dimensional socle case \(d=1\); then \(P=1\), so the local matrix has size and rank \(3\). For \(d>1\), the matrix dimension grows with the number of projective directions but its rank remains \(3\).

Schlage-Puchta's determinant theorem concerns the classical divisor-indexed Ramanujan matrix for \(\mathbb Z/n\mathbb Z\) and establishes full rank in that classical setting; it does not give the rank of the generalized matrix for non-Frobenius square-zero rings.

## Limitations
The result does not determine ranks for local factors with \(\mathfrak m^2\ne0\), and it does not classify kernels of arbitrary products beyond the rank formula. The literature comparison found no statement implying this square-zero rank formula, but terminology for generalized Ramanujan matrices varies, so an unindexed equivalent formulation remains a residual originality risk.

## References
1. Tung T. Nguyen, Nguyen Duy Tân, and Enrique Treviño, “Supercharacter theory and applications to Ramanujan sums over a finite Frobenius ring,” arXiv:2609.30407v1, first posted 2026-09-24. See Theorems 3.1–3.3, equation (3.2), and Question 3.4.
2. Jan-Christoph Schlage-Puchta, “A determinant involving Ramanujan sums and So’s conjecture,” Archiv der Mathematik 117 (2021), DOI 10.1007/s00013-021-01643-8.
3. Tung T. Nguyen and Nguyen Duy Tân, “On gcd-graphs over finite rings,” arXiv:2503.04086v1.
