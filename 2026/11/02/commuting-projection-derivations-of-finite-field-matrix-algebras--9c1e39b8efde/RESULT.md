# Commuting projection derivations of finite-field matrix algebras: an exact valency census

## Finding

For a finite field \(k=\mathbb F_q\) and \(n\ge2\), consider the set of **idempotent associative derivations**
\[
\mathcal P_{n,q}=\{D:M_n(k)\to M_n(k)\mid D(XY)=D(X)Y+XD(Y),\quad D^2=D\}.
\]
Define the **reflexive commuting neighborhood** of \(D\) to be \(\mathcal N(D)=\{E\in\mathcal P_{n,q}:DE=ED\}\); it includes \(D\) itself. The following formulas determine the number of vertices, the entire neighborhood-size multiset, and therefore the number of ordered commuting pairs for every \(n\) and \(q\).

If \(q\) is odd, there is only the zero derivation, so the neighborhood-size multiset is \(\{1:1\}\) and there is one ordered pair.

Suppose \(q\) is even. Write
\[
I_t(q)=\sum_{j=0}^t {t\brack j}_q q^{j(t-j)},\qquad
J_t(q)=\begin{cases}
|\mathrm{GL}_t(q)|/|\mathrm{GL}_{t/2}(q^2)|,&2\mid t,\\
0,&2\nmid t.
\end{cases}
\]
Here \({t\brack j}_q=\prod_{i=0}^{j-1}(q^{t-i}-1)/(q^{j-i}-1)\) is a Gaussian binomial, \(|\mathrm{GL}_t(q)|=\prod_{i=0}^{t-1}(q^t-q^i)\), and \(I_t(q)\) is the exact number of idempotent matrices of size \(t\). For \(1\le r\le\lfloor n/2\rfloor\) set
\[
S_{n,r}=\frac{{n\brack r}_q q^{r(n-r)}}{1+\mathbf 1_{2r=n}},\qquad
C_{r,s}=\frac{I_r(q)I_s(q)+J_r(q)J_s(q)}2.
\]
If \(n\) is even, put \(U_n=|\mathrm{GL}_n(q)|/(2|\mathrm{GL}_{n/2}(q^2)|)\); if \(n\) is odd, put \(U_n=0\). Finally write \(P_n=1+\sum_{r=1}^{\lfloor n/2\rfloor}S_{n,r}+U_n\).

**Theorem.** The set \(\mathcal P_{n,q}\) has exactly \(P_n\) members. Its complete multiset of commuting-neighborhood sizes is:

- one derivation (the zero derivation) of neighborhood size \(P_n\);
- for each \(r\) with \(1\le r\le\lfloor n/2\rfloor\), exactly \(S_{n,r}\) derivations of neighborhood size \(C_{r,n-r}\);
- additionally, for even \(n\), exactly \(U_n\) derivations of neighborhood size \(I_{n/2}(q^2)\).

These are disjoint families, even when two numerical neighborhood sizes coincide. In particular the exact number of ordered commuting pairs is
\[
\boxed{K_{n,q}=P_n+\sum_{r=1}^{\lfloor n/2\rfloor}S_{n,r}C_{r,n-r}+U_n I_{n/2}(q^2)},
\]
where the last term is omitted for odd \(n\). For the ordinary simple commuting graph (without loops), subtract one from each neighborhood size.

At \((n,q)=(4,2)\), there are exactly \(457\) idempotent derivations; the neighborhood sizes and multiplicities are \(457:1\), \(58:120\), \(34:280\), and \(22:56\). Thus \(K_{4,2}=18169\). For \(n=2\) and even \(q\), the number is \(K_{2,q}=3q^2+1\).

## Assumptions and scope

All derivations are \(k\)-linear **associative** derivations of the full unital matrix algebra. Commutation means equality of the two endomorphism compositions, not commutation of representative matrices up to conjugacy. The formula holds for every finite field including nonprime extensions, all \(n\ge2\), and both parities. Counts are of **actual operators**, not classes up to algebra automorphism. The common zero derivation is included; the graph convention is explicitly reflexive.

## Proof

