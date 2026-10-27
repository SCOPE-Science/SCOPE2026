# A universal prevalence coboundary and sharp interior-residence threshold for vaccination-risk feedback

## Finding
For the demographic SIR infection process coupled to logistic perceived-vaccination-risk dynamics studied by Liu and Wu [1], there is an *exact finite-time prevalence balance*: with the definitions in the next section, a logarithmic observable \(H\) satisfies
\[
\frac{dH}{dt}=I-I_c,\qquad I_c=\frac{\mu}{\gamma+\mu}\left(\frac1{2+\theta}-\frac1{\mathcal R_0}\right).
\]
Consequently, for every finite \(T>0\),
\[
\frac1T\int_0^T I(t)\,dt=I_c+\frac{H(T)-H(0)}T.
\]
Every compactly supported invariant probability measure strictly inside the positive-infection, interior-risk region has average infection exactly \(I_c\), irrespective of the parameters of the vaccination-payoff response. Such a measure is impossible when \(\mathcal R_0\le2+\theta\). A uniform explicit upper bound on how long any trajectory can remain inside a prescribed positive-infection/interior-risk strip is given below. The threshold is sharp in the existential sense: each \(\mathcal R_0>2+\theta\) permits positive-cost parameters for which a strictly interior endemic equilibrium exists.

## Assumptions and scope
Let \(\mu,\beta,\gamma,\varepsilon_1,\varepsilon_2,\theta\) be positive, with \(0<\varepsilon_1,\varepsilon_2\le1\) in the source's intended range, and let \(C>V_H>V_L>0\). The autonomous five-state system is
\[
\begin{aligned}
\dot S&=\mu(1-x)-\beta SI-\mu S,\\
\dot I&=\beta SI-(\gamma+\mu)I,\\
\dot R&=\mu x+\gamma I-\mu R,\\
\dot x&=\varepsilon_1 x(1-x)\left[\frac{C\beta I}{\beta I+\mu}-V_L-(V_H-V_L)n\right],\\
\dot n&=\varepsilon_2 n(1-n)[1+\theta-(2+\theta)x].
\end{aligned}
\]
The population fractions satisfy \(S,I,R\ge0\), \(S+I+R=1\); \(x,n\in[0,1]\). When the identity is used assume \(I>0\) and \(0<n<1\). These interior conditions are preserved over each finite positive time interval from interior initial data. Set
\[
\mathcal R_0=\frac\beta{\gamma+\mu},\qquad
A=\frac{\mu}{(\gamma+\mu)\varepsilon_2(2+\theta)},\qquad
B=\frac{\mu}{\beta(\gamma+\mu)},
\]
\[
H=A\log\frac{n}{1-n}-B\log I-\frac{S+I}{\gamma+\mu},\qquad
I_c=\frac{\mu}{(\gamma+\mu)(2+\theta)}-\frac\mu\beta.
\]
The identity depends on the SIR and perceived-risk equations, not on the particular rule for \(\dot x\): it remains valid when \(x(t)\in[0,1]\) is any admissible continuous input. The invariant-measure conclusion, in contrast, refers to invariant probabilities of an autonomous flow on compact subsets of the stated interior.

## Proof
**Exact cancellation.** Adding the first two equations and dividing the second by \(I\) gives
\[
\dot S+\dot I=\mu(1-x-S)-(\gamma+\mu)I,\qquad
\frac{\dot I}{I}=\beta S-(\gamma+\mu).
\]
The perceived-risk logistic equation gives
\[
\frac{d}{dt}\log\frac{n}{1-n}=\varepsilon_2[1+\theta-(2+\theta)x].
\]
Substitution in \(\dot H\) cancels both \(x\) and \(S\), leaving
\[
\dot H=I-\frac{\mu}{(\gamma+\mu)(2+\theta)}+\frac\mu\beta=I-I_c.
\]
Integrating this identity proves the formula for every \(T\). No quasi-steady approximation or assumption about the detailed vaccination payoff is involved.

**Stationary and recurrent consequences.** Let \(\nu\) be an invariant Borel probability measure with support contained in a compact invariant subset of \(\{I>0,0<n<1\}\) in the population simplex. Here \(H\), \(\log I\), and \(\log(n/(1-n))\) are bounded continuously differentiable observables, so invariance and differentiation along the flow give \(\int \dot H\,d\nu=0\). Hence \(\int I\,d\nu=I_c\). Invariance of the two log observables separately yields
\[
\int x\,d\nu=\frac{1+\theta}{2+\theta},\qquad
\int S\,d\nu=\frac{\gamma+\mu}{\beta}.
\]
Invariance of \(I\) yields the additional exact incidence balance \(\beta\int SI\,d\nu=(\gamma+\mu)I_c\). Since \(I>0\) on this compact support, \(I_c\) must be strictly positive, equivalent to \(\mathcal R_0>2+\theta\). In particular, when \(\mathcal R_0\le2+\theta\), \(H\) is strictly increasing throughout the stated interior and no compact interior invariant probability, including a periodic orbit or an interior stationary equilibrium, can exist. This argument does **not** rule out long transients or convergence to a boundary subset.

