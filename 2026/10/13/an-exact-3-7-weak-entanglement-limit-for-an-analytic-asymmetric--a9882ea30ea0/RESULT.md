# An exact \(3/7\) weak-entanglement limit for an analytic asymmetric \(I_{3322}\) qubit strategy
## Finding
Consider the asymmetric three-setting Bell test based on \(I_{3322}\), with Alice detected perfectly and Bob assigning a no-click event to outcome \(0\). Let
\[
|\psi_\theta\rangle=\cos\theta|00\rangle+\sin\theta|11\rangle,
\qquad \theta>0,
\]
and use real qubit observables in the \(x\)-\(z\) plane,
\[
A_i=\cos(\alpha_i)Z+\sin(\alpha_i)X,
\qquad
B_j=\cos(\beta_j)Z+\sin(\beta_j)X,
\]
where outcome \(0\) is the \(+1\) projector.

The explicit analytic choice
\[
\alpha_1=0,\quad
\alpha_2=2\sqrt{\theta},\quad
\alpha_3=\frac{\pi}{2},\qquad
\beta_1=\frac{2}{3}\theta,\quad
\beta_2=-\frac{2}{3}\theta,\quad
\beta_3=-2\sqrt{\theta}
\]
has ideal Bell value \(Q(\theta)\) and one-sided no-click value \(M_A(\theta)\) satisfying
\[
Q(\theta)=\frac43\theta^2-\frac{25}9\theta^3-\frac19\theta^4+O(\theta^5),
\qquad
M_A(\theta)=-\sin^2\theta=-\theta^2+\frac13\theta^4+O(\theta^6).
\]
Consequently the threshold formula
\[
\eta_B^{\mathrm{th}}=
\frac{-M_A}{Q-M_A}
\]
gives
\[
\eta_B^{\mathrm{th}}
=\frac37+\frac{25}{49}\theta+\frac{562}{1029}\theta^2+O(\theta^3),
\]
so
\[
\lim_{\theta\to0^+}\eta_B^{\mathrm{th}}=\frac37.
\]
In particular, every fixed efficiency \(\eta_B>3/7\) is achieved by this explicit qubit strategy for all sufficiently small positive \(\theta\).

There is also a sharp leading-order classification inside the natural weak-entanglement scaling family
\[
\alpha_1=u\theta,\quad
\alpha_2=a\sqrt{\theta},\quad
\alpha_3=\frac{\pi}{2}+c\sqrt{\theta},\qquad
\beta_1=b\theta,\quad
\beta_2=d\theta,\quad
\beta_3=f\sqrt{\theta},
\]
with fixed real \(u,a,c,b,d,f\). Writing \(Q(\theta)=q_4\theta^2+O(\theta^{5/2})\), one obtains
\[
q_4=
\frac43-
\frac{(af+4)^2}{16}-
\frac38\left(b-\frac23\right)^2-
\frac38\left(d+\frac23\right)^2-
\frac{u^2}4.
\]
Also
\[
-M_A(\theta)=\left(1+\frac{u^2}4\right)\theta^2+O(\theta^3).
\]
Therefore the leading Bell-to-loss ratio is at most \(4/3\), and every member with \(q_4>0\) has limiting threshold at least \(3/7\). Equality holds exactly when
\[
u=0,\qquad af=-4,\qquad b=\frac23,\qquad d=-\frac23,
\]
while \(c\) is unrestricted at leading order. The explicit family above is the simplest symmetric representative with \(a=2\) and \(f=-2\).

## Assumptions and scope
The Bell polynomial is the standard probability form
\[
\begin{aligned}
I_{3322}={}&P(A_1B_1)+P(A_1B_2)+P(A_1B_3)+P(A_2B_1)+P(A_2B_2)+P(A_3B_1)\\
&-P(A_2B_3)-P(A_3B_2)-2P(A_1)-P(A_2)-P(B_1),
\end{aligned}
\]
with local bound \(0\). Alice's efficiency is \(1\), Bob's no-click output is fixed to \(0\), and all measurements are binary projective qubit measurements in one real Bloch plane. The state parameter obeys \(\theta\to0^+\).

The six-parameter optimality statement concerns only the displayed asymptotic scaling. It is not a lower bound for arbitrary qubit measurements with a different dependence on \(\theta\), not a proof of global optimality of \(3/7\), and not a proof of the later numerical dimension-witness statement at efficiency \(0.428\).

## Proof
For outcome-\(0\) projectors \(\Pi(\alpha)=(I+\cos(\alpha)Z+\sin(\alpha)X)/2\), direct evaluation on \(|\psi_\theta\rangle\) gives
\[
P(A_i)=\frac12\left[1+\cos(2\theta)\cos(\alpha_i)\right]
\]
and
\[
P(A_iB_j)=\frac14\left[1+\cos(2\theta)(\cos\alpha_i+\cos\beta_j)
+\cos\alpha_i\cos\beta_j+\sin(2\theta)\sin\alpha_i\sin\beta_j\right].
\]
Substitution into \(I_{3322}\) gives the ideal Bell value \(Q\). When Bob does not click and outputs \(0\), the source reduction gives
\[
M_A=P(A_1)-1,
\qquad
\eta_B^{\mathrm{th}}=\frac1{1-Q/M_A}=\frac{-M_A}{Q-M_A}.
\]

