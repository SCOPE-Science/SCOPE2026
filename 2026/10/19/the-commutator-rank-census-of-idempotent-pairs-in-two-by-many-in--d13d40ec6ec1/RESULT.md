# The commutator-rank census of idempotent pairs in two-by-many incidence algebras

## Finding
Let \(q\) be any prime power and \(m\geq1\). Let \(P_{2,m}\) be the height-two poset with two minimal elements \(u_1,u_2\), \(m\) maximal elements \(v_1,\ldots,v_m\), and all relations \(u_i<v_j\). Write \(A=I(P_{2,m},\mathbb F_q)\). For an ordered pair of idempotents \((e,f)\in A^2\), its commutator \([e,f]=ef-fe\) lies in the \(2\)-by-\(m\) radical block and has matrix rank at most \(2\).

The following formulas determine the **complete commutator-rank distribution**. Set
\[
 a=1+3q^2,\quad b=2q(q+1),\quad h=1+2q^2+q^3,\quad
 c=q^3+q^2+2q,\quad d=3q^2+q.
\]
For \(j=0,1,2\), let \(N_j(q,m)\) count ordered pairs \((e,f)\) with \(e^2=e\), \(f^2=f\) and \(\operatorname{rank}([e,f])=j\). Then
\[
\begin{aligned}
N_0(q,m)&=4a^m+12b^m,\\
N_1(q,m)&=4(q+1)(h^m-a^m)+16(c^m-b^m)+8(d^m-b^m),\\
N_2(q,m)&=\bigl[2(1+q^2)^m+2(2q)^m\bigr]^2-N_0(q,m)-N_1(q,m).
\end{aligned}
\]
The previously available single-idempotent enumeration and the commuting-pair contribution \(N_0\) are contextual, not claimed separately as new. The positive-rank strata \(N_1,N_2\), with their three-color-pattern mechanism, supply the substantive additional information.

For every \(q\), rank two occurs exactly when \(m\geq2\). For fixed \(q\), the proportion of idempotent pairs with rank-two commutator tends to \(1\) as \(m\to\infty\). For example, when \((q,m)=(2,2)\), the three counts are \((2404,3648,672)\), adding up to \(82^2\).

## Assumptions and scope
The coefficient field is arbitrary finite \(\mathbb F_q\), including characteristic two; \(m\) is an integer at least one. The incidence algebra \(A\) consists of matrices
\[
\begin{pmatrix}D_2&M\\0&D_m\end{pmatrix}
\]
with diagonal matrices \(D_2,D_m\) and arbitrary \(M\in M_{2\times m}(\mathbb F_q)\). Its radical is precisely the off-diagonal block and has square zero. A commutator has zero diagonal, so its rank as a \((m+2)\)-square matrix equals its \(2\)-by-\(m\) block rank. All pairs are **ordered**; no quotient by conjugation or interchange is taken. We count the zero and identity idempotents.

## Proof
**1. A local two-bit rule.** For one idempotent \(e\), let \(\epsilon_x=e_{xx}\in\{0,1\}\) be the diagonal entry at vertex \(x\). For any relation \(u_i<v_j\), the equality \(e^2=e\) reduces, using radical square zero, to
\[
(\epsilon_{u_i}+\epsilon_{v_j}-1)e_{u_iv_j}=0.
\]
Consequently that off-diagonal entry is free in \(\mathbb F_q\) exactly when the two diagonal bits differ; otherwise it is zero. For \(f\) write the corresponding diagonal bits \(\phi_x\). Each vertex has a color \((\epsilon_x,\phi_x)\in\{0,1\}^2\). On one relation, if the endpoint colors have Hamming distance zero, one or two, the pair \((e_{uv},f_{uv})\) has respectively \(1,q,q^2\) possibilities.

The commutator entry equals
\[
[e,f]_{uv}=(\epsilon_u-\epsilon_v)f_{uv}-(\phi_u-\phi_v)e_{uv}.
\]
At Hamming distance zero or one it is automatically zero. At Hamming distance two it is an onto linear map from the \(q^2\) choices of \((e_{uv},f_{uv})\) to \(\mathbb F_q\), with exactly \(q\) preimages for each commutator value. This holds in every characteristic. Different relations contribute independent variables.

**2. Fix the colors on the two minimal vertices.** There are four ordered same-color pairs, eight ordered distinct pairs differing in one bit, and four ordered opposite-color pairs. For each maximal vertex the possible commutator column \(z\in\mathbb F_q^2\) receives a *weight* equal to its number of off-diagonal lifts, summed over the four possible colors of that maximal vertex. The weights are independent between maximal vertices:

* **Same bottom color (four choices):** the zero column has weight \(a=1+3q^2\), and every nonzero column has weight \(q^2\). Therefore the sum of weights of columns in any fixed line through zero is \(h=a+(q-1)q^2\), while the sum over all columns is \((1+q^2)^2\).
* **Adjacent bottom colors (eight choices):** the zero column has weight \(b=2q+2q^2\); each nonzero vector on either coordinate axis has weight \(q^2\); all vectors with both coordinates nonzero have weight zero. The two coordinate axes each have total weight \(c=b+(q-1)q^2\); the total weight is \(2q(1+q^2)\).
* **Opposite bottom colors (four choices):** the zero column again has weight \(b\); each nonzero vector on either coordinate axis has weight \(q\); vectors off the coordinate axes have weight zero. The axes each have weight \(d=b+(q-1)q\); the total weight is \(4q^2\).

