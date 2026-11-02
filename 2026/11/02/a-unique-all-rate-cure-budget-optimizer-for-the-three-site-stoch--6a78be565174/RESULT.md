# A unique all-rate cure-budget optimizer for the three-site stochastic epidemic

## Finding

Consider the exact continuous-time susceptible–infected–susceptible (SIS) contact process on the three-vertex path, initially infected at all three vertices. Each susceptible vertex is infected at rate \(\beta>0\) per infected neighbor, while the three vertices cure at independently assigned constant rates of fixed sum \(B>0\). **The unique global assignment minimizing expected time until the all-healthy absorbing state** has equal rates at the two endpoints, strictly more curing at the center, and a center budget share strictly between one third and one half for every finite positive infection rate.

Put \(r=\beta/B\), assign the two endpoints rates \(x=Bt/(2t+1)\) and the center rate \(y=B/(2t+1)\). The unique optimum is the unique positive zero \(t_*(r)\) of the explicitly certified quintic \(P_r(t)\) below, and

\[
\frac12<t_*(r)<1,\qquad
\frac B3<y_*<\frac B2,\qquad
\frac B4<x_*<\frac B3.
\]

In particular, neither uniform curing nor the degree-proportional/linearized-threshold allocation \((B/4,B/2,B/4)\) minimizes the exact extinction time at any \(\beta>0\). The optimal rate ratio returns toward uniform allocation in both limiting regimes:

\[
t_*(r)=1-r+O(r^2)\quad(r\downarrow0),\qquad
 t_*(r)=1-\frac5{12r}+O(r^{-2})\quad(r\to\infty).
\]

At \(r=1\), the root lies in \((0.836926,0.836928)\), giving \(B\mathbb E[T]\approx19.62910114\), against \(19.8125\) for uniform curing and \(21.29090909\) for the linearized-threshold allocation.

## Assumptions and scope

The graph is the undirected path with endpoint vertices \(1,3\) and center \(2\); there are exactly three vertices. A vertex is either infected or susceptible. For each infected–susceptible edge, infection occurs at rate \(\beta>0\); cure of infected vertex \(i\) occurs at its own constant rate \(\delta_i\ge0\), independently of the other clocks. Rates obey \(\delta_1+\delta_2+\delta_3=B>0\). Initially all vertices are infected. Let \(T\) be the first hitting time of the state with zero infected vertices. There is no exogenous reinfection. Curing rates are static, not state-dependent. The expectation is infinite if any curing rate is zero, since that initially infected vertex cannot recover. Thus any finite minimizer must lie in the positive interior.

## Proof

**1. Exact first-step equations.** Write \(x\) for the common endpoint rate, \(y\) for the center rate, and \(b=\beta\). By exchanging endpoints, collapse the seven transient configurations into five: one endpoint infected \(E\); center alone \(C\); center and one endpoint \(A\); the two endpoints \(D\); all three \(F\). If \(h_Z\) denotes the mean remaining absorption time, the Markov first-step equations are

\[
\begin{aligned}
(x+b)h_E&=1+bh_A,\\
(y+2b)h_C&=1+2bh_A,\\
(x+y+b)h_A&=1+xh_C+yh_E+bh_F,\\
(2x+2b)h_D&=1+2xh_E+2bh_F,\\
(2x+y)h_F&=1+2xh_A+yh_D.
\end{aligned}
\]

Solving these five linear equations gives the exact expected extinction time \(H(b,x,y)=h_F\):

\[
H(b,x,y)=\frac{4b^4+4b^3(4x+y)+b^2(24x^2+32xy+y^2)+b(16x^3+28x^2y+18xy^2)+4x^4+6x^3y+9x^2y^2+3xy^3}{2x^2y(2b+x+y)(4b+2x+y)}.
\]

**2. Equality of endpoint rates is globally optimal, not assumed.** Let \(H_7(b,u,y,v)\) denote the mean hitting time from full infection found from the seven transient configurations with independent endpoint rates \(u,v>0\). It is symmetric in \(u,v\), and \(H_7(b,x,y,x)=H(b,x,y)\). Put \(u=x+h\), \(v=x-h\), with \(0<|h|<x\), and \(z=x^2-h^2>0\). Exact elimination of the seven-state first-step system and a common-denominator calculation give

\[
H_7(b,x+h,y,x-h)-H(b,x,y)=
\frac{h^2\,[N_0(b,x,y)+zN_1(b,x,y)]}
{2x^2yz(2b+x+y)(4b+2x+y)[Q_0(b,x,y)+zQ_1(b,x,y)]}.
\]

The four polynomials in this identity are *explicitly defined* by coefficient extraction: form \(H_7\) from the generator in the verification script, subtract \(H\), cancel the factor \(h^2\), and substitute \(h^2=x^2-z\). The script checks the **exact symbolic identity**, not sampled values, and establishes that \(N_0,N_1\) together have 55 strictly positive integer monomials and \(Q_0,Q_1\) together have 16 strictly positive integer monomials. In particular all four are positive at positive \(b,x,y,z\), proving strict symmetrization. As the sum \(u+v=2x\) is preserved, no asymmetric assignment can be globally optimal. The full symbolic construction and coefficient assertions in `VERIFY.py` are a finite, reproducible polynomial-positivity certificate for this nonstandard step.

**3. Unique symmetric optimum.** Parameterize \(x=Bt/(2t+1)\), \(y=B/(2t+1)\), \(r=b/B\), and write \(F_r(t)=BH(b,x,y)\). Direct symbolic differentiation of the displayed rational function gives

\[
F'_r(t)=\frac{P_r(t)}{2t^3(4r+1)(4rt+2r+t+1)^2},
\]

