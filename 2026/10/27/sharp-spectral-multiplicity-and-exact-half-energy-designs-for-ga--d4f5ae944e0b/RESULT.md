# Sharp spectral multiplicity and exact half-energy designs for Gaussian localization on concentric annuli

## Finding

Let \(m\ge1\) and let \(S=\bigcup_{j=1}^{m}(a_j,b_j)\), with
\[
0<a_1<b_1<a_2<b_2<\cdots<a_m<b_m<\infty.
\]
On the standard Bargmann–Fock space \(\mathcal F^2\) over \(\mathbb C\), define the radial concentration operator
\[
T_S f=P_{\mathcal F^2}\!\left(\mathbf1_{\{|z|^2\in S\}}f\right).
\]
Its monomial eigenvalues are
\[
\lambda_n(S)=\frac1{n!}\int_S t^n e^{-t}\,dt,\qquad n=0,1,2,\ldots.
\]

**Sharp multiplicity theorem.** For any real \(\tau\), the equation \(\lambda_n(S)=\tau\) holds for **at most \(2m\) distinct nonnegative integers** \(n\). In particular every nonzero spectral eigenspace, including the top eigenspace, has dimension at most \(2m\). If the first interval is allowed to begin at zero while the remaining endpoints remain strictly separated, the upper bound improves to \(2m-1\).

**Sharpness and canonical design.** For every \(m\ge1\), there is an \(m\)-interval set \(S_m\) as above satisfying
\[
\lambda_0(S_m)=\lambda_1(S_m)=\cdots=\lambda_{2m-1}(S_m)=\tfrac12
>\lambda_{2m}(S_m)>\lambda_{2m+1}(S_m)>\cdots>0.
\]
Moreover **\(S_m\) is the unique union of exactly \(m\) bounded intervals strictly inside \((0,\infty)\)** for which the first \(2m\) eigenvalues all equal \(1/2\). Thus the sharp maximum multiplicity can occur **at the operator norm**, at exactly half-energy, for arbitrarily large \(m\).

The endpoints are specified exactly as the ordered roots of the unique monic degree-\(2m\) polynomial minimizing
\[
\int_0^\infty |Q(t)|e^{-t}\,dt
\]
among real monic polynomials \(Q\) of that degree; \(S_m=\{t>0:Q(t)<0\}\).

## Assumptions and scope

The Fock norm is \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2 e^{-|z|^2}\,dA(z)\), and \(P_{\mathcal F^2}\) is the orthogonal projection from the ambient weighted \(L^2\)-space. The normalized monomials \(e_n(z)=z^n/\sqrt{n!}\) form an orthonormal basis. The mask is the indicator of a finite union of **bounded, full concentric annuli**, with \(m\) meaning the exact number of connected radial components. The statement makes no assertion for arbitrary nonradial domains or general weighted radial masks. Via the standard Bargmann transform, \(T_S\) is unitarily equivalent to Gaussian-window short-time Fourier concentration on phase-space annuli \(\pi(x^2+\xi^2)\in S\).

## Proof

**1. Radial diagonalization.** Angular orthogonality makes distinct monomials orthogonal under radial multiplication. Polar integration gives
\[
\langle T_S e_n,e_n\rangle=\frac{1}{n!}\int_S t^n e^{-t}\,dt.
\]
Every \(\lambda_n\) lies strictly between zero and one, and \(\lambda_n\to0\), because \(S\) has positive finite measure and lies in a bounded interval. Thus the operator is positive and compact, with no zero eigenvectors, and its spectral multiplicities are precisely the numbers of coinciding monomial eigenvalues.

**2. A finite-exponential bound.** Integration by parts yields, for every \(n\ge0\),
\[
(n+1)!\big(\lambda_{n+1}-\lambda_n\big)=F(n+1),\qquad
F(x)=\sum_{j=1}^{m}\big(e^{-a_j}a_j^x-e^{-b_j}b_j^x\big).
\]
For any \(N\) distinct real exponents, a nontrivial linear combination of their exponentials has at most \(N-1\) distinct real zeros. Indeed, divide by the exponential with smallest exponent, differentiate, apply Rolle's theorem, and induct on \(N\). Here \(F\) has exactly \(2m\) distinct exponential terms and is nonzero (its largest-exponent coefficient is \(-e^{-b_m}\)), hence at most \(2m-1\) real zeros.

If \(r\) distinct indices \(n_1<\cdots<n_r\) satisfy \(\lambda_{n_i}=\tau\), then for each consecutive pair,
\[
0=\lambda_{n_{i+1}}-\lambda_{n_i}
=\sum_{n=n_i}^{n_{i+1}-1}\frac{F(n+1)}{(n+1)!}.
\]
Either some sampled summand vanishes, or nonzero summands of both signs occur; continuity then supplies a zero of \(F\) in \([n_i+1,n_{i+1}]\). These \(r-1\) intervals are pairwise disjoint, so \(r-1\le2m-1\), proving \(r\le2m\). If \(a_1=0\), the corresponding exponential term vanishes identically for \(x>0\), leaving only \(2m-1\) nonzero terms and the improved bound.

**3. Constructing all \(2m\) equal top modes.** Fix \(m\) and minimize \(\int_0^\infty |Q(t)|e^{-t}dt\) among real monic degree-\(2m\) polynomials. A minimizer \(Q\) exists: writing \(Q(t)=t^{2m}-q(t)\), the objective tends to infinity with the coefficients of \(q\) by the triangle inequality and equivalence of norms on the finite-dimensional lower-degree polynomial space.

