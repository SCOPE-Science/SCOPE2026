# Arithmetic second-order boundary amplification in discrete quadratic least squares

## Finding
For every integer \(m\ge 2\), sample at the \(m+1\) equally spaced nodes \(x_j=-1+2j/m\), \(0\le j\le m\), and fit a real polynomial of degree at most two by unweighted least squares. Write \(\mathcal L_m(y)\) for the fitted polynomial's value at \(1\), and define its sharp bounded-data amplification by
\[
E_m=\sup_{\max_j|y_j|\le1}|\mathcal L_m(y)|.
\]
The exact finite-grid value is the Bernoulli-root formula below. In particular, with \(C=1+12\sqrt6/25\),
\[
E_m=C-\frac{54\sqrt6}{25m}
+\frac{\sqrt6}{m^2}\left(\frac{327}{50}-6\{B_2(\{m\alpha_-+\beta_-\})+B_2(\{m\alpha_++\beta_+\})\}\right)
+O(m^{-3}),
\]
where \(B_2(t)=t^2-t+1/6\) on \([0,1]\), \(\{t\}\) is fractional part, and
\[
\alpha_\pm=\frac{4\pm\sqrt6}{10},\qquad
\beta_\pm=-\frac3{10}\pm\frac{\sqrt6}{20}.
\]
The sharp and complete accumulation interval of the scaled second-order remainder is
\[
\boxed{\operatorname{Acc}_{m\to\infty}
\left[m^2\left(E_m-C+\frac{54\sqrt6}{25m}\right)\right]
=\left[\frac{227\sqrt6}{50},\frac{377\sqrt6}{50}\right].}
\]
Thus even after the constant and inverse-grid corrections are removed, the boundary sensitivity has no convergent second-order coefficient. Instead it fills a nondegenerate interval along subsequences; the phenomenon comes from two irrational kernel zeros crossing the uniform sampling lattice.

**Exact finite-grid expression.** Set \(h=1/m\), \(D_h=6+6h-11h^2\),
\[
r_\pm(h)=\frac{-1-3h\pm\sqrt{D_h}}5,\qquad
\theta_\pm=\left\{\frac{m(1+r_\pm(h))}{2}\right\},
\]
and \(B_3(t)=t^3-\tfrac32t^2+\tfrac12t\). Then, with no asymptotic qualification,
\[
\boxed{E_m=1+\frac{
\frac{2}{25}D_h^{3/2}-6h^2\sqrt{D_h}\,[B_2(\theta_-)+B_2(\theta_+)]
+20h^3[B_3(\theta_+)-B_3(\theta_-)]
}{(1+h)(1+2h)(1+3h)}.}
\]
This formula includes \(m=2\), when the fit interpolates the three data values. If a kernel root is a grid node, its zero contribution makes the fractional-part convention harmless.

## Assumptions and scope
The input data are arbitrary real values at the \(m+1\) **distinct** nodes specified above, and every node has equal positive least-squares weight. There is no smoothness or stochastic assumption. The output is **one boundary evaluation**, not the full supremum norm of the polynomial on the entire interval, nor a bound for interior evaluation rows. Complex data give the same induced modulus norm because the kernel coefficients are real. Every supremum is attained by data with signs matching the boundary reproducing kernel.

## Proof
**1. Exact reproducing kernel.** Give functions on the grid the probability inner product \(\langle f,g\rangle_m=(m+1)^{-1}\sum_{j=0}^mf(x_j)g(x_j)\). Reflection symmetry orthogonalizes \(1\), \(x\), and \(x^2-\mu_2\), where direct power summation gives
\[
\mu_2=\frac{1+2h}{3},\qquad
\mu_4=\frac15+\frac{4h}5+\frac{8h^2}{15}-\frac{8h^3}{15},\qquad
v=\mu_4-\mu_2^2=\frac4{45}(1-h)(1+2h)(1+3h)>0.
\]
The reproducing kernel for quadratic polynomials, evaluated at \(1\), is
\[
K_h(s)=1+\frac{s}{\mu_2}+\frac{(1-\mu_2)(s^2-\mu_2)}v
=A_hs^2+B_hs+C_h,
\]
with
\[
A_h=\frac{15}{2(1+2h)(1+3h)},\quad B_h=\frac3{1+2h},\quad
C_h=\frac{-3+6h}{2(1+3h)}.
\]
Therefore \(\mathcal L_m(y)=(m+1)^{-1}\sum_jK_h(x_j)y_j\) and \(E_m=(m+1)^{-1}\sum_j|K_h(x_j)|\). Also \((m+1)^{-1}\sum_jK_h(x_j)=1\).