For the general scaling family, Taylor expansion of the preceding exact trigonometric formulas yields
\[
Q(\theta)=q_4\theta^2+O(\theta^{5/2}),
\qquad
M_A(\theta)=-\left(1+\frac{u^2}4\right)\theta^2+O(\theta^3),
\]
where
\[
q_4=-\frac1{16}\left[a^2f^2+8af+6b^2-8b+6d^2+8d+4u^2\right].
\]
Completing squares gives
\[
q_4=\frac43-
\frac{(af+4)^2}{16}-
\frac38\left(b-\frac23\right)^2-
\frac38\left(d+\frac23\right)^2-
\frac{u^2}4.
\]
Thus
\[
\frac{q_4}{1+u^2/4}\leq\frac43,
\]
with equality exactly under the four stated conditions. Since \(\eta_B^{\mathrm{th}}=1/(1+Q/(-M_A))\), for every member with \(q_4>0\), the limiting threshold in this scaling class is no smaller than \(3/7\), with equality at those conditions.

Taking \(u=0\), \(a=2\), \(c=0\), \(b=2/3\), \(d=-2/3\), and \(f=-2\) and expanding the exact formulas one order further gives
\[
Q(\theta)=\frac43\theta^2-\frac{25}9\theta^3-\frac19\theta^4+O(\theta^5),
\]
while \(M_A=-\sin^2\theta\). Formal series division then yields the displayed expansion for \(\eta_B^{\mathrm{th}}\). Analyticity of the trigonometric expressions makes the remainder statements ordinary Taylor remainders, and the positive leading coefficient \(4/3\) ensures \(Q(\theta)>0\) for all sufficiently small positive \(\theta\).

## Verification
The bundled `verify.py` independently evaluates the exact probability formulas with the displayed angles using only Python's standard library. It checks positivity of \(Q\) at decreasing \(\theta\), convergence of the threshold to \(3/7\), the exact completed-square identity for the leading coefficient on a deterministic rational test set, and the exact leading coefficients \(4/3\), \(-25/9\), \(-1/9\), \(-1\), and \(1/3\) used in the proof. Its successful terminal output is `VERIFY_OK`.

The checker is confirmatory rather than the proof of the infinite statement: the infinite claim follows from the displayed symbolic Taylor expansion and completed-square identity.

## Relationship to prior work
Brunner, Gisin, Scarani, and Simon introduced the asymmetric detection-loophole analysis for this \(I_{3322}\) setting. For weakly entangled qubits they reported a threshold tending numerically to about \(43\%\), explicitly stating that they could not find an analytical expression for the optimal settings as a function of \(\theta\); their paper supplies a numerical example at \(\theta=\pi/100\). The present result supplies a closed analytic one-parameter family whose threshold tends to the exact rational value \(3/7\approx0.428571\), and a complete leading-order classification of the positive-leading-violation regime inside the displayed six-parameter scaling.

Vertesi, Pironio, and Brunner later gave analytic \(N\)-dimensional constructions approaching efficiency \(1/N\). For the qubit behavior of \(I_{3322}\), however, they described the nonviolation below efficiency \(0.428\) as strong numerical evidence. The present finding addresses only the constructive qubit side and does not imply that global nonviolation statement.

Targeted searches for the exact constant \(3/7\), the decimal \(0.428571\), the weak-entanglement scaling, and analytic settings for the 2007 asymmetric \(I_{3322}\) problem did not locate a prior statement with the same hypotheses and conclusion. This search evidence is not by itself a proof of novelty; the closest inspected primary sources and residual indexing risk are recorded in `AUDIT.json`.

## Limitations
No global optimality over all qubit strategies is claimed. A different asymptotic scaling could in principle beat \(3/7\); ruling that out would require a separate argument. The result does not establish the 2010 conjectural/numerical qubit dimension-witness boundary, does not treat detector noise or background noise, and does not optimize finite \(\theta\). The exact asymptotic construction is noiseless and projective.

## References
1. N. Brunner, N. Gisin, V. Scarani, C. Simon, *Detection loophole in asymmetric Bell experiments*, arXiv:quant-ph/0702130v1 (first public 2007-02-13), Phys. Rev. Lett. 98, 220403 (2007), DOI:10.1103/PhysRevLett.98.220403.
2. T. Vertesi, S. Pironio, N. Brunner, *Closing the detection loophole in Bell experiments using qudits*, arXiv:0909.3171v1 (first public 2009-09-17), Phys. Rev. Lett. 104, 060401 (2010), DOI:10.1103/PhysRevLett.104.060401.
3. MSC2020, 81P15: Quantum measurement theory, state operations, state preparations.
