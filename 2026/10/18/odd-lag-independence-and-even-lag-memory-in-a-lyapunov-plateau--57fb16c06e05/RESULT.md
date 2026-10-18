# Odd-lag independence and even-lag memory in a Lyapunov plateau

## Finding

For each real parameter \(3\le\beta<9/2\), let
\[
T_\beta(x)=\begin{cases}x+2,&x\le0,\\ \beta-2x,&x>0,\end{cases}
\qquad -\beta\le x\le\beta.
\]
Take the absolutely continuous invariant probability \(\mu_\beta\) with the explicit density in [1, Appendix A], and let \(X\sim\mu_\beta\). Write \(J_n=\mathbf 1_{\{T_\beta^n(X)>0\}}\), for integers \(n\ge0\), and \(C_\beta(n)=\operatorname{Cov}(J_0,J_n)\). Then the following **combined correlation-phase theorem** holds.

First, \(\mathbb P(J_n=1)=2/3\) for every \(n\ge0\), whereas the exact one-lag covariance is
\[
\boxed{C_\beta(1)=\begin{cases}
(\beta-4)/18,&3\le\beta\le4,\\
(\beta-4)/54,&4\le\beta<9/2.
\end{cases}}
\]
Thus the first-lag correlation changes sign exactly once, at the parameter \(\beta=4\), despite the constant Lyapunov exponent \((2/3)\log2\) throughout the stated range.

At this distinguished parameter the **complete all-lag covariance law** is
\[
\boxed{C_4(n)=\begin{cases}
0,&n\text{ odd},\\
\dfrac29\left(-\dfrac12\right)^{n/2},&n\text{ even},
\end{cases}\qquad n=0,1,2,\ldots .}
\]
Since each \(J_n\) is Bernoulli with the same success probability, every pair of observations at an odd time separation is independent. At every positive even separation the pair is dependent, with alternating-sign covariance. In particular, the stationary binary process is **not independent across all times**: \(C_4(2)=-1/9\), and the block \((J_0,J_1,J_2)=(0,0,0)\) has probability zero, whereas an independent Bernoulli process with success probability \(2/3\) would assign probability \(1/27\).

## Assumptions and scope

The map is considered on its invariant interval \([-\beta,\beta]\); the initial condition is distributed according to the **particular absolutely continuous invariant probability** \(\mu_\beta\) tabulated in [1]. The statement does not concern arbitrary invariant measures, including measures supported on periodic orbits. Changes at discontinuity points or finitely many density endpoints affect neither the distribution nor any stated correlation.

For the proof, the densities of [1, Appendix A, equations (56)--(59)] can be written as follows, with every interval open and with zero probability assigned to its finitely many endpoints. For \(3<\beta<4\), the successive breakpoints are
\[
-\beta,\quad 2-\beta,\quad \beta-4,\quad\beta-2,\quad2,\quad\beta
\]
with respective interval-density values
\[
\frac1{18},\quad\frac19,\quad\frac29,\quad\frac13,\quad\frac19.
\]
For \(4<\beta<9/2\), the successive breakpoints are
\[
-\beta,\quad3\beta-16,\quad2-\beta,\quad3\beta-14,\quad4-\beta,
\quad\beta-4,\quad6-\beta,\quad2,\quad8-\beta,\quad\beta
\]
with interval-density values
\[
\frac1{27},\quad\frac1{18},\quad\frac5{54},\quad\frac19,\quad\frac4{27},
\quad\frac29,\quad\frac7{27},\quad\frac19,\quad\frac2{27}.
\]
At \(\beta=4\), the four intervals \((-4,-2),(-2,0),(0,2),(2,4)\) have densities \(1/18,1/9,2/9,1/9\), respectively. At \(\beta=3\), the limiting density is explicitly covered in [1, equation (56)]. The densities above are given for transparency, but the results below are also rechecked against the Perron--Frobenius equation by the exact-arithmetic companion script.

## Proof

