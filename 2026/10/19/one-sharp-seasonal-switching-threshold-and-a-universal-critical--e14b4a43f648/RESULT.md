# One sharp seasonal switching threshold and a universal critical extinction profile in two-patch cross-recruitment

## Finding
A two-patch ecological population with seasonally reversed directional cross-recruitment and shared density limitation has an **exact, strictly monotone persistence threshold in the length of the season**. Even when each frozen ecological environment has a negative spectral bound, sufficiently fast seasonal switching can sustain a unique globally attracting positive periodic population. At the single borderline season length, all nonzero populations instead become extinct at rate \(t^{-1}\), with an explicit universal phase-dependent limit independent of initial abundance and composition.

Write \(C=\cosh h>1\) and set
\[
\Lambda(T)=-d+\frac{2}{T}\operatorname{arsinh}\!\left(C\sinh(rT/2)\right).
\]
For all \(T,r,d,h,\kappa>0\), extinction is exponential when \(\Lambda(T)<0\), the unique strictly positive \(T\)-periodic solution attracts every nonzero nonnegative initial state when \(\Lambda(T)>0\), and extinction is algebraic with the exact universal profile below when \(\Lambda(T)=0\). Furthermore \(\Lambda(T)\) strictly decreases as \(T\) increases, from \(-d+r\cosh h\) as \(T\downarrow0\) to \(-d+r\) as \(T\to\infty\). Thus a unique finite seasonal threshold \(T_*\) exists **if and only if** \(r<d<r\cosh h\), defined exactly by
\[
\sinh(dT_*/2)=\cosh h\,\sinh(rT_*/2).
\]
At the marginal cases \(d\le r\) every finite-period model persists, while at \(d\ge r\cosh h\) every finite-period model is exponentially extinct.

## Assumptions and scope
Fix strictly positive \(d,r,h,\kappa,T\). With \(u=(u_1,u_2)^{\mathsf T}\) and \(N=u_1+u_2\), consider the continuous, piecewise smooth ODE
\[
\frac{du}{dt}=A(t)u-\kappa Nu,
\quad
A_+=\begin{pmatrix}-d&r e^h\\r e^{-h}&-d\end{pmatrix},\qquad
A_-=\begin{pmatrix}-d&r e^{-h}\\r e^h&-d\end{pmatrix}.
\]
In every period \(T\), use \(A_+\) for its first half and \(A_-\) for its second; repeat for all positive time. The population begins at \(u(0)\in[0,\infty)^2\setminus\{0\}\). Its biological components represent abundance in two patches; the off-diagonal terms represent cross-patch recruitment and the shared \(-\kappa N\) term a common density-dependent brake. This is **not** the general Lotka–Volterra interaction model, nor a claim about arbitrary seasonal durations or arbitrary nonlinear density dependence.

