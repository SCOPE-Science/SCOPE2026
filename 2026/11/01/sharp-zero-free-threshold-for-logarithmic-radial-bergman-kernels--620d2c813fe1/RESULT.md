# Sharp zero-free threshold for logarithmic radial Bergman kernels

## Finding

For every real \(\alpha>-1\), let the analytic weighted Bergman space on the unit disk \(\mathbb D\) carry the measure \(w_\alpha(z)dA(z)\), where \(dA=\pi^{-1}dx\,dy\) and
\[
w_\alpha(z)=(-\log|z|^2)^\alpha.
\]
Its reproducing kernel is zero-free on \(\mathbb D\times\mathbb D\) **if and only if** \(-1<\alpha\le1\). For each \(\alpha>1\), a kernel zero is realized by a pair with negative real product \(z\overline\zeta\in(-1,0)\).

The stronger half-plane certificate holds throughout the zero-free regime: writing \(p=\alpha+1\), \(u=z\overline\zeta\), and \(F_p(u)=\sum_{n=0}^\infty(n+1)^p u^n\),
\[
\operatorname{Re}[(1-u)^2F_p(u)]>0\qquad(0<p\le2,\ |u|<1).
\]
The exact kernel is \(K_\alpha(z,\zeta)=F_p(u)/\Gamma(p)=\operatorname{Li}_{-p}(u)/(\Gamma(p)u)\), where the expression at \(u=0\) is defined by continuity.

## Assumptions and scope

Only real \(\alpha>-1\) and the full open disk are considered; \(\alpha=-1\) is excluded because the weight is not integrable near the boundary. At \(z=0\), the logarithmic weight may vanish, diverge, or have a removable exceptional value depending on \(\alpha\); changing a single point does not affect the Hilbert norm. Every scalar \(u\) of modulus less than one is of the form \(z\overline\zeta\) with both points in \(\mathbb D\). All statements about the kernel concern these scalar products rather than zeros of individual analytic functions.

## Proof

**Moment computation.** Radial orthogonality and the substitution \(t=r^2\) give, for every integer \(n\ge0\),
\[
\|z^n\|_{A^2(w_\alpha)}^2=\int_0^1t^n(-\log t)^\alpha dt
=\frac{\Gamma(\alpha+1)}{(n+1)^{\alpha+1}}.
\]
Summing the orthonormal monomial kernels proves the asserted representation; the series converges locally uniformly for \(|u|<1\).

**Half-plane certificate, low exponents.** For \(0<p<1\), the positive constant \(c_p=p/\Gamma(1-p)\) satisfies the Bernstein identity
\[
x^p=c_p\int_0^\infty(1-e^{-xt})t^{-p-1}dt.
\]
Set \(a=e^{-t}\) and sum the two geometric series after multiplying by \((1-u)^2\):
\[
(1-u)^2F_p(u)=c_p\int_0^\infty t^{-p-1}(1-a)\frac{1-u}{1-au}\,dt.
\]
For \(0<a<1\), \(\operatorname{Re}[(1-u)/(1-au)]>0\) on the open unit disk. Indeed its boundary real part is \((1+a)(1-\cos\theta)/|1-ae^{i\theta}|^2\ge0\), and the harmonic minimum principle gives strict positivity inside. The integrand is dominated by an integrable bound: it is \(O(t^{-p})\) at zero and \(O(t^{-p-1})\) at infinity, uniformly on compact subdisks. Thus the integral has strictly positive real part. At \(p=1\), \((1-u)^2F_1(u)=1\).

**Half-plane certificate, intermediate exponents.** For \(1<p<2\), write \(q=p-1\in(0,1)\). Applying the preceding Bernstein identity to \(x^q\), but multiplying by \(x\), yields
\[
(1-u)^2F_p(u)=c_q\int_0^\infty t^{-q-1}\left[1-a\left(\frac{1-u}{1-au}\right)^2\right]dt.
\]
For fixed \(a\in(0,1)\), maximum modulus gives
\[
\sup_{|u|\le1} a\left|\frac{1-u}{1-au}\right|^2
=\frac{4a}{(1+a)^2}<1.
\]
(The boundary squared modulus is \(a(2-2\cos\theta)/(1+a^2-2a\cos\theta)\), decreasing in \(\cos\theta\), hence maximal at \(\theta=\pi\).) Every integrand consequently has positive real part. Convergence follows by cancellation of order \(O(t)\) at zero and the \(t^{-q-1}\) tail at infinity. At \(p=2\),
\[
(1-u)^2F_2(u)=\frac{1+u}{1-u},
\]
whose real part is positive in the open disk. Since \(1-u\) never vanishes there, the certificate proves zero-freeness for all \(0<p\le2\).