**1. Marginal stationarity and first lag.** The known probability \(\mu_\beta\) is invariant and satisfies \(\mu_\beta((0,\beta))=2/3\) for \(3\le\beta<9/2\), as established in [1, Appendix A]. This gives stationary success probability \(2/3\). The event that both first two observations equal one is, apart from a null set, exactly the interval
\[
\{J_0=1,J_1=1\}=\{0<X<\beta/2\},
\]
because \(x>0\) entails \(T_\beta(x)=\beta-2x\). Hence
\[
C_\beta(1)=\mu_\beta((0,\beta/2))-\frac49.
\]
For \(3<\beta<4\), the cut \(\beta/2\) is between \(\beta-2\) and \(2\). The source density gives
\[
\mu_\beta((0,\beta/2))=
\frac29(\beta-2)+\frac13\left(\frac\beta2-(\beta-2)\right)
=\frac{\beta+4}{18}.
\]
For \(4<\beta<9/2\), we have the strict ordering
\[
0<\beta-4<6-\beta<2<\beta/2<8-\beta.
\]
Integrating the successive source density values gives
\[
\begin{aligned}
\mu_\beta((0,\beta/2))
&=\frac4{27}(\beta-4)+\frac29(10-2\beta)
 +\frac7{27}(\beta-4)+\frac19\left(\frac\beta2-2\right)\\
&=\frac{\beta+20}{54}.
\end{aligned}
\]
At \(\beta=3\) and \(\beta=4\), direct integration of the endpoint density agrees with the adjacent formulas. Subtracting \(4/9\) proves the full sign-changing one-lag law.

**2. The natural four-state Markov partition at \(\beta=4\).** Define consecutive cells
\[
A=(-4,-2),\qquad B=(-2,0),\qquad C=(0,2),\qquad D=(2,4).
\]
Their invariant probabilities, calculated from the preceding constant densities, are \(\pi=(1,2,4,2)/9\). Each branch maps a whole cell linearly across complete target cells:
\[
T_4(A)=B,\quad T_4(B)=C,\quad T_4(C)=C\cup D,\quad T_4(D)=A\cup B
\]
(up to endpoints), with constant absolute slope on each source cell. More explicitly, the slopes on \(A,B,C,D\) are \(1,1,-2,-2\), respectively. Conditional Lebesgue measure on a source cell is therefore pushed forward to uniform measure on its image; conditional on any target cell it remains uniform. Induction over finite cell itineraries proves the state process is a stationary Markov chain with row-stochastic transition matrix
\[
P=\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&1/2&1/2\\
1/2&1/2&0&0
\end{pmatrix},\qquad \pi P=\pi.
\]
(The stationary measure of this Markov chain is precisely the cell distribution computed from the source density.)

The branch indicator is the state function \(f=(0,0,1,1)^\mathsf T\). Centering by its stationary mean yields
\[
v=f-\frac23\mathbf1=\left(-\frac23,-\frac23,\frac13,\frac13\right)^\mathsf T,
\qquad
Pv=\left(-\frac23,\frac13,\frac13,-\frac23\right)^\mathsf T.
\]
Direct multiplication gives the two **exact identities**
\[
P^2v=-\frac12v,\qquad
\sum_{i\in\{A,B,C,D\}}\pi_i v_i(Pv)_i=0.
\]
By the Markov property,
\[
C_4(n)=\sum_i\pi_i v_i(P^nv)_i.
\]
For every integer \(k\ge0\), the eigenvector relation \(P^{2k}v=(-1/2)^kv\) and \(P^{2k+1}v=(-1/2)^kPv\) gives
\[
C_4(2k)=\left(-\frac12\right)^k\sum_i\pi_i v_i^2
=\frac29\left(-\frac12\right)^k,
\qquad C_4(2k+1)=0.
\]
This proves the **infinite-lag** assertion, rather than extrapolating it from a finite computation.

**3. Independence assertions.** If two Bernoulli random variables \(U,V\) share success probability \(2/3\), their entire joint distribution is fixed by \(\mathbb P(U=V=1)\). Zero covariance is equivalent to this joint probability equalling \(4/9\), which in turn is exactly pairwise independence. Thus the zero odd-lag covariances prove independent pairs at all positive odd lags; the nonzero even-lag covariances prove dependence for every positive even lag. On the other hand, whenever \(x<0\), the first negative branch adds \(2\) to the state. Since the initial invariant interval lies above \(-4\), three consecutive negative-branch visits are impossible, proving \(\mathbb P(J_0=J_1=J_2=0)=0\). The observations are therefore not mutually independent.