**1. Reduction to inner matrices and odd characteristic.** Every derivation of \(M_n(k)\) is inner. For completeness, with matrix units \(E_{ij}\) define \(A=\sum_iD(E_{i1})E_{1i}\); expanding \(D(E_{ab}E_{i1})\) and summing shows \(D(E_{ab})=AE_{ab}-E_{ab}A\). Thus \(D=\operatorname{ad}_A\), and \(\operatorname{ad}_A=\operatorname{ad}_B\) exactly when \(A-B\) is scalar. If \(\operatorname{char}k\ne2\) and \(\operatorname{ad}_A\) is idempotent, then over an algebraic closure the eigenvalue differences of \(A\) must lie in \(\{0,1\}\); each difference occurs together with its negative, forcing every difference to be zero. The map \(\operatorname{ad}_A\) is then nilpotent (because \(A\) is scalar plus nilpotent) and idempotent, hence zero.

**2. Quadratic inner representatives in characteristic two.** Assume \(q\) even. The commuting left- and right-multiplication maps give \((\operatorname{ad}_A)^2=\operatorname{ad}_{A^2}\), so \((\operatorname{ad}_A)^2=\operatorname{ad}_A\) if and only if
\[
A^2+A=cI_n\qquad\text{for some }c\in k.
\]
Replacing \(A\) by \(A+tI_n\) changes \(c\) by \(t^2+t\). The Artin–Schreier image comprises precisely the elements of absolute trace zero. For trace zero, shift \(A\) to an idempotent matrix \(F\). The only shifts preserving \(F^2=F\) are \(F\) and \(F+I_n\); thus its rank \(r\) is identified with \(n-r\). For \(1\le r\le\lfloor n/2\rfloor\), the number of distinct nonzero maps of this split type is
\[
S_{n,r}=\frac{{n\brack r}_q q^{r(n-r)}}{1+\mathbf1_{2r=n}},
\]
because an idempotent of rank \(r\) is determined by an image subspace and a complementary kernel. The rank-zero and rank-\(n\) idempotents give the single zero derivation. For absolute trace one, the polynomial \(t^2+t+c\) is irreducible. The dimension \(n\) must be even, say \(n=2m\); the matrix is multiplication by a quadratic-field element on \(k_2^m\), where \(k_2=\mathbb F_{q^2}\). All such matrices are conjugate, with centralizer \(\mathrm{GL}_m(k_2)\), and each derivation is represented twice by matrices satisfying the fixed quadratic equation (\(A\) and \(A+I_n\)). Therefore their number is \(U_n=|\mathrm{GL}_n(q)|/(2|\mathrm{GL}_m(q^2)|)\). This proves the size \(P_n\).

**3. Commuting derivations force commuting representatives.** Let \(D=\operatorname{ad}_A\) and \(E=\operatorname{ad}_B\) be idempotent derivations in characteristic two. Since \([D,E]=\operatorname{ad}_{[A,B]}\), they commute precisely when \([A,B]=\lambda I_n\) for some \(\lambda\in k\). But \(A^2+A\) is scalar and
\[
0=[A^2+A,B]=A[A,B]+[A,B]A+[A,B]=\lambda I_n
\]
(using \(2=0\)). Hence \(\lambda=0\). This yields the decisive exact equivalence \(DE=ED\iff AB=BA\).

**4. A split representative's neighbors.** Suppose \(A\) is a noncentral idempotent with image rank \(r\) and kernel dimension \(s=n-r\). Its matrix centralizer consists of block-diagonal matrices \(B\in M_r(k)\times M_s(k)\). We count \(B\) satisfying \(B^2+B=cI_n\) for a *common* scalar \(c\). For each of the \(q/2\) values of \(c\) with trace zero, both blocks have respectively \(I_r(q)\) and \(I_s(q)\) possibilities, by a scalar shift to idempotents. For each of the \(q/2\) trace-one values, the irreducible quadratic condition has \(J_r(q)J_s(q)\) choices: it forces both block sizes even, and its centralizer is over \(\mathbb F_{q^2}\). Finally, \(B\mapsto\operatorname{ad}_B\) has exactly \(q\) scalar representatives. Therefore the number of distinct commuting idempotent derivations is exactly \(C_{r,s}=\tfrac12(I_r(q)I_s(q)+J_r(q)J_s(q))\).

