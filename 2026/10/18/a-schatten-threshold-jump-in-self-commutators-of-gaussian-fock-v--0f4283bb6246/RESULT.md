# A Schatten threshold jump in self-commutators of Gaussian Fock Volterra operators

## Finding

Let \(T_{a,b}\) be the Volterra-type operator on the standard Gaussian Fock space defined by
\[
(T_{a,b}f)(z)=\int_0^z f(w)(2aw+b)\,dw,\qquad a,b\in\mathbb C,
\]
and set \(H_{a,b}=T_{a,b}^*T_{a,b}-T_{a,b}T_{a,b}^*\). The complete classification is:

1. \(H_{a,b}\) is trace class for all coefficients, and \(\operatorname{tr}H_{a,b}=8|a|^2\).
2. For every \(p>0\), \(H_{0,0}\in\mathcal S_p\). If exactly one coefficient is nonzero, \(H_{a,b}\in\mathcal S_p\) if and only if \(p>1/2\). If both coefficients are nonzero, \(H_{a,b}\in\mathcal S_p\) if and only if \(p>2/3\).
3. Counting strictly positive and strictly negative eigenvalues with multiplicity, the respective inertias are \((0,0)\) in the zero case, \((\infty,0)\) for \(a\ne0,b=0\), \((1,\infty)\) for \(a=0,b\ne0\), and \((\infty,\infty)\) for \(ab\ne0\).

Thus any nonzero linear perturbation of a pure quadratic symbol makes the self-commutator indefinite with infinitely many eigenvalues of each sign, while changing its optimal Schatten exponent from \(1/2\) to \(2/3\). The trace remains fixed. In the customary convention \(H_{a,b}=[T_{a,b}^*,T_{a,b}]\), hyponormality is equivalent to \(b=0\); no nonzero member is cohyponormal.

## Assumptions and scope

The Hilbert space \(\mathcal F^2\) consists of entire functions with norm
\[
\|f\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
Its orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\), for integers \(n\ge0\). Complex coefficients are arbitrary. The constant term of an integration symbol is irrelevant because its derivative is zero. Schatten classes \(\mathcal S_p\) are understood for all real \(p>0\), including quasi-Banach exponents. Inertia counts only nonzero eigenvalues; compactness of the self-adjoint trace-class commutator implies that these are well-defined discrete counts.

## Proof

**1. Explicit two-step shift.** Direct integration on the orthonormal monomial basis gives
\[
T_{a,b}e_n=u_ne_{n+1}+v_ne_{n+2},\quad
u_n=\frac{b}{\sqrt{n+1}},\quad
v_n=2a\sqrt{\frac{n+1}{n+2}}.
\]
The two coefficient sequences are bounded, so this also proves boundedness of \(T_{a,b}\). Put \(H=H_{a,b}\). Because \(T_{a,b}\) has two superdiagonals in the usual matrix convention, \(H\) is a Hermitian tridiagonal matrix. With \(H_{ij}=\langle e_i,H e_j\rangle\), its diagonal entries are
\[
d_0=2|a|^2+|b|^2,\qquad d_1=\frac83|a|^2-\frac12|b|^2,
\]
and, for \(n\ge2\),
\[
d_n=\frac{8|a|^2}{n(n+2)}-\frac{|b|^2}{n(n+1)}.
\]
The only nonzero upper off-diagonal entries are
\[
c_0=\overline a b,\qquad
c_n=-\frac{2\overline a b}{(n+2)\sqrt{n+1}}\quad(n\ge1),
\]
with the opposite off-diagonal given by complex conjugation. For example, the latter identity follows by subtracting the two overlapping output/input path products:
\[
c_n=\overline v_nu_{n+1}-u_{n-1}\overline v_{n-1}
=2\overline a b\left(\frac{\sqrt{n+1}}{n+2}-\frac1{\sqrt{n+1}}\right).
\]

**2. Trace class and trace.** For all coefficients, \(d_n=O(n^{-2})\) and \(c_n=O(n^{-3/2})\). Expressing the Jacobi matrix as a sum of diagonal and single-entry matrix units gives absolute convergence in the trace norm, hence \(H\in\mathcal S_1\). For \(N\ge1\), the diagonal sum telescopes exactly:
\[
\sum_{n=0}^N d_n
=\frac{|b|^2}{N+1}
+4|a|^2\left(\frac{N+1}{N+2}+\frac{N}{N+1}\right).
\]
Letting \(N\to\infty\) gives \(\operatorname{tr}H=8|a|^2\).

