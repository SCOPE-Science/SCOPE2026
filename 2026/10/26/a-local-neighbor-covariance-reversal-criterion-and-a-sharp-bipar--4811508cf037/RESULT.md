# A local-neighbor covariance reversal criterion and a sharp bipartite threshold for exclusion with resetting

## Finding
For a connected finite undirected simple graph \(G=(V,E)\) with \(n\ge3\) vertices, run symmetric simple exclusion with each allowed particle-vacancy edge exchange occurring at rate one. Fix a reset configuration \(S\subseteq V\) of \(k\) occupied vertices, where \(2\le k<n\), and reset the **entire** configuration to \(S\) at an independent Poisson rate \(r>0\). For two distinct vertices \(x,y\in S\), write \(A_x=N_G(x)\setminus S\), \(A_y=N_G(y)\setminus S\), \(d_x=|A_x|\), \(d_y=|A_y|\), and \(c=|A_x\cap A_y|\). If \(C_r(x,y)\) is their stationary occupation covariance, then
\[
\lim_{r\downarrow0}C_r(x,y)=-\frac{k(n-k)}{n^2(n-1)},\qquad
\lim_{r\to\infty}r^2 C_r(x,y)=d_xd_y-2c.
\]
In particular, \(d_xd_y>2c\) guarantees a negative-to-positive covariance reversal at at least one finite reset rate; this sufficient criterion is not claimed to be necessary, and the zero-coefficient boundary is not classified by this limit.

For a sharp solvable family, let \(G=K_{2,m}\), \(m\ge1\), with the two vertices of the size-two part occupied by each reset. For these vertices,
\[
C_r=\frac{m((m-2)r-4)}{(m+r+2)^2(2m+r+2)}.
\]
Consequently the covariance is strictly negative for all \(r>0\) if \(m\le2\). If \(m\ge3\), it changes sign **exactly once**, at \(r=4/(m-2)\), from negative to positive. Thus a coordination threshold of three vacant common neighbors produces an exact, finite-system correlation phase diagram.

As another direct consequence, on every even cycle with at least four vertices, resetting to a consecutive occupied half-block forces a negative-to-positive stationary covariance reversal between the two occupied boundary vertices. In the four-cycle this covariance is exactly \((r-2)/((r+2)^2(r+6))\).

## Assumptions and scope
The graph is finite, connected, undirected, and simple. Exclusion has exactly \(k\) particles and rate-one symmetric exchanges on each undirected edge with one occupied and one vacant endpoint. Resetting instantaneously replaces **all** particle positions by the fixed configuration \(S\); there are no other creation, annihilation, or boundary processes. Reset times are independent Poisson events. The stationary law exists uniquely for each \(r>0\) on the \(k\)-particle configuration space. The limits are first taken at **fixed graph**; no simultaneous graph-size and rate limit is asserted. Covariance is connected: \(C_r(x,y)=\mathbb E_r[\eta_x\eta_y]-\mathbb E_r[\eta_x]\mathbb E_r[\eta_y]\).

## Proof
**1. Exact stationary renewal law.** Let \(L\) be the generator of ordinary exclusion on the finite set of \(k\)-subsets of \(V\), with semigroup \(P_t=e^{tL}\). Independence of the reset clock gives, for every observable \(f\),
\[
\pi_r(f)=r\int_0^\infty e^{-rt}(P_t f)(S)\,dt.
\]
Equivalently \(\pi_r=r\delta_S(rI-L)^{-1}\). Every configuration communicates with \(S\) under the reset, and ordinary exclusion connects all \(k\)-subsets of a connected graph, establishing a unique stationary probability distribution. Because the state space is finite, this resolvent is rational and continuous in \(r>0\).

**2. Weak resetting.** Ordinary finite connected symmetric exclusion has the uniform stationary distribution on all \(\binom nk\) configurations, by edge-exchange detailed balance. The finite irreducible chain converges to it as \(t\to\infty\), so the renewal integral tends to that law as \(r\downarrow0\). For distinct vertices \(x,y\), the uniform moments are \(\mathbb E[\eta_x]=k/n\) and \(\mathbb E[\eta_x\eta_y]=k(k-1)/(n(n-1))\). Their difference is exactly \(-k(n-k)/(n^2(n-1))<0\).

**3. A two-jump short-time identity.** Put \(U=1-\eta_x\) and \(V=1-\eta_y\). Both vanish at the reset state. Only hops from \(x\) to an initially vacant neighbor can create \(U\) in one transition, and similarly for \(V\). Hence the ordinary process, started from \(S\), satisfies
\[
\mathbb E_S[U(t)]=d_x t+O(t^2),\quad
\mathbb E_S[V(t)]=d_y t+O(t^2).
\]
To have both \(U=V=1\) in two exchanges, the two occupied particles initially at \(x,y\) must each hop to **distinct** initially vacant destinations; there are \(d_xd_y-c\) unordered choices of ordered-by-origin destination pairs. Both temporal orderings are allowed and contribute the same product of unit rates. In the semigroup Taylor expansion, their combined \(2(d_xd_y-c)\) coefficient in \(L^2(UV)(S)\), divided by \(2!\), gives
\[
\mathbb E_S[U(t)V(t)]=(d_xd_y-c)t^2+O(t^3).
\]
The finite generator makes every remainder uniform near \(t=0\). Integrating the short-time expansions against \(re^{-rt}dt\), with \(\int_0^\infty rt^j e^{-rt}dt=j!/r^j\), gives
\[
\mathbb E_r U=\frac{d_x}{r}+O(r^{-2}),\quad
\mathbb E_r V=\frac{d_y}{r}+O(r^{-2}),\quad
\mathbb E_r UV=\frac{2(d_xd_y-c)}{r^2}+O(r^{-3}).
\]
Thus \(C_r(x,y)=\operatorname{Cov}_r(U,V)=(d_xd_y-2c)/r^2+O(r^{-3})\). If its leading coefficient is positive, continuity together with the strictly negative weak-reset limit yields a genuine sign reversal and a zero at an intermediate positive rate.

