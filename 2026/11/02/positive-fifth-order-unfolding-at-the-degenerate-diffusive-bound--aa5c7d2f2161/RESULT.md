# Positive fifth-order unfolding at the degenerate diffusive-boundary Hopf point

## Finding

Consider the half-line diffusion equation with dynamic boundary kinetics
\[
 u_t=u_{xx},\quad x>0,\qquad a(t)=u(t,0),\qquad
 \dot a=-\alpha a+\beta a^2+\gamma a^3+(\mu+\sqrt{2\alpha})(-u_x(t,0)),
\]
with \(\alpha>0\), \(\beta\in\mathbb R\setminus\{0\}\), and no bulk degradation. At the cubic Hopf-degeneracy threshold
\[
 \gamma=\gamma_c=\frac{\beta^2}{\alpha}\left(\frac{4\sqrt2}{9}-\frac23\right),
\]
the smooth small-amplitude periodic branch of Pelz–Scheel, parameterized by the real first Fourier harmonic \(a(t)=r\cos(\omega t)+O(r^2)\), satisfies
\[
 \boxed{\displaystyle \mu(r)=K\frac{\beta^4}{\alpha^{7/2}}r^4+O(r^6),\qquad
 0.70584603791928416421<K<0.70584603791928416422.}
\]
The coefficient \(K\) is specified *exactly* by the finite algebraic Fourier recursion in the proof. In particular the degenerate critical branch bends to \(\mu>0\), with the fourth-root onset
\[
 |r|\sim\left(\frac{\mu\alpha^{7/2}}{K\beta^4}\right)^{1/4}\quad (\mu\downarrow0).
\]
For normalized parameters \(\alpha=\beta=1\), the frequency has the further verified expansion
\[
 \omega(r)=1-1.13807118745769834960\,r^2-0.75482240260628012349\,r^4+O(r^6).
\]
This establishes the leading finite-amplitude parameter law at the cubic criticality. No assertion about orbital stability of these degenerate cycles is made.

## Assumptions and scope

The equation is the \(\sigma=0\) case of the cubic dynamic-boundary model in Pelz and Scheel (2026), Section 3, equation (3.1). We use the branch existence and smoothness (evenness of \(\mu\) and \(\omega\) in \(r\)) proved in their Theorem 1.4 and the identification of the cubic degeneracy from their Corollary 3.3. The branch normalization fixes the first harmonic exactly to \(r\cos s\), with phase \(s=\omega t\) and all higher amplitude corrections having zero first-harmonic projection. The far-field constant mode is allowed, as required by the source's half-line setting. The conclusions concern only the local branch as \(r\to0\); they do not assert uniqueness of arbitrary large-amplitude cycles.

## Proof

**1. Reduction and scaling.** With \(\tau=\alpha t\), \(\xi=\sqrt\alpha\,x\), and \(v=(\beta/\alpha)u\), the system takes the same form with \(\alpha=\beta=1\), effective cubic \(g=\gamma\alpha/\beta^2\), and effective unfolding \(m=\mu/\sqrt\alpha\). The normalized first-harmonic amplitude is \(R=(\beta/\alpha)r\), possibly signed. Hence it suffices to prove \(m(R)=KR^4+O(R^6)\) at \(g=4\sqrt2/9-2/3\).

**2. Fourier equations.** For a \(2\pi\)-periodic boundary trace \(v(s;R)\), the decaying positive and negative Fourier modes of the bulk heat equation give the Dirichlet-to-Neumann multiplier \(q_j(\omega)=\sqrt{ij\omega}\) (principal square root); the zero mode has multiplier zero. Define
\[
 L_j(\omega,m)=1+ij\omega-(\sqrt2+m)\sqrt{ij\omega},\quad
 \Lambda_j=L_j(1,0),\quad
 A_j=-\sqrt{ij},\quad B_j=ij-\frac{\sqrt2}2\sqrt{ij}.
\]
The periodic equation is \(L_j(\omega,m)[v]_j=[v^2+gv^3]_j\). Expand
\[
 v(s;R)=\sum_{n=1}^4R^nV_n(s)+O(R^5),\quad
 m(R)=m_2R^2+m_4R^4+O(R^6),\quad
 \omega(R)=1+w_2R^2+w_4R^4+O(R^6),
\]
where \([V_1]_{\pm1}=1/2\), all other \([V_1]_j=0\), and \([V_n]_{\pm1}=0\) for \(n\ge2\). Set \(F_n=[(\sum_{k<n}R^kV_k)^2+g(\sum_{k<n}R^kV_k)^3]_{R^n}\), with the extraction taken coefficientwise in Fourier modes. Equivalently, convolution only involves lower-order known coefficients.

