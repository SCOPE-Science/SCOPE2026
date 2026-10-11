# Sharp square-root boundary law for center-conditioned harmonic Bohr radii

## Finding

Let \(\mathbb D\) be the unit disk. For \(0\le a\le1\), consider all complex-valued harmonic functions
\[
f:\mathbb D\longrightarrow\overline{\mathbb D},\qquad |f(0)|=a.
\]
Every such function has the canonical harmonic Fourier expansion
\[
f(re^{it})=c_0+\sum_{n\ge1}\bigl(c_n r^n e^{int}+c_{-n}r^n e^{-int}\bigr),
\]
where \(|c_0|=a\). Define the harmonic Bohr majorant and center-conditioned Bohr radius by
\[
B_f(r)=a+\sum_{n\ge1}(|c_n|+|c_{-n}|)r^n,
\]
\[
R_H(a)=\sup\bigl\{r\in[0,1): B_f(r)\le1\ \text{for every such }f\bigr\}.
\]

For every \(0\le a<1\), the following **quantitative universal lower bound** holds:
\[
\boxed{R_H(a)\ge\sqrt{\frac{1-a}{3+a}}}.
\]
This improves strictly, at every \(a<1\), the expression
\[
\rho(a)=\frac{1-a}{1-a+4/\pi}
\]
called the sharp bounded-harmonic radius in Theorem 2.1 of Ahamed and Hossain (2026).

Moreover, the new bound has the **exact optimal boundary order and leading constant**:
\[
\boxed{\lim_{a\uparrow1}\frac{R_H(a)}{\sqrt{1-a}}=\frac12}.
\]
Thus the best fixed-center radius shrinks on the square-root scale rather than the linear scale of \(\rho(a)\). At the terminal value, all functions are constant and
\[
R_H(1)=1,
\]
so the fixed-center radius jumps discontinuously at \(a=1\).

## Assumptions and scope

The class contains **all** complex-valued harmonic functions bounded in modulus by one; no sense-preserving, univalent, quasiconformal or bounded-analytic-part hypothesis is imposed. This is the normalization of the bounded-harmonic fixed-center problem in the cited recent preprint with \(M=1\). Scaling handles any positive bound \(M\).

The coefficients \(c_{-n}\) are boundary Fourier coefficients of negative index, equivalent in modulus to the conjugate analytic coefficients in the usual decomposition \(f=h+\overline g\). The majorant uses both signs exactly as in the source.

The bound is global for \(0\le a<1\). Sharpness claimed here concerns the **asymptotic leading constant** as \(a\uparrow1\); an exact expression for \(R_H(a)\) for every other parameter is not established.

## Proof

**1. A coefficient-energy inequality.** A bounded complex-valued harmonic function has a radial boundary function \(F\in L^\infty(\mathbb T)\), with \(|F|\le1\) almost everywhere and \(f=P[F]\). The coefficients \(c_n\) are its Fourier coefficients, with normalized arc measure. Parseval therefore gives
\[
\sum_{n\in\mathbb Z}|c_n|^2
=\frac1{2\pi}\int_0^{2\pi}|F(e^{it})|^2\,dt
\le1.
\]
Since \(|c_0|=a\),
\[
\sum_{n\ne0}|c_n|^2\le1-a^2.
\]
Apply Cauchy--Schwarz to the positive and negative Fourier indices, using their common radial weights:
\[
\begin{aligned}
B_f(r)-a
&=\sum_{n\ge1}(|c_n|+|c_{-n}|)r^n\\
&\le\left(\sum_{n\ne0}|c_n|^2\right)^{1/2}
\left(2\sum_{n\ge1}r^{2n}\right)^{1/2}\\
&\le\sqrt{2(1-a^2)}\frac r{\sqrt{1-r^2}}.
\end{aligned}
\]
For \(0\le a<1\), the right side is at most \(1-a\) whenever
\[
2(1-a^2)r^2\le(1-a)^2(1-r^2),
\]
which is equivalent to
\[
r^2\le\frac{1-a}{3+a}.
\]
This proves the universal lower bound. It yields
\[
\liminf_{a\uparrow1}\frac{R_H(a)}{\sqrt{1-a}}\ge\frac12.
\]

