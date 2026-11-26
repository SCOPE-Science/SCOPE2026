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
the smooth small-amplitude periodic branch of Pelz–Scheel, parameterized so that the first harmonic of \(a(t)\) is exactly \(r\cos(\omega t)\), satisfies
\[
 \mu(r)=K\frac{\beta^4}{\alpha^{7/2}}r^4+O(r^6),\qquad
 K=-\frac59+\frac{23\sqrt2}{27}+\frac{5\sqrt6}{216}.
\]
In particular \(0.70584603791928416421<K<0.70584603791928416422\). The branch bends to \(\mu>0\), with the fourth-root onset
\[
 |r|\sim\left(\frac{\mu\alpha^{7/2}}{K\beta^4}\right)^{1/4}\quad (\mu\downarrow0).
\]
For normalized parameters \(\alpha=\beta=1\), write
\[
 \omega(r)=1+w_2r^2+w_4r^4+O(r^6),\qquad
 w_2=-\frac{2+\sqrt2}{3},\qquad
 w_4=\frac{149}{108}-\frac{11\sqrt2}{9}-\frac{7\sqrt3}{54}-\frac{2\sqrt6}{27}.
\]
The respective coefficient approximations are \(w_2\approx-1.13807118745769834960\) and \(w_4\approx-0.75482240260628012349\). No assertion about orbital stability of these degenerate cycles is made.

## Assumptions and scope

The equation is the \(\sigma=0\) case of the cubic dynamic-boundary model in Pelz–Scheel [1], Section 3, equation (3.1). The proof uses their Theorem 1.4 for the smooth local branch, with its hypotheses verified for this model in Lemma 3.1, and their Corollary 3.3 and Remark 3.4 for cubic degeneracy. Phase is chosen so that the first Fourier harmonic is real, and its signed cosine coefficient is the branch coordinate. This coordinate has derivative one with respect to the original amplitude at zero and is therefore a smooth local coordinate. Reversing its sign corresponds to a phase shift by \(\pi\); the parameters \(\mu\) and \(\omega\) are smooth even functions of this coordinate. The bounded zero bulk mode is allowed and corresponds to a far-field constant. The branch claims are local as \(r\to0\).

## Proof

**Scaling.** Set \(\tau=\alpha t\), \(\xi=\sqrt\alpha\,x\), and \(v=(\beta/\alpha)u\). Then the equation takes the same form with \(\alpha=\beta=1\), cubic coefficient \(g=\gamma\alpha/\beta^2\), and unfolding parameter \(m=\mu/\sqrt\alpha\). Its normalized first-harmonic amplitude is \(R=(\beta/\alpha)r\), which may be signed. The frequency below is with respect to normalized time \(\tau\).

**Fourier equations.** With phase variable \(s=\omega\tau\), the normal-flux multiplier for a nonzero Fourier mode \(j\) of the bounded bulk solution is the principal square root \(\sqrt{ij\omega}\); the bounded zero mode is constant with multiplier zero. Thus, for the boundary trace (also denoted by \(v\)),
\[
 L_j(\omega,m)[v]_j=[v^2+gv^3]_j,\qquad
 L_j(\omega,m)=1+ij\omega-(\sqrt2+m)\sqrt{ij\omega}.
\]
Set \(\Lambda_j=L_j(1,0)\), \(A_j=-\sqrt{ij}\), and \(B_j=ij-(\sqrt2/2)\sqrt{ij}\). The only vanishing \(\Lambda_j\) are at \(j=\pm1\): for \(j\ge0\), \(\Lambda_j=1-\sqrt j+i(j-\sqrt j)\), and the negative-frequency multipliers are conjugates. Use the expansions
\[
 v(s;R)=\sum_{n=1}^4 R^n V_n(s)+O(R^5),\quad
 m(R)=m_2 R^2+m_4 R^4+O(R^6),\quad
 \omega(R)=1+w_2 R^2+w_4 R^4+O(R^6).
\]
Here \([V_1]_{\pm1}=1/2\), with all other modes zero, and all higher Taylor coefficients have zero first-harmonic projection. Denote by \(F_n\) the coefficient of \(R^n\) in the nonlinear term evaluated on the sum of the already known terms \(R^kV_k\), \(k<n\). This gives, in particular,
\[
\begin{aligned}
 F_2&=V_1^2,\\
 F_3&=2V_1V_2+gV_1^3,\\
 F_4&=2V_1V_3+V_2^2+3gV_1^2V_2,\\
 F_5&=2V_1V_4+2V_2V_3+3g(V_1^2V_3+V_1V_2^2).
\end{aligned}
\]
At order two, \([V_2]_j=[F_2]_j/\Lambda_j\) for \(j=0,\pm2\). At order three, \((A_1m_2+B_1w_2)/2=[F_3]_1\). At \(g=4\sqrt2/9-2/3\) this gives \(m_2=0\) and \(w_2=-(7/6+3g/4)=-(2+\sqrt2)/3\), consistently with [1]. The only nonzero possible modes at order three are \([V_3]_{\pm3}=[F_3]_{\pm3}/\Lambda_{\pm3}\). At order four the potentially nonzero coefficients are
\[
 [V_4]_j=\frac{[F_4]_j-B_j w_2[V_2]_j}{\Lambda_j},\qquad j=0,\pm2,\pm4.
\]
At order five, the resonant equation is
\[
 A_1m_4+B_1w_4=2[F_5]_1-D_1,\qquad D_1=\frac{\sqrt2\sqrt i}{8}w_2^2.
\]
The term \(D_1\) is the quadratic Taylor term from \(\sqrt\omega\); the mixed \(m_2w_2\) term vanishes at criticality. There is no unknown order-five first-harmonic contribution to the left-hand side from the trace itself, and none enters the quadratic or cubic products.

