# A feedback-resonance boundary forbids interior recurrence in two-community eco-evolutionary games

## Finding

For the five-dimensional two-community evolutionary game with three logistic environmental states introduced by Betz, Fu and Masuda [1], there is an exact **affine log-odds law** independent of the payoff matrices, the interaction rate, and the strategy trajectory. Write the cooperator fractions as \(x,y\in[0,1]\), the within-community and between-community environmental states as \(n_1,n_2,n_{12}\in(0,1)\), and the positive feedback ratios as \(\theta_1,\theta_2,\theta_{12}\). Define

\[
\ell(s)=\log\frac{s}{1-s},\qquad
 a=\frac{1+\theta_{12}}{2(1+\theta_1)},\qquad
 b=\frac{1+\theta_{12}}{2(1+\theta_2)},
\]
\[
\mathcal I=\ell(n_{12})-a\ell(n_1)-b\ell(n_2),\qquad
\kappa=\frac{\theta_{12}(2+\theta_1+\theta_2)-(\theta_1+\theta_2+2\theta_1\theta_2)}{2(1+\theta_1)(1+\theta_2)}.
\]

For every solution with initially interior environmental states, at every finite time \(t\ge0\),

\[
\boxed{\mathcal I(t)=\mathcal I(0)+\kappa t.}
\]

Consequently, unless the **feedback resonance**

\[
\boxed{\theta_{12}=\frac{\theta_1+\theta_2+2\theta_1\theta_2}{2+\theta_1+\theta_2}}
\]

holds, there is no equilibrium, periodic orbit, recurrent point, or nonempty compact forward-invariant set contained in the part of state space with all three environments strictly interior. At resonance, \(\mathcal I\) is an exact first integral, and an admissible family with a continuum of fully interior equilibria is exhibited below; thus the obstruction is sharp as a condition on feedback ratios alone.

There is also a quantitative **directed boundary-selection law**. Fix \(0<\varepsilon<1/2\), set \(H_\varepsilon=(1+a+b)\log((1-\varepsilon)/\varepsilon)\), and let
\[
T_\varepsilon=\frac{H_\varepsilon+|\mathcal I(0)|}{|\kappa|}.
\]
If \(\kappa>0\), then for every \(t>T_\varepsilon\), at least one of
\[
n_{12}(t)>1-\varepsilon,\qquad n_1(t)<\varepsilon,\qquad n_2(t)<\varepsilon
\]
holds. If \(\kappa<0\), then for every \(t>T_\varepsilon\), at least one of
\[
n_{12}(t)<\varepsilon,\qquad n_1(t)>1-\varepsilon,\qquad n_2(t)>1-\varepsilon
\]
holds. The result does **not** assert convergence of any one specified environmental coordinate to an endpoint.

## Assumptions and scope

The governing equations are [1, Eqs. (5)--(10)] with cooperator strategy dynamics defined by its environmentally interpolated payoff matrices, and environmental equations

\[
\begin{aligned}
\dot n_1 &=n_1(1-n_1)((1+\theta_1)x-1),\\
\dot n_2 &=n_2(1-n_2)((1+\theta_2)y-1),\\
\dot n_{12}&=n_{12}(1-n_{12})\left((1+\theta_{12})\frac{x+y}{2}-1\right).
\end{aligned}
\]

The feedback ratios are strictly positive; the mixing parameter satisfies \(0<\delta<1\). The source's payoff inequalities, \(R_0>T_0\), \(S_0>P_0\), \(R_1<T_1\), \(S_1<P_1\), are retained. The result is independent of their particular values. Initial environmental states are strictly between zero and one; strategies may begin anywhere in their closed unit intervals. The smooth vector field leaves the closed state cube invariant and has bounded coefficients, so every such solution exists for all positive time, and an initially interior environmental coordinate never reaches an endpoint in finite time.

## Proof

For any scalar logistic equation \(\dot n=n(1-n)g(t)\) with \(n\in(0,1)\), differentiation gives \(d\ell(n)/dt=g(t)\). Hence in the present model,

\[
\begin{aligned}
\frac{d}{dt}\ell(n_1)&=(1+\theta_1)x-1,\\
\frac{d}{dt}\ell(n_2)&=(1+\theta_2)y-1,\\
\frac{d}{dt}\ell(n_{12})&=\frac{1+\theta_{12}}2(x+y)-1.
\end{aligned}
\]

With the stated positive coefficients \(a,b\), the coefficients of both \(x\) and \(y\) cancel exactly from \(\dot{\mathcal I}\). The remaining constant is

\[
-1+a+b
=\frac{1+\theta_{12}}2\left(\frac1{1+\theta_1}+\frac1{1+\theta_2}\right)-1
=\kappa.
\]

Integrating establishes the affine identity for arbitrary solutions, not merely time averages. Strict positivity of the denominator makes \(\kappa=0\) equivalent to the displayed feedback resonance. If \(\kappa\ne0\), \(\mathcal I\) is unbounded along every forward solution, whereas it is bounded on any compact set whose three environmental coordinates lie strictly inside \((0,1)\). A nonempty compact forward-invariant interior set, a fully interior equilibrium or orbit, or a recurrent interior state would contradict this exact drift. This also rules out compactly supported invariant probability measures in the fully interior environment domain.