**3. Sharp Schatten exponent.** If \(ab=0\), all off-diagonal entries vanish. For every nonzero pure-symbol case, the diagonal has magnitude comparable to \(n^{-2}\) as \(n\to\infty\), so \(H\in\mathcal S_p\) exactly when \(2p>1\). If \(ab\ne0\), the diagonal part belongs to \(\mathcal S_p\) whenever \(p>1/2\), and the upper and lower weighted shifts determined by the off-diagonal sequence belong to \(\mathcal S_p\) whenever \(p>2/3\). Since Schatten ideals are linear spaces also for \(0<p<1\), this proves sufficiency for \(p>2/3\). For necessity, let \(P\) project onto \(\operatorname{span}\{e_{4k}:k\ge1\}\) and \(Q\) onto \(\operatorname{span}\{e_{4k+1}:k\ge1\}\). The compression \(PHQ\) has exactly the singular values \(|c_{4k}|\), since the index sets are separated and \(H\) is tridiagonal. If \(H\in\mathcal S_p\), then \(PHQ\in\mathcal S_p\). But
\[
|c_{4k}|=\frac{2|ab|}{(4k+2)\sqrt{4k+1}}\asymp k^{-3/2},
\]
so \(\sum_{k\ge1}|c_{4k}|^p\) converges only if \(p>2/3\).

**4. Inertia.** When \(b=0\ne a\), all diagonal entries are positive. When \(a=0\ne b\), \(d_0=|b|^2>0\) and \(d_n=-|b|^2/[n(n+1)]<0\) for every \(n\ge1\). If \(ab\ne0\), then \(d_n=O(n^{-2})\) but \(|c_n|\asymp n^{-3/2}\); consequently the principal \(2\times2\) compression of \(H\) to \(\operatorname{span}\{e_{4k},e_{4k+1}\}\) has negative determinant for every sufficiently large \(k\), and hence has one positive and one negative eigenvalue. Distinct such pairs are separated far enough that the quadratic form has no cross terms between their supported vectors. Selecting respectively a positive or negative test vector in each pair constructs infinite-dimensional positive and negative subspaces. Compact self-adjoint spectral theory then gives infinitely many eigenvalues of each sign. The zero case is immediate.

## Verification

The accompanying standalone file `verify_fock_commutator.py` constructs a finite matrix for the bounded two-step shift, retains two extra output rows to avoid artificial top-edge truncation, compares every entry of the leading self-commutator block with the displayed Jacobi coefficients, and checks finite spectral inertia and exact rational telescoping. Its executed result is `PASS 258 matrix, inertia and rational-trace checks`. These finite tests verify formulas and sample spectra; the infinite-dimensional classification relies on the independent analytic arguments above.

## Relationship to prior work

The classical Fock Volterra symbol classification and spectrum are established in Constantin's 2012 study, including the fact that boundedness forces degree at most two and that the spectral disk has radius \(2|a|\) for quadratic coefficient \(a\). The later weighted-Fock analysis by Constantin and Peláez (2013 preprint) treats boundedness, compactness and Schatten classes of the integration operator itself. Constantin and Persson (2015 preprint) extend spectral results to generalized Fock spaces. Those results are essential context but distinguish neither the signs nor the sharp Schatten threshold of the *self-commutator*. In particular, knowing the spectral disk of the nonnormal integration operator does not determine the eigenvalue signs or Schatten class of \([T^*,T]\).

## Limitations

The theorem is for the standard one-variable Gaussian Fock Hilbert space and symbols of degree at most two. It does not determine the exact nonzero eigenvalues or their individual asymptotic constants, nor does it extend the classification to non-Gaussian weights or several complex variables. The cited literature and targeted published-result searches did not establish an equivalent earlier self-commutator theorem, but comprehensive priority or independent mathematical review is not claimed.

## References

- O. Constantin, *A Volterra-type integration operator on Fock spaces*, Proc. Amer. Math. Soc. 140 (2012), 4247–4257, DOI: 10.1090/S0002-9939-2012-11541-2. Author-shared full text at https://www.researchgate.net/publication/266218842_A_Volterra-type_integration_operator_on_Fock_spaces .
- O. Constantin and J. Á. Peláez, *Integral operators, embedding theorems and a Littlewood-Paley formula on weighted Fock spaces*, arXiv:1304.7501 (first posted 2013-04-28), https://arxiv.org/abs/1304.7501 .
- O. Constantin and A.-M. Persson, *The Spectrum of Volterra-type integration operators on generalized Fock spaces*, arXiv:1509.01401 (first posted 2015-09-04), https://arxiv.org/abs/1509.01401 .
