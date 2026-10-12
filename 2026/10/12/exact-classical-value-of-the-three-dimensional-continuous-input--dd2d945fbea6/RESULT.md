# Exact classical value of the three-dimensional continuous-input sign game
## Finding
For the third continuous-input game introduced by Aharon, Machnes, Reznik, Silman, and Vaidman, let the inputs be independent uniform directions \(x,y\in\mathbb S^2\). Outside the measure-zero set where \(x\cdot y=0\), the verifier requires the product of the binary outputs to be
\[
-\operatorname{{sgn}}(x\cdot y).
\]
Among all classical strategies, including arbitrary measurable local response functions and shared randomness, the exact optimal winning probability is
\[
P_{{\mathrm{{cl}}}}^*=1-\frac1\pi.
\]
The hemispherical strategy described in the source attains this value. The source's singlet strategy has winning probability \(3/4\), so the game has the exact certified quantum advantage
\[
\frac34-\left(1-\frac1\pi\right)=\frac1\pi-\frac14>0.
\]
This resolves the source's conjectured quantum advantage and its stated likelihood that the hemispherical classical strategy is optimal. No claim is made here that \(3/4\) is the globally optimal quantum value.

## Assumptions and scope
Let \(\sigma\) be normalized rotation-invariant surface measure on \(\mathbb S^2\). A deterministic classical strategy is a pair of measurable maps \(a,b:\mathbb S^2\to\{{-1,+1}}\). Shared-randomness strategies are convex mixtures of deterministic strategies, so an upper bound for every deterministic pair is also an upper bound for every classical strategy.

Write
\[
K(x,y)=\operatorname{{sgn}}(x\cdot y).
\]
Changing \(K\) on the orthogonality set does not change any integral. The classical winning probability is
\[
P_{{\mathrm{{win}}}}(a,b)=\frac12+\frac12 B(a,b),
\qquad
B(a,b)=-\iint K(x,y)a(x)b(y)\,d\sigma(x)d\sigma(y).
\]
The claim concerns this exact game with independent isotropic inputs. It does not impose antipodality on the response functions.

## Proof
Fix \(a\) and define its hemisphere transform
\[
h_a(y)=\int_{{\mathbb S^2}}K(x,y)a(x)\,d\sigma(x).
\]
For this fixed \(a\), optimizing pointwise over \(b\) gives
\[
\sup_b B(a,b)=\int_{{\mathbb S^2}}|h_a(y)|\,d\sigma(y).
\]
Thus it is enough to prove a sharp uniform bound on the last integral.

First, \(h_a\) is odd. If \(d(y,z)=\delta\) is geodesic distance, then the two sign functions \(K(\cdot,y)\) and \(K(\cdot,z)\) differ on two spherical lunes of total normalized area \(\delta/\pi\). Hence
\[
|h_a(y)-h_a(z)|
\le \int |K(x,y)-K(x,z)|\,d\sigma(x)
=\frac{2\delta}{\pi}.
\]
Therefore every \(h_a\) is geodesically Lipschitz with constant \(L=2/\pi\).

We use the following sharp consequence of Lévy's spherical isoperimetric inequality. If \(h:\mathbb S^2\to\mathbb R\) is odd and \(L\)-Lipschitz, then
\[
\int |h|\,d\sigma\le L\left(\frac\pi2-1\right).
\]
To prove it, for \(t>0\) set \(A_t=\{{h>t}}\). Oddness and Lipschitz continuity imply that \(A_t\) and \(-A_t\) are separated by geodesic distance at least \(2t/L\). For any \(\varepsilon<2t/L\), the \(\varepsilon\)-neighborhood of \(A_t\) is disjoint from \(-A_t\). If a spherical cap of radius \(r\le\pi/2\) has the same measure as \(A_t\), Lévy isoperimetry says that its \(\varepsilon\)-neighborhood has no larger measure than the corresponding neighborhood of \(A_t\). Sending \(\varepsilon\uparrow2t/L\) yields
\[
\frac{1-\cos(r+2t/L)}2+\frac{1-\cos r}2\le1.
\]
Equivalently, \(r\le\pi/2-t/L\), and therefore
\[
\sigma(A_t)\le\frac{1-\sin(t/L)}2
\qquad
\left(0\le t\le\frac{L\pi}{2}\right).
\]
Oddness also gives \(\sigma(|h|>t)=2\sigma(A_t)\), and \(|h|\le L\pi/2\). The layer-cake formula now gives
\[
\int |h|\,d\sigma
\le\int_0^{{L\pi/2}}\left(1-\sin(t/L)\right)dt
=L\left(\frac\pi2-1\right).
\]
With \(L=2/\pi\), every classical bias satisfies
\[
B(a,b)\le1-\frac2\pi,
\]
so every classical winning probability is at most \(1-1/\pi\).

