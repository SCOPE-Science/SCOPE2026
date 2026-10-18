# Strict survival ordering under redistributed local extinction risk

## Finding
Consider a continuous-time two-patch occupancy process with initially occupied patches, positive local extinction rates \(a,b\), and a common nonnegative recolonization rate \(c\). Hold the total local extinction intensity \(S=a+b\) and the recolonization rate \(c\) fixed. For two positive-rate allocations \((a,b)\) and \((a',b')\) satisfying \(a+b=a'+b'=S\), let \(T_{a,b,c}\) denote the first time both patches are empty. Then

\[
|a-b|>|a'-b'|\quad\Longrightarrow\quad
\Pr(T_{a,b,c}>t)>\Pr(T_{a',b',c}>t)
\quad\text{for every }t>0.
\]

In particular, the equal-rate allocation is the unique least persistent allocation at **every** positive time horizon, in the usual stochastic order. This remains true with arbitrarily frequent finite recolonization; it is not merely an ordering of expected lifetimes. The strict conclusion requires both local extinction rates to be positive. For a fixed \(S\), the dependence of the survival distribution on the pair \((a,b)\) is symmetric and strictly increasing with their imbalance.

## Assumptions and scope
The occupancy state is \(B=(1,1)\), \(U=(1,0)\), \(V=(0,1)\), or absorbing \(\varnothing=(0,0)\). Extinction of occupied patch one occurs with constant intensity \(a>0\) and of occupied patch two with constant intensity \(b>0\), independently in the infinitesimal Markov sense. While exactly one patch remains occupied, it recolonizes the empty patch at intensity \(c\ge0\), independent of direction. Events are exponential and memoryless, and extinction of both patches ends the process irreversibly. The process starts at \(B\). Parameters \(a,b,c\) are finite. Rates are held fixed in time. The allocation comparison holds for any two positive pairs at fixed \(S=a+b\) and fixed \(c\), not for arbitrary changes of total extinction intensity or direction-dependent recolonization.

The transient generator in the state order \((B,U,V)\) is

\[
Q=\begin{pmatrix}
-(a+b)&b&a\\
c&-(a+c)&0\\
c&0&-(b+c)
\end{pmatrix}.
\]

Let \(u_{S,P,c}(t)=\mathbf e_B^{\mathsf T}e^{Qt}\mathbf1\) be survival at time \(t\), with \(P=ab\in(0,S^2/4]\). This notation is well defined because the survival function depends on \((a,b)\) through \(S\) and \(P\).

## Proof
Define the resolvent \(R(z)=(zI-Q)^{-1}\) for \(z>0\), and put

\[
D(z)=z(z+S+c)^2+P(z+S+2c).
\]

Direct elimination in the three transient states yields the survival Laplace transform

\[
\widehat u_{S,P,c}(z)
=\int_0^\infty e^{-zt}u_{S,P,c}(t)\,dt
=\frac{(z+S+c)^2-P}{D(z)}.
\]

At fixed \(S,c\), differentiation with respect to \(P\) gives the exact factorization

\[
-\frac{\partial\widehat u}{\partial P}(z)
=\underbrace{\frac{(z+S+c)^2}{D(z)}}_{A(z)}
\underbrace{\frac{2z+S+2c}{D(z)}}_{G(z)}.
\]

**Positivity of both inverse transforms.** For the first factor, rewrite

\[
A(z)=\widehat u_{S,P,c}(z)+\frac{P}{D(z)}.
\]

Write \(k(t)\) for the inverse Laplace transform of \(1/D(z)\). When \(c>0\), a resolvent cofactor identity is

\[
R_{U,V}(z)=\frac{ac}{D(z)},
\qquad
k(t)=\frac{(e^{Qt})_{U,V}}{ac}\ge0.
\]

When \(c=0\), the factorization \(D(z)=(z+S)(z+a)(z+b)\) shows instead that \(k\) is the convolution of the three nonnegative exponential functions \(e^{-St}\), \(e^{-at}\), and \(e^{-bt}\). Thus \(A\) is the Laplace transform of

\[
f(t)=u_{S,P,c}(t)+Pk(t)>0\quad(t\ge0),
\]

where the strict inequality follows from the positive probability of remaining in \(B\) without an event.

For the second factor the cofactor identities are

\[
R_{B,U}(z)=\frac{b(z+b+c)}{D(z)},\qquad
R_{B,V}(z)=\frac{a(z+a+c)}{D(z)}.
\]

Consequently,

\[
G(z)=\frac{R_{B,U}(z)}{b}+\frac{R_{B,V}(z)}{a}
\]

is the Laplace transform of

\[
g(t)=\frac{(e^{Qt})_{B,U}}{b}+\frac{(e^{Qt})_{B,V}}{a}>0
\quad(t>0).
\]

