# Sharp angular dissipation cost of persistence and chirality in preferred-reorientation run-and-tumble particles

## Finding

For a planar run-and-tumble particle with Poisson reorientations at rate \(\alpha>0\), let \(P\) be its law of signed turning increments \(\psi\in\mathbb R/(2\pi\mathbb Z)\). Write
\[
 c=\int\cos\psi\,P(d\psi),\qquad s=\int\sin\psi\,P(d\psi),\qquad m=c+is.
\]
Let \(P^R\) be the pushforward of \(P\) under \(\psi\mapsto-\psi\), and define the *angular jump irreversibility rate* (in nats per unit time) as
\[
 \sigma_{\rm ang}=\alpha\,D_{\rm KL}(P\Vert P^R),
\]
with extended value \(+\infty\) when absolute continuity fails. This is the stationary entropy-production rate of the orientation-jump process, not a claim about the entire active particle's physical heat dissipation.

**Sharp dissipation theorem.** For every turning law with \(c^2+s^2<1\),
\[
 \boxed{\ \sigma_{\rm ang}\ \ge\ 2\alpha\,r\operatorname{artanh}(r),\qquad
 r=\frac{|s|}{\sqrt{1-c^2}}\in[0,1).\ }
\]
The right side is defined as zero for \(r=0\). The bound is the exact minimum over all turning probability measures with the specified first complex moment \(m\). When \(s\ne0\), its unique minimizer is the two-angle law
\[
 \boxed{\quad P_* =\frac{1+q}{2}\,\delta_{\vartheta}
                  +\frac{1-q}{2}\,\delta_{-\vartheta},\quad
 \vartheta=\arccos c,\quad q=\frac{s}{\sqrt{1-c^2}}.\quad}
\]
For \(s=0\), the minimizers are exactly the reflection-symmetric turning laws with cosine moment \(c\). The optimum is approached by smooth turning densities while preserving both first moments *exactly*.

The source model identifies the effective orientational relaxation rate \(D_\theta=\alpha(1-c)\) and signed angular drift \(\Omega=\alpha s\), with the sign convention \(\Omega=-\alpha\operatorname{Im}\Pi_1\) and \(\Pi_1=\int e^{-i\psi}P(d\psi)\). Hence the equivalent experimentally interpretable form is
\[
 \boxed{\quad\sigma_{\rm ang}\ge 2\alpha\,R\operatorname{artanh}R,\quad
 R=\frac{|\Omega|}{\sqrt{D_\theta(2\alpha-D_\theta)}}.\quad}
\]
It is valid when \(0<D_\theta<2\alpha\) and \(|\Omega|<\sqrt{D_\theta(2\alpha-D_\theta)}\). At a fixed orientational relaxation rate and fixed angular drift, the unique entropy-efficient asymmetric tumbling strategy therefore alternates between a single left-turn angle and its right-turn reflection, with unequal weights.

For \(c^2+s^2=1\) with \(s\ne0\), every compatible law has \(\sigma_{\rm ang}=+\infty\). For \(m=\pm1\), the unique law is a deterministic zero or half-turn and the angular irreversibility is zero.

## Assumptions and scope

Time is continuous. The orientation lives on the circle and, at each independent Poisson event with rate \(\alpha\), changes by an independent increment drawn from a fixed Borel probability \(P\). Its generator is
\[
 (Lf)(\theta)=\alpha\int[f(\theta+\psi)-f(\theta)]\,P(d\psi).
\]
Haar-uniform orientation is stationary for all such increment laws; uniqueness of the stationary distribution is unnecessary. Angular irreversibility means the stationary jump-path relative-entropy rate between forward and reversed orientation trajectories. It is well-defined as an extended nonnegative number for singular as well as absolutely continuous increment laws. Any additional self-propulsion, spatial diffusion or external forces are excluded from the quantity \(\sigma_{\rm ang}\); they are not asserted to have the same entropy production.

Throughout the main theorem, \(\alpha>0\) and \(c,s\in\mathbb R\) satisfy \(c^2+s^2<1\). All probability measures over the circle with these first moments are included in the minimization. The indicated uniqueness concerns the minimizing *turning law*, not a trajectory realization or a unique invariant orientation ensemble.

## Proof

**1. Stationary angular path cost.** Haar measure is invariant under the convolution jump generator. The reversed stationary jump intensity replaces the increment law \(P\) by its reflected law \(P^R(B)=P(-B)\). Consequently the mean forward/reverse log likelihood ratio accumulated per Poisson jump is \(D_{\rm KL}(P\Vert P^R)\), and the jump rate is \(\alpha\). Stationary boundary terms vanish per unit time. Therefore the angular jump-path entropy-production rate is exactly \(\sigma_{\rm ang}=\alpha D_{\rm KL}(P\Vert P^R)\), including the convention for singular support.

