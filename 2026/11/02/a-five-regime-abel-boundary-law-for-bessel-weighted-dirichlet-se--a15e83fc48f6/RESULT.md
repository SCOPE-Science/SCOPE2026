# A five-regime Abel boundary law for Bessel-weighted Dirichlet series

## Finding
For every integer \(d\geq1\) and every \(a_1,\dots,a_d>0\), set \(A=\sum_{j=1}^d a_j\) and
\[
F_d(\delta)=\sum_{n=1}^{\infty}\frac{\prod_{j=1}^d I_0(2a_j\log n)}{n^{1+2A+\delta}},\qquad\delta>0,
\]
where \(I_0(x)=\sum_{m\ge0}(x/2)^{2m}/(m!)^2\) and \(K_d=(4\pi)^{-d/2}\prod_{j=1}^d a_j^{-1/2}\). Then the **exact leading five regimes** as \(\delta\downarrow0\) are
\[
\begin{array}{ll}
 d=1:&F_1(\delta)\sim\sqrt\pi K_1\,\delta^{-1/2},\\
 d=2:&F_2(\delta)\sim K_2\log(1/\delta),\\
 d=3:&F_3(0)-F_3(\delta)\sim2\sqrt\pi K_3\,\delta^{1/2},\\
 d=4:&F_4(0)-F_4(\delta)\sim K_4\delta\log(1/\delta),\\
 d\ge5:&F_d(0)-F_d(\delta)\sim\delta J_d,
\end{array}
\]
with \(J_d=\sum_{n\ge2}n^{-1-2A}\prod_j I_0(2a_j\log n)\log n\in(0,\infty)\). The boundary value \(F_d(0)\) exists precisely for \(d\ge3\); the finite one-sided derivative exists precisely for \(d\ge5\). Here every parameter vector is fixed; estimates are not uniform as any \(a_j\to0\).

For distinct primes \(p_1,\ldots,p_d\), this Dirichlet-series boundary law is the exact boundary sensitivity of a natural Hardy--Dirichlet Hilbert--Schmidt norm: for \(\varphi_\varepsilon(s)=\frac12+A+\varepsilon-\sum_j a_jp_j^{-s}\),
\[
\|C_{\varphi_\varepsilon}\|_{\mathcal S_2}^2=F_d(2\varepsilon),\qquad\varepsilon>0.
\]
This is an application, not the novelty claim that Hilbert--Schmidt membership at \(\varepsilon=0\) occurs for \(d\ge3\), which was already known.

## Assumptions and scope
The primary object is the scalar analytic Dirichlet series \(F_d\), with complex parameter \(\delta\) in \(\operatorname{Re}\delta>0\). The Bessel function \(I_0\) is the standard modified Bessel function. All asymptotics are along positive real \(\delta\downarrow0\). The finite derivative statement concerns approach from the right. The auxiliary Hardy space \(\mathcal H^2\) consists of \(f(s)=\sum_{n\ge1}c_nn^{-s}\) with \(\sum_n|c_n|^2<\infty\). Composition acts as \(C_\varphi f=f\circ\varphi\). Distinct primes ensure rational independence of logarithms. No assertion is made about arbitrary nonlinear composition symbols.

## Proof
**1. Exact coefficient asymptotics.** The integral representation \(I_0(t)=(2\pi)^{-1}\int_{-\pi}^{\pi}e^{t\cos\theta}\,d\theta\) and elementary Gaussian Laplace asymptotics at the unique maximum \(\theta=0\) give, for each fixed \(a>0\),
\[
e^{-2au}I_0(2au)=(4\pi au)^{-1/2}(1+O_a(u^{-1}))\qquad(u\to\infty).
\]
Multiplying finitely many factors produces
\[
h(u):=e^{-2Au}\prod_jI_0(2a_ju)=K_du^{-d/2}(1+O_{d,\boldsymbol a}(u^{-1})).
\]
Consequently the exact Dirichlet-series coefficient equals \(v(n)=n^{-1}h(\log n)\) and has the critical logarithmic exponent \(d/2\). For large \(u\), the derivative of \(h\) is \(O(u^{-d/2-1})\), by differentiating the same Laplace integral, so the corresponding real interpolation \(x\mapsto x^{-1}h(\log x)\) has an integrable derivative and logarithm-weighted derivative on \([2,\infty)\).

**2. Reduction from sums to Laplace integrals.** Write \(g_\delta(x)=x^{-1-\delta}h(\log x)\). For \(0\le\delta\le1\), the sum--integral comparison on each interval \([n,n+1]\) gives
\[
\left|\sum_{n\ge2}g_\delta(n)-\int_2^\infty g_\delta(x)\,dx\right|
\le\int_2^\infty|g_\delta'(x)|\,dx=O(1).
\]
Moreover the difference between its values at \(\delta>0\) and \(\delta=0\) is \(O(\delta)\): use the mean value theorem in \(\delta\), differentiate under the comparison, and bound \(\int_2^\infty|\partial_x(\log x\,x^{-1-\delta}h(\log x))|\,dx\) uniformly. The \(n=1\) term is exactly one and does not change with \(\delta\). Under \(u=\log x\), the integral is \(\int_{\log2}^\infty e^{-\delta u}h(u)\,du\). The comparison remainder is bounded in the divergent cases and varies only by \(O(\delta)\) in the finite-difference cases.

