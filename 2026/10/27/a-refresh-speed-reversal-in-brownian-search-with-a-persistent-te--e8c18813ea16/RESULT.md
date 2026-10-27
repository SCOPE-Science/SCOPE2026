# A refresh-speed reversal in Brownian search with a persistent telegraph reset rate

## Finding

A Brownian searcher whose Poisson resetting intensity fluctuates between two positive values can be **slower** than a constant-intensity searcher when environmental switching is slow, yet **faster** when switching is sufficiently rapid. This is an exact first-passage distinction at fixed mean intensity, not a statement about stationary spatial localization.

Fix \(D,a,m>0\), \(0<\delta<m\), and let \(\nu>0\) be the switching rate. Define
\[
 f(r)=\frac{\exp(a\sqrt{r/D})-1}{r},\qquad
 z=a\sqrt{m/D},\qquad
 f'(m)=\frac{e^z(z/2-1)+1}{m^2}.
\]
Let \(H_\nu\) be the mean first-passage time defined below, and let \(H_{\mathrm{const}}=f(m)\) be the benchmark with nonfluctuating rate \(m\). Then
\[
 \lim_{\nu\downarrow0}H_\nu
 =\frac{f(m-\delta)+f(m+\delta)}2>f(m),
\]
and
\[
 H_\nu=f(m)-\frac{\delta^2}{2\nu}f'(m)+O(\nu^{-2})
 \quad(\nu\to\infty).
\]
The \(O(\nu^{-2})\) remainder is for fixed \(D,a,m,\delta\).

There is exactly one positive number \(z_*\) solving \(e^{z_*}(z_*-2)+2=0\), numerically \(z_*=1.593624260040\ldots\). Whenever
\[
 m>\frac{D z_*^2}{a^2},
\]
**there exist finite switching rates** \(\nu_{\mathrm{slow}},\nu_{\mathrm{fast}}>0\) with
\[
 H_{\nu_{\mathrm{slow}}}>H_{\mathrm{const}}
 \quad\text{and}\quad
 H_{\nu_{\mathrm{fast}}}<H_{\mathrm{const}}.
\]
By continuity there is at least one intermediate crossing. No uniqueness of the crossing is asserted. At \(m<D z_*^2/a^2\), the fast-switching correction has the opposite sign, so sufficiently rapid intensity fluctuations also worsen mean search time. The critical case \(m=D z_*^2/a^2\) requires a higher-order expansion and is not classified here.