**2. Reflection decomposition.** Set \(\nu=(P+P^R)/2\), a symmetric probability measure, and define the odd Radon–Nikodym function \(u=d(P-P^R)/d(P+P^R)\). Then \(-1\le u\le1\), \(u(-\psi)=-u(\psi)\) almost everywhere and
\[
 P=(1+u)\nu,\qquad P^R=(1-u)\nu.
\]
When \(D_{\rm KL}(P\Vert P^R)<\infty\), \(|u|<1\) almost everywhere on the nontrivial reflected pairs. Symmetry of \(\nu\) gives
\[
 c=\int\cos\psi\,d\nu,\qquad
 s=\int\sin\psi\,u\,d\nu,
\]
and the odd part of the log likelihood integrates to zero, so
\[
 D_{\rm KL}(P\Vert P^R)
 =\int u\log\frac{1+u}{1-u}\,d\nu
 =\int g(u^2)\,d\nu,
\quad g(t)=2\sqrt t\operatorname{artanh}\sqrt t.
\]
Set \(g(1)=+\infty\). The identities also hold by extended-value approximation when the divergence is infinite.

**3. Sharp lower bound.** Cauchy–Schwarz and the variance inequality imply
\[
 s^2\le\left(\int\sin^2\psi\,d\nu\right)
       \left(\int u^2\,d\nu\right),\qquad
 \int\sin^2\psi\,d\nu
 =1-\int\cos^2\psi\,d\nu\le1-c^2.
\]
Hence \(\int u^2d\nu\ge s^2/(1-c^2)=r^2\). For \(0\le t<1\),
\[
 g(t)=2\sum_{j=1}^{\infty}\frac{t^j}{2j-1}.
\]
The power series shows that \(g\) is increasing and strictly convex, including the one-sided boundary at \(t=0\). Jensen's inequality therefore yields
\[
 D_{\rm KL}(P\Vert P^R)
  =\int g(u^2)d\nu
  \ge g\left(\int u^2d\nu\right)
  \ge g(r^2)
  =2r\operatorname{artanh}r.
\]
This proves the bound for every compatible turning law, including ones with infinite cost.

**4. Sharpness, rigidity and the zero-chirality case.** For \(s\ne0\), let \(\vartheta=\arccos c\in(0,\pi)\) and \(q=s/\sin\vartheta\). The condition \(c^2+s^2<1\) ensures \(|q|<1\). The stated two-angle measure has \(\mathbb E\cos\psi=c\), \(\mathbb E\sin\psi=s\) and
\[
 D_{\rm KL}(P_*\Vert P_*^R)=q\log\frac{1+q}{1-q}
 =2r\operatorname{artanh}r.
\]
Conversely, equality in the lower bound with \(s\ne0\) forces equality in the cosine variance inequality, hence \(\cos\psi=c\) almost surely under \(\nu\). Thus \(\nu\) is supported on \(\{\vartheta,-\vartheta\}\); reflection symmetry forces half its mass on each point, and the prescribed sine moment determines their unequal weights uniquely. If \(s=0\), the minimum is zero, and the divergence vanishes if and only if \(P=P^R\); reflection-symmetric laws with the required cosine moment exist, proving the complete zero-chirality statement.

**5. Density sharpness.** Let \(b_\varepsilon\) be a smooth even probability density supported in a shrinking neighborhood of zero, and set \(\rho_\varepsilon=\int\cos\psi\,b_\varepsilon(\psi)\,d\psi\uparrow1\). For sufficiently small \(\varepsilon\), choose
\[
 \vartheta_\varepsilon=\arccos(c/\rho_\varepsilon),\qquad
 q_\varepsilon=s/\sqrt{\rho_\varepsilon^2-c^2},
\]
with \(|q_\varepsilon|<1\), and set
\[
 p_\varepsilon(\psi)=\tfrac{1+q_\varepsilon}{2}b_\varepsilon(\psi-\vartheta_\varepsilon)
 +\tfrac{1-q_\varepsilon}{2}b_\varepsilon(\psi+\vartheta_\varepsilon).
\]
For sufficiently small supports the two bumps are disjoint, and reflection interchanges them. Their first complex moment is exactly \(c+is\), while their relative entropy to reflection equals \(2|q_\varepsilon|\operatorname{artanh}|q_\varepsilon|\). This converges to the proved lower bound. Thus restricting to smooth turning densities changes attainment but not the sharp infimum.