For clarity, the first weight line follows because a maximal vertex of the same bottom color gives only a zero column with weight one; either of the two adjacent colors gives only zero with weight \(q^2\); and the opposite color gives every column with weight \(q^2\). In the adjacent and opposite cases the nonzero columns occur on separate coordinate axes; their weights follow directly from the Hamming-distance-two rule in step 1.

**3. Count matrix ranks.** For independent weighted columns in \(\mathbb F_q^2\), the weight of a rank-zero matrix is the \(m\)-th power of the zero-column weight. For rank exactly one, choose its unique one-dimensional column span, take the \(m\)-th power of the total weight inside that line and subtract the all-zero contribution. There are \(q+1\) lines in \(\mathbb F_q^2\). In the same-color case all lines have weight \(h\); in the other cases only the two coordinate axes contain supported nonzero vectors. Multiplying by the respective numbers \(4,8,4\) of bottom-color choices yields exactly \(N_0\) and \(N_1\) as displayed. All remaining matrices have rank two.

For a single idempotent the number of choices is
\[
E(q,m)=2(1+q^2)^m+2(2q)^m.
\]
Indeed, its two bottom diagonal bits are equal in two ways, giving \((1+q^2)^m\) lifts, or different in two ways, giving \((2q)^m\) lifts. The number of ordered idempotent pairs is \(E(q,m)^2\), proving the formula for \(N_2\).

**4. Nonempty rank strata and asymptotics.** For \(m=1\) the commutator block has one column, so \(N_2=0\). For \(m\ge2\), select the same bottom color and opposite top colors at two distinct maximal vertices, with independent nonzero commutator columns; every choice has a nonempty preimage by step 1, so \(N_2>0\). To prove the asymptotic statement, the largest exponential base in \(E(q,m)^2\) is \((1+q^2)^2\). Every base occurring in \(N_0+N_1\) is strictly smaller when \(q>1\): explicitly \(a,b,h,c,d<(1+q^2)^2\), and \(2q(1+q^2)<(1+q^2)^2\) because \((q-1)^2>0\). Thus \((N_0+N_1)/E(q,m)^2\to0\).

## Verification
`verify_commutator.py` independently enumerates all idempotents and checks every ordered pair by direct matrix commutator and ordinary row-reduction rank, over \((q,m)=(2,1),(2,2),(2,3),(3,1),(3,2)\). In these cases it obtains, in order,
\[
(196,128,0),\ (2404,3648,672),\ (29524,78608,34752),\
(400,624,0),\ (10048,42912,21024).
\]
All agree with the formula; the program also checks the rank-two existence threshold for several field sizes. The proof is algebraic and covers all prime powers, not just the prime fields handled by the direct enumerator. Run with `python verify_commutator.py`; no third-party packages are required.

## Relationship to prior work
Khripchenko and Novikov, *Finitary incidence algebras* (arXiv:0803.0069v1, public 2008-03-01), Theorem 3, prove the important one-idempotent diagonal-conjugacy result. Gargate and Gargate, *Involutions on Incidence Algebras of Finite Posets* (arXiv:1907.06805v1), enumerate scalar involutions in certain poset incidences for odd characteristic. Their *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets* (arXiv:2009.04243v1), Theorems 1.1–1.2 and Section 4, treat individual potent elements and single-element enumerations. By spectral encoding these earlier results can imply certain **commuting-pair, rank-zero** enumerations: that ingredient is not asserted to be independent of prior work. None of these inspected statements counts the positive-rank **commutator matrices of two separately idempotent elements** as done here.

Radjavi and Rosenthal, *On Commutators of Idempotents* (2002; DOI 10.1080/03081080290019540), concern operator triangularizability under nilpotent commutators rather than a finite-field rank distribution. Its accessible abstract, not full text, was examined. Broader structure theorems on idempotent commutators may constrain possibilities, but such constraints alone do not enumerate multiplicities of rank one and rank two inside this poset algebra.

## Limitations
No isomorphism or orbit classification is asserted. The radical has two rows, which makes its commutator rank at most two; general \(a\)-by-\(m\) height-two incidence algebras are not enumerated here. The checker uses prime fields only; the algebraic proof applies to all finite fields. The published-source comparison does not establish exhaustive novelty: an unindexed finite-ring enumeration or an inaccessible specialized treatment of commutators may subsume the formulas.

## References
1. N. S. Khripchenko and B. V. Novikov, *Finitary incidence algebras*, arXiv:0803.0069v1 (2008), https://arxiv.org/abs/0803.0069.
2. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805v1 (2019), https://arxiv.org/html/1907.06805v1.
3. I. Gargate and M. Gargate, *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1 (2020), https://arxiv.org/html/2009.04243v1.
4. H. Radjavi and P. Rosenthal, *On Commutators of Idempotents*, Linear and Multilinear Algebra 50 (2002), 121–124, https://doi.org/10.1080/03081080290019540.
