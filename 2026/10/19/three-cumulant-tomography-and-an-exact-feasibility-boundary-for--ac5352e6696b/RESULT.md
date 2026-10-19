# Three-cumulant tomography and an exact feasibility boundary for trapped active particles

## Finding

For the stationary one-dimensional harmonic run-and-tumble diffusion defined below, **the variance, fourth cumulant, and sixth cumulant determine its three stationary parameter combinations uniquely**, including an unknown thermal diffusivity and an unknown propulsion scale. Conversely, an explicit system of inequalities on the three cumulants is necessary and sufficient for a stationary law of this model to realize them. The variance and fourth cumulant alone leave a continuous one-parameter ambiguity, so the sixth cumulant is the *lowest-order additional nonzero even cumulant* that resolves it.

Let \(K_2,K_4,K_6\) denote the second, fourth and sixth cumulants of the centered stationary position. Put \(b=1+2\gamma/k>1\), \(a=v/k>0\), \(w=D/k>0\). Then

\[
K_2=w+\frac{a^2}{b},\qquad
K_4=-\frac{6a^4}{b^2(b+2)},\qquad
K_6=\frac{240a^6}{b^3(b+2)(b+4)}.
\]

In particular, the thermal-insensitive shape ratio

\[
R:=\frac{K_6}{(-K_4)^{3/2}}=\frac{20\sqrt6}{3}\frac{\sqrt{b+2}}{b+4}
\]

is strictly decreasing as \(b\) increases from \(1\) to infinity, with exact image \((0,4\sqrt2)\). Define \(q=3R^2/800\). The unique admissible solution and the recovered parameters are

\[
 b=\frac{1-8q+\sqrt{1-8q}}{2q},\qquad
 a=\left(\frac{(-K_4)b^2(b+2)}6\right)^{1/4},\qquad
 w=K_2-\frac{a^2}{b}.
\]

Thus a real triple of cumulants is realizable in the **strictly positive** physical-parameter regime if and only if \(K_4<0\), \(K_6>0\), \(0<R<4\sqrt2\) and the reconstructed \(w\) is strictly positive (equivalently \(K_2>a^2/b\)). The corresponding dimensionless physical parameters are \((\gamma/k,v/k,D/k)=((b-1)/2,a,w)\). The absolute rate \(k\) is not identified by the stationary position law because simultaneous rescaling of all four rates leaves it unchanged.

## Assumptions and scope

Fix \(k,v,D,\gamma>0\). The stationary real-valued process satisfies

\[
 dX_t=(-kX_t+vS_t)\,dt+\sqrt{2D}\,dB_t,
\]

where \(B_t\) is standard Brownian motion and the independent two-state process \(S_t\in\{-1,+1\}\) changes sign at Poisson rate \(\gamma\). The trap center is fixed at the origin; the orientation switching is symmetric. The result concerns the exact population cumulants of stationary position, not estimated finite-sample cumulants or sampled trajectories. All comparisons take place within this same model class, with strictly positive parameters. The source's Gaussian-convolution stationary distribution and its ordinary moments are **not** new claims.

## Proof

**1. Independent stationary summands and beta moments.** Solving the stable linear stochastic equation backward gives two independent stationary terms, one depending on the telegraph process and one on Brownian increments. The Ornstein–Uhlenbeck term is centered normal with variance \(w\). The athermal term has the established beta density on \((-a,a)\), proportional to \((1-(x/a)^2)^{\ell-1}\) with \(\ell=\gamma/k>0\). Therefore, writing \(X\overset d=aY+\sqrt w Z\) for independent standard normal \(Z\) and \(Y\) with density proportional to \((1-y^2)^{\ell-1}\), one has for every integer \(j\ge0\)

\[
 \mathbb E[Y^{2j}]=\frac{(1/2)_j}{(\ell+1/2)_j},\qquad \mathbb E[Y^{2j+1}]=0.
\]

In particular, writing \(b=2\ell+1\), \(\mathbb E[Y^2]=1/b\), \(\mathbb E[Y^4]=3/[b(b+2)]\), and \(\mathbb E[Y^6]=15/[b(b+2)(b+4)]\). These are exact beta-integral identities. The Gaussian's cumulants of order four and six vanish and cumulants add under convolution.

