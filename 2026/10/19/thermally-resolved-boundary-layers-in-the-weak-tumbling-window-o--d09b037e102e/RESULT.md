# Thermally resolved boundary layers in the weak-tumbling window of a reflecting lattice run-and-tumble particle

## Finding

A confined, thermally hopping run-and-tumble particle has a nondegenerate two-scale stationary crossover when the flip rate is inversely proportional to the lattice half-length. Fix two distinct positive hopping rates \(u>v>0\), and write \(\delta=u-v\). On lattice sites \(\{-L,\ldots,L\}\), let \(I_L\) denote the stationary position and let the orientation be \(\Sigma_L\in\{+,-\}\). Suppose the orientation switches at rate \(\alpha_L>0\), with \(L\alpha_L\to c\in[0,\infty)\).

**Two-scale crossover theorem.** The macroscopic position converges weakly to the probability measure
\[
\frac{I_L}{L}\ \Longrightarrow\
\frac{c}{\delta+2c}\,\mathbf1_{(-1,1)}(x)\,dx
+\frac{\delta}{2(\delta+2c)}\bigl(\delta_{-1}+\delta_{+1}\bigr).
\]
The bulk mass is \(2c/(\delta+2c)\) and the total atom weight at the two walls is \(\delta/(\delta+2c)\). Unlike a literal boundary atom at finite lattice spacing, the wall mass resolves into a *geometric thermal boundary layer*. More precisely, for each fixed integer \(j\ge0\),
\[
\lim_{L\to\infty}\Pr\{I_L=L-j,\Sigma_L=+\}
=\lim_{L\to\infty}\Pr\{I_L=L-j\}
=\frac{\delta^2}{2u(\delta+2c)}\left(\frac vu\right)^j,
\]
whereas \(\Pr\{I_L=L-j,\Sigma_L=-\}\to0\); the left edge follows by reflection and orientation reversal. For any sequence of sites with \(i_L/L\to x\in(-1,1)\),
\[
L\Pr\{I_L=i_L\}\longrightarrow\frac{c}{\delta+2c}.
\]
The two scales account for all stationary probability; the geometric edge ratio \(v/u\) does not depend on the crossover parameter \(c\). At \(c=0\), all weak-limit mass lies at the two endpoints, while each endpoint remains microscopically spread over infinitely many geometrically weighted lattice sites.

There is an exact critical logarithmic response for the *macroscopic boundary fraction* \(W(c)=\delta/(\delta+2c)\):
\[
-\frac{dW}{d\log c}=\frac{2\delta c}{(\delta+2c)^2}\le\frac14,
\]
with equality at the unique positive value \(c=\delta/2\). Hence the maximally responsive regime occurs at \(\alpha_L\sim(u-v)/(2L)\). This exact peak is **for the macroscopic boundary fraction**, not a claim about the maximum of the nonequilibrium heat capacity or the finite-size single-site response.

## Assumptions and scope

For integer \(L\ge1\), the continuous-time Markov chain \((I,\Sigma)\) has \(2(2L+1)\) states. At every permitted nearest-neighbor bond, a particle oriented \(+\) jumps to the right at rate \(u\) and to the left at rate \(v\); orientation \(-\) interchanges these two rates. Jumps that would leave the interval are suppressed. Orientation independently reverses at rate \(\alpha>0\). The chain is irreducible and has a unique invariant distribution. Put
\[p_i=\Pr\{I=i,\Sigma=+\},\quad m_i=\Pr\{I=i,\Sigma=-\},\quad \rho_i=p_i+m_i,\quad s_i=p_i-m_i.\]
Rates \(u,v\) are held fixed as \(L\) grows. The thermal hopping realization \(u=\nu\exp(\beta fa/2)\), \(v=\nu\exp(-\beta fa/2)\) with \(f>0\), \(\nu>0\), is a special case. The theorem excludes the unbiased case \(u=v\), for which the position marginal is exactly uniform for each \(L\) and each positive \(\alpha\). All weak-limit assertions refer to the *stationary distributions* of successive finite chains; they are not time-dependent mixing statements.

## Proof

