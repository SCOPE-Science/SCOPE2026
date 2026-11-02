# A sharp retraction-compatibility transition in four-dimensional quantum complete intersections

## Finding

Let \(K=\mathbb F_q\) be any finite field and let \(\lambda\in K^\times\). For the four-dimensional quantum complete intersection
\[
 A_\lambda=K\langle x,y\rangle/(x^2,y^2,xy-\lambda yx),
\]
write \(\operatorname{End}(A_\lambda)\) for the monoid of unital \(K\)-algebra endomorphisms. Two distinct idempotent endomorphisms are adjacent when they commute under composition. Delete the zero-on-the-radical (augmentation) endomorphism and the identity before forming the graph \(\Gamma_\lambda\).

**Nonexterior theorem.** If \(\lambda\ne-1\), then exactly \(2q^2+2\) endomorphisms are idempotent and
\[
 \Gamma_\lambda\cong K_{q,q}\ \sqcup\ 2q(q-1)K_1.
\]
In particular, there are exactly \(q^2\) inclusion-maximal commuting families of four idempotents and \(2q(q-1)\) such families of three idempotents (counting augmentation and identity in each). The clique polynomial of the entire idempotent-commutation graph, including its two universal vertices, is
\[
 (1+t)^2(1+2q^2t+q^2t^2).
\]
This graph, its maximal-family profile and its clique polynomial are independent of \(\lambda\) throughout the nonexterior range, including both ordinary-commutative and genuinely quantum parameters.

**Exterior boundary.** If \(\lambda=-1\), the algebra is the exterior algebra of a two-dimensional space (also when the field has characteristic two). Its previously known retraction structure gives \(q^2(q+1)+2\) idempotents and
\[
 \Gamma_{-1}\cong\frac{q(q+1)}2\,K_{q,q}.
\]
The complete clique polynomial is therefore
\[
 (1+t)^2\left(1+q^2(q+1)t+\frac{q^3(q+1)}2t^2\right).
\]
Thus the compatibility graph changes sharply and uniformly at exactly the exterior parameter \(\lambda=-1\).

For completeness, the total number of endomorphisms, and automorphisms respectively, are
\[
\begin{array}{c|c|c}
\text{parameter}&|\operatorname{End}(A_\lambda)|&|\operatorname{Aut}(A_\lambda)|\\ \hline
\lambda=-1&q^6&q^2(q^2-1)(q^2-q)\\
\lambda=1\ne-1&q^2(2q-1)^2&2q^2(q-1)^2\\
\lambda\notin\{1,-1\}&q^3(3q-2)&q^2(q-1)^2
\end{array}.
\]
The middle row exists only in odd characteristic; in characteristic two, the parameter \(1\) belongs to the exterior row.

## Assumptions and scope

The statements hold for every prime-power field order \(q\ge2\), every invertible deformation parameter \(\lambda\), and **unital** algebra homomorphisms that fix \(K\) pointwise. We use the basis \(1,x,y,z\) with \(z=xy\) and \(yx=\lambda^{-1}z\); multiplication by \(z\) annihilates the radical \((x,y)\), and \(z^2=0\). Augmentation maps the radical to zero and fixes scalars. Graph edges connect distinct maps, not pairs with repetition. Clique polynomials count all unordered cliques, including the empty clique.

## Proof

**1. Endomorphism normal form and defining relations.** The ideal \(J=(x,y)\) is the nilpotent radical, so a unital endomorphism carries \(J\) into \(J\). Every such map is specified uniquely by
\[
 f(x)=ax+by+cz,\quad f(y)=dx+ey+hz,\qquad
 P=\begin{pmatrix}a&d\\b&e\end{pmatrix},\quad\ell=(c,h).
\]
The images satisfy the algebra relations if and only if
\[
 (\lambda+1)ab=(\lambda+1)de=(\lambda^2-1)bd=0.
\]
Indeed, \(f(x)^2=ab(1+\lambda^{-1})z\), \(f(y)^2=de(1+\lambda^{-1})z\), and
\(f(x)f(y)-\lambda f(y)f(x)=(\lambda^{-1}-\lambda)bdz\). There are no restrictions on \(c,h\). Moreover \(f(z)=\delta(P)z\) with
\[
\delta(P)=ae+\lambda^{-1}bd.
\]
The composition law, with the left-hand map applied last, is
\[
 (P,\ell)\circ(Q,m)=(PQ,\ell Q+\delta(P)m).
\]
Consequently, idempotence is equivalent to \(P^2=P\) and \(\ell=\ell P+\delta(P)\ell\).

**2. The nonexterior retractions.** Suppose \(\lambda\ne-1\). The first two relations force each column of \(P\) to have at most one nonzero entry. Each nonzero proper projection \(P^2=P\) therefore has rank one and must be of exactly one of the following forms:
\[
 E_s=\begin{pmatrix}1&s\\0&0\end{pmatrix},\qquad
 F_t=\begin{pmatrix}0&0\\t&1\end{pmatrix},\qquad s,t\in K.
\]
These forms obey all three relations for every \(\lambda\); they each have \(\delta(P)=0\). The row equation \(\ell P=\ell\) therefore gives precisely \(q\) lifts of each matrix:
\[
 e_{s,c}:\ \ell=c(1,s),\qquad f_{t,d}:\ \ell=d(t,1),\qquad c,d\in K.
\]
At rank zero the only idempotent is augmentation; at rank two, \(P=I\) and the row equation forces \(\ell=0\), giving identity. There are \(2q^2+2\) idempotents total.

