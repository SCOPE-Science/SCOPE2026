# Distinct integer beta maps eliminate zero variance and give an exact noise-onset coefficient

## Finding

Let \(a,b\geq 2\) be **distinct integers**. At each step independently apply \(T_a(x)=ax\pmod 1\) with probability \(1-\varepsilon\) or \(T_b(x)=bx\pmod 1\) with probability \(\varepsilon\), starting from Lebesgue-uniform \(X_0\) on \(\mathbb T=\mathbb R/\mathbb Z\). For every \(0<\varepsilon<1\) and every real mean-zero nonzero \(\varphi\in BV(\mathbb T)\), the annealed asymptotic variance

\[
\sigma_\varepsilon^2(\varphi)=\lim_{N\to\infty}\frac1N\operatorname{Var}\!\left(\sum_{j=0}^{N-1}\varphi(X_j)\right)
\]

exists and is **strictly positive**; the normalized sum converges in law, under the joint distribution of the initial point and independent map choices, to \(\mathcal N(0,\sigma_\varepsilon^2(\varphi))\).

The exact first-order emergence of variance can also be determined. Fix any real mean-zero \(\psi\in BV(\mathbb T)\) and the deterministic \(T_a\)-coboundary \(\varphi=\psi-\psi\circ T_a\). Then

\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}\frac{\sigma_\varepsilon^2(\varphi)}{\varepsilon}
=\int_0^1\!\bigl(\psi(ax)-\psi(bx)\bigr)^2\,dx.}
\]

For every nonconstant \(\psi\), this exact coefficient is strictly positive. Thus a coboundary with zero deterministic asymptotic variance acquires a strictly positive variance at precisely first order in the probability of switching to a distinct integer slope. Both assertions are parts of the same nondegeneracy-and-onset theorem.

For example, with \(a=2\), \(b=3\), and \(\varphi(x)=\cos(2\pi x)-\cos(4\pi x)\), the **exact identity** \(\sigma_\varepsilon^2(\varphi)=\varepsilon\) holds for all \(0\le\varepsilon\le1\). The role of arithmetic resonance in other slope pairs is specified in the proof.

## Assumptions and scope

The circle is equipped with normalized Lebesgue measure \(m\). All functions are considered up to almost-everywhere equality. A real \(BV\) observable has finite total variation on the circle and is bounded; no differentiability is required. The two integer slopes are distinct and at least two; they may have common prime factors, and one may divide the other. All probabilities and variances average over *both* the initial uniform point and the independent choices of maps (annealed law). The initial point is independent of those choices. The central limit theorem is not claimed to be a quenched variance assertion.

Put \(U_m f=f\circ T_m\) and

\[
(P_m f)(y)=\frac1m\sum_{j=0}^{m-1}f\left(\frac{y+j}{m}\right),\qquad
P_\varepsilon=(1-\varepsilon)P_a+\varepsilon P_b.
\]

Each map preserves \(m\), \(P_m\) is the \(L^2(m)\)-adjoint of \(U_m\), and the reversed stationary chain has transition \(P_\varepsilon\). The claim includes \(\varepsilon=0\) only for the stated one-sided limiting comparison, not for strict positivity at that endpoint.

## Proof

**1. Transfer gap, Poisson solution, and variance.** For \(f\in BV(\mathbb T)\), subinterval variation gives

\[
\operatorname{Var}_{\mathrm{tot}}(P_mf)\leq m^{-1}\operatorname{Var}_{\mathrm{tot}}(f),\qquad
\int P_mf\,dm=\int f\,dm.
\]

Consequently, for \(\int f\,dm=0\), the total variation of \(P_\varepsilon^nf\) is at most \(\theta_\varepsilon^n\operatorname{Var}_{\mathrm{tot}}(f)\), where \(\theta_\varepsilon=(1-\varepsilon)/a+\varepsilon/b<1\). Since a mean-zero \(BV\) function has supremum norm at most its variation, the series

\[
h_\varepsilon=\sum_{n=0}^\infty P_\varepsilon^n\varphi
\]

converges uniformly and in \(BV\) variation. It solves \((I-P_\varepsilon)h_\varepsilon=\varphi\). Adjunction and geometric covariance decay give the convergent Green--Kubo identity

\[
\sigma_\varepsilon^2(\varphi)=\int\varphi^2\,dm+2\sum_{n\geq1}\int\varphi\,( (1-\varepsilon)U_a+\varepsilon U_b)^n\varphi\,dm
=\|h_\varepsilon\|_2^2-\|P_\varepsilon h_\varepsilon\|_2^2.
\]

