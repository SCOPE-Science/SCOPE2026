# Exact two-cycle invasion threshold and the failure of mean-game prediction in a harvested-resource evolutionary game

## Finding
Consider the discrete eco-evolutionary resource game below, with its two standard strategy update rules. On the all-defector boundary, a stable positive resource period-two orbit has an **exact transverse invasion multiplier**
\[
\Lambda_C=\frac{\alpha^2+(\mu+1)(\mu-2)\alpha\sigma+(\mu+1)\sigma^2}{\mu^2}.
\]
Here \(\alpha\) is the depleted-resource cooperator-versus-defector payoff, \(\sigma\) the corresponding resource-rich payoff, and \(\mu\) the net resource growth rate under all-defector harvesting. This formula is identical for the type-I and type-II discrete replicator update rules. A unique critical value \(\alpha_* >1\), specified exactly below, separates local attraction of the all-defector resource two-cycle (\(\Lambda_C<1\)) from its transverse instability (\(\Lambda_C>1\)); at equality the linear transverse test is inconclusive.

The conventional *mean-game* substitution at the average resource state has a strictly smaller threshold \(\alpha_{\mathrm{mean}}<\alpha_*\). Thus there is an open, physically admissible parameter region where the mean game predicts that rare cooperators invade but the **actual resource two-cycle attracts sufficiently small cooperator perturbations**. An exact rational parameter example is given below.

## Assumptions and scope
Let \(x\in[0,1]\) be the fraction of low-harvesting cooperators and \(n\in[0,1]\) the normalized resource. Fix
\[
3<\mu<1+\sqrt6,\qquad d>0,\qquad (\mu+d)^2<4\mu.
\]
For harvesting parameters \(e_L>0\), \(e_H=e_L+d\), and intrinsic resource growth \(r=e_H+\mu\), the resource map of Mondal--Ray--Chakraborty reduces precisely to
\[
n'=\mu n(1-n)+d x n.
\]
For payoff parameters \(1<\alpha<2\), \(0<\sigma<1\), \(1<T_0<2\), \(2<T_1<3\), write
\[
S(n)=(1-n)\alpha+n\sigma,\qquad
T(n)=(1-n)T_0+nT_1,
\]
\[
U(n)=\begin{pmatrix}2&S(n)\\T(n)&1\end{pmatrix},\qquad
f_C(x,n)=2x+S(n)(1-x),\quad f_D(x,n)=T(n)x+1-x.
\]
The two discrete-time strategy updates, each coupled to the same resource map, are
\[
\begin{aligned}
\text{type I:}\quad &x'=x+x(1-x)(f_C-f_D),\\
\text{type II:}\quad &x'=\frac{x f_C}{x f_C+(1-x)f_D}.
\end{aligned}
\]
All stated parameter inequalities are strict, and \(x,n\) refer to states at the same discrete time. Both maps preserve \([0,1]^2\): the payoff difference \(f_C-f_D\) lies between \(-1\) and \(1\), all entries of \(U(n)\) are positive, and the resource parabola has nonnegative values and maximum below \(1\) for every \(x\in[0,1]\). The game is of evolutionary-game type (MSC2020 91A22).

## Proof
**Step 1: the resident resource cycle.** On the invariant all-defector edge \(x=0\), the resource map is the logistic map \(F(n)=\mu n(1-n)\). For \(\mu>3\), the two points
\[
n_\pm=\frac{\mu+1\pm\sqrt{(\mu-3)(\mu+1)}}{2\mu}
\]
form its unique nonfixed real period-two orbit. They lie strictly in \((0,1)\), and
\[
n_-+n_+=\frac{\mu+1}{\mu},\qquad
n_-n_+=\frac{\mu+1}{\mu^2},\qquad
(1-n_-)(1-n_+)=\frac1{\mu^2}.
\]
The longitudinal multiplier of the two-step return map is
\[
\Lambda_n=F'(n_-)F'(n_+)=4+2\mu-\mu^2.
\]
The parameter interval \(3<\mu<1+\sqrt6\) is precisely the strict stable two-cycle range \(-1<\Lambda_n<1\) following the first logistic flip.

