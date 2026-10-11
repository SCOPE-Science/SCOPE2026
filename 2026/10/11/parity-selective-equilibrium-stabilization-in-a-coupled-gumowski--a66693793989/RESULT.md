# Parity-selective equilibrium stabilization in a coupled Gumowski–Mira ring

## Finding

For the nearest-neighbor coupled planar map written in Fatoyinbo and Ghosh [1], **all three explicit spatially homogeneous fixed points** have an exact, necessary-and-sufficient spectral stability criterion on rings of every length \(N\ge3\). Put \(E_s=((s,0),\ldots,(s,0))\) for \(s\in\{-1,0,1\}\), \(c_s=\mu\) for \(s=\pm1\), and \(c_0=2-\mu\). For \(a\ge0\), \(b\ge0\), \(\mu\in\mathbb R\), and \(0\le\varepsilon<1\), let
\[
\delta_N=\begin{cases}0,&N\text{ even},\\1-\cos(\pi/N),&N\text{ odd}.\end{cases}
\]
Then the linearization at \(E_s\) is strictly Schur stable (equivalently, \(E_s\) is a hyperbolic attracting fixed point) **if and only if**
\[
\boxed{\quad \varepsilon>\frac{a}{1+a},\qquad c_s<1,\qquad
(1-\varepsilon)(2+a)(1+c_s)+\varepsilon\delta_N>0.\quad}
\tag{1}
\]
Every such fixed point has a nonempty open basin of exponentially convergent initial conditions. The parameter \(b\) has no effect on this local classification.

In particular, for **even** \(N\), criterion (1) simplifies exactly to \(\varepsilon>a/(1+a)\) and \(-1<c_s<1\). For **odd** \(N\), values \(c_s<-1\) can still yield hyperbolic sinks: putting \(A=(2+a)(-1-c_s)>0\), the additional threshold is exactly
\[
\boxed{\qquad\varepsilon>\frac{A}{A+\delta_N}.\qquad}
\tag{2}
\]
No even ring has this strong-coupling sink, while every odd ring does for a suitable \(\varepsilon<1\). The actual admissible coupling interval has lower endpoint \(\max\{a/(1+a),A/(A+\delta_N)\}\), and hence **exact width**
\[
\min\left\{\frac{1}{1+a},\frac{\delta_N}{A+\delta_N}\right\}
\sim \frac{\pi^2}{2A N^2}\quad(N\to\infty\text{ through odd integers}).
\tag{3}
\]
This is a sharp odd-even finite-size stabilization effect, not merely a sampling artifact.

For the exact source-study band \(\mu\in[-0.6,0.6]\) [1], both \(E_{+1}\) and \(E_{-1}\) have nonempty open attracting basins **at every ring length** whenever \(\varepsilon>1/101\) in its Case A \((a,b)=(0.01,0.05)\), or \(\varepsilon>33/133\) in its Case B \((a,b)=(0.33,0.10)\). Both inequalities intersect the studied coupling range \(\varepsilon\in[0,0.30]\). These basins may coexist with other attractors; no claim about basin volume or predominance is made.

## Assumptions and scope

Indices are taken modulo \(N\), and the state space is \(\mathbb R^{2N}\). The map is precisely the version **displayed** in [1]:
\[
F_\mu(x)=\mu x+\frac{2(1-\mu)x}{1+x^2},
\qquad u_i=(1+a)y_i-ab y_i^3+F_\mu(x_i),
\]
\[
x_i^+=(1-\varepsilon)u_i+\frac{\varepsilon}{2}(x_{i-1}+x_{i+1}),
\qquad y_i^+=-x_i+F_\mu(x_i^+).
\tag{4}
\]
This odd-numerator formula differs from a quadratic-numerator historical Gumowski–Mira variant in [2]. The conclusions refer to (4), not to the alternative rule. We do not assert that the three displayed equilibria are the only equilibria, and do not classify periodic or chaotic attractors.

## Proof

1. **Stationarity and derivative.** Direct substitution gives \(F_\mu(0)=0\) and \(F_\mu(\pm1)=\pm1\), hence each \(E_s\) is fixed. Further,
\[
F'_\mu(x)=\mu+\frac{2(1-\mu)(1-x^2)}{(1+x^2)^2},
\quad F'_\mu(\pm1)=\mu,\quad F'_\mu(0)=2-\mu.
\]
At \(y_i=0\), the derivative of \((1+a)y_i-ab y_i^3\) is \(1+a\); this explains independence from \(b\).

2. **Fourier blocks.** The cyclic-neighbor averaging matrix is real symmetric and has eigenvalues \(\lambda_k=\cos(2\pi k/N)\), \(0\le k<N\). In each complex Fourier mode, the Jacobian of (4) reduces to
\[
M_k=\begin{pmatrix} d_k&B\\c_s d_k-1&c_s B\end{pmatrix},
\quad d_k=(1-\varepsilon)c_s+\varepsilon\lambda_k,
\quad B=(1-\varepsilon)(1+a)>0.
\]
Consequently
\[
\operatorname{tr}(M_k)=(1-\varepsilon)(2+a)c_s+\varepsilon\lambda_k,
\qquad\det M_k=B.
\tag{5}
\]
The block eigenvalues together (with conjugate-paired modes) form the full spectrum of the real \(2N\)-dimensional Jacobian.

