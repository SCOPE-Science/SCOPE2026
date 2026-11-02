# Universal first-passage ordering under diffusivity rearrangement and renewal resetting

## Finding

Fix a physical interval \([0,L]\), an absorbing target at \(0\), a reflecting endpoint at \(L\), and a fixed initial and reset position \(a\in(0,L)\). A heterogeneous diffusivity field may be spatially rearranged, but its value distribution (the material inventory) is fixed. For the optical-coordinate interpretation of one-dimensional Stratonovich diffusion, **the entire first-passage-time distribution, under any independent positive renewal reset clock, is optimized by placing the largest diffusivities next to the target**. Placing the smallest diffusivities next to the target gives the opposite, slowest, extreme. All intermediate first-passage laws form a strictly stochastically ordered one-parameter family; no other property of the spatial arrangement affects this law.

To state the sharp bounds, let \(g(x)=D(x)^{-1/2}\), let \(g^{\uparrow}\) be its nondecreasing rearrangement on \([0,L]\), and put
\[
Y=\int_0^L g(x)\,dx,\qquad
u_-=\int_0^a g^{\uparrow}(x)\,dx,\qquad
u_+=\int_{L-a}^L g^{\uparrow}(x)\,dx.
\]
Write \(D_{\rm fast}\) for a nonincreasing arrangement of \(D\) (large diffusion near the absorber), and \(D_{\rm slow}\) for a nondecreasing arrangement (small diffusion near the absorber). If \(\tau_D\) is the actual completion time, then for every equimeasurable \(D\) and every shared iid positive reset-interval law there is a coupling satisfying
\[
\boxed{\tau_{D_{\rm fast}}\leq\tau_D\leq\tau_{D_{\rm slow}}\quad\text{almost surely}.}
\]
Consequently the bounds hold simultaneously for survival probabilities, all quantiles, all nondecreasing losses with well-defined extended expectations, and all Laplace transforms in the reversed direction. For two distinct optical starting distances \(u<v\), the corresponding completion-time laws are distinct and strictly ordered at some positive time. Every \(u\in[\nu_-,\nu_+]\) is realized by an equimeasurable arrangement, so this interval is the **exact** set of achievable first-passage laws.

## Assumptions and scope

The parameters satisfy \(L>0\) and \(0<a<L\). The diffusivity histogram is prescribed by a measurable \(D_*:[0,L]\to(0,\infty)\) with constants \(0<d_-\leq D_*(x)\leq d_+<\infty\) almost everywhere. An admissible \(D\) is any measurable profile on \([0,L]\) equimeasurable with \(D_*\). Define the strictly increasing, bi-Lipschitz optical map \(y_D(x)=\int_0^xD(s)^{-1/2}\,ds\) and its inverse.

Let \(U\) be a Brownian motion with generator \(\partial_{yy}\) reflected at \(Y=y_D(L)\) and killed on first reaching \(0\). Between resets, the physical process is \(X_t=y_D^{-1}(U_t)\). For differentiable positive \(D\), this is the usual reflected/absorbed Stratonovich equation \(dX_t=\sqrt{2D(X_t)}\circ dW_t\), with the appropriate reflection at \(L\). For discontinuous or merely measurable \(D\), **the optical pullback is the definition**, avoiding unspecified interface conventions for multiplicative noise.

At time zero the process starts at \(a\). Following each unsuccessful reset interval it returns instantly to \(a\), uses fresh Brownian increments, and continues until absorption. Reset intervals \(R_1,R_2,\ldots\) are iid, strictly positive and finite almost surely, independent of all Brownian motions and with the same distribution for every arrangement. No moment assumption is imposed on their law. This covers deterministic, exponentially distributed, and general independent renewal clocks, but not position-dependent, feedback-adapted, or arrangement-dependent resetting.

## Proof

**1. Optical reduction.** Under the optical map, every admissible profile has the same reflected length \(Y=\int_0^L g\), because equimeasurability preserves integrals. Its reset position is \(u_D=y_D(a)=\int_0^a g\). Hence the completed-time law depends on \(D\) only through \((Y,u_D)\) and the common reset clock. This is an exact process equivalence, not an effective-diffusion approximation.