**1. Exact finite-volume solution.** Reflection and uniqueness imply \(p_i=m_{-i}\), so \(\rho_i\) is even and \(s_i\) is odd. The total stationary current through each interior bond vanishes. With \(w=u+v\) and \(\delta=u-v\), it gives
\[
w(\rho_{i+1}-\rho_i)=\delta(s_i+s_{i+1}).\tag{1}\]
The orientation balance, obtained by subtracting the two stationary master equations and eliminating \(\rho\) using (1), gives
\[
uv(s_{i+1}+s_{i-1})=(u^2+v^2+\alpha w)s_i.\tag{2}
\]
The constant-coefficient recurrence and oddness imply \(s_i=A\sinh(ki)\) with \(k>0\) uniquely specified by
\[
2uv\cosh k=u^2+v^2+\alpha w.\tag{3}\]
Writing \(z=e^k>1\) and
\[
H=\frac{\delta}{w}\frac{z+1}{z-1}>0,\tag{4}\]
summing (1) gives \(\rho_i=B+AH\cosh(ki)\). At the right end, stationary balance for the \(+\) orientation is \(j^+_{L-1}=\alpha s_L\), where \(j^+_{i}=up_i-vp_{i+1}\). Substitution into this condition and use of (3) yield
\[
B=\frac{A\alpha}{\delta(z-1)}\bigl(z^{L+1}+z^{-L}\bigr).\tag{5}\]
The left boundary then holds by reflection. Normalization follows from
\[
\sum_{i=-L}^{L}\cosh(ki)=\frac{z^{L+1}-z^{-L}}{z-1}.\tag{6}\]
Thus, with \(U=z^{L+1}+z^{-L}\), \(T=z^{L+1}-z^{-L}\), and
\[
Q=\frac{HT+(2L+1)\alpha U/\delta}{z-1},\tag{7}\]
the unique normalized stationary marginal is
\[
\boxed{\rho_i=\frac{H\cosh(ki)+\alpha U/[\delta(z-1)]}{Q},\qquad -L\le i\le L.}\tag{8}
\]
This formula is positive and normalized, and the stationary solution matches the unique irreducible-chain equilibrium. It also proves a finite-size structural fact: \(\rho_i\) is strictly increasing in \(|i|\) and is strictly discretely convex in the interior, **for every** \(\alpha>0\) whenever \(u>v\). Hence there is no finite-rate sign change of the modal curvature in this parameter range; the observed flattening is a continuous crossover.

**2. Uniform control of both scales.** If \(L\alpha_L\to c\ge0\), equation (3) implies \(z_L\to u/v>1\) and (4) implies \(H_L\to1\). Divide the numerator and denominator of (8) by \(z_L^{L+1}/(z_L-1)\) to obtain the stable identity
\[
\rho_i=\frac{(z_L-1)H_L\{z_L^{i-L-1}+z_L^{-i-L-1}\}/2+(\alpha_L/\delta)(1+t_L)}{H_L(1-t_L)+(2L+1)(\alpha_L/\delta)(1+t_L)},\tag{9}
\]
where \(t_L=z_L^{-(2L+1)}\). The denominator tends to \(1+2c/\delta>0\). For each fixed \(j\ge0\), setting \(i=L-j\) in (9) yields
\[
\rho_{L-j}\to\frac{(u/v-1)(v/u)^{j+1}}{2(1+2c/\delta)}
=\frac{\delta^2}{2u(\delta+2c)}(v/u)^j.\tag{10}
\]
For interior \(i_L/L\to x\in(-1,1)\), the geometric terms in (9) decay exponentially; the remaining term gives \(L\rho_{i_L}\to c/(\delta+2c)\). Moreover (9), with \(z_L\) bounded below uniformly by a number bigger than one and denominator bounded away from zero, gives the global majorant
\[
0\le\rho_i\le\frac{K}{L}+Kq^{L-i}+Kq^{L+i},\qquad q\in(0,1),\tag{11}
\]
for all sufficiently large \(L\), with \(K,q\) independent of \(L,i\). This bound makes the two boundary layers tight in their inward integer coordinate, while the interior contributes a Riemann integral. Summing the right-edge fixed-\(j\) limits gives
\[
\sum_{j\ge0}\frac{\delta^2}{2u(\delta+2c)}(v/u)^j=\frac{\delta}{2(\delta+2c)},\tag{12}
\]
and the left edge has the same mass. The bulk density has integral \(2c/(\delta+2c)\), so the three contributions sum to one and yield the claimed weak convergence without unaccounted mass. For orientation, equation (7) gives \(A=1/Q\); using \(s_{L-j}=A\sinh(k(L-j))\) yields exactly the limit in (10). Hence \(m_{L-j}=(\rho_{L-j}-s_{L-j})/2\to0\) and \(p_{L-j}\to\rho_{L-j}\).