Let \(\Phi(t)\) denote the fundamental matrix for \(X'=A(t)X\) with \(\Phi(0)=I\), and \(P=\Phi(T)\). Its positive Perron eigenpair is \(Pv=\mu v\), with \(v_1+v_2=1\). Write
\[
I_s(v)=\int_0^s\mathbf 1^{\mathsf T}\Phi(\tau)v\,d\tau,\quad I=I_T(v)>0.
\]
Then \(\mu=\exp(T\Lambda(T))\). In the persistent regime the globally attracting periodic solution, for each season-phase \(0\le s<T\), is
\[
u_*(s)=\frac{(\mu-1)\Phi(s)v}{\kappa\,[I+(\mu-1)I_s(v)]}.
\]
At the critical regime \(\mu=1\), every nonzero nonnegative initial state satisfies the **universal** limit, uniformly for \(0\le s<T\),
\[
\lim_{n\to\infty}(nT+s)u(nT+s)
=\frac{T\Phi(s)v}{\kappa I}.
\]
Both frozen matrices have eigenvalues \(-d\pm r\). The explicit example \(r=1\), \(d=9/8\), \(h=\log2\) has individually stable frozen matrices but positive \(\Lambda(2)=0.052444418600\ldots\), negative \(\Lambda(5)=-0.036709836247\ldots\), and \(T_*=3.376610599770\ldots\).

## Proof
**1. Positivity, exact density transform, and the monodromy.** Each \(A_\pm\) is irreducible Metzler, so its exponential is strictly positive for positive time. Define \(X(t)=\Phi(t)u(0)\) and \(H(t)=1+\kappa\int_0^t\mathbf 1^{\mathsf T}X(\tau)\,d\tau\). Direct differentiation gives \(u(t)=X(t)/H(t)\), which is the unique global nonnegative solution. In particular, \(u(t)\) is strictly positive for every \(t>0\).

Set \(J_\pm=(A_\pm+dI)/r\); then \(J_\pm^2=I\). For \(s=rT/2\),
\[
P=e^{-dT}(\cosh s\,I+\sinh s\,J_-)
(\cosh s\,I+\sinh s\,J_+).
\]
Thus \(\det(e^{dT}P)=1\), and
\[
\tfrac12\operatorname{tr}(e^{dT}P)
=1+2\cosh^2(h)\sinh^2(s)
=\cosh\!\left(2\operatorname{arsinh}(\cosh h\sinh s)\right).
\]
The two positive eigenvalues of \(P\) are \(\exp[-dT\pm2\operatorname{arsinh}(C\sinh s)]\); since \(P\) is strictly positive, the plus sign is its simple Perron eigenvalue \(\mu\).

**2. Strict monotonicity and the unique threshold.** Let \(g(s)=\operatorname{arsinh}(C\sinh s)\), with \(C>1\). Direct differentiation yields
\[
g'(s)=\frac{C\cosh s}{\sqrt{1+C^2\sinh^2s}},\qquad
 g''(s)=\frac{C(1-C^2)\sinh s}{(1+C^2\sinh^2s)^{3/2}}<0\quad(s>0).
\]
Since \(g(0)=0\), strict concavity makes \(g(s)/s\) strictly decreasing, with limits \(C\) at zero and \(1\) at infinity. Accordingly \(\Lambda(T)=-d+r\,g(rT/2)/(rT/2)\) has the stated limits and strict decrease. The sign classification and uniqueness of the positive solution of the displayed hyperbolic-sine equation follow directly. The equality cases \(d=r\) and \(d=rC\) are excluded from the finite critical period because strict concavity places the ratio strictly between \(1\) and \(C\) for finite \(T\).

**3. Nonlinear extinction and persistence.** Let \(w>0\) be the left Perron eigenvector normalized by \(w^{\mathsf T}v=1\), and let \(\nu\) be the second eigenvalue. By positivity and the explicit spectrum, \(0<\nu<\mu\). For \(0\le s<T\) and integer \(n\ge0\), \(X(nT+s)=\Phi(s)P^n u(0)\); writing \(c=w^{\mathsf T}u(0)>0\), we have \(P^n u(0)=c\mu^n v+O(\nu^n)\).

If \(\mu<1\), this implies uniform exponential decay of \(u\), since \(H(t)\ge1\). If \(\mu>1\), integrate the exact decomposition over complete and partial periods to obtain, uniformly in phase,
\[
H(nT+s)=\kappa c\mu^n\left(\frac{I}{\mu-1}+I_s(v)\right)+o(\mu^n).
\]
Dividing \(X\) by \(H\) yields the claimed positive periodic limit. Since the period map \(u\mapsto Pu/(1+\kappa\int_0^T\mathbf1^{\mathsf T}\Phi(\tau)u\,d\tau)\) has exactly one strictly positive fixed point \((\mu-1)v/(\kappa I)\), this establishes uniqueness as well as attraction.

If \(\mu=1\), spectral decomposition instead yields \(P^n u(0)=cv+O(\nu^n)\) and \(H(nT+s)=\kappa nc I+O(1)\). Hence
\[
(nT+s)u(nT+s)\to \frac{T\Phi(s)v}{\kappa I}
\]
uniformly in \(s\), as asserted. The limit is positive for every phase, and consequently exponential extinction is impossible at criticality. This also covers initial states on the boundary axes.

## Verification
Run `python3 verify.py` from this directory (Python standard library only). The checker executes 135 matrix/monodromy parameter combinations plus five nonlinear/limit cases: 140 checks total. It independently compares the explicit eigenvalue with direct \(2\times2\) matrix products, verifies eigenvectors/determinants, compares Runge–Kutta integration with the exact nonlinear period map, tests attraction and the \(1/n\) threshold normalization. It reports the numerical example and the unique threshold. These are **finite numerical consistency checks**, not a proof of the limiting theorems. The proof is the exact reduction above.

## Relationship to prior work
Nag Chowdhury (arXiv:2608.14081, first posted August 14, 2026) studies smooth periodic environmental modulation and ecological network stability, including a commuting linearized limit. The present result treats a distinct two-patch piecewise constant, noncommuting regime and proves a complete nonlinear persistence/extinction threshold and exact critical profile. Lagasquie (arXiv:1612.01861) shows that switching among planar stable linear systems can cause instability, but his randomly switched matrices have opposite-signed off-diagonal entries and his deterministic illustrations involve other stability bands, not this cooperative population threshold or the nonlinear critical limit. Zheng and coauthors (2023) treat cyclic stabilization in positive switched systems, especially when constituent modes are unstable, rather than this extinction-to-persistence transition with individually stable frozen modes. General results on positive/switched systems may cover parts of the spectral or global dynamics abstractly; novelty is **not** asserted for switching-induced instability alone, nor for the elementary shared-density integrating factor in isolation. The focused contribution is their exact combination for the ecological seasonal model.

## Limitations
The two seasonal durations are equal; each season has constant coefficients; both patches share exactly the same quadratic crowding coefficient; there is no stochastic demographic noise, migration delay, unequal damping, or inference claim. The globally attracting orbit exists only when the **principal** Floquet multiplier exceeds one. The threshold profile concerns absolute abundances; no general statement about arbitrary competition matrices or ecological field data follows. Prior literature comparison is not an exhaustive mathematical novelty certificate. In particular, the complete text of a relevant older planar switching study and of a 2026 general switched-systems preprint was not available for full examination; their abstracts and visible scope do not demonstrate subsumption of this exact combined nonlinear result.

## References
1. S. Nag Chowdhury, *Periodic Environmental Forcing Shapes the Stability of Complex Ecological Networks*, arXiv:2608.14081v1 (August 14, 2026), https://arxiv.org/abs/2608.14081.
2. G. Lagasquie, *A note on simple randomly switched linear systems*, arXiv:1612.01861v1 (2016), https://arxiv.org/abs/1612.01861.
3. Y. Zheng and collaborators, *A combined cyclic stabilizing switching law for continuous time positive switched systems*, IET Control Theory & Applications (2023), DOI: 10.1049/cth2.12459.
4. U. Boscain, *Stability of Planar Switched Systems: The Linear Single Input Case*, SIAM Journal on Control and Optimization (2002), DOI: 10.1137/S0363012900382837 (full text not examined).
5. I. O. Shevchenko and X. Liu, *Stability and Bifurcations of Planar Switched Linear and Homogeneous Systems*, arXiv:2607.12189 (2026; full text not examined).