The bound is attained. Fix a unit vector \(u\) and take
\[
a_u(x)=\operatorname{{sgn}}(u\cdot x),
\qquad
b_u(y)=-\operatorname{{sgn}}(u\cdot y).
\]
If \(\theta=d(u,y)\), then the same spherical-lune calculation gives
\[
h_{{a_u}}(y)=1-\frac{2\theta}{\pi}.
\]
Its sign is \(\operatorname{{sgn}}(u\cdot y)\), so the displayed \(b_u\) is pointwise optimal, and direct integration gives bias \(1-2/\pi\). Hence \(P_{{\mathrm{{cl}}}}^*=1-1/\pi\).

For the singlet strategy with measurement axes equal to the two input directions, the outcome-product expectation conditioned on \(x,y\) is \(-x\cdot y\). Its conditional winning probability is therefore \((1+|x\cdot y|)/2\). For independent uniform directions, \(x\cdot y\) is uniform on \([-1,1]\), so \(\mathbb E|x\cdot y|=1/2\) and the winning probability is exactly \(3/4\). This proves the stated positive gap.

## Verification
The proof is analytic and dimension-specific to \(\mathbb S^2\). The critical external lemma is Lévy's spherical isoperimetric theorem in its neighborhood form: spherical caps minimize the measure of metric neighborhoods among sets of fixed spherical measure. This form is stated, for example, in Keith Ball's exposition *An Elementary Introduction to Modern Convex Geometry*.

The packaged script `verify.py` was executed from its package path. It checks the algebraic identities for the classical bias, classical value, singlet value, and gap; performs a high-resolution quadrature of the hemispherical transform; and runs a fixed-seed Monte Carlo stress test of the two displayed strategies. It returned `VERIFY_OK`. These finite checks are regression tests only and are not used as a proof of optimality.

## Relationship to prior work
Aharon et al. define the three-dimensional game, compute the hemispherical classical value \(1-1/\pi\), and state that this strategy appears likely to be optimal. They give the singlet strategy with value \(3/4\), while reporting only numerical evidence for quantum optimality. Their abstract explicitly leaves quantum advantage for the third game as a conjecture.

Kent and Pitalúa-García later study Bloch-sphere colourings at a *fixed angular separation* and formulate hemispherical-colouring maximality hypotheses. Their setup also imposes the antipodal response relation natural for spin-axis colourings. The present game instead averages over independent directions with the sign of the inner product as the target and allows arbitrary classical response functions. Their fixed-angle bounds and hypotheses therefore do not imply the exact integrated classical value proved here.

Targeted source-title, exact-constant, hemisphere-transform, fixed-angle-colouring, and implication searches located no publication stating this exact classical optimum for the Aharon et al. third game. Previously recorded scientific findings were compared at claim and implication level and do not cover this game or bound.

## Limitations
The result proves the classical optimum and thereby certifies a strict quantum advantage using the displayed singlet strategy. It does not prove that \(3/4\) is the optimal quantum value. It also does not claim a new proof of the general spherical isoperimetric theorem; that theorem is used as a standard geometric input. An obscure or poorly indexed later proof of the same game value remains a residual bibliographic risk.

## References
1. N. Aharon, S. Machnes, B. Reznik, J. Silman, and L. Vaidman, *Continuous input nonlocal games*, arXiv:0706.2159; Natural Computing 12 (2013), 5--8, DOI 10.1007/s11047-012-9354-5.
2. A. Kent and D. Pitalúa-García, *Bloch sphere colourings and Bell inequalities*, arXiv:1307.6839; Physical Review A 90, 062124 (2014), DOI 10.1103/PhysRevA.90.062124.
3. K. Ball, *An Elementary Introduction to Modern Convex Geometry*, in *Flavors of Geometry*, MSRI Publications 31, Cambridge University Press (1997), discussion of Lévy's spherical isoperimetric inequality.
