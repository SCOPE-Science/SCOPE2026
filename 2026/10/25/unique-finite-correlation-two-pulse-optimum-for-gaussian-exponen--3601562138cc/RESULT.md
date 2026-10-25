# Unique finite-correlation two-pulse optimum for Gaussian exponential dephasing

## Finding

For stationary Gaussian pure-dephasing frequency noise with covariance \(\mathbb E[\xi(t)\xi(s)]=\sigma^2e^{-|t-s|/\tau}\), consider precisely two ideal instantaneous sign-inverting control pulses at \(0<t_1<t_2<T\). For every positive dimensionless observation duration \(L=T/\tau\), there is exactly one global pulse-timing pair maximizing ensemble-averaged qubit coherence. It is reflection-symmetric, and its dimensionless middle-interval length \(b_*\) is the unique positive solution of

\[
L=2b_*+2\log\cosh(b_*/2),\qquad
\frac{t_1^*}{\tau}=\frac{L-b_*}{2},\qquad
t_2^*=T-t_1^*.
\]

The timing rule obeys the sharp bounds

\[
\frac14<\frac{t_1^*}{T}<\frac13,
\qquad \frac23<\frac{t_2^*}{T}<\frac34.
\]

The first optimal pulse fraction increases strictly with \(T/\tau\). The conventional symmetric two-pulse Carr–Purcell timing \((t_1,t_2)=(T/4,3T/4)\) is strictly suboptimal for every finite \(T/\tau>0\) in this covariance model, even though the two schedules agree asymptotically as \(T/\tau\downarrow0\).

## Assumptions and scope

The noise \(\xi\) is a real stationary, centered *Gaussian* process of strictly positive covariance amplitude \(\sigma^2\) and finite positive correlation time \(\tau\). The two pulses are instantaneous ideal \(\pi\) rotations about a transverse axis and invert the sign of the pure-dephasing Hamiltonian \(H(t)=\xi(t)\sigma_z/2\), without pulse errors or other relaxation. Total duration \(T>0\) and number of pulses (exactly two) are fixed. Pulse times may be selected freely with strict ordering and no imposed zero-area condition.

Writing \(u=t/\tau\), let \(y(u)=+1\) for \(0<u<a\), \(y(u)=-1\) for \(a<u<a+b\), and \(y(u)=+1\) for \(a+b<u<L\), where \(a,b,c>0\) and \(a+b+c=L\), \(c=L-a-b\). The coherence attenuation is exactly

\[
W=\left|\mathbb E\exp\left(-i\int_0^T y(t/\tau)\xi(t)\,dt\right)\right|
=\exp[-\sigma^2\tau^2\mathcal Q(a,b,c)/2],
\quad
\mathcal Q=\int_0^L\!\int_0^L y(u)y(v)e^{-|u-v|}\,du\,dv.
\]

Thus maximizing coherence is equivalent to minimizing the nonnegative quadratic functional \(\mathcal Q\). The strict Gaussian hypothesis matters: random telegraph noise has an exponential two-point function but generally does not have this Gaussian coherence law.

## Proof

**1. Exact three-interval functional.** Splitting the double integral into its nine rectangular blocks gives

\[
\begin{aligned}
\mathcal Q(a,b,c)={}&2L-10+4(e^{-a}+e^{-c})+8e^{-b}\\
&-4(e^{-(a+b)}+e^{-(b+c)})+2e^{-L}.
\end{aligned}
\]

For independent verification without symbolic differentiation, define recursively \(z_0=0\) and, for the three lengths \(\ell_1=a,\ell_2=b,\ell_3=c\) and signs \(s_1=1,s_2=-1,s_3=1\), set

\[
z_j=s_j+(z_{j-1}-s_j)e^{-\ell_j},\quad
\mathcal Q=2\sum_{j=1}^3[\ell_j+s_j(z_{j-1}-s_j)(1-e^{-\ell_j})].
\]

Both expressions follow by elementary integration of the kernel and agree identically.

**2. Symmetry is forced globally.** Holding \(b\) fixed, write \(c=L-b-a\). Direct differentiation of the exact expression yields

\[
\left.\frac{\partial\mathcal Q}{\partial a}\right|_{b,L}
=4(1-e^{-b})(e^{-c}-e^{-a}).
\]

Since \(b>0\), the derivative is strictly negative when \(a<c\) and strictly positive when \(a>c\). The unique minimum at each fixed middle duration is therefore \(a=c=(L-b)/2\). In particular, no asymmetric two-pulse schedule can improve on the symmetric schedule with the same \(b\).

**3. Unique optimal middle duration.** Along \(a=c=(L-b)/2\), differentiation gives

\[
\frac{d\mathcal Q}{db}
=4e^{-a}(1+e^{-b})-8e^{-b}.
\]

The sign of this derivative is the sign of

\[
F(b)-L,\qquad F(b)=2b+2\log\cosh(b/2),
\]

because the derivative is positive precisely when \(e^a<(1+e^b)/2\), equivalently \(F(b)>L\). The function \(F\) is continuous, strictly increasing from \(F(0)=0\) to infinity; \(F(L)>L\) and \(F(0)<L\). There is exactly one \(b_*\in(0,L)\) with \(F(b_*)=L\), at which the symmetric functional decreases then increases. Boundary schedules with coincident pulses or pulses at endpoints have strictly larger \(\mathcal Q\) by continuity and the strict interior minimum. This establishes uniqueness of the unrestricted global minimizer.

