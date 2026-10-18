# The five \(p\)-rank-one parameters of a genus-four cyclic-symmetry family in characteristic seven

## Finding
Let \(k=\overline{\mathbf F}_7\), and let \(H_{a,b}\) be the smooth genus-four hyperelliptic curve
\[
H_{a,b}:\quad y^2=x^{10}+x^7+a x^4+b x,
\qquad (a,b)\in k^2.
\]
Put
\[
\begin{aligned}
\Delta&=a^2-4a^3-4b-27b^2+18ab,\\
U&=a^3-ab+3b^2,\\
V&=3a^2+3a-b,\\
W&=3ab^2+3(a+1)^7.
\end{aligned}
\]
All polynomial equalities and inequalities below are interpreted in characteristic seven. Assume \(b\Delta\ne0\), which is exactly the smoothness condition. Then the ordered pair
\(\bigl(f(H_{a,b}),\,a(H_{a,b})\bigr)\) of Jacobian \(p\)-rank and Jacobian \(a\)-number is
\[
\begin{array}{c|c}
\text{parameter condition}&(p\text{-rank},a\text{-number})\\\hline
U\ne0,\ V\ne0&(4,0)\\
U=0,\ V\ne0&(3,1)\\
V=0,\ W\ne0&(2,2)\\
V=0,\ W=0&(1,2).
\end{array}
\]
Every row occurs. The \(p\)-rank-one locus consists of **exactly five geometric parameter pairs**:
\[
(a,b)=(2,4),\quad (3,1),\quad\text{and}\quad
b=3a(a+1),\quad a^3+3a^2-1=0.
\]
The final cubic is irreducible over \(\mathbf F_7\), so the remaining three pairs are defined over \(\mathbf F_{7^3}\), not over \(\mathbf F_7\). In particular, no smooth curve in this normalized family has \(p\)-rank zero or \(a\)-number at least three. The number five counts parameters, **not asserted pairwise nonisomorphic curves**.

## Assumptions and scope
The base field \(k\) is algebraically closed of characteristic seven. The parameters are arbitrary elements of \(k\) satisfying \(b\Delta\ne0\). The curve denotes the smooth projective completion of the displayed affine model. Both invariants belong to its Jacobian. The calculation concerns exactly the two-parameter normalized family displayed above, not every genus-four hyperelliptic curve with an automorphism of order six: additional automorphism types and normalizations can lie outside it. No statement about complete Ekedahl–Oort types or Newton polygons is made.

The choice of family is motivated by the cyclic-order-six genus-four search family in Kudo–Nakagawa–Takagi [1]. That work determines superspecial parameters, chiefly for primes at least seventeen; the present question concerns the finer \(p\)-rank and \(a\)-number degeneration in the smallest prime admitted by the family's automorphism classification. Frei's investigation [2, Section 4.3] highlights the subtlety of large \(a\)-numbers in characteristic seven; the present theorem settles the maximal \(a\)-number only within this particular family.

## Proof
**Smoothness.** Write \(f(x)=xg(x^3)\), where \(g(z)=z^3+z^2+az+b\). Since the characteristic is prime to three, the polynomial \(f\) is squarefree precisely when \(x=0\) is a simple root and \(g\) has three distinct nonzero roots. These requirements are \(b\ne0\) and \(\operatorname{disc}(g)=\Delta\ne0\). Its degree is ten, so the smooth completion has genus four.

**The Cartier matrix.** For the standard basis \(x^{j-1}dx/y\), \(1\le j\le4\), the coefficient matrix underlying Cartier has entries \(M_{ij}=[x^{7i-j}]f(x)^3\), as in [1, Section 2.2]. The multinomial expansion yields
\[
M=\begin{pmatrix}
3ab^2&0&0&b^3\\
0&U&0&0\\
0&0&V&0\\
3&0&0&3(a+1)
\end{pmatrix},\qquad \det M=3b^2 U V^2.
\]
The \(2\times2\) corner block in indices \(1,4\) has rank two if \(V\ne0\), and rank one if \(V=0\), because its lower-left entry is three. On \(V=0\), substitution \(b=3a(a+1)\) gives
\[
U=6a^2(a-5)^2,\quad
\Delta=2a(a+2)^3,\quad b=3a(a+1).
\]
Thus the smooth part of \(V=0\) excludes exactly \(a=0,5,6\), and hence has \(U\ne0\). Consequently \(\operatorname{rank}(M)\) is respectively \(4,3,2\) in the first, second, and last two rows of the claimed table. Since \(a(H)=4-\operatorname{rank}(M)\), the \(a\)-number classification follows.

