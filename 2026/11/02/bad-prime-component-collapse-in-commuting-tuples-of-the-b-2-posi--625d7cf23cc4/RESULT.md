# Bad-prime component collapse in commuting tuples of the \(B_2\) positive-root Lie algebra

## Finding

Let \(k\) be any field. Define the four-dimensional Lie algebra \(\mathfrak u_k\) with basis \(e_1,e_2,e_3,e_4\), nonzero basic brackets
\[
[e_1,e_2]=e_3,\qquad [e_1,e_3]=2e_4,
\]
and all other brackets obtained by skew-symmetry or equal to zero. This is the integral Chevalley positive-root algebra of type \(B_2\) with the short simple root labeled first, base-changed to \(k\). In characteristic two the second displayed bracket vanishes.

For every integer \(m\ge2\), let \(\mathcal C_m(\mathfrak u_k)\) be the **reduced** variety of ordered, pairwise-commuting \(m\)-tuples. Write the tuple coordinates as four row vectors \(a,b,c,d\in k^m\), with \(x_i=a_i e_1+b_i e_2+c_i e_3+d_i e_4\).

**Theorem.** If \(\operatorname{char}k\ne2\), there are exactly two geometrically irreducible components, both defined over \(k\):
\[
C_0=\{a=0\}\cong\mathbb A_k^{3m},\qquad
C_1=\left\{\operatorname{rank}\begin{pmatrix}a\\b\\c\end{pmatrix}\le1\right\}\times\mathbb A_k^m.
\]
They have respective dimensions \(3m\) and \(2m+2\), and meet along the irreducible subvariety
\[
C_0\cap C_1=\left\{a=0,\quad \operatorname{rank}\begin{pmatrix}b\\c\end{pmatrix}\le1\right\}\times\mathbb A_k^m
\]
of dimension \(2m+1\). The singular locus of the reduced union is exactly this intersection. Hence it is equidimensional if and only if \(m=2\).

If \(\operatorname{char}k=2\), the reduced commuting variety instead has **one** geometrically irreducible component:
\[
\mathcal C_m(\mathfrak u_k)=\left\{\operatorname{rank}\begin{pmatrix}a\\b\end{pmatrix}\le1\right\}\times\mathbb A_k^{2m}.
\]
Its dimension is \(3m+1\), and its singular locus is exactly the linear subspace \(\{a=b=0\}\cong\mathbb A_k^{2m}\).

For every finite field \(\mathbb F_q\) the exact number of ordered commuting \(m\)-tuples is
\[
N_m(q)=\begin{cases}
q^{3m}+q^{m+2}(q^m-1),&q\text{ odd},\\
q^{2m}\big(1+(q+1)(q^m-1)\big),&q\text{ even}.
\end{cases}
\]
The exact number of \(\mathbb F_q\)-points on the singular locus is
\[
S_m(q)=\begin{cases}
q^m\big(1+(q+1)(q^m-1)\big),&q\text{ odd},\\
q^{2m},&q\text{ even}.
\end{cases}
\]
Writing \(\mathbb L=[\mathbb A_k^1]\), the corresponding reduced-variety classes in \(K_0(\mathrm{Var}_k)\) are obtained by replacing \(q\) by \(\mathbb L\) in the two formulas for \(N_m(q)\).

## Assumptions and scope

The Lie brackets are specified over \(\mathbb Z\) before base change: no nonvanishing coefficient is silently assumed after changing characteristic. The field \(k\) need not be algebraically closed or perfect, \(m\) is any integer at least two, and \(\mathcal C_m\) is the reduction of the affine scheme defined by the original pairwise bracket equations. Component and singular-locus statements concern this reduction after geometric base change; point counts concern its rational points over finite fields.

## Proof

**1. Original bracket equations.** For any indices \(i,j\), direct expansion of the defining brackets gives
\[
[x_i,x_j]=(a_i b_j-a_j b_i)e_3+2(a_i c_j-a_j c_i)e_4.
\]
Thus in odd characteristic the vanishing equations say that every \(2\times2\) minor involving row \(a\) and either row \(b\) or row \(c\) vanishes. The row \(d\) is free. In characteristic two only the minors of the \(2\times m\) matrix with rows \(a,b\) remain.

**2. Set-theoretic decomposition in odd characteristic.** If \(a=0\), all equations vanish, giving \(C_0\). If \(a\ne0\), choose an index \(j\) with \(a_j\ne0\). The two families of vanishing minors imply \(b_i=(b_j/a_j)a_i\) and \(c_i=(c_j/a_j)a_i\) for every \(i\). Hence \(\operatorname{rank}(a;b;c)\le1\), giving \(C_1\). Conversely either displayed component satisfies every equation. This argument is preserved over algebraic closures, so it identifies the reduced variety without claiming that the unreduced ideal is radical.

**3. Components, dimensions and intersections.** For \(r\ge2\), the affine determinantal variety \(D_{r,m}^{\le1}\) of \(r\times m\) matrices of rank at most one is irreducible of dimension \(r+m-1\), since it is the image of the irreducible affine space of pairs of vectors under their outer-product map; a nonzero rank-one matrix has a one-dimensional scaling fiber. Its rank-one locus is smooth by a local nonzero-pivot parametrization. Its only singular point is the zero matrix when \(m,r\ge2\): at zero, all defining quadratic minors have zero linear part, so tangent-space dimension \(rm\) exceeds \(r+m-1\). This proves the component dimensions \(3m\) and \(m+(3+m-1)=2m+2\). The intersection is obtained by setting \(a=0\) in the \(3\times m\) determinantal condition; its remaining \(2\times m\) rank-one condition has dimension \(m+1\), plus the free \(d\)-row, giving \(2m+1\).

