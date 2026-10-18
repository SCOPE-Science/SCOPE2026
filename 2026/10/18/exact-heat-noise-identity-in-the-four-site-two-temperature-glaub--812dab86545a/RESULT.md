# Exact heat-noise identity in the four-site two-temperature Glauber ring

## Finding

For the four-spin periodic nearest-neighbor Ising chain with alternating Glauber-bath parameters \(0\le a,b<1\), let \(Q_t\) be the signed heat absorbed from the bath acting on sites \(0,2\), measured in units of \(4J\), during time \(t\). Write \(a\) for the bath parameter at sites \(0,2\), and \(b\) for that at sites \(1,3\). In the unique stationary state, the long-time mean heat flux and its asymptotic variance rate are, for every such parameter pair,

\[
\lim_{t\to\infty}\frac{\mathbb E Q_t}{t}=\frac{b-a}{2},\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(Q_t)}{t}
=\frac{8-a^2-6ab-b^2}{16}.
\]

In particular, with \(\bar\gamma=(a+b)/2\) and \(j=(b-a)/2\), the **exact nonequilibrium heat-noise identity** is

\[
\boxed{\;\lim_{t\to\infty}t^{-1}\operatorname{Var}(Q_t)
=\frac{1-\bar\gamma^2}{2}+\frac{j^2}{4}.\;}
\]

Thus at fixed mean bath parameter, the excess variance rate over the equal-temperature case is exactly one quarter of the squared current, for arbitrary temperature contrast in the stated domain, not just near equilibrium. With an infinite-temperature even-site bath (\(a=0\)) and \(0<b<1\), the unit-heat-normalized dispersion is

\[
F(b)=\frac{\lim_{t\to\infty}\operatorname{Var}(Q_t)/t}{\lim_{t\to\infty}\mathbb E Q_t/t}
=\frac1b-\frac b8.
\]

It is strictly decreasing, crosses the unit-Poisson benchmark precisely at \(b_*=2\sqrt6-4\), and satisfies \(F(b)<1\) exactly when \(b>b_*\). This is a comparison for **signed net heat**, not an assertion that the number of energy-exchange events is a Poisson or renewal count.

## Assumptions and scope

Four spins \(\sigma_i\in\{-1,1\}\), with indices understood modulo \(4\), interact through \(H=-J\sum_{i=0}^3\sigma_i\sigma_{i+1}\), where \(J>0\). A flip of site \(i\) occurs at rate

\[
w_i(\sigma)=1-\frac{\gamma_i}{2}\sigma_i(\sigma_{i-1}+\sigma_{i+1}),\qquad
\gamma_0=\gamma_2=a,\quad \gamma_1=\gamma_3=b.
\]

For physical nonnegative inverse temperatures, \(\gamma_i=\tanh(2J/(k_{\rm B}T_i))\), with the infinite-temperature convention \(\gamma_i=0\). The domain \(0\le a,b<1\) ensures every flip rate is strictly positive and the continuous-time 16-state chain is irreducible. An even-site flip changes the system energy by \(4Jq_i\), where \(q_i=\sigma_i(\sigma_{i-1}+\sigma_{i+1})/2\in\{-1,0,1\}\); the random variable \(Q_t\) sums these \(q_i\) over flips at sites \(0,2\) and ignores odd-site flips. Units of time correspond to the rate normalization above. The limits also hold for any initial distribution, as finite-state irreducibility makes the limiting cumulant rates initial-state independent.

## Proof

Define the four even spin observables

\[
U=\sum_{i=0}^3\sigma_i\sigma_{i+1},\qquad
V=\sigma_0\sigma_2,\qquad
W=\sigma_1\sigma_3,\qquad
P=\sigma_0\sigma_1\sigma_2\sigma_3.
\]

Let \(L\) be the backward Markov generator, \(Lg(\sigma)=\sum_iw_i(\sigma)[g(\sigma^{[i]})-g(\sigma)]\). Directly applying each of the four flips, and using \(PU=U\), gives the closed identities

\[
\begin{aligned}
LU&=-4U+4a(1+W)+4b(1+V),\\
LV&=aU-4V,\\
LW&=bU-4W,\\
LP&=-8P+(a+b)U.
\end{aligned}
\]

Denoting stationary expectation by \(\langle\cdot\rangle\), these relations and \(\langle Lg\rangle=0\) give

\[
\begin{aligned}
\langle U\rangle&=\frac{2(a+b)}{2-ab},\\
\langle V\rangle&=\frac{a(a+b)}{2(2-ab)},\\
\langle W\rangle&=\frac{b(a+b)}{2(2-ab)},\\
\langle P\rangle&=\frac{(a+b)^2}{4(2-ab)}.
\end{aligned}
\]

Here \(2-ab>0\) throughout the assumed domain. No assumption about Gibbs form or factorization of the stationary measure is needed.

For the signed heat current introduce the tilted backward operator

\[
L_zg(\sigma)=\sum_i w_i(\sigma)
\left[e^{zq_i\mathbf1_{i\in\{0,2\}}}g(\sigma^{[i]})-g(\sigma)\right].
\]

