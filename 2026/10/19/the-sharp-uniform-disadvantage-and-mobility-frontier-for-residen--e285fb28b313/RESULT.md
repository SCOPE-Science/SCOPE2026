# The sharp uniform-disadvantage and mobility frontier for resident-mimicking dispersal

## Finding

For the directed-dispersal two-species competition model, a rare invader that adopts the resident's stationary spatial density as its dispersal target has a strictly positive invasion exponent at equal post-harvest carrying capacity unless the resident already follows an ideal-free profile. More strongly, a spatially uniform carrying-capacity disadvantage has an exact, unique mobility cutoff.

Precisely, let \(\Omega\subset\mathbb R^n\) be bounded, connected and smooth, and let \(P,m,a_1,a\) be strictly positive smooth functions on its closure. Let \(Q=u_*\) be the unique strictly positive stationary solution of
\[
\nabla\!\cdot\!\left(a_1\nabla\frac{u_*}{P}\right)+u_*(m-u_*)=0,\qquad
\partial_\nu(u_*/P)=0.
\]
Put \(r=m-u_*\). For each \(d>0\), define \(\Lambda(d)\) as the principal eigenvalue of
\[
\nabla\!\cdot\!\left(da\nabla\frac{v}{Q}\right)+rv=\Lambda(d)v,
\qquad\partial_\nu(v/Q)=0.
\]
If \(m/P\) is not constant, then \(r\not\equiv0\) and
\[
0<\Lambda(d)<\max_{\bar\Omega}r,\qquad \Lambda'(d)<0,\qquad
\lim_{d\downarrow0}\Lambda(d)=\max_{\bar\Omega}r,
\qquad \lim_{d\to\infty}\Lambda(d)=0.
\]
The invader with post-harvest capacity \(m_2=m-c\), where \(c\ge0\) is spatially constant and \(m-c>0\), has linear invasion exponent exactly \(\Lambda(d)-c\). Thus at equal capacities (\(c=0\)) its invasion exponent is positive for every finite \(d>0\). For every \(0<c<\min\{\max r,\min m\}\), there is exactly one \(d_c\in(0,\infty)\) with \(\Lambda(d_c)=c\): invasion is linearly favored for \(d<d_c\), linearly disfavored for \(d>d_c\), and spectrally neutral at equality.

Let \(h\) be the unique weighted-mean-zero Neumann solution of
\[
-\nabla\!\cdot(a\nabla h)=Qr,\qquad \int_\Omega Qh=0,
\]
and set \(C=\int_\Omega a|\nabla h|^2/\int_\Omega Q>0\). Then
\[
\Lambda(d)=\frac{C}{d}+O(d^{-2})\quad(d\to\infty),\qquad
\lim_{c\downarrow0}c\,d_c=C.
\]
These are sharp linear invasion thresholds, not claims of global species replacement.

A fully explicit one-dimensional example has \(\Omega=(0,\pi)\), \(P=a_1=a=1\),
\[
Q(x)=1+\tfrac14\cos x,\qquad
m(x)=Q(x)+\frac{\cos x/4}{Q(x)},\qquad
m_2(x)=m(x)-\tfrac1{100}.
\]
Both carrying capacities are positive. At invader mobility \(d=1\), the exact positive test function \(v=Q^2\) gives
\[
\Lambda(1)\ge\frac1{35},\qquad
\lambda_{\rm invade}\ge\frac1{35}-\frac1{100}=\frac{13}{700}>0,
\]
although \(m_2<m\) everywhere. In this example \(C=1/32\) and \(d_c\sim 1/(32c)\) for small disadvantages.

## Assumptions and scope

The ecological reaction terms use complete resource sharing and logistic per-capita growth, with no Allee effect, demographic noise or time dependence. The resident's movement operator is \(\nabla\cdot[a_1\nabla(u/P)]\); the invader uses \(\nabla\cdot[da\nabla(v/Q)]\), where the target profile \(Q\) is fixed at the resident-only equilibrium \(u_*\). The boundary condition is zero normal derivative of the population-to-target ratio. Positivity and smoothness ensure a unique resident equilibrium and a simple real principal eigenvalue. The value of \(Q\) need not be normalized: multiplying it by a positive constant can be absorbed into \(a\). Invasion refers to the sign of the linearized invader eigenvalue at \((u_*,0)\).