**Step 2: triangular Jacobians and exact invasion threshold.** At every state \((0,n)\), either strategy update has derivative \(\partial x'/\partial x=S(n)\) and \(\partial x'/\partial n=0\). Thus, in the ordered coordinates \((x,n)\), the one-step Jacobian is lower triangular with diagonal \((S(n),\mu(1-2n))\). Multiplying the two Jacobians gives transverse multiplier \(S(n_-)S(n_+)\). Expanding it with the symmetric identities in Step 1 yields
\[
\begin{aligned}
S(n_-)S(n_+)
&=\alpha^2(1-n_-)(1-n_+)\\
&\quad+\alpha\sigma[n_-(1-n_+)+n_+(1-n_-)]\\
&\quad+\sigma^2n_-n_+\\
&=\frac{\alpha^2+(\mu+1)(\mu-2)\alpha\sigma+(\mu+1)\sigma^2}{\mu^2}.
\end{aligned}
\]
This strictly increases with \(\alpha>0\). Its value at \(\alpha=1\) is strictly less than \(1\) since \(0<\sigma<1\) and both resource states are positive; it tends to infinity as \(\alpha\to\infty\). Hence its unique positive crossing \(\alpha_*>1\) is
\[
\alpha_* =\frac{-(\mu+1)(\mu-2)\sigma+\sqrt{(\mu+1)^2(\mu-2)^2\sigma^2+4[\mu^2-(\mu+1)\sigma^2]}}{2}.
\]
Within the physically admissible interval \(1<\alpha<2\), the two-cycle is locally asymptotically attracting exactly when \(\alpha<\alpha_*\); when \(\alpha>\alpha_*\), it is a hyperbolic saddle of the two-step return map, with a positive transverse multiplier exceeding \(1\). At \(\alpha=\alpha_*\) no nonlinear attraction or bifurcation type is asserted.

**Step 3: strict gap with mean-game invasion.** The average cycle resource is
\[
\bar n=\frac{n_-+n_+}{2}=\frac{\mu+1}{2\mu}.
\]
Substituting \(\bar n\) into the resource-dependent payoff gives the mean-game cooperator multiplier \(\bar S=(1-\bar n)\alpha+\bar n\sigma\). It crosses \(1\) at
\[
\alpha_{\mathrm{mean}}=\frac{2\mu-(\mu+1)\sigma}{\mu-1}>1.
\]
The exact identity
\[
\Lambda_C=\bar S^2-
\frac{(\alpha-\sigma)^2(\mu-3)(\mu+1)}{4\mu^2}
\]
shows that \(\Lambda_C<1\) when \(\alpha=\alpha_{\mathrm{mean}}\). Monotonicity therefore gives
\[
\alpha_{\mathrm{mean}}<\alpha_*.
\]
For \(\sigma>2/(\mu+1)\), also \(\alpha_{\mathrm{mean}}<2\). Hence every \(\alpha\) in the nonempty interval
\[
\alpha_{\mathrm{mean}}<\alpha<\min\{2,\alpha_*\}
\]
produces an admissible, attracting resident two-cycle whose *mean-game* test incorrectly indicates cooperator invasion. This is an exact arithmetic-mean versus geometric-growth discrepancy; no probabilistic assumption about phase sampling is used.