**Sharpness, first regime.** For real \(2<p<4\), the function \(F_p\) extends continuously from the interval \((-1,0]\) to \(-1\). Its Abel value is the continued alternating Dirichlet function
\[
F_p(-1)=\eta(-p)=(1-2^{p+1})\zeta(-p)<0.
\]
The strict sign holds because \(\zeta(-p)>0\) for \(2<p<4\), directly from the zeta functional equation and the sign of \(\sin(-\pi p/2)\). Since \(F_p(0)=1\), the intermediate value theorem gives a root \(u\in(-1,0)\).

**Sharpness, all remaining exponents.** For \(p\ge4\), put \(r=2^{1-p}\). Set \(a_n=(n+1)^p r^n\). For \(n\ge2\),
\[
\frac{a_{n+1}}{a_n}\le2(2/3)^p<1.
\]
The alternating tail from \(n=2\) is therefore bounded above by the truncation ending at the positive term \(n=4\). Consequently,
\[
F_p(-r)\le-1+4(3/4)^p-8(1/2)^p+16(5/16)^p=:U(p).
\]
Exactly \(U(4)=-335/4096<0\). The expression \(4(3/4)^p-8(1/2)^p\) is strictly decreasing for \(p\ge4\), because
\[
2\log2\,(2/3)^4<\log(4/3),
\]
and the final positive summand also decreases. Hence \(U(p)<0\) for all \(p\ge4\), so \(F_p\) again changes sign between \(-r\) and zero. This proves sharpness for every \(p>2\), including integral and nonintegral parameters.

## Verification

The included `checker.py` performs exact rational tests of the alternating-tail cutoff and the endpoint polynomial, checks gamma-moment identities at integer parameters, numerically compares the defining series with the continued polylogarithm, and confirms representative positive-real certificates and negative-real sign changes on both sides of the transition. It is supplementary: the uniform, infinite-dimensional statement follows from the analytical argument above, not finite computation.

## Relationship to prior work

Perälä (2017) develops radial Bergman-kernel zero constructions and the moment formulation; his general theorems do not state an exact classification for the present one-parameter logarithmic weights. Yamamori (2011), especially Proposition 1, records negative real zeros of the integer-order polylogarithm quotients for integers \(p\ge3\). Those integer cases are **prior art**, not claimed as novel. The present result covers *all real* \(p>0\) with a sharp cut at \(p=2\), and additionally proves an explicit positive-real certificate in the complete zero-free range. Zeytuncu (2010) treats zeros for certain bounded-comparable radial weights, unlike the present logarithmic singular/vanishing family. These comparisons are about exact statements, not just similarity of titles.

## Limitations

This is a zero-free versus existence classification only. It does not determine every zero, its multiplicity, or quantitative distance from the unit circle. No classification is claimed for other radial weights, several complex variables, or complex weight exponents. Numerical checks do not certify a global analytic theorem, and historical novelty has not received independent validation. The full literature may contain an equivalent fractional-polylogarithm theorem not identified in this search.

## References

1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (first public 2017-03-17), especially the moment representation and Section 3.
2. A. Yamamori, *Zeros of the Bergman kernel of the Fock-Bargmann-Hartogs domain and the interlacing property*, arXiv:1101.3135 (2011), especially Proposition 1 on negative-order integer polylogarithms.
3. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: \(L^p\) Regularity and Zeros*, arXiv:1009.2806 (2010).
4. S. Shimorin, *An Integral Formula for Weighted Bergman Reproducing Kernels*, Complex Variables 47 (2002), 1015–1028 (general integral-representation background, not a claim of identical logarithmic weights).
