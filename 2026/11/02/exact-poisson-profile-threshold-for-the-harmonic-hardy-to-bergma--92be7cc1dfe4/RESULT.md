# Exact Poisson-profile threshold for the harmonic Hardy-to-Bergman fourth-power embedding

## Finding
Let \(\mathcal C\) be the fourth-power operator norm of the inclusion of complex harmonic \(h^2(\mathbb D)\) into \(L^4(\mathbb D,dA/\pi)\), as defined below. Then
\[
\frac52\le \mathcal C\le\frac{3+2\sqrt2}{2}.
\]
The lower bound is the **exact, nonattained supremum over normalized harmonic Poisson kernels**. More precisely, for \(0<\rho<1\), put \(P_\rho(z)=\operatorname{Re}\left(\frac{1+\rho z}{1-\rho z}\right)\) and \(f_\rho=P_\rho/\|P_\rho\|_{h^2}\). Define \(x=\rho^2\) and
\[
R(x)=\frac{(1-x)^2}{x(1+x)^2}\left(-x-12\log(1-x)+20-\frac{30}{1-x}+\frac{10}{(1-x)^2}\right).
\]
Then \(\|f_\rho\|_{L^4(dA/\pi)}^4=R(\rho^2)\); the function \(R\) extends continuously to \(R(0)=1\), is strictly increasing on \((0,1)\), and tends to \(5/2\) as \(x\uparrow1\). Rotating the Poisson kernel does not change its value. Hence this natural concentration family supplies a concrete nonholomorphic lower barrier for the sharp Hardy-to-Bergman inequality.

## Assumptions and scope
On \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let \(dA/\pi\) denote normalized Euclidean area and \(dm=d\theta/(2\pi)\) normalized boundary measure. For harmonic \(f\) with \(L^2\) boundary trace let \(\|f\|_{h^2}^2=\int_{\partial\mathbb D}|f^*|^2dm\). Let
\[
\mathcal C=\sup_{0\ne f\in h^2(\mathbb D)}\frac{\int_{\mathbb D}|f(z)|^4dA(z)/\pi}{\|f\|_{h^2}^4}.
\]
The claim holds for all complex harmonic functions, by use of an explicit real harmonic subclass; the upper bound is the existing general theorem. It does **not** assert \(\mathcal C=5/2\), and it does not assert a global extremizer.

## Proof
Write \(P_\rho(re^{i\theta})=(1-\rho^2r^2)/|1-\rho re^{i\theta}|^2\). Its boundary Fourier series is \(1+\sum_{n\ge1}\rho^n(e^{in\theta}+e^{-in\theta})\), so Parseval gives
\[
\|P_\rho\|_{h^2}^2=1+2\sum_{n\ge1}\rho^{2n}=\frac{1+\rho^2}{1-\rho^2}.
\]
For \(0\le q<1\), the absolutely convergent binomial series for \((1-qe^{i\theta})^{-4}\) and its conjugate give
\[
\frac1{2\pi}\int_0^{2\pi}\left(\frac{1-q^2}{|1-qe^{i\theta}|^2}\right)^4d\theta
=(1-q^2)^4\sum_{k\ge0}\binom{k+3}{3}^2q^{2k}
=\frac{1+9q^2+9q^4+q^6}{(1-q^2)^3}.
\]
The final equality follows by applying the coefficient recurrence \((k+1)^2a_{k+1}=(k+4)^2a_k\), \(a_0=1\), to the rational generating function; this proves the identity for the entire convergence disk. Radial integration \(dA/\pi=2r\,dr\,dm\) with \(u=\rho^2r^2\) yields
\[
\|P_\rho\|_{L^4(dA/\pi)}^4=\frac1x\int_0^x\frac{1+9u+9u^2+u^3}{(1-u)^3}\,du.
\]
An elementary antiderivative, normalized to vanish at zero, is
\[
I(x)=-x-12\log(1-x)+20-\frac{30}{1-x}+\frac{10}{(1-x)^2}.
\]
Dividing by the square of the boundary \(h^2\) norm gives the stated \(R\). Differentiation gives
\[
R'(x)=\frac{4N(x)}{x^2(1+x)^3},\quad
N(x)=3(x-1)(x^2-4x-1)\log(1-x)-9x^3+11x^2+3x.
\]
Expansion at zero produces the *globally convergent, termwise positive* series
\[
N(x)=\frac{x^2}2+\frac{x^3}2+\sum_{k=4}^\infty\frac{6(2k^2-8k+3)}{k(k-1)(k-2)(k-3)}x^k.
\]
Every coefficient is positive since \(2k^2-8k+3>0\) for integer \(k\ge4\). Hence \(R'(x)>0\) on \((0,1)\). The integral expression yields \(R(0)=1\), and \(I(x)\sim10/(1-x)^2\) yields \(R(x)\to10/4=5/2\). The supremum over Poisson profiles equals \(5/2\) and is not attained within this family. It is a lower bound for \(\mathcal C\) since each \(f_\rho\) is an admissible harmonic function. The 2026 Das–Rasila–Zhu inclusion theorem with \(p=m=2\) gives \(\mathcal C\le(\sqrt2\cos(\pi/8))^4=(3+2\sqrt2)/2\).

## Verification
Run `python verify_poisson.py` with Python 3 and SymPy. The program verifies the binomial-generating-function differential equation with initial condition, rational fourth-moment identity, antiderivative, derivative, series coefficient formula, and end-point limit symbolically. This is an algebraic cross-check; the analytic justification of termwise integration and positivity is given above.

## Relationship to prior work
Das, Rasila and Zhu (arXiv:2606.31024v1, June 30, 2026), Theorem 1.1 and Problem 7.1, give an upper bound and ask for its sharpness, noting the elementary lower bound \(1\) and suggesting normalized Szegő kernels as potential probes. The present result evaluates a related normalized *real Poisson harmonic* family explicitly and obtains the larger quantitative obstruction \(5/2\), together with exact strict monotonicity. It does not settle the universal best constant and is distinct from their upper-bound argument. Earlier work by Kalaj and Meštrović (2011) and Kalaj (2019) establishes harmonic Carleman/Riesz-type inequalities; full texts of those particular comparisons were not inspected, so implicit coverage of this specific Poisson-family computation remains possible.

## Limitations
The supremum over this one-parameter family is not necessarily the full operator norm, and the proof does not characterize general extremizing sequences. The lower bound is independent of domain dimension by embedding the function into one polydisc coordinate; no stronger dimension-specific bound is claimed. Historical prior-art verification is incomplete for relevant earlier full texts, which remain a disclosed originality risk. No independent audit has been performed.

## References
1. S. Das, A. Rasila, J.-F. Zhu, *Isoperimetric-type inequalities for pluriharmonic functions on the polydisc*, arXiv:2606.31024v1 (June 30, 2026), Theorem 1.1 and Problem 7.1. https://arxiv.org/abs/2606.31024
2. D. Kalaj and R. Meštrović, *Isoperimetric type inequalities for harmonic functions*, Journal of Mathematical Analysis and Applications **373** (2011), 439–448, DOI:10.1016/j.jmaa.2010.08.009 (metadata/abstract comparison only).
3. D. Kalaj, *On Riesz type inequalities for harmonic mappings on the unit disk*, Transactions of the American Mathematical Society **372** (2019), 4031–4051, arXiv:1701.04785 (abstract comparison only).