The two components are distinct: \(C_1\) contains points with \(a\ne0\), while \(C_0\) contains points where \(b,c\) are independent (possible for \(m\ge2\)). Every point of the intersection is singular in the reduced union because two distinct geometric components pass through it. Outside the intersection, \(C_0\) is smooth, and \(C_1\) is smooth because its singular locus \(a=b=c=0\) lies inside the intersection. Hence the singular locus is exactly the intersection. Equality \(3m=2m+2\) occurs precisely at \(m=2\).

**4. Characteristic two.** Because \(2=0\), the equations are exactly all the \(2\times2\) minors of \((a;b)\). The reduced determinantal variety is irreducible of dimension \(m+1\); the independent \(c,d\) rows contribute \(2m\), giving \(3m+1\). Smoothness at nonzero rank-one points and the quadratic-minor tangent calculation at rank zero show that the singular locus is \(a=b=0\), with freely variable \(c,d\).

**5. Point counts and motivic classes.** Over \(\mathbb F_q\), the number of \(r\times m\) matrices of rank at most one is
\[
D_{r,m}(q)=1+\frac{(q^r-1)(q^m-1)}{q-1}.
\]
Indeed a nonzero rank-one matrix is a pair of nonzero column/row vectors modulo simultaneous inverse scaling by \(q-1\) choices. In odd characteristic, inclusion-exclusion for the two components gives
\[
q^{3m}+q^m D_{3,m}(q)-q^m D_{2,m}(q)
=q^{3m}+q^{m+2}(q^m-1).
\]
The intersection count is \(q^m D_{2,m}(q)\), agreeing with the singular count. In even characteristic, the whole variety has \(q^{2m}D_{2,m}(q)\) points, while the singular locus has \(q^{2m}\) points. The same identities hold in \(K_0(\mathrm{Var}_k)\) because nonzero rank-one matrices form the complement of the zero section in the rank-\(m\) vector bundle \(\mathcal O(-1)^{\oplus m}\) over \(\mathbb P^{r-1}\). Hence \([D_{r,m}^{\le1}]=1+(1+\mathbb L+\cdots+\mathbb L^{r-1})(\mathbb L^m-1)\), yielding the asserted classes. No inference from finite samples is used.

## Verification

The standalone checker `check_commuting_B2.py` enumerates all \(a,b,c\) row vectors in ten finite-field/length configurations, evaluates the *original* Lie bracket equations and the component-membership equivalences, and checks the global and singular-locus counts. It also exhaustively evaluates every pair of full four-coordinate Lie elements for \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\). Extension fields \(\mathbb F_4\) and \(\mathbb F_9\) use explicit finite-field arithmetic. See `check_output.txt` for actual results. These checks support but do not prove the statements for all fields and tuple lengths; the preceding structural proof does.

## Relationship to prior work

Goodwin and Röhrle, arXiv:1209.1289 (first public 2012-09-06), Section 3.5, establish the **two-component commuting-pair result for type \(B_2\) in characteristic zero**. This known case of the present classification is not claimed as novel. Farnsteiner, arXiv:1802.09223, extends commuting-pair theory to good characteristic and addresses type \(B_2\) under an odd-characteristic hypothesis; that work does not establish the bad-prime or arbitrary-tuple claims here. Ngo, arXiv:1401.6820, studies commuting restricted-nilpotent tuples in the full classical Lie algebra under good-prime assumptions, a different parameter space. Roman, arXiv:2602.02935, studies bad-characteristic commuting varieties of full classical Lie algebras, not the present explicit nilradical and its all-arity census. In characteristic two this algebra is the direct sum of the three-dimensional Heisenberg Lie algebra and a central line. Consequently its characteristic-two determinantal tuple formula is already implied by the general commuting-tuple classification of the three-block nilradical of block sizes \(1,1,1\), after adding one central coordinate per tuple entry; this specialization is also not claimed as independently new. The contribution assessed here is the arbitrary-length good-characteristic classification, including non-equidimensionality for \(m\ge3\), singular strata, exact arithmetic/motivic formulas, and its comparison with this covered bad-prime specialization.

## Limitations

Only the specified four-dimensional integral positive-root Lie algebra is treated. The classification concerns reduced varieties, so no reducedness claim is made about the original bracket-equation scheme. It does not classify simultaneous adjoint orbits, arbitrary parabolic nilradicals, other ranks, or the higher nilpotent cone of the full classical Lie algebra. The external-priority comparison is best-knowledge rather than exhaustive, and independent mathematical audit has not been performed.

## References

1. Simon M. Goodwin and Gerhard Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289, version 1 publicly posted 2012-09-06, especially Section 3.5. https://arxiv.org/abs/1209.1289
2. Rolf Farnsteiner, *Commuting varieties for nilpotent radicals*, arXiv:1802.09223, publicly posted 2018-02-26, especially Section 5.2. https://arxiv.org/abs/1802.09223
3. Nham V. Ngo, *On nilpotent commuting varieties and cohomology of Frobenius kernels*, arXiv:1401.6820, publicly posted 2014-01-27. https://arxiv.org/abs/1401.6820
4. Roman, *Commuting varieties in bad characteristic*, arXiv:2602.02935, 2026. https://arxiv.org/abs/2602.02935
