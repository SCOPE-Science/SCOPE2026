# Strict qubit orbit profile for maximal quantum \(f\)-divergences

## Finding
Let \(\rho\) and \(\sigma\) be faithful qubit density matrices with distinct spectra. After ordering eigenvalues, write
\[\rho=\operatorname{diag}(r,1-r),\qquad \sigma=\operatorname{diag}(s,1-s),\qquad \frac12<r,s<1.\]
For a unitary \(U\), let \(q(U)=|\langle e_1,U^*f_1\rangle|^2\), where \(e_1\) and \(f_1\) are the top-eigenvalue eigenvectors of \(\rho\) and \(\sigma\). For every non-affine operator-convex \(f:(0,\infty)\to\mathbb R\), the maximal quantum \(f\)-divergence \(\widehat S_f(\rho\|U^*\sigma U)\) is a strictly decreasing function of \(q(U)\). Thus, after quotienting by eigenvector phase stabilizers, the whole qubit unitary-orbit optimization landscape is one-dimensional and has no interior critical level: same-order eigenbasis alignment is the unique minimum, opposite-order alignment is the unique maximum, and every intermediate divergence value determines the transition probability \(q\) uniquely.

More explicitly, set
\[\delta=\frac{r(1-r)}{s(1-s)},\qquad \Delta=\frac{(2r-1)(2s-1)}{s(1-s)},\qquad t_{\min}=\frac r s+\frac{1-r}{1-s}.\]
For the standard operator-convex representation
\[f(x)=f(1)+f'(1)(x-1)+c(x-1)^2+\int_{[0,\infty)}\frac{(x-1)^2}{x+a}\,d\lambda(a),\]
with \(c\ge0\) and positive \(\lambda\), one has
\[\widehat S_f(\rho\|U^*\sigma U)=F_f\!\left(t_{\min}+\Delta(1-q(U))\right),\]
where
\[F_f(t)=f(1)+c(t-\delta-1)+\int_{[0,\infty)}\frac{(a+1)(t-\delta-1)}{\delta+at+a^2}\,d\lambda(a),\]
and
\[F_f'(t)=c+\int_{[0,\infty)}\frac{(a+1)^2(\delta+a)}{(\delta+at+a^2)^2}\,d\lambda(a)>0.\]
If \(q=\cos^2\theta\), then
\[\widehat S_f(\theta)-\widehat S_f(0)=\Delta F_f'(t_{\min})\theta^2+O(\theta^4).\]

## Assumptions and scope
The states are faithful and have nondegenerate qubit spectra. The function \(f\) is operator convex on \((0,\infty)\) and non-affine. Affine \(f\) gives a constant divergence on density matrices and is therefore excluded from the strictness statement. Degenerate spectra, including a maximally mixed state, make \(\Delta=0\) and likewise collapse the orbit profile. The claim concerns maximal quantum \(f\)-divergence defined through the commutant Radon--Nikodym derivative, not other quantum \(f\)-divergence constructions.

## Proof
Put \(\sigma_U=U^*\sigma U\) and
\[A=\sigma_U^{-1/2}\rho\sigma_U^{-1/2}.\]
Its determinant is orbit-independent:
\[\det A=\delta=\frac{r(1-r)}{s(1-s)}.\]
Its trace is
\[t=\operatorname{Tr}A=\operatorname{Tr}(\rho\sigma_U^{-1}).\]
For two-dimensional unitaries the matrix of squared eigenbasis overlaps is doubly stochastic and necessarily has the form with entries \(q,1-q,1-q,q\). Hence
\[t(q)=q\!\left(\frac r s+\frac{1-r}{1-s}\right)+(1-q)\!\left(\frac r{1-s}+\frac{1-r}s\right)=t_{\min}+\Delta(1-q),\]
with \(\Delta>0\).

Cayley--Hamilton gives
\[A^2-tA+\delta I=0\]
and therefore, for every \(a\ge0\),
\[(A+aI)^{-1}=\frac{(t+a)I-A}{\delta+at+a^2}.\]
Since \(\operatorname{Tr}\sigma_U=\operatorname{Tr}\rho=1\) and \(\operatorname{Tr}(\sigma_UA)=1\),
\[\operatorname{Tr}\!\left[\sigma_U(A+aI)^{-1}\right]=\frac{t+a-1}{\delta+at+a^2}.\]
Also Cayley--Hamilton yields
\[\operatorname{Tr}\!\left[\sigma_U(A-I)^2\right]=t-\delta-1.\]
For \(g_a(x)=(x-1)^2/(x+a)\), polynomial division gives
\[g_a(x)=x-(a+2)+\frac{(a+1)^2}{x+a},\]
so
\[\operatorname{Tr}[\sigma_U g_a(A)]=\frac{(a+1)(t-\delta-1)}{\delta+at+a^2}.\]
Substitution into the integral representation of \(f\) gives the displayed formula for \(F_f\). Differentiation under the integral is justified on the compact orbit interval by the representation's integrability condition and gives
\[F_f'(t)=c+\int_{[0,\infty)}\frac{(a+1)^2(\delta+a)}{(\delta+at+a^2)^2}\,d\lambda(a).\]
Every integrand is positive. A non-affine operator-convex \(f\) has either \(c>0\) or nonzero positive measure \(\lambda\), hence \(F_f'(t)>0\). Since \(dt/dq=-\Delta<0\), the orbit profile is strictly decreasing in \(q\). The extremal and level-set assertions follow immediately. Finally \(q=\cos^2\theta\) gives \(t=t_{\min}+\Delta\sin^2\theta\), and Taylor expansion gives the stated quadratic stability law.

## Verification
The accompanying `artifacts/verify.py` checks the exact rational identities for \(t(q)\), the Cayley--Hamilton kernel reduction, positivity of the derivative kernel, strict monotonicity at multiple rational orbit parameters, and the quadratic small-angle coefficient for representative faithful nondegenerate spectra. These computations corroborate the algebra but are not used as an exhaustive proof; the proof above applies to all admissible \(r,s,f,U\).

## Relationship to prior work
Nguyen, Nguyen, and Le determine the exact minimum and maximum of maximal quantum \(f\)-divergence on arbitrary finite-dimensional unitary orbits and show that the image is the closed interval between the same-order and opposite-order spectral rearrangements. Their paper supplies the operator-convex integral representation used here, but it does not give a qubit-wide strict orbit parametrization, level-set rigidity, or the explicit local stability coefficient. The present result refines that endpoint theorem in dimension two by exploiting Cayley--Hamilton to collapse every non-affine operator-convex maximal divergence to one strictly ordered scalar profile.

Earlier unitary-orbit work of Zhang and Fei treats extremal quantum fidelity and Umegaki relative entropy, rather than the general maximal quantum \(f\)-divergence profile. A later mixed-unitary-orbit paper studies optimization over a larger majorization polytope; its questions and feasible set are different and do not imply the strict unitary-orbit level-set classification proved here.

## Limitations
The theorem is dimension-specific: in dimensions above two, determinant and trace no longer determine the spectrum of \(\sigma_U^{-1/2}\rho\sigma_U^{-1/2}\), so the same one-scalar reduction does not follow. The theorem also does not address non-maximal quantum \(f\)-divergences, singular states, or degenerate spectra. The literature search found no equivalent general qubit profile, but an equivalent formulation could exist under specialized divergence terminology not indexed by the searched phrases.

## References
1. H. M. Nguyen, H. A. Nguyen, and C. T. Le, “Optimization of maximal quantum \(f\)-divergences between unitary orbits,” arXiv:2601.08268, first public 13 January 2026, revised version 1 February 2026.
2. L. Zhang and S.-M. Fei, “Quantum fidelity and relative entropy between unitary orbits,” Journal of Physics A: Mathematical and Theoretical 47 (2014), 055301; arXiv:1305.1472.
3. H. M. Nguyen, T. H. Dinh, and C. T. Le, “Optimization of maximal quantum \(f\)-divergences between mixed-unitary orbits,” 2026 preprint.