**Stable Cartier rank.** The Cartier operator is Frobenius-inverse-semilinear: its matrix is obtained by taking seventh roots of the entries of \(M\). Its stable image rank, which equals Jacobian \(p\)-rank, can therefore be computed from the ranks of the twisted products \(M^{[7^{n-1}]}\cdots M^{[7]}M\), where brackets mean entrywise Frobenius powers. Nonzero diagonal blocks \(U,V\), and invertible corner blocks, contribute their full dimensions to stable rank.

When \(V=0\), write the corner block as \(B=uv^{\mathsf T}\) with
\[
u=\binom{3ab^2}{3},\qquad v=\binom1{a+1}.
\]
Then
\[
B^{[7]}B=u^{[7]}\bigl((v^{[7]})^{\mathsf T}u\bigr)v^{\mathsf T}
= W\,u^{[7]}v^{\mathsf T}.
\]
If \(W=0\) its semilinear square vanishes, while if \(W\ne0\), further twisted products remain nonzero (their intervening scalar factors are successive seventh powers of \(W\)). The nonzero \(U\) block always contributes rank one. Hence the \(p\)-rank is one or two according as \(W=0\) or \(W\ne0\), proving the table.

**Exact geometric census.** On \(V=0\), a direct polynomial identity gives
\[
W=3(a-2)(a-3)(a+1)^2(a^3+3a^2-1).
\]
Its possible roots are \(2,3,6\) and the three roots of \(Q(a)=a^3+3a^2-1\). The root \(a=6\) has \(b=0\) and must be discarded. Neither \(2\) nor \(3\) is excluded by \(b\Delta\ne0\); the polynomial \(Q\) has no root in \(\mathbf F_7\), is therefore irreducible and separable, and is coprime to \(a(a+1)(a+2)\). All three of its roots are smooth parameters. Thus there are exactly five and they are distinct.

All four strata occur: the respective sample pairs for \((p\text{-rank},a\text{-number})=(4,0),(3,1),(2,2),(1,2)\) are \((0,1),(3,4),(1,6),(2,4)\).

## Verification
The accompanying standalone `verify.py` uses Python's standard library only. Run `python3 verify.py` in the directory containing this report. It independently reconstructs all sixteen Cartier coefficients by multinomial enumeration, checks the determinant-related rank criteria, polynomial substitutions and factorization, irreducibility and coprimality conditions, and exhaustive comparisons of stable matrix ranks for all smooth \(\mathbf F_7\)-parameter pairs. It finds 37 smooth pairs over \(\mathbf F_7\), distributed across the four \((p\text{-rank},a\text{-number})\) strata in counts \(29,4,2,2\), respectively. These finite-field counts corroborate, but do not replace, the polynomial proof over the algebraic closure. The precise five-point geometric count follows from the displayed degree-three irreducibility argument, not finite enumeration alone.

## Relationship to prior work
Kudo, Nakagawa and Takagi [1] study superspecial genus-four curves with order-six automorphisms; their family is exactly the one considered here. Their characteristic-seven discussion supplies the general setting but not the displayed complete rank stratification or its five isolated \(p\)-rank-one parameters. In particular their superspecial search is not a full enumeration of positive \(p\)-rank strata. Frei [2] studies global bounds for large \(a\)-number hyperelliptic curves and partial computations in characteristic seven, without specializing to this normalized two-parameter family and obtaining the four strata. The formulas here apply only to the precise displayed family and do not contradict the broader open questions.

## Limitations
No classification of arbitrary genus-four curves, all order-six automorphism types, geometric isomorphism classes of the five parameters, complete Ekedahl–Oort types, Newton polygons, or global smooth genus-four \(a\)-number-three existence is established. The algebraic closure includes field extensions beyond \(\mathbf F_7\); the three roots of \(Q\) are not rational over the prime field. The originality comparison included the most closely matching accessible literature; an unindexed equivalent result remains a bibliographic risk. Computational checks were not treated as a proof of assertions over all algebraically closed parameters.

## References
[1] M. Kudo, T. Nakagawa, T. Takagi, *Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing \(C_6\)*, arXiv:2210.14822 (first public version 2022-10-26), Mathematics in Computer Science 17 (2023), article 21, https://doi.org/10.1007/s11786-023-00571-w .

[2] S. Frei, *The a-number of hyperelliptic curves*, Colorado State University thesis (2014), especially Section 4.3, https://math.rice.edu/~sf31/Frei_CSU.pdf .
