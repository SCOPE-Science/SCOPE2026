# Sharp Schatten and Fredholm transitions for translations on radial power Fock spaces

## Finding
Let \(\mathcal F_{\alpha,m}^2\) be the Hilbert space of entire functions square-integrable against \(e^{-\alpha|z|^m}\,dA(z)\), with \(\alpha>0\), \(0<m\le1\), and let \(b\in\mathbb C\setminus\{0\}\). The translation \(T_bf(z)=f(z+b)\) is bounded. The following statements quantify its behavior at the threshold \(m=1\).

**Subcritical singular values.** If \(0<m<1\), put \(\beta=(1-m)/m\). Then \(T_b-I\) is compact, and its decreasing singular values obey the *exact* leading law
\[
\lim_{n\to\infty}n^{\beta}s_n(T_b-I)
=|b|\left(\frac{\alpha m}{2}\right)^{1/m}.
\]
In particular, for every \(p>0\),
\[
T_b-I\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac{m}{1-m}.
\]
At equality, \(T_b-I\) belongs to the weak ideal \(\mathcal S_{p,\infty}\), where \(p=m/(1-m)\), but not to \(\mathcal S_p\). The spectra (ordinary and Fredholm essential) of \(T_b\) are both \(\{1\}\).

**Critical spectral folding.** At \(m=1\), write \(R=\alpha/2\). Then
\[
\sigma(T_b)=\{e^{b\lambda}:|\lambda|\le R\},\qquad
\sigma_{\mathrm F}(T_b)=\{e^{b\lambda}:|\lambda|=R\}.
\]
If \(\mu\notin\sigma_{\mathrm F}(T_b)\), the operator \(T_b-\mu I\) is Fredholm, has zero cokernel, and
\[
\operatorname{ind}(T_b-\mu I)
=\dim\ker(T_b-\mu I)
=\#\{\lambda:|\lambda|<R,\ e^{b\lambda}=\mu\},
\]
where solutions are counted once (they are simple). Its index therefore records how many logarithmic preimages of \(\mu\) lie in a disk; the boundary curve may self-intersect. In particular,
\[
\dim\ker(T_b-I)
=2\left\lceil\frac{\alpha|b|}{4\pi}\right\rceil-1,
\]
including at boundary-resonance parameters (where Fredholmness itself fails).

At the critical exponent, for every matrix-valued polynomial \(F\) of any finite size,
\[
\|F(T_b)\|=\|F(T_b)\|_{\mathrm{ess}}
=\max_{|\lambda|=R}\|F(e^{b\lambda})\|,
\]
where the essential norm is taken on the corresponding finite Hilbert direct sum. In particular, \(\|T_b\|=\|T_b\|_{\mathrm{ess}}=e^{R|b|}\).

## Assumptions and scope
The scalar field is complex. Use the norm
\[
\|f\|^2=\frac{\alpha^{2/m}m}{2\pi\,\Gamma(2/m)}
\int_{\mathbb C}|f(z)|^2e^{-\alpha|z|^m}\,dA(z).
\]
The scalar prefactor simply normalizes \(\|1\|=1\) and does not affect operator properties. Normalized monomials form an orthonormal basis. Singular values are listed decreasingly with multiplicity. The Fredholm essential spectrum means the values \(\mu\) where \(T_b-\mu I\) is not Fredholm; the Fredholm index is \(\dim\ker-\dim\operatorname{coker}\). For \(\mathcal S_p\), \(0<p<1\) uses the standard quasi-norm definition. The theorem does not cover \(m>1\), arbitrary weights, or weighted composition operators.

## Proof
**1. Exact monomial model and bounded translation.** For \(e_n(z)=z^n/\|z^n\|\), polar integration yields
\[
\|z^n\|^2=\alpha^{-2n/m}\frac{\Gamma((2n+2)/m)}{\Gamma(2/m)}.
\]
Writing \(D=d/dz\), one obtains the weighted backward shift
\[
De_0=0,\quad De_n=w_ne_{n-1},\qquad
w_n=\alpha^{1/m}n\left(\frac{\Gamma(2n/m)}{\Gamma((2n+2)/m)}\right)^{1/2}.
\]
The gamma-ratio formula gives, as \(n\to\infty\),
\[
w_n\sim c_m n^{-\beta},\qquad
\beta=1/m-1,\quad c_m=(\alpha m/2)^{1/m}.
\]
Consequently, \(D\) is bounded for \(0<m\le1\). The operator series \(e^{bD}=\sum_{k\ge0}b^kD^k/k!\) converges in norm. For polynomials it agrees with translation by the Taylor identity. Polynomial density extends the equality \(T_b=e^{bD}\) to the whole space, independently establishing boundedness.

**2. Compact singular-value law.** Assume \(0<m<1\), so \(\beta>0\). The weighted shift \(D\) is compact, and the multiset of its nonzero singular values is exactly the multiset of weights \(\{w_n:n\ge1\}\). Although initial weights need not be monotone, their asymptotic behavior implies
\[
s_n(D)\sim c_m n^{-\beta}.
\]
Moreover, \(D^2\) is a two-step weighted shift with squared singular values determined by the products \(w_nw_{n-1}\), so \(s_n(D^2)=O(n^{-2\beta})\). (The possible finite index displacement has no effect on this order.) By holomorphic functional calculus,
\[
T_b-I=bD+D^2H_b(D),\quad
H_b(z)=\sum_{j\ge0}\frac{b^{j+2}z^j}{(j+2)!}.
\]
The ideal inequality \(s_n(AB)\le\|B\|s_n(A)\) gives \(s_n(D^2H_b(D))=O(n^{-2\beta})\). To recover the sharp constant after adding the remainder, apply the singular-value Ky Fan inequalities with a rank shift \(k=\lfloor n^\gamma\rfloor\), where \(1/2<\gamma<1\). The leading shift singular values at \(n\pm k\) are \(c_mn^{-\beta}(1+o(1))\), and the remainder singular values at rank \(k\) are \(O(k^{-2\beta})=o(n^{-\beta})\). Both inequalities force
\[
s_n(T_b-I)\sim |b|c_mn^{-\beta}.
\]
Convergence of \(\sum_ns_n(T_b-I)^p\) now gives the asserted sharp Schatten cutoff. Compact quasinilpotent \(D\) has \(\sigma(D)=\{0\}\), since \(\|D^k\|^{1/k}\to0\) for weights tending to zero; ordinary and Calkin spectral mapping give both spectra of \(T_b\) equal to \(\{1\}\).

