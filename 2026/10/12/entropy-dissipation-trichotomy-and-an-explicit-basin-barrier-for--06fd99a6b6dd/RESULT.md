# Entropy-dissipation trichotomy and an explicit basin barrier for the incremental voter model

## Finding

**Theorem (all finite numbers of opinion states).** For every integer \(k\geq1\), the mean-field incremental voter model of Cao and Gong on \(2k+1\) opinion states possesses a strict entropy-like Lyapunov function. Every trajectory from an arbitrary probability vector converges exponentially to exactly one of the three equilibria: left-end consensus, the uniform distribution, or right-end consensus. Uniform opinion is a hyperbolic equilibrium with exactly one unstable direction, whereas both consensus equilibria are hyperbolic sinks. An explicit entropy-versus-polarization inequality certifies subsets of the two consensus basins, including profiles outside the previously proved extreme-mean basins.

Set \(L=2k\), \(q=(q_0,\ldots,q_L)\), \(M(q)=\sum_{j=0}^L j q_j\), \(r(q)=M(q)/L\), \(s(q)=1-r(q)\), and use \(0\log0=0\). Define
\[
 \mathcal F(q)=\sum_{j=0}^{L}q_j\log q_j-M(q)\log M(q)
 -(L-M(q))\log(L-M(q))+L\log L.
\]
For every nonconsensus trajectory and every \(t>0\), the exact identity is
\[
 \frac{d}{dt}\mathcal F(q(t))=-\sum_{j=0}^{L-1}
 (r q_j-sq_{j+1})\log\!\frac{r q_j}{s q_{j+1}}\leq0,
\]
with equality at a positive state only at the uniform equilibrium. Put
\[
 \mathcal F_*=L\log2-\log(L+1)>0.
\]
If \(\mathcal F(q(0))<\mathcal F_*\) and \(M(q(0))<L/2\), then \(q(t)\to(1,0,\ldots,0)\). If \(\mathcal F(q(0))<\mathcal F_*\) and \(M(q(0))>L/2\), then \(q(t)\to(0,\ldots,0,1)\). These claims include initial boundary distributions; no positivity is assumed at time zero. The test is sufficient, not an exact formula for the complete basin boundary.

## Assumptions and scope

The probability simplex is \(\Delta_L=\{q_j\geq0,\ \sum_{j=0}^Lq_j=1\}\). Time is the normalization of the published mean-field ODE (equations (2.1) and (3.2) of Cao–Gong). Define the edge fluxes
\[
 J_j(q)=r(q)q_j-s(q)q_{j+1}\quad(0\leq j<L),
 \qquad J_{-1}=J_L=0,
\]
and evolve \(\dot q_j=J_{j-1}-J_j\) for every \(0\leq j\leq L\). Every conclusion holds for every integer \(k\geq1\), every initial vector in \(\Delta_L\), and all positive times. In the original centered labels the indices \(j=0,L\) correspond to opinions \(-k,+k\).

## Proof

**1. Positivity and well-posedness.** The vector field is polynomial and preserves total mass. At a face \(q_j=0\), the inflow from its neighbors is nonnegative, so the simplex is forward invariant, compact, and globally well posed. If the initial state is not one of the endpoint point masses, then \(0<M(0)<L\). On any finite time interval the mean remains strictly between its endpoints (otherwise finite-time uniqueness would put the trajectory on an endpoint equilibrium). Thus \(r,s>0\). Connectedness of the nearest-neighbor path and positivity of all allowed jump rates imply \(q_j(t)>0\) for every \(j\) and \(t>0\), even when some initial coordinates vanish; this follows by iterated variation of constants from any initially occupied coordinate.

**2. Exact dissipation.** For a simplex-tangent perturbation \(h\), write \(\delta M=\sum jh_j\). Differentiation in the relative interior yields
\[
 D\mathcal F(q)[h]=\sum_{j=0}^Lh_j\log q_j
 +\log\!\frac{L-M}{M}\sum_{j=0}^L jh_j.
\]
Consequently, the difference between the contributions of coordinates \(j+1\) and \(j\) is \(\log(sq_{j+1}/(rq_j))\). Summation by parts using \(\dot q_j=J_{j-1}-J_j\) gives the announced dissipation law. Since \((a-b)\log(a/b)\geq0\) for \(a,b>0\), it is strict unless all \(J_j\) vanish.

