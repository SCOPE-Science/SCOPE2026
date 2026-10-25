# Six-dimensional spherical-cap Fourier nulls from an incomplete-gamma boundary layer

## Finding
For \(h\in(-1,1)\), define the solid six-dimensional spherical cap
\[
 C_h=\{(y,s)\in\mathbb R^5\times\mathbb R:\ |y|^2+s^2<1,\ s>h\}.
\]
For the Fourier convention \(\widehat{\mathbf1_{C_h}}(\xi)=\int_{C_h}e^{-i\xi\cdot x}\,dx\), there are infinitely many distinct levels \(h_n\in(-1,1)\), tending to \(-1\), whose transforms have a genuine real zero on the cap axis at \(\xi_n=(0,\ldots,0,t_n)\), with \(t_n>0\). More precisely, for every sufficiently large positive integer \(n\), one such zero is locally unique and
\[
 t_n=\pi n+\theta_*+O(n^{-1}),\qquad
 h_n=-1+\frac{c_*}{\pi n}+O(n^{-2}).
\]
Here \(c_*\) is the **unique** solution in \((9/10,1)\) of
\[
 |\Gamma(7/2,i c_*)|=\Gamma(7/2),
\]
where the upper incomplete gamma uses the principal branch; \(c_*=0.96131491167342160479\ldots\). Set
\[
 a_*=e^{-7\pi i/4}\Gamma(7/2,ic_*),\qquad
 b_*=e^{7\pi i/4}\Gamma(7/2),\qquad
 e^{2i\theta_*}=-b_*/a_*,\quad 0\le\theta_*<\pi.
\]
Then \(\theta_*=0.74848728058477646099\ldots\). Local uniqueness means one real zero pair \((h,t)\) in each sufficiently small, fixed scaled neighborhood of \((c_*,\theta_*)\), with scaled variables \(c=t(h+1)\) and \(\theta=t-\pi n\). No global enumeration of other zeros is claimed.

## Assumptions and scope
The dimension is exactly six; \(h\in(-1,1)\) cuts a **solid** unit ball, not its surface, and the frequency is restricted to the real symmetry axis. The overall positive cross-sectional factor \(|B_5(1)|\) does not affect zeros. With \(\alpha=5/2\) and \(s=\alpha+1=7/2\), the axial transform equals
\[
 |B_5(1)|\,F_h(t),\qquad F_h(t)=\int_h^1(1-u^2)^{5/2}e^{-itu}\,du.
\]
The source motivating this problem is the classical study of real Fourier null varieties of convex domains; the present result concerns a specific nonsymmetric family and does not imply global null-variety classifications.

## Proof
**1. Endpoint scaling.** Put \(t=\pi n+\theta\) and \(h=-1+c/t\), with \(c\) in a fixed compact subset of \((0,\infty)\) and \(\theta\) in a bounded interval. The complete-ball integral has the exact Bessel representation
\[
 F_{-1}(t)=\sqrt\pi\,\Gamma(7/2)(2/t)^3J_3(t),
\]
because \(\int_{-1}^1(1-u^2)^{\nu-1/2}e^{-itu}du=\sqrt\pi\Gamma(\nu+1/2)(2/t)^\nu J_\nu(t)\), here \(\nu=3\). Its standard large-real-argument expansion gives
\[
 \frac{t^{7/2}}{2^{5/2}}F_{-1}(t)
 =2\Gamma(7/2)\cos(t-7\pi/4)+O(t^{-1}),
\]
with the same order for a \(t\)-derivative of the remainder on bounded phase ranges. The missing bottom tip, after \(u=-1+v/t\), satisfies
\[
 \frac{t^{7/2}}{2^{5/2}}\int_{-1}^{-1+c/t}(1-u^2)^{5/2}e^{-itu}du
 =e^{it}\int_0^c v^{5/2}e^{-iv}(1-v/(2t))^{5/2}\,dv
 =e^{it}i^{-7/2}\gamma(7/2,ic)+O(t^{-1}).
\]
The errors and their first derivatives with respect to \(c\) and \(\theta\) are uniform on such compact rectangles (the tip is a bounded-interval integral and the Bessel remainder is differentiable). Subtraction gives the \(C^1\) limit
\[
 \frac{(-1)^n t^{7/2}}{2^{5/2}}F_{-1+c/t}(t)
 \longrightarrow L(c,\theta):=e^{i\theta}a(c)+e^{-i\theta}b,
\]
where \(a(c)=i^{-7/2}\Gamma(7/2,ic)\) and \(b=i^{7/2}\Gamma(7/2)\).