where \(P_r(t)=a_5t^5+a_4t^4+a_3t^3+a_2t^2+a_1t+a_0\) with

\[
\begin{aligned}
a_5&=4(2r+1)^4(4r+1),\\
a_4&=8(2r+1)^5,\\
a_3&=-(128r^5+96r^4+96r^3+44r^2+16r+3),\\
a_2&=-2(2r+1)(4r+1)(16r^3+12r^2+12r+3),\\
a_1&=-(2r+1)^2(28r^3+15r^2+12r+3),\\
a_0&=-2r^2(2r+1)^3.
\end{aligned}
\]

For each \(r>0\), the descending coefficient signs are \((+,+,-,-,-,-)\), so Descartes' rule of signs permits at most one positive zero. Existence in the claimed interval follows from exact endpoint values

\[
\begin{aligned}
P_r(1/2)&=-\frac{512r^5+640r^4+512r^3+288r^2+90r+11}{4}<0,\\
P_r(1)&=r(540r^3+540r^2+207r+28)>0.
\end{aligned}
\]

The derivative consequently switches from negative to positive at the unique root. Because \(H\) diverges at the feasible simplex boundary, and endpoint symmetrization is strict, this root yields the unique global minimum among **all three independent positive curing rates**. At \(r=0\), \(P_0(t)=t(t-1)(4t^3+12t^2+9t+3)\), showing uniformity at zero infection. For weak infection the implicit-function derivative is \(-1\), using \(\partial_tP(1,0)=\partial_rP(1,0)=28\). For strong infection the leading \(r^5\) term of \(P_r(t)\) is \(16(t-1)(2t+1)^4\); its \(t\)-derivative at one is \(1296\), while the next coefficient of \(r^4\) at one is \(540\), giving the correction \(-5/(12r)\).

**4. A distinct objective.** For the symmetric linearized infection system \(\dot q=[bA-\operatorname{diag}(x,y,x)]q\), zero is a linear threshold when \(b_c=\sqrt{xy/2}\). Maximizing this threshold under \(2x+y=B\) gives \(x=B/4,y=B/2\), i.e. \(t=1/2\). The strict inequality \(t_*(r)>1/2\) proves that maximizing the linearized threshold and minimizing the *exact* finite-network extinction time are different optimization problems.

## Verification

The standalone `VERIFY.py` requires Python 3 and SymPy and runs with `python VERIFY.py`. It independently constructs the seven transient Markov states, checks 60 exact-rational full-chain instances, reconstructs and proves the symbolic endpoint-symmetrization polynomial identity with 55 positive numerator coefficients and 16 positive denominator coefficients, and checks the entire quintic derivative identity and endpoint signs. The executable reports 103 exact assertions. Numerical illustrations and root brackets are supplementary; the all-parameter statements follow from exact algebra and sign arguments.

## Relationship to prior work

Wagner and Anantharam study spatially variable **reproduction** rates and the large-system extinction-growth exponent, not an all-rate finite three-site cure allocation. Borgs, Chayes, Ganesh and Saberi study heterogeneous cure rates and epidemic control, prominently degree-based schemes, but not this exact finite-size all-infected global optimization. Van de Bovenkamp and Van Mieghem derive exact star survival times under homogeneous cure rates and analyze outbreak thresholds. McFadden, Daly and Shneer (2025) establish general weak/strong infection principles, and numerically illustrate a **three-node star** with symmetric leaves from **one uniformly randomly chosen initial infection**; they do not supply an exact all-positive-infection-rate theorem for **full initial infection** or a proof of unrestricted endpoint symmetrization. The latter two differences in initial state and optimization scope matter. The novelty assessment remains provisional pending additional historical-source examination.

## Limitations

The theorem pertains only to three sites, uniform edge transmission, independent exponential clocks, constant cure rates and starting from full infection. It does not optimize extinction time averaged over other initial states, nor dynamic cure controls, costs, prevention, vaccination, or epidemics on larger graphs. A plausible closely related later doctoral thesis was not available for full-text comparison; this is a historical-priority risk, not a gap in the mathematical proof.

## References

1. Wagner, A. B. and Anantharam, V., *Designing a Contact Process: The Piecewise-Homogeneous Process on a Finite Set with Applications*, Stochastic Processes and their Applications 115 (2005), 117–153. https://doi.org/10.1016/j.spa.2004.08.003. Author full text: https://people.eecs.berkeley.edu/~ananth/Preprints/Aaron/erlmemo.pdf.
2. Borgs, C., Chayes, J., Ganesh, A., and Saberi, A., *How to Distribute Antidote to Control Epidemics*, Random Structures & Algorithms 37 (2010), 204–222. https://doi.org/10.1002/rsa.20315. Version of record online February 18, 2010. Author full text: https://web.stanford.edu/~saberi/antidote.pdf.
3. Van de Bovenkamp, R. and Van Mieghem, P., *Survival Time of the Susceptible-Infected-Susceptible Infection Process on a Graph*, Physical Review E 92 (2015), 032806. https://doi.org/10.1103/PhysRevE.92.032806.
4. McFadden, R., Daly, F., and Shneer, V., *Optimal Curing Rate Allocation in the SIS Epidemic Model*, Statistics and Probability Letters 216 (2025), 110284. https://doi.org/10.1016/j.spl.2024.110284. Open-access full text: https://pure.hw.ac.uk/ws/portalfiles/portal/142344823/1-s2.0-S0167715224002530-main.pdf.
5. Drakopoulos, K., Ozdaglar, A., and Tsitsiklis, J. N., *An Efficient Curing Policy for Epidemics on Graphs* (2014 preprint, 2015 journal). https://arxiv.org/abs/1407.2241.
