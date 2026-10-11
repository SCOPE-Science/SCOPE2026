# Exact fourth-power norm of the order-five cyclic Hilbert transform
## Finding
Let \(C_5=\mathbb Z/5\mathbb Z\), and normalize
\[
\widehat f(k)=\frac15\sum_{x=0}^4 f(x)e^{-2\pi i kx/5},\qquad
\|f\|_4^4=\frac15\sum_{x=0}^4|f(x)|^4.
\]
On real functions with \(\widehat f(0)=0\), define the cyclic Hilbert transform by
\[
\widehat{Hf}(1)=-i\widehat f(1),\quad
\widehat{Hf}(2)=-i\widehat f(2),\quad
\widehat{Hf}(3)=i\widehat f(3),\quad
\widehat{Hf}(4)=i\widehat f(4),
\]
with \(\widehat{Hf}(0)=0\).

Let \(t_*\) be the unique positive root of
\[
3t^4-12t^2+8t-9=0.
\]
Then
\[
\|H\|_{L^4_0(C_5)\to L^4_0(C_5)}^4
=X_*:=\frac{3t_*^4+4t_*^3+12t_*^2-4t_*+3}
{3t_*^4-4t_*^3+12t_*^2-4t_*+3}.
\]
Equivalently, \(X_*\) is the unique root in \((2.08,2.10)\) of
\[
3185X^4-17948X^3+42750X^2-47500X+15625=0.
\]
Numerically,
\[
t_*=1.8532580986253061869\ldots,\qquad
X_*=2.0896890045699923995\ldots,
\]
and therefore
\[
\boxed{\|H\|_{L^4_0(C_5)\to L^4_0(C_5)}=1.2023209494390236357\ldots}.
\]

Every nonzero extremizer is characterized by
\[
|\widehat f(2)|=t_*|\widehat f(1)|,
\]
and by the two phase conditions
\[
\widehat f(1)^3\widehat f(2)\in(-\infty,0),\qquad
\widehat f(1)\overline{\widehat f(2)}^{\,3}\in(-\infty,0).
\]
Equivalently, modulo nonzero real scaling and cyclic translation there is a single extremizer.

## Assumptions and scope
The theorem is for real-valued, zero-mean functions on the five-point cyclic group and for the sign multiplier displayed above. It does not claim the sharp norm for complex-valued inputs, for other cyclic orders, or for a different finite Hilbert-transform convention.

The order-five case is the first nontrivial odd cyclic case for this question. On \(C_3\), every real zero-mean triple \((x,y,z)\) satisfies
\[
x^4+y^4+z^4=\frac12(x^2+y^2+z^2)^2,
\]
so the \(L^2\)-isometry of the sign multiplier already forces its \(L^4\)-norm to be exactly \(1\).

## Proof
Write
\[
\widehat f(1)=re^{i\alpha},\qquad \widehat f(2)=se^{i\beta},\qquad r,s\ge0.
\]
Real-valuedness gives \(\widehat f(4)=\overline{\widehat f(1)}\) and \(\widehat f(3)=\overline{\widehat f(2)}\). Parseval applied to \(f^2\), whose Fourier coefficients are the cyclic convolution of \(\widehat f\) with itself, gives
\[
\|f\|_4^4=C+8r^3s\cos(3\alpha+\beta)+8rs^3\cos(\alpha-3\beta),
\]
where
\[
C=6r^4+24r^2s^2+6s^4.
\]
The multiplier sends \((\alpha,\beta)\) to \((\alpha-\pi/2,\beta-\pi/2)\). Hence
\[
\|Hf\|_4^4=C+8r^3s\cos(3\alpha+\beta)-8rs^3\cos(\alpha-3\beta).
\]