**5. A nonsplit representative's neighbors.** If \(n=2m\) and \(A\) is nonsplit, its matrix centralizer is \(M_m(k_2)\). Every scalar polynomial \(t^2+t+c\), \(c\in k\), splits in \(k_2\), so for each \(c\) the solution count in this centralizer is \(I_m(q^2)\). Summing over all \(q\) scalars and dividing by the \(q\) scalar representatives of each derivation gives exactly \(I_m(q^2)\) neighbors. The zero derivation commutes with all \(P_n\) operators. Multiplying each neighborhood size by the number of operators in its class gives the stated multiset and pair count. All counting uses disjoint cases, completing the proof. \(\square\)

## Verification

Run `python3 verify.py` in the same folder as this document. The self-contained Python checker independently constructs the original matrix multiplication, each candidate inner derivation as an operator on the full matrix-unit basis, and tests both \(D^2=D\) and the commuting condition. For six configurations it also directly compares full operator compositions; in the larger \((n,q)=(4,2)\) configuration it compares representative matrix commutators and independently confirms each candidate satisfies the operator idempotence equation. The seven configurations include \(\mathbb F_4\) with extension-field arithmetic; the expected output is recorded in `verification_output.txt`. The finite checks are corroboration, not a proof for all fields and dimensions.

## Relationship to prior work

Britnell–Wildon (arXiv:1001.0811, first publicly available 2010-01-06) study when similarity classes of matrices contain commuting representatives and classify centralizer types; that is different from enumerating the reflexive commuting neighborhoods of the constrained **inner derivations** here. Diniz (arXiv:1407.1288) treats graded identities of elementary matrix gradings over infinite fields, while Diniz–Pellegrino (arXiv:2004.02285) count **isomorphism classes** of gradings, not the number of actual operator pairs or their degree distribution. Fulman–Guralnick (arXiv:1611.05499) treat unrestricted commuting matrix pairs and various nilpotent pairs; these do not directly give the projection-derivation valency census. A particularly relevant later work, Diniz–Martinez Correa–Gonçalves–Koshlukov (arXiv:2610.20113, 2026), classifies individual finite-field gradings for groups whose finite subgroups are cyclic. Individual order-two gradings overlap the structural input above, but the **relative commuting-pair problem** can be interpreted as a grading by \((\mathbb Z/2\mathbb Z)^2\), which fails that group's cyclic-subgroup hypothesis. Its complete text was not available for inspection; the overlap risk is explicitly retained. The claim of contribution is limited to the exact **commuting-neighborhood multiset and ordered-pair census**, not the established general classification of single gradings or unrestricted commuting matrices.

## Limitations

The theorem counts derivations of full associative matrix algebras only. It does not classify simultaneous conjugacy orbits of pairs, their higher-order commuting cliques, general finite-dimensional algebras, or geometric scheme structure. A more general historical formula for weighted simultaneous semisimple matrix conjugacy classes could imply the count; priority is provisional pending fuller literature comparison. Independent review has not been performed.

## References

- J. R. Britnell and M. Wildon, *On Types and Classes of Commuting Matrices over Finite Fields*, arXiv:1001.0811 (first public 2010-01-06), https://arxiv.org/abs/1001.0811.
- D. Diniz, *On the Graded Identities for Elementary Gradings in Matrix Algebras over Infinite Fields*, arXiv:1407.1288 (2014-07-04), https://arxiv.org/abs/1407.1288.
- D. Diniz and D. Pellegrino, *On the Number of Gradings on Matrix Algebras*, arXiv:2004.02285 (2020-04-05), https://arxiv.org/abs/2004.02285.
- J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016-11-16), https://arxiv.org/abs/1611.05499.
- D. Diniz, D. Martinez Correa, D. J. Gonçalves and P. Koshlukov, *Identities and Isomorphisms of Finite Graded Matrix Algebras*, arXiv:2610.20113 (2026-10-14), https://arxiv.org/abs/2610.20113.
