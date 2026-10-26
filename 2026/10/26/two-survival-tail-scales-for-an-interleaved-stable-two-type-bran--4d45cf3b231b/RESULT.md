# Two survival-tail scales for an interleaved-stable two-type branching process

## Finding

The two-type continuous-state branching mechanism singled out as undecided by the available criteria in Chaumont–Lamoureux (2026, Section 3.2) is **nonconservative**. In fact, from every nonzero finite initial mass it reaches its cemetery state in finite time almost surely. Its nonexplosion probability has two distinct asymptotic scales determined by which type is initially present.

Let the increasing sequence \(a_0=0\), \(a_1=1\), and, for integers \(n\ge1\),
\[
a_{n+1}=\bigl((\sqrt{a_n}+1)e^{\sqrt{a_n}}\bigr)^2
\]
and let
\[
A_1=\bigcup_{n\ge0}[a_{2n},a_{2n+1}),\qquad
A_2=\bigcup_{n\ge0}[a_{2n+1},a_{2n+2}).
\]
For \(j\in\{1,2\}\) and \(x\ge0\), define
\[
\phi_j(x)=\int_{A_j}(1-e^{-xy})y^{-3/2}\,dy,\qquad
L=\int_{A_2}y^{-3/2}\,dy
 =2\sum_{n\ge0}\bigl(a_{2n+1}^{-1/2}-a_{2n+2}^{-1/2}\bigr).
\]
Here \(0<L<2\). The branching mechanism is
\[
\psi_j(\lambda_1,\lambda_2)=-\phi_j(\lambda_1)-\phi_j(\lambda_2),\qquad j=1,2.
\]
Let \(\zeta\) denote the cemetery-state hitting time, and let \(u(t)=(u_1(t),u_2(t))\) be the zero-argument cumulant vector. For every \(t>0\), both coordinates of \(u(t)\) are positive and
\[
\boxed{\pi t^2\le u_1(t)+u_2(t)\le2\pi t^2.}
\]
As \(t\to\infty\),
\[
\boxed{u_1(t)=\pi t^2+4\sqrt{2\pi L}\,t^{3/2}+o(t^{3/2}),\qquad
u_2(t)=2Lt+o(t).}
\]
For every finite \(z_1,z_2\ge0\) with \(z_1+z_2>0\),
\[
\mathbb P_{(z_1,z_2)}(\zeta>t)
=\exp\{-z_1u_1(t)-z_2u_2(t)\}.
\]
Thus for \(z_1>0\) the log-survival probability has leading term \(-\pi z_1t^2\) and the explicit next correction \(-4z_1\sqrt{2\pi L}\,t^{3/2}\). Starting solely from type two, \(z_1=0<z_2\), the log-survival probability instead equals \(-2Lz_2t+o(t)\). For equal initial masses \(z_1=z_2=b>0\), the finite-time inequalities specialize to
\[
\boxed{e^{-2\pi bt^2}\le\mathbb P_{(b,b)}(\zeta>t)\le e^{-\pi bt^2}.}
\]

## Assumptions and scope

The mechanism, sets, and recurrence are precisely those of the explicitly undecided example in Section 3.2 of Chaumont–Lamoureux (arXiv:2610.23649v1). No immigration, deaths, killing term, or finite-moment assumption is introduced. The process is the standard two-type continuous-state branching process determined by that mechanism. The assertion concerns the cemetery/explosion time, not extinction at zero. Times \(t\) are deterministic nonnegative reals, and initial mass vectors are finite and nonnegative. The first-public date of the motivating mechanism is 2026-10-16.

The power expansions concern \(t\to\infty\) for this fixed mechanism. They are not uniform over arbitrary modifications of the disjoint sets. The positive constant \(L\) is intrinsic to the displayed second set, whose lower endpoint is \(1\).

## Proof

**1. Stable identity and bounds.** The sets partition \([0,\infty)\), so an integration by parts gives, for all \(x\ge0\),
\[
\phi_1(x)+\phi_2(x)=\int_0^\infty(1-e^{-xy})y^{-3/2}\,dy
=2\sqrt\pi\,\sqrt x.
\]
Because \(A_2\subset[1,\infty)\) and has positive Lebesgue measure, monotone convergence gives \(0<\phi_2(x)\uparrow L<2\) as \(x\to\infty\). Consequently \(\phi_1(x)=2\sqrt\pi\sqrt x-\phi_2(x)\), and both functions are continuous, nondecreasing, and strictly positive on \((0,\infty)\).

**2. Cumulants and the nonzero solution from zero.** For any \(\varepsilon>0\), write \(v^{\varepsilon}(t)=(v_1,v_2)\) for the solution of
\[
\dot v_1=\phi_1(v_1)+\phi_1(v_2),\qquad
\dot v_2=\phi_2(v_1)+\phi_2(v_2),\qquad
v_1(0)=v_2(0)=\varepsilon.
\]
The right-hand side is locally Lipschitz on the positive quadrant and cooperative. Thus the solution exists uniquely, is coordinatewise nondecreasing, and is monotone in \(\varepsilon\). Let \(s^\varepsilon=v_1+v_2\). The stable identity yields
\[
\dot s^\varepsilon=2\sqrt\pi(\sqrt{v_1}+\sqrt{v_2}),
\]
and hence
\[
\sqrt\pi\le\frac{d}{dt}\sqrt{s^\varepsilon}
=\sqrt\pi\frac{\sqrt{v_1}+\sqrt{v_2}}{\sqrt{v_1+v_2}}
\le\sqrt{2\pi}.
\]
For every \(t\ge0\),
\[
(\sqrt{2\varepsilon}+\sqrt\pi t)^2\le s^\varepsilon(t)
\le(\sqrt{2\varepsilon}+\sqrt{2\pi}t)^2.
\]
These bounds prove global existence and uniform boundedness on finite time intervals. Cooperative comparison gives a coordinatewise limit as \(\varepsilon\downarrow0\). Equicontinuity on compact intervals and dominated passage in the integral equations show that the limit \(u(t)\) is a continuous solution with \(u(0)=0\). It is the zero-argument cumulant of the branching process by monotone convergence of its positive-argument Laplace cumulants. The last display gives \(\pi t^2\le u_1(t)+u_2(t)\le2\pi t^2\). Its sum is positive for \(t>0\); since each \(\phi_j\) is strictly positive away from zero, integration over \((t/2,t)\) gives \(u_j(t)>0\).