## Verification

Run `python3 CHECKER.py` from the directory containing this document and the companion script. No third-party libraries or downloaded input files are needed. The script uses Python rational arithmetic and checks:

1. The two entire open parameter chambers \((3,4)\) and \((4,9/2)\) satisfy the exact Perron--Frobenius stationarity identity, normalization, success probability, and first-lag formulas. It enumerates every parameter where any affine density/image endpoint or the threshold \(\beta/2\) could exchange order; between those breakpoints, each identity is affine in \(\beta\), and is verified at two distinct rational values.
2. The four-cell probability vector and Markov transition matrix are stationary, \(P^2v=-v/2\), and the required centered lag-one dot product vanishes exactly.
3. The stated all-lag formula agrees with exact matrix iterates for lags \(0\) through \(30\); moreover, an independent subdivision of initial-condition intervals into exact iterated branches reproduces the joint probabilities through lag \(12\).

The successful script emits `VERIFY_OK`. The analytical matrix identity, not finite brute-force enumeration, establishes all infinitely many lags. The endpoint parameter \(\beta=3\) is covered by the explicit density [1, equation (56)] and the parameter \(\beta=4\) by the four-cell proof above; the script's open-chamber checks do not substitute for these separate boundary arguments.

## Relationship to prior work

Botella-Soler, Oteo, Ros and Glendinning [1] define this map, derive the piecewise constant densities in Appendix A and prove the constant Lyapunov exponent. Their manuscript analyzes kneading invariants and entropy but does not state the one-lag sign transition or the four-state all-lag odd/even binary correlation law derived here. The density formulas and constant Lyapunov value are **prior results**, not new claims.

Bruin, Carminati, Marmi and Profeti [2] revisit the same affine family in conjugate coordinates, establish matching mechanisms and characterize entropy monotonicity/plateaux. The corresponding theorems concern entropy and invariant-density structure, not the branch-sign autocovariance or the distinction between odd- and even-lag independence. The exact correlation theorem is a new quantitative deduction whose implication does not follow merely from their entropy statements.

An earlier analysis of this same family on a *different parameter interval* \(2<\beta<3\) established a branch-count asymptotic-variance plateau and its one-lag covariance formula, but did not cover the phase change at \(\beta=4\) or the all-lag parity law. Other examples of first-lag independence with later dependence concern different dynamical systems. These partial coincidences do not imply the claim here, which fixes the natural discontinuity sensor and proves all odd and positive even lags exactly at the canonical four-state parameter.

## Limitations

All covariance and pairwise-independence statements concern the natural absolutely continuous stationary measure, not other invariant probabilities. The parameter formula is asserted only for \(3\le\beta<9/2\); the open upper endpoint is deliberate because the source density changes beyond it. The all-lag parity law is proved only at \(\beta=4\), and makes no assertion that nonadjacent or adjacent higher-order blocks are mutually independent. The literature assessment is a statement-level comparison against inspected sources and mathematical-result searches, not proof of absolute historical priority; independent verification of originality remains outstanding.

## References

[1] V. Botella-Soler, J. A. Oteo, J. Ros, and P. Glendinning, *Families of piecewise linear maps with constant Lyapunov exponent* (2012), arXiv:1205.5360v1, especially equations (5), (9), and Appendix A (56)--(60). First publicly posted 2012-05-24. https://arxiv.org/abs/1205.5360

[2] H. Bruin, C. Carminati, S. Marmi, and A. Profeti, *Matching in a family of piecewise affine maps*, arXiv:1707.07488v1 (2017); *Nonlinearity* 32 (2019), 172--208. https://arxiv.org/abs/1707.07488

[3] V. Botella-Soler, J. A. Oteo, and J. Ros, *Dynamics of a map with a power-law tail* (2008), arXiv:0812.4551. https://arxiv.org/abs/0812.4551
