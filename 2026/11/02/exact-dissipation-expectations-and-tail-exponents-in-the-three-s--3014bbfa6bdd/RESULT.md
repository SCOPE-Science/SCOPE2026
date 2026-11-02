# Exact dissipation expectations and tail exponents in the three-state stationary-flow hyperensemble

## Finding

Let \(m\) range over normalized, nonnegative, stationary two-step flow matrices on three labeled states, with zero diagonal. Let \(\mathcal U_{\mathrm{sta}}\) be the uniform three-dimensional volume distribution on this polytope, and let \(\mathcal U_{\mathrm{bal}}\) be uniform one-dimensional length on the section whose three stationary one-time probabilities are exactly \(1/3\). For the stationary entropy production per transition
\[
\Sigma(m)=\sum_{i\ne j}m_{ij}\log\frac{m_{ij}}{m_{ji}},
\]
we prove
\[
\boxed{\mathbb E_{\mathrm{sta}}\Sigma=2\log(3/2)-\frac12,\qquad
\mathbb E_{\mathrm{bal}}\Sigma=1.}
\]
The values use natural logarithms. More strongly, for every real \(t\ge0\),
\[
\boxed{\mathbb E_{\mathrm{sta}}e^{t\Sigma}<\infty\ \Longleftrightarrow\ t<3,
\qquad \mathbb E_{\mathrm{bal}}e^{t\Sigma}<\infty\ \Longleftrightarrow\ t<1.}
\]
Their upper tails consequently differ at the sharp exponential scale:
\[
\boxed{\lim_{s\to\infty}\frac{\log\Pr_{\mathrm{sta}}(\Sigma>s)}s=-3,
\qquad \Pr_{\mathrm{bal}}(\Sigma>s)\sim2e^{-s}.}
\]
In particular, knowing exactly the balanced one-time stationary distribution changes the mean and the exponential tail scale of the same entropy-production observable. These are probabilities over randomly chosen stationary transition laws, not fluctuations along a single fixed chain.

## Assumptions and scope

The state space is \(\{1,2,3\}\). A flow matrix \(m\) has \(m_{ii}=0\), nonnegative off-diagonal entries, \(\sum_{ij}m_{ij}=1\), and \(\sum_j m_{ij}=\sum_jm_{ji}\) for every state. All allowed off-diagonal entries are strictly positive almost surely under the two uniform measures; boundary points do not affect the conclusions. Setting \(\rho_i=\sum_jm_{ij}\) and \(T_{ij}=m_{ij}/\rho_i\) produces a stationary discrete-time Markov chain. No self-transitions, continuum-time rate normalization, external temperature or Boltzmann factor is assumed. Uniformity means Euclidean volume in the affine hull, respectively Euclidean arclength in the balanced section, not entrywise-uniform transition probabilities.

For oriented cycle \(1\to2\to3\to1\), write \(J=m_{12}-m_{21}=m_{23}-m_{32}=m_{31}-m_{13}\) and edge-pair activities \(a=m_{12}+m_{21}\), \(b=m_{23}+m_{32}\), \(c=m_{31}+m_{13}\). Stationarity gives
\[
a+b+c=1,\qquad a,b,c\ge|J|,\qquad |J|\le1/3.
\]
The full uniform family has three affine dimensions. The balanced section \(\rho=(1/3,1/3,1/3)\) fixes \(a=b=c=1/3\) and leaves one free cycle current.

## Proof