**2. A matching unimodular boundary family.** For small \(\varepsilon>0\), define
\[
F_\varepsilon(e^{it})=e^{i\varepsilon\cos t},
\qquad f_\varepsilon=P[F_\varepsilon].
\]
Because \(|F_\varepsilon|=1\), its Poisson extension satisfies \(|f_\varepsilon(z)|\le1\). Since the trace is even in \(t\), the first positive and negative Fourier coefficients coincide. Taylor expansion, with uniform remainder on the circle and parity cancellation in the integrals, yields
\[
\begin{aligned}
c_0(\varepsilon)
&=\frac1{2\pi}\int_0^{2\pi}e^{i\varepsilon\cos t}\,dt
=1-\frac{\varepsilon^2}{4}+O(\varepsilon^4),\\
c_1(\varepsilon)=c_{-1}(\varepsilon)
&=\frac1{2\pi}\int_0^{2\pi}e^{i\varepsilon\cos t}e^{-it}\,dt
=\frac{i\varepsilon}{2}+O(\varepsilon^3).
\end{aligned}
\]
For sufficiently small positive \(\varepsilon\), \(c_0(\varepsilon)>0\), and its derivative is
\[
c_0'(\varepsilon)=-\frac\varepsilon2+O(\varepsilon^3)<0.
\]
Thus every \(a<1\) sufficiently close to one is uniquely of the form \(a=c_0(\varepsilon)\) with small \(\varepsilon>0\). Put
\[
A_\varepsilon=|c_1(\varepsilon)|+|c_{-1}(\varepsilon)|
=\varepsilon+O(\varepsilon^3).
\]
Since all terms of the majorant are nonnegative,
\[
B_{f_\varepsilon}(r)\ge a+A_\varepsilon r.
\]
For any \(r>(1-a)/A_\varepsilon\), this explicit admissible map violates the Bohr inequality. Consequently,
\[
R_H(a)\le\frac{1-a}{A_\varepsilon}.
\]
Now
\[
1-a=\frac{\varepsilon^2}{4}+O(\varepsilon^4),
\qquad
\frac{1-a}{A_\varepsilon}
=\left(\frac12+o(1)\right)\sqrt{1-a}.
\]
This proves the complementary limsup and therefore the exact boundary limit \(1/2\).

**3. Strict comparison with the reported radius.** Set \(t=1-a\), so \(0<t\le1\). Since \(4/\pi>1\),
\[
(t+4/\pi)^2>(t+1)^2>t(4-t),
\]
where the second strict inequality is exactly
\[
(t+1)^2-t(4-t)=1-2t+2t^2>0.
\]
Taking positive square roots and dividing gives
\[
\frac{t}{t+4/\pi}<\sqrt{\frac{t}{4-t}}
=\sqrt{\frac{1-a}{3+a}}\le R_H(a).
\]
Thus the reported sharpness expression is strictly below an admissible universal radius for **every** nonterminal center value.

**4. The terminal center.** If \(|f(0)|=1\), rotate \(f\) so \(f(0)=1\). The real-valued harmonic function \(\operatorname{Re}f\le1\) attains its maximum at the origin. The harmonic maximum principle forces \(\operatorname{Re}f\equiv1\), and the bound \(|f|\le1\) then forces \(f\equiv1\). Its majorant is identically one, so the supremum of admissible radii is \(R_H(1)=1\). On the other hand, the proved boundary limit implies \(R_H(a)\to0\) as \(a\uparrow1\). Hence the jump.

## Verification

The coefficient energy estimate is an exact Fourier Parseval identity for the \(L^\infty\) boundary trace, followed by one Cauchy--Schwarz inequality; no assumption of simultaneous coefficient saturation is made. The comparison with the published expression is a strict elementary inequality on the entire parameter range.

