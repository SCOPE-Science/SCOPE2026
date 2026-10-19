# Marked-Poisson limit for wrong-polarity first-visit paint islands

## Finding
Consider a one-dimensional run-and-tumble Brownian particle whose first passage of a location paints it with its instantaneous propulsion sign. On the positive half-line, its complete infinite-time paint field is a two-state continuous-time Markov chain when spatial position, rather than physical time, is the parameter. More significantly, its short opposite-polarity islands have an exact **marked-Poisson limit** as translational diffusion vanishes.

Let the propulsion speed be \(v>0\), the positive translational diffusivity \(D>0\), and the actual sign-flip rate \(f>0\). Set
\[
s_D=\sqrt{v^2+2Df},\qquad a_D=\frac{s_D-v}{2D}=\frac{f}{s_D+v},\qquad b_D=\frac{s_D+v}{2D}.
\]
The generator of the first-visit sign field \(C_D(x)\in\{+1,-1\}\), ordered by position \(x\ge0\), is exactly
\[
G_D=\begin{pmatrix}-a_D&a_D\\ b_D&-b_D\end{pmatrix}.
\]
Consequently, successive intervals painted \(+\) and \(-\) have independent exponential lengths of rates \(a_D\) and \(b_D\), respectively, conditional on their initial sign. With \(D\downarrow0\) at fixed \(v,f\), consider each transition location \(z>0\) from positive to negative paint and mark it with \(v\ell_z/D\), where \(\ell_z\) is the complete spatial length of the ensuing negative-painted interval. On bounded positive spatial windows,
\[
\boxed{\quad\sum_{z:\,+\to-}\delta_{(z,v\ell_z/D)}\ \Longrightarrow\ \operatorname{PPP}\!\left(\frac{f}{2v}\,dz\,e^{-w}\,dw\right).\quad}
\]
In particular, for each \(L>0\), the number of negative islands beginning in \((0,L]\) converges in distribution to \(\operatorname{Poisson}(fL/(2v))\), and conditional limiting scaled island widths are independent unit exponentials. The initial negative-colored interval, if any, begins at \(0\) and is not counted.

## Assumptions and scope
Let \(W_t\) be standard Brownian motion, independent of a symmetric two-state continuous-time chain \(\sigma_t\in\{+1,-1\}\) flipping at rate \(f\). Starting from \(X_0=0\) and an arbitrary deterministic sign \(\sigma_0\), define
\[
X_t=v\int_0^t\sigma_u\,du+\sqrt{2D}\,W_t,\qquad T_x=\inf\{t\ge0:X_t=x\},\qquad C_D(x)=\sigma_{T_x},\quad x\ge0.
\]
All claims concern the infinite-time completed painting, not a finite observation-time window. Parameters satisfy \(v,f,D>0\). Because sample paths of \(X_t\) are continuous and the process is recurrent in both spatial directions, \(T_x<\infty\) almost surely for each finite \(x\). An almost-sure right-continuous spatial modification of the first-passage sign field is used to define its maximal monochromatic intervals. Convergence of marked point measures means convergence in distribution in the vague topology on locally compact subsets of \((0,\infty)\times(0,\infty)\); at fixed bounded windows it applies jointly to counts and full rescaled widths.

The model in Sezik, Britton, Touma and Pruessner, *Run, Tumble and Paint* (2026), uses tumble rate \(\alpha=2f\), propulsion speed \(\nu_0=v\), and \(D_x=D\). These parameters must not be confused: the actual sign-flip rate is half the paper's tumble rate.

## Proof
**1. Every positive level is reached.** Observe the process at every second flip time. Consecutive two-run displacements are independent and identically distributed as \(v(E_1-E_2)+\sqrt{2D}\,Z\), where \(E_1,E_2\) are independent exponentials of rate \(f\) and, conditional on the holding times, \(Z\) is a centered normal of variance \(E_1+E_2\). These iid increments are centered, nondegenerate and have finite variance. The classical oscillation theorem for centered one-dimensional random walks implies the sampled process has arbitrarily large positive and negative values almost surely. Continuity of \(X_t\) then ensures every finite spatial level is reached.