**1. Reduction to independent beta and simplex variables.** The affine map from \((a,b,J)\) (with \(c=1-a-b\)) to \(m\) has constant nonzero Euclidean Jacobian. Thus \(\mathcal U_{\mathrm{sta}}\) is constant-density on \(a,b,c\ge|J|\) and \(a+b+c=1\). Put
\[
w=3|J|\in[0,1],\qquad a_i=\frac w3+(1-w)u_i\quad(i=1,2,3),\qquad \sum_i u_i=1.
\]
For fixed \(w\), the activity triangle has area proportional to \((1-w)^2\); its normalized coordinates \(u\) are uniform on the probability simplex. Consequently, independently,
\[
f_w(w)=3(1-w)^2\quad(0<w<1),\qquad u\sim\operatorname{Dirichlet}(1,1,1).
\]
Each single \(u_i\) has density \(2(1-u_i)\). Under \(\mathcal U_{\mathrm{bal}}\), the corresponding \(w=3|J|\) is instead uniform on \([0,1]\).

**2. The entropy-production functional.** Opposite directed edges contribute their difference times the logarithm of their ratio, so
\[
\Sigma=|J|\sum_{i=1}^3\log\frac{a_i+|J|}{a_i-|J|}
=\frac w3\sum_{i=1}^3\log\left(1+\frac{2w}{3(1-w)u_i}\right).
\]
For the balanced section this reduces to \(\Sigma_{\mathrm{bal}}(w)=w\log((1+w)/(1-w))\), a strictly increasing function of \(w\). For fixed nonzero current, the function \(a\mapsto\log((a+|J|)/(a-|J|))\) is strictly convex for \(a>|J|\); hence Jensen's inequality shows that the balanced activities minimize dissipation **at a prescribed current**. This conditional minimization is compatible with the opposite unconditional mean comparison below because the two ensembles have different current distributions.