**2. Two roots and a signed sum.** The quadratic has positive leading coefficient and roots \(r_-(h)<r_+(h)\) stated above; for every \(0<h\le1/2\), both lie in \([-1,1]\). Its only negative region is \((r_-(h),r_+(h))\). Hence
\[
E_m=1-\frac2{m+1}\sum_{r_-<x_j<r_+}K_h(x_j).
\]
The maximizing data may be chosen \(y_j=\operatorname{sgn}K_h(x_j)\). Put \(\delta=2h\) and \(u_\pm=(1+r_\pm)/\delta\). The exact quadratic Euler-summation identity, obtained directly by applying the elementary sums of \(1\), \(j\), and \(j^2\) between the two floor indices, is
\[
\begin{aligned}
\delta\sum_{r_-<x_j<r_+}K_h(x_j)
={}&\int_{r_-}^{r_+}K_h(s)\,ds\\
&+\frac{\delta^2}2\{B_2(\theta_+)K_h'(r_+)-B_2(\theta_-)K_h'(r_-)\}\\
&-\frac{\delta^3}6 K_h''\{B_3(\theta_+)-B_3(\theta_-)\}.
\end{aligned}
\]
It remains valid when an endpoint is an integer grid index because the values vanish at both roots and the periodic Bernoulli endpoint conventions coincide. To see it without asymptotics, write the finite sum as \(F(\lfloor u_+\rfloor+1)-F(\lfloor u_-\rfloor+1)\), where \(F(z)\) is the degree-three polynomial extending \(\sum_{j=0}^{z-1}K_h(-1+\delta j)\), and Taylor-expand \(F\) exactly about \(u_\pm\).

Set \(d_h=r_+-r_-=(2/5)\sqrt{D_h}\). Because \(K_h(s)=A_h(s-r_-)(s-r_+)\),
\[
\int_{r_-}^{r_+}K_h(s)\,ds=-\frac{A_hd_h^3}{6},\quad
K_h'(r_\pm)=\pm A_hd_h,\quad K_h''=2A_h.
\]
Substitution, together with \(B_2(1-t)=B_2(t)\) and \(B_3(1-t)=-B_3(t)\), gives the displayed **exact** formula.

**3. Uniform expansion.** Since \(B_2\) and \(B_3\), periodically extended by fractional parts, are bounded, the cubic Bernoulli term is uniformly \(O(m^{-3})\). Taylor expansion of the smooth bulk factor gives
\[
\frac{(2/25)D_h^{3/2}}{(1+h)(1+2h)(1+3h)}
=\frac{12\sqrt6}{25}-\frac{54\sqrt6}{25}h+\frac{327\sqrt6}{50}h^2+O(h^3).
\]
The roots satisfy
\[
r_\pm(h)=\frac{-1\pm\sqrt6}{5}+h\left(-\frac35\pm\frac{\sqrt6}{10}\right)+O(h^2).
\]
Consequently \(u_\pm=m\alpha_\pm+\beta_\pm+O(m^{-1})\). The periodic \(B_2\) is globally Lipschitz, including across integers, so replacing \(B_2(\theta_\pm)\) by \(B_2(\{m\alpha_\pm+\beta_\pm\})\) changes the expansion only by \(O(m^{-3})\). This proves the displayed second-order formula with a uniform remainder.