**4. Exact \(K_{2,m}\) occupation chain.** Let \(J\in\{0,1,2\}\) be the number of occupied vertices in the two-vertex part. For \(m=1\), state \(J=0\) is inaccessible and has zero stationary weight; the equations below remain valid with this zero-weight formal state. The other part contains \(2-J\) particles. Ordinary exclusion has rates \(0\to1:4\), \(1\to0:m-1\), \(1\to2:1\), and \(2\to1:2m\). Whole-configuration resetting sends states \(J=0,1\) to \(J=2\) at rate \(r\). The lumped stationary equations, together with normalization, have denominator \(H=(m+r+2)(2m+r+2)\) and exact solution
\[
 p_0=\frac{2m(m-1)}H,\qquad
 p_1=\frac{2m(r+4)}H,\qquad
 p_2=\frac{r^2+(m+4)r+4}H.
\]
In each \(J=1\) state, symmetry gives occupancy probability one half for each distinguished vertex, while both are occupied precisely if \(J=2\). Therefore \(\mathbb E_r\eta_x=\mathbb E_r\eta_y=p_2+p_1/2\) and \(\mathbb E_r\eta_x\eta_y=p_2\). Substitution and factorization yield
\[
 p_2-(p_2+p_1/2)^2=\frac{m((m-2)r-4)}{(m+r+2)^2(2m+r+2)}.
\]
All denominator factors are positive. For \(m\le2\) the numerator is negative at all positive rates. For \(m\ge3\) it has the unique simple zero \(4/(m-2)\), with the claimed strict signs.

**5. Cycles and a common-destination obstruction.** On a cycle of \(2m\ge4\) vertices, start from the occupied consecutive block \(S=\{0,\ldots,m-1\}\). The two occupied boundary vertices each have one initially empty neighbor, and those neighbors are distinct, so \(d_x=d_y=1\), \(c=0\), and step 3 forces the reversal. In the four-cycle the exact six-configuration resolvent simplifies to \((r-2)/((r+2)^2(r+6))\). Conversely, the length-two path with occupied endpoints has \(d_x=d_y=c=1\): a shared initial vacancy leads to the exact always-negative covariance \(-1/(r+3)^2\). These computations demonstrate the geometric distinction between independent and competing departure routes.

## Verification
A standalone script `verify.py` rederives the \(K_{2,m}\) three-state stationary probabilities symbolically for nine values of \(m\), verifies the closed covariance formula, compares against independently constructed full finite-configuration Markov generators for seven values of \(m\) and eight rates each, checks small/large-rate behavior on cycles, and verifies the four-cycle identity by an exact symbolic six-state resolvent. It reports **251 successful symbolic and numerical checks**. These finite checks are independent corroboration; the preceding general finite-graph and all-integer \(m\) proof is analytical. Run `python verify.py` with Python 3, NumPy and SymPy.

## Relationship to prior work
Basu, Kundu and Pal (2019) introduced fixed step-configuration stochastic resetting for symmetric exclusion, studied density profiles and integrated currents, and supplied the renewal framework. Sadekar and Basu (2020) investigated spatial correlations under **dichotomous resetting** to two complementary profiles, reporting a spatial-correlation renewal expression and a nearest-neighbor relation but not the fixed-single-state finite-graph covariance sign criterion or \(K_{2,m}\) phase diagram. Mishra and Basu (2022) addressed **power-law waiting times** and density/current statistics rather than this Poisson finite-graph threshold. Mendonça (2012) exactly diagonalized ordinary exclusion generators on complete bipartite graphs without configuration resetting; its spectral results alone do not explicitly give the reset stationary covariance threshold. The result here is the combined geometric coefficient, universal low-rate sign, and exact topology-controlled sign transition, not the underlying renewal identity or the existence of correlations under resetting.

## Limitations
The finite-graph asymptotics do not identify every possible sign reversal, nor classify the equality case \(d_xd_y=2c\). The \(K_{2,m}\) classification is exact but specialized to resetting both vertices of the two-vertex part. Neither the general condition nor the cycle corollary establishes uniqueness of the transition outside \(K_{2,m}\). All limits keep graph size and particle count fixed. No thermodynamic-limit scaling, non-Poisson resetting extension, nor asymmetric exclusion result is claimed. Scholarly priority remains subject to independent comparison with the wider literature on restart resolvents and exclusion correlations.

## References
1. U. Basu, A. Kundu and A. Pal, “Symmetric Exclusion Process under Stochastic Resetting,” arXiv:1906.11801, first public June 27, 2019. https://arxiv.org/abs/1906.11801
2. O. Sadekar and U. Basu, “Zero-current Nonequilibrium State in Symmetric Exclusion Process with Dichotomous Stochastic Resetting,” arXiv:2004.00951, first public April 2, 2020. https://arxiv.org/abs/2004.00951
3. S. Mishra and U. Basu, “Symmetric Exclusion Process under Stochastic Power-law Resetting,” arXiv:2211.14120, first public November 25, 2022. https://arxiv.org/abs/2211.14120
4. J. R. G. Mendonça, “Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs,” arXiv:1207.4106, first public July 17, 2012. https://arxiv.org/abs/1207.4106
