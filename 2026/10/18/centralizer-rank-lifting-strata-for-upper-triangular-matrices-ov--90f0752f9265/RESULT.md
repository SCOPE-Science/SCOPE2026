# Centralizer-rank lifting strata for upper triangular matrices over dual numbers

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), \(R=k[\varepsilon]/(\varepsilon^2)\), and \(A=\operatorname{UT}_3(R)\), the associative algebra of upper triangular three-by-three matrices. For \(T\in A\), let \(r(T)=\operatorname{rank}_k(\operatorname{ad}_T)\), where \(\operatorname{ad}_T(S)=TS-ST\) on the twelve-dimensional \(k\)-space \(A\). Every rank from zero through six occurs. The number \(c_j(q)=|\{T\in A:r(T)=j\}|\) is given exactly by

\[
\begin{aligned}
c_0(q)&=q^2,\\
c_1(q)&=q^2(q-1),\\
c_2(q)&=3q^3(q-1)(q+1),\\
c_3(q)&=q^3(q-1)(q^3+4q^2-4q-2),\\
c_4(q)&=q^4(q-1)(6q^3-3q+2),\\
c_5(q)&=q^7(q-1)^2(3q+5),\\
c_6(q)&=q^8(q-1)(q^3+q^2-2q-1).
\end{aligned}
\]

In particular, if two elements of \(A\) are independently uniform, their commuting probability is
\[
\Pr(TS=ST)=\frac{q^5+3q^4+3q^3-6q^2-3q+3}{q^{11}}.
\]

The rank-at-most-two reduction locus controlling these formulas is a union of three irreducible three-dimensional components in a five-dimensional affine parameter space. The intersections of these components have different first-order lifting counts; this accounts for the two distinct rank-five contributions.

## Assumptions and scope
All fields are finite fields of arbitrary characteristic, including characteristic two. The rank is a **field-linear** rank on the underlying \(k\)-space, not the rank of a matrix over \(R\); the latter need not be a single integer. The algebra has cardinality \(q^{12}\). The theorem concerns elements of the whole triangular algebra (not only its units), with the additive commutator and not group commutation. The geometric component statement is set-theoretic; no assertion of reducedness or scheme-theoretic multiplicity is made for the minors ideal.

## Proof
Write the diagonal entries of \(T\) as \(d_1,d_2,d_3\) and its upper off-diagonal entries as \(u=T_{12}\), \(v=T_{23}\), \(w=T_{13}\). Put \(a=d_1-d_2\) and \(b=d_2-d_3\). If the tested matrix has upper off-diagonal entries \(y_{12},y_{23},y_{13}\) and diagonal differences \(s=s_1-s_2\), \(t=s_2-s_3\), the three upper off-diagonal entries of its commutator with \(T\) are the image under the following \(R\)-linear map:
\[
M(a,b,u,v,w)=
\begin{pmatrix}
a&0&0&-u&0\\
0&b&0&0&-v\\
-v&u&a+b&-w&-w
\end{pmatrix}.
\]
The common diagonal of \(T\) is arbitrary and contributes a factor \(|R|=q^2\) to every count. The two diagonal differences of the tested matrix are independent variables over \(R\); the common diagonal is in the kernel. Hence \(r(T)\) is exactly the \(k\)-linear rank of \(M\colon R^5\to R^3\).

**Reduction stratification.** Consider the same matrix over \(k\). Its rank is zero only when all five parameters vanish, and it has rank one precisely when \(a=b=u=v=0\) and \(w\ne0\). The rank-two cases, mutually disjoint as written, are:

1. \(a=u=0\), \((b,v)\ne(0,0)\), and \(w\) arbitrary;
2. \(b=v=0\), \((a,u)\ne(0,0)\), and \(w\) arbitrary;
3. \(a\ne0\), \(b=-a\), \(aw+uv=0\).

Indeed the first two rows are linearly independent when both are nonzero; in that case the third row can depend on them only if \(a+b=0\). If \(a=0\), the nonzero \(u,v\) give independent third-row coordinates, forcing rank three. If \(a\ne0\), dependence is equivalent to \(aw+uv=0\). When exactly one of the first two rows is zero, the third row necessarily adds one rank. Thus the numbers of residue points at ranks \(0,1,2,3\) are respectively
\[
1,\quad q-1,\quad 3q^3-q^2-2q,\quad q^5-3q^3+q^2+q.
\]
Set-theoretically, the rank-at-most-two determinantal locus has the irreducible components \(V(a,u)\), \(V(b,v)\), and \(V(a+b,aw+uv)\). They all have dimension three. The last component is irreducible because \(aw+uv\) is irreducible in \(k[a,u,v,w]\) (its coefficients as a polynomial in \(w\) are coprime). Pairwise intersections of the first two with the third contain the rank-two loci responsible for the exceptional lift counts.

**First-order lifting rule.** Every parameter over \(R\) has a unique expression \(z_0+\varepsilon z_1\). For \(M=M_0+\varepsilon M_1\), elementary row and column operations over \(R\) first isolate \(r=\operatorname{rank}_k(M_0)\) unit pivots. On the remaining block, reduction is zero and the first-order coefficient is a \((3-r)\)-by-\((5-r)\) matrix \(K\) over \(k\). Therefore
\[
\operatorname{rank}_k(M:R^5\to R^3)=2r+\operatorname{rank}_k(K).
\]
For rank-three residues all \(q^5\) lifts have full \(k\)-rank six. At the zero residue, all lifts have the residue-rank distribution just calculated, because \(M=\varepsilon M_1\).