**3. First and second large-time scales.** Since \(\phi_2\le L\),
\[
0<u_2(t)\le2Lt,\qquad
u_1(t)\ge\pi t^2-2Lt\longrightarrow\infty.
\]
The second-coordinate equation and \(\phi_2(u_1(t))\to L\) show that \(u_2(t)\to\infty\) as well. Therefore
\[
\dot u_2(t)=\phi_2(u_1(t))+\phi_2(u_2(t))=2L+o(1),
\]
and integration gives \(u_2(t)=2Lt+o(t)\).

Write \(r(t)=\sqrt{u_1(t)}\) for \(t>0\). Substitution of the stable identity gives exactly
\[
\dot r(t)=\sqrt\pi+\sqrt\pi\frac{\sqrt{u_2(t)}}{r(t)}
-\frac{\phi_2(u_1(t))+\phi_2(u_2(t))}{2r(t)}.
\]
The quadratic lower bound on \(u_1\) and the linear upper bound on \(u_2\) first yield \(\dot r(t)=\sqrt\pi+O(t^{-1/2})\), so \(r(t)=\sqrt\pi t+O(\sqrt t)\). Using \(u_2(t)/t\to2L\) in the same exact equation then gives
\[
\sqrt t\bigl(\dot r(t)-\sqrt\pi\bigr)\longrightarrow\sqrt{2L}.
\]
Integration yields \(r(t)=\sqrt\pi t+2\sqrt{2L}\sqrt t+o(\sqrt t)\), and squaring proves the stated coefficient \(4\sqrt{2\pi L}\).

**4. Explosion probabilities.** The standard branching cumulant identity gives
\[
\mathbb P_z(\zeta>t)=\exp\{-z_1u_1(t)-z_2u_2(t)\}.
\]
Both cumulants are positive for positive times and diverge as time tends to infinity. Thus every nonzero finite starting vector has positive finite-time explosion probability and explosion occurs almost surely at some finite time. Substitution of the bounds and asymptotics from Steps 2–3 yields all survival statements.

## Verification

The proof is analytic. Run `python check.py` to reproduce supplementary finite computations of the truncated Lévy integral, the rigorous bound on its omitted tail, and sample ODE trajectories from small positive initial arguments. The numerical script uses only Python's standard library. Its finite samples do not establish the infinite-time limits or uniqueness assertions. The exact proof depends only on the partition identity, cooperative ODE comparison, elementary inequalities, dominated convergence, and the established cumulant interpretation.

For a numerical value, since \(a_2=4e^2\), a truncation after the second interval of \(A_2\) gives
\[
L=2(1-a_2^{-1/2})+2a_3^{-1/2}+E,\qquad
-2a_4^{-1/2}\le E\le0.
\]
Hence \(L\) is approximately \(1.633473585414\), with an absolute truncation error bounded by \(2a_4^{-1/2}\). The approximation is not needed in the proof.

## Relationship to prior work

Chaumont and Lamoureux, *On conservativity of multitype continuous-state branching processes*, arXiv:2610.23649v1 (2026), Section 3.2, explicitly define the two interleaved sets and the displayed branching mechanism. They show that their Theorems 3.1–3.3 do not decide conservativity in this example. Those theorems are **not** restated as new findings here. The new conclusion classifies their specific process and gives its two distinct explosion-tail scales.

Li and Li, *Uniqueness Problem for the Backward Differential Equation of a Continuous-State Branching Process*, arXiv:2405.05879v1 (2024), Theorem 4.1, give the general relationship between uniqueness of the zero-start backward equation and conservativity. Duffie, Filipović and Schachermayer (2003), Section 9, give a related criterion for affine processes. Neither inspected result evaluates this interleaved-stable example or the explicit two-scale survival asymptotics; their general framework is used rather than claimed as novel. Grey's one-type criterion provides background but does not by itself determine the coupled example.

## Limitations

The asymptotic coefficients rely on \(A_2\subset[1,\infty)\) and the full interleaved partition. They do not classify all two-type branching mechanisms, prove a converse to any general conservativity criterion, or establish sample-path explosion-rate asymptotics. An equivalent treatment in older specialized literature cannot be excluded by searches alone. This analysis has not undergone independent mathematical audit.

## References

1. L. Chaumont and C. Lamoureux, *On conservativity of multitype continuous-state branching processes*, arXiv:2610.23649v1, 16 October 2026, Section 3.2, https://arxiv.org/html/2610.23649v1.
2. P.-S. Li and Z. Li, *Uniqueness Problem for the Backward Differential Equation of a Continuous-State Branching Process*, arXiv:2405.05879v1 (2024), Theorem 4.1, https://arxiv.org/pdf/2405.05879.
3. D. Duffie, D. Filipović and W. Schachermayer, *Affine Processes and Applications in Finance*, Annals of Applied Probability 13 (2003), Section 9, https://web.stanford.edu/~duffie/affine.pdf.
4. D. R. Grey, *Asymptotic behaviour of continuous time, continuous state-space branching processes*, Journal of Applied Probability 11 (1974), 669–677.