3. **Sharp Schur conditions.** A real monic quadratic \(z^2-Tz+B\) has both roots strictly inside the open unit disk if and only if \(1-B>0\), \(1-T+B>0\), and \(1+T+B>0\), given \(B>0\) (the elementary degree-two Jury criterion). The first condition gives \(\varepsilon>a/(1+a)\). Since \(T\) is increasing in \(\lambda_k\), the tight upper-trace inequality occurs at \(\lambda_0=1\), and simplifies to
\[
1-T_0+B=(1-\varepsilon)(2+a)(1-c_s)>0
\quad\Longleftrightarrow\quad c_s<1.
\]
The tight lower-trace inequality occurs at the minimum mode \(\lambda_{\min}\), where \(\lambda_{\min}=-1\) for even \(N\), and \(-\cos(\pi/N)\) for odd \(N\). It becomes
\[
1+T_{\min}+B=(1-\varepsilon)(2+a)(1+c_s)+\varepsilon(1+\lambda_{\min})>0.
\]
By \(1+\lambda_{\min}=\delta_N\), this is exactly the third condition in (1). Each inequality is independently necessary and jointly sufficient, proving (1) including all parameter boundaries.

4. **Parity and sharpness.** When \(N\) is even, \(\delta_N=0\), so \(c_s>-1\) is required. When \(N\) is odd and \(c_s<-1\), the third inequality is \(\varepsilon\delta_N>(1-\varepsilon)A\), equivalently (2). Because \(\delta_N>0\), its threshold is strictly less than 1, and sufficiently strong coupling simultaneously meets the independent determinant condition \(\varepsilon>a/(1+a)\). The true finite-ring coupling window is the intersection of these two strict lower bounds; its length is the minimum in (3). Conversely even rings cannot meet the third inequality. Taylor's formula gives \(\delta_N\sim\pi^2/(2N^2)\) along odd \(N\); for any fixed \(c_s<-1\) and \(a\ge0\), the second threshold eventually dominates, establishing the asymptotic in (3). For example, \(a=1/4\), \(b=1/10\), \(\mu=-2\), \(\varepsilon=9/10\) makes \(E_{\pm1}\) hyperbolically attracting on the three-site ring, whereas on every even ring they have a Fourier eigenvalue outside the unit circle.

5. **Nonlinear conclusion and source regimes.** The map (4) is smooth on \(\mathbb R^{2N}\). A strict Schur derivative at a fixed point implies local exponential attraction by choosing a contracting equivalent norm and using continuity of the derivative. On \(\mu\in[-0.6,0.6]\), \(-1<\mu<1\), so even and odd rings have exactly the same sink condition for \(E_{\pm1}\), namely \(\varepsilon>a/(1+a)\); substituting the two exact values of \(a\) gives \(1/101\) and \(33/133\).

## Verification

The accompanying standalone \(`verify.py`\) uses Python's standard library only. It performs 3,263,634 checks of exact-rational fixed-point identities, complete Fourier-mode traces and determinants, the strict Schur criterion over 41 ring lengths and a parameter grid, explicit odd-even witnesses, and independent central-difference comparisons with the nonlinear \(2N\)-dimensional Jacobian. Run \(`python3 verify.py`\) in the folder containing the extracted files. The computational tests are finite diagnostics; all quantified claims follow from the preceding proof.

## Relationship to prior work

Fatoyinbo and Ghosh [1] specify (4) and numerically study Lyapunov, synchronization, and cluster statistics across two parameter regimes. The present classification concerns **local equilibria**, rather than their dominant numerically observed attractors, and supplies an exact all-parameter criterion absent from their displayed analyses. Ambika and Ambika [2] analyze intermittency and a different two-map coupling, with a different printed local nonlinearity; their fixed-point and synchronization analyses do not directly imply (1). General master-stability and network-spectral approaches, such as [3], supply established tools for Fourier-mode reduction. No novelty is claimed for the elementary Jury test, Fourier diagonalization, or the generic linearization principle. The specific necessary-and-sufficient region (1), exact odd-even boundary (2), and the two original parameter-band consequences are the assessed contributions.

## Limitations

The stability condition is strict and classifies hyperbolic sinks only; on equality surfaces the Jacobian has a unit-modulus root and nonlinear behavior is not determined. Failure of the conditions means only that the fixed point is not a **strictly Schur-stable** sink, and not necessarily that it is nonlinearly unstable at equality. The result neither classifies other equilibria or their basins nor proves global synchronization, uniqueness of attractors, or the size of basin fractions. The parameter \(b\) can affect nonlinear and global dynamics despite its absence from the local eigenvalues at \(E_s\). The older alternative quadratic-numerator map is outside scope. Existing master-stability theory may admit equivalent derivations; mathematical priority beyond the inspected sources is not certified.

## References

[1] H. O. Fatoyinbo and I. Ghosh, *Collective Phase Reorganization and Cluster Synchronization in Networks of Coupled Gumowski–Mira Maps*, arXiv:2607.03686v1 (first posted 2026-07-04), https://arxiv.org/abs/2607.03686. Equations (1)–(7), parameter intervals (8)–(10), and phase diagrams.

[2] G. Ambika and K. Ambika, *Intermittency and Synchronisation in Gumowski-Mira Maps*, arXiv:nlin/0606005v1 (2006), https://arxiv.org/abs/nlin/0606005. Equations and Sections 2, 5.

[3] J. Juang and Y.-H. Liang, *Synchronous Chaos in Coupled Map Lattices with General Connectivity Topology*, SIAM J. Appl. Dyn. Syst. (2008), https://doi.org/10.1137/070705179. General spectral/master-stability context, not the displayed specialization.
