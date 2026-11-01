# A sharp \(e^{-1}\) conditioning transition for circular Fock interpolation

## Finding

Consider the classical Bargmann–Fock space
\[
\mathcal F^2=\left\{f\text{ entire}:\ \|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}
\]
with reproducing kernel \(K(z,w)=e^{z\overline w}\). Fix \(\rho>0\), let \(N\ge2\) be an integer, put \(\omega_N=e^{2\pi i/N}\), and choose the regular circular interpolation nodes
\[
z_j=\sqrt{\rho N}\,\omega_N^j\qquad(0\le j<N).
\]
Let \(G_N\) be the Gram matrix of their **unit-normalized** reproducing kernels
\[
k_j(z)=\exp\bigl(z\overline{z_j}-\rho N/2\bigr),
\qquad
G_N=(\langle k_\ell,k_j\rangle)_{j,\ell=0}^{N-1}\quad\text{with }\langle f,g\rangle=\pi^{-1}\int_{\mathbb C}f\overline g\,e^{-|z|^2}dA.
\]
Write \(\lambda_{N,\min}\) and \(\lambda_{N,\max}\) for its extreme eigenvalues, and define the **squared interpolation condition number**
\[
\kappa_N(\rho)=\frac{\lambda_{N,\max}}{\lambda_{N,\min}}.
\]
Thus its entries are \(G_{N,j\ell}=\exp[\rho N(\omega_N^{j-\ell}-1)]\), and \(v^{(k)}_j=\omega_N^{kj}\) denotes the corresponding Fourier eigenvector convention. All eigenvalues are strictly positive. Their exact expression as Poisson residue masses is previously known; the following uniform-in-mode extremal asymptotics are the finding.

Define, for \(x>0\),
\[
I_\rho(x)=\rho-x+x\log(x/\rho),\qquad I_\rho(0)=\rho,
\]
and the threshold \(\rho_c=e^{-1}\). For every fixed \(0<\rho\le\rho_c\), set \(H_\rho=I_\rho(1)=\rho-1-\log\rho\). Then, as \(N\to\infty\),
\[
\boxed{\lambda_{N,\min}=\frac{\sqrt N}{\rho\sqrt{2\pi}}e^{-NH_\rho}\bigl(1+O_\rho(N^{-1})\bigr),\qquad
\kappa_N(\rho)=\sqrt\rho\,e^{NH_\rho}\bigl(1+O_\rho(N^{-1})\bigr).}
\]
Moreover **the unique minimizing Fourier mode is \(N-1\) for all sufficiently large \(N\)**, including at \(\rho=e^{-1}\).

For each fixed \(\rho>\rho_c\), let \(u=u_\rho>0\) be the unique solution of
\[
(u+1)\log(u+1)-u\log u=1+\log\rho.
\]
It satisfies \(u<\rho<u+1\) and \(I_\rho(u)=I_\rho(u+1)\). Set
\[
H_\rho=I_\rho(u),\quad a=\rho/u>1,\quad b=\rho/(u+1)<1,
\quad\eta_N=\{Nu\},
\]
where braces denote fractional part. Define the strictly positive, bounded, explicit factor
\[
D_N(\rho)=\min_{m\in\mathbb Z}\left\{
\frac{a^{m-\eta_N}}{\sqrt u}
+\frac{b^{m-\eta_N}}{\sqrt{u+1}}
\right\}.
\]
Then
\[
\boxed{\lambda_{N,\min}=\sqrt{\frac{N}{2\pi}}e^{-NH_\rho}
\bigl(D_N(\rho)+O_\rho(N^{-1})\bigr),\qquad
\kappa_N(\rho)=\frac{e^{NH_\rho}}{\sqrt\rho\,D_N(\rho)}
\bigl(1+O_\rho(N^{-1})\bigr).}
\]
The implicit minimum in \(D_N\) requires at most **two evaluations**: the real function minimized has its unique continuous minimizer at
\[
\delta_*=\frac{\log\!\left(\frac{-\log b}{\log a}\sqrt{\frac{u}{u+1}}\right)}{\log(a/b)},
\]
so one evaluates integers immediately below and above \(\eta_N+\delta_*\). Every minimizing Fourier mode differs by a bounded number of integers, modulo \(N\), from \(Nu\). In both regimes,
\[
\boxed{\lim_{N\to\infty}\frac1N\log\kappa_N(\rho)=H_\rho>0.}
\]
Thus the asymptotic worst-mode mechanism changes exactly at \(\rho=e^{-1}\): an endpoint residue controls the subcritical and critical regimes, while two competing Poisson aliases control the supercritical regime and create a fractional-phase modulation in the leading coefficient.

