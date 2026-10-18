# Optimal migration grows inversely with the season length in a two-habitat sink model

## Finding
For the symmetric periodically switching two-patch model below, optimize the principal long-run population growth rate over all constant symmetric migration rates \(m\ge0\) *at each fixed half-period* \(T>0\). The exact growth exponent is
\[
\lambda(m,T,\varepsilon)=-\varepsilon-m+\frac1T\operatorname{arsinh}\!\left(\frac{m}{\sqrt{1+m^2}}\sinh(T\sqrt{1+m^2})\right).
\]
There is exactly one positive solution \(z_*\) of
\[
2\tanh z=z(2-\tanh^2z),\qquad z_*=1.606115298802767\ldots,
\]
and, with \(G=(z_*-\tanh z_*)/(2z_*^2)=0.132487539446827\ldots\), every sufficiently small \(T>0\) has a *unique global* maximizing migration rate \(m_*(T)\) satisfying
\[
m_*(T)=\frac{z_*}{T}+O(T),\qquad
\max_{m\ge0}\lambda(m,T,\varepsilon)=-\varepsilon+GT+O(T^3).
\]
The error constants are independent of the common mortality shift \(\varepsilon\ge0\). In particular, if \(\varepsilon(T)/T\to\kappa\ge0\), then \(T^{-1}\max_m\lambda\to G-\kappa\), so the leading fast-season invasion threshold is \(\kappa=G\) (no conclusion at equality without higher-order terms).

## Assumptions and scope
Take arbitrary \(T>0\), \(m\ge0\), \(\varepsilon\ge0\). For column abundance \(x(t)=(x_1(t),x_2(t))^\top\), let \(\dot x=A_+(m,\varepsilon)x\) on each first half-period of length \(T\), followed by \(\dot x=A_-(m,\varepsilon)x\) on the second half; repeat with period \(2T\), where
\[
A_+=\begin{pmatrix}1-\varepsilon-m&m\\m&-1-\varepsilon-m\end{pmatrix},\quad
A_-=\begin{pmatrix}-1-\varepsilon-m&m\\m&1-\varepsilon-m\end{pmatrix}.
\]
The principal Floquet exponent means \(\lambda=(2T)^{-1}\log\rho(e^{TA_-}e^{TA_+})\). For strictly positive initial abundance vectors this is the asymptotic exponential growth rate. Neither time-varying migration control nor nonlinear regulation is allowed in the optimization.

## Proof
**Exact monodromy.** Put \(k=\sqrt{1+m^2}\), \(B_\pm=A_\pm+(\varepsilon+m)I\). Direct multiplication yields \(B_\pm^2=k^2I\), so \(e^{TB_\pm}=\cosh(kT)I+\sinh(kT)B_\pm/k\). Let \(Q=e^{TB_-}e^{TB_+}\). Then \(\det Q=1\) and
\[
\tfrac12\operatorname{tr}Q=1+\frac{2m^2}{1+m^2}\sinh^2(kT)=\cosh(2a),\quad
a=\operatorname{arsinh}\!\left(\frac m k\sinh(kT)\right).
\]
Thus \(\rho(Q)=e^{2a}\). Multiplication by the common factor \(e^{-2(\varepsilon+m)T}\) proves the displayed Floquet formula, including \(m=0\). For \(m>0\), strict increase of \(\sinh u/u\) implies \((m/k)\sinh(kT)>\sinh(mT)\), whence \(\lambda> -\varepsilon\). Conversely \(a\le kT\) gives
\[
0<\lambda+\varepsilon\le k-m=\frac{1}{k+m},
\]
so the enhancement vanishes as \(m\to\infty\). Continuity, positivity at finite \(m>0\), and baseline equality at \(m=0\) imply a positive finite global maximizer for every \(T>0\).

