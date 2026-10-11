# An exact population mode corrects the first-delay crossing in a synthetic-drug DDE
## Finding
For the numerical delay system printed as equation (5.1) by Wang, Zeb, Upadhyay and Pratap, define
\[
N=S+P_1+P_2+T.
\]
Adding the four printed equations cancels every transfer term, including the delayed term, and gives
\[
\dot N=\frac65-\frac150N.
\]
Thus the linearization has the exact delay-independent characteristic root \(\lambda=-1/50\). At the exact positive equilibrium of the printed equations,
\[
E_*=\left(\frac{1407}{4561},\frac{544506}{305587},\frac{105271160}{2139109},\frac{18603955}{2139109}\right),
\]
the characteristic determinant factors as
\[
\det(\lambda I-A_0-e^{-\lambda\tau}A_1)
=\frac{50\lambda+1}{17493700000000}
\left(P(\lambda)+Q(\lambda)e^{-\lambda\tau}\right),
\]
where
\[
P(\lambda)=349874000000\lambda^3+1406053367500\lambda^2+1163274624350\lambda+191256352392
\]
and
\[
Q(\lambda)=157443300000\lambda^2+597344121000\lambda+391122490185.
\]
The reduced equation has exactly one positive imaginary frequency. Writing \(u=\Omega^2\), its modulus condition is
\[
122411815876000000000000u^3
+1138198587703536256250000u^2
+581713807208182432802500u
-116397809998222537212561=0.
\]
Its unique positive root is
\[
u_*=0.1533334188148464043\ldots,
\qquad
\Omega_*=0.391578113299053532\ldots.
\]
The first positive delay satisfying the phase equation is
\[
\tau_*=5.31769616572693034\ldots.
\]
At this point
\[
\operatorname{Re}\left(\frac{d\lambda}{d\tau}\right)
=0.0169758691356184\ldots>0,
\]
so the conjugate pair crosses from left to right. The reduced cubic at \(\tau=0\) has positive coefficients and the exact Routh--Hurwitz determinant
\[
2548962325924970823125000>0,
\]
so it is Hurwitz. Consequently the printed system is linearly asymptotically stable for \(0\le\tau<\tau_*\) and first loses linear stability at \(\tau_*\).

The paper instead reports \(\Omega=0.320220\) and \(\tau_0=5.105862\) for system (5.1). Those numbers therefore are not the first characteristic crossing of the equations as printed.

## Assumptions and scope
The claim treats equation (5.1) literally. In particular, its first equation contains the natural-removal coefficient \(0.02\), and the remaining printed removal coefficients \(0.22\), \(0.14\), and \(0.72\) are consistent with the same \(0.02\) contribution. The prose immediately above (5.1) lists \(\delta=0.2\); this is inconsistent with the displayed system. The result concerns the displayed system, not a hypothetical system obtained by replacing its coefficients with the prose value.

The conclusion is a linear stability/crossing statement. It does not assert the nonlinear direction or orbital stability of the branch created at the corrected crossing, because the source's normal-form coefficients were evaluated using its reported critical value and are not recomputed here.

## Proof
Adding the four equations of (5.1) gives \(\dot N=6/5-N/50\). Therefore perturbations in the total-population direction have the exact scalar eigenvalue \(-1/50\), independent of delay.

Solving the four equilibrium equations with the delayed value equal to the current value gives the displayed rational point \(E_*\). Its coordinates are positive and sum to \(60\), as required by the scalar population balance.

At this equilibrium the current-state Jacobian is
\[
A_0=\begin{pmatrix}
-416714303/139949600&-1407/74600&-1407/59680&0\\
413915311/139949600&-3001/14920&1407/59680&0\\
0&0&-7/50&7/10\\
0&1/5&3/25&-18/25
\end{pmatrix},
\]
and the delayed Jacobian has only
\[
(A_1)_{22}=-9/20,
\qquad
(A_1)_{32}=9/20
\]
nonzero, when coordinates are ordered as \(S,P_1,P_2,T\). Direct determinant expansion gives the displayed factorization.