**3. Exact equilibrium census.** If \(M=0\) or \(M=L\), the probability vector is the corresponding endpoint mass. At every other equilibrium the chain is irreducible, hence all coordinates are positive and every flux vanishes. Let \(z=r/s>0\). Detailed balance forces \(q_j=q_0z^j\); self-consistency of \(M=Lz/(1+z)\) leads, after clearing denominators, to
\[
 f_L(z)=(L-1)z^{L+1}-(L+1)z^L+(L+1)z-(L-1)=0.
\]
For \(L\geq2\),
\[
 f_L'(z)=(L+1)\bigl[(L-1)z^L-Lz^{L-1}+1\bigr].
\]
The expression in brackets decreases to zero on \((0,1]\) and increases from zero on \([1,\infty)\), because its derivative is \(L(L-1)z^{L-2}(z-1)\). Hence \(f_L\) is strictly increasing and vanishes only at \(z=1\). This gives the sole interior equilibrium \(u=(1/(L+1),\ldots,1/(L+1))\), in addition to the endpoint masses \(e_0,e_L\). The equilibrium census agrees with Proposition 3.2 of Cao–Gong and is recalled to make the convergence proof self-contained.

**4. Global convergence.** The continuous function \(\mathcal F\) is bounded below on the compact simplex and is nonincreasing along each nonconsensus solution; therefore it has a limit. An omega-limit set is nonempty, compact, connected, and invariant. If it contained a non-equilibrium point \(p\), then the trajectory started at \(p\) would enter the relative interior and strictly decrease \(\mathcal F\) over some positive time interval, contradicting constancy of \(\mathcal F\) on the omega-limit set. Therefore the omega-limit set is contained in \(\{e_0,u,e_L\}\). Connectedness forces a singleton. No classification of the complete separating stable manifold is needed.

**5. Hyperbolic equilibria and rates.** At \(u\), the Hessian of \(\mathcal F\) on the \(L\)-dimensional tangent space \(\sum h_j=0\) is
\[
 D^2\mathcal F(u)[h,h]=(L+1)\sum_{j=0}^Lh_j^2
 -\frac4L\left(\sum_{j=0}^Lj h_j\right)^2.
\]
The squared norm of \((j-L/2)_{j=0}^L\) is \(L(L+1)(L+2)/12\), so this quadratic form has one strictly negative direction and \(L-1\) strictly positive directions: the magnitude of the rank-one negative correction relative to the identity is \((L+2)/3>1\). Introduce the positive logarithmic mean \(\Lambda(a,b)=(a-b)/(\log a-\log b)\) with continuous diagonal value. The evolution is \(\dot q=-K(q)\nabla_{\Delta}\mathcal F(q)\), where \(K\) is the path-graph Laplacian with edge weights \(\Lambda(rq_j,sq_{j+1})\). At \(u\), every weight is \(1/[2(L+1)]\), hence \(K(u)\) is positive definite on the tangent space. The linearization \(-K(u)D^2\mathcal F(u)\) is similar to a symmetric matrix with one positive and \(L-1\) negative eigenvalues. At \(e_0\), coordinates \((q_1,\ldots,q_L)\) yield an upper triangular Jacobian with eigenvalues \(-1+1/L\) and \(-1\) repeated \(L-1\) times. Reflection gives the same at \(e_L\). Thus all three equilibria are hyperbolic, with the stated stability indices. Every convergent orbit eventually lies in the local stable manifold of its limiting hyperbolic equilibrium, so standard hyperbolic stable-manifold estimates yield \(\|q(t)-q_\infty\|\leq C(q(0))e^{-c(q(0))t}\) for sufficiently large \(t\). Neither \(C\) nor \(c\) is claimed uniform over all initial conditions.