## Proof

**Resident balance and the exceptional case.** Integrate the resident's stationary equation and use the no-flux condition to obtain
\[\int_\Omega Qr=\int_\Omega u_*(m-u_*)=0.\]
If \(r\equiv0\), then \(u_*=m\) and \(\nabla\cdot[a_1\nabla(m/P)]=0\) with homogeneous Neumann boundary condition. Multiplication by \(m/P\), integration by parts, and positivity of \(a_1\) imply \(m/P\) is constant. Conversely, if \(m=\kappa P\), then \(u_*=m\) is the resident equilibrium and \(r=0\). Thus non-ideal residency means exactly \(r\not\equiv0\), and its weighted mean zero forces \(\max r>0\) and \(\min r<0\).

**Strict invasion at equality.** Write \(v=Qw\). The self-adjoint Neumann eigenproblem on \(L^2(\Omega,Q\,dx)\) has the Rayleigh formula
\[
\Lambda(d)=\sup_{0\ne w\in H^1(\Omega)}
\frac{\int_\Omega Qr\,w^2-d\int_\Omega a|\nabla w|^2}
{\int_\Omega Qw^2}.
\]
For \(w=1+\epsilon r\) and sufficiently small \(\epsilon>0\), the numerator is
\[
2\epsilon\int_\Omega Qr^2+\epsilon^2\left(\int_\Omega Qr^3-d\int_\Omega a|\nabla r|^2\right)>0.
\]
Hence \(\Lambda(d)>0\) at each finite \(d\); a constant test function alone would have given only a zero lower bound. The universal upper bound \(\Lambda(d)\le\max r\) is strict for positive diffusion and nonconstant \(r\), because equality would require a spatially constant positive eigenfunction concentrated entirely at maxima, which cannot solve a nonconstant potential eigenproblem.

**Mobility monotonicity and endpoints.** Let \(w_d>0\) be the simple normalized top eigenfunction. Differentiating the variational eigenvalue gives
\[
\Lambda'(d)=-\frac{\int_\Omega a|\nabla w_d|^2}{\int_\Omega Qw_d^2}<0.
\]
If this derivative vanished, \(w_d\) would be constant, forcing \(r\) constant and contradicting the non-ideal assumption. The upper bound by \(\max r\), together with smooth bump test functions localized near a maximizer, yields \(\Lambda(d)\to\max r\) as \(d\downarrow0\). For large \(d\), the Neumann spectral gap above the constant mode and \(\int Qr=0\) yield \(\Lambda(d)\to0\).

**Quantitative large-mobility law.** On the weighted Hilbert space let \(B=-Q^{-1}\nabla\cdot(a\nabla)\) with Neumann domain. It is nonnegative, self-adjoint, has compact resolvent, and has the one-dimensional kernel of constants. With \(\epsilon=1/d\), the principal eigenvalue of \(-B+\epsilon r\) equals \(\epsilon\Lambda(1/\epsilon)\). Analytic perturbation of its simple isolated eigenvalue zero gives first coefficient \(\int Qr/\int Q=0\) and second coefficient
\[
\frac{\langle r,B^{-1}r\rangle_{L^2(Qdx)}}{\int_\Omega Q}
=\frac{\int_\Omega a|\nabla h|^2}{\int_\Omega Q}=C>0,
\]
where \(B^{-1}\) is restricted to weighted-mean-zero functions. Therefore \(\Lambda(d)=C/d+O(d^{-2})\). The positive, continuous, strictly decreasing function \(\Lambda\) maps \((0,\infty)\) onto \((0,\max r)\). Applying this bijection to \(\Lambda(d_c)=c\) proves existence, uniqueness and \(cd_c\to C\). Replacing \(r\) with \(r-c\) shifts the entire spectrum exactly by \(-c\).