## Assumptions and scope

All claims hold for every **fixed** real \(\rho>0\), with constants in the error terms allowed to depend on \(\rho\). The limit varies \(N\) with squared node radius precisely \(|z_j|^2=\rho N\); no assertion is made for a varying \(\rho\) approaching the critical value. The condition number here is the ratio of **Gram eigenvalues**, equivalently the square of the singular-value condition number for the normalized evaluation operator on the span of the kernel vectors. It is not the condition number of an unnormalized kernel matrix.

## Proof

**1. Exact Fourier diagonalization.** Set \(t=\rho N\). The normalized Gram entries are \(G_{j\ell}=\exp[t(\omega_N^{j-\ell}-1)]\). Expanding the exponential and taking the discrete Fourier transform gives, for \(0\le k<N\),
\[
\lambda_{N,k}=N e^{-t}\sum_{r=0}^{\infty}\frac{t^{k+rN}}{(k+rN)!}
=N\,\Pr\{X_N\equiv k\pmod N\},
\quad X_N\sim\operatorname{Poisson}(t).
\tag{1}
\]
This identity, including the Fourier diagonalization, is established in the circular coherent-state literature [2]; it is recalled here to identify the object and fix normalization. Positivity follows directly from the first summand. Denote the Poisson mass at the integer \(n\) by \(p_n=e^{-t}t^n/n!\).

**2. Largest eigenvalue.** The Poisson mode is an integer within one of \(t\); Stirling's formula yields
\[
\max_{n\ge0}p_n=\frac{1}{\sqrt{2\pi\rho N}}\bigl(1+O_\rho(N^{-1})\bigr).
\]
At most one integer in each residue class lies within \(\varepsilon N\) of \(t\), for any sufficiently small fixed \(\varepsilon>0\). Strict convexity of \(I_\rho\) and its unique zero at \(x=\rho\) show that all other summands are exponentially smaller than the global Poisson maximum, uniformly over residues. Conversely the residue containing an integer mode attains that maximum to the same relative precision. Hence
\[
\lambda_{N,\max}=\sqrt{\frac N{2\pi\rho}}\bigl(1+O_\rho(N^{-1})\bigr).
\tag{2}
\]

**3. Pinned residue up through the critical point.** Suppose \(0<\rho\le e^{-1}\). Since \(p_n\) is unimodal in \(n\), the least mass among \(p_0,\ldots,p_{N-2}\) is attained at one of its endpoints. The exact adjacent-mass relation gives
\[
\frac{p_{N-2}}{p_{N-1}}=\frac{N-1}{\rho N}\longrightarrow\rho^{-1}>1.
\]
Stirling also gives
\[
\frac{p_0}{p_{N-1}}=\rho\sqrt{2\pi N}\,
\exp\!\bigl(N(-1-\log\rho)\bigr)\bigl(1+O(N^{-1})\bigr).
\]
For \(\rho<e^{-1}\) this grows exponentially; at \(\rho=e^{-1}\) it still grows as \(\sqrt N\). Thus every \(p_k\) with \(0\le k\le N-2\) exceeds \(p_{N-1}\) by a factor bounded below by a fixed number greater than one for all large \(N\). At the same time, because \(\rho<1\), the remaining terms in the residue \(N-1\) satisfy
\[
\sum_{r\ge1}p_{N-1+rN}=o(p_{N-1})
\]
with an exponentially small ratio, by Stirling and strict increase of \(I_\rho\) above \(1\). Every other residue mass is at least \(p_k\). Therefore \(N-1\) is the unique least eigenmode and
\[
\lambda_{N,\min}=Np_{N-1}(1+O_\rho(e^{-c_\rho N}))
=\frac{\sqrt N}{\rho\sqrt{2\pi}}e^{-NI_\rho(1)}
\bigl(1+O_\rho(N^{-1})\bigr).
\]
Combining with (2) proves the first regime.