**Explicit residence-time bound.** Fix \(\delta\in(0,\tfrac12)\) with \(\delta>I_c\). Suppose throughout \([0,T]\) that \(I(t)\ge\delta\) and \(\delta\le n(t)\le1-\delta\). Then \(\Delta H=\int_0^T(I-I_c)dt\ge(\delta-I_c)T\). The positive contribution from the logit term is at most \(2A\log((1-\delta)/\delta)\); that from \(-B\log I\) at most \(B\log(1/\delta)\); and that from \(-(S+I)/(\gamma+\mu)\) at most \(1/(\gamma+\mu)\), since all population fractions lie in \([0,1]\). Thus necessarily
\[
T\le T_\delta:=\frac{2A\log((1-\delta)/\delta)+B\log(1/\delta)+1/(\gamma+\mu)}{\delta-I_c}.
\]
For \(\mathcal R_0\le2+\theta\), every positive \(\delta<1/2\) satisfies \(\delta>I_c\); a trajectory therefore cannot stay indefinitely in any one such closed interior strip. The bound is independent of the vaccine costs and of \(\varepsilon_1\).

**Sharpness, without a universal converse.** Let \(\mathcal R_0>2+\theta\) and write \(f_*=1-(2+\theta)/\mathcal R_0\in(0,1)\). Choose \(C=1\), \(V_L=f_*/2\), and \(V_H=(1+f_*)/2\), so \(0<V_L<V_H<C\). Then
\[
S_*=1/\mathcal R_0,\quad I_*=I_c,\quad R_*=1-S_*-I_*,\quad x_*=(1+\theta)/(2+\theta),\quad n_*=f_*
\]
is a strictly interior endemic equilibrium. Indeed, \(\beta I_*/(\beta I_*+\mu)=f_*\), and \(V_L+(V_H-V_L)n_*=f_*\); all five derivatives vanish. The quantity \(R_*\) is positive because \(I_*<\mu/[(\gamma+\mu)(2+\theta)]<1-1/\mathcal R_0\). A rational example is \(\mu=1\), \(\gamma=3\), \(\beta=16\), \(\theta=1\), \(C=10\), \(V_L=1\), \(V_H=3\), with equilibrium \((S,I,R,x,n)=(1/4,1/48,35/48,2/3,3/4)\). These choices establish existence for suitable payoffs above the threshold, not existence for every possible fixed payoff tuple.

## Verification
The accompanying `verify.py` uses exact symbolic simplification to check the cancellation \(\dot H-I+I_c=0\), verifies all five equilibrium equations with rational arithmetic for the explicit sharpness witness, numerically integrates fifteen admissible parameter sets and checks the finite-time integral balance, and checks positive finite upper bounds on one hundred parameter sets at and below the threshold. Running `python verify.py` with packages in `requirements.txt` yields the specified check messages. The tested integral identity had maximum absolute numerical discrepancy under \(10^{-8}\) at the indicated solver tolerances. The universal claims follow from the displayed symbolic algebra and measure-theoretic argument; the finite computations are corroborative, not proofs by enumeration.

## Relationship to prior work
Liu and Wu [1] introduced these coupled SIR, vaccination-behavior, and perceived-risk equations and analyzed equilibrium configurations, bistability, and recurring epidemic waves, including a fast-epidemic reduction. The exact finite-time coboundary, the compact-recurrence mean constraint, and the uniform residence-time bound are not statements identified in the inspected model paper. They apply to the unreduced equations, with no time-scale separation. Doncel, Gast, and Gaujal [2] study optimal timing of vaccination in a different finite-horizon SIR mean-field game without the evolving logistic perceived-risk state; their control and equilibrium results do not directly entail this identity. The positivity requirement and the threshold emerge here from a derived invariant of the joint demographic and opinion feedback, not merely by counting equilibria.

## Limitations
The theorem applies to this exact demographic SIR/perceived-risk coupling with positive infection and interior perceived risk. It is not a statement that infection clears globally below the threshold, nor that general orbits possess limiting time averages: the endpoint term can be unbounded along trajectories approaching \(I=0\) or \(n\in\{0,1\}\). It does not establish a nonconstant recurrent orbit or an endemic equilibrium for arbitrary fixed payoffs above the threshold, and does not imply stochastic epidemic consequences. The novelty comparison is bounded by inspected sources and cannot exclude an unknown equivalent result under different terminology.

## References
[1] Y. Liu and B. Wu, *Co-evolution of Vaccination Behavior and Perceived Vaccination Risk can lead to a Stag-Hunt like Game*, arXiv:2207.05964, first public July 13, 2022; journal version *Physical Review E* 106, 034308 (2022), DOI 10.1103/PhysRevE.106.034308. https://arxiv.org/abs/2207.05964

[2] J. Doncel, N. Gast, and B. Gaujal, *A Mean Field Game Analysis of SIR Dynamics with Vaccination*, *Probability in the Engineering and Informational Sciences* 36, 482–499, DOI 10.1017/S0269964820000522; author-accessible full text: https://josudoncel.github.io/publicat/PEIS_2020.pdf