For each polynomial \(h\) of degree at most \(2m-1\), differentiation of the objective under \(Q+\varepsilon h\) is legitimate by dominated convergence: the zero set of \(Q\) is finite and \(|h|e^{-t}\) is integrable. The first-order condition is
\[
\int_0^\infty \operatorname{sgn}Q(t)\,h(t)e^{-t}\,dt=0.
\]
If \(Q\) changed sign at fewer than \(2m\) positive points, the product \(h\) of the corresponding linear factors would have degree less than \(2m\) and would make \(\operatorname{sgn}Q(t)h(t)\) have one strict sign almost everywhere, contradicting this orthogonality. Since \(\deg Q=2m\), it has exactly \(2m\) distinct, simple positive roots. Its leading coefficient is positive, so its negative set is exactly \(m\) bounded, nondegenerate intervals \(S_m\), alternating between these roots.

The sign-orthogonality condition says
\[
0=\int_0^\infty (1-2\mathbf1_{S_m}(t))t^k e^{-t}\,dt,
\qquad k=0,\ldots,2m-1.
\]
As \(\int_0^\infty t^k e^{-t}dt=k!\), this yields \(\lambda_k(S_m)=1/2\) for all \(k=0,\ldots,2m-1\).

Therefore \(F(1)=F(2)=\cdots=F(2m-1)=0\) for this mask. The exponential zero bound is saturated, so \(F\) has no other real zero. Because \(F(x)\sim-e^{-b_m}b_m^x<0\) as \(x\to\infty\), it follows that \(F(x)<0\) for all \(x>2m-1\). The difference formula proves \(\lambda_{n+1}<\lambda_n\) for every \(n\ge2m-1\), establishing the sharp top-eigenspace claim.

**4. Uniqueness of the half-energy design.** If \(Q_1,Q_2\) were distinct monic minimizers, convexity would give
\[
\int\left|\frac{Q_1+Q_2}{2}\right|e^{-t}dt
=\frac12\int(|Q_1|+|Q_2|)e^{-t}dt.
\]
Consequently \(Q_1\) and \(Q_2\) have the same sign almost everywhere. Each has exactly \(2m\) simple positive roots, so identical signs force identical sign-change locations, and monicity implies \(Q_1=Q_2\). Conversely, any \(m\)-interval design with \(\lambda_0=\cdots=\lambda_{2m-1}=1/2\) determines the monic root polynomial \(Q_S(t)=\prod_j(t-a_j)(t-b_j)\). Its sign is \(1-2\mathbf1_S\), so the moment conditions give \(\int \operatorname{sgn}Q_S\,h e^{-t}=0\) for all lower-degree \(h\). The elementary inequality \(|R|\ge \operatorname{sgn}Q_S\,R\) then shows \(Q_S\) is an \(L^1\) minimizer. By uniqueness, \(S=S_m\).

## Verification

A standalone numerical checker in `checker.py` solves the gamma-moment equations for \(m=1,2\) and evaluates independently the finite difference identity. For \(m=1\), its approximate squared-radius endpoints are \(0.435551673687\) and \(1.917950871302\). For \(m=2\), they are \(0.253097107387,1.041033064951,2.471720862953,4.861071837398\). The numerical first \(2m\) eigenvalues are one-half to machine precision, followed by strictly decreasing tested modes. The analytic proof above, not these finite tests, establishes the conclusion for every \(m\) and every \(n\).

To reproduce the numerical checks with Python, NumPy and SciPy installed, execute `python checker.py` from the directory containing that file. Its tests comprise six moment equations, 26 strict tail comparisons, and 28 difference-identity comparisons.

## Relationship to prior work

Daubechies' foundational Gaussian localization theorem supplies the Hermite diagonalization and incomplete-gamma eigenvalue representation; that formula is **not** claimed as new. Knutsen (2020), Section 3.1, studies a single annulus of prescribed area and obtains high-radius norm estimates, while Section 4 analyzes Cantor-type radial masks. Those results do not contain the finite-component sharp multiplicity theorem or the canonical all-mode half-energy design proved here. Esmeral García and Maximenko (2025) study approximation of arbitrary convergent eigenvalue sequences by radial Toeplitz–Fock symbols, allowing symbol classes broader than finitely many indicator annuli. Bdarneh (2026) studies invariant radial Fock Toeplitz algebras and eigenvalue representations, not exact finite-component multiplicity. Svela and Trapasso (2026) study broad time-frequency concentration and optimizer existence rather than this sharp radial inverse spectral design.

The argument uses classical finite-exponential zero counting and monic \(L^1\)-extremal-polynomial ideas. The proposed distinct contribution is their exact combination into an operator-level sharpness and uniqueness statement for **geometrically constrained radial concentration masks**, not either classical ingredient independently.

## Limitations

The theorem applies to the standard Gaussian Fock weight in one complex dimension and finite unions of **full concentric annuli**. It gives neither a bound for masks with infinitely many components nor a classification of all maximizing masks at levels other than \(1/2\). The uniqueness assertion is specifically for the first \(2m\) eigenvalues equal to \(1/2\). The numerical endpoint data are approximate and are not proofs. Independent expert validation and exhaustive historical-priority certification have not been performed; classical sign-quadrature or extremal-moment literature is a residual priority risk.

## References

1. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612. https://www.nokia.com/bell-labs/publications-and-media/publications/time-frequency-localization-operators-a-geometric-phase-space-approach/
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, Journal of Fourier Analysis and Applications 26 (2020), article 47. https://doi.org/10.1007/s00041-020-09751-9
3. K. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators* (2025), arXiv:2503.23276. https://arxiv.org/abs/2503.23276
4. E. A. T. Svela and S. I. Trapasso, *A quantum harmonic analysis approach to nonlinear time-frequency concentration* (first public 2026-05-27), arXiv:2605.28786. https://arxiv.org/abs/2605.28786
5. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation* (first public 2026-09-17), arXiv:2609.20652. https://arxiv.org/abs/2609.20652
