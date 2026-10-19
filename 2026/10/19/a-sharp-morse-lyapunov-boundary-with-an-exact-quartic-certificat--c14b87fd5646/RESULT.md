# A sharp Morse–Lyapunov boundary with an exact quartic certificate for a cubic flow

## Finding
For real parameters \(a>0\), \(0\leq b<\omega\), consider the homogeneous planar cubic system, expressed in the complex coordinate \(z=x+iy\),
\[
\dot z=(-a+i\omega)|z|^2z+b\overline z^{\,3}.
\]
Its unique equilibrium is the origin, which is globally asymptotically stable for **every** parameter triple in this region. An explicit strictly decreasing, positive-definite, coercive, quartic polynomial is
\[
P(x,y)=(x^2+y^2)^2-\frac b\omega\operatorname{Im}\bigl((x+iy)^4\bigr),
\qquad
\dot P=-4a(x^2+y^2)P.
\]
Nevertheless, a globally coercive smooth **Morse Lyapunov function** (strictly decreasing away from the origin and with positive-definite Hessian there) exists **if and only if** \(b\leq a\). More strongly, if \(b>a\), no local \(C^2\) strict Lyapunov function with positive-definite Hessian at the origin exists. If \(b\leq a\), the explicit polynomial \(V=x^2+y^2+P\) is a global smooth Morse Lyapunov function.

The smallest total degree of a globally positive-definite *strict polynomial* Lyapunov function is \(2\) when \(b<a\), and \(4\) when \(b\geq a\). Thus the Morse threshold is sharp even though the global stability and the existence of a polynomial strict Lyapunov certificate never change across it. Throughout the family \(Df(0)=0\), so its zero-eigenvalue linearization is semisimple.

## Assumptions and scope
The state space is the whole real plane. The parameter restrictions are \(a>0\), \(0\leq b<\omega\) (in particular \(\omega>0\)). This is the canonical real-phase normal form for fourfold-equivariant homogeneous planar cubics: the only cubic complex monomials covariant under \(z\mapsto iz\) are \(z^2\overline z\) and \(\overline z^{\,3}\), and a constant coordinate rotation makes the latter coefficient real nonnegative. The condition \(\omega>b\) makes the angular velocity positive at every nonzero point. Set \(r=|z|\). By a global smooth Morse Lyapunov function we mean a proper, positive-definite \(C^\infty\) function that vanishes only at the origin, has strictly negative Lie derivative at every nonzero point, and has positive-definite Hessian at the origin. A local Morse obstruction requires only \(C^2\) regularity, a local minimum at the origin, a positive-definite Hessian there, and strict decay in a punctured neighborhood. A strict polynomial Lyapunov function is globally positive definite and has strictly negative Lie derivative away from the origin; degree is its total polynomial degree.

## Proof
**1. Exact quartic identity and stability.** For \(z=re^{i\theta}\), direct separation of real and imaginary parts gives
\[
\dot r=r^3(-a+b\cos4\theta),\qquad
\dot\theta=r^2(\omega-b\sin4\theta).
\]
Set \(k=b/\omega\in[0,1)\). The displayed polynomial has polar form \(P=r^4(1-k\sin4\theta)\). Consequently
\[
(1-k)r^4\leq P\leq(1+k)r^4,
\]
and differentiation yields
\[
\begin{aligned}
\dot P
&=4r^6\bigl[(-a+b\cos4\theta)(1-k\sin4\theta)
-k\cos4\theta(\omega-b\sin4\theta)\bigr]\\
&=-4ar^6(1-k\sin4\theta)=-4ar^2P.
\end{aligned}
\]
Hence \(P\) is proper, positive definite, and strictly decreasing at every nonzero point, implying uniqueness of the equilibrium and forward completeness. Its sublevel sets are compact, and its derivative is negative on every punctured sublevel set, proving global Lyapunov stability and attraction. Quantitatively, because \(r^2\geq\sqrt{P/(1+k)}\), integration gives
\[
P(t)\leq\left(P(0)^{-1/2}+\frac{2at}{\sqrt{1+k}}\right)^{-2}
\]
for every nonzero initial state and \(t\geq0\), establishing convergence directly.

**2. Morse certificate on and below the boundary.** Since
\[
\frac{d}{dt}r^2=2r^4(-a+b\cos4\theta)\leq0
\]
when \(b\leq a\), the polynomial \(V=r^2+P\) is proper and positive definite, and its Lie derivative is strictly negative for every \(r>0\) by the quartic identity. Its Hessian at zero is \(2I_2\), since \(P\) has homogeneous degree four; thus \(V\) is a smooth global Morse Lyapunov function. When \(b<a\), the degree-two polynomial \(r^2\) is already strictly decreasing.

