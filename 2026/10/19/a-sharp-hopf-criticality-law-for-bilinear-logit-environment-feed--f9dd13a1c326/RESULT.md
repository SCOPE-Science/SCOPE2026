# A sharp Hopf-criticality law for bilinear logit–environment feedback games

## Finding
Consider a two-strategy logit learner coupled to a scalar environmental resource. At every nondegenerate interior Hopf point of the bilinear-payoff family defined below, the first Lyapunov coefficient, in the explicitly specified rotation normalization, is
\[
\ell_1=\frac{(r-2)\omega^2-(r+2)}{16s(1-s)},
\qquad r=\frac{a(1-2s)}{as+c}.
\]
Here \(s\) is the equilibrium strategy frequency, \(\omega>0\) is the Hopf frequency, and \(a,c\) are payoff-interaction coefficients. Consequently, Hopf is **supercritical** for every environmental timescale whenever \(-2\le r\le2\). If \(r>2\), its criticality switches from supercritical to subcritical exactly at \(\omega^2=(r+2)/(r-2)\); if \(r<-2\), the switch occurs in the opposite direction at the same positive ratio. At a zero coefficient no generic Hopf or Bautin claim is made.

In the 2023 logit-feedback numerical example of Paarporn (Figure 3), \(r=-1/4\) and
\[
\ell_1=-\frac{81}{1280}(7+9\omega^2)<0
\]
for **every** positive environmental timescale. A second explicit rational-payoff example instead has \(r=12/5\), with a sharp timescale threshold \(\varepsilon_c=82.41624191834188\ldots\) across which the small emergent cycle changes from attracting to repelling.

## Assumptions and scope
Let \(\sigma(z)=(1+e^{-z})^{-1}\), and consider, for arbitrary real \(a,b,c,d\), positive \(\beta,\varepsilon,\kappa\), and \(0<\lambda<\kappa\),
\[
\dot x=\sigma\!\left(\beta[a x n+b x+c n+d]\right)-x,
\qquad \dot n=\varepsilon n(1-n)(\kappa x-\lambda).
\]
The biological state square is \([0,1]^2\). Define \(s=\lambda/\kappa\), \(H=s(1-s)\), \(q=as+c\), and \(p=an_*+b\), with \(n_*\in(0,1)\). Assume \(q<0\), \(p>0\), and that a positive rationality \(\beta_*\) satisfies the two Hopf identities
\[
\beta_*\,[q n_*+bs+d]=\log\frac{s}{1-s},\qquad \beta_*Hp=1.
\]
The first is precisely the interior fixed-point equation, the second is zero trace. The determinant is positive because \(q<0\), \(p>0\), and \(\varepsilon>0\). For conclusions about a one-parameter Hopf *bifurcation as \(\beta\) varies*, additionally assume
\[
\frac{d\,\operatorname{tr}J}{d\beta}
=H\left[b-\frac{a(bs+d)}q\right]\ne0
\]
along the interior equilibrium branch. The sign of the coefficient classifies cycle stability, irrespective of the sign of that derivative; which side of the bifurcation contains the small cycle depends on its sign.

## Proof
**Equilibrium and crossing.** The environment equation forces an interior fixed point to have \(x_*=s\). Its logit equation is \(\beta(qn_*+bs+d)=\log(s/(1-s))\). At a zero-trace point, the Jacobian simplifies to
\[
J=\begin{pmatrix}0&A\\B&0\end{pmatrix},\qquad
A=H\beta_*q=\frac{q}{p}<0,\qquad B=\varepsilon\kappa n_*(1-n_*)>0,
\]
so \(\omega=\sqrt{-AB}>0\). Solving the fixed-point condition for \(n(\beta)\) and differentiating \(\operatorname{tr}J=\beta H(an(\beta)+b)-1\) gives the stated constant crossing derivative.