For the directed quantitative conclusion, set \(L=\log((1-\varepsilon)/\varepsilon)\). If \(n_{12}\le1-\varepsilon\) and \(n_1,n_2\ge\varepsilon\), then monotonicity of \(\ell\) gives \(\mathcal I\le(1+a+b)L=H_\varepsilon\). If the three reversed inequalities \(n_{12}\ge\varepsilon\) and \(n_1,n_2\le1-\varepsilon\) hold, then \(\mathcal I\ge-H_\varepsilon\). For \(t>T_\varepsilon\) the affine law violates the respective bound and proves the stated union of oriented endpoint neighborhoods.

To demonstrate sharp attainability at resonance, choose
\[
\theta_1=1,\qquad \theta_2=3,\qquad \theta_{12}=5/3,\qquad \delta=1/2,
\]
with depleted and rich payoff matrices
\[
A_0=\begin{pmatrix}2&2\\1&1\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&1\\2&2\end{pmatrix}.
\]
Both matrices satisfy the source's strict payoff inequalities. The payoff difference between cooperation and defection at environment \(n\) equals \(1-2n\), independently of the opponent's strategy. For every \(u\in(0,1)\), the state
\[
\boxed{(x,y,n_1,n_2,n_{12})=(1/2,\,1/4,\,1-u,\,1-u,\,u)}
\]
is therefore an equilibrium: the two strategy payoff differences vanish because each mixed effective environment equals \(1/2\), and all three environmental derivatives vanish because \(x=1/(1+\theta_1)\), \(y=1/(1+\theta_2)\), and \((x+y)/2=1/(1+\theta_{12})\). This example proves existence of fully interior recurrence on the resonant parameter hypersurface, but does not imply that resonance guarantees such recurrence for arbitrary payoffs.

## Verification

The standalone `verify.py` (Python with SymPy, NumPy and SciPy) symbolically checks the affine derivative and the resonant identity, verifies the equilibrium curve exactly for arbitrary symbolic \(u\), and computes the drift for two feedback choices depicted in [1, Fig. 8]. They are

\[
(\theta_1,\theta_2,\theta_{12})=(3,5,8):\quad\kappa=7/8>0,
\]
\[
(\theta_1,\theta_2,\theta_{12})=(3/10,2/5,9/20):\quad\kappa=55/728>0.
\]

Thus neither choice can support a genuinely compact, fully interior periodic or recurrent orbit, regardless of its apparent finite-time oscillations. The script also numerically integrates a separate admissible game and checks the exact linear-drift identity along the resulting trajectory. The numerical test is corroboration, not the proof of the nonrecurrence theorem. Run `python verify.py` after installing `sympy`, `numpy`, and `scipy`.

## Relationship to prior work

Betz, Fu and Masuda [1] establish the five-variable model, classify many equilibria and report apparent oscillatory or aperiodic motion in its general asymmetric regime. Their Table 2 includes some stability inequalities related to the sign of the feedback-resonance expression, but neither their equilibrium table nor the numerical section supplies the payoff-independent affine law, its oriented endpoint selection, or the global exclusion of fully interior recurrent motion for nonresonant feedback ratios. Their three-dimensional equal-feedback reduction admits an equilibrium line, a different, specialized phenomenon.

The equal-feedback three-variable restriction in [1] permits an invariant environmental log-odds difference, but only after equality of community strategies and of their environmental states has been imposed. That restricted invariant does not imply the present five-dimensional affine drift for independent, unequal feedback ratios. Gong, Gao and Cao [2] use one shared environmental variable for a two-population game, while Gong et al. [3] and Liu, Cao and Wu [4] investigate different well-mixed feedback or imitation dynamics; their reported orbit results cannot imply this three-environment log-odds identity. The comparison is about the mathematical implications of the statements, not absence of matching terminology.

## Limitations

The result excludes compact recurrence only when all three environmental coordinates remain strictly interior and \(\kappa\ne0\). It does not classify recurrent dynamics on invariant boundary faces, does not prove which of the oriented faces individually attracts a trajectory, and does not establish recurrence for every resonant parameter choice. It is specific to the three linear-logistic environmental feedback laws in [1]; adding intrinsic resource dynamics, modifying those laws, or changing the meaning of the between-community average may destroy the exact cancellation. A published but unlocated equivalent global drift theorem remains a residual originality possibility; independent validation has not been performed.

## References

[1] K. Betz, F. Fu and N. Masuda, *Evolutionary game dynamics with environmental feedback in a network with two communities*, arXiv:2404.17082, version 1 publicly posted 2024-04-25, version 2 2024-06-07; *Bulletin of Mathematical Biology* 86, article 84 (2024). https://arxiv.org/html/2404.17082v2

[2] L. Gong, J. Gao and M. Cao, *Evolutionary Game Dynamics for Two Interacting Populations in a Co-evolving Environment*, IEEE CDC (2018), DOI:10.1109/CDC.2018.8619801. Author manuscript: https://pure.rug.nl/ws/files/75924983/generated_14387232.pdf

[3] L. Gong, W. Yao, J. Gao and M. Cao, *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, *Automatica* 145, 110536 (2022), arXiv:2205.10734. https://arxiv.org/abs/2205.10734

[4] Y. Liu, L. Cao and B. Wu, *General non-linear imitation leads to limit cycles in eco-evolutionary dynamics*, *Chaos, Solitons & Fractals* 165, 112817 (2022), arXiv:2210.10552. https://arxiv.org/abs/2210.10552