Its dominant eigenvalue \(k(z)\), analytic near \(z=0\) by irreducibility, generates the limiting cumulants: \(k'(0)=\lim t^{-1}\mathbb E Q_t\) and \(k''(0)=\lim t^{-1}\operatorname{Var}(Q_t)\). Set \(L_1=\partial_zL_z|_{0}\) and \(L_2=\partial_z^2L_z|_{0}\). Since \(q_i^3=q_i\) for even-site flips, their action on the constant function is

\[
f=L_1\mathbf1=\frac U2-a(1+W),\qquad
v=L_2\mathbf1=1+W-\frac{aU}{2}.
\]

The mean follows from the stationary moments:

\[
k'(0)=\langle f\rangle=\frac{b-a}{2}=:j.
\]

An explicit centered Poisson corrector is obtained from

\[
h_0=\frac{U+bV-aW}{8},\qquad
Lh_0=j-f,\qquad
\langle h_0\rangle=\frac{a+b}{4(2-ab)}.
\]

Indeed \(h=h_0-\langle h_0\rangle\) obeys \(Lh=j-f\) and \(\langle h\rangle=0\). Differentiate the tilted eigenvalue equation twice, using the normalized eigenfunction \(1+zh+O(z^2)\), to obtain the standard finite-state Poisson identity

\[
k''(0)=\langle v+2L_1h\rangle
=\langle v+2L_1h_0\rangle-2j\langle h_0\rangle.
\]

A direct four-spin calculation (the supplied checker verifies it for all 16 configurations as an identity in \(a,b\)) yields

\[
v+2L_1h_0
=\frac{a^2+2}{4}-\frac{5a+b}{8}U
+\frac{ab+2}{4}V+\frac{a^2+2}{4}W
+\frac{ab+2}{4}P.
\]

Substituting the four stationary moments and \(\langle h_0\rangle\) cancels the apparent denominators and gives exactly

\[
k''(0)=\frac{8-a^2-6ab-b^2}{16}.
\]

Writing \(a=\bar\gamma-j\) and \(b=\bar\gamma+j\) gives \(k''(0)=(1-\bar\gamma^2)/2+j^2/4\). For \(a=0\), division by \(j=b/2>0\) gives \(F(b)=1/b-b/8\), with derivative \(-1/b^2-1/8<0\). The unique positive solution of \(F(b)=1\) is \(b=2\sqrt6-4\), which lies in \((0,1)\). This proves all stated conclusions.

## Verification

Run `python verify_heat.py` with Python 3 and SymPy (specified in `requirements.txt`). The program reconstructs the sixteen spin states and all four physical flip transitions. It checks every displayed generator, current, corrector, and second-cumulant identity symbolically for all sixteen configurations, then independently builds the complete 16-by-16 forward generator and its two tilted derivatives for eight exact rational pairs \((a,b)\). It obtains a stationary law and the derivative of the tilted stationary eigenvector by independent rational linear solves, and compares the resulting cumulants with the theorem. All checks passed. The analytic generator and Poisson identities, not the eight finite parameter tests, prove the parameter-wide statement.

## Relationship to prior work

Schmüser and Schmittmann (2002, arXiv:cond-mat/0206345) define this alternating-bath Glauber dynamics and analyze its nonequilibrium stationary law perturbatively; Section V derives mean heat transfer and entropy production. Schmittmann and Schmüser (2002, arXiv:cond-mat/0212616) give an exact representation of stationary **equal-time** correlations for general even rings, including a finite-ring appendix. Those static results and the earlier exact mean are not claimed as new. They do not supply the time-integrated second cumulant, the displayed mean–variance identity, or the unit-dispersion threshold of the four-spin heat-exchange trajectory. Lebowitz and Spohn (1998/1999, arXiv:cond-mat/9811220) establish general fluctuation-theorem machinery for Markov jump currents; the use of tilted generators and the Poisson response is standard, whereas the explicit polynomial evaluation in this interacting four-spin example is the present point. Existing broader derivations might yield the same formula by further computation; the bibliographic comparison is not exhaustive.

## Limitations

The claim is confined to the four-site periodic Ising ring with rates exactly as stated and \(0\le a,b<1\). It concerns only the first two long-time cumulants of signed even-bath heat in units of \(4J\), not its full large-deviation function, event-count Fano factor, finite-time distribution, arbitrary ring lengths, other bath assignments, or a thermodynamic phase transition. The strict zero-temperature boundary \(a=1\) or \(b=1\) is outside the proved irreducible domain; formulas may have continuous limits there without asserting a unique stationary law at every such boundary.

## References

1. F. Schmüser and B. Schmittmann, “Non-equilibrium stationary state of a two-temperature spin chain,” arXiv:cond-mat/0206345 (first public 2002-06-18), https://arxiv.org/abs/cond-mat/0206345.
2. B. Schmittmann and F. Schmüser, “Exact stationary correlations for a far-from-equilibrium spin chain,” arXiv:cond-mat/0212616 (first public 2002-12-27), https://arxiv.org/pdf/cond-mat/0212616.
3. J. L. Lebowitz and H. Spohn, “A Gallavotti–Cohen type symmetry in the large deviation functional for stochastic dynamics,” arXiv:cond-mat/9811220 (first public 1998-11-16), https://arxiv.org/pdf/cond-mat/9811220.
