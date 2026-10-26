# Sharp reentrant arrival-direction bounds for finite-site Brownian resetting on a circle

## Finding

For Brownian motion on an absorbing circle, resetting to a finite set of spatial sites can reverse which direction of approach to the target is more probable multiple times as the reset rate increases. The sharp number of such reversals equals at most one less than the number of distinct *effective antipodal distances* represented in the resetting law. Every number permitted by the bound is realizable, and every prescribed finite increasing sequence of critical positive reset rates is realizable with the minimal corresponding number of sites.

More precisely, suppose there are \(m\geq1\) distinct offsets \(0<a_1<\cdots<a_m<L/2\) with nonzero signed left-minus-right resetting weights \(c_j\), after combining all sites symmetric around the antipode and discarding cancellations. If \(P_0(r)\) and \(P_L(r)\) denote the probabilities of first approaching the absorbing target from the two respective sides, then for all \(r>0\),
\[
\operatorname{sgn}(P_0(r)-P_L(r))
=\operatorname{sgn}\!\left(\sum_{j=1}^{m}c_j\sinh(a_j\sqrt{r/D})\right).
\]
There are at most \(m-1\) distinct positive resetting rates satisfying \(P_0(r)=P_L(r)\), unless these two probabilities agree for every resetting rate. The upper bound is sharp. In particular, a three-site law gives exactly two reversals, whereas one or two effective offsets cannot.

An explicit three-site example uses circle circumference \(L=8d\), the resetting sites \(3d,6d,d\) with respective probabilities \(25/36,10/36,1/36\), and any \(D,d>0\). The only two positive ties occur at
\[
r_1=\frac{D}{d^2}\operatorname{arcosh}(2)^2,\qquad
r_2=\frac{D}{d^2}\operatorname{arcosh}(3)^2.
\]
The more probable approach side is respectively \(0\), \(L\), and \(0\) on the intervals \((0,r_1)\), \((r_1,r_2)\), and \((r_2,\infty)\).

## Assumptions and scope

Take a geometric circle of circumference \(L>0\) with one absorbing target marked at its identified endpoints \(0\sim L\). Until absorption, the angular coordinate evolves as a one-dimensional Brownian motion with generator \(D\partial_{xx}\), where \(D>0\). A homogeneous independent Poisson clock of rate \(r>0\) relocates the particle instantaneously to a new independent site drawn from a fixed finite discrete distribution
\[
\rho=\sum_{i=1}^{M}w_i\delta_{x_i},\qquad 0<x_i<L,\quad w_i>0,\quad\sum_{i=1}^{M}w_i=1.
\]
The starting site is independently drawn from that same distribution. The target terminates the experiment at its first hit. A first hit at the left endpoint of the unwrapped interval is called approach from side \(0\); a first hit at the right endpoint is approach from side \(L\). This is a directional/approach-side observable, *not* a probability of hitting either of two physically different targets.

For every represented distance \(a\in(0,L/2)\), set the signed weight
\[
c(a)=\rho(\{L/2-a\})-\rho(\{L/2+a\}),
\]
interpreting absent atoms as zero. Atoms at the midpoint contribute zero. Combine sites sharing an offset and retain only those with \(c(a)\neq0\); list their offsets as \(a_1<\cdots<a_m\) and let \(c_j=c(a_j)\). When no offsets survive, the approach probabilities are both \(1/2\) at every reset rate and the finite-zero claim is inapplicable.

## Proof

**1. Renewal expression for the approach probabilities.** Put \(k=\sqrt{r/D}>0\) and let \(\tau\) be the exit time of an unreset Brownian excursion from \((0,L)\). For a starting point \(x\), the discounted left-exit and right-exit probabilities solve the backward boundary-value equations \(Du''=ru\). Their respective boundary conditions give
\[
u_0(x;k)=\mathbb E_x[e^{-r\tau}\mathbf 1_{\{X_\tau=0\}}]
=\frac{\sinh(k(L-x))}{\sinh(kL)},\qquad
u_L(x;k)=\mathbb E_x[e^{-r\tau}\mathbf 1_{\{X_\tau=L\}}]
=\frac{\sinh(kx)}{\sinh(kL)}.
\]
(The notation \(X_\tau=0\) and \(X_\tau=L\) refers to the unwrapped interval.) Each attempt starts with the same law \(\rho\), terminates at absorption or at an independent reset, and is conditionally independent of earlier attempts. Write \(U_s(k)=\int u_s(x;k)\,d\rho(x)\) for \(s=0,L\). Each attempt has left-exit probability \(U_0\), right-exit probability \(U_L\), and reset-before-exit probability \(1-U_0-U_L\). The geometric sum therefore gives
\[
P_0(r)=\frac{U_0(k)}{U_0(k)+U_L(k)},\qquad
P_L(r)=\frac{U_L(k)}{U_0(k)+U_L(k)}.
\]
In particular, \(U_0+U_L>0\), and both the probability normalization and the sign of their difference are exact.

