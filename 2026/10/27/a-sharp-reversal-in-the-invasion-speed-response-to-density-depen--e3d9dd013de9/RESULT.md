# A sharp reversal in the invasion-speed response to density-dependent motility

## Finding

Consider a population with a strong Allee effect and density-dependent motility. For \(D_0>0\), \(\rho>0\), \(0<a<1\), and \(-1<b\leq 1\), let
\[
\partial_t u=\partial_x\!\left(D_0[1+b u(2-u)]\,\partial_xu\right)
                 +\rho u(1-u)(u-a),\qquad x\in\mathbb R.
\]
This diffusivity corresponds to the individual crowding law \(G(u)=(1-u)(1+b u)\) in the Li--Buenzli--Simpson continuum construction [1]. The model admits a unique, up to translation, strictly decreasing travelling front \(u(x,t)=U_b(x-c_b t)\) from the occupied equilibrium \(1\) to extinction \(0\).

**Theorem (speed response and exact phase boundaries).** For each fixed \(a\in(0,1)\), the speed \(c_b\) is smooth in \(b\) near \(b=0\), and
\[
\boxed{\displaystyle
 c_b=\sqrt{\rho D_0}\left[
 \frac{1-2a}{\sqrt{2}}
 +b\frac{\sqrt{2}(1+2a)(4a^2-17a+9)}{60}
 +O_a(b^2)\right].}
\]
In particular, the response to strengthening motility changes sign at exactly
\[
\boxed{\displaystyle a_*=\frac{17-\sqrt{145}}8=0.619800677650963\ldots .}
\]
For \(0<a<a_*\) the derivative \(\partial_b c_b|_{b=0}\) is positive; for \(a=a_*\) it is zero; and for \(a_*<a<1\) it is negative. Since the unperturbed speed is negative for \(a>1/2\), increasing motility **slows an already retreating population front** when \(1/2<a<a_*\), but **speeds its retreat** when \(a_*<a<1\). For \(a<1/2\), it speeds an advancing front. These are statements about derivatives at zero crowding perturbation, not global monotonicity at arbitrary \(b\).

Separately, for the entire admissible motility range the direction of the front is characterized exactly:
\[
\boxed{\displaystyle
\operatorname{sgn}(c_b)
=\operatorname{sgn}\bigl(5+4b-(10+7b)a\bigr).}
\]
Thus the standing-front boundary is \(a=(5+4b)/(10+7b)\). The speed-response threshold \(a_*\) and the propagation/retreat threshold \(1/2\) at \(b=0\) are distinct: they answer different biological questions.

## Assumptions and scope

The unknown \(u\) is a continuous normalized population density taking values in \([0,1]\). The spatial domain is the entire real line with no external forcing, advection, immigration, seasonal effects, or stochastic fluctuations. The Allee reaction is exactly \(\rho u(1-u)(u-a)\), and the population front is the monotone heteroclinic from \(1\) on the left to \(0\) on the right. Positive \(c_b\) denotes invasion to the right; negative \(c_b\) denotes retreat. We assume \(-1<b\leq1\) to ensure strictly positive diffusivity on \([0,1]\); at \(b=-1\) the diffusion degenerates at occupancy \(1\), and that endpoint is deliberately excluded. The parameter \(a\) remains fixed inside \((0,1)\) for the small-\(b\) expansion. Scaling parameters \(D_0\) and \(\rho\) enter only through the positive speed factor \(\sqrt{D_0\rho}\).

The cited source [1] studies bistable population survival under finite-strip initial conditions; the present calculation instead concerns the asymptotic velocity of a monotone wave on an unbounded habitat. A front's local speed response does not by itself determine a finite inoculum's extinction probability or threshold width.

## Proof