The strict inequality holds because, starting at \(B\), there is positive probability at every positive time to undergo exactly one patch-extinction event and remain in the corresponding singleton state until observation. Uniqueness of Laplace transforms, together with analytic dependence of the finite-state semigroup on \(P\), now implies the **pointwise sensitivity identity**

\[
-\frac{\partial u_{S,P,c}}{\partial P}(t)
=\int_0^t f(s)g(t-s)\,ds>0\quad(t>0).
\]

The algebra and inverse-transform argument is valid throughout \(0<P\le S^2/4\), including the one-sided derivative at the balanced endpoint. Finally,

\[
P=\frac{S^2-(a-b)^2}{4}.
\]

At fixed \(S\), increasing \(|a-b|\) strictly decreases \(P\). Integrating the strictly negative sensitivity over the interval of \(P\) between two allocations proves the strict all-horizon stochastic order, including when one allocation is balanced. This completes the proof.

As an independent moment consequence, evaluation at \(z=0\) yields

\[
\mathbb E[T_{a,b,c}]
=\frac{(S+c)^2-P}{P(S+2c)},\qquad
\left.\frac{\partial\mathbb E[T]}{\partial P}\right|_{S,c}
=-\frac{(S+c)^2}{P^2(S+2c)}<0.
\]

For instance, at \(S=4,c=1\), the equal allocation \((2,2)\) has mean extinction time \(7/8\), whereas \((1,3)\) has mean \(11/9\) and greater survival at every positive horizon. The mean calculations are consequences, not substitutes for the stochastic-order proof.

## Verification
Run `python verify.py` in an environment with Python, SymPy, NumPy, and SciPy. The script verifies the generator determinant, the resolvent cofactors, the Laplace transform, the product derivative, the mean and its sensitivity, and the exact rational example. It also checks 216 finite matrix-exponential inequalities across a parameter grid. These finite diagnostics do not constitute an exhaustive proof for arbitrary rates or times; the analytic convolution argument above is the proof of the universal inequality.

## Relationship to prior work
Etienne and Heesterbeek [1] study conservation decisions in a stochastic winking-patch metapopulation, with a reported management rule favoring protection of patches already having low extinction risk. This is closely motivated prior work on expected persistence, but the available abstract does not assert a fixed-sum **strict usual stochastic order at every time** for the specified continuous-time two-patch generator; the complete paper was not accessible for a decisive theorem-by-theorem comparison. Frank [2] highlights qualitative and ranking consequences of stochastic habitat heterogeneity, motivating direct all-horizon comparisons; the publicly available abstract does not supply this exact ordering. The earlier warm-standby reliability model of Srinivasan and Gopalan [3] concerns active-versus-standby behavior and a repair facility, not the four-state occupancy process here.

Corujo, Valdés, and Laria [4] give substantial stochastic-order theory for **warm and cold standby** two-unit repairable systems, including likelihood-ratio and hazard-rate criteria. Their stated Markovian warm-standby generator has two transient operational states, a principal unit and a spare with position-dependent hazard; it is not the present three-transient-state process with two patch-specific extinction hazards and symmetric recolonization. In particular, their parameter conditions do not imply the fixed-sum strict redistribution law proved here. The result for \(c=0\) is the classical independent-parallel exponential special case; the substantive assertion is that the strict all-horizon order persists for every \(c>0\).

## Limitations
The fixed-sum comparison is a stylized redistribution of local extinction hazards, not a claim that conservation interventions can freely shift rates while preserving their sum. It assumes only two patches, constant independent local hazards, symmetric recolonization, an initially fully occupied system, and absorbing global extinction. It does not establish hazard-rate ordering, likelihood-ratio ordering, variance ordering, or generalizations to patch networks with three or more patches. The related 2001 management study could not be read in full; an equivalent unlocated statement is a residual originality risk.

## References
[1] R. S. Etienne and J. A. P. Heesterbeek, “Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model,” *The American Naturalist* **158** (2001), 389–407. DOI: `10.1086/321986`.

[2] K. Frank, “Metapopulation Persistence in Heterogeneous Landscapes: Lessons about the Effect of Stochasticity,” *The American Naturalist* **165** (2005), 374–388; publicly online February 3, 2005. DOI: `10.1086/428293`.

[3] S. K. Srinivasan and M. N. Gopalan, “Probabilistic Analysis of a Two-Unit System with a Warm Standby and a Single Repair Facility,” *Operations Research* **21** (1973), 748–754. DOI: `10.1287/opre.21.3.748`.

[4] J. M. Corujo, J. E. Valdés, and J. C. Laria, “Stochastic Comparisons of Two-Units Repairable Systems” (2018), arXiv:`1804.03098`.

[5] M. S. EL-Sherbeny, “Stochastic Analysis of a Two Non-Identical Unit Parallel System with Different Types of Failures Subject to Preventive Maintenance and Repairs,” *Journal of Applied Mathematics* (2013), Article 192545. DOI: `10.1155/2013/192545`.
