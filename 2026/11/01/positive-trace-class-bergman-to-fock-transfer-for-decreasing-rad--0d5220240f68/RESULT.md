# Positive trace-class Bergman-to-Fock transfer for decreasing radial masks

## Finding

Let \(\beta>0\), let \(w:[0,\infty)\to[0,\infty)\) be a bounded measurable nonincreasing function vanishing almost everywhere above a finite \(S>0\), and let \(N>S\). Compare the weighted Bergman Toeplitz operator with symbol \(w(N|z|^2)\) and weight exponent \(N\) with the Gaussian Fock Toeplitz operator with symbol \(w(\beta|\zeta|^2)\), identifying their normalized monomial bases. Then the transferred Bergman operator dominates the Fock operator in the positive-operator order, and their nonincreasing eigenvalue sequences satisfy \(\lambda_n^{\mathrm B}(N)\ge\lambda_n^{\mathrm F}\) for **every** \(n\ge0\). Both are trace class, and the defect has the exact trace norm
\[
\boxed{\|U_NT_{w(N|z|^2)}^{\mathrm B,N}U_N^{-1}-T_{w(\beta|\zeta|^2)}^{\mathrm F,\beta}\|_{\mathcal S_1}
=\int_0^S w(v)\left[\frac{N+1}{N(1-v/N)^2}-1\right]\,dv.}
\]
Consequently,
\[
\lim_{N\to\infty}N\|U_NT_{w(N|z|^2)}^{\mathrm B,N}U_N^{-1}-T_{w(\beta|\zeta|^2)}^{\mathrm F,\beta}\|_{\mathcal S_1}
=\int_0^S(1+2v)w(v)\,dv.
\]
For every fixed \(t>0\), the disk mask \(w=\mathbf1_{[0,t]}\) admits the finite-scale identity
\[
\boxed{\|U_NT_{\mathbf1_{|z|^2\le t/N}}^{\mathrm B,N}U_N^{-1}-T_{\mathbf1_{\beta|\zeta|^2\le t}}^{\mathrm F,\beta}\|_{\mathcal S_1}=\frac{t(t+1)}{N-t},\qquad N>t.}
\]
The constant in the asymptotic law is strictly positive for every mask not vanishing almost everywhere; thus its \(N^{-1}\) rate is sharp within this class.

## Assumptions and scope

The weighted analytic Bergman space \(A_N^2(\mathbb D)\) uses the probability measure
\[
d\mu_N(z)=\frac{N+1}{\pi}(1-|z|^2)^N\,dA(z),
\]
where \(N>S>0\). The Gaussian Fock space \(\mathcal F_\beta^2(\mathbb C)\) uses
\[
d\mu_\beta(\zeta)=\frac{\beta}{\pi}e^{-\beta|\zeta|^2}\,dA(\zeta),\qquad \beta>0.
\]
For either space, \(T_f\) is the bounded Toeplitz compression of multiplication by the specified real radial symbol \(f\). The normalized Bergman monomials are
\[
e_n^{\mathrm B,N}(z)=\left(\frac{\Gamma(n+N+2)}{n!\,\Gamma(N+2)}\right)^{1/2}z^n,
\]
and the normalized Fock monomials are
\[
e_n^{\mathrm F,\beta}(\zeta)=\left(\frac{\beta^n}{n!}\right)^{1/2}\zeta^n.
\]
The unitary \(U_N:A_N^2\to\mathcal F_\beta^2\) is **defined** by \(U_N e_n^{\mathrm B,N}=e_n^{\mathrm F,\beta}\) for every \(n\ge0\). This is a canonical monomial-coordinate identification, not the unbounded pointwise rescaling of general analytic functions. The parameter \(N\) need not be integral; in the scaling convention of Ma--Yan--Zheng--Zhu it is \(N=\beta r^2\). Functions differing on null sets are identified.

## Proof

