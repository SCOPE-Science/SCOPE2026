# Exact color-composition law and Gaussian fluctuations among stable cycle opinions

## Finding
For each integer \(n\ge3\), consider labeled agents on the undirected cycle \(C_n\), with blue/white opinions and deterministic synchronous majority updating. When the two neighboring opinions disagree, an agent retains its own opinion. Let \(A_{n,k}\) be the number of fixed-point opinion profiles with exactly \(k\) blue agents. Then \(A_{n,0}=A_{n,n}=1\), and for \(0<k<n\),
\[
A_{n,k}=\sum_{r=1}^{\min(\lfloor k/2\rfloor,\lfloor(n-k)/2\rfloor)}
\frac nr\binom{k-r-1}{r-1}\binom{n-k-r-1}{r-1}.
\]
In particular, for the full polynomial \(P_n(z)=\sum_{k=0}^n A_{n,k}z^k\),
\[
P_n(1)=L_n+2\cos(n\pi/3),
\]
where \(L_n=\varphi^n+(1-\varphi)^n\) is the integer Lucas sequence and \(\varphi=(1+\sqrt5)/2\).

Choose one fixed-point coloring uniformly and denote its blue count by \(K_n\). Then for every \(n\ge3\), \(\mathbb E K_n=n/2\), and as \(n\to\infty\),
\[
\operatorname{Var}(K_n)=\frac{5+3\sqrt5}{40}\,n+O(n^2\varphi^{-n}),\qquad
\frac{K_n-n/2}{\sqrt n}\ \Longrightarrow\ N\!\left(0,\frac{5+3\sqrt5}{40}\right).
\]
The variance constant is approximately \(0.292705098312484\), larger than the \(1/4\) coefficient for independent fair binary choices. This describes the equilibrium **landscape**, not the outcome distribution of a dynamically selected attractor.

## Assumptions and scope
The cycle has labeled vertices indexed cyclically, with \(n\ge3\). Both colors are distinguishable; rotations are not identified. In the synchronous majority model, an agent adopts a strict majority among its two neighbors and preserves its own color at a tie. A stable coloring means an exact one-step fixed point. All probability statements concern the uniform distribution over these stable colorings, not random initial conditions or random updating.

## Proof
**Fixed-point condition.** An agent with both neighbors of the opposite color changes; an agent sharing its color with at least one neighbor stays. Thus a coloring is fixed precisely when it has no isolated singleton monochromatic run, equivalently when each cyclic monochromatic run has length at least two. This is also the fixed-point criterion established in the motivating work.

**Exact weight enumeration.** For \(0<k<n\), a coloring with \(k\) blue vertices decomposes into \(r\) blue runs alternating with \(r\) white runs, each of length at least two. Their lengths form positive ordered compositions of \(k\) and \(n-k\) after subtracting one from every run length; there are respectively \(\binom{k-r-1}{r-1}\) and \(\binom{n-k-r-1}{r-1}\) possibilities. Mark a blue-run beginning and choose its labeled cycle vertex, giving \(n\) choices; each resulting coloring is represented \(r\) times. Division by \(r\) yields the stated formula. Each all-one-color profile contributes one endpoint term.

**Transfer matrix and total.** Index binary pair states in order \((00,01,10,11)\), and let the transition from \((a,b)\) to \((b,c)\) have weight \(z^c\) except when \(a=c\ne b\), in which case it is forbidden. Thus
\[
T(z)=\begin{pmatrix}1&z&0&0\\0&0&0&z\\1&0&0&0\\0&0&1&z\end{pmatrix}.
\]
A closed walk of length \(n\) uniquely corresponds to a labeled periodic binary coloring, and the product of its weights equals \(z^{\text{number of blue vertices}}\). Hence \(P_n(z)=\operatorname{tr}(T(z)^n)\). Direct determinant expansion gives
\[
\det(\lambda I-T(z))=\lambda^4-(1+z)\lambda^3+z\lambda^2-z^2.
\]
At \(z=1\), this factors as \((\lambda^2-\lambda-1)(\lambda^2-\lambda+1)\); summing the \(n\)-th powers of the eigenvalues gives \(P_n(1)=L_n+2\cos(n\pi/3)\).

**Limit law.** For real \(z>0\), \(T(z)\) is irreducible and aperiodic (both constant-color states have loops), hence has a simple strictly dominant Perron eigenvalue \(\lambda(z)\), analytic around \(z=1\). Write \(\lambda(1)=\varphi\). Differentiating the displayed quartic implicitly at \(z=1\) gives
\[
\lambda'(1)=\frac{1+\sqrt5}{4},\qquad \lambda''(1)=\frac18-\frac{\sqrt5}{40}.
\]
For \(M_n(t)=\mathbb E[e^{tK_n}]=P_n(e^t)/P_n(1)\), the spectral gap implies, uniformly near \(t=0\),
\[
\log M_n(t)=n\log\frac{\lambda(e^t)}{\varphi}+O(\rho^n)
\]
for some \(\rho<1\) (and derivatives have exponentially small errors up to polynomial factors). The first derivative at zero is \(\lambda'(1)/\varphi=1/2\), while the second equals
\[
\frac{\lambda'(1)}{\varphi}+\frac{\lambda''(1)}{\varphi}-\left(\frac{\lambda'(1)}{\varphi}\right)^2=\frac{5+3\sqrt5}{40}.
\]
Color complementation proves \(\mathbb E K_n=n/2\) exactly at finite \(n\). Taylor expansion of \(\log M_n(t/\sqrt n)\) after centering gives convergence of moment-generating functions to \(\exp((5+3\sqrt5)t^2/80)\), yielding the claimed central limit theorem. The non-leading eigenvalues at \(z=1\) all have modulus at most one, so differentiating the finite spectral representation supplies the stated \(O(n^2\varphi^{-n})\) variance remainder.

## Verification
The standalone script `verify.py` exhaustively enumerates each binary profile for \(3\le n\le16\), tests the actual majority best-response condition, computes the run-composition coefficients independently, and compares those with traces of the explicit polynomial transfer matrix. Every case passed. The implicit eigenvalue-derivative calculation was also checked by exact symbolic differentiation; sample variance-over-\(n\) values for \(n=12,20,30\) were respectively approximately \(0.29012345679\), \(0.29274097580\), and \(0.29270464929\).

## Relationship to prior work
Zehmakan (2023) establishes the stable-coloring characterization and the exponential order \(\Theta(\varphi^n)\) of its total count, alongside convergence and random-initial-condition results. Those facts are not presented as new. The contribution here is the exact two-color composition spectrum and a closed quantitative fluctuation law for the uniform fixed-point ensemble. The four-state transfer-matrix argument is standard as a technique, and the total counting sequence has classical combinatorial interpretations; the claimed distinction is the explicit equilibrium-composition distribution and its limiting variance in this opinion model. Equivalent enumerative or thermodynamic formulas in the broader cyclic-word literature may exist.

## Limitations
The central limit theorem concerns uniform sampling over all stable profiles and must not be interpreted as the probability distribution of eventual states reached from uniformly random initial conditions; those absorption basins are not uniformly sized. No convergence rates beyond the displayed variance remainder, local central limit theorem, or arbitrary-graph claim is made. The transfer matrix uses a natural finite-state encoding; it is not claimed to be a newly invented technique.

## References
1. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first released 2023-02-14, https://arxiv.org/abs/2302.06760.
2. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems (2024), https://link.springer.com/article/10.1007/s10458-024-09651-y.
3. OEIS A007040, cyclic binary run-restriction count, https://oeis.org/A007040; related combinatorial background, not asserted to tabulate the present weighted fixed-point count.