**3. Exact means.** In the balanced family, expanding \(\log((1+w)/(1-w))\) as an increasing nonnegative power series gives
\[
\mathbb E_{\mathrm{bal}}\Sigma
=\int_0^1w\log\frac{1+w}{1-w}\,dw
=2\sum_{k=0}^\infty\frac1{(2k+1)(2k+3)}=1.
\]
For the full family, let \(F(c)=\int_0^1(1-u)\log(1+c/u)\,du\) for \(c>0\). Direct differentiation gives \(F'(c)=(1+c)\log(1+1/c)-1\), and \(F(0)=0\) gives
\[
F(c)=\frac12\left[(1+c)^2\log(1+c)-c(c+2)\log c-c\right].
\]
The simplex marginal and the current density therefore imply
\[
\mathbb E_{\mathrm{sta}}\Sigma
=6\int_0^1 w(1-w)^2 F\!\left(\frac{2w}{3(1-w)}\right)dw.
\]
After substitution, the integrand expands into these four elementary terms (each integrated over \(0\le w\le1\)):
\[
\begin{aligned}
&\frac{w(3-w)^2}{3}\log(3-w),\\
&-\frac{4w^2(3-2w)}3\log(2w),\\
&-3w(1-w)^2\log(3(1-w)),\\
&-2w^2(1-w).
\end{aligned}
\]
Their integrals, in order, are
\[
-\frac43\log2-\frac{109}{144}+\frac94\log3,\quad
\frac5{18}-\frac23\log2,\quad
\frac7{48}-\frac14\log3,\quad-\frac16.
\]
Summing yields \(2\log(3/2)-1/2\) exactly. All endpoint logarithmic terms are integrable.

**4. Sharp exponential moments.** Write \(\delta=1-w\). For \(0<w<1\) and positive simplex coordinates, the inequality
\[
1+\frac{2w}{3\delta u_i}\le\frac1{\delta u_i}
\]
follows from \(\delta u_i+2w/3\le1\). Thus
\[
e^{t\Sigma}\le\delta^{-tw}\prod_{i=1}^3u_i^{-tw/3}
\le\delta^{-t}\prod_{i=1}^3u_i^{-t/3},\qquad t\ge0.
\]
The last bound is integrable under the independent \(3\delta^2d w\) and uniform-simplex laws whenever \(t<3\): the beta integral at \(\delta=0\) needs \(2-t>-1\), and all three simplex singularities require \(t/3<1\).

For necessity, take any fixed compact positive-area triangle patch with all \(u_i\) bounded away from zero. Uniformly there as \(\delta\downarrow0\), the exact expression gives \(\Sigma=-\log\delta+O(1)\). Hence \(e^{t\Sigma}\) is comparable to \(\delta^{-t}\) and \(\int_0^\varepsilon\delta^{2-t}d\delta\) diverges for \(t\ge3\). On the balanced line, \(\Sigma_{\mathrm{bal}}(w)=\log(2/\delta)+o(1)\) and \(w\) is uniform, proving the threshold \(t=1\).

**5. Upper tails.** Balanced monotonicity and \(\Sigma_{\mathrm{bal}}(1-\delta)=\log(2/\delta)+o(1)\) give \(\Pr_{\mathrm{bal}}(\Sigma>s)\sim2e^{-s}\). In the full family, finiteness of the exponential moment at every \(t<3\) gives \(\limsup_{s\to\infty}s^{-1}\log\Pr(\Sigma>s)\le-3\). For the lower bound restrict \(u\) to the same positive-area interior patch. Uniformly on it, \(\Sigma/(-\log\delta)\to1\); for any \(\varepsilon\in(0,1)\), all sufficiently small \(\delta\) satisfy \(\Sigma\ge(1-\varepsilon)(-\log\delta)\). Since \(\Pr(\delta<h)=h^3\), this yields the lower logarithmic exponent at least \(-3/(1-\varepsilon)\). Letting \(\varepsilon\downarrow0\) establishes the claimed exact exponent \(-3\).

## Verification

The supplied `verify.py` reconstructs the flow matrix from independent simplex and current coordinates and checks normalization, stationarity, entropy-production equality and the convexity lower bound at 1,000 deterministic samples. It also symbolically integrates all four elementary mean contributions and independently checks the balanced integral. The actual saved script passed 5,007 assertions. Numerical samples and software do not prove universal statements; the analytical calculations above do.

To replay, install SymPy 1.12 or newer and run `python verify.py` in a directory containing this document and the supplied script.

## Relationship to prior work

Hartle, Kumar and Wolpert [1], Section IV.2 and equations (43)–(56), introduce these uniform stationary-flow hyperensembles, the three-state flow parametrization, the exact two current densities, and the general entropy-production functional. Those objects, current distributions, and the fact that almost every random flow is irreversible are prior work. They derive \(\mathbb E|J|\), not the hyperensemble expectation, exponential-moment threshold or large-dissipation tail of \(\Sigma\). The present result integrates the nonlinear current–affinity observable over the **joint** current/activity law; current marginals alone cannot supply that information in the full polytope.

General Markov-kernel information geometry [2], including its characterization of entropy production as a time-reversal divergence, addresses individual Markov transition kernels and their geometric families, rather than these two exact hyperensemble push-forward laws. Searches for equivalent formulations and broader coverage have not identified an explicit earlier theorem yielding all stated dissipation predictions. This comparison is not an independent novelty certification.

## Limitations

The theorem applies only to the three-state zero-self-loop model and the two specified Euclidean-uniform hyperensembles. It does not describe time-integrated entropy-production fluctuations for a fixed chain, higher-state polytopes, nonuniform priors, continuous-time jump rates, or physical entropy in units including a Boltzmann constant. The full-ensemble upper tail is determined here only at its logarithmic exponential rate; no constant prefactor is asserted. Priority beyond inspected sources remains subject to further literature assessment, and no independent audit has been performed.

## References

[1] H. Hartle, A. Kumar and D. H. Wolpert, *Distributional statistics of nonequilibrium*, arXiv:2610.33383v1 (first public version, 2026-10-24), Sections IV.2.1–IV.2.2 and equations (43)–(56). https://arxiv.org/html/2610.33383v1

[2] G. Wolfer and S. Watanabe, *Information geometry of Markov Kernels: a survey*, Frontiers in Physics **11**, 1195562 (2023), especially Sections 2.3 and 4.2.4. https://doi.org/10.3389/fphy.2023.1195562