**1. Exact spectral probability laws.** Both Toeplitz operators commute with rotations and are diagonal in the displayed monomial bases. Put \(v=N|z|^2\) on the Bergman side and \(v=\beta|\zeta|^2\) on the Fock side. Direct beta and gamma integrals give, for all integers \(n\ge0\),
\[
\lambda_n^{\mathrm B}(N)=\int_0^N w(v)q_{n,N}(v)\,dv,\quad
q_{n,N}(v)=\frac{\Gamma(N+n+2)}{n!\,\Gamma(N+1)N^{n+1}}v^n(1-v/N)^N\mathbf1_{(0,N)}(v),
\]
\[
\lambda_n^{\mathrm F}=\int_0^\infty w(v)p_n(v)\,dv,\quad p_n(v)=\frac{v^ne^{-v}}{n!}.
\]
Thus \(q_{n,N}\) and \(p_n\) are probability densities. They are respectively the density of \(N X\) for \(X\sim\mathrm{Beta}(n+1,N+1)\), and of \(Y\sim\mathrm{Gamma}(n+1,1)\), with unit rate in the latter.

**2. Strict distributional ordering.** For \(0<v<N\),
\[
\frac{q_{n,N}(v)}{p_n(v)}
=\left[\prod_{j=1}^{n+1}\left(1+\frac jN\right)\right](1-v/N)^N e^v.
\]
Its logarithmic derivative is exactly
\[
\frac{d}{dv}\log\frac{q_{n,N}(v)}{p_n(v)}=-\frac{v}{N-v}<0.
\]
The likelihood ratio begins above one and decreases continuously to zero at \(N\). Since each density has total mass one, it crosses one exactly once. Integrating the signed density difference before or after that crossing shows, for every \(s>0\),
\[
\int_0^s q_{n,N}(v)\,dv>\int_0^s p_n(v)\,dv.
\]
For \(s\ge N\), the left integral is one and the right integral is strictly less than one. A nonnegative bounded nonincreasing compactly supported \(w\) is a positive superposition (in the Stieltjes/layer-cake sense, up to null sets) of indicators \(\mathbf1_{[0,s]}\). It follows that \(\lambda_n^{\mathrm B}(N)\ge\lambda_n^{\mathrm F}\) for every \(n\), with strictness if \(w\) is not almost everywhere zero. This establishes the asserted positive operator order after conjugation by \(U_N\).

**3. Eigenvalue indexing.** The likelihood ratios \(q_{n+1,N}/q_{n,N}\) and \(p_{n+1}/p_n\) are positive constants times \(v\), hence strictly increasing in \(v\). Each of the two probability families is therefore stochastically increasing in \(n\). Since \(w\) is nonincreasing, both eigenvalue sequences are nonincreasing. The comparison is consequently a comparison of the eigenvalues **in spectral decreasing order**, not merely of arbitrarily labeled diagonal entries.

**4. Exact trace norm.** The diagonal reproducing kernels are \(K_N(z,z)=(1-|z|^2)^{-N-2}\) and \(K_\beta(\zeta,\zeta)=e^{\beta|\zeta|^2}\). Integrating the positive symbols against their diagonal kernel measures, or summing the nonnegative spectral terms by Tonelli, yields
\[
\operatorname{tr}T_{w(N|z|^2)}^{\mathrm B,N}=\frac{N+1}{N}\int_0^S\frac{w(v)}{(1-v/N)^2}\,dv,
\quad\operatorname{tr}T_{w(\beta|\zeta|^2)}^{\mathrm F,\beta}=\int_0^S w(v)\,dv.
\]
Both are finite because \(S<N\) and \(w\) is bounded. Their transferred difference is positive and trace class, so its trace equals its \(\mathcal S_1\) norm. Subtracting these two expressions proves the displayed exact integral formula.

**5. Sharp rate and disk calculation.** For fixed \(S\), uniformly on \(0\le v\le S\),
\[
\frac{N+1}{N(1-v/N)^2}-1=\frac{1+2v}{N}+O_S(N^{-2})
\quad(N\to\infty).
\]
Bounded convergence, or the uniform expansion, proves the limit and a remainder of order \(O_{S,\|w\|_\infty}(N^{-2})\). If \(w\) has positive mass, its coefficient \(\int_0^S(1+2v)w(v)\,dv\) is positive. For \(w=\mathbf1_{[0,t]}\), integrating the elementary rational function gives
\[
\frac{N+1}{N}\int_0^t(1-v/N)^{-2}\,dv-t
=\frac{(N+1)t}{N-t}-t=\frac{t(t+1)}{N-t}.
\]
This concludes the proof.

