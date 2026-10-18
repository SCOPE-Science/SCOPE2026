# A sharp dynamical stability criterion for finite-size fixed-flux populations

## Finding

Consider a size-structured population with positive fixed recruitment flux and constant mortality hazard per unit of size traversed. Although its finite residence time creates a genuinely distributed memory, **every nondegenerate stationary population is linearly exponentially stable exactly when the scalar stationary response is increasing; otherwise it has a real positive growth eigenvalue**. No stationary state can lose linear stability through a nonzero imaginary eigenvalue.

More precisely, let \(L,\kappa,B>0\), and let \(g:[0,\infty)\to(0,\infty)\) be \(C^2\), bounded below by a positive constant. For \(0<x<L\), set
\[
\partial_tu+g(E(t))\partial_xu=-\kappa g(E(t))u,\qquad
E(t)=\int_0^L u(t,x)\,dx,\qquad
 g(E(t))u(t,0)=B.
\]
Every positive equilibrium corresponds uniquely to a positive solution of
\[
h(E)=BJ,\qquad h(E)=Eg(E),\qquad J=\frac{1-e^{-\kappa L}}{\kappa},
\]
and has density \(u_E(x)=B e^{-\kappa x}/g(E)\). If \(h'(E)>0\), the linearization about \(u_E\) is exponentially stable. If \(h'(E)<0\), the linearization has a strictly positive real eigenvalue. At \(h'(E)=0\), zero is a simple characteristic root. There are no nonzero imaginary characteristic roots for any positive \(L,\kappa,B\) and any real \(g'(E)\).