**3. Exact crossover response.** From the limiting wall mass \(W(c)=\delta/(\delta+2c)\) for \(c>0\), direct differentiation gives
\[-cW'(c)=\frac{2\delta c}{(\delta+2c)^2}.\]
Writing \(y=2c/\delta>0\), this is \(y/(1+y)^2\), with a unique maximum \(1/4\) at \(y=1\). The value \(c=0\) follows by continuity, and no assertion about derivatives at \(c=0\) is required.

## Verification

The accompanying standalone `verify.py` computes (9) without overflowing large exponential powers, constructs and directly solves the unrelated full \(2(2L+1)\)-state Markov-generator stationary equations, and compares the resulting marginals. For fifteen distinct size/rate triples with \(L\in\{1,2,4,6,12\}\), the maximum absolute discrepancy was \(2.11\times10^{-15}\). The script also checks exact normalization, reflection, strict discrete convexity, and approach to the independently predicted wall and bulk constants at \(L\in\{20,80,300,1000\}\). In particular, at \(u=2.5\), \(v=1\), \(c=1.7\), the predicted edge-site probability is \(0.091836735\) and the computed value at \(L=1000\) is \(0.092152390\); the predicted central rescaled density is \(0.346938776\) and the observed value is \(0.346932803\). The finite checks corroborate, but do not substitute for, the infinite-volume proof.

## Relationship to prior work

Santra's 2026 single-particle lattice model (arXiv:2608.17903v1, Section III.1, equations (5)--(17), Appendix B) gives a transfer-matrix characterization and numerical stationary density. It observes wall accumulation and proposes the inverse-length crossover \(\alpha^*\simeq(u-v)/(2L)\). That scale and the underlying finite model are **prior results**, not novel assertions here. Equation (8) is an explicit simplification of information already encoded in that transfer matrix. The contribution being assessed is the **joint asymptotic theorem** connecting (i) a continuum wall-atom/interior mixture, (ii) the temperature-dependent geometric and outward-oriented lattice microstructure of the same atoms, and (iii) the precise normalized logarithmic-response curve. The derivation establishes these limits from the finite lattice invariant measure with uniform control of probability lost between scales.

Malakar and collaborators (arXiv:1711.08474, Section 3.2) derive an exact stationary distribution for a continuum diffusion-plus-telegraph model in a reflecting interval. Bressloff (arXiv:2302.01158, Section 2) gives continuum run-and-tumble equations with sticky-wall probabilities and a uniform stationary interior. Those works supply genuine prior coverage of related continuum shapes and wall atom mechanisms. Neither treats this discrete thermal hopping model's fixed-lattice-spacing geometric edge law at \(L\alpha_L\to c\). General continuum boundary mechanisms alone therefore do not imply the lattice ratio \(v/u\) or its exact microscopic normalization. The present limit should not be conflated with a newly discovered general boundary-atom mechanism.

## Limitations

The theorem assumes spatially constant distinct rates \(u>v>0\), symmetric orientation flips, perfectly reflecting endpoints, and the specified inverse-length weak-flip regime; it does not treat interacting particles, nonconstant potentials, an unbiased force, time-dependent relaxation, or any nonequilibrium heat-capacity asymptotic. The exact maximum \(1/4\) concerns the limiting *macroscopic boundary mass*, not the finite-size single-site slope plotted by Santra. The macroscopic wall-atom fraction is also consistent with established continuum sticky-boundary theory; independent novelty rests on the matched microscopic lattice layer and complete two-scale statement. Existing transfer-matrix formulas may implicitly encode these consequences; no independent priority or expert audit has been performed.

## References

1. I. Santra, *Heat capacity as a marker for shape and jamming transitions in active systems*, arXiv:2608.17903v1 (first publicly posted 2026-08-18), particularly Section III.1 and Appendix B. https://arxiv.org/abs/2608.17903
2. K. Malakar, V. Jemseena, A. Kundu, K. Vijay Kumar, S. Sabhapandit, S. N. Majumdar, S. Redner, and A. Dhar, *Steady state, relaxation and first-passage properties of a run-and-tumble particle in one-dimension*, arXiv:1711.08474 (2017), particularly Section 3.2. https://arxiv.org/abs/1711.08474
3. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158 (2023), particularly Section 2. https://arxiv.org/abs/2302.01158
4. A. B. Slowman, M. R. Evans, and R. A. Blythe, *Exact solution of two interacting run-and-tumble random walkers with finite tumble duration*, arXiv:1705.04812 (2017), for structurally distinct lattice-jamming stationary layers. https://arxiv.org/abs/1705.04812