**Boundary of the monotonicity hypothesis.** The operator order does not hold for arbitrary nonnegative radial masks. At \(N=2\) and monomial degree \(n=0\), the beta/gamma density ratio equals \(\frac32 e^v(1-v/2)^2\), which is below one throughout \(3/2\le v\le7/4\). The annular mask \(\mathbf1_{[3/2,7/4]}\) therefore has a strictly *negative* difference on the constant monomial. This counterexample limits only the positivity and trace-norm-as-trace assertions; it does not assert a failure of convergence for general compact radial symbols.

## Verification

The included `verify.py` runs in Python using only standard-library exact fractions and high-precision decimal arithmetic. It checks 124 positive spectral gaps (four distinct integral Bergman weights, 31 monomial degrees each), 16 exact rational likelihood-ratio derivative instances, eight exact trace identities/finite-scale rate bounds, eight finite partial-trace and tail bounds, and the sign of the annular counterexample, totaling 157 assertions. It prints `TRANSFER_FINITE_CHECKS_OK count=157 disk_cases=4 modes_per_case=31`. The infinite-dimensional theorem is proven in Steps 1--5, not by this finite test set. In particular, the numerical tail comparisons have no role in the trace-class proof.

## Relationship to prior work

Ma, Yan, Zheng and Zhu (arXiv:2603.04051v1, initial public version dated 2026-03-04) prove weak convergence from scaled weighted Bergman localization operators to Gaussian Fock localization operators (Theorems 1.3 and 4.3); their specialization to constant windows gives the relevant Toeplitz context, and Corollary 1.4 supplies a sharp Fock Toeplitz norm estimate. The present result concerns a different, more quantitative statement: a positive operator difference under **explicit monomial identification**, exact mode-by-mode inequalities and a finite-scale \(\mathcal S_1\) distance for decreasing compact radial masks. Weak convergence and separate norm/trace formulas alone do not imply the operator order or the norm of the *difference*.

Esmeral and Maximenko (arXiv:1505.07906v1) study radial Fock Toeplitz eigenvalue sequences and associated operator algebras. Rozenblum and Vasilevski (arXiv:1912.05855v1) study trace-class Bergman Toeplitz operators with possibly singular symbols. Their inspected results establish useful individual-space background, but do not compare the beta and gamma monomial laws of two different spaces or give the exact cross-space trace-norm defect here. Suárez (2008) describes radial Bergman Toeplitz spectral sequences; only the accessible abstract was checked, so an implicit comparison in its full text is a residual literature risk.

## Limitations

The result is restricted to centered radial masks that are bounded, nonnegative, nonincreasing and compactly supported in the scaled radial coordinate. The Bergman parameter must satisfy \(N>S\). No comparison is claimed for arbitrary windows, general nonradial symbols, annuli, or the same spatial identification used by every alternative localization construction. The monotonicity hypothesis cannot be dropped from the positivity claim. Independent validation has not been performed; possible older equivalent stochastic-order applications remain a literature risk.

## References

1. P. Ma, F. Yan, D. Zheng and K. Zhu, *Localization operators on Bergman and Fock spaces*, arXiv:2603.04051v1 (2026-03-04), especially Theorems 1.3 and 4.3, Corollary 1.4 and Section 5.
2. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906v1 (2015-05-29), especially Section 2.
3. G. Rozenblum and N. Vasilevski, *Trace class Toeplitz operators with singular symbols*, arXiv:1912.05855v1 (2019-12-12), especially Sections 1--2.
4. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, Bull. Lond. Math. Soc. 40 (2008), 631--641, DOI:10.1112/blms/bdn042 (abstract consulted).
