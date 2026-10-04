# Fixed-perimeter Gaussian torsion has a negative centrally symmetric Hessian at the disk
## Finding
Let \(d\gamma=(2\pi)^{-1}e^{-|x|^2/2}\,dx\) in the plane and let \(T_\gamma(K)=\int_K u\,d\gamma\), where
\[
(\Delta-x\cdot\nabla)u=-1\quad\text{in }K,\qquad u=0\quad\text{on }\partial K.
\]
For every nonzero smooth \(2\pi\)-periodic function \(f\) satisfying central symmetry \(f(\theta+\pi)=f(\theta)\) and zero mean
\[
\int_0^{2\pi}f(\theta)\,d\theta=0,
\]
define, for sufficiently small \(|\varepsilon|\), the convex body \(K_\varepsilon\) by the support function
\[
h_\varepsilon(\theta)=1+\varepsilon f(\theta).
\]
If
\[
f(\theta)=\sum_{\substack{k\ge2\\ k\ \mathrm{even}}}(a_k\cos k\theta+b_k\sin k\theta),
\]
then \(\operatorname{Per}(K_\varepsilon)=2\pi\) exactly and
\[
\left.\frac{d^2}{d\varepsilon^2}T_\gamma(K_\varepsilon)\right|_{\varepsilon=0}
=\frac{\sqrt e-1}{2\sqrt e}\sum_{\substack{k\ge2\\ k\ \mathrm{even}}}\left[2-(\sqrt e-1)(k^2+2\lambda_k)\right](a_k^2+b_k^2),
\]
where \(\lambda_k=F_k'(1)\) and
\[
F_k(r)=\frac{r^k\,{}_1F_1(k/2;k+1;r^2/2)}{{}_1F_1(k/2;k+1;1/2)}.
\]
Every summand is strictly negative. Hence the unit disk is strictly second-order stable in every nontrivial smooth centrally symmetric Euclidean-perimeter-preserving support direction for Gaussian torsional rigidity.

## Assumptions and scope
The perturbation is a smooth support-function path about the unit disk. For sufficiently small \(|\varepsilon|\), convexity follows from
\[
h_\varepsilon+h_\varepsilon''=1+\varepsilon(f+f'')>0.
\]
Central symmetry is imposed because the lead source explicitly leaves open the fixed-perimeter maximization problem for centrally symmetric planar convex bodies. The zero-mean condition makes Euclidean perimeter constant because Cauchy's support-function formula gives
\[
\operatorname{Per}(K_\varepsilon)=\int_0^{2\pi}h_\varepsilon(\theta)\,d\theta=2\pi.
\]
The result is a second-directional-variation theorem at the disk, not a global fixed-perimeter inequality and not a neighborhood theorem in a specified Banach norm.

## Proof
Write \(A=\sqrt e-1\). For the unit disk, the radial Gaussian torsion function \(u_0\) satisfies the explicit derivative formulas from the lead source,
\[
u_0'(r)=-\frac{e^{r^2/2}-1}r,
\qquad
u_0''(1)=-1.
\]
Thus
\[
a:=u_0'(1)=-A,\qquad b:=u_0''(1)=-1.
\]
Also
\[
G:=\gamma(B_1)=1-e^{-1/2}=\frac{A}{\sqrt e},
\qquad
w:=e^{-1/2}=\frac1{\sqrt e}.
\]

A boundary point written in outer-normal angle \(\phi\) is
\[
x_\varepsilon(\phi)=h_\varepsilon(\phi)n(\phi)+h_\varepsilon'(\phi)t(\phi).
\]
Converting to polar angle \(\theta\) gives the radial graph expansion
\[
\rho_\varepsilon(\theta)
=1+\varepsilon f(\theta)-\frac{\varepsilon^2}{2}f'(\theta)^2+O(\varepsilon^3)
\]
in every fixed smooth norm controlled by finitely many derivatives of \(f\).

For a fixed smooth path, standard elliptic domain perturbation after pullback to the disk gives an Eulerian expansion
\[
u_\varepsilon=u_0+\varepsilon u_1+\varepsilon^2u_2+o(\varepsilon^2).
\]
Because the differential operator itself is fixed, the interior equations are
\[
(\Delta-x\cdot\nabla)u_1=0,
\qquad
(\Delta-x\cdot\nabla)u_2=0
\]
in \(B_1\). Expanding the Dirichlet condition on \(r=\rho_\varepsilon(\theta)\) yields
\[
u_1(1,\theta)=-a f(\theta)
\]
and
\[
u_2(1,\theta)
=\frac a2 f'(\theta)^2-\frac b2 f(\theta)^2-f(\theta)\,\partial_r u_1(1,\theta).
\]

For the Fourier mode \(\cos k\theta\) or \(\sin k\theta\), the regular radial solution of the homogeneous Ornstein--Uhlenbeck equation is \(F_k\), where
\[
F_k''+\left(\frac1r-r\right)F_k'-\frac{k^2}{r^2}F_k=0,
\qquad F_k(1)=1,
\]
and the displayed Kummer formula follows by the substitution \(z=r^2/2\). Therefore
\[
\partial_r u_1(1,\theta)=-a\,\Lambda f(\theta),
\]
where \(\Lambda\) is diagonal in Fourier modes with eigenvalue \(\lambda_k=F_k'(1)\). Differentiating the Kummer expression gives
\[
\lambda_k
=k+\frac{k}{2(k+1)}
\frac{{}_1F_1(k/2+1;k+2;1/2)}{{}_1F_1(k/2;k+1;1/2)}>k,
\]
because both hypergeometric series have strictly positive terms.

For a single normalized Fourier pair with amplitude square \(a_k^2+b_k^2\), angular averaging gives the constant boundary component of \(u_2\) as
\[
(a_k^2+b_k^2)\left(\frac{a k^2}4-\frac b4+\frac{a\lambda_k}2\right).
\]
Only this constant angular mode contributes to \(\int_{B_1}u_2\,d\gamma\), and a regular radial homogeneous zero-mode is constant. Hence its interior contribution equals \(G\) times the preceding boundary constant.

The moving boundary contributes one further second-order term. In radial coordinates, with density factor \(r e^{-r^2/2}\), expansion of the collar integral from \(r=1\) to \(r=\rho_\varepsilon(\theta)\) gives
\[
-\frac{a w}4(a_k^2+b_k^2).
\]
Combining the interior and collar terms gives
\[
T_\gamma(K_\varepsilon)
=T_\gamma(B_1)
+\varepsilon^2\sum_{\substack{k\ge2\\k\ \mathrm{even}}}
\frac{A}{4\sqrt e}\left[2-A(k^2+2\lambda_k)\right](a_k^2+b_k^2)
+o(\varepsilon^2).
\]
Multiplying the quadratic coefficient by two gives the stated second derivative.

Finally, \(\lambda_k>k\), so for every even \(k\ge2\),
\[
k^2+2\lambda_k>k^2+2k\ge8.
\]
Since \(\sqrt e-1>1/4\),
\[
2-(\sqrt e-1)(k^2+2\lambda_k)<2-8(\sqrt e-1)<0.
\]
A nonzero smooth centrally symmetric zero-mean \(f\) has at least one nonzero even Fourier coefficient, proving strict negativity.

## Verification
The accompanying `verify.py` independently evaluates the Kummer series by its positive-term recurrence, reconstructs \(\lambda_k\) and the Hessian coefficient for several even modes, checks the analytic all-mode sign margin \(2-8(\sqrt e-1)<0\), checks the support-to-radial expansion numerically at cubic order, and checks the zero-mode collar/interior normalization against the exact ball second derivative. Its role is a reproducibility and algebra sanity check; the proof of negativity for all even modes is the analytic inequality \(\lambda_k>k\), not a finite numerical sweep.

## Relationship to prior work
Nguyen and Stancu, arXiv:2608.29941v1, prove failure of every positive-power Brunn--Minkowski-type convexity inequality for Gaussian torsional rigidity and derive the explicit two-dimensional disk derivative used above. They state that their first-order coefficient is not established as an exact Hadamard first variation and explicitly leave open whether, among centrally symmetric planar convex bodies of fixed Euclidean perimeter, the disk maximizes Gaussian torsional rigidity. The present result addresses a local second-order part of that open fixed-perimeter question.

Marín Sola and Salerno, arXiv:2603.19164v1, establish broad counterexamples for Ornstein--Uhlenbeck torsion under Minkowski interpolation and a positive convexity theorem restricted to centered Euclidean balls. Those statements do not imply the fixed-perimeter support-function Hessian computed here.

There are classical support-function second-variation formulas for ordinary Laplace torsional rigidity, and general second-order shape-calculus frameworks can justify differentiability. They do not supply the Gaussian coefficient above: the Ornstein--Uhlenbeck drift and Gaussian weight replace the classical Dirichlet-to-Neumann spectrum by the Kummer values \(\lambda_k\).

## Limitations
The theorem is local and directional. It does not prove the global fixed-perimeter inequality posed in the lead source. It is restricted here to smooth centrally symmetric support perturbations of the unit disk; no claim is made for nonsmooth perturbations, other radii, higher dimensions, or a quantitative neighborhood in a chosen topology. Standard smooth-domain differentiability for the uniformly elliptic Dirichlet problem with smooth coefficients is used to justify the second Eulerian expansion; the explicit coefficient calculation then proceeds directly.

## References
1. X. H. Nguyen and A. Stancu, *Failure of a Brunn--Minkowski-type inequality for the Gaussian torsional rigidity*, arXiv:2608.29941v1, first public 2026-08-30.
2. F. Marín Sola and F. Salerno, *Remarks on Brunn--Minkowski-type inequalities related to the Ornstein--Uhlenbeck operator*, arXiv:2603.19164v1, first public 2026-03-19.