**4. The two-alias balancing point.** Suppose \(\rho>e^{-1}\). The function
\[
\varphi(u)=(u+1)\log(u+1)-u\log u
\]
is strictly increasing from \(0\) to infinity for \(u>0\), because \(\varphi'(u)=\log((u+1)/u)>0\). Thus the equation defining \(u\) has exactly one positive solution. Rearrangement yields \(I_\rho(u)=I_\rho(u+1)\). Equivalently,
\[
\log\rho=\int_u^{u+1}\log x\,dx,
\]
so strict monotonicity of the logarithm gives \(u<\rho<u+1\). As \(I_\rho\) is strictly convex, on the open interval \((u,u+1)\) it lies **strictly below** the common endpoint height \(H_\rho\).

For each residue \(k\), there is exactly one integer \(n_k\equiv k\pmod N\) in the half-open interval \([Nu,N(u+1))\); it is nonnegative for sufficiently large \(N\). Since Stirling is uniform for \(n/N\in[u,u+1]\), there is a constant \(C_\rho>0\) such that
\[
Np_{n_k}\ge C_\rho\sqrt N\,e^{-N I_\rho(n_k/N)}.
\tag{3}
\]
By continuity, strict convexity and the nonzero endpoint slopes \(I_\rho'(u)=\log(u/\rho)<0\) and \(I_\rho'(u+1)=\log((u+1)/\rho)>0\), there is \(c_\rho>0\) with
\[
H_\rho-I_\rho(x)\ge c_\rho\min\{x-u,u+1-x\}
\quad\text{for all }x\in[u,u+1].
\tag{4}
\]
On the other hand, choose an integer \(n\) within distance one of \(Nu\) and its residue \(k_*\). Because all other congruent integers, apart from \(n\) and \(n+N\), have Poisson rate **strictly greater** than \(H_\rho\), uniform Stirling and geometric tail control give
\[
\lambda_{N,k_*}\le C'_\rho\sqrt N\,e^{-NH_\rho}.
\tag{5}
\]
The combination of (1), (3), (4) and (5) forces every globally minimizing residue to satisfy
\[
\min\{n_k-Nu,N(u+1)-n_k\}=O_\rho(1).
\tag{6}
\]
Indeed the left-hand side enters as a positive exponential in the lower bound (3) while (5) supplies a fixed upper competitor. We may therefore represent every minimizing residue by an integer \(n=Nu+\delta\) with \(|\delta|\le C''_\rho\); the two dominant terms are at \(n\) and \(n+N\). This localization is uniform in the fractional phase \(\{Nu\}\).

**5. Uniform local expansion and discrete phase.** For bounded \(\delta\), Stirling's expansion uniformly yields
\[
\begin{aligned}
Np_{Nu+\delta}&=\sqrt{\frac N{2\pi}}e^{-NH_\rho}
\left(\frac{(\rho/u)^\delta}{\sqrt u}+O_\rho(N^{-1})\right),\\
Np_{N(u+1)+\delta}&=\sqrt{\frac N{2\pi}}e^{-NH_\rho}
\left(\frac{(\rho/(u+1))^\delta}{\sqrt{u+1}}+O_\rho(N^{-1})\right).
\end{aligned}
\tag{7}
\]
The expression \(Np_s\) for a noninteger subscript is used here only when \(s=Nu+\delta\) is an integer. All other aliases are \(O_\rho(e^{-c_\rho N})\) relative to (7), by the strict rate gaps outside \([u,u+1]\). Integer constraints on \(n\) mean exactly \(\delta=m-\eta_N\) for \(m\in\mathbb Z\). The positive function
\[
F(\delta)=a^\delta/\sqrt u+b^\delta/\sqrt{u+1}
\]
is strictly convex, tends to infinity at both ends of the real line, and has the unique stationary point \(\delta_*\) displayed above. Its minimum over the shifted integer lattice therefore exists in a uniformly bounded region. Taking the minimum of the uniform error estimates (7) over that region establishes the lower-eigenvalue formula with additive \(O_\rho(N^{-1})\) relative to the displayed \(\sqrt N e^{-NH_\rho}\) scale. Since \(F\) has a strictly positive real minimum and admits a uniformly bounded nearest-integer test, \(D_N\) stays between two strictly positive constants. Division into (2) proves the supercritical condition-number formula. Positivity of \(H_\rho\) follows from \(u\ne\rho\) and strict convexity of the Poisson rate.

The two formulas imply the logarithmic growth limit and complete the proof.

## Verification

`CHECK.py` uses only the Python standard library and was executed from the supplied artifact. It checks the exact discrete-Fourier spectrum independently against direct complex Gram-kernel Fourier sums on small instances, verifies the equation and ordering of the balancing point, and checks the two asymptotic regimes at several fixed ratios and four increasing dimensions. The executed checker passed 85 assertions. These finite numerical checks do not prove the asymptotic theorem; Steps 2–5 above provide its universal analytical justification. The published exact Gram eigenvalue identity has been distinguished explicitly from the new asymptotic minimization.

## Relationship to prior work

The 2026 work of Alpay, De Martino and Diki [1] develops complex reproducing-kernel representer methods and Fock-space superoscillatory learning examples. Its Section 4.1 uses collinear Fock nodes rather than regular circular node families; it does not establish condition-number limits for growing circles.

Horoshko, De Bièvre, Kolobov and Patera [2], especially their Eq. (9) and Sec. III–IV, **already give the exact Poisson-residue Fourier spectrum for circular coherent states**. Hence (1) is background, not asserted as original. Their asymptotic discussion concerns state/entanglement behavior, not the worst Gram eigenvalue when the radius-squared parameter is exactly proportional to the number of nodes. The present mathematical distinction is the sharp minimization over all growing residue classes, the critical value \(e^{-1}\), the pinned critical boundary mode and the leading oscillatory two-alias prefactor.

Luo, Tang and Zhang [3] study optimal circular states for average photon number and nonclassicality; only a publisher preview of their complete article was available. The accessible material does not identify these interpolation-conditioning asymptotics, but a full-text implication comparison remains an originality risk. Janszky, Domokos and Adam [4] provide foundational circle-state constructions; an accessible abstract, not the entire paper, was inspected. These access limits are substantive and are not presented as proofs of absence.

## Limitations

The analysis applies to one classical Fock space, equally spaced points on a single circle, and fixed \(\rho\). It does not give uniform asymptotics in a critical \(N\)-dependent window around \(\rho=e^{-1}\), and makes no assertion for perturbed polygons, other reproducing kernels, or nonuniform data sampling. The asymptotic assertion determines the least eigenvalue and a worst-mode localization, not an exact finite-\(N\) formula for the minimizing residue in the supercritical regime. Previously published exact Gram eigenvalues already permit finite numerical calculation; the added result is their sharp nontrivial simultaneous \(N\)-large extremal analysis. Complete full-text coverage of all historical circular-state literature was not possible; a later equivalent formulation cannot be excluded categorically. No independent mathematical audit has been performed.

## References

[1] N. Alpay, A. De Martino and K. Diki, *Representer theorem in complex reproducing kernel Hilbert spaces with applications to Fock and Hardy spaces and superoscillations*, arXiv:2604.22165v1, publicly submitted 24 April 2026; https://arxiv.org/html/2604.22165v1.

[2] D. B. Horoshko, S. De Bièvre, M. I. Kolobov and G. Patera, *Entanglement of quantum circular states of light*, arXiv:1602.07852v1, 25 February 2016, Eq. (9) and Sec. III–IV; https://arxiv.org/pdf/1602.07852.

[3] S. Luo, S. Tang and Y. Zhang, *Optimal circular states*, *Journal of Physics A* **57** (2024), 465301, DOI:10.1088/1751-8121/ad8792.

[4] J. Janszky, P. Domokos and P. Adam, *Coherent states on a circle and quantum interference*, *Physical Review A* **48** (1993), 2213–2219, DOI:10.1103/PhysRevA.48.2213.
