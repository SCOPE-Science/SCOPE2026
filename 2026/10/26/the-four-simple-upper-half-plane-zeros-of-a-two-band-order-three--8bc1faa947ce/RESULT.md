# The four simple upper-half-plane zeros of a two-band order-three Cauchy wavelet

## Finding
For all real \(0<a<b\), put \(E=[-b,-a]\cup[a,b]\). The holomorphic order-three Cauchy-wavelet signal
\[
F_{a,b}(z)=\int_E\frac{dx}{(z-x)^4},\qquad \operatorname{Im}z>0,
\]
has **exactly four simple zeros in the open upper half-plane**. Two are on the positive imaginary axis. The remaining two have nonzero, opposite real parts and equal positive imaginary parts. The four-zero geometry is unchanged for every \(a/b\in(0,1)\), without genericity assumptions. Multiplication by the usual nonzero order-three wavelet normalization does not alter the zeros.

## Assumptions and scope
The two bands have equal height and common half-width \((b-a)/2\), with central gap \((-a,a)\). Real parameters obey \(0<a<b\). Zeros are analytic zeros in \(\operatorname{Im}z>0\), counted with multiplicity only where explicitly stated. Real-axis values at the four endpoints are excluded. Let \(\rho=a/b\in(0,1)\) and \(w=z/b\); then \(F_{a,b}(bw)=b^{-3}F_{\rho,1}(w)\).

## Proof
Elementary endpoint integration gives
\[
F_{\rho,1}(w)=\frac13\left[(w+\rho)^{-3}-(w+1)^{-3}+(w-1)^{-3}-(w-\rho)^{-3}\right].
\]
With \(y=w^2\), a common denominator yields
\[
F_{\rho,1}(w)=\frac{2(1-\rho)P_\rho(w^2)}{3(w^2-\rho^2)^3(w^2-1)^3}.
\]
Here
\[
P_\rho(y)=3y^4+(\rho^2+10\rho+1)y^3-(9\rho^3+12\rho^2+9\rho)y^2
+3\rho(\rho^4+\rho^3+\rho+1)y+\rho^3(\rho^2+\rho+1).
\]
Since \(0<\rho<1\), the prefactor is nonzero, and the denominator has no zeros in the open upper half-plane. Consequently the upper-half-plane zeros come precisely from the roots of \(P_\rho(w^2)\).

Direct expansion of the quartic resultant \(\operatorname{Res}_y(P_\rho,\partial_y P_\rho)\), with the standard quartic discriminant convention, gives
\[
\operatorname{disc}_y(P_\rho)=-108\rho^3(1-\rho)^2(1+\rho)^6Q(\rho),
\]
where
\[
Q(\rho)=\rho^{10}+326\rho^9+669\rho^8+1448\rho^7+3682\rho^6+6180\rho^5
+3682\rho^4+1448\rho^3+669\rho^2+326\rho+1.
\]
Every coefficient of \(Q\) is positive, hence the discriminant is strictly negative for \(0<\rho<1\). A real quartic with negative nonzero discriminant has exactly two distinct real roots and one distinct nonreal conjugate pair.

To locate the real roots, observe the exact identities
\[
P_\rho(0)=\rho^3(\rho^2+\rho+1)>0,\qquad
P_\rho(-\rho)=-3\rho^2(1+\rho)^4<0,
\]
and \(P_\rho(y)\to+\infty\) as \(y\to-\infty\). Hence there is a root in \(( -\infty,-\rho)\) and another in \((-\rho,0)\). The discriminant count proves these are the only real roots and are simple.

Each negative root \(y=-s\) gives \(w=\pm i\sqrt s\), exactly one zero in the open upper half-plane. Each of the two nonreal conjugate roots gives two square roots, exactly one of which lies in the open upper half-plane; these upper roots are \(u+iv\) and \(-u+iv\) with \(u,v>0\). Since \(P_\rho(0)>0\) and its roots are simple, all corresponding square roots are simple. Scaling \(w\mapsto z=bw\) preserves the conclusion for arbitrary \(0<a<b\).

## Verification
The accompanying Python/SymPy checker re-derives the rational identity, quartic discriminant factorization, and both sign identities from exact symbolic arithmetic, and computes representative zero sets at multiple rational gap ratios. It also compares the analytic endpoint expression to direct numerical integration at sample points in the upper half-plane. The infinite-parameter theorem follows from the explicit algebra and sign arguments above, not from finite samples.

## Relationship to prior work
Mallat and Waldspurger's 2014 paper develops the analytic Cauchy-wavelet transform and the connection between upper-half-plane zeros and phase retrieval, but does not establish the four-zero, two-imaginary/two-off-axis census for this two-band step signal. Standard pole expansions and quartic-discriminant facts are used as tools, not asserted as new. A previously studied four-atom Cauchy-wavelet family concerns point masses rather than a two-interval density and does not imply this classification. The result supplies a concrete full analytic zero geometry for the elementary disconnected two-band signal in the wavelet setting.

## Limitations
Only equal-height, symmetric, two-interval densities and the exact fourth-power Cauchy kernel are treated. Other orders, unequal amplitudes, and nonsymmetric support are not classified. The theorem describes analytic zeros, not global phase-retrieval conditioning; the connection to potential phase instability is contextual, not a claimed stability bound. Novelty is based on inspected and indexed material, not independent publication-priority certification.

## References
Mallat, S. and Waldspurger, I. (2014). *Phase retrieval for the Cauchy wavelet transform*, arXiv:1404.1183v1 (first posted 2014-04-04), https://arxiv.org/abs/1404.1183.