**Canonical coordinates.** Write \(u=x-s\), \(v=(n-n_*)/k\), where \(k=B/\omega>0\). The linear dynamics is \(\dot u=-\omega v\), \(\dot v=\omega u\). Put \(z=u-\omega v\), \(D=1-6s+6s^2\), and \(C=\beta_*ak=-a\omega/(Hq)\). Taylor expansion of the *actual sigmoid*, using \(\sigma'=H\), \(\sigma''=H(1-2s)\), \(\sigma'''=HD\), gives the homogeneous quadratic and cubic terms of the first component:
\[
\begin{aligned}
f_2(u,v)&=\frac{1-2s}{2H}z^2+HCuv,\\
f_3(u,v)&=\frac{D}{6H^2}z^3+(1-2s)Cuvz.
\end{aligned}
\]
In particular, the mixed cubic factor is \((1-2s)C\), **not** \((1-2s)C/H\). For the second component the nonlinear terms are exactly
\[
g_2(u,v)=\varepsilon\kappa(1-2n_*)uv,\qquad
 g_3(u,v)=-\varepsilon\kappa k\,uv^2.
\]
All remainders in the first component are of degree at least four; the second equation is cubic exactly.

**First Lyapunov coefficient.** For the normalized linear flow \((\dot u,\dot v)=(-\omega v,\omega u)\), use the standard real planar derivative convention
\[
\ell_1=\frac{f_{uuu}+f_{uvv}+g_{uuv}+g_{vvv}}{16}
+\frac{f_{uv}(f_{uu}+f_{vv})-g_{uv}(g_{uu}+g_{vv})-f_{uu}g_{uu}+f_{vv}g_{vv}}{16\omega},
\]
where derivatives are evaluated at \((0,0)\). In this model \(g_{uu}=g_{vv}=g_{uuv}=g_{vvv}=0\). Differentiating \(f_2,f_3\), inserting \(C=-a\omega/(Hq)\), and simplifying with \(r=a(1-2s)/q\) yields the exact identity
\[
16H\ell_1=(r-2)\omega^2-(r+2).
\]
The formula extends to \(s=1/2\) by continuity, since the original derivative expression has no singularity there and \(r=0\). This algebra is reproduced with exact symbolic arithmetic in `verify_hopf.py`; a separate complex-eigenvector tensor contraction checks the same coefficient using \(\operatorname{Re}G_{21}=8\ell_1\) in the stated normalization.

**Signs and bifurcation directions.** Because \(16H>0\), the coefficient is strictly negative for all \(\omega^2>0\) if \(-2\le r\le2\). For \(r>2\) it crosses zero upward at \((r+2)/(r-2)\); for \(r<-2\) it crosses downward at that positive value. If the trace crosses zero nondegenerately and \(\ell_1\ne0\), the planar Hopf theorem gives the corresponding locally attracting (supercritical) or repelling (subcritical) small periodic orbit, on the appropriate side of the rationality threshold. These conclusions are local, not global statements about other cycles or basins.

**Published example: all positive timescales.** The values in Figure 3 of Paarporn (2023) are \(\delta_{TR1}=1/2\), \(\delta_{PS1}=1/4\), \(\delta_{SP0}=-1/2\), \(\delta_{RT0}=3/2\), and \(\theta=4/5\), giving
\[
(a,b,c,d,\kappa,\lambda)=(-9/4,2,1/4,-1/2,9/5,1).
\]
Let \(L_0=\log(5/4)\). Direct substitution gives
\[
\begin{aligned}
s&=5/9,& \beta_*&=\frac{18}{25}(9-5L_0),\\
n_*&=\frac{99-80L_0}{18(9-5L_0)},& r&=-1/4,\\
\omega^2&=\varepsilon\frac{2(99-80L_0)(63-10L_0)}{2025(9-5L_0)},&
\frac{d\operatorname{tr}J}{d\beta}&=25/162>0.
\end{aligned}
\]
These values match the paper's numerical Hopf rationality \(5.6767\ldots\) when rounded. The interior requirements hold, and \(\ell_1=-81(7+9\omega^2)/1280<0\) for *all* \(\varepsilon>0\), not merely the simulated choice \(\varepsilon=0.5\). Thus a locally attracting small cycle appears for \(\beta>\beta_*\) sufficiently close to \(\beta_*\), for each fixed positive \(\varepsilon\).