**Exact positive-disadvantage witness.** Put \(t=\cos x\), \(\theta=1/4\), \(Q=1+\theta t\). Then \(Q''=-\theta t\) and \(Qr=\theta t\), so the resident equilibrium equation holds identically. Since \(m=Q+\theta t/Q\) is strictly increasing as a function of \(t\in[-1,1]\), its minimum is \(5/12\), and the invader's minimum capacity is \(5/12-1/100=61/150\). With \(d=1\), choose \(w=Q\), equivalent to \(v=Q^2\). Elementary cosine integrals give
\[
\frac1\pi\int_0^\pi Qr\,w^2\,dx=\frac1{16},\qquad
\frac1\pi\int_0^\pi |w'|^2\,dx=\frac1{32},\qquad
\frac1\pi\int_0^\pi Qw^2\,dx=\frac{35}{32}.
\]
The quotient is \(1/35\), and subtracting \(c=1/100\) gives \(13/700\). The Neumann corrector \(h=\cos x/4-1/32\) has weighted mean zero and satisfies \(-h''=Qr\). Therefore \(C=(\int|h'|^2)/(\int Q)=1/32\), as claimed.

## Verification

The self-contained `verify.py` checks the exact rational cosine-moment integrals, both boundary equilibria, the minimum admissible carrying capacities, the strictly positive invasion witness, and the corrector coefficient. Run `python3 verify.py` from the directory containing this file and the program. The monotonicity, continuum endpoint limits, and asymptotic threshold are proved above analytically; no finite discretization is used as a proof of these infinite-dimensional claims.

## Relationship to prior work

Braverman and Lawson, *Trimming to Coexistence* (2025), define exactly this directed-dispersal competition model. Their Theorem 3.4 proves invasion when the invader targets the resident equilibrium and has a nonnegative carrying-capacity advantage that is strict somewhere. Their Section 5, Question 1(a), explicitly asks for an equal-capacity invasion theorem under non-ideal resident dispersal. Their Example 2 numerically observes some invasions with lower invader capacity; it does not give a mobility-dependent universal sharp cutoff or its inverse-disadvantage scaling. The strict second-variation test here settles Question 1(a) at the linear-invasion level and quantifies the disadvantage that a fixed mimicking strategy can tolerate.

The principal-eigenvalue variational method is standard and used in Braverman and Lawson, as well as in Zahan and collaborators (2024). Cantrell, Cosner, DeAngelis and Padrón (2007) prove, for a discrete-patch family, that a non-ideal resident can be invaded by some dispersal strategy; they do not identify the specified target \(Q=u_*\) for this continuous PDE or the uniform-loss frontier. Wang, Lam and Lutscher (2026) analyze the dispersal reduction principle in a different patch-interface movement operator. Neither the general spectral monotonicity nor prior numerical observations alone establish this coupling-specific threshold and the exact witness here.

## Limitations

The conclusions concern linear invasion at the resident-only equilibrium, not fixation, extinction of the resident, global coexistence, stochastic establishments, or nonlinear outcomes at the neutral cutoff. Part (b) of Braverman and Lawson's Question 1—universal resident exclusion—is not claimed. The exact disadvantage threshold assumes a spatially uniform shift in post-harvest capacity; arbitrary spatial reductions require their own spectral calculation. The small-disadvantage asymptotic is valid for fixed resident equilibrium and fixed normalized mobility profile, not for simultaneously varying environmental fields or singularly rough domains. Independent validation has not been performed.

## References

1. E. Braverman and J. Lawson, *Trimming to Coexistence: How Dispersal Strategies Should Be Accounted for in Resource Management*, Journal of Mathematical Biology (first published 6 December 2025), DOI: 10.1007/s00285-025-02324-8; open preprint arXiv:2512.10898v1 (11 December 2025), especially Sections 3.3, 5 and Appendix A.
2. R. S. Cantrell, C. Cosner, D. L. DeAngelis, and V. Padrón, *The ideal free distribution as an evolutionarily stable strategy*, Journal of Biological Dynamics 1 (2007), 249–271, DOI: 10.1080/17513750701450227, especially Theorem 2.
3. L. Wang, K.-Y. Lam, and F. Lutscher, *Evolution of movement strategies in patchy landscapes*, Journal of Differential Equations 463 (2026), 114217, DOI: 10.1016/j.jde.2026.114217, especially Lemma 4.3.
4. I. Zahan and collaborators, *Evolution of dispersal and the analysis of a resource flourished population model with harvesting* (2024), open access PMC11103478, especially Section 3 principal-eigenvalue arguments.