**6. Unit-circle boundary.** If \(|m|=1\), equality in \(|\int e^{i\psi}dP|\le1\) implies \(P\) is concentrated at one angle. Unless that angle is \(0\) or \(\pi\), reflection moves it to a disjoint point, making the relative entropy infinite. The two reflection-fixed angles instead have zero cost.

## Verification

The standalone `verify.py` uses only the Python standard library and requires no external datasets. Execute `python verify.py` from this package. It checks 240 randomly generated reflected turning laws against the bound; six exact two-angle equality examples; five sharply concentrated four-point approximations preserving both complex-moment components; 64 independently formed finite cyclic orientation jump kernels using direct stationary edge fluxes; and three weak-chirality expansions, totaling 318 passing comparisons. All are finite corroborations; the theorem for arbitrary measures follows from the displayed measure-theoretic proof.

For a sample with \(c=3/5\) and \(s=2/5\), the predicted optimizer places probabilities \(3/4\) and \(1/4\) at \(\pm\arccos(3/5)\), giving exact cost per unit jump rate \(\tfrac12\log3\). A symmetric law with the same \(c\) but \(s=0\) can have zero jump irreversibility. These exact arithmetic checks expose the role of chirality, not just persistence.

## Relationship to prior work

Britton, Zhang, Han and Bertrand (2026), *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519v1, derive the free-particle model with arbitrary turning increments, identify the mapping between the first Fourier mode and effective rotational relaxation/chirality, and study spatial/orientational correlations and higher moments. Their manuscript, including the main results and discussion, does not give the optimized angular path-relative-entropy cost at prescribed first harmonic or the two-angle rigidity statement. Those original model and first-harmonic identifications are credited to them.

Olsen and Löwen (2024), *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326 / Physical Review E 110, 064606, optimize transport diffusivity by tumble strategies in a chiral active Brownian model, rather than minimizing stationary angular jump entropy at a prescribed first harmonic. Shreshtha and Harris (2019), *Thermodynamic uncertainty for run-and-tumble type processes*, arXiv:1903.01972, bound the ratio of mean current and current variance for a one-dimensional renewal-reward model in terms of tumble-related entropy; that different inequality does not directly specify the circle-valued two-angle minimizer at a prescribed complex first moment.

Garcia-Millan and Pruessner (2021), *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, Journal of Statistical Mechanics 063203, examine entropy production in a confined one-dimensional run-and-tumble model. Pruessner and Garcia-Millan (2025), *Field theories of active particle systems and their entropy production*, Reports on Progress in Physics 88, 097601, develop broad microscopic entropy-production formulas. The general stationary entropy formula and elementary convexity ingredients are standard; the specific sharp joint persistence–chirality tradeoff and exact optimizer under arbitrary turning laws are the assessed contribution, not a new definition of entropy production or a general thermodynamic-uncertainty relation.

## Limitations

This is a theorem about the informational time-asymmetry of *orientation jumps* with translation-invariant Poisson turning increments. It does not compute total positional entropy production, physical heat, motor energy, path irreversibility with odd-parity conventions for all degrees of freedom, or effects of interactions or confined spatial boundaries. The entropy-efficient two-angle optimizer is an atomic distribution; for smooth densities the identical sharp value is an infimum, not an attained minimum. The bound constrains the first harmonic only: distinct higher harmonics can have different entropy costs above the infimum. The proof does not require or establish ergodicity for every atomic rotation law. No claim of independent external validation is made.

## References

1. C. Britton, Z. Zhang, S. Han, T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519v1 (first public 2026-08-24), https://arxiv.org/abs/2608.23519 .
2. K. S. Olsen, H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, Phys. Rev. E 110, 064606 (2024), arXiv:2405.14326, https://doi.org/10.1103/PhysRevE.110.064606 .
3. M. Shreshtha, R. J. Harris, *Thermodynamic uncertainty for run-and-tumble type processes*, EPL 126, 40007 (2019), arXiv:1903.01972, https://arxiv.org/abs/1903.01972 .
4. R. Garcia-Millan, G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. 063203 (2021), https://doi.org/10.1088/1742-5468/ac014d .
5. G. Pruessner, R. Garcia-Millan, *Field theories of active particle systems and their entropy production*, Rep. Prog. Phys. 88, 097601 (2025), https://doi.org/10.1088/1361-6633/adff30 .
