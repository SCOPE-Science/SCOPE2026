# Factorial synchronization with a logarithmic-square correction at the critical coupled-logistic extinction point

## Finding
Consider the two-site, state-diffusively coupled logistic map
\[
(x_{n+1},y_{n+1})=\bigl(x_n(1-x_n)+\varepsilon(y_n-x_n),\ y_n(1-y_n)+\varepsilon(x_n-y_n)\bigr),
\]
with fixed \(0\le\varepsilon\le1/2\) and initial coordinates \(0<x_0,y_0<1/2\), \(x_0\ne y_0\). Put \(u_n=(x_n+y_n)/2\), \(d_n=(x_n-y_n)/2\), and \(\lambda=1-2\varepsilon\). Both coordinates remain strictly inside \((0,1/2)\), and \(x_n,y_n\to0\) with \(n u_n\to1\).

There is a sharp trichotomy in the **absolute synchronization error** \(|x_n-y_n|\):

1. At zero coupling, \(\varepsilon=0\), there is a constant \(A_0>0\) depending on the initial pair such that
   \[
   |x_n-y_n|\sim A_0 n^{-2}.
   \]
2. For every fixed \(0<\varepsilon<1/2\), either exact synchronization occurs at a finite time (and persists), or there is a constant \(A_{\varepsilon}>0\) such that
   \[
   |x_n-y_n|\sim A_{\varepsilon}\lambda^n n^{-2/\lambda}.
   \]
   The exceptional finite-hit condition is exactly \(\lambda=2u_j\) for some integer \(j\ge0\) before synchronization.
3. At maximal coupling, \(\varepsilon=1/2\), define the well-defined orbit-dependent constant
   \[
   C=\lim_{n\to\infty}\bigl(u_n^{-1}-n-\log n\bigr).
   \]
   There is \(A_{1/2}>0\) for which the sharper factorial law holds:
   \[
   |x_n-y_n|\sim A_{1/2}\,\frac{2^n}{\Gamma(n)}\,n^{-C}
   \exp\!\left[-\tfrac12(\log n)^2\right].
   \]
   The signed discrepancy \(x_n-y_n\) reverses sign at every iteration. In particular, its factorial normalization has the **universal** logarithmic-square coefficient \(-1/2\):
   \[
   \lim_{n\to\infty}\frac{\log|x_n-y_n|+\log\Gamma(n)-n\log2}{(\log n)^2}=-\tfrac12.
   \]

All asymptotics are for fixed initial data and fixed coupling, and none is asserted uniformly when \(\varepsilon\) approaches an endpoint. The amplitude constants are positive but need not have elementary closed forms.

## Assumptions and scope
The map acts on the invariant open square \((0,1/2)^2\). Its logistic growth parameter is exactly one, the extinction/transcritical threshold of the uncoupled logistic map. Coupling is applied **to the state variables after the logistic terms**, not to the two logistic outputs. The permissible coupling interval is the closed interval \([0,1/2]\). We quantify forward trajectories from every distinct positive initial pair in that square, with the explicitly stated possible finite synchronization for interior couplings. Asymptotic equivalence is for the positive error magnitude and the usual natural logarithm.

## Proof
**Invariant region and recurrence.** For \(0<x,y<1/2\),
\[
0<x(1-x)+\varepsilon(y-x)=(1-\varepsilon)x+\varepsilon y-x^2<1/2,
\]
where the lower inequality follows from \(1-\varepsilon-x>0\) and the upper inequality from \((1-\varepsilon)x+\varepsilon y<1/2\). The same holds with coordinates exchanged. Direct expansion gives the *exact* center/difference recurrences
\[
u_{n+1}=u_n-u_n^2-d_n^2,\qquad
 d_{n+1}=(\lambda-2u_n)d_n.\tag{1}
\]
Because \(0<|d_n|<u_n<1/2\), the mean strictly decreases and
\(0<u_{n+1}\le u_n-u_n^2\). Thus \(u_n\to0\), and all iterates stay positive. Moreover, if \(w_n=u_n^{-1}\) and \(t_n=d_n/u_n\), then
\[
w_{n+1}-w_n=\frac{1+t_n^2}{1-(1+t_n^2)/w_n}.\tag{2}
\]
The inequalities \(w_{n+1}-w_n\ge1\) and
\(w_{n+1}-w_n\le2/(1-2u_0)\) imply
\[
w_0+n\le w_n\le w_0+\frac{2n}{1-2u_0}.\tag{3}
\]