**1. Normalization and underlying motility.** Put \(\xi=x\sqrt{\rho/D_0}\) and \(\tau=\rho t\). After dropping the new coordinate labels, write \(d_b(u)=1+bq(u)\), \(q(u)=u(2-u)\), and \(f_a(u)=u(1-u)(u-a)\). The reduced equation is \(u_t=(d_b(u)u_x)_x+f_a(u)\). For \(u\in[0,1]\), \(q(u)\in[0,1]\); consequently \(d_b(u)>0\) if \(-1<b\leq1\). Substituting \(G(u)=(1-u)(1+bu)\) into [1, Eq. (4)] yields precisely \(d_b(u)=uG'(u)+(1+u)G(u)/(1-u)=1+b(2u-u^2)\).

**2. Front existence, uniqueness, and direction.** A decreasing profile satisfies
\[
(d_b(U)U')'+cU'+f_a(U)=0,\qquad
U(-\infty)=1,\quad U(+\infty)=0.
\]
For smooth positive diffusivity and the bistable sign pattern, existence and uniqueness of the selected speed and decreasing profile follow from the shooting theorem of Drábek--Zahradníková [2, Theorem 4.12 and Remark 4.13], with the stationary case obtained directly below. Let \(P=d_b(U)U'\). Multiply the wave equation by \(P\), integrate across the real line, and use \(P(\pm\infty)=0\). This gives the exact identity
\[
 c\int_{\mathbb R}d_b(U)(U')^2\,dz
 =\int_0^1d_b(s)f_a(s)\,ds
 =\frac{5+4b-(10+7b)a}{60}.
\]
The left integral is strictly positive except for its speed factor. This proves the sign formula. At equality, the standing profile can be constructed directly. Set
\[
 P(s)=-\left(2\int_s^1 d_b(v)f_a(v)\,dv\right)^{1/2},\qquad
 U'=P(U)/d_b(U).
\]
The integral under the square root is positive for \(0<s<1\): this follows from \(f_a<0\) below \(a\), \(f_a>0\) above \(a\), and its zero total weighted integral. Its quadratic vanishing at both endpoints produces infinite spatial tails. This determines a decreasing stationary front uniquely up to translation. Therefore the sign law includes the zero-speed boundary without invoking an unproved limiting argument.

**3. Differentiability at constant diffusivity.** In the normalized problem at \(b=0\), the explicit front and speed are
\[
 U_0(z)=\frac1{1+e^{z/\sqrt2}},\qquad c_0=\frac{1-2a}{\sqrt2},\qquad U_0'=-\frac{U_0(1-U_0)}{\sqrt2}.
\]
For local smoothness of the front-speed branch, rewrite the travelling equation as the planar system \(U'=P/d_b(U)\), \(P'=-cP/d_b(U)-f_a(U)\). Its equilibria \((U,P)=(1,0)\) and \((0,0)\) are hyperbolic saddles for \(a\in(0,1)\) and \(b\) close to zero. Each relevant one-dimensional invariant branch depends smoothly on \((b,c)\) and crosses the section \(U=1/2\). At \((b,c)=(0,c_0)\) the branches meet. Their intersection is transverse with respect to the parameter \(c\): otherwise differentiating both branches with respect to \(c\) would produce a decaying solution \(W\) of \(LW=-U_0'\), where
\[
L=\partial_z^2+c_0\partial_z+f'_a(U_0).
\]
But \(L^*(e^{c_0z}U_0')=0\), and integration against this adjoint zero mode would require \(\int_{\mathbb R}e^{c_0z}(U_0')^2\,dz=0\), an impossibility. The integral is positive and finite because \(0<a<1\). Smooth invariant manifolds and the ordinary implicit-function theorem now give a locally unique smooth \(c_b\) and phase-fixed \(U_b\). This also justifies the \(O_a(b^2)\) remainder.

**4. Adjoint perturbation and beta integration.** Differentiate the travelling equation in \(b\) at zero. With \(U_1=\partial_bU_b|_{b=0}\) and \(c_1=\partial_b c_b|_{b=0}\),
\[
LU_1+c_1U_0'+\bigl(q(U_0)U_0'\bigr)'=0.
\]
Pair against \(\psi=e^{c_0z}U_0'\). Integration by parts (the boundary terms vanish exponentially) yields
\[
 c_1=
 \frac{\int_{\mathbb R}\bigl(e^{c_0z}U_0'\bigr)'q(U_0)U_0'\,dz}
 {\int_{\mathbb R}e^{c_0z}(U_0')^2\,dz}
 =\sqrt2\,\mathbb E[Q(2-Q)(Q-a)],
\]
where \(Q\) has the beta density proportional to \(s^{2a}(1-s)^{2-2a}\) on \((0,1)\), namely \(Q\sim\operatorname{Beta}(1+2a,3-2a)\). The second equality uses \(U_0''/U_0'=(2U_0-1)/\sqrt2\), so that \(c_0+U_0''/U_0'=\sqrt2(U_0-a)\).

Writing \(p=1+2a\), the beta moments are \(\mathbb EQ=p/4\), \(\mathbb EQ^2=p(p+1)/20\), and \(\mathbb EQ^3=p(p+1)(p+2)/120\). Therefore
\[
\mathbb E[Q(2-Q)(Q-a)]
 =2\mathbb EQ^2-\mathbb EQ^3-a(2\mathbb EQ-\mathbb EQ^2)
 =\frac{(1+2a)(4a^2-17a+9)}{60}.
\]
The root of the quadratic factor inside \((0,1)\) is \((17-\sqrt{145})/8\); the other root lies above \(1\). This proves the sharp derivative trichotomy. Restoring the speed scale \(\sqrt{\rho D_0}\) completes the theorem.

## Verification

The accompanying `verify_front.py` uses rational polynomial arithmetic to check the complete beta-moment polynomial identity, and independently solves the two-sided travelling-wave boundary-value problem at several small positive and negative crowding strengths. The numerical method integrates the physical flux \(P=d_b(U)U'\) on both sides of the midpoint \(U=1/2\), matching the slopes there and imposing the correct linearized exponential tails. It also checks that fronts at two nonzero-crowding exact Maxwell points have numerically vanishing speed. Run `python verify_front.py` with the dependencies in `requirements.txt`.

The reported checks passed. For \(a=0.20\), \(a=0.50\), and \(a=0.80\), the symmetric numerical speed differences at \(b=\pm0.005\) were, respectively, \(0.190070706\), \(0.070710969\), and \(-0.125016577\), against analytical derivatives \(0.190070303\), \(0.070710678\), and \(-0.125016479\). At \(b=-0.5\) and \(b=0.5\), the exactly balanced values \(a=6/13\) and \(a=14/27\) produced numerical speeds of magnitude below \(5\cdot10^{-12}\). This finite numerical corroboration is not a proof of the infinite-domain theorem; the proof is above.

## Relationship to prior work

Li, Buenzli, and Simpson [1] derive the crowding-to-diffusivity map and investigate survival/extinction for strip inocula numerically. Their examples include \(b=\pm1/2\), and they provide no small-crowding front-speed coefficient or Allee-level reversal threshold. Drábek and Zahradníková [2] establish a general bistable existence/uniqueness and weighted-sign theory, covering the existence and sign ingredients used here, but not this model-specific adjoint speed derivative or its sign change. The earlier Li--van Heijster--Marangell--Simpson study [3] treats logistic growth and diffusivity that may become negative; it does not furnish the strictly positive-diffusion strong-Allee speed response. Petrovskii and Li [4] obtain exact invasion fronts for a nonlinear *advection* velocity proportional to density, retaining constant diffusive transport; this is not the flux-nonlinearity perturbation studied here. Tsai [5] studies *minimal* wave speeds and linear-versus-nonlinear determinacy for a migration/advection model, rather than the unique-speed bistable front with the cubic reaction and crowding-derived positive diffusivity of [1]. Strier, Zanette, and Wio [6] study front speeds with piecewise-linearized kinetics and abruptly changing diffusivity; their full text was not accessible for a complete comparison, so possible hidden specialization is a residual bibliographic uncertainty. The full primary text of [5] was likewise not accessible, though its public abstract and displayed results concern minimal-speed selection rather than the unique bistable speed calculated here.

The new mathematical assertion is the evaluated exact speed derivative and its sharp sign reversal, not the general existence of bistable waves, not the general weighted-area sign principle, and not the observation that motility influences population survival.

## Limitations

The result is for the deterministic one-dimensional continuous-density PDE on the whole line. It does not quantify finite population extinction probabilities, finite initial patch critical widths, multidimensional curved fronts, or varying \(a\) on the same perturbation scale as \(b\). The derivative sign at \(b=0\) does not prove a speed monotonicity law for all admissible \(b\). At the exact reversal \(a=a_*\), higher-order terms decide the nonzero-\(b\) response; no sign claim is made there. Smoothness and uniform constants become more delicate as \(a\to0\), \(a\to1\), or \(b\to-1\). The reference comparison does not exclude every possible equivalent formula in earlier front-perturbation literature. In particular, full primary text was unavailable for [5] and [6], and any unindexed matching smooth-diffusion perturbation remains a bibliographic risk.

## References

[1] Y. Li, P. R. Buenzli, and M. J. Simpson, *Interpreting how nonlinear diffusion affects the fate of bistable populations using a discrete modelling framework*, Proceedings of the Royal Society A **478** (2022), 20220013, doi:10.1098/rspa.2022.0013. First arXiv version publicly listed 2021-12-21: https://arxiv.org/abs/2112.10989 ; full author manuscript: https://arxiv.org/pdf/2112.10989.

[2] P. Drábek and M. Zahradníková, *Traveling waves for unbalanced bistable equations with density dependent diffusion*, Electronic Journal of Differential Equations **2021** no. 76, 1-21 (2021), doi:10.58997/ejde.2021.76. Open full text: https://www.maths.tcd.ie/EMIS/journals/EJDE/Volumes/2021/76/drabek.pdf.

[3] Y. Li, P. van Heijster, R. Marangell, and M. J. Simpson, *Travelling wave solutions in a negative nonlinear diffusion--reaction model*, Journal of Mathematical Biology **81** (2020), 1495-1522, doi:10.1007/s00285-020-01547-1. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7717045/.

[4] S. Petrovskii and B.-L. Li, *An exactly solvable model of population dynamics with density-dependent migrations and the Allee effect*, Mathematical Biosciences **186** (2003), 79-91, doi:10.1016/S0025-5564(03)00098-1 (author-deposited full text, especially Sections 2 and 4.2: https://www.researchgate.net/publication/9064016_An_exactly_solvable_model_of_population_dynamics_with_density-dependent_migrations_and_the_Allee_effect).

[5] J.-C. Tsai, *Minimal wave speed for a population model with density-dependent migrations and the Allee effect*, Discrete and Continuous Dynamical Systems B **28** (2023), 6393-6411, doi:10.3934/dcdsb.2023058 (journal abstract and displayed figures accessed; full article text not obtained).

[6] D. E. Strier, D. H. Zanette, and H. S. Wio, *Wave fronts in a bistable reaction-diffusion system with density-dependent diffusivity*, Physica A **226** (1996), 310-323, doi:10.1016/0378-4371(95)00397-5 (abstract accessible; full primary manuscript not obtained).