**Attainable opposite criticality under the game's original payoff assumptions.** With the rational coefficients
\[
(a,b,c,d,\kappa,\lambda)=(10,1/2,-21/2,-1/10,5/4,1),\quad L=\log4,
\]
the Hopf point is interior and has
\[
\begin{aligned}
s&=4/5,& q&=-5/2,&r&=12/5,\\
\beta_*&=\frac{5(25+16L)}{34},&
n_*&=\frac{15-4L}{5(25+16L)},\\
\omega^2&=\varepsilon\frac{(15-4L)(55+42L)}{170(25+16L)},&
\frac{d\operatorname{tr}J}{d\beta}&=34/125>0.
\end{aligned}
\]
The associated paper-style payoff differences are \(\delta_{SP0}=-1/10\), \(\delta_{RT0}=2/5\), \(\delta_{TR1}=1/10\), and \(\delta_{PS1}=53/5\), which satisfy the source's strict payoff assumptions and \(\theta=1/4<1\). Here \(\ell_1=5(\omega^2-11)/32\); hence the sharp timescale threshold is
\[
\varepsilon_c=\frac{1870(25+16L)}{(15-4L)(55+42L)}=82.41624191834188\ldots.
\]
At \(\varepsilon=1\) Hopf is supercritical; at \(\varepsilon=200\) it is subcritical, with a locally repelling small cycle for \(\beta<\beta_*\). At \(\varepsilon=\varepsilon_c\), \(\ell_1=0\) and no claim about higher-order bifurcation type is made.

## Verification
`verify_hopf.py` reconstructs the symbolic coefficient exactly, checks both equilibria, tests positive determinant and sigmoid consistency, and independently contracts quadratic/cubic tensors with complex eigenvectors. It asserts \(\operatorname{Re}G_{21}=8\ell_1\) to numerical tolerance for four source-game timescales and two timescales on opposite sides of the second model's transition. The computations check the displayed algebra, not an infinite enumeration or global orbit classification. Reproduce with Python 3, SymPy and NumPy by running `python verify_hopf.py`.

## Relationship to prior work
Paarporn's 2023 logit-learning feedback game (arXiv:2311.02745v1) derives the equilibrium bifurcation and provides oscillatory simulations; its discussion identifies an explicit first-Lyapunov stability calculation as an outstanding problem. The formula above provides an exact answer, including the formerly untested dependence on resource timescale, and shows that a related rational-payoff game can have either Hopf criticality. The logistic learning analysis in Gavin–Cao–Paarporn (arXiv:2409.05044) treats a static one-dimensional game, with no environmental Hopf mode. Gong–Cao (arXiv:2105.04659) and Gong–Yao–Gao–Cao (arXiv:2205.10734) analyze replicator and replicator–mutator environmental feedback, respectively; their first Lyapunov coefficients concern different behavioral laws and do not imply the bilinear-logit formula.

## Limitations
This is a local Hopf theorem at interior fixed points satisfying the displayed algebraic hypotheses. If \(\ell_1=0\) the coefficient alone does not establish a generalized Hopf/Bautin bifurcation. No global attraction, uniqueness of cycles, or large-amplitude behavior is claimed. The Lyapunov coefficient's magnitude depends on the explicitly chosen normal-form scaling; its sign and the stated bifurcation classification do not. A different payoff law or learning rule requires a new calculation.

## References
1. K. Paarporn, *The madness of people: rational learning in feedback-evolving games*, arXiv:2311.02745v1, first public November 5, 2023. https://arxiv.org/abs/2311.02745
2. R. Gavin, M. Cao, and K. Paarporn, *An Analysis of Logit Learning with the r-Lambert Function*, arXiv:2409.05044. https://arxiv.org/abs/2409.05044
3. L. Gong and M. Cao, *Different Environment Feedback in Fast-slow Eco-evolutionary Dynamics*, arXiv:2105.04659. https://arxiv.org/abs/2105.04659
4. L. Gong, W. Yao, J. Gao, and M. Cao, *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734. https://arxiv.org/abs/2205.10734
