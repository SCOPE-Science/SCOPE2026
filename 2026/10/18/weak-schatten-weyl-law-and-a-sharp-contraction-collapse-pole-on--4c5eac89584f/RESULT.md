# Weak-Schatten Weyl law and a sharp contraction-collapse pole on finite-type Bergman ellipsoids

## Finding

Put \(d=n-1\), \(a=k/(2m)\), and \(p_*=d/a=2m(n-1)/k\). For every pair of integers \(n,m\geq2\), every integer \(k\geq1\), and each \(0\leq\rho<1\), the generalized Volterra companion \(T_\rho\) defined below is compact and has the exact Weyl law
\[
\lim_{t\downarrow0}t^{p_*}\#\{j:s_j(T_\rho)>t\}=L_{m,n,k}(\rho),
\qquad
L_{m,n,k}(\rho)=\frac1{(n-1)!}\sum_{b=0}^{\infty}\rho^{bp_*}A_b^{p_*},
\]
with \(0^0=1\), where
\[
A_b=\left[\frac{b+1}{b+k+1}\frac{\Gamma(1+(b+k+1)/m)}{\Gamma(1+(b+1)/m)}\right]^{1/2}.
\]
The coefficient is strictly positive and finite. Equivalently, in decreasing order and with multiplicity,
\[
s_j(T_\rho)\sim (L_{m,n,k}(\rho)/j)^{1/p_*}.
\]
Consequently \(T_\rho\in\mathcal S_p\) exactly when \(p>p_*\), while \(T_\rho\in\mathcal S_{p_*,\infty}\setminus\mathcal S_{p_*}\), and the critical logarithmic spectral sum has the exact residue
\[
\lim_{J\to\infty}\frac{1}{\log J}\sum_{j=1}^{J}s_j(T_\rho)^{p_*}=L_{m,n,k}(\rho).
\]
As the undamped transverse direction is restored, the coefficient develops an exact pole:
\[
\boxed{\lim_{\rho\uparrow1}(1-\rho)^n L_{m,n,k}(\rho)
=\frac1{m^{n-1}p_*^n}.}
\]
The endpoint operator \(T_1\) is bounded but noncompact, with \(\|T_1\|=\|T_1\|_{\mathrm e}=1\); \(T_\rho\to T_1\) strongly as \(\rho\uparrow1\), although \(\|T_1-T_\rho\|=1\) for every \(\rho<1\).

In the explicit complex two-dimensional type-four model \(n=m=k=2\), the critical exponent is \(p_*=2\), and the coefficient simplifies to
\[
\boxed{L_{2,2,2}(\rho)=\frac{1}{2(1-\rho^2)^2}.}
\]
Thus this family gives compact weak-Hilbert–Schmidt companions with an exact double-pole spectral coefficient, despite lacking relatively compact composition range.

## Assumptions and scope

Let
\[
\Omega_{m,n}=\{(z,w)\in\mathbb C^{n-1}\times\mathbb C:\ |z|^2+|w|^{2m}<1\},
\]
and let \(A^2(\Omega_{m,n})\) be its Hilbert Bergman space with unweighted Lebesgue volume. Let \(Rf(z,w)=\sum_{i=1}^{n-1}z_i\partial_{z_i}f(z,w)+w\partial_wf(z,w)\). Set \(\varphi_\rho(z,w)=(z,\rho w)\), \(g(z,w)=w^k\), and, initially for polynomials,
\[
(T_\rho f)(z,w)=\int_0^1(Rf)(tz,\rho tw)(tw)^k\,\frac{dt}{t}.
\]
This is the generalized Volterra companion with the derivative acting on the input. At \(\rho=0\), use \(\rho^0=1\) and \(\rho^b=0\) for positive integers \(b\). The map \(\varphi_\rho(\Omega_{m,n})\) is not relatively compact in \(\Omega_{m,n}\) for any \(\rho<1\), because it retains the full tangential \(z\)-coordinate. All claims concern this specified unweighted Hilbert space, integer parameters, monomial symbol, and partial contraction.

## Proof

