# Sharp covariance sign reversals in globally reset complete-graph exclusion

## Finding
Consider a symmetric simple exclusion process on the complete graph with \(N\ge 3\) vertices and exactly \(1\le k\le N-1\) particles. Each unordered edge has a unit-rate exchange clock. A separate Poisson clock of rate \(r>0\) replaces the entire occupation configuration by a fixed configuration \(b\in\{0,1\}^{N}\) with \(k\) occupied vertices. Write \(\ell=N-k\), let \(\eta_i\) denote stationary occupancy at vertex \(i\), and put
\[
D=(N+r)^2(2N+r-2).
\]
The complete two-point stationary covariance classification, for distinct vertices, is
\[
\operatorname{Cov}(\eta_i,\eta_j)=
\begin{cases}
\dfrac{k[(k-2)r-2\ell]}{D},&b_i=b_j=0,\\[5pt]
\dfrac{\ell[(\ell-2)r-2k]}{D},&b_i=b_j=1,\\[5pt]
-\dfrac{r^2+(N+k\ell)r+2k\ell}{D},&b_i\ne b_j.
\end{cases}
\]
A \(00\) pair exists only if \(\ell\ge2\). Its covariance crosses zero exactly once as \(r\) increases if and only if \(k\ge3\), at \(r=2\ell/(k-2)\); it is strictly negative below and strictly positive above. A \(11\) pair exists only if \(k\ge2\). Its covariance crosses exactly once if and only if \(\ell\ge3\), at \(r=2k/(\ell-2)\), with the same strict signs. Every mixed \(01\) pair remains strictly negatively correlated for all \(r>0\). Where no positive-rate crossing is specified, the corresponding existing pair is strictly negative at every finite \(r>0\).

Thus, when \(N\ge5\) and \(2\le k\le N-2\), at least one reset-homogeneous pair class becomes positively correlated for sufficiently rapid resetting. In particular, this stationary law cannot then be negatively associated. This does **not** assert that the absence of positive pairwise covariance establishes negative association.

## Assumptions and scope
The state space is \(\Omega_{N,k}=\{\eta\in\{0,1\}^{N}:\sum_i\eta_i=k\}\). At rate one for each unordered pair \(\{i,j\}\), the two occupations are transposed (an occupied-to-vacant jump when they differ). Every reset independently restores the **entire** fixed configuration \(b\), not each site independently. The rate \(r\) is expressed relative to the unit rate **per edge**, not total unit rate per particle. All assertions concern this unique stationary distribution. The no-reset limit \(r\downarrow0\) is the uniform measure on \(\Omega_{N,k}\).

## Proof
For an observable \(f\), let \(\eta^{ij}\) be the configuration with occupations at \(i,j\) interchanged and define
\[
(\mathcal Lf)(\eta)=\sum_{i<j}\bigl[f(\eta^{ij})-f(\eta)\bigr]+r\bigl[f(b)-f(\eta)\bigr].
\]
The complete graph connects every configuration in \(\Omega_{N,k}\) by allowed exchanges. Hence the continuous-time chain is irreducible for all \(r\ge0\), so its stationary distribution is unique. Write \(m_i=\mathbb E\eta_i\) and \(u_{ij}=\mathbb E(\eta_i\eta_j)\), for distinct \(i,j\).

**First-moment closure.** Every particle outside vertex \(i\) can enter that vertex when it is vacant, and a particle at \(i\) can leave for any vacant vertex. Since the particle count is always \(k\),
\[
\mathcal L_0\eta_i=k-N\eta_i.
\]
Stationarity for \(\mathcal L\eta_i\) gives \((N+r)m_i=k+rb_i\), hence
\[
m_i=\frac{k+rb_i}{N+r}.
\]

**Second-moment closure.** Swapping the occupations of \(i,j\) leaves their product unchanged. Only exchanges between one of these vertices and the remaining \(N-2\) vertices matter. Using \(\eta_i^2=\eta_i\) and \(\sum_h\eta_h=k\), direct summation gives the identity valid at every configuration:
\[
\mathcal L_0(\eta_i\eta_j)=(k-1)(\eta_i+\eta_j)-2(N-1)\eta_i\eta_j.
\]
For the four possibilities \((\eta_i,\eta_j)=(0,0),(1,0),(0,1),(1,1)\), the generator gives respectively \(0,k-1,k-1,-2\ell\), exactly the values of the displayed expression. Stationarity now gives
\[
u_{ij}=\frac{(k-1)(m_i+m_j)+rb_ib_j}{2(N-1)+r}.
\]
Subtracting \(m_im_j\), inserting the exact one-point means, and collecting over the common strictly positive denominator \(D\) yields the three displayed covariance formulas. This derives the whole infinite family without assuming pair independence or extrapolating from finite cases.