**3. Critical Fredholm picture.** At \(m=1\), exact simplification gives
\[
w_n=\frac\alpha2\sqrt{\frac{2n}{2n+1}}\nearrow R=\frac\alpha2.
\]
Thus \(\|D\|=R\), and \(D-RS^*\) is compact on the monomial coordinate space, where \(S\) is the unilateral forward shift. Standard Toeplitz-shift Fredholm theory therefore gives \(\sigma_{\mathrm F}(D)=R\mathbb T\), with index \(+1\) for \(|\lambda|<R\), and index zero outside. Every interior point is a simple eigenvalue, with eigenfunction \(e^{\lambda z}\); no boundary eigenvalues exist because those exponentials are not square-integrable against \(e^{-\alpha|z|}\). From \(\|D\|\le R\) and the dense disk of eigenvalues, \(\sigma(D)=\{\lambda:|\lambda|\le R\}\).

Holomorphic spectral mapping in the operator algebra and its Calkin quotient gives the two displayed translation spectra. When \(\mu\) avoids the Calkin spectral curve, the entire function \(e^{bz}-\mu\) has no zero on \(|z|=R\) and only finitely many roots inside it. Factor on a neighborhood of the closed disk into a product of the corresponding linear factors and a holomorphic zero-free factor. The latter yields an invertible operator function of \(D\). Each interior linear factor has surjective image and one-dimensional kernel, so the Fredholm indices add and the composite remains surjective. Every root is simple because \(b\ne0\) and \(e^{b\lambda}=\mu\ne0\). For \(\mu=1\), additionally factor out the finitely many boundary roots. Those boundary factors are injective, commute with every other factor, and therefore do not change the kernel. Counting interior roots \(\lambda=2\pi i k/b\) gives the resonance formula.

**4. Exact complete polynomial norms.** Since \(D/R\) is a contraction, the matrix version of von Neumann's inequality bounds \(\|F(e^{bD})\|\) by \(\max_{|\lambda|\le R}\|F(e^{b\lambda})\|\). The maximum of the norm of an analytic matrix function occurs on the boundary. In the Calkin algebra, the image of \(D/R\) is the unitary image of \(S^*\), with full unit-circle spectrum; continuous functional calculus therefore shows that \(\|F(e^{bD})\|_{\mathrm{ess}}\) equals the same boundary maximum. The ordinary norm dominates the essential norm, proving equality.

## Verification
The supplied `check_translation.py` uses finite monomial matrices and directly evaluates gamma-ratio weights, normalized asymptotics, finite-dimensional exponential identities, limiting critical weights, and integral lattice-count resonances. Its completed execution reported **75 passed finite checks**. These computations are consistency tests and do not replace any infinite-dimensional proof step. For reproduction run `python check_translation.py` with Python, NumPy and SciPy installed. The singular-value law itself follows from the exact shift model, gamma asymptotics, and Ky Fan inequalities; the Fredholm statement follows from the compact-shift model and holomorphic factorization.

## Relationship to prior work
Barik, Sen and Paul (2026, arXiv:2607.17170) establish general boundedness, compactness, Hilbert–Schmidt and essential-norm results for composition operators on power-weight Fock spaces. Their boundedness and membership classifications are not claimed as new here. Mengestie (2016, arXiv:1606.09144) studies compactness and ordinary spectra of differentiation in generalized Fock spaces; the differentiation spectrum used above is classical in that context. A published classification of bounded entire weighted translations on radial power Fock spaces likewise covers boundedness, not the sharp singular-value sequence of \(T_b-I\) or the critical Fredholm index count. The present statement isolates the *difference-from-identity* ideal asymptotics and *critical exponential folding of Fredholm indices*, not a new classification of bounded translations. An older statement claiming all Schatten exponents for compact differentiation is not used: the exact monomial singular values above furnish a direct test and show that any such blanket assertion conflicts with the stated power-weight Hilbert normalization.

## Limitations
These conclusions concern radial power weights and one complex variable. The subcritical result determines leading singular-value asymptotics but not lower-order coefficients. At the critical point the Fredholm classification does not assert Fredholmness on the folded essential curve, even when its interior root count is positive. Inaccessible or unindexed general operator-theoretic treatments could contain equivalent formulations; bibliographic priority is not independently certified. The finite numerical checker is not an infinite-dimensional certificate.

## References
1. S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170, first submitted July 19, 2026, https://arxiv.org/abs/2607.17170.
2. T. Mengestie, *A note on the differential operator on generalized Fock spaces*, arXiv:1606.09144, first submitted June 29, 2016, https://arxiv.org/abs/1606.09144.
3. I. Chalendar, J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, arXiv:2106.00427 (2021), https://arxiv.org/abs/2106.00427.
4. B. Sz.-Nagy, C. Foiaș, *Harmonic Analysis of Operators on Hilbert Space* (classical unilateral shift, matrix von Neumann inequality and holomorphic functional calculus).
