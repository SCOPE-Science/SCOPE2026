# An exact finite-size trapping-delay resonance for alternating antipodal gates on a directed cycle

## Finding

Let \(k\ge1\) be an integer. On a directed cycle of \(2k\) sites, one particle moves clockwise to the next site at independent rate one. Two diametrically opposite sites, \(0\) and \(k\), are possible perfect traps. Independently of the particle, a symmetric two-state gate switches at rate \(g\ge0\): in gate state \(0\), only site \(0\) absorbs; in gate state \(1\), only site \(k\) absorbs. Absorption is immediate whenever the particle occupies the currently active trap, including at time zero. Initially its position is uniform on all \(2k\) sites and the gate state is uniform and independent. Let \(T\) denote absorption time. Then for every \(k\ge1\) and \(g\ge0\),

\[
\boxed{\mathbb E[T]=M_k(g)=\frac{k-1}{2}+\frac{k(1+2g)^{k-1}}{1+(1+2g)^k}.}
\]

For \(k=1,2\), the mean is strictly decreasing in \(g\) on \([0,\infty)\). For each \(k\ge3\), it has precisely one strict global **maximum**, at

\[
\boxed{g_{*,k}=\frac{(k-1)^{1/k}-1}{2}.}
\]

The peak value and its asymptotic effect are

\[
M_k(g_{*,k})=\frac{k-1}{2}+(k-1)^{1-1/k},\qquad
 g_{*,k}\sim\frac{\log k}{2k},\qquad
 \frac{M_k(g_{*,k})}{M_k(0)}\longrightarrow\frac32.
\]

Thus slowing or accelerating the switching relative to an optimal, strictly positive finite rate can **shorten** expected absorption time on every directed cycle with at least six sites; at large sizes the maximal delay is fifty percent larger than the static-gate mean.

## Assumptions and scope

The graph is the finite clockwise directed cycle \(C_{2k}^{\rightarrow}\), not an undirected cycle. The motion is a Poisson process of rate one with deterministic clockwise steps; there are no reverse jumps, holding sites, or particle-particle interactions. The independent gate jumps between its two states with symmetric transition rates \(g\). Exactly one of two antipodal sites is perfectly absorbing at every instant, and switching while at the newly active trap absorbs immediately. The initial joint law is uniform across all \(4k\) possible site–gate pairs; an initially active-trap configuration has absorption time zero. This unconditional convention is needed for the formula. If instead the initial law is conditioned on nonabsorption at time zero, its mean is \(\frac{2k}{2k-1}M_k(g)\), so the optimal switching rate is unchanged. At \(g=0\), one fixed trap remains absorbing and absorption is almost sure as the walker completes circuits. For \(g>0\), finite-state irreducibility before killing likewise makes absorption almost sure with finite expectation.

## Proof

**1. Reduction.** Let \(X_t\in\mathbb Z/(2k\mathbb Z)\) be the position and \(E_t\in\{0,1\}\) the gate, and set \(Y_t=X_t-kE_t\pmod{2k}\). Then \(Y_t=0\) if and only if the walker is at the currently active trap. Before absorption, a walker jump changes \(Y\) to \(Y+1\) at rate one; a gate flip changes \(Y\) to \(Y+k\) at rate \(g\), since both \(+k\) and \(-k\) are the same residue modulo \(2k\). The initial \(Y\) is uniform. On the un-killed full cycle the generator is

\[
(\mathcal Lf)(y)=f(y+1)-f(y)+g\bigl(f(y+k)-f(y)\bigr).
\]

Let \(h(y)\) be the expected hitting time of \(0\) by this chain. Its boundary equation is \(h(0)=0\), and \(\mathcal Lh(y)=-1\) for every \(y\ne0\). Since the uniform distribution is stationary for \(\mathcal L\), summing \(\mathcal Lh\) over all sites shows \(\mathcal Lh(0)=2k-1\). Therefore over the entire periodic cycle, with \(N=2k\),

\[
\mathcal Lh=-\mathbf1+N\delta_0.
\]

**2. Fourier solution.** Let \(z_\ell=e^{2\pi i\ell/N}\), \(1\le\ell\le N-1\). On the mode \(z_\ell^y\), the generator has eigenvalue \(z_\ell-1+g((-1)^\ell-1)\), whose real part is strictly negative. The Poisson equation hence has a solution unique up to an additive constant. Its nonconstant Fourier coefficients are exactly \(1/[z_\ell-1+g((-1)^\ell-1)]\). Since \(h(0)=0\), its spatial average is the negative of their sum, namely

\[
\frac1N\sum_{y=0}^{N-1}h(y)
=\sum_{\ell=1}^{N-1}\frac{1}{1-z_\ell+2g\,\mathbf1_{\{\ell\ \mathrm{odd}\}}}.
\]