**2. First-visit orientation kernel.** For a target \(0\), a particle started at \(-y\) with sign \(s\) has the probability \(U_s(y)\) of being in sign \(+\) upon hitting the target. The bounded hitting harmonic functions solve, for \(y>0\),
\[
D U_+''-v U_+'+f(U_--U_+)=0,\qquad
D U_-''+v U_-'+f(U_+-U_-)=0,
\]
with \(U_+(0)=1\), \(U_-(0)=0\). The characteristic determinant is \(q^2[D^2q^2-(v^2+2Df)]\). Eliminating growing and linear modes by boundedness yields the unique bounded solution
\[
U_+(y)=p_D+(1-p_D)e^{-q_Dy},\qquad U_-(y)=p_D(1-e^{-q_Dy}),
\quad q_D=s_D/D,\quad p_D=(s_D+v)/(2s_D).
\]
Direct substitution verifies the equations and both boundary values. Optional stopping on a bounded interval, followed by the almost-sure hitting result and bounded convergence, identifies this bounded harmonic solution with the hitting probabilities. By complementing the probabilities, the two-by-two transition kernel between first-passage signs at targets separated by \(y\) is
\[
K_D(y)=\begin{pmatrix}
 p_D+(1-p_D)e^{-q_Dy}&(1-p_D)(1-e^{-q_Dy})\\
 p_D(1-e^{-q_Dy})&(1-p_D)+p_De^{-q_Dy}
\end{pmatrix}.
\]
**3. Spatial Markov property.** At \(T_x\), the full physical state is \((x,C_D(x))\). By the strong Markov property and spatial translation invariance, \(\Pr(C_D(x+y)=j\mid \sigma_{T_x}=i,\mathcal F_{T_x})=K_D(y)_{ij}\). Thus, \(C_D\) is homogeneous Markov in \(x\), with \(K_D(y)=\exp(yG_D)\) and rates \(a_D=q_D(1-p_D)\), \(b_D=q_Dp_D\). Its successive sign-run lengths are therefore independent exponentials with those two rates. This establishes all finite-dimensional joint paint statistics without a field-theoretic multipoint expansion.

**4. Marked-Poisson singular limit.** Write successive positive-run lengths as \(P_j(D)=E_j/a_D\) and negative-run lengths as \(N_j(D)=F_j/b_D\), using independent unit-exponential random variables \((E_j,F_j)_{j\ge1}\). A possible initial negative run has the same negative length law and shrinks to zero. Since \(a_D\to f/(2v)\), \(b_D\to\infty\), and \(D b_D/v\to1\), this coupling yields, for each fixed \(j\),
\[
P_j(D)\to\frac{2v}{f}E_j,\qquad N_j(D)\to0,\qquad \frac{vN_j(D)}D\to F_j\quad\text{almost surely}.
\]
Therefore the first \(k\) negative-island start locations converge jointly to the arrival times of a homogeneous Poisson process of rate \(f/(2v)\); their marks converge jointly to independent unit-exponential random variables. On any bounded window the number of such starts is tight because each start requires one positive exponential segment and \(a_D\) remains bounded. The limiting process has no atom at a fixed window boundary. Truncation to the first \(k\) arrivals followed by \(k\to\infty\) proves vague convergence of the locally finite marked point measures. The Poisson counting assertion and mark law follow.

