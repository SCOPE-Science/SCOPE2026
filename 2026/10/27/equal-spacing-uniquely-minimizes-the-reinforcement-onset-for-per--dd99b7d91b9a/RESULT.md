# Equal spacing uniquely minimizes the reinforcement onset for periodically activated group contagion

## Finding

For a single group of \(n\ge3\) interacting individuals, consider the independent-probability, discrete-time higher-order susceptible–infected–susceptible (SIS) closure defined below. Fix a recovery probability \(0<\mu<1\), a group-adoption probability \(0<\eta\le1\), an integer \(k\ge2\) of group-activation steps per cycle, and an integer \(a\ge1\). Exactly \(ka\) recovery-only steps occur per cycle; their nonnegative integer gaps \(g_1,\ldots,g_k\) after successive activation steps sum to \(ka\). Define

\[
r=1-\mu,\qquad x_*=\frac{n-2}{n-1},\qquad m_n=\frac{(n-2)^{n-2}}{(n-1)^{n-1}},\qquad \eta_* = \frac{r^{-a}-r}{m_n}.\]

The following sharp threshold and strict scheduling separation hold.

1. For \(\eta<\eta_*\), every admissible activation schedule drives every initial probability vector in \([0,1]^n\) to zero. At \(\eta=\eta_*\), every schedule other than the equally spaced one \(g_1=\cdots=g_k=a\) still drives every initial vector to zero.
2. If \(\eta_*\le1\), equal spacing at \(\eta=\eta_*\) has a nonzero group-symmetric periodic orbit, whose probability immediately before every activation is \(x_*\). For \(\eta_*<\eta\le1\), equal spacing has precisely three nonnegative, group-symmetric periodic states, consisting of zero, a lower positive saddle, and a higher positive attractor. All trajectories converge at corresponding activation phases to one of these symmetric periodic states.
3. If \(\eta_*<1\), every fixed nonequally spaced gap vector admits an \(\varepsilon>0\), depending on that vector, such that **all** initial states become extinct for \(\eta_*\le\eta\le\eta_*+\varepsilon\), while equal spacing has an attracting positive periodic state for \(\eta_*<\eta\le1\). Thus equal spacing is the **unique** gap arrangement attaining the smallest possible reinforcement threshold for positive periodic activity; the inequality is strict for every other arrangement. If \(\eta_*>1\), no physically admissible reinforcement strength supports a positive periodic orbit under any schedule.
4. Every solution becomes exponentially group-synchronized, whatever the gaps. The threshold \(\eta_*\) strictly increases with group size \(n\).

For an exact example, take a three-person group, \(\mu=1/10\), two activations, and two recovery-only steps per cycle. The critical value is \(\eta_*=38/45\). With gap vector \((1,1)\), the pre-activation state \((1/2,1/2,1/2)\) is periodic at this value; with gaps \((0,2)\) every initial state instead converges to zero. For this same initial state the nonuniform cycle returns \((8081/16200,8081/16200,8081/16200)\), a strict reduction of \(19/16200\) per coordinate.

There is also a sharp group-size cutoff: at \(\mu=1/100\), \(a=2\), and \(\eta=1/2\), equal spacing is bistable for precisely \(3\le n\le7\); for \(n\ge8\), no schedule with the same activation count and recovery-only budget supports a positive periodic orbit.

## Assumptions and scope

A single complete \(n\)-person group activates intermittently. All lower-order transmission probabilities are set to zero, while a susceptible participant adopts with probability \(\eta\) on an active step only when all other participants are active/infected. Adoption is subsequently reversible by recovery with probability \(\mu\) per step. This is a deterministic *individual-probability closure*, not the exact joint-state Markov chain of a finite stochastic epidemic. Conditional-independence products specify the closure.

Write \(p=(p_1,\ldots,p_n)\in[0,1]^n\). On an active step and a recovery-only step, respectively, set

\[
F_i(p)=r p_i+\eta(1-p_i)\prod_{j\ne i}p_j,\qquad R_i(p)=r p_i.
\]

One cycle applies an active update followed by \(g_1\) recovery-only updates, then an active update followed by \(g_2\), and so on. These maps preserve \([0,1]^n\). A positive periodic orbit means strictly positive pre-activation probabilities at the given activation phases, repeating after the complete cycle. Zero remains an attracting state; positive periodicity is a distinct nonlinear phenomenon and does not mean almost-sure indefinite survival in a finite stochastic SIS process.

## Proof

**1. Universal transverse contraction.** For distinct participants \(i,j\), direct cancellation yields the exact identity