**Sign analysis and boundaries.** The numerators for \(00\) and \(11\) classes are affine in \(r\), with negative constant terms \(-2k\ell\) and slopes \(k(k-2)\) and \(\ell(\ell-2)\), respectively. Those slopes are positive precisely at the specified integer thresholds. The mixed-pair numerator is the negative of a polynomial whose coefficients are all strictly positive for \(r>0\). Hence exactly the stated crossings occur, with no unproved uniqueness assumption.

At \(r=0\), all three formulas reduce to
\[
\operatorname{Cov}(\eta_i,\eta_j)=-\frac{k\ell}{N^2(N-1)}\qquad(i\ne j),
\]
in agreement with uniform sampling of \(k\) occupied sites. At large resetting rate, the same-class covariances behave as \(k(k-2)r^{-2}+O(r^{-3})\) and \(\ell(\ell-2)r^{-2}+O(r^{-3})\), whereas mixed covariances behave as \(-r^{-1}+O(r^{-2})\).

## Verification
The accompanying `verify_complete_graph_reset.py` constructs the full finite-state generator, independently solves its invariant distribution, and compares the resulting covariances with the formulas. Tests cover all \(3\le N\le8\), all \(1\le k<N\), six positive resetting rates and every ordered class of unordered vertex pairs: 2,766 covariance comparisons and all one-point means. It also checks the three polynomial identities symbolically. A separate exact-rational generator solve checked \((N,k,r)=(5,3,4)\) and \((6,3,6)\), including zero covariance exactly at the predicted thresholds. The finite checks are not used in place of the proof. Execute the script with Python 3, NumPy, SciPy, and SymPy installed.

## Relationship to prior work
Borcea, Brändén, and Liggett (2007/2009) proved negative-dependence preservation for ordinary symmetric exclusion evolution from deterministic or strongly Rayleigh initial measures. Their statement fixes a deterministic observation time and does not assert closure under an independent random-time mixture produced by repeated global resetting. The new result isolates a sharp mechanism by which that mixture can instead produce positive stationary pair covariance, despite exact particle-number conservation.

Evans and Majumdar (2011) established Poisson resetting and the renewal framework for a diffusive particle. Basu, Kundu, and Pal (2019, arXiv:1906.11801) studied stochastic resetting of symmetric exclusion on a nearest-neighbor ring, deriving density and current statistics. Sadekar and Basu (2020, arXiv:2004.00951) studied two reset configurations on a nearest-neighbor ring and analyzed spatial correlations for their symmetric-reset zero-current state. These sources motivate resetting in interacting transport, but the examined primary texts do not state the complete-graph, one-reset-configuration, all-density stationary covariance classification or the three exact sign regimes above. A general renewal representation by itself does not evaluate the complete-graph pair functions or their sharp sign boundaries.

## Limitations
This theorem treats an all-to-all graph with identical unit edge rates, a fixed number of particles, a single deterministic reset configuration, and Poisson reset times. It does not claim a comparable sign classification for general graphs, site-dependent rates, independent single-site resetting, or multiple stochastic reset states. It identifies when pairwise negative covariance is violated; where all pairwise covariances are nonpositive, higher-order negative association is not established. Literature comparison supports originality only within the specifically examined sources; unindexed equivalent specializations remain a residual risk. No independent mathematical audit has been performed.

## References
1. J. Borcea, P. Brändén, T. M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340 (first public 2007-07-16); J. Amer. Math. Soc. 22 (2009), 521–567. Sections 3.5 and 5.
2. M. R. Evans, S. N. Majumdar, *Diffusion with stochastic resetting*, arXiv:1102.2704 (first public 2011-02-14); Phys. Rev. Lett. 106 (2011), 160601.
3. U. Basu, A. Kundu, A. Pal, *Symmetric exclusion process under stochastic resetting*, arXiv:1906.11801 (first public 2019-06-27); Phys. Rev. E 100 (2019), 032136. Sections II–V and appendices.
4. O. Sadekar, U. Basu, *Zero-current nonequilibrium state in symmetric exclusion process with dichotomous stochastic resetting*, arXiv:2004.00951 (first public 2020-04-02). Especially Sections 2 and 5.3.
