# Two-to-three pulse rigidity and the divergence of mean and peak vaccination timing

## Finding

Consider a periodically renewed susceptible population receiving proportional vaccination pulses. There are two distinct exact scheduling phenomena.

**Two-pulse theorem.** For any recovery rate \(\mu>0\), period \(T>0\), and fixed vaccination fractions \(p,q\in(0,1)\), give the first pulse at time zero and the second at \(\tau\in(0,T)\). In the unique disease-free periodic state, the time-average susceptible fraction \(\bar S(\tau)\) is **uniquely minimized at** \(\tau=T/2\), regardless of unequal pulse strengths. Consequently the scalar infected-class Floquet multiplier is uniquely minimized there when its transmission rate is constant and positive. In contrast, the **unique minimizer of the maximum susceptible fraction** occurs at the explicitly determined phase \(\tau_*\) below, and \(\tau_*=T/2\) if and only if \(p=q\). In particular, unequal pulse strengths force disagreement between average-invasion and worst-instantaneous-growth objectives.

**Three-pulse boundary.** Fix any three ordered fractions \(p,q,r\in(0,1)\) and allow the three positive inter-pulse durations, totaling \(T\), to vary. Equal spacing is a stationary point of the mean-susceptibility objective **if and only if** \(p=q=r\). Thus unequal strengths, although compatible with globally optimal equal spacing for two pulses, always make equal spacing nonoptimal for three pulses. This is a local first-variation statement for three pulses, not a global classification of three-pulse minimizers.

## Assumptions and scope

Time is periodic with period \(T>0\), and the disease-free susceptible fraction \(S(t)\in[0,1]\) obeys
\[
\dot S=\mu(1-S)\quad\text{between pulses},\qquad
S(t_i^+)=(1-p_i)S(t_i^-)\quad\text{at pulse }t_i.
\]
Here \(\mu>0\), and every pulse strength \(p_i\) lies strictly between zero and one. Pulse strengths are **fractions of susceptibles currently present**, not fixed counts of vaccine doses delivered. Pulse strengths and their chronological order are fixed while times vary; intervals between distinct pulses are positive. The one-period affine return map contracts by \(e^{-\mu T}\prod_i(1-p_i)\in(0,1)\), hence has a unique globally attracting periodic disease-free state.

Define \(\bar S=T^{-1}\int_0^T S(t)\,dt\), taking pulses to have zero temporal duration. Define \(S_{\max}=\sup_{0\le t<T}S(t)\); since \(\dot S>0\) between pulses, it equals the largest pre-pulse value. For a single rare infected class with constant transmission and removal coefficients \(\beta>0\) and \(\delta>0\), the linearization \(\dot I=(\beta S(t)-\delta)I\) has multiplier \(\exp[T(\beta\bar S-\delta)]\). The peak objective instead minimizes \(\max_t (\beta S(t)-\delta)\). No equivalence of these two epidemiological objectives is presumed.

For two pulses, set \(E=e^{-\mu T}\in(0,1)\), \(x=e^{-\mu\tau}\in(E,1)\), and \(D=1-(1-p)(1-q)E>0\). For three pulses at times \(0,\tau_0,\tau_0+\tau_1\) with \(\tau_0+\tau_1+\tau_2=T\), put \(x=e^{-\mu\tau_0},y=e^{-\mu\tau_1},z=e^{-\mu\tau_2},xyz=E\), and \(D_3=1-(1-p)(1-q)(1-r)E>0\).

## Proof