\[
F_i(p)-F_j(p)=\left(r-\eta\prod_{\ell\notin\{i,j\}}p_\ell\right)(p_i-p_j).
\]

Because \(0<r<1\), \(0<\eta\le1\), and every component lies in \([0,1]\), the difference multiplier has absolute value at most \(q=\max\{r,1-r\}<1\). Each silent step multiplies differences by \(r\). Thus the maximum coordinate separation contracts by at most \(q^k r^{ka}<1\) per cycle, irrespective of the gap arrangement. Every orbit asymptotically synchronizes, and every period-one state of the cycle map is exactly group-symmetric.

**2. Product bound and equality rigidity.** Along the invariant symmetric diagonal, one active update multiplies a positive probability \(x\) by

\[
G(x)=r+\eta x^{n-2}(1-x).
\]

The function \(x^{n-2}(1-x)\) on \([0,1]\) has the unique maximum \(m_n\) at \(x_*\). If \(x_1,\ldots,x_k>0\) are the pre-activation values of a positive symmetric periodic orbit, then

\[
1=\prod_{j=1}^k\frac{x_{j+1}}{x_j}=r^{ka}\prod_{j=1}^k G(x_j)\le r^{ka}(r+\eta m_n)^k.
\]

Hence \(\eta\ge\eta_*\). At equality \(\eta=\eta_*\), all the factors must attain their individual maxima, so \(x_j=x_*\) for every \(j\). Each step equation \(x_{j+1}=r^{g_j}G(x_j)x_j\) then requires \(r^{g_j}(r+\eta_*m_n)=1\). Since \(r+\eta_*m_n=r^{-a}\) and \(r\in(0,1)\), necessarily \(g_j=a\) for all \(j\). This proves unique threshold attainment.

**3. Extinction without positive periodic points.** Let \(P_{g,\eta}\) be the continuous scalar full-cycle map on the symmetric diagonal. The previous product bound gives \(P_{g,\eta}(x)<x\) for every \(x>0\) when \(\eta<\eta_*\), and also when \(\eta=\eta_*\) with nonuniform gaps. This scalar strict inequality implies extinction even from asymmetric initial states. Indeed, transverse contraction implies that the coordinate mean at successive cycle starts, \(u_t\), satisfies \(u_{t+1}=P_{g,\eta}(u_t)+e_t\) with \(e_t\to0\) exponentially. For each fixed \(\delta>0\), continuity gives a strictly positive lower bound for \(x-P_{g,\eta}(x)\) on \([\delta,1]\). Eventually, the mean decreases by a fixed amount whenever it lies above \(\delta\). Once it falls below \(\delta\), its next value is below \(\delta+o(1)\), and it cannot sustain excursions above \(2\delta\). Since \(\delta\) is arbitrary, \(u_t\to0\), and contraction forces all coordinates to zero.

For fixed nonuniform gaps at \(\eta=\eta_*\), the continuous quotient \(P_{g,\eta}(x)/x\) is strictly below one on the compact interval \([0,1]\), extending continuously at zero with value \(r^{k+ka}<1\). Its maximum is therefore strictly less than one. Continuity of the quotient in \(\eta\) uniformly on that interval preserves this inequality for an open right-neighborhood of \(\eta_*\). The same extinction argument proves the strict gap above threshold.

**4. Exact positive branch for uniform gaps.** When every gap equals \(a\), the phase-to-phase map along the diagonal is

\[
H(x)=r^a F(x)=r^{a+1}x+\eta r^a x^{n-1}(1-x).
\]

Here \(F(x)=rx+\eta x^{n-1}(1-x)\) is the scalar active update. A nonzero fixed point of \(H\) satisfies

\[
x^{n-2}(1-x)=\frac{r^{-a}-r}{\eta}.
\]

The left side increases up to \(x_*\) and decreases thereafter. Consequently there is no positive root below \(\eta_*\), one double root at equality, and exactly two distinct positive roots \(x_-<x_*<x_+\) above it. The full cycle repeats this single-pulse map \(k\) times. After one single-pulse period, all components are at most \(r^a\). On \([0,r^a]^n\), the single-pulse map has nonnegative partial derivatives, because its diagonal partial is at least \(r^a(r-\eta r^{a(n-1)})>0\) for \(a\ge1\), \(n\ge3\). Its scalar restriction \(H\) is strictly increasing, and hence has no nontrivial periodic scalar cycles. The same transverse contraction plus a one-dimensional barrier argument proves that every vector orbit converges to one of the fixed points of \(H\): if its mean had distinct liminf and limsup, choosing a nonfixed intermediate level would contradict the eventual impossibility of crossing that level against the sign of \(H(x)-x\). Thus no other attracting cycles are omitted.

