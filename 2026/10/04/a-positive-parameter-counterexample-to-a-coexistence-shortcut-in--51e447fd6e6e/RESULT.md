# A positive-parameter counterexample to a coexistence shortcut in a prey-taxis model
## Finding
For the spatially homogeneous equilibrium equations in Liu and Tan's memory-based prey-taxis predator–prey model, the prey component of a positive coexistence equilibrium must lie in
\[
(L_0,U),\qquad L_0=\max\{0,L\}.
\]
The paper derives this admissible interval in its proof of Theorem 3.1, but the theorem statement classifies coexistence using the signs at \(L\) and \(U\), and states that the weak-Allee inequalities \(\gamma_1>\beta_2\) and \(\beta<C_1\) imply the unique-equilibrium case.

That shortcut is false when \(L<0\). Take
\[
r=K=m=\beta=\gamma=\beta_1=\beta_2=\beta_3=A=1,\qquad
\alpha=2,\qquad \gamma_1=2,\qquad \eta=\frac{1}{10}.
\]
Then \(r>\beta_1\eta\), \(\gamma_1>\beta_2\), and \(\beta<C_1\), exactly as in the printed weak-Allee shortcut, but the model has no positive coexistence equilibrium. The correct sign-change test is at \(L_0\), not at a negative value of \(L\).

## Assumptions and scope
The source model has positive biological parameters and studies spatially homogeneous equilibria \((u,v)\) with \(u>0\) and \(v>0\). Diffusion, taxis sensitivity, and delay do not enter the homogeneous equilibrium equations. For this counterexample they may therefore take any values allowed by the source; for definiteness one may set the positive diffusion and taxis coefficients to \(1\) and the delay to \(0\).

Following the source, define
\[
C_1=\gamma+\beta_2A+\beta_3\eta,\qquad C_2=\beta_2-\gamma_1,
\]
\[
R(u)=r\left(1-\frac{u}{K}\right)-\beta_1\eta,
\]
and
\[
v=\frac{uR(u)}{\alpha-mR(u)}.
\]
Positivity of \(u\) and \(v\) is equivalent to
\[
0<R(u)<\frac{\alpha}{m},
\]
so an admissible root must satisfy
\[
u\in(L_0,U),\qquad
L_0=\max\{0,L\},\quad
L=K\left(1-\frac{\alpha+m\beta_1\eta}{rm}\right),\quad
U=K\left(1-\frac{\beta_1\eta}{r}\right).
\]
The claim concerns only existence of a positive homogeneous coexistence equilibrium and the stated shortcut in Theorem 3.1(a). It does not reassess the paper's later stability or bifurcation results at their numerical parameter choices.

## Proof
The source reduces the coexistence condition to a quadratic
\[
f(u)=A_q u^2+B_q u+C_q,
\]
where, writing \(\Theta=K(\alpha-mr+m\beta_1\eta)\),
\[
A_q=\beta(rm)^2+\alpha KrC_2,
\]
\[
B_q=2\beta rm\Theta-\alpha KrmC_1-\alpha K^2(r-\beta_1\eta)C_2,
\]
and
\[
C_q=\beta\Theta^2-\alpha K\Theta C_1.
\]
For the displayed parameter tuple,
\[
C_1=\frac{21}{10},\qquad C_2=-1,\qquad
L=-\frac{11}{10},\qquad L_0=0,\qquad U=\frac{9}{10},\qquad
\Theta=\frac{11}{10}.
\]
The source's theorem hypotheses and printed weak-Allee shortcut hold because
\[
r=1>\frac{1}{10}=\beta_1\eta,\qquad
\gamma_1=2>1=\beta_2,\qquad
\beta=1<\frac{21}{10}=C_1.
\]
Substitution into the quadratic coefficients gives
\[
A_q=-1,\qquad B_q=-\frac{1}{5},\qquad C_q=-\frac{341}{100},
\]
thus
\[
f(u)=-u^2-\frac{u}{5}-\frac{341}{100}.
\]
Every term on the right is strictly negative for \(u>0\). Hence \(f(u)<0\) for every positive \(u\), in particular throughout \((0,9/10)\). The source's own reduction says that positive coexistence equilibria are in one-to-one correspondence with roots in the admissible interval, so none exists.

The mismatch is visible directly in the endpoint formulas. For this tuple,
\[
f(L)=f(U)=-\frac{22}{5},
\]
so even the theorem statement's written premise \(f(L)f(U)<0\) is not implied by its following weak-Allee shortcut. More fundamentally, when \(L<0\), \(L\) is outside the biological domain. The proof correctly switches to \(L_0=\max\{0,L\}\) and uses \(f(L_0)f(U)<0\). Therefore the sign-change argument must use \(L_0\).

## Verification
The accompanying `verify.py` performs all arithmetic with exact rational numbers. It verifies the theorem-side inequalities, computes \(C_1\), \(C_2\), \(L\), \(L_0\), \(U\), and \(\Theta\), reconstructs \(A_q\), \(B_q\), and \(C_q\), checks \(f(L)=f(U)=-22/5\), and certifies that all three coefficients of \(f(u)\) are negative. Since \(u>0\), that coefficient sign pattern is itself an exact proof that \(f(u)<0\); no finite sampling is used as a substitute for the universal statement.

## Relationship to prior work
Liu and Tan derive the admissible interval \((L_0,U)\) and the quadratic reduction in Section 3 of the motivating paper, so the counterexample is checked against the paper's own equations rather than an altered model. The theorem statement uses \(L\) in its endpoint classification, while the proof uses \(L_0\); the counterexample exploits exactly the regime where those quantities differ.

Related recent predator–prey models with memory mechanisms study positive equilibria and bifurcations, including Meng and Liang's delayed memory-diffusion/fear model and Zhu, Zhang, and Li's cognitive-map/perceptual-taxis model. Their reported models and equilibrium analyses are different and do not imply this source-specific counterexample or the required replacement of the inadmissible lower endpoint.

Published published-finding corpus searches for the exact DOI, the theorem's weak-Allee conditions, the \(L\)-versus-\(L_0\) distinction, and the no-coexistence conclusion returned no result that states or implies this claim. The closest hits concern different models and different stability or pattern questions.

## Limitations
This result is a counterexample to the printed parameter shortcut and a correction to the endpoint used by its sign-change argument. It does not claim that every conclusion in Theorem 3.1(b) is false, nor does it provide a complete replacement classification for all parameter regimes. It also does not assert anything about nonhomogeneous steady states, transient dynamics, or the later bifurcation calculations at parameter values for which a positive equilibrium actually exists.

## References
1. D. Liu and X. Tan, “Memory-based prey-taxis and environmental stress shape spatiotemporal predator-prey dynamics,” *AIMS Mathematics* 11(6), 17880–17916 (2026). DOI: 10.3934/math.2026729.
2. X.-Y. Meng and Z.-W. Liang, “Dynamics analysis of a delayed diffusive predator–prey model with memory-based diffusion and fear effect of prey,” *International Journal of Biomathematics* (2025). DOI: 10.1142/S1793524525501013.
3. K. Zhu, X. Zhang, and S. Li, “Bifurcation analysis and spatiotemporal patterns in a consumer-resource model with cognitive map and perceptual taxis,” *Physica Scripta* 101 (2026). DOI: 10.1088/1402-4896/ae7ced.