The equality follows directly by substituting \(\varphi=h_\varepsilon-P_\varepsilon h_\varepsilon\) into twice the inner product \(\langle\varphi,h_\varepsilon\rangle\) minus \(\|\varphi\|_2^2\); stationarity proves that this Green--Kubo sum is the limit of normalized finite-time variances.

**2. Central limit theorem.** Under the time-reversed stationary Markov law with transition \(P_\varepsilon\), write \(Y_j\) for the states and

\[
D_{j+1}=h_\varepsilon(Y_{j+1})-(P_\varepsilon h_\varepsilon)(Y_j).
\]

These are bounded martingale differences. For all \(N\geq1\),

\[
\sum_{j=0}^{N-1}\varphi(Y_j)=\sum_{j=0}^{N-1}D_{j+1}+h_\varepsilon(Y_0)-h_\varepsilon(Y_N).
\]

Their stationary mean conditional variance is \(\|h_\varepsilon\|_2^2-\|P_\varepsilon h_\varepsilon\|_2^2\). The reverse chain is mixing: on centered \(BV\) functions, \(P_\varepsilon^n\) converges to zero uniformly, and density extends the convergence to \(L^2\); the Markov property then yields ergodicity of the stationary path shift. Birkhoff's theorem makes the normalized conditional quadratic variation tend almost surely to this constant. Bounded increments give the Lindeberg condition, so the standard martingale central limit theorem applies. The final bounded coboundary term disappears after division by \(\sqrt N\). Reversing the order of a stationary finite block leaves its sum unchanged, giving the claimed annealed CLT for the forward chain.

**3. Zero variance forces a common functional identity.** For \(h=h_\varepsilon\) one has the pointwise conditional-variance identity

\[
\sigma_\varepsilon^2(\varphi)=\int_0^1\!\left[
(1-\varepsilon)P_a(h^2)(y)+\varepsilon P_b(h^2)(y)-(P_\varepsilon h(y))^2\right]dy.
\]

The bracket is the variance of a finite discrete distribution with **strictly positive weights** \((1-\varepsilon)/a\) and \(\varepsilon/b\) at every inverse branch of \(T_a\) and \(T_b\). If its integral is zero, it vanishes almost everywhere. Every inverse-branch value must then be the same value \(H(y)=P_\varepsilon h(y)\). In particular \(h(x)=H(ax)=H(bx)\) for almost every \(x\).

**4. Arithmetic Fourier rigidity.** Suppose \(H\in L^2(\mathbb T)\) satisfies \(H(ax)=H(bx)\) almost everywhere. Write \(d=\gcd(a,b)\), \(r=a/d\), \(s=b/d\); composition by \(x\mapsto dx\) is injective on \(L^2\), so \(H(rx)=H(sx)\). Interchanging the maps if needed, take \(s\geq2\), with \(\gcd(r,s)=1\). Let \(c_k\) be the \(k\)-th Fourier coefficient of \(H\). Comparing frequency \(rk\) on the two sides gives

\[
 c_k=\begin{cases}c_{rk/s},&s\mid k,\\0,&s\nmid k.\end{cases}
\]

For each nonzero integer \(k\), repeated replacement by \(rk/s\) cannot remain divisible by \(s\) forever, because \(r\) is coprime to \(s\). Hence \(c_k=0\) for all \(k\ne0\); completeness of the Fourier basis forces \(H\) to be constant almost everywhere. The conclusion of Step 3 thus makes \(h\) constant and \(\varphi=h-P_\varepsilon h=0\), contrary to hypothesis. This proves strict positivity, including when the two slopes are multiplicatively dependent.

