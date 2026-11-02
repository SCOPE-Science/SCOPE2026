# The exact Fourier sampling defect on reciprocal hyperbolas over prime fields

## Finding
Fix an odd prime \(p\), put \(G=\mathbb F_p^\times\), and let \(a,b\in\mathbb F_p\). Define the square complex matrix, indexed by \(s,t\in G\),
\[
M_{a,b}(s,t)=\exp\!\left(\frac{2\pi i}{p}\bigl(ast+b(st)^{-1}\bigr)\right).
\]
Its rank is completely determined by the Legendre symbol \(\eta\):
\[
\operatorname{rank}_{\mathbb C} M_{a,b}=
\begin{cases}
1,& a=b=0,\\
p-2,&ab\ne0\ \text{and }\eta(ab)=-1,\\
p-1,&\text{otherwise}.
\end{cases}
\]
In the singular nondegenerate case, its nullspace is exactly the span of the quadratic-character vector \(t\mapsto\eta(t)\). Thus the sole missing sampling mode is explicit, and the loss is exactly one dimension. This is an exact classification for all odd primes, including \(p=3\).

## Assumptions and scope
The prime is odd, and zero parameters are permitted. Every inverse is taken in \(\mathbb F_p^\times\). The matrix is the restriction of the additive Fourier pairing of \(\mathbb F_p^2\) between the hyperbola \(X=\{(t,t^{-1}):t\in G\}\) and the frequency set \(Y_{a,b}=\{(as,bs^{-1}):s\in G\}\). The latter degenerates if a parameter is zero; the formula remains valid, and the zero pair gives a rank-one matrix. The complex rank is unchanged by phase-sign convention or character normalization.

## Proof
**1. Multiplicative Fourier diagonalization.** Put \(\zeta=\exp(2\pi i/p)\), \(f(u)=\zeta^{au+bu^{-1}}\), and for every multiplicative character \(\chi:G\to\mathbb C^\times\) define
\[
T_\chi=\sum_{u\in G}\chi(u)f(u).
\]
The vector \(v_\chi(t)=\chi(t)\) satisfies
\[
(M_{a,b}v_\chi)(s)=\chi(s)^{-1}T_\chi.
\]
The characters give a basis of \(\mathbb C^G\), and inversion permutes that basis, so the rank equals the number of nonzero \(T_\chi\). A zero \(T_\chi\) contributes exactly the character vector \(v_\chi\) to the kernel.

**2. The degenerate parameters.** If \(a=b=0\), the matrix is all ones. If exactly one parameter is nonzero, a change of variable turns every \(T_\chi\) into a nonzero scalar multiple of \(\sum_{u\ne0}\chi(u)\zeta^u\), or its inverse-character version. This is \(-1\) for the trivial character and is a nonzero Gauss sum of absolute value \(\sqrt p\) for every nontrivial character. Thus rank is \(p-1\) whenever exactly one parameter vanishes.

**3. The cyclotomic zero criterion.** Assume \(ab\ne0\). Character values belong to \(K=\mathbb Q(\zeta_{p-1})\), while the primitive \(p\)th root \(\zeta\) has minimal polynomial \(1+Z+\cdots+Z^{p-1}\) over \(K\), since cyclotomic fields of coprime conductors \(p\) and \(p-1\) are linearly disjoint. Define the weighted phase-fiber sums
\[
c_\lambda=\sum_{u\in G:\,au+bu^{-1}=\lambda}\chi(u)\in K
\qquad(\lambda\in\mathbb F_p).
\]
Then \(T_\chi=\sum_\lambda c_\lambda\zeta^\lambda\) vanishes **if and only if** all \(p\) coefficients \(c_\lambda\) are equal. For trivial \(\chi\), the fiber coefficients are integers totaling \(p-1\), so they cannot all be equal. For nontrivial \(\chi\), their sum is zero, so equality forces \(c_\lambda=0\) for every phase \(\lambda\).

**4. Involutive fibers and the sole exceptional character.** Put \(c=b/a\). The equation \(au+bu^{-1}=\lambda\) is \(au^2-\lambda u+b=0\). Its roots, if distinct, come in pairs \(u,c/u\), and a singleton occurs precisely when \(u^2=c\).

If \(c\) is a square, a singleton fiber exists, with nonzero weight \(\chi(u)\); therefore every \(T_\chi\) is nonzero. If \(c\) is a nonsquare, there are no singleton fibers and every attained phase has exactly two roots. Their weighted sum vanishes for every phase precisely when
\[
\chi(u)+\chi(c/u)=0\quad\text{for all }u\in G.
\]
Multiplying by \(\chi(u)\), and then taking \(u=1\), gives \(\chi(c)=-1\) and \(\chi(u)^2=1\) for all \(u\). Because \(G\) is cyclic, the only nontrivial order-two character is its quadratic character \(\eta\). Conversely, \(\eta(c)=-1\) implies \(\eta(u)+\eta(c/u)=0\) for every \(u\). Thus exactly one Fourier coefficient vanishes if and only if \(\eta(c)=-1\), and its kernel vector is \(\eta\).

Finally, \(c=b/a=ab/a^2\), hence \(\eta(c)=\eta(ab)\). Combining the character counts proves the three rank cases and the nullspace statement.

## Verification
The accompanying reproducibility program `verify_kloosterman.py` directly constructs these complex matrices and checks their numerical singular-value ranks for \(p=3,5,7,11,13,17,19,23,29,31\), covering 178 parameter choices and all three cases. It uses Python 3 and NumPy. The test threshold is numerical; these finitely many tests are diagnostic only. The unbounded prime assertion and exact nullities follow from the four analytic steps above, including cyclotomic linear disjointness, not from computation.

## Relationship to prior work
Twisted Kloosterman sums \(T_\chi\) are classical. The Salié evaluation of the quadratic-character case accounts for the zero associated with a nonsquare product; that particular vanishing is not claimed as new. Kelmer's prime-power distribution work and Louvel's Salié moment work address these scalar sums. Nica develops their theory and moments over finite Frobenius rings, with the stated main theorem restricted to local rings that are not fields. The exact complete rank of this **principal multiplicative sampling matrix**, its exclusion of all nonquadratic zero modes in prime fields, and its explicitly identified one-dimensional sampling defect are the assessed result. A similar classification may exist in earlier spectral-set or character-sum literature and has not been excluded exhaustively.

## Limitations
Only odd prime fields and this reciprocal-parameter curve are classified. No claim is made for prime-power extension fields, arbitrary frequency sets, singular-value conditioning, or matrix ranks over other coefficient fields. The cited literature comparison is bounded; independent mathematical validation has not been performed.

## References
1. D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162 (first posted 2008-01-27).
2. B. Louvel, *The first moment of Salié sums*, arXiv:1107.5282 (2011).
3. B. Nica, *Kloosterman sums over finite Frobenius rings*, arXiv:1910.00165 (2019); especially introduction and Sections 8–11.
4. K. Conrad, *On Weil's proof of the bound for Kloosterman sums*, https://kconrad.math.uconn.edu/articles/kloosterman.pdf (reference treatment of twisted sums and the classical bounds).
5. Y.-H. Lin and F.-T. Tu, *Twisted Kloosterman sums*, Journal of Number Theory 147 (2015), 666–690, DOI 10.1016/j.jnt.2014.08.004 (abstract inspected; full text not accessed).