**1. Exact orthogonal singular representation.** For a multi-index \(\beta\in\mathbb N_0^{n-1}\), put \(N=|\beta|\) and \(\beta!=\prod_i\beta_i!\). Fubini and beta integration give
\[
\|z^\beta w^b\|_{A^2}^2
=\frac{\pi^n\beta!}{b+1}\frac{\Gamma(1+(b+1)/m)}{\Gamma(N+n+(b+1)/m)}.
\]
The monomials are mutually orthogonal and complete by the Reinhardt symmetry and holomorphic polynomial density. Radial differentiation and integration yield
\[
T_\rho(z^\beta w^b)=\rho^b\frac{N+b}{N+b+k}\,z^\beta w^{b+k}.
\]
Distinct inputs map to mutually orthogonal target monomials. Thus all positive singular values, before sorting, are
\[
\sigma_{N,b}(\rho)=\rho^b\frac{N+b}{N+b+k}
\left[\frac{b+1}{b+k+1}
\frac{\Gamma(1+(b+k+1)/m)}{\Gamma(1+(b+1)/m)}
\frac{\Gamma(N+n+(b+1)/m)}{\Gamma(N+n+(b+k+1)/m)}\right]^{1/2},
\]
with multiplicity \(M_N=\binom{N+n-2}{n-2}=\binom{N+d-1}{d-1}\). The input constant has singular value zero; further zero columns occur at \(\rho=0\). Since \(|w|<1\), the monomial norm ratio is at most one, and the prefactor \((N+b)/(N+b+k)\) is at most one. Hence \(\|T_\rho\|\leq1\) for every \(\rho\in[0,1]\), proving bounded extension by density.

**2. Fixed transverse degree.** For every fixed \(b\geq0\), the gamma quotient estimate gives
\[
\sigma_{N,b}(\rho)\sim \rho^b A_bN^{-a}\qquad(N\to\infty)
\]
for \(0<\rho<1\); the same statement applies to \(b=0\) at \(\rho=0\). The exact multiplicity sum is \(\sum_{N=0}^{X}M_N=\binom{\lfloor X\rfloor+d}{d}\sim X^d/d!\). Therefore each fixed \(b\) contributes
\[
\lim_{t\downarrow0}t^{p_*}\sum_{N\geq0}M_N\mathbf1_{\{\sigma_{N,b}(\rho)>t\}}
=\frac{(\rho^b A_b)^{p_*}}{d!}.
\]
The unique missing constant column is negligible.

