# Exact inoculum basin and partner-imbalance law in a three-species ecological-fitting system

## Finding
For the three-species ecological-fitting model below, a harmful newcomer that **cannot invade an infinitesimal resident equilibrium** can nevertheless cause extinction of the entire community if its initial inoculum is sufficiently large. The exact boundary, valid for every positive initial triple including unequal resident abundances, is a one-dimensional beta-type integral. Near loss of one resident mutualist the required inoculum vanishes with an explicit fractional power.

Let \(a>0\), \(0<c<a/2\), \(d<0\), and \(\mu>0\). Set \(k=a/2-c>0\), \(q=k/a\in(0,1/2)\). With residents' initial sum \(R=N_1(0)+N_2(0)\), invader inoculum \(I=N_3(0)\), and partner imbalance
\[
r=\left(\frac{N_1(0)-N_2(0)}{R}\right)^2\in[0,1),\qquad
T(r)=\frac1a\int_0^1\frac{t^{q-1}}{\sqrt{1-r+rt}}\,dt,
\]
the exact critical inoculum is
\[
I_c(R,r)=\frac{R}{(-d)T(r)}.
\]
There are precisely three outcomes for strictly positive initial conditions: if \(I<I_c\), the residents recover and the invader vanishes; if \(I=I_c\), all three species approach a positive (basin-boundary) equilibrium; if \(I>I_c\), all three populations vanish. In the last case the total population satisfies the sharp algebraic law \(\lim_{t\to\infty}\mu t(N_1+N_2+N_3)=1\), although the invader becomes asymptotically the entire *fraction* of the declining population.

The critical initial invader fraction \(z_c(r)=[1+(-d)T(r)]^{-1}\) decreases strictly with imbalance. It satisfies
\[
z_c(0)=\frac{k}{k-d},\qquad
z_c(r)\sim \frac{a}{(-d)B(1/2-c/a,c/a)}(1-r)^{c/a}\quad(r\uparrow1).
\]
Here \(B\) is Euler's beta function. For balanced residents with \((a,c,d)=(2,1/2,-1)\), the collapse threshold is exactly one-third of the total initial population (equivalently, invader inoculum equal to half the resident sum).

## Assumptions and scope
The physical abundances \(N_i(t)>0\) satisfy for all \(t\ge0\)
\[
\dot N_i=N_i\left[\sum_{j\ne i}J_{ij}\frac{N_j}{N}-\mu N\right],\qquad N=N_1+N_2+N_3,
\]
where \(J=\begin{pmatrix}0&a&d\\a&0&d\\c&c&0\end{pmatrix}\). The two residents are obligate mutualists (positive cross-benefit \(a\)); the outsider gains \(c\) from either resident but damages both equally (\(d<0\)); all taxa consume a common crowding-limited resource. All four inequalities on parameters are strict. No species can persist alone in the model. Results are deterministic; no demographic noise, migration, or extinction cutoff is imposed. The initial community need not be at its pair equilibrium.

## Proof
**1. Positivity and separation.** The vector field is smooth in the positive orthant. Boundedness follows because the per-capita interaction term is bounded above by the largest \(J_{ij}\) and \(\dot N\le N(C-\mu N)\). Positivity is preserved and no finite-time extinction occurs. Define frequencies \(x_i=N_i/N\), invader share \(z=x_3\), resident share \(p=x_1+x_2=1-z\), resident contrast \(y=(x_1-x_2)/p\), and imbalance \(r=y^2\). The common crowding term cancels from frequency dynamics:
\[
\dot x_i=x_i[(Jx)_i-x^TJx],\quad
\dot r=-a p r(1-r),\quad
\dot z=z p\left[\left(c-\frac a2(1-r)\right)p-dz\right].
\]
These identities hold exactly, including \(r=0\). Introduce ecological time \(s(t)=\int_0^t p(u)\,du\). Let \(w=p/z\) (resident-to-invader odds) and \(A(r)=c-a(1-r)/2\). Exact differentiation gives
\[
\frac{dr}{ds}=-a r(1-r),\qquad \frac{dw}{ds}=-A(r)w+d.
\]

**2. Integrating factor.** If \(r_0=r(0)\in[0,1)\), its exact solution is
\[
r(s)=\frac{r_0}{r_0+(1-r_0)e^{as}}.
\]
Hence the positive integrating factor for the odds equation is
\[
H(s)=\exp\left(\int_0^s A(r(u))\,du\right)
=\frac{e^{cs}}{\sqrt{r_0+(1-r_0)e^{as}}}.
\]
Since \(k=a/2-c>0\), \(H(s)=O(e^{-ks})\); the exact solution is
\[
w(s)=\frac{w_0+d\int_0^sH(u)\,du}{H(s)},\qquad w_0=R/I.
\]
The substitution \(t=e^{-as}\) proves
\[
\int_0^\infty H(s)\,ds=\frac1a\int_0^1t^{q-1}(1-r_0+r_0t)^{-1/2}\,dt=T(r_0).
\]
The numerator is strictly decreasing because \(d<0\); its terminal sign gives the complete basin trichotomy.

**3. Recovery and the separatrix.** If \(w_0>(-d)T(r_0)\), the numerator stays positive and tends to a positive constant, so \(w(s)\to\infty\), \(z(s)\to0\), and \(r(s)\to0\). If equality holds, the numerator equals \((-d)\int_s^\infty H(u)\,du\), and the exponential tail gives \(w(s)\to(-d)/k\), \(z(s)\to k/(k-d)\), and \(p(s)\to(-d)/(k-d)\). In both cases \(s(t)\to\infty\): were \(s\) bounded, the positive limiting value of \(p=w/(1+w)\) would force \(ds/dt=p\) bounded below, a contradiction. The total-population equation
\[
\dot N=N(\Phi-\mu N),\qquad
\Phi=x^TJx=\frac a2p^2(1-r)+(c+d)zp
\]
then yields \(N\to a/(2\mu)\) for recovery, and \(N\to c(-d)/[\mu(k-d)]\) on the separatrix, using the standard scalar logistic comparison for \(\Phi\) converging to a positive limit. Multiplication by the limiting frequencies gives the individual limits: on the separatrix
\[
N_1=N_2\to \frac{c(-d)}{2\mu(k-d)},\qquad
N_3\to\frac{ck}{\mu(k-d)}.
\]
The equality surface is the exact stable separatrix, not an open basin of positive coexistence.