**4. Sharp timing geometry.** For \(b>0\), \(0<\log\cosh(b/2)<b/2\). Hence \(2b_*<L<3b_*\), proving \(L/3<b_*<L/2\) and \(L/4<a_*<L/3\). The ratio

\[
\frac{a_*}{b_*}=\frac12+\frac{\log\cosh(b_*/2)}{b_*}
\]

increases strictly with \(b_*\): strict convexity and zero intercept of \(\log\cosh(b/2)\) make its secant slope strictly increasing. Because \(b_*\) increases with \(L\), the pulse fraction \(a_*/L\) also increases strictly from \(1/4\) toward \(1/3\).

**5. Endpoint asymptotics and the CPMG gap.** Taylor expansion of \(F(b_*)=L\) and the exact functional gives, as \(L\downarrow0\),

\[
 b_*=\frac L2-\frac{L^2}{32}+O(L^3),\qquad
 \frac{t_1^*}{T}=\frac14+\frac L{64}+O(L^2),
\]

and

\[
\mathcal Q_{\mathrm{CPMG}}-\mathcal Q_{\min}
=\frac{L^4}{256}+O(L^5)>0
\]

for sufficiently small positive \(L\); strict positivity for *all* positive \(L\) already follows from uniqueness. As \(L\to\infty\), since \(2\log\cosh(b/2)=b-2\log2+2\log(1+e^{-b})\),

\[
 b_*=\frac{L+2\log2}{3}+O(e^{-L/3}),\quad
 \frac{t_1^*}{T}=\frac13-\frac{\log2}{3L}+O(e^{-L/3}/L).
\]

The optimized modulation has nonzero signed area \(\int_0^T y(t/\tau)dt=T-2\tau b_*>0\); imposing exact static-noise cancellation therefore excludes the true finite-correlation optimizer.

## Verification

The accompanying standalone `checker.py` requires only the Python 3 standard library. It evaluates the quadratic kernel in two independent ways: an interval-state recursion and a blockwise exponential integral. It reproduces the unique root by bisection, compares against the symmetric equal-area schedule, and samples unrestricted competing two-pulse schedules. Its deterministic test execution passed 3,509 comparisons. Sample: when \(L=2\), the unique optimal normalized segment lengths are \((0.5491770806,0.9016458387,0.5491770806)\), rather than \((0.5,1,0.5)\). Numerical tests support, but do not replace, the global analytical argument.

## Relationship to prior work

Cywiński et al. (first posted 2007-12-13) established the Gaussian filter-function treatment of pure dephasing, and discuss standard Carr–Purcell and Uhrig pulse sequences and exponentially correlated random-telegraph noise. Pan, Xi and Cui (first posted 2010-01-18) optimized pulse times for an *Ohmic cutoff* spectrum; their general optimization principle is shared, but their spectral objective and resulting optimizers differ from the stationary exponential kernel. Ajoy, Alvarez and Suter (first posted 2010-11-29) compare pulse-spacing schemes for *Gaussian-frequency* spin-bath spectra. Ji and Zhao (first posted 2025-12-31) formulate a stationary Gaussian exponential-covariance dephasing objective and numerically design multi-pulse sequences, including a zero-average constraint; the explicit unconstrained two-pulse global theorem here is not given there. The physical model and filter-function method are established; the specific exact two-pulse global minimizer, unique transcendental timing law, strict finite-correlation displacement, and sharp limiting timing bounds are the assessed mathematical contribution.

## Limitations

The result is restricted to exactly two ideal instantaneous control inversions, stationary centered Gaussian exponential covariance, and pure dephasing. It does not assert optimality over other pulse counts, finite-duration controls, non-Gaussian noise, fluctuating correlation parameters, or pulse calibration errors. It is an optimization theorem for a specified idealized model, not a claim of experimental improvement under additional constraints. Historical-priority uncertainty remains possible in specialized dynamical-decoupling literature despite searches and comparison with the cited sources.

## References

1. L. Cywiński, R. M. Lutchyn, C. P. Nave and S. Das Sarma, *How to Enhance Dephasing Time in Superconducting Qubits*, arXiv:0712.2225 (v1 2007-12-13), https://arxiv.org/abs/0712.2225.
2. Y. Pan, Z. Xi and W. Cui, *Optimal Dynamical Decoupling Sequence for Ohmic Spectrum*, arXiv:1001.2960 (v1 2010-01-18), https://arxiv.org/abs/1001.2960.
3. A. Ajoy, G. A. Álvarez and D. Suter, *Optimal pulse spacing for dynamical decoupling in the presence of a purely-dephasing spin bath*, arXiv:1011.6243 (v1 2010-11-29), https://arxiv.org/abs/1011.6243.
4. Ji and Zhao, *Entanglement dynamics of multi-fluxonium-qubits under Non-Markovian TLS noise*, arXiv:2601.00884 (v1 2025-12-31), https://arxiv.org/abs/2601.00884.
