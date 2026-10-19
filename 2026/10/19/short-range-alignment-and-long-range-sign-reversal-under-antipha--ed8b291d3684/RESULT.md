# Short-range alignment and long-range sign reversal under antiphasic switching boundaries

## Finding

A single, common, independently switching environment drives two competing boundary opinions on a finite voter chain. **Nearest-neighbor correlations remain positive at every switching speed, but every pair separated by more than half the extended chain changes from negative to positive stationary correlation between slow and fast switching.** In the first chain with this effect, the zero is unique and explicit.

Fix any integer \(N\ge2\) and switching rate \(\kappa>0\). For \(1\le i<j\le N\), define the stationary covariance \(C_{i,j}(\kappa)=\operatorname{Cov}(\sigma_i,\sigma_j)\). Then:

1. For each \(1\le i<N\), \(C_{i,i+1}(\kappa)>0\) for all \(\kappa>0\).
2. For every pair, with \(d=j-i\),
   \[
   \lim_{\kappa\downarrow0}C_{i,j}(\kappa)=1-\frac{2d}{N+1},\qquad
   \lim_{\kappa\to\infty}C_{i,j}(\kappa)=p_{i,j}>0.
   \]
   Here \(p_{i,j}\) is the probability that two independent nearest-neighbor dual walkers starting at the indicated sites coalesce before either hits an exterior boundary. Thus whenever \(d>(N+1)/2\), at least one positive switching rate has \(C_{i,j}(\kappa)=0\).
3. For four interior sites, the pair of extreme sites satisfies
   \[
   C_{1,4}(\kappa)=\frac{32\kappa^2+14\kappa-11}{11(16\kappa^2+20\kappa+5)},
   \qquad \kappa_* =\frac{\sqrt{401}-7}{32}=0.4070307623281496\ldots.
   \]
   This is the unique positive zero of the endpoint covariance.

## Assumptions and scope

Spins are in \(\{-1,+1\}\) on interior sites \(1,\ldots,N\). At each interior site, independent Poisson arrows of rate \(1/2\) arrive from each of its two neighbors; upon an arrow, the site copies the corresponding neighboring spin. An independent two-state process \(Z_t\) flips sign at rate \(\kappa\). Throughout, the exterior sites are prescribed by \(\sigma_0(t)=Z_t\) and \(\sigma_{N+1}(t)=-Z_t\); they never copy interior spins. The two boundaries switch *synchronously* and remain antiphasic, not independently.

The finite system has a unique stationary distribution. One construction runs stationary telegraph noise and stationary voter arrows from the remote past. Each backwards ancestral line on a finite interval eventually reaches an exterior boundary almost surely, so interior spins cease to depend on arbitrary initial data. Stationarity is invariant under simultaneous inversion of \(Z\) and all interior spins, and uniqueness implies \(\mathbb E[\sigma_i]=0\). Thus the covariance equals \(\mathbb E[\sigma_i\sigma_j]\).

## Proof

Put \(L=N+1\), \(a_i=\mathbb E[Z\sigma_i]\), and \(b_{i,j}=\mathbb E[\sigma_i\sigma_j]\) at stationarity. Since the environment flips at rate \(\kappa\), the mixed moments obey
\[
(2+4\kappa)a_i=a_{i-1}+a_{i+1}\quad(1\le i\le N),\qquad a_0=1,\quad a_L=-1.
\]
The unique solution has \(a_{L-i}=-a_i\). For pairs \(1\le i<j\le N\), the voter generator gives a discrete harmonic Dirichlet problem
\[
4b_{i,j}=b_{i-1,j}+b_{i+1,j}+b_{i,j-1}+b_{i,j+1},
\quad b_{i,i}=1,\quad b_{0,j}=a_j,\quad b_{i,L}=-a_i.
\]
The finite Dirichlet problem is unique by the maximum principle, or by the finite absorbing dual-walk representation. Its coefficients are independent of \(\kappa\) and its boundary data depend continuously on \(\kappa\), hence all \(b_{i,j}\) are continuous in \(\kappa>0\) and have the limits used below.

As \(\kappa\downarrow0\), the unique solution of the first recurrence approaches \(a_i=1-2i/L\). The function \(b_{i,j}=1-2(j-i)/L\) is harmonic in the pair-domain, equals one on the diagonal, and matches both exterior boundary values. Uniqueness proves the displayed slow-switching limit. Equivalently, each frozen-boundary stationary chain contains one uniformly wandering domain wall; the wall picture itself is classical.