**3. Uniform summable bound and the full counting law.** The standard uniform gamma ratio bound, applied with arguments at least a fixed positive number, gives
\[
\sigma_{N,b}(\rho)\leq C\rho^b(1+b)^a(1+N)^{-a}
\]
for all \(N,b\geq0\), with a constant depending only on \(n,m,k\). Put \(c_b=\rho^b(1+b)^a\). If the summand in the count is nonzero, then \(c_b\geq t/C\); the same bound forces \(N\leq C'(c_b/t)^{1/a}\). Hence, using the exact polynomial multiplicity sum,
\[
t^{p_*}\sum_{N\geq0}M_N\mathbf1_{\{\sigma_{N,b}(\rho)>t\}}
\leq C''c_b^{p_*}=C''\rho^{bp_*}(1+b)^d.
\]
The majorant is summable in \(b\) for each fixed \(0<\rho<1\). Dominated convergence interchanges the transverse sum and the fixed-\(b\) counting limit, proving the stated positive finite \(L\). At \(\rho=0\) only \(b=0\) contributes, and the same fixed-degree argument applies. The counting law implies compactness, ordered-singular-value asymptotics, all Schatten thresholds, and the logarithmic spectral sum by standard monotone inversion and comparison with the harmonic series.

**4. Degeneration of the coefficient.** As \(b\to\infty\), the gamma quotient formula gives \(A_b\sim(b/m)^a\) and hence \(A_b^{p_*}\sim m^{-d}b^d\). As \(\rho\uparrow1\), the elementary power-series Abelian asymptotic is
\[
\sum_{b\geq0}\rho^{bp_*}b^d\sim
\frac{d!}{p_*^{d+1}(1-\rho)^{d+1}}.
\]
A finite initial segment is negligible, so dividing by \(d!\) gives the asserted pole \(m^{-d}p_*^{-(d+1)}\) of order \(d+1=n\).

**5. Loss of compactness at the endpoint.** For any fixed \(N\), taking \(b\to\infty\) in the exact singular formula at \(\rho=1\) gives \(\sigma_{N,b}(1)\to1\). The corresponding input and output monomials are orthogonal for distinct \(b\), so \(T_1\) has norm one and essential norm one. For \(\rho<1\), the coefficient of \(T_1-T_\rho\) on each normalized input monomial is \((1-\rho^b)\sigma_{N,b}(1)\). Its supremum is one by letting \(b\to\infty\), proving \(\|T_1-T_\rho\|=1\). For each fixed monomial, the difference tends to zero as \(\rho\uparrow1\); the uniform operator bound then gives strong convergence on the Hilbert space.

**6. Closed two-dimensional model.** When \(n=m=k=2\), the gamma functional equation yields \(A_b^2=(b+1)/2\) and
\[
\sigma_{N,b}(\rho)^2=\rho^{2b}\left(\frac{N+b}{N+b+2}\right)^2\frac{b+1}{2N+b+5}.
\]
Since \(d=1\) and \(p_*=2\), summing the geometric derivative \(\sum_{b\geq0}(b+1)\rho^{2b}\) gives exactly \(L_{2,2,2}(\rho)=1/[2(1-\rho^2)^2]\).

## Verification

The complete gamma-ratio singular formula and the coefficient are analytically derived above; the asymptotic theorem is not inferred from a finite experiment. The standalone `check_spectral.py` checks the special-case identity against the general gamma expression at sixteen parameter combinations, tests fixed-degree large-\(N\) limits for three parameter families, and compares a truncated counting function with its predicted coefficient. Run `python check_spectral.py` with dependencies in `requirements.txt`. The finite counting comparison is a diagnostic with explicit cutoffs, not exhaustive enumeration of an infinite spectrum.

## Relationship to prior work

Dong and Xu, *Generalized Volterra Companion Operators on Bergman Spaces over Convex Domains of Finite Type* (arXiv:2609.27584v1, September 23, 2026), introduce this companion class and compute the Schatten threshold and power-order singular decay for the **fully collapsed** ellipsoid map \(\varphi(z,w)=(z,0)\), together with general criteria. Our starting example and operator normalization come from that work. The new claim treats the continuum of **partially collapsed** maps \(\varphi_\rho(z,w)=(z,\rho w)\), determines the exact Weyl constant and critical logarithmic residue, and identifies its sharp \(n\)-th-order singularity as the partial contraction approaches the noncompact endpoint. It does not claim to discover the fully collapsed power-law exponent.

Dong and Xu, *Absolutely Summing Operators on Bergman Spaces over Convex Domains of Finite Type* (arXiv:2609.23653v1, September 20, 2026), prove exact spectral asymptotics for **positive quasi-radial Toeplitz operators** on ellipsoids (Theorem 9.14 and Proposition 9.15). Those are not the present derivative-on-input companions; the existing constants do not specialize directly to the present \(\rho\)-dependent formula. Mengestie's *Schatten Class Generalized Volterra Companion Integral Operators* (arXiv:1507.03536v1, 2015) concerns Fock-space companions. These works motivate careful comparison, but their inspected statements do not establish the present joint spectral and endpoint law.

## Limitations

The proof uses Reinhardt monomial orthogonality, an integer finite-type ellipsoid, an unweighted Hilbert Bergman space, the symbol \(w^k\), and the specific one-coordinate partial contractions. It gives an iterated asymptotic: first \(t\downarrow0\) for a fixed \(\rho<1\), then \(\rho\uparrow1\); no uniform double-scaling theorem in \(t\) and \(\rho\) is asserted. The critical logarithmic residue is a singular-value sum, not a claim of a particular independently defined noncommutative integration functional. Broader general spectral counting theorems for monomial multipliers or unseen equivalent results could subsume the formula; publication priority has not been independently established.

## References

1. J. Dong and C. Xu, *Generalized Volterra Companion Operators on Bergman Spaces over Convex Domains of Finite Type*, arXiv:2609.27584v1 (first posted September 23, 2026), Section 3.3 and Section 4.
2. J. Dong and C. Xu, *Absolutely Summing Operators on Bergman Spaces over Convex Domains of Finite Type*, arXiv:2609.23653v1 (first posted September 20, 2026), Section 9.3, Theorem 9.14 and Proposition 9.15.
3. T. Mengestie, *Schatten Class Generalized Volterra Companion Integral Operators*, arXiv:1507.03536v1 (2015).