The matching family is an explicit Poisson extension of unimodular smooth boundary data. The mean and first coefficients can be checked directly by integrating the Taylor expansion of \(e^{i\varepsilon\cos t}\). The bounds are uniform as \(\varepsilon\downarrow0\), and only these first two harmonics are needed to force the sharp asymptotic constant.

High-precision numerical evaluations of the corresponding Bessel-integral formulas and the lower bound were used as consistency checks only. The analytic argument alone proves the continuum statement.

## Relationship to prior work

Ahamed and Hossain's 2026 preprint, Theorem 2.1, uses separately sharp degreewise bounded-harmonic coefficient estimates to obtain \((1-a)/(1-a+4/\pi)\). It declares this a best-possible fixed-center radius. Its proof does not control the simultaneous coefficient energy. The present result retains the same class and coefficient majorant but exploits Parseval across all Fourier modes, proving a strictly larger globally admissible radius and determining its exact leading rate near \(a=1\).

Abu Muhanna's 2010 paper proves a phase-adjusted Bohr inequality for bounded complex harmonic maps and explains that **no single positive radius** works for the absolute constant-plus-majorant inequality uniformly over all center values. This is compatible with \(R_H(a)\to0\); it neither specifies the sharp fixed-center decay rate nor the constant \(1/2\). Its known negative uniform-radius conclusion is not presented as new here.

Abu Muhanna and collaborators' 2014 Bohr study gives harmonic and subordination inequalities, including a different phase-dependent harmonic bound, but does not establish the exact near-one fixed-center radius asymptotic. Kayumov--Ponnusamy--Shakirov (2018) and Alkhaleefah--Kayumov--Ponnusamy (2019) consider more restrictive harmonic subclasses with analytic or quasiconformal assumptions, so their bounds do not settle the full complex-valued bounded-harmonic problem here.

The result addresses a sharpness question for a natural center-conditioned invariant, not the distinct \(L^p\)-dependent formula later in Ahamed--Hossain's preprint. Searches for fixed-center absolute Fourier majorants, square-root boundary laws, and unimodular Poisson witnesses found no literature statement implying this exact asymptotic law.

## Limitations

No closed formula for \(R_H(a)\) at every fixed \(a<1\) is claimed, and the global lower bound need not be optimal away from \(a=1\). The coefficient-energy inequality is sharp to leading order at the endpoint but not asserted to be attained by a nonconstant map for a fixed interior radius.

The conclusion concerns all bounded complex harmonic mappings with unrestricted analytic and coanalytic parts. It is not a theorem about sense-preserving maps, analytic-only maps, or harmonic maps with separately bounded analytic parts.

The discontinuity at \(a=1\) concerns the **exact center-conditioned radius**; it is not a claim about any alternative radius convention in which the endpoint is defined by continuity.

## References

1. M. B. Ahamed and R. Hossain, *Bohr Radius and Landau-type Theorems for Harmonic Mappings with Boundary Functions in Lebesgue Spaces*, arXiv:2604.14217v1, first posted 12 April 2026; especially Theorem 2.1 and its sharpness argument.
2. Y. Abu Muhanna, *Bohr's phenomenon in subordination and bounded harmonic classes*, Complex Variables and Elliptic Equations 55 (2010), 1071–1078, DOI: 10.1080/17476931003628190, especially Theorem 2 and Remark 3.
3. Y. Abu Muhanna et al., *Bohr radius for subordinating families of analytic functions and bounded harmonic mappings*, Journal of Mathematical Analysis and Applications 420 (2014), 124–136, DOI: 10.1016/j.jmaa.2014.05.076.
4. I. R. Kayumov, S. Ponnusamy, and N. Shakirov, *Bohr radius for locally univalent harmonic mappings*, Mathematische Nachrichten 291 (2018), 1757–1768, DOI: 10.1002/mana.201700068.
5. S. A. Alkhaleefah, I. R. Kayumov, and S. Ponnusamy, *On the Bohr inequality with a fixed zero coefficient*, arXiv:1903.12646v1 (2019).
