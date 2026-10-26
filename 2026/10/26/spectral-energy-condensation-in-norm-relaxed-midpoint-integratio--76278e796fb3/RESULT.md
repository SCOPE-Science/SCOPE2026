# Spectral energy condensation in norm-relaxed midpoint integration

## Finding

A single global quadratic-norm relaxation can transfer all numerical modal energy to the **largest initially active oscillator frequency**, even when the underlying oscillators are completely uncoupled and every individual modal norm is exactly conserved by the differential equation. For explicit midpoint followed by a common positive relaxation factor, the transfer is unconditional for every fixed positive base step and has a sharp small-step onset at physical time proportional to \(h^{-3}\).

**Theorem.** Let \(m\ge2\), \(\omega_j>0\), and \(u_j(0)\in\mathbb R^2\) with \(\sum_{j=1}^m\|u_j(0)\|_2^2>0\). Write
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\dot u_j=\omega_jJu_j,\qquad E_{j,n}=\|u_{j,n}\|_2^2.
\]
For arbitrary fixed \(h>0\), take the unrelaxed explicit-midpoint increment
\[
d_{j,n}=h\omega_jJu_{j,n}+\tfrac12h^2\omega_j^2J^2u_{j,n}
\]
and update \(u_{j,n+1}=u_{j,n}+\gamma_n d_{j,n}\), using the **same positive** \(\gamma_n\) in all modes and choosing its nonzero value to enforce \(\sum_jE_{j,n+1}=\sum_jE_{j,n}\). Set the relaxed physical-time increment to \(\gamma_n h\). With \(t_j=h^2\omega_j^2\) and
\[
Q_n=\frac{\sum_j t_j^2E_{j,n}}{\sum_j t_jE_{j,n}},
\]
the parameter and all modal energies satisfy the exact identities
\[
\gamma_n=\frac{1}{1+Q_n/4},\qquad
E_{j,n+1}=E_{j,n}\left(1+\frac{t_j(t_j-Q_n)}{4(1+Q_n/4)^2}\right).\tag{1}
\]
Let \(t_*=\max\{t_j:E_{j,0}>0\}\), \(I_*=\{j:E_{j,0}>0,\ t_j=t_*\}\), and \(E_{\rm tot}=\sum_jE_{j,0}\). Then
\[
\lim_{n\to\infty}E_{j,n}=
\begin{cases}
E_{\rm tot}\,E_{j,0}/\sum_{k\in I_*}E_{k,0},&j\in I_*,\\
0,&j\notin I_*.
\end{cases}\tag{2}
\]
For every initially active lower-frequency mode, the exact asymptotic law is
\[
E_{j,n}=A_j\rho_j^n(1+o(1)),\quad A_j\in(0,\infty),\quad
\rho_j=1-\frac{t_j(t_*-t_j)}{4(1+t_*/4)^2}\in(0,1).\tag{3}
\]
These conclusions hold for all \(h>0\), not merely small steps; an initially zero mode remains zero.

The small-step transfer clock is also exact. With \(\lambda_j=\omega_j^2\) and
\[
\mathcal Q(e)=\frac{\sum_j\lambda_j^2e_j}{\sum_j\lambda_je_j},
\]
let \(\mathcal E(s)\) solve on the energy simplex
\[
\frac{d\mathcal E_j}{ds}=\frac14\lambda_j\bigl(\lambda_j-\mathcal Q(\mathcal E)\bigr)\mathcal E_j,
\qquad\mathcal E_j(0)=E_{j,0}.\tag{4}
\]
Then for every fixed \(S>0\), for sufficiently small \(h>0\),
\[
\max_{0\le nh^4\le S}\bigl|E_{j,n}-\mathcal E_j(nh^4)\bigr|\le C_Sh^2,
\qquad h^3T_n=nh^4\bigl(1+O(h^2)\bigr),\tag{5}
\]
where \(T_n=\sum_{k=0}^{n-1}\gamma_kh\), with the time estimate uniform for \(nh^4\le S\). Thus the nontrivial transfer scale is \(n\asymp h^{-4}\) steps or physical time \(T\asymp h^{-3}\).

For two positive initial modes with \(0<a=\lambda_1<b=\lambda_2\), normalize \(x(s)=\mathcal E_2(s)/E_{\rm tot}\) and \(x_0=E_{2,0}/E_{\rm tot}\in(0,1)\). The limiting transfer is strictly toward the fast mode and uniquely specified by
\[
a\log\frac{x(s)}{x_0}-b\log\frac{1-x(s)}{1-x_0}
=\frac{ab(b-a)}4s.\tag{6}
\]
For \(a=1\), \(b=4\), \(x_0=1/4\), at \(s=1\) it yields \(x(1)=0.5655220123\ldots\), even though the exact differential equation keeps the fast-mode share \(1/4\) at all physical times.