**2. Sharp rearrangement bounds.** Equimeasurability of \(g\) and the elementary layer-cake rearrangement inequality imply
\[
\nu_-\leq \int_0^a g(x)\,dx\leq\nu_+.
\]
The lower endpoint is attained by \(g=g^{\uparrow}\), equivalent to nonincreasing \(D\); the upper endpoint is attained by \(g(x)=g^{\uparrow}(L-x)\), equivalent to nondecreasing \(D\). Ties and rearrangements within either side of \(a\) need not be unique.

**3. Order-preserving reflected Brownian coupling.** For a Brownian path \(B\) beginning at zero and \(u\in(0,Y)\), the upper-reflected but not-yet-killed coordinate is exactly
\[
V_t^u=u+\sqrt2 B_t-\bigl(u+\sup_{0\le s\le t}\sqrt2 B_s-Y\bigr)_+.
\]
For fixed \(t\), this expression is nondecreasing and \(1\)-Lipschitz in \(u\); explicitly, it is \(u+\sqrt2 B_t\) before activation of the upper regulator and \(Y+\sqrt2 B_t-\sup_{s\le t}\sqrt2 B_s\) afterwards. Thus \(u\le v\) implies \(V_t^u\le V_t^v\) on the same Brownian sample path. Killing at zero preserves the order of the **first hitting times**: \(H^u\le H^v\) almost surely. One does not need a monotone ordering of physical positions under different coordinate maps.

**4. Reset coupling.** Use the same positive reset lengths \(R_j\) and the same independent Brownian segment for the \(u\)- and \(v\)-processes in each cycle. If the \(v\)-process is absorbed during a cycle, the \(u\)-process must already have been absorbed in that cycle or an earlier one. At every reset both surviving processes return to their ordered optical starts. Induction over the cycles proves \(\tau^u\le\tau^v\) pathwise. This reasoning uses no exponential-memorylessness and no reset-time moments.

Each cycle has a strictly positive chance to complete: choose \(t_0>0\) with \(\Pr(R_1>t_0)>0\), and use \(\Pr(H^u\le t_0)>0\). Independence gives a positive per-cycle success probability, so \(\tau^u<\infty\) almost surely. If \(u<v\), Brownian full support provides a positive-probability event with \(H^u<t_0<H^v\), while \(R_1>t_0\). Therefore \(\Pr(\tau^u\le t_0<\tau^v)>0\), establishing genuine distinction of the completion laws.

**5. Exact attainability.** For \(s\in[0,L-a]\), define an equimeasurable cyclic shift of the monotone optical profile by \(g_s(x)=g^{\uparrow}((x+s)\bmod L)\). Then
\[
u(s)=\int_0^a g_s(x)\,dx=\int_s^{s+a}g^{\uparrow}(z)\,dz.
\]
The function \(\nu(s)\) is continuous, nondecreasing, and satisfies \(\nu(0)=\nu_-\) and \(\nu(L-a)=\nu_+\). Its image is the full interval \([\nu_-,\nu_+]\). Together with strictness, this proves the complete one-parameter classification, not only endpoint bounds.

**6. Renewal and Poisson checks.** Writing \(S_0(t;u)=\Pr(H^u>t)\), the completion survival function for arbitrary \(R\) satisfies the exact first-renewal identity
\[
S_R(t;u)=\Pr(R>t)S_0(t;u)+\int_{(0,t]}S_0(s;u)S_R(t-s;u)\,dF_R(s).
\]
The no-reset hitting-time Laplace transform is
\[
q_s(u)=\mathbb E[e^{-sH^u}]=\frac{\cosh(\sqrt{s}(Y-u))}{\cosh(\sqrt{s}Y)},\qquad s>0.
\]
For Poisson resets of rate \(r>0\), the transformed completed-time law and its mean are
\[
\mathbb E[e^{-s\tau_r^u}]=\frac{(r+s)q_{r+s}(u)}{s+r q_{r+s}(u)},\qquad
\mathbb E\tau_r^u=\frac{q_r(u)^{-1}-1}{r}.
\]
The latter mean expression is **prior work** (the equivalent formula in Menon Jr. and Anteneodo, Eq. (19)); it is provided only as an exact normalization and reproducibility check, not as a new finding. The new classification is the full stochastic order for every independent renewal clock and the exact attainable family under equimeasurable material constraints.