**Step 1: Two-pulse periodic state.** Write the deficit \(J=1-S\), which decays as \(\dot J=-\mu J\) between pulses and jumps by \(J^+=p+(1-p)J^-\) at a pulse of strength \(p\). Let \(J_A\) and \(J_B\) denote deficits immediately after the pulses of strengths \(p\) and \(q\), respectively. The periodicity equations are
\[
J_A=p+(1-p)(E/x)J_B,\qquad J_B=q+(1-q)xJ_A.
\]
Solving them gives
\[
J_A=\frac{p+(1-p)qE/x}{D},\qquad
J_B=\frac{q+(1-q)px}{D}.
\]
The integrated deficit over one period is
\[
\mu T(1-\bar S)=J_A(1-x)+J_B(1-E/x).
\]
Substitution and exact simplification yield
\[
\boxed{\displaystyle
\bar S(x)=1-\frac{(p+q)(1-E)+2Epq-pq(x+E/x)}{\mu T D}.}
\]
Since \(x+E/x\ge2\sqrt E\), with equality only at \(x=\sqrt E\), it follows for every admissible \(x\) that
\[
\bar S(x)-\bar S(\sqrt E)=\frac{pq}{\mu T D}(x+E/x-2\sqrt E)\ge0,
\]
and equality holds only at \(\tau=T/2\). The positive derivative of the infected-class multiplier with respect to \(\bar S\) transfers the result to invasion.

**Step 2: Peak susceptibility and its exact unique optimizer.** Immediately before the pulse at time \(\tau\) the deficit is \(A(x)=xJ_A\); immediately before the pulse at the next period boundary it is \(B(x)=(E/x)J_B\). Thus
\[
A(x)=\frac{px+(1-p)qE}{D},\qquad
B(x)=\frac{qE/x+(1-q)pE}{D},\qquad
S_{\max}(x)=1-\min\{A(x),B(x)\}.
\]
On \(E<x<1\), \(A\) is strictly increasing and \(B\) strictly decreasing. At \(x=E\), \(A-B=q(E-1)/D<0\); at \(x=1\), \(A-B=p(1-E)/D>0\). Their unique crossing is
\[
\boxed{\displaystyle x_* =\frac{E(p-q)+\sqrt{E^2(p-q)^2+4pqE}}{2p},\qquad \tau_*=-\frac{\log x_*}{\mu}.}
\]
Before the crossing the minimum equals \(A\) and increases, while after it the minimum equals \(B\) and decreases, proving the unique minimax solution. At \(x=\sqrt E\),
\[
A(\sqrt E)-B(\sqrt E)=\frac{(p-q)(\sqrt E-E)}D.
\]
Hence \(x_*=\sqrt E\) precisely when \(p=q\); if \(p>q\), then \(x_*<\sqrt E\) and \(\tau_*>T/2\), with reversed inequality for \(p<q\).

**Step 3: Three-pulse equal-spacing first variation.** Let \(J_0,J_1,J_2\) denote the post-pulse deficits, in chronological order. Solving their cyclic equations gives
\[
J_0=\frac{p+(1-p)rz+(1-p)(1-r)qyz}{D_3},\quad
J_1=q+(1-q)xJ_0,\quad
J_2=r+(1-r)yJ_1,
\]
where \(z=E/(xy)\). All variables are positive, and the open feasible region is \(0<x,y,z<1\) with \(xyz=E\). Define the dimensionless integrated deficit
\[
F(x,y)=J_0(1-x)+J_1(1-y)+J_2(1-z)=\mu T(1-\bar S).
\]
At equal spacing let \(u=E^{1/3}\in(0,1)\), so \(x=y=z=u\). Differentiation **with the constraint** \(z=E/(xy)\) yields the two exact identities
\[
\boxed{\displaystyle
\left.\frac{\partial F}{\partial x}\right|_{x=y=z=u}
=\frac{p(q-r)(u-1)}{D_3},\qquad
\left.\frac{\partial F}{\partial y}\right|_{x=y=z=u}
=\frac{r(q-p)(u-1)}{D_3}.}
\]
Because \(p,r>0\), \(u-1\ne0\), and \(D_3>0\), both components vanish exactly when \(q=r\) and \(q=p\), equivalently \(p=q=r\). Any other triple has a nonzero gradient; moving a sufficiently small distance in its gradient direction increases \(F\), hence strictly decreases \(\bar S\). Such a move stays in the open region of positive gaps. This proves both the stationary characterization and the nonoptimality of equal spacing for unequal strengths. No global characterization for three pulses is asserted.