**3. Divergent boundary regimes.** When \(d=1\), \(h(u)=K_1u^{-1/2}+O(u^{-3/2})\); thus \(F_1(\delta)=K_1\Gamma(1/2)\delta^{-1/2}+O(1)\). For \(d=2\), \(h(u)=K_2u^{-1}+O(u^{-2})\), hence \(F_2(\delta)=K_2\log(1/\delta)+O(1)\). These are the first two formulas.

**4. Fractional cusp and logarithmic cusp.** When \(d=3\), subtract the finite boundary value before integrating. The leading integral becomes
\[
K_3\int_0^\infty(1-e^{-\delta u})u^{-3/2}\,du
=2\sqrt\pi K_3\delta^{1/2}.
\]
The omission of a fixed finite lower interval and the \(O(u^{-5/2})\) coefficient error each contribute \(O(\delta)\); the sum--integral correction also contributes \(O(\delta)\). When \(d=4\), the same argument gives \(K_4\int_1^\infty(1-e^{-\delta u})u^{-2}\,du=K_4\delta\log(1/\delta)+O(\delta)\). Its \(O(u^{-3})\) error contributes \(O(\delta)\).

**5. Finite derivative regime.** When \(d\ge5\), \(\sum_{n\ge2}v(n)\log n<\infty\), because its tail is bounded by a constant multiple of \(\sum_n[n(\log n)^{d/2-1}]^{-1}\), with exponent \(d/2-1>1\). Termwise dominated convergence in \((1-n^{-\delta})/\delta\to\log n\) yields the last formula and strict positivity of \(J_d\). At \(d=3,4\), the preceding cusps show the difference quotient diverges, so the threshold is exact.

**6. Operator interpretation and normalization.** For fixed \(n\ge1\),
\[
n^{-\varphi_\varepsilon(s)}=n^{-1/2-A-\varepsilon}\prod_{j=1}^d\exp(a_j(\log n)p_j^{-s}).
\]
Expansion as a Dirichlet series in the multiplicatively independent primes and Parseval give
\[
\|n^{-\varphi_\varepsilon}\|_{\mathcal H^2}^2=n^{-1-2A-2\varepsilon}\prod_j\sum_{m\ge0}\frac{(a_j\log n)^{2m}}{(m!)^2}
=n^{-1-2A-2\varepsilon}\prod_jI_0(2a_j\log n).
\]
Summing over the canonical orthonormal basis \(\{n^{-s}\}_{n\ge1}\) proves the stated Hilbert--Schmidt identity. The \(\varphi_\varepsilon\) map belongs to the characteristic-zero Gordon--Hedenmalm class since its real part on \(\operatorname{Re}s>0\) is strictly larger than \(1/2\); thus the composition operator is well-defined. The identity remains a formal extended-value Parseval sum when \(\varepsilon=0\), recovering the previously established qualitative classification but not claiming it as novel.

## Verification
The accompanying `checker.py` tests the exact Bessel coefficient identity by finite Taylor expansions, the Gaussian saddle constant for several dimension and coefficient vectors, and the analytic Abel integral constants independently with high-precision incomplete Gamma integrals. These are finite corroboration only; the displayed integral and dominated-convergence arguments prove the infinitely many-dimensional-index statements. Run `python checker.py` with Python 3, SciPy, and mpmath. All file dependencies are contained in this package except these standard libraries.

## Relationship to prior work
Brevig, Kouroupis and Perfekt (arXiv:2405.03522, first public 2024-05-06) study almost-periodic and boundary values of analytic Dirichlet series, the motivating analytic context and primary classification 30B50; their Hardy--Stein and Littlewood--Paley results do not state Bessel coefficient critical Abel expansions. Bayart and Kouroupis (arXiv:2306.05733, first public 2023-06-09) give general Schatten criteria for Dirichlet composition operators, but not these five explicit leading boundary moduli. Bayart (2003) already treats the qualitative Hilbert--Schmidt threshold for this independent-frequency linear symbol family; the threshold alone is **not new**. Bayart and Brevig (arXiv:1505.02944) establish geometric compactness and approximation-number bounds for polynomial symbols; those estimates do not specify the present critical constants. The novelty assessed here is the exact five-regime Abel law with the explicit constants and finite-differentiability transition for the **specific Bessel-weighted Dirichlet series**, not the general operator membership theorem or any known Abelian principle.

## Limitations
A first-order Abelian theorem applied to the explicit Bessel coefficient asymptotics is sufficient; this is a sharp specialized calculation, not a new general Tauberian theorem. The formula is pointwise in the fixed positive amplitude vector, not uniform as amplitudes vanish. Only first-order boundary behavior is claimed. No statement of historical absolute novelty or independent verification is made. Closely related specialized constants outside the inspected sources remain a priority risk.

## References
1. O. F. Brevig, A. Kouroupis, K.-M. Perfekt, *Almost periodicity and boundary values of Dirichlet series*, arXiv:2405.03522v1 (2024-05-06), https://arxiv.org/html/2405.03522v1.
2. F. Bayart, A. Kouroupis, *Schatten class composition operators on the Hardy space of Dirichlet series and a comparison-type principle*, arXiv:2306.05733v1 (2023-06-09), https://arxiv.org/abs/2306.05733.
3. F. Bayart, *Compact composition operators on a Hilbert space of Dirichlet series*, Illinois J. Math. 47 (2003), 725--743.
4. F. Bayart, O. F. Brevig, *Compact composition operators with non-linear symbols on the \(H^2\) space of Dirichlet series*, arXiv:1505.02944v1 (2015-05-12), https://arxiv.org/html/1505.02944v1.