**3. The Morse obstruction above the boundary.** Write \(f:\mathbb R^2\to\mathbb R^2\) for the cubic vector field, and let \(R\) denote the rotation \((x,y)\mapsto(-y,x)\). It has the exact equivariance \(f(Ru)=Rf(u)\). Suppose \(b>a\) and a local \(C^2\) strict Morse Lyapunov function \(W\) exists. Put \(H=D^2W(0)\succ0\). Taylor's theorem and homogeneity give, for each unit vector \(u\),
\[
\nabla W(ru)\cdot f(ru)
=r^4\bigl(u^{\mathsf T}Hf(u)+o(1)\bigr)<0
\quad(r\downarrow0),
\]
therefore \(u^{\mathsf T}Hf(u)\leq0\). Apply the last inequality to the four directions \(u,Ru,R^2u,R^3u\) and average. Since
\[
\frac14\sum_{j=0}^3(R^j)^{\mathsf T}HR^j
=\frac{\operatorname{tr}H}{2}I_2,
\]
we obtain
\[
\frac{\operatorname{tr}H}{2}\,u\cdot f(u)\leq0.
\]
The trace is positive. Choosing \(u=(1,0)\) gives \(u\cdot f(u)=b-a>0\), a contradiction. The argument excludes *every* local \(C^2\) strict Morse candidate, not just quadratic or polynomial ones.

**4. Minimal polynomial degree.** A globally positive-definite polynomial vanishing at the origin cannot have odd total degree: its leading odd homogeneous term takes both signs on opposite rays. Degree one is likewise impossible. Any positive-definite degree-two polynomial has the form \(Q(u)=u^{\mathsf T}Hu\) with \(H\succ0\). If \(\dot Q<0\) globally, the same fourfold averaging at \(u=(1,0)\) gives \(b-a<0\), since now each summand is *strictly* negative without taking a limit. Conversely, \(Q=r^2\) is strict for \(b<a\). For \(b\geq a\), degrees below four are excluded, while \(P\) provides degree four. This proves the claimed minimum.

## Verification
The standalone file `check.py` symbolically expands the real polynomial vector field, verifies \(\mathcal L_f(\omega P)=-4ar^2(\omega P)\) as an identity in all coordinates and parameters, verifies the radial identity and fourfold equivariance, and performs \(600\) exact rational checks of positivity, strict descent, and the boundary Morse construction. The checker ran successfully with Python 3 and SymPy. These finite checks corroborate, but do not replace, the all-parameter algebraic proof and fourfold Hessian argument.

## Relationship to prior work
Jongeneel's 2026 study proves that global asymptotic stability need not admit a Morse Lyapunov function and provides a semisimplicity *necessary* condition on a center linearization; its explicit non-Morse polynomial example has a nonzero nilpotent linear part. The present all-cubic system has the diagonalizable zero linearization and a globally strict *polynomial* quartic certificate, yet exhibits a sharp Morse nonexistence region. Thus the non-Morse conclusion here is not a corollary of Jongeneel's nilpotent obstruction.

Liu and Fitzsimmons (2026) give a different homogeneous cubic family with angular harmonic \(\cos2\theta\) and show that some of its stable members have **no** polynomial Lyapunov certificate of any degree. Their exhibited system has \(\dot\theta=r^2\) and differs from the fourfold-equivariant field here, for which the positive quartic certificate exists throughout the stated parameter range. Their results do not determine this sharp Morse existence boundary or minimum polynomial degree. A previously published construction comparing two flat-time-scaled systems with identical Taylor jets concerns smooth nonpolynomial vector fields; it does not cover the polynomial family and parameter threshold here. General rational Lyapunov existence for stable homogeneous systems does not decide Morse existence.

## Limitations
The statements apply only to this three-parameter, fourfold-equivariant cubic family with \(0\leq b<\omega\) and \(a>0\). They do not classify all planar cubic fields, other symmetry classes, or the regime \(\omega\leq b\). The local nonexistence claim applies to \(C^2\) functions with positive-definite Hessian, not to all strict smooth Lyapunov functions; indeed \(P\) itself is smooth and strict but degenerate at the equilibrium. The literature comparison gives best-knowledge originality, not proof of priority or independent verification.

## References
1. W. Jongeneel, *On global Lyapunov functions being Morse*, arXiv:2610.05626v1, submitted 2026-10-04, especially Proposition 3.5 and Corollary 3.9. https://arxiv.org/abs/2610.05626
2. J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171v1, submitted 2026-07-17, especially Theorem II.2 and Section IV.D. https://arxiv.org/abs/2607.16171
3. A. A. Ahmadi and B. El Khadir, *On Algebraic Proofs of Stability for Homogeneous Vector Fields*, arXiv:1803.01877, first posted 2018, for the general rational converse. https://arxiv.org/abs/1803.01877