The criterion yields a fully explicit **two-linearly-stable/one-unstable stationary hysteresis window** at finite size. Take \(L=\kappa=1\) and \(g(E)=1-9E/5+E^2\). Define
\[
B_{\pm}=\frac{21/125\ \pm\ 4\sqrt6/1125}{1-e^{-1}}.
\]
For \(B_-<B<B_+\) there are exactly three positive stationary populations. Their lowest and highest environmental masses are linearly exponentially stable; the intermediate one has a positive real eigenvalue. There is a simple stationary fold at each endpoint. At the central flux \(B=21/[125(1-e^{-1})]\), the three masses are exactly
\[
E_1=\frac{3-\sqrt2}{5},\qquad E_2=\frac35,\qquad E_3=\frac{3+\sqrt2}{5},
\]
with \(h'(E_1)=h'(E_3)=4/25>0\), \(h'(E_2)=-2/25<0\). This is a classification of linearized dynamics, **not** a global basin theorem for the nonlinear transport equation.

## Assumptions and scope

The size interval is exactly \([0,L]\); the right boundary is absorbing (outflux), with no return of exiting individuals. Recruitment is prescribed as the physical flux \(B\), not boundary density. There is no harvesting. The environmental output is total abundance, with weight identically one. Positive speed \(g(E)\) depends on abundance but not on size; mortality is \(\kappa g(E)\), so death hazard per unit distance traversed is the constant \(\kappa\). The spectral claim concerns linearization on size-density perturbations with compatible linearized boundary conditions; initial perturbations pass through the finite interval in finite physiological time. No assertion of nonlinear global stability, time-periodic orbit exclusion, or generality for arbitrary mortality functions is made.

## Proof

**Stationary closure.** At a stationary profile, \(g(E)u_x=-\kappa g(E)u\); hence \(u(x)=C e^{-\kappa x}\). The flux boundary fixes \(C=B/g(E)\), and integration gives \(E=BJ/g(E)\), equivalently \(h(E)=BJ\). These steps are reversible.

**Exact time change and renewal reduction.** Define physiological time \(\sigma(t)=\int_0^t g(E(s))\,ds\), strictly increasing. Then the *nonlinear* transport equation becomes \(u_\sigma+u_x=-\kappa u\), while its boundary value is \(u(\sigma,0)=B/g(E(\sigma))\). After one full traversal, \(\sigma\ge L\), the initial-data contribution has exited. Characteristics yield the exact nonlinear renewal relation
\[
E(\sigma)=B\int_0^L\frac{e^{-\kappa x}}{g(E(\sigma-x))}\,dx.
\]
At a stationary \(E\), the linearized renewal relation for an abundance perturbation \(m\) is
\[
m(\sigma)=-\frac{Bg'(E)}{g(E)^2}\int_0^L e^{-\kappa x}m(\sigma-x)\,dx.
\]
For a mode \(e^{\nu\sigma}\), put \(s=\nu/\kappa\), \(k=\kappa L>0\) and \(R=-Bg'(E)/[\kappa g(E)^2]\). The *unmultiplied* characteristic equation is
\[
1=R\int_0^k e^{-(1+s)y}\,dy.
\]
For \(s\ne-1\), it is equivalent to
\[
F(s)=s+1-R+Re^{-k(1+s)}=0.
\]
The polynomial-exponential equation has a potential extraneous root at \(s=-1\) introduced by multiplication; that root lies strictly in the left half-plane and is never used to infer instability.

**Stability and instability.** The stationary closure gives
\[
1-R(1-e^{-k})=\frac{h'(E)}{g(E)}.
\]
If \(R\le0\), no root of \(F\) can have \(\Re s\ge0\): the equality \(|s+1-R|=|R|e^{-k(1+\Re s)}\) contradicts \(|s+1-R|\ge1-R>|R|e^{-k}\). If \(R>0\) and \(h'(E)>0\), then \(R<1/(1-e^{-k})\). Writing \(s=a+ib\) with \(a\ge0\), the imaginary part of \(F=0\) gives
\[
|b|=Re^{-k(1+a)}|\sin(kb)|\le Rke^{-k}|b|.
\]
But \(Rke^{-k}<k/(e^k-1)<1\), so \(b=0\). For real \(a\ge0\), \(F(0)=1-R(1-e^{-k})>0\) and \(F'(a)=1-Rke^{-k(1+a)}>0\), excluding nonnegative real roots too.

If \(h'(E)<0\), necessarily \(R>1/(1-e^{-k})\), so \(F(0)<0\), whereas \(F(a)\to+\infty\) for real \(a\to+\infty\). There is a positive real root and, because the characteristic equation was not multiplied by a zero factor at that root, a genuine exponentially growing mode. If \(h'(E)=0\), \(F(0)=0\) and \(F'(0)=1-k/(e^k-1)>0\), proving simplicity. There is **never** a root \(s=ib\) with \(b\ne0\): for \(R\le0\) the real part of \(F\) is strictly positive, and for \(R>0\) eliminating \(R\) from the real and imaginary parts gives
\[
(kb)(e^k-\cos(kb))=k\sin(kb),
\]
which is impossible since \(e^k-1>k\) and \(|\sin z|\le|z|\). Finally, the initial transport component vanishes after a finite traversal, and standard finite-delay linear renewal theory transfers absence of characteristic roots in the closed right half-plane to exponential stability of the full linearized size-density dynamics. Returning from \(\sigma\) to physical time multiplies local exponents by \(g(E)>0\), leaving their signs unchanged.

**The exact three-branch window.** For \(g(E)=E^2-9E/5+1=(E-9/10)^2+19/100>0\), the closure is \(h(E)=E^3-9E^2/5+E\). Its derivative vanishes only at \((9\pm\sqrt6)/15\), a local maximum and minimum respectively. Their heights are \(21/125\pm4\sqrt6/1125\), yielding exactly the stated flux interval after division by \(J=1-e^{-1}\). At the central flux, the identity
\[
h(E)-21/125=(E-3/5)(E^2-6E/5+7/25)
\]
gives the three exact positive roots and the derivative signs stated above. As \(h(0)=0\), \(h(E)\to+\infty\) and \(h'\) has exactly two zeros, no other stationary roots exist. At the endpoints \(h''\ne0\), so the folds are nondegenerate.

## Verification

The included `verify.py` is an executable independent arithmetic recheck of the exact cubic factorization, critical values, positivity of the speed, root/derivative identities, threshold ordering, and the key inequality \(e^k-1>k\) for sample positive \(k\). It additionally checks representative normalized stationary/characteristic identities. The proof of the universal all-parameter spectral inequality is analytic above and is not replaced by finite testing. Reproducibility: run `python verify.py` with Python 3 and its standard library.

## Relationship to prior work

Wang and Yu (arXiv:2607.03790v1, July 4, 2026), *Optimal Harvesting of Size-Structured Populations with Environmental Feedback and Fixed Recruitment Flux*, introduce and analyze the wider fixed-flux size-structured framework, proving global well-posedness, a stationary scalar closure, generic fold resonance, and harvesting optimality conditions. The stationary-closure reduction and generic folds are established prior work and are **not** claimed as new. The result here adds a solvable natural subclass with constant hazard per size traversed, an exact post-transit renewal relation, a universal spectral sign theorem (including exclusion of imaginary-axis crossings), and an exact dynamically classified three-branch flux interval.

Chu and Magal (2013), *Hopf bifurcation for a size-structured model with resting phase*, examine a distinct nonlocal boundary formulation in which Hopf behavior can occur. General results about distributed-delay stability (for example Bernard, 2009) supply context but do not, in the material accessed, state this specific fixed-flux spectral equivalence or cubic benchmark.

## Limitations

The speed and mortality must have the proportional form \(\mu(E)=\kappa g(E)\). The general fixed-flux model with size-dependent rates and harvesting is not covered. The result concerns local exponential **linear** stability (or a positive real linear instability), not nonlinear global basins; positive real eigenvalues should not be confused with stochastic population establishment. Source-based originality assessment is limited by incomplete access to some older structured-population stability papers. Equal stationary fold eigenvalue zero does not by itself prove a nonlinear saddle-node dynamical normal form. No independent external audit has been performed.

## References

1. L. S. Wang and J. Yu, *Optimal Harvesting of Size-Structured Populations with Environmental Feedback and Fixed Recruitment Flux*, arXiv:2607.03790v1 (first posted 2026-07-04), https://arxiv.org/html/2607.03790.
2. J. Chu and P. Magal, *Hopf bifurcation for a size-structured model with resting phase*, Discrete and Continuous Dynamical Systems 33 (2013), 4891–4921, DOI:10.3934/dcds.2013.33.4891.
3. S. Bernard, *Distributed delays stabilize negative feedback loops*, arXiv:0910.4520 (2009), https://arxiv.org/abs/0910.4520.