**Exact coefficients.** Since \(A_1=-(1+i)/\sqrt2\) and \(B_1=(-1+i)/2\), writing \(Y=2[F_5]_1-D_1\) gives \(m_4=-(\operatorname{Re}Y+\operatorname{Im}Y)/\sqrt2\) and \(w_4=\operatorname{Im}Y-\operatorname{Re}Y\). In the convolution one uses \(\sqrt{2i}=1+i\), \(\sqrt{3i}=(1+i)\sqrt6/2\), \(\sqrt{4i}=(1+i)\sqrt2\) and their conjugates. Substituting the indicated second-, third- and fourth-order coefficients into \(F_5\), summing and differencing the real and imaginary parts as above, yields
\[
 m_4=-\frac59+\frac{23\sqrt2}{27}+\frac{5\sqrt6}{216},\qquad
 w_4=\frac{149}{108}-\frac{11\sqrt2}{9}-\frac{7\sqrt3}{54}-\frac{2\sqrt6}{27}.
\]
These operations take place over \(\mathbb Q(\sqrt2,\sqrt3)\) for the real and imaginary parts. For example, strict decimal bounds on \(m_4\) follow by substituting the rational radical endpoints \(\lfloor\sqrt{qN^2}\rfloor/N\) and \((\lfloor\sqrt{qN^2}\rfloor+1)/N\), \(q=2,6\), with \(N=10^{30}\), using the positive coefficients of both radicals in \(m_4\).

**Consequences.** Smooth evenness gives \(m(R)=m_4R^4+O(R^6)\) and the analogous frequency expansion. Positivity of \(m_4\) gives positive unfolding for sufficiently small nonzero \(R\) and the fourth-root law. Undoing the scaling gives \(\mu=\sqrt\alpha\,m\) and \(R=(\beta/\alpha)r\), as asserted.

## Verification

The accompanying standalone `verify_quintic.py` uses integer-only outward interval arithmetic to evaluate the finite Fourier recursion and enclose \(m_4\) strictly between the stated rational endpoints. The expected final line is `EXACT_OUTWARD_INTERVAL_QUINTIC_SIGN_PASS`; see `verification_output.txt`. The coefficients in the frequency expansion above are exact; the decimal values are only rounded approximations. The computation certifies the finite algebra conditional on the smooth branch theorem, not that theorem or the stability of its solutions.

## Relationship to prior work

Pelz–Scheel [1], Theorem 1.4, establishes the local periodic branch despite essential spectrum. Corollary 3.3 and Remark 3.4 supply the quadratic unfolding, cubic degeneracy and lower-order boundary profile; the strict nondegenerate stability cases do not resolve the equality case. The further contribution here is the order-five solvability calculation at equality and the resulting branch-side and amplitude law, not existence of the branch or the lower-order coefficients. Generalized-Hopf theory motivates the calculation but does not specify these square-root Fourier coefficients for this boundary equation. Pelz [2] treats a different system with two dynamic boundaries. The comparisons do not establish exhaustive historical priority.

## Limitations

The result uses a single half-line boundary without bulk degradation, \(\beta\ne0\), and exactly the stated cubic degeneracy. It makes no stability claim at degeneracy. The quartic frequency term uses the specified exact first-harmonic amplitude and need not be invariant under arbitrary nonlinear amplitude changes. The result is local and does not address other finite-amplitude cycles.

## References

1. Merlin Pelz and Arnd Scheel, *Oscillations in a scalar differential equation coupled to a diffusive field*, arXiv:2604.01135v1, especially Theorem 1.4, equation (3.1), Lemma 3.1, Corollary 3.3 and Remark 3.4. https://arxiv.org/html/2604.01135v1
2. Merlin Pelz, *Dynamical behavior of diffusively coupled scalar differential equations as Wentzell boundary conditions*, arXiv:2608.08537v1. https://arxiv.org/abs/2608.08537