**Uniform singular scaling.** Set \(z=mT\), \(u=T^2\), and define the analytic function
\[
F(z,u)=\operatorname{arsinh}\!\left[z\,\frac{\sinh\sqrt{z^2+u}}{\sqrt{z^2+u}}\right],
\]
using the regular power series at zero. Here \(F(z,0)=z\) for all \(z\ge0\). Differentiation with respect to \(u\) at zero gives
\[
\partial_uF(z,0)=g(z):=\frac{z-\tanh z}{2z^2},\quad g(0):=0.
\]
Therefore, with \(H_T(z)=[F(z,T^2)-z]/T^2\), the exact exponent obeys \(\lambda+\varepsilon=T H_T(mT)\). On any compact interval of nonnegative \(z\), Taylor's theorem gives \(H_T=g+O(T^2)\); the convergence is also \(C^2\) on neighborhoods of every positive \(z\). For every \(z>0\), the previous monodromy bound gives the global tail estimate
\[
0\le H_T(z)\le\frac{1}{\sqrt{z^2+T^2}+z}\le\frac1{2z}.
\]
Hence a maximizing \(z=mT\) cannot escape to infinity. Compact uniform convergence, and the fact that \(g(0)=0\) while \(g\) is positive in the interior, keep all maximizing \(z\) away from zero.

**Unique limiting optimizer.** For \(z>0\), the sign of \(g'(z)\) is the sign of
\[
h(z)=2\tanh z-z(2-\tanh^2z).
\]
An exact derivative calculation gives \(h'(z)=\tanh z\,[2z\operatorname{sech}^2z-\tanh z]\). Thus \(h'\) switches from positive to negative exactly once, when \(\sinh(2z)=4z\), because \(\sinh(2z)/z\) increases strictly on the positive line. Since \(h(0)=0\), \(h(z)>0\) for sufficiently small \(z>0\), and \(h(z)\to-\infty\), the function \(g\) has exactly one global maximizer \(z_*>0\), and \(g''(z_*)<0\). All global maximizers of \(H_T\) therefore converge to \(z_*\). Strict local concavity of \(H_T\), following from its uniform \(C^2\) convergence near \(z_*\), forces their uniqueness for all sufficiently small \(T\). Expanding the stationary equation \(H_T'(z)=0\) yields \(z_T=z_*+O(T^2)\), and inserting this into \(H_T=g+O(T^2)\) yields the two claimed asymptotic formulas. The mortality dependence is an exact additive shift.

## Verification
Run the standalone file `verify.py` with Python 3 and `mpmath` installed. It compares the formula against independently evaluated \(2\times2\) matrix exponentials for 24 parameter triples at 65-digit precision, checks 10 local singular-scale expansions, and checks four optimized small-period regimes. On the packaged program these tests returned `PASS`; they are finite consistency checks, not a proof of the limit or global uniqueness.

## Relationship to prior work
Katriel's *Dispersal-induced growth in a time-periodic environment* (first public April 4, 2021) gives a general framework for dispersal-mediated growth and analyzes the high-frequency regime when migration is fixed. Benaïm, Lobry, Sari and Strickler's *Untangling the role of temporal and spatial variations in persistence of populations* (first public November 24, 2021) studies this exact opposite-season two-patch environment; its Section 2.2 gives a closed form for its Floquet exponent and fixed-migration asymptotic regimes. The exact Floquet formula is therefore **rederived background, not a claim of priority**. The present contribution is the global optimization under simultaneous \(T\downarrow0\), \(m\asymp T^{-1}\), including unique optimal scale and sharp growth coefficient. Related optimizations for other migration classes or unindexed equivalent derivations cannot be excluded.

## Limitations
The leading critical case \(\varepsilon(T)/T\to G\) is unresolved by the first-order criterion. The model is linear with precisely balanced alternating environments, symmetric constant migration, and a principal Floquet exponent; it gives no stochastic survival or density-regulated persistence result. The optimization is asymptotic for small \(T\); uniqueness is not asserted for arbitrary periods. Literature priority is not independently certified.

## References
1. Guy Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589, first submitted 2021-04-04; later *Journal of Mathematical Biology*, DOI 10.1007/s00285-022-01791-7.
2. Michel Benaïm, Claude Lobry, Tewfik Sari, Édouard Strickler, *Untangling the role of temporal and spatial variations in persistence of populations*, arXiv:2111.12633, first submitted 2021-11-24; later *Theoretical Population Biology*, DOI 10.1016/j.tpb.2023.07.003, especially Section 2.2, Proposition 2.3 and Proposition 2.4.
