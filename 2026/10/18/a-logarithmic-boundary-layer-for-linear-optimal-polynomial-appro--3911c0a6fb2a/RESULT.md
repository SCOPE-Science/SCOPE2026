# A logarithmic boundary layer for linear optimal polynomial approximants in Hardy spaces

## Finding
For every real \(1<p<\infty\), let \(q_p\) be the unique polynomial of degree at most one minimizing
\[
E_p=\min_{\deg q\le 1}\|1-(1-z)q(z)\|_{H^p},\qquad
\|h\|_{H^p}^{p}=\frac1{2\pi}\int_{-\pi}^{\pi}|h(e^{it})|^p\,dt.
\]
There is a unique \(a_p\in(1/4,1/2)\) such that
\[
q_p(z)=1-a_p+a_pz,\qquad
\int_0^2\frac{s(1-2a_ps)|1-2a_ps|^{p-2}}{\pi\sqrt{s(2-s)}}\,ds=0.
\]
In particular, the unique root \(w_p=-(1-a_p)/a_p\) satisfies \(w_p<-1\) for every finite \(p>1\). As \(p\to\infty\) through arbitrary real values,
\[
\boxed{a_p=\frac12-\frac{\log(4p)}{4p}+o(p^{-1})},\qquad
\boxed{w_p=-1-\frac{\log(4p)}p+o(p^{-1})},
\]
and the optimal residual has the sharp asymptotic
\[
\boxed{E_p^p\sim\frac1{\sqrt{2\pi p}}}.
\]
Thus the boundary approach is logarithmic in the exponent. A notable noncommutation of limits occurs: the fixed limiting residual \((1+z^2)/2\) has \(p\)-th boundary moment \(\int_{-\pi}^{\pi}|\cos t|^p\,dt/(2\pi)\sim\sqrt{2/(\pi p)}\), exactly **twice** the optimal leading moment, although the optimal residual converges coefficientwise to it.

## Assumptions and scope
The norm is normalized Haar measure on the unit circle; the admissible approximants are all *complex*-coefficient polynomials of degree at most one, not only real or symmetric ones. The generating function is exactly \(f(z)=1-z\). All finite-exponent conclusions hold for real \(1<p<\infty\); the displayed asymptotics are for the exponent tending to positive infinity while the approximation degree is fixed. No statement is made about varying approximation degree, other generators, or the endpoint spaces \(H^1\) and \(H^\infty\).

## Proof
**1. Symmetry and one real parameter.** The residual \(r(z)=1-(1-z)q(z)\) ranges bijectively over polynomials of degree at most two satisfying \(r(1)=1\). Its objective is strictly convex in the coefficients for \(p>1\), because \(|\cdot|^p\) is strictly convex and distinct polynomials differ on a positive-measure set of the circle. Finite dimensionality and coercivity ensure existence, so the minimizer is unique. Coefficient conjugation \(r(z)\mapsto\overline{r(\bar z)}\) preserves the norm and constraint. So does reversal \(r(z)\mapsto z^2\overline{r(1/\bar z)}\). Uniqueness makes the minimizer real and reciprocal: \(r(z)=a+(1-2a)z+az^2\), where \(a\) is real. It follows that \(q(z)=1-a+az\). On \(z=e^{it}\),
\[
|r(z)|=|1-2a(1-\cos t)|.
\]
Putting \(s=1-\cos t\) pushes normalized Haar measure to \(\rho(s)\,ds=ds/(\pi\sqrt{s(2-s)})\) on \((0,2)\). Therefore the strictly convex objective is
\[
F_p(a)=\int_0^2|1-2as|^p\rho(s)\,ds.
\]
For \(p>1\), differentiation under the integral is valid and
\[
F_p'(a)=-2pR_p(a),\quad R_p(a)=\int_0^2s(1-2as)|1-2as|^{p-2}\rho(s)\,ds.
\]
At \(a=1/4\), the integrand in \(R_p\) is positive almost everywhere. At \(a=1/2\), writing \(s=1-\cos t\), the odd part in \(\cos t\) integrates to zero and \(R_p(1/2)=-\int_{-\pi}^{\pi}|\cos t|^p\,dt/(2\pi)<0\). Strict convexity gives a unique critical point \(a_p\in(1/4,1/2)\), and hence its root lies below \(-1\).

**2. Competing endpoints.** Set \(b_p=2a_p\in(1/2,1)\) and \(L_p=2b_p-1\in(0,1)\). At the critical point \(R_p(a_p)=0\) is exactly \(P_p(b_p)=N_p(b_p)\), where
\[
P_p(b)=\int_0^{1/b}s(1-bs)^{p-1}\rho(s)\,ds,\qquad
N_p(b)=\int_{1/b}^{2}s(bs-1)^{p-1}\rho(s)\,ds.
\]
For every fixed \(b\in(1/2,1)\), the first integral is bounded below by a positive constant times \(p^{-3/2}\), while the second is at most \(2(2b-1)^{p-1}\). Thus \(P_p(b)>N_p(b)\) for sufficiently large \(p\), so the unique critical value satisfies \(b_p>b\) for sufficiently large \(p\). Since \(b\) was arbitrary, \(b_p\to1\) and \(L_p\to1\).