**Step 4: an exact admissible example.** Set
\[
\begin{gathered}
(e_L,e_H,r)=(1,11/10,43/10),\qquad\mu=16/5,\qquad d=1/10,\\
(\alpha,\sigma,T_0,T_1)=(9/5,3/5,19/10,21/10).
\end{gathered}
\]
The strict physical inequality holds: \((\mu+d)^2=1089/100<64/5=4\mu\). The resource orbit has
\[
n_\pm=\frac{21\pm\sqrt{21}}{32},\qquad
\bar S=\frac{81}{80}>1.
\]
The two exact return multipliers are
\[
\boxed{\Lambda_C=\frac{1593}{1600}<1,\qquad \Lambda_n=\frac4{25}<1.}
\]
Therefore the period-two orbit attracts an open neighborhood in the two-dimensional biological state rectangle for **both** replicator updates, contrary to the one-state mean-game invasion verdict. The threshold for this example is \(\alpha_{\mathrm{mean}}=97/55\) and \(\alpha_*=(-189+8\sqrt{2689})/125\), with \(97/55<9/5<\alpha_*<2\).

## Verification
The accompanying standalone file `verify.py` checks the exact symmetric-root identity, the closed-form multiplier, and the variance correction symbolically using SymPy. It also checks the rational example exactly and numerically verifies the invariant rectangle on a finite grid and contraction from a small positive cooperator perturbation for each of the two updates. Execute `python verify.py` with SymPy installed. The printed exact values are \(\Lambda_C=1593/1600\), \(\Lambda_n=4/25\), and \(\bar S=81/80\). Grid tests and finite trajectories are *illustrative*, not proofs of global invariance or asymptotic stability; those claims follow from Steps 1--4.

## Relationship to prior work
Mondal, Ray and Chakraborty introduced precisely these coupled harvested-logistic resource and discrete replicator maps, investigated hypochaotic/periodic regimes, and proposed replacing the fluctuating resource state by its time average when predicting transverse stability (see their Section III.2 and Table 1). The present result gives a closed-form exact period-two criterion common to both discrete strategy updates and identifies a nonempty domain where mean substitution and true stability differ. Their numerical figures and fixed-point stability calculations do not imply this threshold or its strict gap. Mukhopadhyay and Chakraborty study evolutionary stability of cycles in *autonomous strategy-only* discrete replicator maps, not the resident harvested-resource two-cycle and its cooperator invasion multiplier. The usual Floquet-product principle and classical logistic two-cycle formulas are established tools; novelty is not claimed for those general principles in isolation.

## Limitations
The result is local to a period-two resource cycle on the all-defector boundary. It does not assert global defector fixation, global two-cycle attraction, existence of an interior cycle after transverse loss of stability, or any sharp threshold for chaotic or higher-period resource attractors. The equality \(\alpha=\alpha_*\) is nonhyperbolic transversely and is excluded from the attraction/instability dichotomy. The parameter regime \(3<\mu<1+\sqrt6\), positive payoff restrictions, and both explicitly stated replicator rules are essential. Although the cited literature and research records were compared, an equivalent unindexed result remains a residual originality risk; independent assessment is outstanding.

## References
1. S. S. Mondal, A. Ray and S. Chakraborty, *Hypochaos prevents tragedy of the commons in discrete-time eco-evolutionary game dynamics*, arXiv:2401.12245v1, first publicly posted 2024-01-20. https://arxiv.org/abs/2401.12245 . Sections II--III, in particular equations (3), (13), (21), (23), the period-doubling results and the mean-game proposal in Section III.2.
2. A. Mukhopadhyay and S. Chakraborty, *Periodic Orbit can be Evolutionarily Stable: Case Study of Discrete Replicator Dynamics*, arXiv:2102.11034, first publicly posted 2021-02-17. https://arxiv.org/abs/2102.11034 . Autonomous strategy-only replicator cycles.
3. S. D. Mylius and O. Diekmann, *The Resident Strikes Back: Invader-Induced Switching of Resident Attractor*, Journal of Theoretical Biology **211** (2001), 297--311. The abstract identifies the broader significance of phase-dependent invasion in periodic environments; no implication of the present model-specific threshold is claimed. https://sido.mylius.nl/pubrstrb.html .