**2. Reduction to an odd exponential sum.** The identity
\[
\sinh(k(L-x))-\sinh(kx)=2\cosh(kL/2)\sinh(k(L/2-x))
\]
gives
\[
U_0(k)-U_L(k)=\frac{2\cosh(kL/2)}{\sinh(kL)}
\sum_{j=1}^{m}c_j\sinh(ka_j).
\]
The prefactor and renewal denominator are strictly positive; therefore the directional excess has the claimed sign and zeros.

**3. Strict positivity of the hyperbolic-sine determinant.** For any integer \(n\geq1\), any strictly increasing positive \(k_1<\cdots<k_n\) and \(a_1<\cdots<a_n\),
\[
\det[\sinh(k_i a_j)]_{i,j=1}^{n}>0.
\]
Indeed, expand \(\sinh(ka)=\sum_{q\geq0}(ka)^{2q+1}/(2q+1)!\), apply Cauchy--Binet to each finite truncation of this expansion, and then take the absolutely convergent limit. Every nonzero summand has the form
\[
\frac{\det[k_i^{2q_\ell+1}]_{i,\ell}\;\det[a_j^{2q_\ell+1}]_{j,\ell}}
{\prod_{\ell=1}^{n}(2q_\ell+1)!},\qquad 0\leq q_1<\cdots<q_n.
\]
The two generalized Vandermonde determinants are strictly positive for ordered positive arguments and ordered exponents; already the term with \(q_\ell=\ell-1\) is positive. No cancellation is possible. Absolute convergence justifies the limit.

**4. Optimal zero count.** If \(F(k)=\sum_{j=1}^{m}c_j\sinh(ka_j)\) has \(m\) distinct positive zeros \(k_1<\cdots<k_m\), the vector \((c_1,\ldots,c_m)\) is annihilated by the invertible matrix \([\sinh(k_i a_j)]\). This would force every \(c_j\) to vanish, contrary to the definition of the active offsets. Therefore at most \(m-1\) positive zeros are possible, irrespective of their multiplicities. Since every actual sign reversal must be such a zero, the same upper bound applies to reversals.

**5. Sharpness at any prescribed rates.** Fix arbitrary distinct positive \(k_1<\cdots<k_{m-1}\) and any \(m\) distinct offsets \(0<a_1<\cdots<a_m<L/2\). Form the \((m-1)\)-by-\(m\) matrix \(A_{ij}=\sinh(k_i a_j)\), and let
\[
c_j=(-1)^{m+j}\det A_{\widehat j},
\]
where \(A_{\widehat j}\) removes column \(j\). Each minor is strictly positive by Step 3. Hence every \(c_j\neq0\), they alternate in sign, and the cofactor identity gives \(\sum_jc_j\sinh(k_i a_j)=0\) for every selected \(k_i\). For any other positive \(k\), this sum is exactly the determinant of the matrix obtained by appending the row \((\sinh(ka_j))_j\) to \(A\). Moving this variable row to its increasing-\(k\) position changes the determinant sign by one at each chosen \(k_i\); the sorted determinant is always positive by Step 3. Hence these \(m-1\) zeros are all sign-changing and, by Step 4, are the only positive zeros.

Set \(Z=\sum_j|c_j|\). Make the physical reset distribution consist of exactly one atom of mass \(|c_j|/Z\) at \(L/2-a_j\) when \(c_j>0\), or at \(L/2+a_j\) when \(c_j<0\). This realizes the same signed sum up to a positive multiple, using exactly \(m\) resetting sites. The desired transition rates are \(r_i=Dk_i^2\). The result includes \(m=1\), for which a single effective offset has no positive tie.