This sum is real because conjugate Fourier modes pair. For the \(k-1\) nontrivial even modes, \(z_\ell\) runs over the nonunit \(k\)-th roots of unity. The identity \(1/(1-z)+1/(1-z^{-1})=1\) shows that their reciprocal sum is \((k-1)/2\), including the \(-1\) root when present. For odd modes, \(z_\ell^k=-1\), the \(k\) roots of \(P(z)=z^k+1\). With \(r=1+2g\ge1\), the logarithmic-derivative identity gives

\[
\sum_{z^k=-1}\frac1{r-z}=\frac{P'(r)}{P(r)}=\frac{k r^{k-1}}{r^k+1}.
\]

Adding the two contributions proves the finite formula for all integer \(k\ge1\), including \(g=0\).

**3. Global optimization and limits.** Differentiating in the nonnegative real variable \(g\) yields

\[
M_k'(g)=\frac{2k r^{k-2}\bigl(k-1-r^k\bigr)}{(1+r^k)^2},\qquad r=1+2g.
\]

For \(k=1,2\), the derivative is negative for every \(g>0\), so the function is strictly decreasing on the closed half-line; for \(k=2\), its derivative vanishes only at the left endpoint \(g=0\). For every \(k\ge3\), the sign is positive exactly when \(1\le r<(k-1)^{1/k}\) and negative when \(r>(k-1)^{1/k}\). Therefore \(g_{*,k}\) is the unique strict global maximum. Substituting \(r^k=k-1\) gives the peak value. Direct substitution yields \(M_k(0)=k-\frac12\), and \(\lim_{g\to\infty}M_k(g)=(k-1)/2\) for every \(k\ge2\) (for \(k=1\) the limit is zero). Finally \(r_* =\exp(\log(k-1)/k)\) gives \(g_{*,k}\sim \log k/(2k)\), and \((k-1)^{1-1/k}/k\to1\) gives the asymptotic peak ratio \(3/2\). Every step uses a finite Fourier calculation or elementary limits; no finite simulation is used as proof.

## Verification

The accompanying standalone program `check_switching_gates.py` builds the original site–gate continuous-time Markov chain and, independently, the reduced difference chain, then solves both absorbing-state hitting-time linear systems with exact rational arithmetic. For \(1\le k\le8\) and seven nonnegative rational switching rates it checks both results against the closed formula, including time-zero absorption normalization. It also tests derivative signs and asymptotic identities. Running `python check_switching_gates.py` returned `PASS: 160 checks; two independently assembled Markov generators agree exactly.` All checks were executed against the actual standalone packaged source. These finite tests are consistency checks; the general theorem follows from the finite Fourier proof above.

## Relationship to prior work

Switching-gate first-passage problems are established. Ammari et al. (2011) treat Brownian narrow escape with alternately open small boundary windows and asymptotic mean escape times, rather than unidirectional motion and an exact finite-cycle parameter threshold. Bressloff and Lawley (2015) give diffusion models with Markov-switching absorbing boundaries and small-hole asymptotics. Scher and Reuveni (2021) give a general network-gating renewal approach, and their discrete-time extension discusses resonances caused by discrete-time updates. Those general methods are relevant background, not claimed as new here. The present evaluated statement uses **two alternating distinct targets** on a finite directed cycle with *continuous-time* motion and specifies the unique positive-rate maximum and its size dependence. The available material did not identify that evaluated claim or a direct stated corollary. A general renewal framework might furnish another derivation, and a specialized or inaccessible treatment may cover the evaluated result; the literature comparison does not establish absolute historical priority.

## Limitations

The theorem does not cover non-antipodal trap separations, bidirectional diffusion, asymmetric gate switching, partially absorbing traps, nonuniform initial states (except the conditional-on-survival normalization stated above), or network geometries beyond directed even cycles. The asymptotic ratio concerns the specified unconditional initial law. Earlier general gated-network results may subsume portions of the derivation. Publication novelty and independent mathematical verification are not certified.

## References

1. H. Ammari, J. Garnier, H. Kang, H. Lee, and K. Sølna, “The Mean Escape Time for a Narrow Escape Problem with Multiple Switching Gates,” *Multiscale Modeling & Simulation* 9 (2011), 817–833. DOI: 10.1137/100817103.
2. P. C. Bressloff and S. D. Lawley, “Escape from Subcellular Domains with Randomly Switching Boundaries,” *Multiscale Modeling & Simulation* 13 (2015), 1420–1445. DOI: 10.1137/15M1019258.
3. Y. Scher and S. Reuveni, “Unified Approach to Gated Reactions on Networks,” *Physical Review Letters* 127 (2021), 018301. DOI: 10.1103/PhysRevLett.127.018301. Preprint: arXiv:2101.05124.
4. Y. Scher and S. Reuveni, “Gated reactions in discrete time and space,” *Journal of Chemical Physics* 155 (2021), 234112. DOI: 10.1063/5.0072393; arXiv:2109.05593.
5. W.-S. Sheu, D.-Y. Yang, and S.-Y. Sheu, “Survival of a walker in gated trapping systems,” *Journal of Chemical Physics* 106 (1997), 9050–9056. DOI: 10.1063/1.474037.