**4. Total collapse and its rate.** If \(w_0<(-d)T(r_0)\), its numerator reaches zero once at a finite \(s_*\). As \(s\uparrow s_*\), \(w(s)\downarrow0\), with \(w'(s_*)=d<0\). Hence \(p=w/(1+w)\sim(-d)(s_*-s)\). Since \(ds/dt=p\), physical time tends to infinity as \(s\uparrow s_*\); moreover \(p(t)\) decays exponentially at rate \(d<0\). Consequently \(\Phi(t)=O(p(t))\) is absolutely integrable on the half line, while \(z(t)\to1\). For \(U=1/N\),
\[
\dot U=\mu-\Phi(t)U,\qquad
U(t)=e^{-F(t)}\left(U(0)+\mu\int_0^t e^{F(v)}dv\right),\quad F(t)=\int_0^t\Phi(v)dv.
\]
As \(F(t)\) has a finite limit, \(U(t)/t\to\mu\). Thus \(\mu tN(t)\to1\), and every absolute abundance tends to zero; in particular \(N_3\sim1/(\mu t)\). This is whole-community collapse rather than positive establishment of the invader.

**5. Threshold monotonicity and near-singleton scaling.** Differentiation under the integral gives
\[
T'(r)=\frac1{2a}\int_0^1\frac{t^{q-1}(1-t)}{(1-r+rt)^{3/2}}\,dt>0\quad(0\le r<1).
\]
For \(\epsilon=1-r\downarrow0\), substitute \(t=\epsilon u\) and apply dominated convergence, using \(0<q<1/2\), to obtain
\[
T(r)\sim \frac{\epsilon^{q-1/2}}a\int_0^\infty\frac{u^{q-1}}{\sqrt{1+u}}\,du
=\frac{B(q,c/a)}{a}\epsilon^{-c/a}.
\]
Combining this with \(z_c=[1+(-d)T]^{-1}\) gives the stated exponent. At \(r=0\), \(T(0)=1/k\) exactly. The invader's rare-growth exponent at the resident-only equilibrium is \(c-a/2=-k<0\), proving that the finite-inoculum collapse cannot be inferred from the ordinary linear-invasion test.

## Verification
Run the accompanying `verify.py` with Python, NumPy, SciPy and SymPy. It checks frequency-coordinate identities symbolically, the exact balanced threshold, monotonic threshold values across six imbalances, the beta-power asymptotic at three near-extreme imbalances, and six high-accuracy ODE integrations on both sides of the predicted basin boundary. Representative checks use \((a,c,d,\mu)=(2,1/2,-1,1/100)\), \(r\in\{0,1/4,16/25\}\), and inocula at half or 1.6 times the critical initial *fraction*. These finite checks illustrate and guard the formulas; global-time statements follow from the analytical proof above.

## Relationship to prior work
Arthur, Nicholson and Wilkinson (2026, arXiv:2609.34956v1) define the shared-crowding interaction law in their equation (2), describe an invasion barrier and multiple outcomes including invasion-triggered total extinction, and simulate random matrices. Their Section 4 and Appendix A do not give this exact all-initial-state three-taxon collapse separatrix, dependence on resident imbalance, or the beta-law exponent. The interaction pattern here is a deterministic allowed choice of their off-diagonal coefficients, not a claim about its frequency under their random ensemble.

Feng, Blumenthal, Mehta and Goyal (2025, arXiv:2503.10865) develop dressed invasion fitness and self-consistent post-invasion communities for a different generalized Lotka–Volterra system, mainly targeting steady-state ecological responses. They do not imply the present initial-inoculum basin partition and algebraic total-collapse law in the shared-crowding, frequency-mediated model. Hale and Valdovinos (2021, DOI:10.1002/ece3.8453) survey low-density mutualistic thresholds in two-species systems, providing conceptual precedent but not this three-taxon invasion calculation.

## Limitations
This exact result relies on two exchange-symmetric resident taxa, equal harm from the invader to both residents, and equal benefit to the invader from both residents. It makes no assertion for arbitrary three-by-three interaction matrices, stochastic extinctions, ongoing immigration, ecological spatial structure, or discrete individual counts. The extinction trajectory has total density decaying as the inverse of time, not an instantaneous loss. A negative *rare* invasion fitness does not imply safety from finite introductions. Mathematical novelty is subject to possible independently obtained equivalent specializations not indexed in the inspected literature.

## References
- R. Arthur, A. Nicholson and D. M. Wilkinson, *Models of Ecological Fitting*, arXiv:2609.34956v1 (first posted 2026-09-28), Sections 2–5 and Appendix A. https://arxiv.org/abs/2609.34956
- Z. Feng, E. Blumenthal, P. Mehta and A. Goyal, *A theory of ecological invasions and its implications for eco-evolutionary dynamics*, arXiv:2503.10865 (2025). https://arxiv.org/abs/2503.10865
- K. R. S. Hale and F. S. Valdovinos, *Ecological theory of mutualism: Robust patterns of stability and thresholds in two-species population models*, Ecology and Evolution (2021). https://doi.org/10.1002/ece3.8453