## Assumptions and scope

The baseline step is the standard explicit midpoint Runge–Kutta scheme, evaluated at fixed base step \(h\), followed by exactly one positive scalar relaxation on the **total Euclidean squared norm** \(\eta(u)=\sum_j\|u_j\|_2^2\). The number of modes is finite and their positive frequencies are fixed; exact arithmetic is assumed. The scheme does not separately enforce each conserved modal norm. The nonzero quadratic-norm relaxation root is uniquely defined here because \(\sum_j t_jE_{j,n}>0\) throughout. These are normal-form independent rotations, not interacting oscillators. The relaxed time convention is part of the numerical method and must not be replaced by unrelaxed \(nh\) without stating it.

## Proof

**1. Exact nonzero relaxation root and modal update.** Since \(J^2=-I\) and \(\langle u,Ju\rangle=0\),
\[
\langle u_j,d_j\rangle=-\frac{t_j}{2}E_j,
\qquad \|d_j\|_2^2=t_j(1+t_j/4)E_j.
\]
The total-norm conservation equation is
\[
0=\sum_j\bigl(2\gamma\langle u_j,d_j\rangle+\gamma^2\|d_j\|_2^2\bigr)
=\gamma\left[-\sum_jt_jE_j+\gamma\sum_jt_j(1+t_j/4)E_j\right].
\]
Its unique positive root is \(\gamma=(1+Q/4)^{-1}\), and substitution gives (1). Each numerical mode transforms by \((1-\gamma t_j/2)I+\gamma\sqrt{t_j}J\), whose squared norm multiplier is strictly positive because the second coefficient is positive; initially positive energies never vanish in finite time. Summing (1) confirms conservation using the definition of \(Q\).

**2. Selection of the maximal active frequency.** The scalar \(Q_n\) is a weighted mean of the active \(t_j\), with weights \(t_jE_{j,n}>0\), so it lies in the closed interval between the smallest and largest initially active values. Denote by \(g_j(Q)\) the multiplier in (1). For any active \(t_j<t_*\), direct factorization yields
\[
g_*(Q)-g_j(Q)=\frac{(t_*-t_j)(t_*+t_j-Q)}{4(1+Q/4)^2}>0.\tag{7}
\]
The inequality is uniform on the compact admissible interval because \(t_*+t_j-Q\ge t_j>0\). Also \(g_*(Q)\ge1\), since \(Q\le t_*\). Therefore \(g_j(Q)/g_*(Q)\le\kappa_j<1\), uniformly for every step. Choose one initially active top mode \(k\). Then
\[
\frac{E_{j,n}}{E_{k,n}}
=\frac{E_{j,0}}{E_{k,0}}\prod_{\ell<n}\frac{g_j(Q_\ell)}{g_*(Q_\ell)}
\le\frac{E_{j,0}}{E_{k,0}}\kappa_j^n.
\]
All active top-mode ratios remain unchanged because they have identical multipliers. Fixed total energy now gives (2); it also implies \(Q_n-t_*=O(\kappa^n)\) for some \(\kappa<1\) whenever any lower mode is active (otherwise \(Q_n=t_*\) exactly). Equation (1) at \(Q=t_*\) gives \(\rho_j\). Continuity of \(g_j\) yields \(g_j(Q_n)=\rho_j+O(\kappa^n)\). Since \(0<\rho_j<1\), the convergent positive infinite product \(\prod_{n\ge0}(g_j(Q_n)/\rho_j)\) defines the finite positive constant \(A_j/E_{j,0}\), establishing (3). If no lower mode is present, the discrete step is a common unitary rotation on each active plane.

**3. Critical small-step scaling.** Substituting \(t_j=h^2\lambda_j\) and \(Q_n=h^2\mathcal Q(E_n)\) into (1) gives the *exact* difference equation
\[
E_{j,n+1}-E_{j,n}
=\frac{h^4}{4}\,
\frac{\lambda_j\bigl(\lambda_j-\mathcal Q(E_n)\bigr)E_{j,n}}
{\bigl(1+h^2\mathcal Q(E_n)/4\bigr)^2}.\tag{8}
\]
Because every \(\lambda_j>0\) and total energy is positive and fixed, \(\mathcal Q\) and the right-hand side of (4) are smooth and uniformly Lipschitz on the compact nonnegative total-energy simplex. The right-hand side of (8), divided by \(h^4\), differs uniformly from that of (4) by \(O(h^2)\). Comparing the recurrence with explicit Euler of step \(h^4\) and applying the discrete Grönwall inequality gives the first estimate in (5), including all boundary faces. For every step,
\[
\frac1{1+h^2\lambda_{\max}/4}\le\gamma_n\le1,
\]
so \(T_n/(nh)=1+O(h^2)\) uniformly whenever \(n\ge1\), proving the second relation in (5). For two modes, substituting \(\mathcal E_1=E_{\rm tot}(1-x)\) and \(\mathcal E_2=E_{\rm tot}x\) into (4) gives
\[
\dot x=\frac{ab(b-a)}4\frac{x(1-x)}{a(1-x)+bx}>0.
\]
Separation and integration give (6). In particular the fast-mode energy differs by an order-one amount from the exact invariant at the physical times \(T_{\lfloor s/h^4\rfloor}\) for every fixed \(s>0\) and both modes initially positive.