**Step 4: Exact rational witness of the three-pulse effect.** Choose \(\mu T=3\log2\), \((p,q,r)=(3/4,1/2,1/4)\), and \(E=1/8\). Equal gaps have \((x,y,z)=(1/2,1/2,1/2)\) and give \(F=257/253\). A valid unequal-gap schedule \((x,y,z)=(2/5,1/2,5/8)\) gives \(F=2573/2530\), larger by exactly \(3/2530\). Therefore the unequal schedule has strictly smaller mean susceptibility, by \(1/(2530\log 2)\).

## Verification

The accompanying standalone `verification.py` uses SymPy to check the two-pulse rational identity and pre-pulse deficits, the exact constrained partial derivatives for three pulses, and the exact three-pulse rational witness. It also checks 36 additional numerical two-pulse parameter combinations and a numerical mean-versus-peak split. Run from a directory containing the attached file using `python verification.py`, with SymPy installed.

For an illustrative two-pulse case \((p,q,\mu T)=(0.6,0.2,2)\), the mean-optimal half-period phase has \((\bar S,S_{\max})\approx(0.6676461,0.8551919)\). The peak-optimal phase has \(\tau_*/T\approx0.6692381\) and \((\bar S,S_{\max})\approx(0.6703147,0.8242133)\). Numerical checks only corroborate the fully symbolic arguments; they do not replace proofs over all positive parameters.

## Relationship to prior work

Classical pulse-vaccination SIR modeling and disease-extinction thresholds are established. Terry (2010) studies a metapopulation with one recurring fixed-fraction vaccination pulse **per patch**, not optimization of two or three unequal campaigns within a single patch. Browne, Smith, and Bourouiba (2013) study the coordination of pulses among different regions and seasonal circulation. Their mean-susceptibility comparisons at a *fixed number of vaccinations administered* have a different constraint from the **fixed fractions of currently susceptible persons per campaign** used here; the number of doses delivered by these protocols generally varies as the timing changes. Doutor, Rodrigues, Soares, and Chalub (2015) optimize vaccination effort and infection-risk controls in a general seasonal SIRS model, rather than the sharp exact two-versus-three fixed-strength scheduling statement here.

The claimed addition is restricted to the combined two-pulse universal equal-spacing minimizer, its incompatible unequal-pulse minimax phase, and the three-pulse equal-spacing first-variation obstruction. Elementary affine recurrence, AM–GM, and the scalar Floquet relation are not asserted as new tools. Literature searches and the accessible primary texts did not reveal the same combined phase/boundary theorem. A stronger general optimal-control or impulse-spacing theorem may nevertheless imply it; historical priority is not conclusively established.

## Limitations

This is a deterministic, homogeneous, disease-free, constant-demography and constant-transmission model. Pulses act instantaneously, immunization is immediate and perfect, and each campaign vaccinates a fixed **fraction of susceptible people present**, without a fixed annual dose-budget constraint. The measured peak is the **instantaneous susceptible fraction**, not epidemic peak cases or nonlinear prevalence. The multiplier conclusion applies only to a single scalar infected class with time-independent transmission and removal parameters; it does not extend automatically to structured SEIR or nonlinear dynamics, seasonally varying transmission, vaccine waning, migration, or other constraints. Three-pulse stationary failure at equal spacing is not an exact global optimizer formula. Relevant broad optimal-control literature and older pulse timing articles may contain implications not established by the inspected material.

## References

1. A. J. Terry, “Pulse vaccination strategies in a metapopulation SIR model,” *Mathematical Biosciences and Engineering* **7** (2010), 455–477. DOI: 10.3934/mbe.2010.7.455. Published 2010-04-01. Full text: https://www.aimspress.com/aimspress-data/mbe/2010/2/PDF/1551-0018_2010_2_455.pdf.
2. C. Browne, R. J. Smith, and L. Bourouiba, “From regional pulse vaccination to global disease eradication: insights from a mathematical model of poliomyelitis,” arXiv:1309.0265 (first public version 2013-09-01). https://arxiv.org/abs/1309.0265.
3. P. Doutor, P. Rodrigues, M. C. Soares, and F. A. C. C. Chalub, “Optimal vaccination strategies and rational behaviour in seasonal epidemics,” arXiv:1507.02940 (first public version 2015-07-10). https://arxiv.org/abs/1507.02940.