**Sharper mean asymptotics at positive coupling.** When \(0<\varepsilon\le1/2\), one has \(0\le\lambda<1\), and, since \(u_n\le u_0\),
\[
|\lambda-2u_n|\le q:=\max\{\lambda,|\lambda-2u_0|\}<1.
\]
By (1), \(|d_n|\le|d_0|q^n\). Combining with (3) yields \(\sum_{n\ge0}t_n^2<\infty\). Equation (2) consequently gives, for all sufficiently large \(n\),
\[
w_{n+1}-w_n=1+w_n^{-1}+O(w_n^{-2}+t_n^2).
\]
Summation and (3) first give \(w_n=n+O(\log n)\). Hence
\(w_n^{-1}=n^{-1}+O(\log n/n^2)\) for \(n\ge1\), and summation a second time shows the existence of a finite \(C\), with
\[
w_n=n+\log n+C+O(\log n/n).\tag{4}
\]
Indeed the increment of \(w_n-n-\log n\) is \(O(\log n/n^2+t_n^2)\); its tail is \(O(\log n/n)\) because \(t_n\) decreases geometrically up to a polynomial factor. It follows also that
\[
\sum_{j=1}^{n-1}u_j=\log n+L+o(1)\tag{5}
\]
for some finite \(L\), and \(n u_n\to1\).

**Interior coupling.** Fix \(0<\varepsilon<1/2\), so \(0<\lambda<1\). From (1), either some factor \(\lambda-2u_j\) vanishes and all subsequent differences vanish, or every factor is nonzero and eventually positive. In the latter case,
\[
\log|d_n|=\log|d_0|+\sum_{j=0}^{n-1}\log|\lambda-2u_j|.
\]
For all sufficiently large \(j\),
\(\log|\lambda-2u_j|=\log\lambda-2u_j/\lambda+O(u_j^2)\).
Since \(\sum_j u_j^2<\infty\), formula (5) proves
\[
\log|d_n|=n\log\lambda-\frac2\lambda\log n+K_\varepsilon+o(1)
\]
with finite real \(K_\varepsilon\). Exponentiation, with \(|x_n-y_n|=2|d_n|\), yields the asserted positive constant \(A_\varepsilon\).

**Maximal coupling and universal logarithmic-square modulation.** At \(\varepsilon=1/2\), the second recurrence in (1) is \(d_{n+1}=-2u_nd_n\). Thus no nonzero difference can reach zero, the sign flips each step, and
\[
|d_n|=|d_0|\,2^n\prod_{j=0}^{n-1}u_j.
\]
By (4), for sufficiently large integers \(j\),
\[
\log(ju_j)=-\frac{\log j+C}{j}
                  +O\!\left(\frac{(1+\log j)^2}{j^2}\right).
\]
The remainder is absolutely summable. The classical integral comparison of the harmonic sums implies both limits
\[
\sum_{j=1}^{n-1}\frac1j-\log n\to\gamma,
\qquad
\sum_{j=1}^{n-1}\frac{\log j}{j}-\frac12(\log n)^2\to\gamma_*,
\]
where the exact values of the finite constants are unnecessary. Since \(\prod_{j=1}^{n-1}j=\Gamma(n)\), these identities give
\[
\log|d_n|=n\log2-\log\Gamma(n)
 -\frac12(\log n)^2-C\log n+K_*+o(1).
\]
Exponentiating establishes the factorial law with \(A_{1/2}=2e^{K_*}>0\), as well as the displayed universal limit.