**6. Minimal explicit double reversal.** Set \(L=8d\) and use the three weighted sites of the Finding. Their offsets and signed weights are \((d,25/36)\), \((2d,-10/36)\), and \((3d,1/36)\). Writing \(z=kd\), the directional numerator simplifies *exactly* to
\[
F(k)=\frac{25\sinh z-10\sinh(2z)+\sinh(3z)}{36}
=\frac{\sinh z}{9}(\cosh z-2)(\cosh z-3).
\]
Since \(z>0\), the only zeros occur at \(\cosh z=2\) and \(\cosh z=3\). The two factors change sign at those two distinct levels, giving the stated positive/negative/positive sequence. The general zero bound establishes that three active offsets (and hence at least three sites) are necessary for two reversals.

## Verification

The standalone file `verify.py` checks the exact factorization, the full renewal normalization, both critical rates and the three sign regions using high-precision arithmetic. It also checks positivity of sample hyperbolic-sine minors and verifies the cofactor constructions for \(2\leq m\leq6\). Running `python verify.py` with `mpmath` and `sympy` installed reports **176 passed deterministic checks**. These tests do not prove total positivity in all dimensions, nor do they establish the zero bound; Steps 3--5 do so analytically.

## Relationship to prior work

Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (arXiv:2605.08414v1) derive a renewal framework for first-passage *times* on a resetting circle and study optimizers and their phase transitions. Its transform and model are inputs, not the novelty claimed here. The present theorem instead classifies the **approach side of the first target hit** and its number of reversals with reset intensity.

Pal and Prasad (arXiv:1812.03009) previously derived interval splitting probabilities under single-site resetting; this supplies the first-passage precedent but cannot produce a two-reversal three-site law.

Vega Coso (arXiv:2605.00657v1) obtains splitting probabilities and spectral neutrality for multi-site *discrete-time biased* resetting random walks, including rate-independent neutral distributions. The inspected full text (especially Sections 4--6 and its conclusion) neither states nor bounds the number of directional side reversals in continuous-time Brownian resetting. The related midpoint-invariance paper (arXiv:2603.24803v2, including Appendix B) concerns fixed or neutral approach ratios. Later works arXiv:2607.10717v1 and arXiv:2608.15805v1 investigate geometric separatrices and rotating response orientations. Only their accessible abstracts were reviewed, so possible broader implicit consequences remain an originality risk. The analytic fact that the \(\sinh\) kernel is strictly totally positive follows from classical positive-kernel theory and is not itself claimed as new.

## Limitations

This theorem assumes unbiased Brownian diffusion on a circle, complete independent Poisson resetting, a fixed discrete reset law, a single absorbing target and an initial draw from the reset law. It concerns which *side* reaches that same target, not multiple distinct targets or optimized mean arrival time. A separate initial distribution creates a different first-attempt term. The finite-support zero count does not impose a finite reversal bound for arbitrary continuous resetting densities, nor does it transfer automatically to drifted diffusion, non-Poisson clocks or biased lattice walks. Accessible comparison literature does not eliminate all possible implicit coverage by more general spectral-response theorems. No independent audit has been performed.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1 (first posted 2026-05-08), https://arxiv.org/html/2605.08414v1 .
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009, https://arxiv.org/pdf/1812.03009 .
3. J. A. Vega Coso, *Spectral Duality and Reset-Neutral Distributions in Random Walks with Multi-Site Geometric Resetting*, arXiv:2605.00657v1, https://arxiv.org/pdf/2605.00657 .
4. J. A. Vega Coso, *Channel Duality and Midpoint Invariance in Random Walks with Resetting*, arXiv:2603.24803v2, https://arxiv.org/pdf/2603.24803 .
5. J. A. Vega Coso, *Separatrix structure and the geometry of reset distributions*, arXiv:2607.10717v1, https://arxiv.org/abs/2607.10717 (abstract examined; full text unavailable in the comparison).
6. J. A. Vega Coso, *Spectral duality structures and the Fisher–Rao geometry of reset distributions*, arXiv:2608.15805v1, https://arxiv.org/abs/2608.15805 (abstract examined; full text unavailable in the comparison).