**2. A simple amplitude crossing.** Write \(s=7/2\), \(K=8/(15\sqrt{2\pi})\), and
\[
 U(c)=\sum_{m\ge0}\frac{(-1)^m c^{2m}}{(2m)!(s+2m)},\qquad
 V(c)=\sum_{m\ge0}\frac{(-1)^m c^{2m+1}}{(2m+1)!(s+2m+1)}.
\]
The lower incomplete-gamma series yields
\[
 \frac{\gamma(s,ic)}{\Gamma(s)}=Kc^{7/2}[(U-V)-i(U+V)],
\]
and thus
\[
 \frac{|\Gamma(s,ic)|^2}{\Gamma(s)^2}-1
 =2Kc^{7/2}H(c),\qquad
 H(c)=Kc^{7/2}(U(c)^2+V(c)^2)-U(c)+V(c).
\]
The completely explicit alternating-series rational enclosures in `check.py` give
\[
 -0.022109<H(9/10)<-0.021986,\qquad
 0.014097<H(1)<0.014256.
\]
For completeness, these signs use only \(0.212<K<0.214\), \(0.948<\sqrt{0.9}<0.949\), and the first seven alternating terms with remainder bounded by the next term. Moreover, for \(9/10\le c\le1\), alternating-series estimates yield
\[
 0<U\le2/7,\quad0<V\le2/9,\quad
 -2/11\le U'<0,\quad0<V'\le2/9,
\]
with \(-U'+V'\ge0.9/(11/2)-1/[6(15/2)]+2/9-1/13\). The absolute value of the derivative of \(Kc^{7/2}(U^2+V^2)\) is at most
\[
 \frac{107}{500}\left[\frac72\left(\frac4{49}+\frac4{81}\right)+2\left(\frac4{77}+\frac4{81}\right)\right].
\]
Their difference exceeds \(0.145\). Consequently \(H'(c)>0.145\) on that interval. The intermediate value theorem supplies exactly one \(c_*\in(9/10,1)\), and the derivative proves the amplitude crossing is transverse.

**3. Exact zeros by the implicit function theorem.** At \(c=c_*\), \(|a(c_*)|=|b|\), and the displayed definition of \(\theta_*\) makes \(L(c_*,\theta_*)=0\). Its real two-variable Jacobian in \((c,\theta)\) is nonzero: varying \(\theta\) changes the relative phase, whereas \(\partial_c|a(c)|^2\ne0\) changes the modulus to first order. The \(C^1\) convergence from step 1 and the implicit-function theorem therefore give unique nearby roots \((c_n,\theta_n)=(c_*,\theta_*)+O(n^{-1})\) of the actual, not truncated, integral for all sufficiently large \(n\). Translating \(t_n=\pi n+\theta_n\) and \(h_n=-1+c_n/t_n\) proves the two expansions. Distinct large \(n\) give distinct positive frequencies and levels tending to \(-1\).

## Verification
`check.py` uses exact rational fractions and alternating remainder bounds for the two decisive signs, and an exact rational derivative lower bound exceeding \(0.145\); these constitute a finite algebraic certificate of the nondegenerate crossing. It additionally computes the incomplete-gamma constant and three illustrative finite-frequency zeros (at indices \(10,20,40\)) with high-precision numerical quadrature. Run `python check.py` with Python 3 and `mpmath`. `checker_output.txt` is the recorded result. Numerical witnesses do not establish the infinite sequence; the analytic endpoint expansion and implicit-function theorem do.

## Relationship to prior work
Benguria, Levitin and Parnovski (2008/2009) develop the Fourier-null-variety viewpoint for convex domains, with the ball's Bessel transform as an explicit standard example, but their accessible full manuscript does not give this six-dimensional truncated-ball endpoint bifurcation. Later work by Gómez-Serrano, Levitin, Platt and Polterovich (2026) investigates a different isoperimetric Fourier-zero problem for centrally symmetric convex bodies; its accessible abstract alone is insufficient to assess all possible related details. Searches for partial balls, spherical segments, characteristic functions and incomplete-gamma amplitude matching did not reveal a directly covering theorem. The calculation specializes to a noncentrally symmetric, dimension-six convex family; it is not implied by results for complete balls or generic balanced bodies.

## Limitations
Only one local family of genuine axial zeros is established, not an exhaustive zero set at a fixed cap height, nor a complete dimension threshold. The constant is uniquely characterized within \((9/10,1)\); possible additional positive solutions of the amplitude equation are not excluded. Directly covering older results in unsearched or inaccessible sources remain possible; this report does not assert publication priority or independent review. Numerical examples are supporting checks, not proofs of asymptotic claims.

## References
1. R. Benguria, M. Levitin, L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, arXiv:0801.1617 (first posted 2008-01-10), especially Introduction and Section 3.
2. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517 (2026-09-09); relevant later contextual work, abstract assessed only.
3. Classical Fourier–Bessel integral identity and large-argument Bessel asymptotic, as stated and normalized in the proof (cf. the standard special-functions formulas used for the ball in Reference 1).