**Zero coupling.** At \(\varepsilon=0\), each coordinate separately obeys \(z_{n+1}=z_n-z_n^2\). Its reciprocal \(W_n=1/z_n\) evolves by
\(W_{n+1}=W_n+1+1/(W_n-1)\), so \(W_n=n+\log n+c_z+o(1)\) by the same summable-increment argument. For two distinct initial coordinates,
\[
W_{x,n+1}-W_{y,n+1}
 =(W_{x,n}-W_{y,n})
 \left(1-\frac1{(W_{x,n}-1)(W_{y,n}-1)}\right).
\]
Every factor is strictly between zero and one because \(W_{x,n},W_{y,n}>2\); the sum of their deficits is finite by their linear growth. Therefore the product converges to a nonzero limit, \(W_{x,n}-W_{y,n}\to\Delta\ne0\). Finally,
\[
|x_n-y_n|=\frac{|W_{x,n}-W_{y,n}|}{W_{x,n}W_{y,n}}
 \sim|\Delta|n^{-2}.
\]
This also proves \(nu_n\to1\) at zero coupling and completes the trichotomy.

## Verification
The independent `verify.py` reproduces both center/difference identities with symbolic algebra, checks the fixed-point Jacobian eigenvalues \(1\) and \(1-2\varepsilon\), and checks rational initial-condition itineraries exactly across all coupling regimes. It then accumulates the logarithm of the transverse difference to avoid floating-point underflow and tests the proposed normalizations at \(\varepsilon=0,1/10,9/20,1/2\), recording stabilization of the asymptotic amplitudes. It returned `VERIFY_OK` in the supplied package. Numerical tests are auxiliary; the proof above covers every specified initial pair and each fixed parameter, including the infinite-time limits.

## Relationship to prior work
The state-diffusive two-site logistic recurrence is explicit in L. D. Hoffman's *The Control of Chaotic Maps* (university archive record made public in 2012, describing an earlier dissertation), whose available abstract concentrates on equilibria, Lyapunov exponents and chaotic-orbit control. Schult, Creamer, Henyey and Wright (1987) study coupled logistic maps broadly. Giberti and Vernia (1994) examine normally attracting manifolds and periodic behavior in coupled-map lattices, while López-Ruiz and Fournier-Prunaret (2004) use a distinct multiplicative symbiosis coupling. Mareno and English (2020) investigate a **different** two-site coupling in which the coupling weights multiply entire logistic-map outputs; their origin's transverse eigenvalue is \(r(1-2\varepsilon)\), rather than \(r-2\varepsilon\) for state diffusion. At the maximal coupling their two coordinates coalesce after one step, so that map does not imply the nonzero factorial discrepancy derived here.

The quantitative three-regime law, and especially the logarithmic-square correction at the double-degenerate extinction/coupling endpoint, was not located in the accessible inspected material or targeted mathematical-result searches. This is a best-knowledge priority assessment, not a proof of historical uniqueness.

## Limitations
The full texts of several historically relevant papers, including Schult et al. (1987), Giberti--Vernia (1994), and the Hoffman dissertation, were not continuously inspectable in this investigation. Those access limits leave a real possibility of antecedent or equivalent asymptotic results. The theorem is deterministic, local to an explicit invariant square, fixed-parameter, and does not claim a uniformly valid crossover when coupling approaches either endpoint. Exact finite-time coalescence for exceptional interior-coupling initial points is separated explicitly. No claim is made about global basins outside the invariant square, chaotic regimes or noise robustness.

## References
- L. D. Hoffman, *The Control of Chaotic Maps*, University of Johannesburg archive record, dated 2012-09-04; https://hdl.handle.net/10210/6845 .
- R. L. Schult, D. B. Creamer, F. S. Henyey and J. A. Wright, *Symmetric and nonsymmetric coupled logistic maps*, Physical Review A 35 (1987), 3115--3118, https://doi.org/10.1103/PhysRevA.35.3115 .
- C. Giberti and C. Vernia, *Normally attracting manifolds and periodic behavior in one-dimensional and two-dimensional coupled map lattices*, Chaos 4 (1994), 651--663, https://doi.org/10.1063/1.166042 .
- R. López-Ruiz and D. Fournier-Prunaret, *Complex behavior in a discrete coupled logistic model for the symbiotic interaction of two species*, Mathematical Biosciences and Engineering 1 (2004), 307--324, https://www.aimspress.com/fileOther/PDF/MBE/1551-0018_2004_2_307.pdf .
- A. Mareno and L. Q. English, *Flip and Neimark--Sacker Bifurcations in a Coupled Logistic Map System*, Discrete Dynamics in Nature and Society (2020), 4103606, https://doi.org/10.1155/2020/4103606 .
