# Sharp Fock-jet singular spectra for affine analytic contractions

## Finding

Let \(\mathcal F^2\) be the one-variable analytic Bargmann–Fock Hilbert space with norm
\[
\|f\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
\]
and let \(\phi(z)=az+b\), where \(0<|a|<1\) and \(a,b\in\mathbb C\). Write \(c=b/(1-a)\) for the fixed point and \(Pf=f(c)\mathbf1\) for the fixed-point evaluation projection (which need not be orthogonal). Set \(C_\phi f=f\circ\phi\). For each fixed integer \(j\ge1\), let \(s_j\) denote the \(j\)-th singular value in nonincreasing order. Then
\[
\boxed{\lim_{n\to\infty}|a|^{-jn}s_j(C_\phi^n-P)
=e^{|c|^2/2}\left(1+\frac{|c|^{2j}}{j!\,\sum_{k=0}^{j-1}|c|^{2k}/k!}\right).}
\]
All displayed constants are strictly positive. Equivalently, the optimal approximation error of rank at most \(j-1\) to \(C_\phi^n-P\) is asymptotic to this explicit constant times \(|a|^{jn}\). For \(c=0\), the identity is exact at every positive iterate: \(s_j(C_\phi^n-P)=|a|^{jn}\). At nonzero \(c\), the leading norm constant for \(j=1\) is \(e^{|c|^2/2}(1+|c|^2)\), which differs from the constant of the uncorrected composition operator.

## Assumptions and scope

The norm is fixed as written; in this normalization \(\|z^k\|^2=k!\), the reproducing kernel is \(K(z,w)=e^{z\bar w}\), and the unitary Weyl translation is \(U_cf(z)=e^{z\bar c-|c|^2/2}f(z-c)\). The coefficient \(a\) can be complex, and the result holds without requiring self-adjointness or normality. The asymptotic concerns each **fixed** rank \(j\) as \(n\to\infty\), not a rank growing with \(n\). If \(a=0\), all positive iterates already equal \(P\), so the stated scaling is not applicable.

## Proof

**1. Taylor decomposition in trace norm.** Put \(t=a^n\). The affine iterate satisfies \(\phi^{\circ n}(z)=c+t(z-c)\). Define \(T_t f(z)=f(c+t(z-c))-f(c)\). Its formal Taylor expansion is
\[
T_t=\sum_{m=1}^\infty t^m(q_m\otimes h_m),\qquad q_m(z)=(z-c)^m,\quad h_m(z)=\frac{z^m e^{z\bar c}}{m!},
\]
where \((q\otimes h)f=q\langle f,h\rangle\) and the inner product is linear in the first slot. Indeed, \(\langle f,h_m\rangle=f^{(m)}(c)/m!\).

The series converges absolutely in trace norm for every \(|t|<1\). To see this, let \(Z\) be a standard complex Gaussian. Orthogonality of monomials gives
\[
\frac{\|q_m\|^2}{m!}=\sum_{\ell=0}^m\frac{(m)_\ell |c|^{2\ell}}{(\ell!)^2}
\le\sum_{\ell=0}^\infty\frac{(m|c|^2)^\ell}{(\ell!)^2}
\le e^{2|c|\sqrt m},
\]
where \((m)_\ell=m!/(m-\ell)!\). The Weyl unitary yields \(\|h_m\|=e^{|c|^2/2}\|q_m\|/m!\). Thus each rank-one term has trace norm at most \(e^{|c|^2/2+2|c|\sqrt m}\), giving the stated convergence.

**2. Exterior-power leading term.** For fixed \(j\), multilinearity of the exterior power and the trace-norm convergence imply
\[
\bigwedge^jT_t
=t^{j(j+1)/2}\bigl((q_1\wedge\cdots\wedge q_j)\otimes(h_1\wedge\cdots\wedge h_j)\bigr)
+O(|t|^{j(j+1)/2+1})
\]
in operator norm as \(t\to0\). Terms with repeated indices vanish, and the unique smallest sum of \(j\) distinct positive indices is \(1+\cdots+j\). Both displayed wedge vectors are nonzero because the underlying polynomial families are linearly independent. Since \(\|\bigwedge^jT_t\|=\prod_{\ell=1}^js_\ell(T_t)\), the asymptotic constant for the \(j\)-th singular value is the product of the successive Gram–Schmidt distances of \(q_j\) and \(h_j\) from their preceding members.