## Verification

The bundled `verify.py` is executable with standard Python: `python verify.py`. It checks every permutation of a six-layer optical medium against the sharp rearrangement bounds; tests all sampled cyclic shifts; runs synchronized discrete-sampling diagnostics for upper-reflected Brownian paths and repeated reset cycles; and independently evaluates Laplace transforms, the prior Poisson formula, and its no-reset limit. It issues 66,696 finite assertions. These numerical and finite checks **do not prove** the continuum stochastic order or exact attainment. The proof is Steps 1–5 above, especially the explicit Skorokhod map and layer-cake rearrangement.

For a two-material example take \(L=1\), \(a=0.4\), diffusivity \(4\) over one half and \(1\) over the other. Every arrangement has \(Y=0.75\). Fast-near-target sorting has \(u=0.2\), slow-near-target sorting has \(u=0.4\). At Poisson reset rate \(r=1\), the mean completion times are approximately \(0.120839494131\) and \(0.219239409018\), respectively. This is illustrative; the theorem holds for the entire distributions and any common positive renewal clock.

## Relationship to prior work

Menon Jr. and Anteneodo (arXiv:2408.04726v1, August 8, 2024) derive the optical coordinate and the exact **mean** first-passage time for arbitrary spatial diffusivity in the Stratonovich model with Poisson resetting; their sections II–IV discuss examples and other noise prescriptions, and their concluding discussion identifies arrival-time distributions as a future direction. The coordinate transform, the exponential-clock renewal framework, and the Poisson mean formula are therefore not new. The present statement adds a distribution-level **uniform material-arrangement optimum for all iid positive reset-clock laws**, an exact pathwise comparison, and realization of every intervening distribution.

Pal and Prasad (arXiv:1812.03009, 2018) treat resetting and first passage in an interval with spatially homogeneous diffusion. Barbini and Giuggioli (J. Phys. A 57 (2024), 425001, DOI 10.1088/1751-8121/ad7ca2) examine a different lattice/interface-resetting model. Linn and Lawley (Phys. Rev. E 108 (2023), 024114) develop asymptotic full-distribution results at high resetting frequencies for broad protocols, rather than a finite-rate material-arrangement optimization. These distinctions are based on the indicated available material; the possibility that a wider comparison or rearrangement theorem already subsumes this result remains an originality risk.

## Limitations

The result is for the **optical-coordinate (Stratonovich) prescription**, not generic Itô, anti-Itô, or interface transmission conventions. The physical initial/reset location \(a\), physical length \(L\), and diffusivity histogram must be held fixed across designs. Resetting must be exogenous, independent, complete and to the original launch point. The claim does not cover adaptive spatially dependent resets, random changes of the material inventory, multiple absorbing targets, or higher dimensions. The inequality does not imply that optimizing all physical observables or finite-sample estimation is possible. For arbitrary waiting-time laws some monotone costs can have infinite expectations; stochastic ordering still holds. Publication priority has not been independently certified.

## References

1. L. Menon Jr. and C. Anteneodo, *Random search with resetting in heterogeneous environments*, arXiv:2408.04726v1 (first publicly submitted 2024-08-08), https://arxiv.org/html/2408.04726v1; Phys. Rev. E **110**, 054111 (2024), DOI 10.1103/PhysRevE.110.054111.
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018); Phys. Rev. E **99**, 032123 (2019), https://arxiv.org/abs/1812.03009.
3. A. Barbini and L. Giuggioli, *Lattice random walk dynamics with stochastic resetting in heterogeneous space*, J. Phys. A: Math. Theor. **57**, 425001 (2024), https://doi.org/10.1088/1751-8121/ad7ca2.
4. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Phys. Rev. E **108**, 024114 (2023), https://doi.org/10.1103/PhysRevE.108.024114.
