# Coprimality exactly characterizes geometric coordinate autocovariance in random affine interval maps

## Finding
Fix integers \(M,N\geq2\), let \(0<p<1\), and set \(q=1-p\), \(d=\gcd(M,N)\), and \(\rho=p/N+q/M\). For the stationary random interval process defined below, write \(C_n=\operatorname{Cov}(X_0,X_n)\). The following conditions are equivalent:

1. \(\gcd(M,N)=1\).
2. For **every** integer \(n\geq0\), the covariance is \(C_n=\rho^n/12\).
3. Already at lag two, \(C_2C_0=C_1^2\).

Indeed, for **every** pair of bases the exact first three covariances are
\[
C_0=\frac1{12},\qquad C_1=\frac{\rho}{12},\qquad C_2=\frac{\rho^2}{12}+\frac{pq(d^2-1)}{12MN}.
\]
For coprime bases, therefore, the exact integrated covariance is
\[
\sum_{n=0}^{\infty}C_n=\frac{1}{12(1-\rho)}.
\]
This persists at the zero-Lyapunov probability \(p=\log M/(\log M+\log N)\), even though the accompanying common-noise two-point motion exhibits intermittent behavior. The theorem concerns a single stationary trajectory's **annealed coordinate covariance**, not the separation of two trajectories driven by a common environment.

## Assumptions and scope
The state space is \([0,1)\). The independently sampled maps are \(T_N(x)=\{Nx\}\), taken with probability \(p\), and \(S_{M,j}(x)=(x+j)/M\) for integers \(0\leq j<M\), each taken with probability \(q/M\). These are the expanding and uniformly chosen contracting branches of Homburg and Kalle (arXiv:2207.09987v1), with their parameter convention. Start \(X_0\) uniformly in \([0,1)\), independent of all subsequent map choices. Stationarity holds because both the expanding map and the uniform mixture of inverse branches preserve Lebesgue probability. Normalize the coordinate as \(f(x)=x-1/2\); thus \(C_n=\mathbb E[f(X_0)f(X_n)]\). The equivalence requires \(0<p<1\): at deterministic endpoints, the covariance can be geometric regardless of the greatest common divisor.

## Proof
**1. Markov--Fourier representation.** Let \(e_k(x)=e^{2\pi i kx}\) for \(k\in\mathbb Z\). On \(L^2([0,1),dx)\), the random Koopman operator is \(P=pA+qB\), where \(A g(x)=g(T_N(x))\) and \(B g(x)=M^{-1}\sum_{j=0}^{M-1}g(S_{M,j}(x))\). For integer frequencies,
\[
Ae_k=e_{Nk},\qquad Be_k=\begin{cases}e_{k/M},&M\mid k,\\0,&M\nmid k.\end{cases}
\]
Consequently \(AB=BA\) **if and only if** \(\gcd(M,N)=1\): if coprime, \(M\mid Nk\) exactly when \(M\mid k\); if not, the mode \(k=M/d\) is killed by \(AB\) but not by \(BA\).

**2. Fourier covariance kernel.** The centered coordinate has \(\widehat f(0)=0\) and \(\widehat f(k)=-1/(2\pi i k)\) for nonzero integer \(k\). Thus, for nonnegative integers \(j,\ell\),
\[
\langle f,A^jB^\ell f\rangle=\frac{1}{12N^jM^\ell}.
\]
To verify this identity, only initial modes divisible by \(M^\ell\) survive. The input frequency \(M^\ell t\) becomes \(N^jt\). The inner product is \(\sum_{t\ne0}(4\pi^2N^jM^\ell t^2)^{-1}\), which equals the displayed expression since \(\sum_{t\ne0}t^{-2}=\pi^2/3\). All operations are bounded on \(L^2\), justifying Fourier approximation by trigonometric polynomials and the limit.