At a positive fixed point, the longitudinal derivative and the transverse multipliers (the latter with multiplicity \(n-1\)) are

\[
\lambda_{\parallel}=1+\eta r^a x^{n-2}\big[(n-2)-(n-1)x\big],\qquad
\lambda_{\perp}=r^a(r-\eta x^{n-2}).
\]

The lower root has \(\lambda_{\parallel}>1\) and \(|\lambda_{\perp}|<1\); the upper root has \(0<\lambda_{\parallel}<1\) and \(|\lambda_{\perp}|<1\). Zero has multiplier \(r^{a+1}<1\). At equality the positive branch has longitudinal multiplier one and transverse contraction, as appropriate for a fold.

**5. Group-size boundary.** For \(0<x<1\), increasing \(n\) strictly decreases \(x^{n-2}(1-x)\); therefore its positive maximum \(m_n\) strictly decreases and \(\eta_*\) strictly increases. With \(r=99/100\), \(a=2\), and \(\eta=1/2\), the required comparison is

\[
\frac{6^6}{7^7}<\frac{29701}{490050}<\frac{5^5}{6^6}.
\]

The middle expression equals \((1-r^3)/(\eta r^2)\); the two endpoints are respectively \(m_8\) and \(m_7\). This proves the claimed sharp size cutoff.

## Verification

The included standalone Python program `verify.py` recomputes cycle maps from the individual active and silent updates, tests the exact difference contraction on \(630\) randomized schedules, checks the rational two-pulse threshold and the exact \(19/16200\) clustered-sequence discrepancy, verifies the group-size inequality with exact fractions, and compares trajectories near the bifurcation. Its observed output is `CHECK_OK`. These finite tests are supplementary: the all-parameter and all-initial-state statements follow from the analytical proof above.

## Relationship to prior work

Iacopini, Petri, Barrat, and Latora (2018/2019) introduced simplicial social contagion, higher-order activation rules, and static mean-field bistability. Chowdhary, Kumar, Cencetti, Iacopini, and Battiston (2021) extended discrete microscopic-probability updates to temporal simplicial networks and studied the effect of refreshing and correlating random contacts on epidemic onset. Malizia and collaborators (2023) developed a continuous-time pair-based approximation for static higher-order contagion. Ferraz de Arruda, Aleta, and Moreno (2024) reviewed these related closures and noted limited analytical understanding of temporality.

The present theorem concerns **deterministic periodic allocation of a fixed number of full-group activation events and fixed total silent time**, including an exact optimization over all integer gap vectors, a strict uniqueness comparison, and synchronization from arbitrary heterogeneous node probabilities. None of the specific source results inspected derives this scheduling optimum. The static homogeneous fixed-point polynomial alone does not compare nonlinear compositions of different temporal schedules. No claim is made that literature searches establish absolute publication priority.

## Limitations

The findings apply only to one homogeneous all-or-nothing higher-order group with no lower-order transmission, independent-probability closure, time-homogeneous recovery and active transmission probabilities, at least two group activations, and a silent-step budget divisible by the number of activations. They do not establish an optimal ordering for uneven integer budgets, arbitrary multiple groups, a stochastic contact process, exact finite-population persistence, or the threshold for every nonequally spaced schedule above the onset gap. Finite stochastic SIS systems with an absorbing healthy state may still become extinct almost surely. Independent external validation has not been performed.

## References

1. I. Iacopini, G. Petri, A. Barrat, V. Latora, *Simplicial models of social contagion*, arXiv:1810.07031 (first public 16 October 2018), https://arxiv.org/abs/1810.07031 .
2. S. Chowdhary, A. Kumar, G. Cencetti, I. Iacopini, F. Battiston, *Simplicial contagion in temporal higher-order networks*, arXiv:2105.04455 (first public 10 May 2021), https://arxiv.org/html/2105.04455v1 .
3. F. Malizia et al., *A pair-based approximation for simplicial contagion*, arXiv:2307.10151 (first public 19 July 2023), https://arxiv.org/abs/2307.10151 .
4. G. Ferraz de Arruda, A. Aleta, Y. Moreno, *Contagion dynamics on higher-order networks*, arXiv:2402.14938 (first public 22 February 2024), https://arxiv.org/html/2402.14938v1 .