For fixed \(s\), the composition of two distinct lifts of \(E_s\) is one of the two factors (and reversing their order gives the other); hence they do not commute. Similarly for the \(F_t\) lifts. For distinct \(s\), the matrices \(E_s\) do not commute, and analogously distinct \(F_t\) do not commute. The cross-products satisfy
\[
 E_sF_t=\begin{pmatrix}st&s\\0&0\end{pmatrix},\qquad
 F_tE_s=\begin{pmatrix}0&0\\t&ts\end{pmatrix}.
\]
Equality forces \(s=t=0\), in which case both products vanish. The composition law then shows that every lift of \(E_0\) commutes with every lift of \(F_0\), for any central coordinates. There are no other edges. This establishes \(K_{q,q}\sqcup2q(q-1)K_1\). Since augmentation and identity commute with all maps, maximal clique sizes and counts follow directly: \(q^2\) edges in the complete bipartite component, and \(2q(q-1)\) isolated vertices. The clique polynomial follows by adjoining the two universal vertices.

**3. Exterior boundary.** At \(\lambda=-1\), all matrices \(P\in M_2(K)\) are allowed and \(\delta(P)=\det P\). For an idempotent matrix \(P\), rank zero and two yield the two universal maps. Rank-one projections have \(q(q+1)\) choices (a projective image line together with one of \(q\) complementary kernel lines), and each admits exactly \(q\) rows \(\ell\) with \(\ell P=\ell\). Two distinct rank-one projections commute precisely when they are complementary; the corresponding lifts commute in both directions because the products of their quotient projections vanish. Each complementary pair gives a full \(K_{q,q}\); the \(q(q+1)\) rank-one projections partition into \(q(q+1)/2\) such pairs. This recovers the established exterior result and proves the stated contrast with the nonexterior regime. In characteristic two, \(\lambda=-1=1\) and the same exterior calculation applies.

**4. All endomorphisms and units.** At \(\lambda=-1\), there are \(q^4\) possible matrices \(P\). Otherwise each of the two columns lies on the union of coordinate axes, which contains \(2q-1\) vectors; at \(\lambda=1\ne-1\), all \((2q-1)^2\) column choices are valid. If \(\lambda\notin\{1,-1\}\), the additional equation \(bd=0\) excludes exactly \((q-1)^2\) matrices and leaves \(q(3q-2)\). In every case \(\ell\) has \(q^2\) choices. A map is invertible if and only if its induced quotient matrix \(P\) is invertible: exterior gives \(\operatorname{GL}_2(K)\); the ordinary-commutative nonexterior case permits the two invertible monomial matrix patterns; the generic case permits only nonzero diagonal matrices. Multiplying these respective counts by \(q^2\) proves the remaining formulas.

## Verification

Run the accompanying standalone script using `python3 verify.py`. It enumerates all maps by the images of the two generators, tests the original multiplication relations directly in the four-dimensional algebra, composes pairs directly, computes idempotents and commutation components, and checks the formulae in all parameter cases over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). It reports `VERIFY_OK` after ten \((q,\lambda)\) tests. These finite tests are corroboration; the proof above, not enumeration, establishes the result for arbitrary finite fields.

## Relationship to prior work

Jin and Zhang, *Bi-Frobenius algebra structure on quantum complete intersections* (2022), examine the same two-generator quantum complete intersection and parameter-dependent coalgebraic structures. Their results do not classify commuting idempotent **algebra endomorphisms** or the full endomorphism-count distribution. Bergh, Erdmann, and Jorgensen (2019) investigate constant Jordan type for modules over quantum complete intersections; Bergh and Erdmann (2007) compute their (co)homology. Neither module-theoretic nor cohomological results give the present commuting-retraction graph. The exterior parameter's complete retraction graph is acknowledged as a pre-existing result, not newly claimed here. The asserted contribution is the nonexterior family, its parameter-uniform commuting graph, the exact endomorphism stratification, and the sharp comparison with that previously known exterior boundary.

## Limitations

All maps are unital and fix the coefficient field; larger families of endomorphisms with semilinear field action are not treated. The statement is specialized to square-zero exponents in two generators; it does not claim analogous graphs for higher quantum complete intersections. Equivalent descriptions under other terminology, especially split algebra retracts or quantum-plane projection monoids, may exist outside the inspected sources. No independent mathematical audit or publication-priority certification has been performed.

## References

1. H. Jin and P. Zhang, *Bi-Frobenius algebra structure on quantum complete intersections*, arXiv:2208.05687v1 (first submitted 2022-08-11), especially its definition of quantum complete intersections and parameter-dependent structural results.
2. P. A. Bergh, K. Erdmann, and D. A. Jorgensen, *Modules of constant Jordan type over quantum complete intersections*, arXiv:1910.06714v1 (2019), introduction and module-theoretic results.
3. P. A. Bergh and K. Erdmann, *(Co)homology of quantum complete intersections*, arXiv:0709.3029v1 (2007), definition and Hochschild (co)homology calculations.