**3. Fock-jet Gram–Schmidt distances.** Let
\[
K_{j-1}(c,c)=\sum_{k=0}^{j-1}\frac{|c|^{2k}}{k!}.
\]
The span of \(q_1,\ldots,q_{j-1}\) consists of polynomials of degree at most \(j-1\) that vanish at \(c\). Inside the polynomials of degree at most \(j-1\), the orthogonal complement of this subspace is spanned by the truncated reproducing kernel \(K_{j-1}(z,c)\). Since \(q_j\) has leading term \(z^j\) and its lower-degree remainder takes value \(-c^j\) at \(c\), its squared distance is precisely
\[
d_j^2=j!+\frac{|c|^{2j}}{K_{j-1}(c,c)}.
\]
The unitary \(U_c\) takes \(e^{|c|^2/2}(z+c)^j/j!\) to \(h_j\). Replacing \(c\) by \(-c\) leaves the preceding distance unchanged, hence the corresponding distance for \(h_j\) is \(e^{|c|^2/2}d_j/j!\). Their product equals
\[
e^{|c|^2/2}\left(1+\frac{|c|^{2j}}{j!K_{j-1}(c,c)}\right).
\]
Dividing consecutive exterior-power norm asymptotics proves the assertion for \(T_{a^n}=C_\phi^n-P\). The equality between singular values and best Hilbert-space finite-rank approximation errors completes the proof.

## Verification

Run `python3 check_fock_jets.py` from the directory containing this document. The standalone script uses only Python's standard library. It checks exact rational Gram determinant pivots for six fixed points through rank eight, the Weyl-translated determinant relation, polynomial Taylor coefficients on rational test points, and the elementary upper bound behind trace-norm convergence. In the completed package it produced **456 exact rational assertions**, all passed. Separately, finite Fock-basis singular-value matrices at decreasing \(|t|\) corroborated the \(j=1,2,3,4\) constants for nonzero fixed points; no finite computation is used to justify the infinite-dimensional asymptotic.

## Relationship to prior work

Chalendar and Partington, *Weighted composition operators on the Fock space: iteration and semigroups* (first public version June 1, 2021), prove the operator-norm convergence of powers of a strict affine composition operator to its fixed-point evaluation projection (Theorem 2.2). Their result does not determine the fixed-rank singular-value decay of the **difference**. Bayart and Tapia-García, *Cyclicity of composition operators on the Fock space* (first public version May 23, 2022), determine the individual approximation numbers of compact affine composition operators (Theorem 7.3), not those of their subtraction by the asymptotic projection. The latter subtraction is not a direct singular-value subtraction: the projection is generally nonorthogonal. The earlier literature on approximation numbers for entire-function composition operators addresses uncorrected operators. The present result identifies the complete fixed-rank asymptotic hierarchy for this corrected error and the nontrivial finite Poisson-sum coefficients arising from the Fock jet Gram geometry.

## Limitations

No uniform estimate in an index \(j\) growing with \(n\) is asserted. The result covers scalar affine strict contractions on the one-variable Gaussian Fock space, not nonlinear compositions, general weights, or several complex variables. Literature overlap was checked by statement and implication in the sources below and in a semantic mathematical-results index; this is not a proof of historical uniqueness. Independent audit has not been performed.

## References

1. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, arXiv:2106.00427 (first public version 2021-06-01), Sections 1–3, especially Theorem 2.2. https://arxiv.org/html/2106.00427v3
2. F. Bayart and S. Tapia-García, *Cyclicity of composition operators on the Fock space*, arXiv:2205.11066 (first public version 2022-05-23), Sections 2 and 7, especially Theorem 7.3. https://arxiv.org/html/2205.11066v1
3. M. L. Doan, B. Hu, L. H. Khoi, and H. Queffélec, *Approximation numbers for composition operators on spaces of entire functions*, Indagationes Mathematicae 28 (2017), 294–305, DOI:10.1016/j.indag.2016.07.003 (comparison context; article abstract and bibliographic records inspected).