**5. Sharp small-noise opening.** Set \(P_0=P_a\), \(P'_0=P_b-P_a\). On mean-zero \(BV\), the inverse \((I-P_\varepsilon)^{-1}\) is differentiable at \(\varepsilon=0\) by the uniformly convergent Neumann series. For \(\varphi=\psi-U_a\psi\) with mean-zero \(\psi\), telescoping the series at zero yields \(h_0=-U_a\psi\) and \(P_ah_0=-\psi\). Differentiate the exact variance identity:

\[
\begin{split}
\left.\frac{d}{d\varepsilon}\sigma_\varepsilon^2(\varphi)\right|_{0+}
&=2\langle h_0,h'_0\rangle-2\langle P_ah_0,(P_b-P_a)h_0+P_ah'_0\rangle\\
&=-2\langle-\psi,(P_b-P_a)(-U_a\psi)\rangle\\
&=2\bigl(\|\psi\|_2^2-\langle U_b\psi,U_a\psi\rangle\bigr)\\
&=\|U_a\psi-U_b\psi\|_2^2.
\end{split}
\]

The terms containing \(h'_0\) cancel because \(U_aP_ah_0=h_0\). Step 4 makes this coefficient positive for nonconstant \(\psi\). At zero noise, the telescoping identity \(\sum_{j<N}(\psi-\psi\circ T_a)(T_a^jx)=\psi(x)-\psi(T_a^Nx)\) proves \(\sigma_0^2(\varphi)=0\). Differentiability and the exact coefficient prove the displayed limit.

**6. Exact Fourier illustration and a resonant boundary.** Let \(\psi(x)=\cos(2\pi x)\) and \(\varphi=\psi-\psi\circ T_a\). Orthogonality gives \(\|\varphi\|_2^2=1\). Since every selected multiplier is at least two, any lagged correlation can arise only if the product of the first \(n\) selected multipliers equals \(a\). For \(n=1\) that event has probability \(1-\varepsilon\). For \(n\geq2\) it can occur only if **all** multipliers equal \(b\) and \(a=b^n\), with probability \(\varepsilon^n\). Thus

\[
\boxed{\displaystyle
\sigma_\varepsilon^2(\varphi)=
\begin{cases}
\varepsilon-\varepsilon^k,&a=b^k\text{ for an integer }k\geq2,\\
\varepsilon,&\text{otherwise.}
\end{cases}}
\]

For example \(a=2,b=3\) gives exactly \(\sigma_\varepsilon^2=\varepsilon\), whereas \(a=4,b=2\) gives \(\varepsilon(1-\varepsilon)\). Both have the same unit right derivative at zero noise, consistent with Step 5, and the resonant pair is also a deterministic coboundary at the opposite endpoint. This example is an explicit illustration of, not a substitute for, the general theorem.

## Verification

The standalone checker `checks/variance_fourier.py` implements the transfer operators exactly on finite cosine-polynomial Fourier coefficients using Python rational arithmetic. It verifies the exact \(\sigma_\varepsilon^2=\varepsilon\) identity for several pairs of distinct integer slopes, including divisibility cases, and checks the small-noise derivative for additional finite Fourier observables with nonzero frequency overlaps. Run with `python3 checks/variance_fourier.py`; successful output ends with `CHECK_OK`. The general \(BV\) assertion and the limit are proved analytically in Steps 1--5, not by these finite tests.

## Relationship to prior work

Suzuki [1] develops invariant densities and their dependence on Bernoulli probabilities for random beta-transformations, including integer slopes. The uniform stationary measure for integer slopes is elementary here, and neither stationary density formulas nor their linear response are claimed as new.

Aimino, Nicol, and Vaienti [2] prove general random-expanding-system limit theorems, state a zero-variance common-coboundary criterion (Proposition 3.4), and explicitly discuss randomly chosen integer multiplication maps (Example 7.3). Their CLT, covariance theory, and abstract criterion are used as established context, **not** claimed as new. The additional content here is the all-pair arithmetic rigidity that excludes every nonconstant zero-variance observable for distinct slopes and, more substantially, the evaluated **first-order variance coefficient** when randomness perturbs a deterministic coboundary.

Dragičević and Hafouta [3] establish differentiability of certain quenched CLT variances in a much more general parameterized setting. Their differentiability theorem is acknowledged; it does not display the specific two-slope Bernoulli endpoint coefficient \(\|\psi\circ T_a-\psi\circ T_b\|_2^2\), or the no-degeneracy classification stated here. An equivalent specialization could nevertheless exist elsewhere; the present work does not claim exhaustive publication priority.

## Limitations

The theorem concerns annealed, stationary data for two **distinct positive integer slopes** and real \(BV\) observables. It does not cover noninteger beta-transformations, correlated slope choices, arbitrary \(L^2\) observables without a solvable Poisson equation, or provide a uniform lower bound for the variance relative to an observable norm. The derivative is a one-sided perturbation of a fixed \(T_a\)-coboundary; it does not claim differentiability for all noise models. The analytical proof establishes all quantified assertions under these hypotheses; finite Fourier checks do not prove them for arbitrary observables. Publication priority remains subject to unindexed or differently phrased literature.

## References

1. Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, first posted 30 March 2023, https://arxiv.org/abs/2303.17521 (consulted v3 full PDF, 25 April 2024).
2. Romain Aimino, Matthew Nicol, and Sandro Vaienti, *Annealed and quenched limit theorems for random expanding dynamical systems*, arXiv:1310.4359, https://arxiv.org/abs/1310.4359; publicly accessible manuscript https://www.cpt.univ-mrs.fr/~vaienti/AANNVV.pdf; Proposition 3.4, Theorem 3.5, Example 7.3.
3. Davor Dragičević and Yeor Hafouta, *Effective quenched linear response for random dynamical systems*, arXiv:2403.04907, first posted 7 March 2024, https://arxiv.org/abs/2403.04907; consulted v3 full PDF, Section 4 (variance differentiability).