**5. Exact finite-diffusion consistency.** The spatially stationary plus fraction is \(p_D\), the minus fraction is \(1-p_D=(s_D-v)/(2s_D)\), and the two-state covariance for a stationary initial color is \(4p_D(1-p_D)e^{-q_D h}\) at separation \(h\ge0\). For a fixed initial sign \(c_0\in\{+1,-1\}\), the plus probability at position \(x\) equals \(p_D+(\mathbf1_{\{c_0=+1\}}-p_D)e^{-q_Dx}\); hence the expected count of negative islands starting by \(L\) is
\[
\mathbb E N_D(L)=a_D\int_0^L\left[p_D+(\mathbf1_{\{c_0=+1\}}-p_D)e^{-q_Dx}\right]dx.
\]
This expression tends to \(fL/(2v)\), independently of the starting sign, consistent with the marked-Poisson theorem.

## Verification
The supplied `verify.py` independently discretizes the two-component backward hitting equations on a fine spatial grid, solves the sparse Dirichlet boundary-value problem, and compares its hitting probabilities with the claimed exact formulas. It separately compares the matrix exponential \(\exp(G_D h)\) with the explicit kernel and checks the singular rates. Three nontrivial parameter triples, nine hitting-distance comparisons and nine semigroup comparisons were checked. The maximum numerical hitting-probability error was \(9.404\times10^{-6}\) at grid spacing \(8/3000\). These numerical checks corroborate the analytic proof; they are not substitutes for the infinite-dimensional point-process limit.

Reproduce with Python 3, NumPy and SciPy: `python verify.py`.

## Relationship to prior work
Sezik, Britton, Touma and Pruessner (2026), arXiv:2603.24277v1, establish the complete one-point state-dependent visit probabilities using field theory and the relative right-/left-paint coverage (their equations (34) and (35)). They also qualitatively describe small opposite-color paint islands of scale \(D/v\). Their one-point result agrees with the stationary fraction \(1-p_D\). These prior results are neither rediscovered nor claimed as new. The exact *spatial* run-length distributions, the joint multipoint paint law and the small-\(D\) marked-Poisson point-process limit are not stated in their treatment of one-point and integrated observables.

The general Markov-modulated Brownian-motion ladder-process framework is longstanding: Asmussen (1995), Ahn and Ramaswami (2017), and Ahn and Meini (2020) identify first-passage phase transition matrices via matrix equations. Thus **spatial Markovianity itself is general prior theory**. The assessed contribution is the explicit paint-island scaling theorem and its physically normalized intensity/marks. Sezik et al. (2025), arXiv:2508.07386v1, derive orientation-dependent bounded-interval splitting probabilities; they do not formulate these infinite-halfline paint-island asymptotics.

## Limitations
The point-process limit fixes \(v,f>0\) and sends only \(D\downarrow0\); it does not cover a simultaneous vanishing-flip-rate, finite-time painting, interacting tracers, or higher dimensions. The unrescaled negative-colored field converges to all positive, so a marked rather than ordinary paint-color limit is essential. The spatial CTMC follows from general ladder-process theory and is not independently a novel theorem. More general Markov-modulated Brownian or rare-state point-process theorems could imply the limit after specialization; the literature comparison does not constitute a proof of absolute novelty. No independent audit has been performed.

## References
1. E. Sezik, C. Britton, A. Touma and G. Pruessner, *Run, Tumble and Paint* (first public 25 March 2026), arXiv:2603.24277v1, https://arxiv.org/html/2603.24277v1 . See Sections II and IV, Eq. (35), Appendix B.4.
2. E. Sezik et al., *Conditional splitting probabilities for hidden-state inference in drift-diffusive processes* (2025), arXiv:2508.07386v1, https://arxiv.org/html/2508.07386v1 . See Section 4.1.
3. S. Ahn and V. Ramaswami, *A quadratically convergent algorithm for first passage time distributions in the Markov-modulated Brownian motion*, Stochastic Models 33 (2017), 59–96, doi:10.1080/15326349.2016.1211018.
4. S. Ahn and B. Meini, *Matrix equations in Markov modulated Brownian motion: theoretical properties and numerical solution*, Stochastic Models 36 (2020), doi:10.1080/15326349.2019.1704785.
