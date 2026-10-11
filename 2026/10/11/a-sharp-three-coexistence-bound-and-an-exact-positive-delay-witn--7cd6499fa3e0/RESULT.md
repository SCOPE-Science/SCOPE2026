# A sharp three-coexistence bound and an exact positive-delay witness in a mosaic-virus system

## Finding

For the four-population, two-delay mosaic-disease model of Al Basir, Blyuss and Venturino (2023), there are at most three *strictly positive* coexistence equilibria at every strictly positive parameter vector and every pair of finite nonnegative delays. If its reproduction number satisfies \(\mathcal R_0\le1\), there are none. The bound three is achieved with **both delays strictly positive**: an explicit exact parameter vector has three distinct positive coexistence equilibria, all corresponding to simple scalar equilibrium roots. This multiplicity persists under sufficiently small independent perturbations of every model parameter and both delays.

## Assumptions and scope

Let \(S,I,U,V\) be healthy plants, infected plants, healthy vectors and infected vectors. We consider the delayed model
\[
\begin{aligned}
\dot S(t)&=rS(t)\left(1-\frac{S(t)+I(t)}K\right)-\lambda S(t)V(t),\\
\dot I(t)&=\lambda e^{-m\tau_1}S(t-\tau_1)V(t-\tau_1)-mI(t),\\
\dot U(t)&=b\big(U(t)+V(t)\big)\left(1-\frac{U(t)+V(t)}{a(S(t)+I(t))}\right)-\beta U(t)I(t),\\
\dot V(t)&=\beta e^{-\mu\tau_2}U(t-\tau_2)I(t-\tau_2)-\mu V(t).
\end{aligned}
\]
All eight rate/capacity parameters \(r,K,\lambda,m,b,a,\beta,\mu\) are strictly positive and \(0\le\tau_1,\tau_2<\infty\). The equilibrium is a constant history \((S,I,U,V)\in(0,\infty)^4\). This is the original source's equation (2.3), including its delay-dependent survival factors. Define its reproduction number
\[
\mathcal R_0=\frac{aK^2\beta\lambda e^{-m\tau_1-\mu\tau_2}}{m\mu}.
\]
No stability assumption is made; distinct equilibria do not imply multiple attracting states.

## Proof

**Reduction and equivalence.** At a strictly positive equilibrium set \(z=\lambda V/r\). The healthy-plant balance gives
\(z=1-(S+I)/K\), so \(0<z<1\). Introduce the four positive dimensionless parameters
\[
A=\frac{re^{-m\tau_1}}m,\qquad R=\mathcal R_0,\qquad
h=\frac{r}{aK\lambda},\qquad q=\frac{\mu e^{\mu\tau_2}}b.
\]
The first, second and fourth equilibrium equations determine *all* state components:
\[
S=\frac{K(1-z)}{1+Az},\qquad I=AzS,\qquad
V=\frac{rz}{\lambda},\qquad U=\frac{aK}{R}\frac{1+Az}{1-z}.
\]
For \(0<z<1\), all four are strictly positive. In particular, no spurious solution is introduced when dividing by these quantities. Put
\[
H(z)=\frac{1+Az}{R}+hz(1-z),\qquad
Q(z)=\big((1-z)^2-H(z)\big)H(z)-qhz(1-z)^3.
\]
Writing \(N=U+V\) and \(M=S+I\), the formulae imply
\[
\frac{N}{aM}=\frac{H(z)}{(1-z)^2},\qquad
\frac{\beta UI}{bN}=\frac{qhz(1-z)}{H(z)}.
\]
Hence the third equilibrium equation is equivalent, without division by zero, to
\[
1-\frac{H(z)}{(1-z)^2}-\frac{qhz(1-z)}{H(z)}=0
\quad\Longleftrightarrow\quad Q(z)=0.
\]
The correspondence between zeros of \(Q\) in \((0,1)\) and strictly positive coexistence equilibria is therefore bijective.

**Sharp universal count and threshold.** Because \(H\) is quadratic, \(Q\) is a real polynomial of degree at most four. At the endpoints,
\[
Q(0)=\frac{R-1}{R^2},\qquad Q(1)=-\frac{(1+A)^2}{R^2}<0.
\]
If \(R>1\), the endpoint signs are opposite. If a polynomial of degree at most four had four *distinct* zeros in \((0,1)\), it would have degree four and all four zeros would be simple, forcing its signs at the endpoints to agree. Thus there can be at most three distinct zeros in the physical interval, with no restriction on their multiplicities. If \(R\le1\), the displayed formula yields
\[
\frac U{aK}=\frac{1+Az}{R(1-z)}>1,
\]
but the positive third equilibrium equation requires \(N<aM\), hence \(U<N<aM<aK\), a contradiction. This excludes all positive equilibria when \(R\le1\).