As \(\kappa\to\infty\), the first recurrence implies \(a_i\to0\) at every interior site. The limiting pair problem therefore has zero exterior values and diagonal value one. It is precisely the harmonic-measure problem for two backwards independent simple random walks, moving at total rate one each, stopped upon first coalescence or first hit of exterior site \(0\) or \(L\). Its solution is \(p_{i,j}\), the probability that coalescence happens first. From any pair of interior sites, a finite legal inward sequence of jumps can cause coalescence without exiting the interval, so \(p_{i,j}>0\). Continuity and the strict negative slow-switching value for \(j-i>L/2\) give at least one zero.

For adjacent sites, use the same backwards dual construction without taking a limit. The first active arrow from either ancestral site arrives after an exponential waiting time and has four equally likely orientations. The two inward arrows coalesce the lineages immediately, giving the spin product \(+1\) with probability \(1/2\). On the remaining paths the spin product is at least \(-1\). Hence \(b_{i,i+1}\ge0\). For \(N\ge3\), at least one of the outward arrows remains in the interior, after which a positive-probability inward sequence causes coalescence; this makes the bound strict. For \(N=2\), the moment equations give directly \(b_{1,2}=(1-1/(3+4\kappa))/2>0\).

For \(N=4\), symmetry and the mixed-moment recurrence yield
\[
D_0=16\kappa^2+20\kappa+5,\quad a_1=\frac{3+4\kappa}{D_0},\quad a_2=\frac1{D_0},\quad a_3=-a_2,\quad a_4=-a_1.
\]
Reflection of the pair equations yields \(b_{2,4}=b_{1,3}\), \(b_{3,4}=b_{1,2}\), and the identities
\[
11b_{1,3}=4-3a_2-2a_1,\qquad 2b_{1,4}=b_{1,3}-a_1.
\]
Substitution gives the stated rational expression. Its denominator is positive for positive \(\kappa\). Its numerator has exactly one positive root, namely \((\sqrt{401}-7)/32\), proving the four-site assertion.

## Verification

The accompanying pure-Python script `verify_telegraph_voter.py` constructs the complete Markov generator on all \(2^{N+1}\) states (including the telegraph sign), solves for the stationary law, and independently solves the closed moment equations. It checks 175 two-site moment comparisons over \(N=2,3,4,5,6\) and five switching rates, and six further four-site rational-formula evaluations. These finite tests are reproducibility checks only; the argument above proves all quantified sizes.

## Relationship to prior work

Static competing zealots and a uniformly wandering domain wall are treated in Mobilia, Georgiev (2004/2005), and Mobilia, Petersen, Redner (2007). The limiting frozen-boundary linear correlation is not claimed to be a new domain-wall result. Caligiuri and Galla (2023) study noisy voter models in stochastic environments, including coherently switching influencer groups, on a fully connected population. Their model has no pair of spatially opposite boundary inputs and does not give the finite-interval pair-sign theorem. The contribution here is the joint **spatial** sign separation at all finite lengths under *antiphasic telegraph boundary driving*, and the exact smallest-chain crossover. The generic Markov-chain and duality methods are not claimed to be new.

## Limitations

Existence, not uniqueness, of a positive crossing is proved for general long-separated pairs. No sign classification is claimed for nonadjacent pairs whose separation is at most half the extended interval. The exact rational crossover is established only for four interior sites. Full bibliographic exclusion of every earlier equivalent formulation is not established, especially for specialized treatments of spatial voter systems with nonstatic zealots.

## References

1. M. Mobilia and I. T. Georgiev, *Voting and Catalytic Processes with Inhomogeneities*, first public arXiv version 13 December 2004, `arxiv:cond-mat/0412306`; Phys. Rev. E 71, 046102 (2005).
2. M. Mobilia, A. Petersen and S. Redner, *On the Role of Zealotry in the Voter Model*, first public arXiv version 20 June 2007, `arxiv:0706.2892`; J. Stat. Mech. P08029 (2007).
3. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, first public arXiv version 30 May 2023, `arxiv:2305.19096`; Phys. Rev. E 108, 044301 (2023).