The substitution \(v=bps\) in \(P_p\) gives
\[
P_p(b)=\frac1{\pi(bp)^{3/2}}\int_0^p
\frac{v^{1/2}(1-v/p)^{p-1}}{\sqrt{2-v/(bp)}}\,dv.
\]
For \(N_p\), use \(u=2-s\), then \(v=bpu/(2b-1)\). With \(L=2b-1\), this yields
\[
N_p(b)=\frac{L^{p-1/2}}{\pi\sqrt{bp}}\int_0^p
v^{-1/2}\sqrt{2-Lv/(bp)}(1-v/p)^{p-1}\,dv.
\]
For any sequence \(b=b_p\to1\), both displayed integrals obey dominated convergence, uniformly along the sequence: the factors involving \(2-v/(bp)\) stay bounded on their domains for all sufficiently large \(p\), and \((1-v/p)^{p-1}\le e^{-v/2}\) for \(p\ge2\) and \(0\le v\le p\). Their limits use \(\Gamma(3/2)=\sqrt\pi/2\) and \(\Gamma(1/2)=\sqrt\pi\), and therefore
\[
P_p(b_p)\sim \frac1{2\sqrt{2\pi}}(b_pp)^{-3/2},\qquad
N_p(b_p)\sim\sqrt{\frac2\pi}\,\frac{L_p^{p-1/2}}{\sqrt{b_pp}}.
\]
The balance \(P_p=N_p\) forces
\[
L_p^{p-1/2}\sim\frac1{4b_pp},\qquad
-p\log L_p=\log(4p)+o(1).
\]
Writing \(\delta_p=1/2-a_p\), we have \(L_p=1-4\delta_p\) and \(\delta_p\to0\). The last relation first gives \(\delta_p=O((\log p)/p)\), hence \(p\delta_p^2\to0\), and then
\[
4p\delta_p=\log(4p)+o(1).
\]
Finally \(w_p=1-1/a_p\), so \(w_p=-1-4\delta_p+O(\delta_p^2)\), yielding the asserted root expansion.

**3. Optimal residual.** Split \(F_p(a_p)\) at \(s=1/b_p\). The same endpoint substitutions, now without the factor \(s\) in the density, yield
\[
\int_0^{1/b_p}(1-b_ps)^p\rho(s)\,ds
\sim\frac1{\sqrt{2\pi b_pp}},
\]
and
\[
\int_{1/b_p}^2(b_ps-1)^p\rho(s)\,ds
\sim\frac{L_p^{p+1/2}}{\sqrt{2\pi b_pp}}=O(p^{-3/2}).
\]
Because \(b_p\to1\), their sum is \(F_p(a_p)\sim(2\pi p)^{-1/2}\), exactly \(E_p^p\). This proves all three asymptotics.

## Verification
A standalone standard-library Python script at `checks/check.py` evaluates the scalar stationarity equation by midpoint-Chebyshev quadrature and bisection for the stated exponents; its actual output is `checks/check_output.txt`. For example, at \(p=2\) it obtains \(a_2=1/3\), giving \(w_2=-2\), and the diagnostics at increasing exponents agree with both predicted limits. These finite tests are **not** the proof of any asymptotic statement; the proof above is analytic. Reproduce by running `python checks/check.py` from the package root.

## Relationship to prior work
Centner, *Optimal Polynomial Approximants in \(L^p\)*, arXiv:2112.14002, Section 6, Example 6.4, already studies exactly the degree-one approximants for \(f(z)=1-z\) and tabulates numerical examples at several fixed even exponents. The existence, uniqueness, orthogonality framework and these fixed-exponent cases are **not claimed as new**. The new mathematical content claimed here is the complete real-exponent characterization through a one-dimensional stationary equation and, principally, the **sharp logarithmic \(p\to\infty\) boundary layer with its constant \(4\)** together with the exact leading residual-moment constant. Centner–Cheng–Felder, arXiv:2305.16068, gives general fixed-exponent bounds for linear Hardy optimal approximants; Cheng–Felder, arXiv:2310.16010, treats degree-one approximation and error estimates, but the inspected relevant sections do not imply the exponent-asymptotic constants for this generator. Searches against related public mathematical result summaries also surfaced multivariate Dirichlet approximation thresholds and bidisk Hardy approximation rates, whose objects and asymptotic variables differ.

## Limitations
The theorem concerns a single canonical generator, fixed degree one, normalized \(H^p\) and real \(p>1\); it does not imply a universal zero-exclusion radius or an analogue for higher-degree approximants. The second-order errors beyond the displayed \(o(p^{-1})\) terms are not established. The originality comparison is based on specified inspected sources and searches, not an exhaustive proof that no equivalent result exists. No independent mathematical audit has been performed.

## References
1. Raymond Centner, *Optimal Polynomial Approximants in \(L^p\)*, arXiv:2112.14002 (first public posting 2021-12-28), especially Example 6.4. https://arxiv.org/abs/2112.14002
2. Raymond Centner, Raymond Cheng, Christopher Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068 (2023-05-25), especially Section 4. https://arxiv.org/abs/2305.16068
3. Raymond Cheng, Christopher Felder, *More Properties of Optimal Polynomial Approximants in Hardy Spaces*, arXiv:2310.16010 (2023-10-24), especially Sections 3–4. https://arxiv.org/abs/2310.16010