**4. Long-time discrepancy from the exact dynamics.** In continuous time each \(E_j(t)=E_{j,0}\) exactly. For any initially positive lower-frequency modes their concatenated exact block has fixed norm \((\sum_{j:t_j<t_*}E_{j,0})^{1/2}\), while the numerical counterpart tends to zero by (2). The reverse triangle inequality therefore gives
\[
\liminf_{n\to\infty}
\|u_{\rm num}(T_n)-u_{\rm exact}(T_n)\|_2
\ge \left(\sum_{j:t_j<t_*}E_{j,0}\right)^{1/2}>0.
\]
This is a long-time statement for each fixed \(h\), not a failure of convergence on fixed physical-time intervals.

## Verification

`verify.py` uses Python standard-library exact rational fractions for conservation and factorization identities on multiple steps and frequencies, and independent finite numerical diagnostics for long-time selection, the geometric ratio and the small-step slow-time equation. Run `python3 verify.py` in the same directory. Its expected final line is `VERIFY_OK`. These finite checks do not establish the infinite-time limit or uniform small-step convergence, which follow from the proofs above. No external numerical datasets or third-party dependencies are required.

## Relationship to prior work

The positive global relaxation root and its use to enforce a single inner-product norm are from Ketcheson (2019), not new. Ranocha and Ketcheson (2020, Section 3.4) explicitly noted coupling between two *uncoupled* oscillators when a single scalar enforces total-energy conservation in the classical fourth-order relaxed Runge–Kutta method; generic coupling is therefore not claimed as new. Bleecke and Ranocha (2023, Sections 1 and 4.1.1) discuss the relaxed time convention, step-size control and a single oscillator. Biswas and Ketcheson (2023) develop *multiple*-relaxation methods for enforcing multiple invariants using additional directions, which differ from the single-parameter scheme examined here.

The specific claimed addition is the exact all-step spectral selection theorem (2), sharp lower-mode decay (3), and the nonlinear \(h^{-3}\) physical-time limit (4)–(6) for global-norm-relaxed **explicit midpoint** on any finite collection of independent harmonic modes. These are not inferred merely from the known possibility of coupling and were not located in the inspected sources. This comparison supports a best-knowledge originality assessment, not a proof of worldwide uniqueness.

## Limitations

This concerns one globally shared quadratic-norm relaxation scalar, fixed base step, exact arithmetic, positive finitely many frequencies and the explicit midpoint baseline. It does not claim the same dynamics for higher-order baseline methods, per-mode relaxation, multiparameter invariant preservation, stochastic perturbations, variable base steps, or nonlinear coupled systems. The small-step slow-time result is uniform on bounded rescaled horizons only; (2) and (3) hold at fixed positive base step. Numerical checks are finite; analytic arguments establish all universal assertions. Earlier equivalent analyses under other terminology remain a residual literature risk.

## References

1. David I. Ketcheson, *Relaxation Runge–Kutta Methods: Conservation and Stability for Inner-Product Norms*, arXiv:1905.09847v1 (23 May 2019), Sections 1–3. https://arxiv.org/html/1905.09847v1
2. Hendrik Ranocha and David I. Ketcheson, *Relaxation Runge–Kutta Methods for Hamiltonian Problems*, arXiv:2001.04826v2 (30 June 2020; first posted 14 January 2020), particularly Section 3.4. https://arxiv.org/html/2001.04826v2
3. Abhijit Biswas and David I. Ketcheson, *Multiple-Relaxation Runge Kutta Methods for Conservative Dynamical Systems*, arXiv:2302.05235v1 (10 February 2023), Sections 1–4. https://arxiv.org/html/2302.05235v1
4. Sebastian Bleecke and Hendrik Ranocha, *Step size control for explicit relaxation Runge-Kutta methods preserving invariants*, arXiv:2311.14050v1 (23 November 2023), Sections 1, 2 and 4.1.1. https://arxiv.org/html/2311.14050v1