At order two, \([V_2]_j=[F_2]_j/\Lambda_j\), for \(j=0,\pm2\). At order three, first-harmonic solvability is
\[
 \frac12(A_1m_2+B_1w_2)=[F_3]_1.
\]
The explicitly published third-order result gives
\[
 m_2=0,\qquad w_2=-\left(\frac76+\frac34g\right)=-1.13807118745769834960\ldots,
\]
when \(g=4\sqrt2/9-2/3\). The remaining third-order modes satisfy \([V_3]_{\pm3}=[F_3]_{\pm3}/\Lambda_{\pm3}\).

At order four, for \(j=0,\pm2,\pm4\),
\[
 [V_4]_j=\frac{[F_4]_j-B_jw_2[V_2]_j}{\Lambda_j}.
\]
At order five, the resonant equation is
\[
 \frac12(A_1m_4+B_1w_4)+\frac12D_1=[F_5]_1,
 \qquad D_1=\frac{\sqrt2\sqrt i}{8}w_2^2.
\]
Here the extra \(D_1\) term comes from the quadratic Taylor term in \(\sqrt\omega\): omitting it would change the fourth-order coefficient. The unique real solution \((m_4,w_4)\) is obtained by taking real and imaginary parts. This is a **finite exact algebraic specification** of \(K=m_4\) using only rational operations and square roots of small integers. The determinant \(\mathrm{Re}(A_1)\mathrm{Im}(B_1)-\mathrm{Im}(A_1)\mathrm{Re}(B_1)\) is nonzero, so the solution is well defined.

**3. Rigorous coefficient sign.** The standalone script `verify_quintic.py` evaluates exactly the recursions above by outward-rounded fixed-point *integer* interval arithmetic, bounding \(\sqrt2\) and \(\sqrt6\) using integer square-root inequalities and performing every division with directed rounding. It confirms
\[
 \frac{70584603791928416421}{10^{20}}<m_4<\frac{70584603791928416422}{10^{20}}.
\]
All other Fourier factors up to order five are rational combinations of these radicals. Thus \(m_4>0\) is a rigorous finite inequality, not a conjecture inferred from floating-point experiments.

**4. Consequences.** Smooth even dependence of the established branch gives \(m(R)=KR^4+O(R^6)\). The strict positive coefficient implies \(m(R)>0\) for all sufficiently small nonzero \(R\), and inversion of the leading law yields the fourth-root amplitude asymptotic. Undoing the scaling in step 1 proves the stated \(\alpha,\beta\) formula. The normalized \(w_4\) from the same exact order-five solvability equation is contained in the verification record.

## Verification

Run `python3 verify_quintic.py` with the Python 3 standard library. The script constructs complex Fourier coefficients through order four and the order-five resonant right-hand side, using integer-enclosed radical intervals and outward integer operations. It checks the published third-order coefficient and verifies the strict rational bounds on \(K\). The expected terminal line is `EXACT_OUTWARD_INTERVAL_QUINTIC_SIGN_PASS`. In addition, a separate high-precision Fourier computation gave \(K\approx0.70584603791928416421526456\) and \(w_4\approx-0.75482240260628012348875401\), consistent with the interval certificate. These numerical values are supplementary; the sign follows from the exact interval calculation and the branch expansion from analysis.

## Relationship to prior work

Pelz and Scheel (2026), Theorem 1.4, establishes the smooth local periodic branch despite essential spectrum; Corollary 3.3 and Remark 3.4 compute its quadratic unfolding \(m_2\) and the explicit cubic-degeneracy threshold. Their stability theorem classifies the nondegenerate regimes \(m_2>0\) and \(m_2<0\); the equality case does not follow from either strict inequality. The fourth-order coefficient and fourth-root emergence at equality are not stated there. The broader generalized-Hopf/Bautin framework motivates this codimension-two question, but does not determine the nonlocal square-root Dirichlet-to-Neumann coefficient for this particular model. A later Pelz paper (arXiv:2608.08537) addresses two boundaries coupled through a diffusion field, with a different configuration; its abstract does not establish this one-boundary coefficient. No priority claim is made beyond the examined literature.

## Limitations

This theorem uses \(\sigma=0\), \(\beta\ne0\), the exact cubic degeneracy, and the specific half-line geometry. It determines the direction and amplitude scaling of the local periodic branch, not its nonlinear or spectral stability at the degenerate point. The source establishes the existence and smoothness of the branch; those analytic foundations are invoked rather than reproved here. A historical source with an equivalent explicit fifth-order coefficient might alter the originality assessment. The verification script certifies the finite algebraic sign only; it does not independently certify the infinite-dimensional branch-existence theorem.

## References

1. Merlin Pelz and Arnd Scheel, *Oscillations in a scalar differential equation coupled to a diffusive field*, arXiv:2604.01135v1, first posted 2026-04-01, especially Theorem 1.4, equation (3.1), Corollary 3.3, and Theorem 4.1. https://arxiv.org/html/2604.01135v1
2. Merlin Pelz, *Dynamical behavior of diffusively coupled scalar differential equations as Wentzell boundary conditions*, arXiv:2608.08537v1, first posted 2026-08-09. https://arxiv.org/abs/2608.08537