**2. Derive the three cumulants.** For every centered symmetric variable, the fourth cumulant is \(\mathbb E[X^4]-3\mathbb E[X^2]^2\), and the sixth is \(\mathbb E[X^6]-15\mathbb E[X^4]\mathbb E[X^2]+30\mathbb E[X^2]^3\). Apply these identities to the active beta variable, then add only the Gaussian variance at order two. Direct common-denominator simplification gives the three displayed formulas. In particular \(K_4<0\) and \(K_6>0\) throughout the stated domain, so the shape ratio is well-defined.

**3. Uniqueness and explicit inversion.** Eliminating \(a\) from the fourth and sixth cumulants gives the displayed \(R\). Its logarithmic derivative is

\[
 \frac{d}{db}\log R=\frac1{2(b+2)}-\frac1{b+4}=-\frac{b}{2(b+2)(b+4)}<0.
\]

It follows by endpoint limits that \(R:(1,\infty)\longrightarrow(0,4\sqrt2)\) is a bijection. Solving \(q(b+4)^2=b+2\) yields two algebraic branches; the displayed plus branch is the unique one with \(b>1\) when \(0<q<3/25\). Once \(b\) is determined, the unique positive \(a\) is fixed by \(K_4\), and \(w\) is fixed by \(K_2\). No other positive parameters can share the triple.

**4. Exact feasibility, including strict boundaries.** Every model triple meets the four inequalities because \(a,w,\ell>0\) and the monotone range is open. Conversely, for any real triple obeying them, the explicit formulas produce unique \(b>1,a>0,w>0\); substituting into the three cumulant formulas recovers all three original numbers, establishing sufficiency. The limits \(b\downarrow1\), \(b\to\infty\), \(a\downarrow0\) or \(w\downarrow0\) are *not* asserted to belong to the strictly positive domain.

**5. Minimality of the sixth cumulant.** Fix any interior model triple. Holding \(K_2,K_4\) fixed, vary \(b\) in an open neighborhood of its true value and choose \(a(b)=((-K_4)b^2(b+2)/6)^{1/4}\) and \(w(b)=K_2-a(b)^2/b\). Continuity keeps \(w(b)>0\) in a sufficiently small neighborhood, producing infinitely many distinct physical parameter triples with exactly the same second and fourth cumulants. Symmetry sets odd cumulants to zero. Thus no lower-order even-cumulant data resolve the three dimensionless parameters; adding the sixth does, by steps 3–4.

## Verification

The companion `verification.py` constructs independent even raw moments by multiplying beta and Gaussian moment-generating series and forms cumulants from their definitions. It checks exact rational equalities for 840 strictly positive parameter triples, tests numerical inversion, verifies the two-cumulant ambiguity along a nontrivial parameter curve, and independently checks the algebraic inverse at several endpoint-sensitive \(b\) values. Its successful execution yielded **3,383 assertions**. The computations check formulas for finite parameter samples and do not substitute for the monotonicity and surjectivity proof above.

## Relationship to prior work

Sevilla and Meléndez Mora (2026), Section III and Appendix B, establish the stationary beta–Gaussian convolution and explicit stationary moments for the same process. Garcia-Millan and Pruessner (2021) had previously obtained the position marginal through field-theoretic methods; Sun, Ye and Podgornik (2025) develop moment formulas for a finite-tumble-time extension. None of these published results is claimed here as a new stationary distribution, convolution, moment formula, or forward solution. The present inverse result is the **global injectivity and exact image of the three-cumulant map**, together with a minimality obstruction when the sixth cumulant is omitted. These are algebraically derived from established forward formulas, which must be acknowledged as strong prior coverage and may reduce any claim of conceptual novelty. The nearest indexed comparisons of this same particle model concern stationary density modality and thermal-noise bifurcation rather than cumulant inverse identifiability.

## Limitations

The result reconstructs only ratios to the known or unknown relaxation scale \(k\), not the absolute physical clock; fixed trap-center calibration and symmetric telegraph switching are assumed. Measurements must yield exact stationary cumulants; finite-sample errors, moment-estimation instability, spatially varying diffusivity and unknown observation noise distributions are excluded. The inverse becomes increasingly ill-conditioned in absolute \(R\) sensitivity at rapid tumbling because \(R\to0\). Higher even moments, complete probability densities and time correlations may provide other identification methods and are not asserted to be impossible. The underlying forward moment formulas are prior work; an independently reviewed novelty assessment is still required.

## References

1. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1, first public August 22, 2026. Sections III and Appendix B.
2. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. (2021) 063203, DOI: 10.1088/1742-5468/ac014d. In particular Appendix D on stationary distributions.
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, Phys. Rev. E 111 (2025) 044136, DOI: 10.1103/PhysRevE.111.044136.