An exact finite-switching formula, suitable for any positive parameters in the stated range, is
\[
 \boxed{\quad
 H_\nu=\frac12\mathbf1^{\mathsf T}(I-E_\nu)
 (Q_\nu+R E_\nu)^{-1}\mathbf1,\quad
 E_\nu=\exp\bigl[-a(A_\nu/D)^{1/2}\bigr],\quad A_\nu=Q_\nu+R,
 \quad}
\]
where \(\mathbf1=(1,1)^{\mathsf T}\),
\[
 R=\operatorname{diag}(m-\delta,m+\delta),\qquad
 Q_\nu=\nu\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The square root is the positive-definite matrix square root. The matrix being inverted is nonsingular for these physical parameters.

## Assumptions and scope

Let \(X_t\) follow \(dX_t=\sqrt{2D}\,dB_t\) on the positive half-line until absorption at \(0\). Initially \(X_0=a>0\). A symmetric two-state continuous-time Markov environment \(J_t\in\{-,+\}\) changes state at rate \(\nu\), independently of Brownian motion. Conditional on \(J_t=-\), the searcher is reset to \(a\) at instantaneous rate \(m-\delta\); conditional on \(J_t=+\), its reset rate is \(m+\delta\). The environment is **not reset** when \(X_t\) returns to \(a\). Set \(\tau=\inf\{t\ge0:X_t=0\}\). The initial environment has its stationary law, \(\Pr(J_0=-)=\Pr(J_0=+)=1/2\), and \(H_\nu=\mathbb E[\tau]\).

The comparator uses the same Brownian diffusion and reset position, but a constant reset intensity \(m\). All reset rates are strictly positive. The theorem concerns the initial environment averaged at stationarity, not any claim about a reset of that environment or a renewal of the entire joint process.

## Proof

**1. Exact backward boundary problem.** Let \(T_-(x),T_+(x)\) be conditional expected absorption times given position \(x>0\) and environment. Write \(T(x)=(T_-(x),T_+(x))^{\mathsf T}\). Dynkin's formula gives
\[
 D T''(x)-(Q_\nu+R)T(x)
 =-\mathbf1-R T(a),\qquad T(0)=0.
\]
For \(\nu\ge0\), \(A_\nu=Q_\nu+R\) is symmetric positive definite. Put \(V=A_\nu^{-1}(\mathbf1+R T(a))\). The bounded solution is
\[
 T(x)=\bigl(I-e^{-x(A_\nu/D)^{1/2}}\bigr)V.
\]
At the reset point \(T(a)=(I-E_\nu)V\); substitution into \(A_\nu V=\mathbf1+R T(a)\) yields
\[
 (Q_\nu+R E_\nu)V=\mathbf1.
\]
This proves the displayed exact formula. There is also a renewal-kernel derivation **without assuming that resets renew the environment**. For Brownian motion started at \(a\), the no-absorption survival function is \(S_B(t)=\operatorname{erf}[a/\sqrt{4Dt}]\). Define \(L=\int_0^\infty S_B(t)e^{-A_\nu t}\,dt=A_\nu^{-1}(I-E_\nu)\). The expected duration of one reset-or-absorption attempt, conditional on its starting environment, is \(b=L\mathbf1\). Its environment-to-environment reset transition matrix is \(K=LR\); the factor \(R\) **must occur on the right**, since it is the reset intensity in the ending environment. Hence \(T(a)=b+KT(a)\), so \(T(a)=(I-K)^{-1}b\). Because every starting environmental state has a uniformly positive probability of Brownian absorption before the next reset, \(K\) is strictly substochastic and has spectral radius below one. This yields finite mean first passage and proves invertibility. Finally, commuting \(A_\nu\) with \(E_\nu\) shows that this renewal answer agrees with \((I-E_\nu)(Q_\nu+R E_\nu)^{-1}\mathbf1\). In particular, the nonlocal reset term uses \(T_i(a)\) in the *same environment state* \(i\), since only position is reset.

**2. Slow environmental switching.** At \(\nu=0\), \(A_0=R\) and \(E_0\) is diagonal with entries \(e^{-a\sqrt{(m\mp\delta)/D}}\). Hence
\[
 T_\pm(a)=f(m\pm\delta),\quad
 H_0=\tfrac12\bigl[f(m-\delta)+f(m+\delta)\bigr].
\]
Because the relevant matrices depend continuously on \(\nu\) and the inverse exists at zero, \(H_\nu\to H_0\). For \(r>0\), writing \(y=a\sqrt{r/D}>0\), direct differentiation shows
\[
 f''(r)=\frac{e^y(y^2-5y+8)-8}{4r^3}>0.
\]
The numerator vanishes at \(y=0\) and has positive derivative \(e^y(y^2-3y+3)>0\) on \([0,\infty)\). Strict midpoint convexity therefore makes \(H_0>f(m)\), proving the slow-switch penalty for every nontrivial modulation amplitude.

**3. Rapid environmental switching.** Use the orthonormal basis of the symmetric and antisymmetric environment vectors. In this basis,
\[
 Q_\nu=\operatorname{diag}(0,2\nu),\quad
 R=\begin{pmatrix}m&\delta\\\delta&m\end{pmatrix},\quad
 A_\nu=\begin{pmatrix}m&\delta\\\delta&m+2\nu\end{pmatrix}.
\]
The smaller eigenvalue is \(m+\nu-\sqrt{\nu^2+\delta^2}=m-\delta^2/(2\nu)+O(\nu^{-3})\); the larger one is \(m+2\nu+O(\nu^{-1})\). Its spectral projector has off-diagonal entry \(-\delta/(2\nu)+O(\nu^{-3})\) in the low-eigenvalue sector and diagonal entries \(1+O(\nu^{-2})\), \(O(\nu^{-2})\). The high-mode exponential is smaller than any inverse power of \(\nu\). Thus, with \(z=a\sqrt{m/D}\), in this basis
\[
 E_{00}=e^{-z}\left(1+\frac{\delta^2 z}{4m\nu}\right)+O(\nu^{-2}),\quad
 E_{01}=-\frac{\delta e^{-z}}{2\nu}+O(\nu^{-2}),\quad
 E_{11}=O(\nu^{-2}).
\]
Set \(B=Q_\nu+R E_\nu\). Its components have expansions
\[
 B_{00}=e^{-z}\left[m+\frac{\delta^2(z-2)}{4\nu}\right]+O(\nu^{-2}),\quad
 B_{01}=O(\nu^{-1}),\quad B_{10}=\delta e^{-z}+O(\nu^{-1}),\quad
 B_{11}=2\nu+O(\nu^{-1}).
\]
Solve \(BV=(\sqrt2,0)^{\mathsf T}\) by Schur complement. Since \(B_{01}B_{10}/B_{11}=O(\nu^{-2})\), the symmetric component of \(V\) is
\[
 V_0=\frac{\sqrt2 e^z}{m}\left[1-\frac{\delta^2(z-2)}{4m\nu}\right]+O(\nu^{-2}),
\]
and its antisymmetric component is \(O(\nu^{-1})\). Consequently
\[
 \begin{aligned}
 H_\nu&=\frac1{\sqrt2}[(I-E)V]_0\\
 &=\frac{e^z-1}{m}-\frac{\delta^2}{4\nu m^2}
 \bigl[e^z(z-2)+2\bigr]+O(\nu^{-2})
 =f(m)-\frac{\delta^2}{2\nu}f'(m)+O(\nu^{-2}).
 \end{aligned}
\]
The bounds follow from a finite-dimensional spectral expansion at fixed positive \(m,D,a,\delta\).

**4. Sharp condition for a reversal.** The sign of \(f'(m)\) is that of \(g(z)=e^z(z-2)+2\). Here \(g(0)=0\) and \(g'(z)=e^z(z-1)\): it first decreases and then increases, and has exactly one positive zero \(z_*>1\). Therefore \(m>D z_*^2/a^2\) gives \(f'(m)>0\), so the fast-switching expansion is strictly below \(f(m)\) for all sufficiently large finite \(\nu\). By the strict slow-switch inequality, sufficiently small finite \(\nu\) give the opposite strict comparison. Continuity supplies at least one switching-speed crossing. The claims hold for every \(0<\delta<m\); no perturbative small-amplitude assumption is imposed.

## Verification

Run `python check.py` using NumPy and SciPy. The script directly diagonalizes the \(2\times2\) positive matrix to evaluate the exact expression, compares its zero-switch limit and rapid-switch coefficient, checks the strict slow penalty, checks constant-rate invariance, and independently discretizes the absorbing/reflected diffusion generator as a sparse linear system. In the tested \(D=a=1\), \(m=5\), \(\delta=2\) example, a finite equality occurs numerically near \(\nu=4.4682413\). These computations test finite instances and the derived formula; they do not certify the infinite-asymptotic proof independently.

## Relationship to prior work

Arutkin and Reuveni, *Diffusion with doubly stochastic resetting* (arXiv:2509.25365v1, 2025), introduce resetting under an intensity that evolves independently of spatial resets and derive stationary spatial laws, including Poisson-refreshed stochastic rates. Their Section 5 explicitly identifies first-passage statistics as a direction for extension. The **stationary propagator, rate-memory principle and physical motivation** belong to that work; the finite-switching first-passage comparison and speed-dependent sign reversal are not stated in its accessible main text.

Barman, Nandi and Das, *Optimizing search processes in systems with state toggling* (arXiv:2410.06933; Phys. Rev. E 111, 024142, 2025), provide exact first-passage equations and resetting-advantage phase diagrams when a **constant** reset rate is combined with an environment-dependent drift. In the present setting the drift is identical in both environmental states but the **reset intensity** itself switches, and a position reset leaves the environment unchanged. Their general backward-equation methods are relevant ingredients; their stated current parameters and inequalities do not imply the comparison proved here.

The classical constant-rate Brownian search formula \(f(m)\) and its optimal-rate threshold are established foundational facts. The numerical value of \(z_*\), standing alone, is not a new optimal-rate discovery. The analyzed contribution is the contrasting strict inequalities at fixed mean intensity and arbitrary nonzero modulation amplitude, together with the explicit fast-switch correction in this nonrenewal environment.

## Limitations

Only symmetric two-state Markov modulation and stationary initial environmental averaging are treated. The analysis fixes positive \(D,a,m\) and nonzero \(\delta<m\). No universal inequality is claimed at intermediate switching speeds, no uniqueness is claimed for the crossing, and the exact threshold case \(f'(m)=0\) is not decided. The result does not concern optimal tuning of \(m\), asymmetric environmental switching, a resetting environment, or non-Brownian transport. Novelty is assessed against the sources inspected, not independently certified; broader matrix-resolvent or Markov-modulated-search results could subsume parts of the theorem.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first public version 29 September 2025), https://arxiv.org/abs/2509.25365.
2. H. K. Barman, A. Nandi and D. Das, *Optimizing search processes in systems with state toggling: exact condition delimiting the efficacy of stochastic resetting strategy*, arXiv:2410.06933 (2024); *Physical Review E* **111**, 024142 (2025), https://arxiv.org/abs/2410.06933.
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, *Physical Review Letters* **106**, 160601 (2011), https://doi.org/10.1103/PhysRevLett.106.160601.
4. P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020), https://arxiv.org/abs/2009.02739.