For \(r,s>0\), put
\[
u=\cos(3\alpha+\beta),\qquad v=\cos(\alpha-3\beta),
\]
and \(A=8r^3s\), \(B=8rs^3\). The linear map
\[
(\alpha,\beta)\longmapsto(3\alpha+\beta,\alpha-3\beta)
\]
has determinant \(-10\), so it is onto the two-torus. Thus \(u\) and \(v\) can be varied independently throughout \([-1,1]\). The fourth-power quotient is
\[
F(u,v)=\frac{C+Au-Bv}{C+Au+Bv}.
\]
For every admissible \(u\), both endpoint denominators are positive because they are fourth moments of nonzero functions. Therefore
\[
\frac{\partial F}{\partial v}=-\frac{2B(C+Au)}{(C+Au+Bv)^2}<0,
\]
so the maximum has \(v=-1\). There,
\[
\frac{\partial F}{\partial u}=-\frac{2AB}{(C+Au-B)^2}<0,
\]
so the maximum also has \(u=-1\). These two equalities are exactly the two negative-real phase conditions in the statement.

With \(t=s/r>0\), cancellation of the common factor \(2r^4\) gives
\[
R(t)=\frac{3t^4+4t^3+12t^2-4t+3}{3t^4-4t^3+12t^2-4t+3}.
\]
A direct differentiation yields
\[
R'(t)=\frac{-8t^2(3t^4-12t^2+8t-9)}{(3t^4-4t^3+12t^2-4t+3)^2}.
\]
Let \(g(t)=3t^4-12t^2+8t-9\). If \(0<t\le1\), then
\[
g(t)\le-9t^2+8t-9<0.
\]
For \(t\ge1\), \(g''(t)=36t^2-24>0\), while \(g'(1)=-4\), \(g(1)=-10\), and \(g(t)\to\infty\). Consequently \(g\) has exactly one positive zero \(t_*>1\); \(R\) increases up to \(t_*\) and decreases afterward. This proves the global maximum.

Eliminating \(t_*\) between \(g(t_*)=0\) and \(X_*=R(t_*)\) gives the displayed quartic for \(X_*\). The phase equations have exactly ten solutions modulo \(2\pi\); five are cyclic translates of one representative and the other five are obtained by multiplying by \(-1\). Hence real scaling and cyclic translation give the complete equality class.

## Verification
The accompanying verifier checks with exact integer polynomial arithmetic that the derivative numerator is
\[
-8t^2(3t^4-12t^2+8t-9),
\]
and that substituting \(X=R(t)\) into the quartic polynomial is divisible by \(g(t)^2\). It isolates the positive root numerically, evaluates the exact formula, compares the moment identities against direct five-point Fourier synthesis on deterministic samples, and checks an explicit extremizer directly. Random tests are regression checks only; the global proof is the analytic argument above.

## Relationship to prior work
De Carli and Samad study discrete Hilbert transforms on \(\ell^p(\mathbb Z)\), their multiplier interpretation, and related operator norms; their first public preprint appeared on 2015-06-10. Their operator acts on the infinite lattice, not on \(C_5\), and their results do not determine this finite quotient norm.

Bañuelos and Kwaśnicki later proved the sharp \(\ell^p(\mathbb Z)\)-norm of the discrete Hilbert transform. Again, the domain and operator are the infinite-lattice problem rather than the finite cyclic sign multiplier.

A public sharp-constant problem for exactly the same cyclic sign-multiplier convention at order \(31\) records only a non-sharp interval and explicitly requires a global certificate. That order-specific problem neither contains nor implies the order-five computation here. Searches over the order-five parameter, the exact critical polynomial, the exact norm polynomial, and the numerical fingerprint did not locate an implication-equivalent result.

## Limitations
No monotonicity in the cyclic order is proved, and no formula for general odd order is asserted. The proof uses the two positive Fourier modes special to \(C_5\); larger orders lead to higher-dimensional phase coupling. The literature search cannot exclude an older equivalent calculation under substantially different finite-signal terminology.

## References
1. L. De Carli and G. S. Samad, “One-parameter groups of operators and discrete Hilbert transforms,” arXiv:1506.03362; Canadian Mathematical Bulletin 59 (2016), 497–507. First public version: 2015-06-10. DOI: 10.4153/CMB-2016-028-7.
2. R. Bañuelos and M. Kwaśnicki, “On the \(\ell^p\)-norm of the discrete Hilbert transform,” arXiv:1709.07427; Duke Mathematical Journal 168 (2019), 471–504. DOI: 10.1215/00127094-2018-0047.
3. “Sharp fourth-power norm of the cyclic Hilbert transform at order 31,” TheoremDB problem P2730, reviewed 2026-08-01.