For a nonzero imaginary root \(\lambda=i\Omega\), the reduced equation implies \(|P(i\Omega)|=|Q(i\Omega)|\). Setting \(u=\Omega^2\) gives the displayed cubic. Its coefficient signs are \(+,+,+,-\), so Descartes' rule gives at most one positive root; its derivative is strictly positive for \(u>0\), while its value at \(0\) is negative and it tends to \(+\infty\). Hence there is exactly one positive root.

For that root, the phase relation is
\[
e^{-i\Omega_*\tau}=-\frac{P(i\Omega_*)}{Q(i\Omega_*)}.
\]
The right side has unit modulus and principal argument \(-2.08229343167296247\ldots\). Thus the smallest positive phase-compatible delay is \(\tau_*=5.31769616572693034\ldots\); all later phase branches add \(2\pi/\Omega_*\).

At \(\tau=0\), the reduced characteristic polynomial has coefficients
\[
349874000000,
\quad 1563496667500,
\quad 1760618745350,
\quad 582378842577,
\]
from cubic to constant term. The cubic Routh--Hurwitz condition is satisfied because
\[
1563496667500\cdot1760618745350
-349874000000\cdot582378842577
=2548962325924970823125000>0.
\]
Since the imaginary-root modulus equation has only one positive frequency, its first phase branch is the first possible nonzero imaginary crossing. Implicit differentiation of \(P(\lambda)+Q(\lambda)e^{-\lambda\tau}=0\) at that point gives the positive real crossing speed stated above. This proves the stability interval and the first loss of linear stability.

## Verification
The accompanying `verify.py` uses only the Python standard library. It checks the exact equilibrium residuals, reconstructs the characteristic determinant from the rational Jacobian, verifies the exact \((50\lambda+1)\) factor and reduced polynomials, derives the exact cubic in \(u\), proves the exact zero-delay Routh--Hurwitz inequality, brackets the unique positive root, and numerically replays the phase and transversality calculations. A successful run prints `VERIFY_OK`.

## Relationship to prior work
Wang et al. introduce the one-delay version of the Saha--Samanta two-stage synthetic-drug model, derive a generic quartic-plus-delayed-cubic characteristic equation, and in their Section 5 report \(\Omega=0.320220\) and \(\tau_0=5.105862\) for the displayed numerical system (5.1). The source does not factor out the exact total-population mode and does not report the corrected values above.

Saha and Samanta study the underlying nondelayed two-stage model, so their results do not contain this delay characteristic crossing. Zhang, Yang and Xia study a different four-compartment synthetic-drug model with two delays and a different transfer structure; its characteristic equation and numerical thresholds do not imply the factorization or corrected crossing for Wang et al.'s system (5.1).

Targeted searches for the exact DOI, title, reported numbers, correction/corrigendum terms, the total-population factor, and the corrected numerical threshold did not locate a publication stating this correction. That negative search evidence is not a proof of uniqueness; it is recorded only as part of the literature comparison.

## Limitations
The result is tied to the coefficients actually printed in (5.1). The prose parameter list immediately above the system says \(\delta=0.2\), whereas the equations use coefficients consistent with \(\delta=0.02\); this finding does not choose a scientifically intended value beyond taking the displayed system literally. It also does not recompute the nonlinear first Lyapunov coefficient, the supercritical/subcritical designation, or the orbital stability of the bifurcating branch.

The literature comparison cannot exclude an unindexed correction or later reuse of the same calculation that was not discoverable in the inspected sources.

## References
1. Y. Wang, A. Zeb, R. K. Upadhyay, A. Pratap, “A delayed synthetic drug transmission model with two stages of addiction and Holling Type-II functional response,” *AIMS Mathematics* 6 (2021), 1–22. DOI: 10.3934/math.2021001. First published 28 September 2020.
2. S. Saha, G. P. Samanta, “Synthetic drugs transmission: stability analysis and optimal control,” *Letters in Biomathematics* 6 (2019), 1–31. DOI: 10.1080/23737867.2019.1624204.
3. Z. Zhang, F. Yang, W. Xia, “Hopf Bifurcation Analysis of a Synthetic Drug Transmission Model with Time Delays,” *Complexity* 2019, Article 3492589. DOI: 10.1155/2019/3492589.