**6. An explicit basin barrier.** At the central mean \(M=L/2\),
\[
 \mathcal F(q)-\mathcal F_*
 =\sum_{j=0}^Lq_j\log\bigl((L+1)q_j\bigr)
 =D_{\rm KL}(q\|u)\geq0.
\]
Hence a trajectory starting at energy strictly below \(\mathcal F_*\) can never cross the hyperplane \(M=L/2\). Its energy also prevents convergence to \(u\), because \(\mathcal F(u)=\mathcal F_*\). The global convergence trichotomy leaves exactly one endpoint consensus on each of the two connected sides of the hyperplane. More generally the exact identity
\[
 \mathcal F(q)-\mathcal F_*
 =D_{\rm KL}(q\|u)-L D_{\rm KL}\!\left({\rm Bern}\!\left(\frac{M}{L}\right)\middle\|{\rm Bern}\!\left(\frac12\right)\right)
\]
expresses the test as a competition between profile nonuniformity and mean polarization.

For a specific illustration beyond the source's proven region, take \(k=2\) and \(q(0)=(625,375,225,135,81)/1441\). Then \(M(0)=1554/1441>1\), while direct substitution gives \(\mathcal F(q(0))\approx0.945236<4\log2-\log5\approx1.163151\). The theorem certifies convergence to left consensus even though the source's sufficient condition \(M(0)<1\) is not satisfied.

## Verification

The standalone `verify.py` script requires Python 3 and its standard library only. Run `python verify.py` in a directory containing the extracted file. It checks exact rational flux/Jacobian identities for several \(k\), the strict entropy inequality for deterministic samples, the barrier identity, and the rational initial-data example. Expected output: `VERIFY_OK`. The unrestricted theorem follows from the preceding algebra and dynamical-systems argument, not from a finite numerical experiment.

## Relationship to prior work

Cao and Gong, arXiv:2605.28984v1, derive this exact mean-field ODE, prove that these are the only three equilibria, establish the three-state global phase portrait, and identify consensus basins when \(M(0)<1\) or \(M(0)>L-1\). Their Section 4 explicitly leaves generic finite-state convergence rates and broader basin identification open. The contribution here is the exact global entropy dissipation, all-initial-data convergence for every finite \(k\), hyperbolic exponential trichotomy, and a new explicit basin certificate; it does not purport to solve the complete basin-separatrix problem.

Cao and Reed, arXiv:2408.00148v1, study an iterative persuasion–polarization process driven by pairwise relative opinion ordering and a persuasion parameter, not the present mean-weighted nearest-neighbor transition rates. Dawson, Sid-Ali, and Zhao, arXiv:2110.02116v1, develop relative-entropy local stability techniques for Gibbs-interaction McKean–Vlasov models; Thai, arXiv:1510.03238v1, develops contractive mean-field birth–death systems with a unique invariant distribution. These are relevant methodological precedents, but neither result directly covers a process with two absorbing extreme equilibria and an interior saddle or supplies this entropy-barrier selection criterion. General gradient-system ideas overlap methodologically; their application here requires the displayed exact potential and its boundary analysis.

## Limitations

This concerns deterministic infinite-population mean-field trajectories, not the finite-agent chain's absorption times, finite-size metastability, noncomplete networks, heterogeneous persuasion rules, or perturbations adding spontaneous opinion changes. The energy condition is only a sufficient basin test; it does not give an exact formula for the saddle's full stable manifold. The proof gives an eventual trajectory-dependent exponential rate, not a dimension-uniform constant nor a complete sharp rate formula. General abstract entropy-gradient theories might provide alternative proofs of some dynamical consequences; no independent mathematical audit has been performed.

## References

1. F. Cao and X. Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984v1 (first public arXiv version, 2026-05-27), https://arxiv.org/pdf/2605.28984.
2. F. Cao and S. Reed, *The iterative persuasion-polarization opinion dynamics and its mean-field analysis*, arXiv:2408.00148v1, https://arxiv.org/pdf/2408.00148.
3. D. A. Dawson, A. Sid-Ali, and Y. Q. Zhao, *Local stability of McKean-Vlasov equations arising from heterogeneous Gibbs systems using limit of relative entropies*, arXiv:2110.02116v1, https://arxiv.org/pdf/2110.02116.
4. M.-N. Thai, *Birth and death process in mean field type interaction*, arXiv:1510.03238v1, https://arxiv.org/pdf/1510.03238.
