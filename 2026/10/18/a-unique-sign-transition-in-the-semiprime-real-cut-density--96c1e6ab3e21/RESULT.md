# A unique sign transition in the semiprime real-cut density

## Finding

Use the real-axis boundary-value normalization for the prime-zeta Möbius series introduced in Belton [1]:
\[
 U(t)=\sum_{n\geq1}\frac{\mu(n)}{n}\log|\zeta(nt)|,
 \qquad \tfrac12<t<1.
\]
Let \(\Delta_2\) be the semiprime jump density of [1]. Then \(\Delta_2(t)=U(t)\) throughout \(\tfrac12<t<1\). The following statements hold without any unproved hypotheses.

**Density sign transition.** The function \(U\) is continuously differentiable and strictly increasing on \((\tfrac12,1)\), with
\[
 \lim_{t\downarrow1/2}U(t)=-\infty,
 \qquad \lim_{t\uparrow1}U(t)=+\infty.
\]
Consequently there is exactly one \(\tau\in(\tfrac12,1)\) such that \(\Delta_2(\tau)=0\). Moreover, \(\Delta_2(t)<0\) for \(\tfrac12<t<\tau\), and \(\Delta_2(t)>0\) for \(\tau<t<1\).

**Integrated sign transition.** The upper-real-cut semiprime contribution explicitly isolated in [1] is
\[
 B(x)=\int_{1/2}^{1}\frac{U(t)x^t}{t}\,dt,\qquad x>0.
\]
There exists exactly one \(\xi>0\) such that \(B(\xi)=0\). One has \(B(x)<0\) for \(0<x<\xi\) and \(B(x)>0\) for \(x>\xi\). More strongly, the normalization
\[
 y\longmapsto e^{-\tau y}B(e^y)
\]
is strictly increasing from \(-\infty\) to \(+\infty\) on the entire real line.

## Assumptions and scope

Here \(\mu\) is the integer Möbius function, \(\zeta\) the meromorphic Riemann zeta function, and all logarithms are natural logarithms of positive real numbers. In particular \(\zeta(t)<0\) for \(\tfrac12<t<1\), so the absolute value in the first term is essential. Belton defines \(A(v)=\sum_{n\leq v}\mu(n)/n\), \(a_j(t)=A(1/(jt))\), and \(\Delta_2(t)=a_1(t)U(t)+\tfrac12a_2(t)\) [1, equations (4)--(5)]. For \(\tfrac12<t<1\), one has \(a_1=1\) and \(a_2=0\), establishing the identification. The theorem concerns only this specified real-axis branch and the \((\tfrac12,1)\) contribution, not every analytic branch of the prime-zeta continuation or the full semiprime smooth function.

## Proof