**Exact delayed realization.** Take
\[
(r,K,\lambda,m,b,a,\beta,\mu,\tau_1,\tau_2)
=(40,1,10000,1,1/20,1,2/25,1,\log2,\log2).
\]
Both delays are strictly positive; the survival factors are exactly \(1/2\), yielding
\[
(A,R,h,q)=(20,200,1/250,40),\quad
H(z)=\frac{5+104z-4z^2}{1000},
\]
\[
10^6Q(z)=155984z^4-367168z^3+262224z^2-67040z+4975.
\]
Exact rational signs of this integer polynomial are respectively positive, negative, negative, positive, positive, negative at
\[
\frac1{10},\ \frac15,\ \frac3{10},\ \frac25,\ \frac35,\ \frac23.
\]
Thus the three disjoint intervals \((1/10,1/5)\), \((3/10,2/5)\), \((3/5,2/3)\) each contain a root in \((0,1)\). The same polynomial is negative at \(1\) and positive at \(3/2\), so there is a fourth real root in \((1,3/2)\). These are four distinct zeros of a degree-four polynomial and hence all are simple. They give **exactly three strictly positive coexistence equilibria** and one nonphysical scalar root. Continuity of the coefficient functions and the implicit-function theorem at the three simple physical roots show that three positive equilibrium branches persist in an open neighborhood of this strictly positive parameter-and-delay vector. The universal bound makes the number exactly three throughout a sufficiently small such neighborhood.

## Verification

The standalone `check_equilibria.py`, run with `python check_equilibria.py` and the installed version of SymPy specified in `requirements.txt`, checks the elimination identity symbolically, the degree/endpoints, the parameter conversion, vanishing of the other three equilibrium residuals, and every witness sign using exact rationals. It prints `CHECK_OK`. The six physical-endpoint sign values for \(10^6Q\), in the order above, are
\[
338544/625,\ -394881/625,\ -116816/625,\ 380799/625,\ 36799/625,\ -93409/81.
\]
The values at \(1\) and \(3/2\) are exactly \(-11025\) and \(44896\). These are an explicit interval certificate for the quartic; the global degree/sign argument is a mathematical proof rather than a finite sampling assertion. A reproducible run requires Python 3 and SymPy.

## Relationship to prior work

The motivating 2023 paper gives the *same two-delay model* in equation (2.3), its coexistence quartic in equation (3.1), and a **sufficient**, coefficient-sign-based single-positive-root result in Theorem 2. It analyzes stability and delay bifurcations, primarily on one equilibrium branch. None of these statements yields the globally sharp feasible coexistence count, a certified three-root example with both delays positive, or an open region realizing that count.

The 2016 zero-delay Jatropha model by Venturino, Roy, Al Basir and Datta is the genuine antecedent, not an unrelated model. Its §3.1 explicitly notes possible one, three or five positive roots of an unrefined degree-five elimination polynomial and leaves equilibrium uniqueness uninvestigated. Thus the *possibility of three algebraic roots* is not claimed as new here. The present result instead proves a sharp upper bound for feasible states and realizes it constructively in the 2023 two-delay model. A related 2020 plant-virus delay model by Al Basir and collaborators has a different vector influx/removal equation; its equilibrium conclusions do not imply this exact Leslie–Gower count.

## Limitations

The theorem classifies the **maximum number** of strictly positive equilibrium points and gives one robust realized region; it is not an exhaustive parameter-space decomposition. It makes no assertion of local stability, multiple attractors, transient trajectories, basin geometry, or the ecological realism of the witness's large transmission parameter. Borderline nonpositive equilibria and infinite delays are outside the statement. The literature comparisons establish no formal guarantee against uncatalogued earlier work.

## References

1. F. Al Basir, K. B. Blyuss, E. Venturino, *Stability and bifurcation analysis of a multi-delay model for mosaic disease transmission*, AIMS Mathematics **8** (2023), 24545–24567, doi:10.3934/math.20231252, first published 2023-08-18; equation (2.3), §3.1 and Theorem 2. Open-access full text: https://www.aimspress.com/aimspress-data/math/2023/10/PDF/math-08-10-1252.pdf.
2. E. Venturino, P. K. Roy, F. Al Basir, A. Datta, *A model for the control of the mosaic virus disease in Jatropha curcas plantations*, Energy, Ecology and Environment **1** (2016), 360–369, doi:10.1007/s40974-016-0033-8, §2–3.1. Open-access full text: https://link.springer.com/content/pdf/10.1007%2Fs40974-016-0033-8.pdf.
3. F. Al Basir, S. Adhurya, M. Banerjee, E. Venturino, S. Ray, *Modelling the Effect of Incubation and Latent Periods on the Dynamics of Vector-Borne Plant Viral Diseases*, Bulletin of Mathematical Biology **82** (2020), article 94, doi:10.1007/s11538-020-00767-2, especially model (1).