At a rank-one residue \((0,0,0,0,w_0)\), \(w_0\ne0\), elimination of the unit pivot reduces \(K\) to a two-by-three matrix
\[
\begin{pmatrix}a_1&0&-u_1\\0&b_1&v_1\end{pmatrix},
\]
with one irrelevant first-order parameter \(w_1\). Among the \(q^4\) choices of \((a_1,b_1,u_1,v_1)\), the rank-zero, rank-one and rank-two multiplicities are, respectively,
\[
1,\qquad3q^2-2q-1,\qquad q^4-3q^2+2q.
\]
For rank one, this follows by separating \(a_1\ne0\), \(b_1\ne0\), and \(a_1=b_1=0\); rank zero occurs only at the origin.

At a rank-two residue, \(K\) is a single row. Its vanishing is equivalent to the first-order deformation annihilating the differentials of every three-by-three minor. Denote the number of independent such linear conditions by \(\nu\). The nonzero minors of \(M\), up to sign, are products drawn from
\[
\begin{gathered}
ab(a+b),\;b(aw+uv),\;a(-bw+uv),\;av(a+b),\\
v(aw+uv),\;bu(a+b),\;u(-bw+uv),\;uv(a+b).
\end{gathered}
\]
Direct differentiation yields \(\nu=2\) for each rank-two residue of the following kinds: \(a=u=0,b\ne0\); \(b=v=0,a\ne0\); and \(a\ne0,b=-a,aw+uv=0\). Their counts total \(3q^2(q-1)\). The remaining rank-two residues have \(\nu=1\): \(a=b=u=0,v\ne0\) or \(a=b=v=0,u\ne0\), with arbitrary \(w\), altogether \(2q(q-1)\) points. For each such residue, exactly \(q^{5-\nu}\) of its \(q^5\) lifts have first-order row \(K=0\), hence rank four; the others have rank five.

**Summation.** Before multiplying by \(q^2\) for the common diagonal, the generating polynomial for \(k\)-linear ranks is
\[
\begin{aligned}
H_q(t)={}&1+(q-1)t+(3q^3-q^2-2q)t^2+(q^5-3q^3+q^2+q)t^3\\
&+q(q-1)\left[t^2+(3q^2-2q-1)t^3+(q^4-3q^2+2q)t^4\right]\\
&+3q^2(q-1)\left[q^3t^4+(q^5-q^3)t^5\right]\\
&+2q(q-1)\left[q^4t^4+(q^5-q^4)t^5\right]\\
&+q^5(q^5-3q^3+q^2+q)t^6.
\end{aligned}
\]
Expanding \(q^2 H_q(t)\) gives the seven displayed formulas for \(c_j(q)\), and their sum is \(q^{12}\). Since every \(T\) has exactly \(q^{12-r(T)}\) commuting partners, dividing \(\sum_j c_j(q)q^{12-j}\) by \(q^{24}\) gives the stated commuting probability. Each proof step is uniform across all finite-field characteristics.

## Verification
The attached `verify.py` performs direct elimination on the six-by-ten \(k\)-matrix describing \(M:R^5\to R^3\). It enumerates every one of the \(q^{10}\) choices of the five dual-number parameters for \(q=2\) and \(q=3\); a factor of \(q^2\) accounts for the free common diagonal. It compares the seven observed rank frequencies with the theorem's formulas and checks their sum. Expected results, for ranks zero through six, are \((4,4,72,112,704,1408,1792)\) when \(q=2\) and \((9,18,648,2646,25110,122472,380538)\) when \(q=3\). The program prints `VERIFY_UT3_DUAL_OK` on success.

## Relationship to prior work
Avni, Onn, Prasad and Vaserstein study similarity classes and centralizers in **full** three-by-three matrix rings over local principal ideal rings (arXiv:0708.1608, initial public submission 12 August 2007). Their object is \(M_3(R)\) under \(\mathrm{GL}_3(R)\)-similarity, whereas this theorem is a complete elementwise adjoint-rank census for the proper algebra \(\operatorname{UT}_3(R)\), whose centralizers are taken *inside that algebra*. Neither the full-matrix similarity classification nor its stabilizer sizes yields the present distribution by direct specialization.

Kaur, Sharma and Singh study branching and commuting probabilities of **invertible** triangular matrix groups over finite fields (arXiv:2006.01493, 2 June 2020); their coefficient ring is a field, not a dual-number ring. A separately available finite-field census of additive commutator fibers in \(\operatorname{UT}_3(\mathbb F_q)\) has commuting probability \((q^4+3q^3-2q^2-2q+1)/q^7\); this establishes the base-field case, not the rank-lift stratification over \(R\). The new information is the lifting distribution controlled by the singular rank-two reduction locus.

## Limitations
No analogous all-length formula is proved for \(k[\varepsilon]/(\varepsilon^m)\) when \(m\ge3\), or for non-split finite chain rings. The component decomposition is a set-theoretic statement and does not address determinantal scheme multiplicities. Exhaustive computational checks are restricted to two prime fields; the uniform result relies on the algebraic argument. No independent mathematical audit or external certification has been performed. A specialized source not located through the documented comparisons might contain an equivalent distribution.

## References
- N. Avni, U. Onn, A. Prasad and L. Vaserstein, *Similarity classes of three-by-three matrices over a local principal ideal ring*, arXiv:0708.1608 (initial public release 2007-08-12), https://arxiv.org/abs/0708.1608 .
- D. Kaur, U. B. Sharma and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493 (2020-06-02), https://arxiv.org/abs/2006.01493 .