**3. Coprime all-lag law.** For \(d=1\), the operators \(A\) and \(B\) commute. The binomial theorem and Step 2 yield for every \(n\geq0\)
\[
C_n=\langle f,P^nf\rangle=\sum_{j=0}^n\binom njp^jq^{n-j}\frac{1}{12N^jM^{n-j}}=\frac1{12}\left(\frac pN+\frac qM\right)^n.
\]
Both bases are at least two, hence \(0<\rho\le1/2<1\), so the geometric sum is valid. The Lyapunov exponent is \(p\log N-q\log M\); at the unique zero parameter \(p=\log M/(\log M+\log N)\), this formula is unaffected.

**4. Exact noncoprime obstruction.** Irrespective of coprimality, the pure terms satisfy \(\langle f,A^2f\rangle=1/(12N^2)\) and \(\langle f,B^2f\rangle=1/(12M^2)\). The mixed terms differ:
\[
\langle f,ABf\rangle=\frac1{12MN},\qquad
\langle f,BAf\rangle=\frac{d^2}{12MN}.
\]
For the latter, \(M\mid Nk\) means \(k\) is a multiple of \(M/d\); its image frequency is then a multiple of \(N/d\). Repeating the Fourier-coefficient calculation proves the factor \(d^2\). Expand \(P^2\), obtaining
\[
C_2=\frac{p^2}{12N^2}+\frac{q^2}{12M^2}+\frac{pq(1+d^2)}{12MN}=
\frac{\rho^2}{12}+\frac{pq(d^2-1)}{12MN}.
\]
Also \(C_0=1/12\) and \(C_1=\rho/12\). Because \(pq>0\), the second-lag excess vanishes **exactly** when \(d=1\). This proves both converses and the equivalence.

## Verification
The standalone `checker.py` uses independent exact-rational integration of the piecewise-affine random trajectories. It partitions the starting interval at every expanding-branch discontinuity, tracks all contracting choices and their probabilities, and integrates \((x-1/2)(X_n(x)-1/2)\) as a polynomial over each rational subinterval. It checks the all-lag formula for several coprime bases through lag four and the general second-lag formula for noncoprime bases. This is a finite consistency check; the preceding Fourier calculation proves the arbitrary-base and arbitrary-lag statements.

## Relationship to prior work
Homburg and Kalle (arXiv:2207.09987v1, first public July 20, 2022) define precisely this randomly expanding/contracting interval system, show Lebesgue stationarity (Proposition 2.1), and analyze common-noise two-point motion, including the zero-Lyapunov regime. They do not state the single-orbit all-lag coordinate covariance or the coprimality criterion in the inspected preprint. Yan and coauthors (arXiv:2308.09269) study position autocorrelation of a **different** random expanding/contracting map with only one contracting branch and a nonuniform invariant density. Kalle and Zeegers (arXiv:2206.07601) study correlations for **different** superattracting intermittent maps. A related result for equal expanding and contracting bases analyzes a different arithmetic regime; in particular, equal bases fail the coprimality condition. The new conclusion is the exact arithmetic equivalence and complete geometric law in this stationary affine family, rather than a generic random-map decay theorem.

## Limitations
No claim is made about quenched correlations, other observables, the full mixing spectrum, uniqueness of the stationary law, or pair-distance statistics. At deterministic endpoints \(p=0\) or \(p=1\), the equivalence fails and those endpoints are excluded. The preprint and explicitly identified related works were inspected; possible equivalent formulas in uncatalogued operator/Markov literature remain an originality risk. Independent verification and priority assessment have not been performed.

## References
1. A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (2022), especially equations (1.1)--(1.4), Proposition 2.1, Theorem 1.1 and Section 3. https://arxiv.org/html/2207.09987v1
2. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (2023), Sections II--III and Appendix D. https://arxiv.org/abs/2308.09269
3. C. Kalle and B. Zeegers, *Decay of correlations for critically intermittent systems*, arXiv:2206.07601v1 (2022), especially equations (1.3)--(1.5) and Theorem 1.3. https://arxiv.org/pdf/2206.07601