**4. Exact accumulation interval.** For all \(t\), \(-1/12\le B_2(\{t\})\le1/6\). Every limit point is therefore within the displayed interval. For \(m\equiv2\pmod5\), the phase sums satisfy
\[
(m\alpha_++\beta_+)+(m\alpha_-+\beta_-)=\frac{4m-3}{5}\in\mathbb Z.
\]
Thus the two Bernoulli values coincide by \(B_2(1-t)=B_2(t)\), and their sum is exactly \(2B_2(\{m\alpha_++\beta_+\})\). Since \(5\alpha_+=(4+\sqrt6)/2\) is irrational, the latter fractional parts are dense in \([0,1]\) along \(m\equiv2\pmod5\). Continuity of the periodic Bernoulli polynomial shows that every value from \(-1/6\) to \(1/3\) occurs as a subsequential limit of the sum. The affine transformation in the second-order expansion yields every point of the stated closed interval, including both endpoints.

## Verification
The accompanying standard-library Python checker `verify.py` independently reconstructs the discrete moments with exact fractions, confirms the reproducing kernel and row normalization for all \(2\le m\le120\), compares the Bernoulli expression with exact rational endpoint row sums at 85 decimal digits, and tests the second-order expansion at six larger grids. It reports 8,461 passed finite assertions. The infinite exact identity and complete accumulation interval follow from the proof, not from these finite tests.

## Relationship to prior work
Bos, Calvi, Levenberg, Sommariva, and Vianello (first public preprint February 2009) provide general discrete least-squares and admissible-mesh stability methods but not the boundary-specific exact quadratic kernel sum or its arithmetic second-order limit set. Cohen, Davenport, and Leviatan (first public preprint November 2011) develop stability conditions for least-squares approximation, including equispaced data, with different global and stochastic control quantities. Adcock, Platte, and Shadrin study general grid-conditioned approximation and sampling-rate estimates rather than the stated fixed-degree, sharp endpoint operator norm. Białas-Cież, Kenne, Sommariva, and Vianello give rigorous numerical Lebesgue-constant evaluation methods, not this exact arithmetic expansion. Related sharp finite-projection norms on Boolean schemes and cyclic Fourier bands have different kernels, sample spaces and asymptotic regimes, so their formulas do not imply this result.

## Limitations
The theorem is specific to degree two, equal sample weights, a uniform closed-interval grid, and boundary evaluation. It does **not** determine the full uniform norm of the least-squares polynomial operator, nor its value at interior locations or with arbitrary perturbed nodes. The references examined do not certify historical priority. In particular, an older calculation in the Gram-polynomial, discrete-Christoffel or endpoint Lebesgue-function literature may be equivalent despite different terminology. The full texts of the particularly relevant Calvi--Levenberg (2008) and Reichel (1986; earlier technical report dated 1983) works were not accessible; neither is claimed to exclude the result. No independent mathematical audit has been performed.

## References
1. L. Bos, J.-P. Calvi, N. Levenberg, A. Sommariva and M. Vianello, *Geometric weakly admissible meshes, discrete least squares approximations and approximate Fekete points*, arXiv:0902.0215 (first version 2009-02-02), https://arxiv.org/pdf/0902.0215.
2. A. Cohen, M. A. Davenport and D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422 (first version 2011-11-18), https://arxiv.org/pdf/1111.4422.
3. B. Adcock, R. B. Platte and A. Shadrin, *Optimal sampling rates for approximating analytic functions from pointwise samples*, arXiv:1610.04769 (first version 2016-10-15), https://arxiv.org/pdf/1610.04769.
4. L. Białas-Cież, D. J. Kenne, A. Sommariva and M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656 (2023-11-30), https://arxiv.org/pdf/2311.18656.
5. J.-P. Calvi and N. Levenberg, *Uniform approximation by discrete least squares polynomials*, J. Approx. Theory 152 (2008), 82--100, DOI 10.1016/j.jat.2007.05.005 (bibliographic record; full text unavailable).
6. L. Reichel, *On polynomial approximation in the uniform norm by the discrete least squares method*, BIT 26 (1986), 349--366, with an earlier 1983 technical-report record ADA127693 (abstract only available).