**1. The zeta factor strictly increases in logarithmic absolute value.** For real \(0<t<1\), the classical fractional-part integral, continued from \(\Re t>1\), is
\[
 \zeta(t)=\frac{t}{t-1}-t\int_1^\infty\frac{\{v\}}{v^{t+1}}\,dv.
\]
The integral converges absolutely for \(t>0\), and both terms on the right are negative when \(0<t<1\). Hence \(\zeta(t)<0\). Differentiating under the integral gives
\[
 \zeta'(t)=-\frac1{(1-t)^2}
 -\int_1^\infty\frac{\{v\}}{v^{t+1}}\,dv
 +t\int_1^\infty\frac{\{v\}\log v}{v^{t+1}}\,dv
 \leq-\frac1{(1-t)^2}+\frac1t<0
 \quad(\tfrac12<t<1).
\]
The last inequality uses \(\{v\}\leq1\), the exact integral \(\int_1^\infty (\log v)v^{-t-1}dv=t^{-2}\), and \((1-t)^{-2}\geq4>2\geq t^{-1}\). Thus \(\zeta'(t)/\zeta(t)>0\).

**2. The rest of the Möbius series also has positive derivative.** Write \(F(z)=\sum_{n\geq2}\mu(n)z^n\). Since \(\mu(2)=\mu(3)=\mu(5)=-1\), \(\mu(4)=0\), and \(\mu(n)\leq1\),
\[
 F(z)\leq-z^2-z^3-z^5+\frac{z^6}{1-z}<-z^3-z^5<0
 \qquad (0<z\leq 2^{-1/2}).
\]
Indeed \(z^4/(1-z)\leq(1/4)/(1-1/\sqrt2)<1\) in this range. For any compact subinterval of \((\tfrac12,1)\), the \(n\geq2\) part of \(U\) and all its derivatives converge locally uniformly. The Euler product logarithmic derivative \(-\zeta'(s)/\zeta(s)=\sum_{m\geq2}\Lambda(m)m^{-s}\) is absolutely convergent for \(s>1\). Therefore termwise differentiation and interchange of absolutely convergent sums yield
\[
 U'(t)=\frac{\zeta'(t)}{\zeta(t)}
 +\sum_{n\geq2}\mu(n)\frac{\zeta'(nt)}{\zeta(nt)}
 =\frac{\zeta'(t)}{\zeta(t)}
 -\sum_{m\geq2}\Lambda(m)F(m^{-t})>0.
\]
Here \(\Lambda(m)\geq0\) and \(m^{-t}<2^{-1/2}\), so every nonzero Dirichlet-series contribution is nonnegative; the first summand is strictly positive.

**3. The two endpoint divergences.** Near \(t=\tfrac12\), the term with \(n=2\) is \(-\tfrac12\log\zeta(2t)=\tfrac12\log(2t-1)+O(1)\); all other terms admit finite limits there, including \(\log|\zeta(t)|\). Thus \(U(t)=\tfrac12\log(2t-1)+O(1)\to-\infty\). Near \(t=1\), the term with \(n=1\) is \(\log|\zeta(t)|=-\log(1-t)+O(1)\), and every \(n\geq2\) term remains bounded. This gives \(U(t)\to+\infty\). Strict monotonicity and continuity prove the unique density zero and its sign classification.

**4. The integral has precisely one zero.** The preceding endpoint bounds show \(U\in L^1((\tfrac12,1))\), hence \(B(x)\) converges for all \(x>0\). Let \(\tau\) be the density zero and define
\[
 G(y)=e^{-\tau y}B(e^y)
 =\int_{1/2}^{1}\frac{U(t)}t e^{(t-\tau)y}\,dt.
\]
Differentiation is justified by the integrable logarithmic endpoint singularities. Since \((t-\tau)U(t)>0\) everywhere except at \(t=\tau\),
\[
 G'(y)=\int_{1/2}^{1}\frac{(t-\tau)U(t)}t
 e^{(t-\tau)y}\,dt>0
 \qquad(y\in\mathbb R).
\]
As \(y\to+\infty\), the integral over any closed subinterval of \((\tau,1)\) grows exponentially and is positive, while the entire negative contribution on \((\tfrac12,\tau)\) stays bounded. Thus \(G(y)\to+\infty\). As \(y\to-\infty\), the negative contribution from any closed subinterval of \((\tfrac12,\tau)\) tends to \(-\infty\), while the positive contribution stays bounded. Therefore \(G(y)\to-\infty\). Strict monotonicity now gives a unique zero of \(G\), and multiplication by \(e^{\tau y}>0\) gives the asserted signs and the unique zero of \(B\).

## Verification

The proof requires no numerical certificates. Critical facts are the exact fractional-part integral for \(\zeta(t)\), the explicit bound \(F(z)<0\) for \(z\leq1/\sqrt2\), absolute convergence of the log-derivative series at \(nt>1\), the two logarithmic endpoint expansions, and the strictly positive derivative of the normalized Laplace integral. The accompanying program `verify.py` reproduces illustrative high-precision sign checks; they are **not** used to prove any universal assertion.

## Relationship to prior work

Belton [1] defines the semiprime real-cut density and its upper-cut contribution, provides convergence and asymptotic properties, and explicitly does not assert general positivity of the resulting signed densities. The present result gives a complete sign classification for that natural restricted density and its upper-cut integral. Mathar [2] develops the classical almost-prime generating functions and describes prime-zeta singularities, but its derivative tables concern the absolutely convergent region and do not establish this real-cut sign classification. Prior prime-zeta zero studies such as Belovas--Čepaitytė--Sabaliauskas [3] investigate the full complex zero geometry, including a zero-free half-plane to the right of one; such a statement does not imply either asserted real-cut transition. The analytic continuation and its branch subtleties are discussed by Camargo [4], which is why the branch convention is fixed in the statement.

## Limitations

The result is **not** a sign theorem for the full \(\mathcal R_2(x)\) or an error bound for semiprime counting. It does not classify zeros of the prime-zeta function on other complex branches or outside the specified real interval. Numerical locations of \(\tau\) or \(\xi\) are not part of the proved claim. Older literature may contain an equivalent implicit monotonicity statement.

## References

[1] M. Belton, *A note on Riemann's R-function and almost primes*, arXiv:2610.11024v1, publicly submitted 8 October 2026, https://arxiv.org/html/2610.11024v1, especially §§2, 5.

[2] R. J. Mathar, *Series of Reciprocal Powers of k-almost Primes*, arXiv:0803.0900v3, https://arxiv.org/html/0803.0900v3, especially §2 and derivative/singularity discussion.

[3] I. Belovas, R. Čepaitytė and M. Sabaliauskas, *On the zero-free region and the distribution of zeros of the prime zeta function*, Analele ştiinţifice ale Universităţii Ovidius Constanţa 33 (2025), 27–44, doi:10.2478/auom-2025-0017.

[4] A. P. de Camargo, *On the analytic continuation, computation and zeros of the prime zeta function*, preprint dated 18 November 2025, abstract and available introductory text: https://www.researchgate.net/publication/397738720_On_the_analytic_continuation_computation_and_zeros_of_the_prime_zeta_function.

[5] C.-E. Fröberg, *On the prime zeta function*, BIT 8 (1968), 187–202, doi:10.1007/BF01933420. Full text not accessed; cited for historical context only.
