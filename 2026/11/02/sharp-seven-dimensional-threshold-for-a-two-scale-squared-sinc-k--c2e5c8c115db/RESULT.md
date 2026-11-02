# Sharp seven-dimensional threshold for a two-scale squared-sinc kernel

## Finding
For every pair of positive real scales \(a,b\), set
\[
F_{a,b}(r)=\left(\frac{\sin(ar)}{ar}\right)^2
\left(\frac{\sin(br)}{br}\right)^2,\qquad F_{a,b}(0)=1.
\]
Let \(\Phi_d\) mean the continuous radial functions \(F\) for which \(F(\|x-y\|_2)\) is positive semidefinite for every finite set of points in \(\mathbb R^d\). Put \(\tau=\max(a,b)/\min(a,b)\). Then
\[
\boxed{F_{a,b}\in\Phi_d\ \Longleftrightarrow\
\begin{cases}
 d\le7,&1\le\tau\le1+\sqrt3,\\
 d\le5,&\tau>1+\sqrt3.
\end{cases}}
\]
Every admitted positive integer dimension has **strict** positive definiteness on finite sets of distinct points. The boundary ratio \(1+\sqrt3\) is included. Thus two individually five-dimensional squared-sinc kernels can have a seven-dimensional positive-definite product, but only below a sharp scale-separation threshold.

## Assumptions and scope
All parameters \(a,b\) are arbitrary strictly positive real numbers; there are no commensurability assumptions. Positive definiteness is in the Hermitian finite-Gram-matrix sense. The assertion concerns Euclidean radial extension, not positive definiteness on spheres or on lattices. By scaling, assume \(a=1\), \(b=t\ge1\). Values of spectral densities at finitely many knots are irrelevant, and density formulas below are asserted on their open intervals.

## Proof
**1. One-dimensional uniform convolution and the dimension walk.** Write \(\Omega_d(z)\) for the characteristic function of a coordinate of a vector uniformly distributed on the unit sphere in \(\mathbb R^d\). Thus \(\Omega_3(z)=\sin(z)/z\). In dimension three, \(F_{1,t}\) is the Fourier transform of the sum of four independent uniform spherical vectors with radii \(1,1,t,t\). The first Cartesian coordinate has density \(q_t\), the convolution of the four uniform laws on \([-1,1],[-1,1],[-t,t],[-t,t]\). Its cubic B-spline formula is
\[
q_t(x)=\frac{1}{96t^2}\sum_{\varepsilon\in\{-1,1\}^4}
\left(\prod_{j=1}^4\varepsilon_j\right)
\left(x+\varepsilon_1+\varepsilon_2+t\varepsilon_3+t\varepsilon_4\right)_+^3.
\]
The three-dimensional **spectral radial** probability density is \(p_3(r)=-2rq_t'(r)\) for \(r>0\). When \(p_d\) is a compactly supported radial density with the requisite distributional derivatives, its unique prospective lift by two dimensions has density
\[
p_{d+2}(r)=\frac{(d-1)p_d(r)-r p_d'(r)}d.
\]
Indeed, integration by parts multiplies the even \(2k\)-th radial moment by \((d+2k)/d\), exactly the quotient of the coefficients in the spherical-Bessel expansions of \(\Omega_d\) and \(\Omega_{d+2}\). Compact support ensures moment determinacy. Here \(q_t\in C^2\), and both lifts are ordinary integrable functions, without endpoint atoms. They are
\[
p_5(r)=\frac23\{r^2q_t''(r)-rq_t'(r)\},\qquad
p_7(r)=\frac2{15}\{3r^2q_t''(r)-3rq_t'(r)-r^3q_t'''(r)\}.
\]
The general scaling is \(p_{d;a,b}(r)=a^{-1}p_{d;1,t}(r/a)\), with \(t=b/a\) after ordering. All these signed densities integrate to one and reproduce \(F_{1,t}\).

**2. Exact seven-dimensional density and its sign.** Put \(L=2(t+1)\). When \(1<t<2\), \(p_7\) vanishes outside \([0,L]\) and is, successively,
\[
\begin{array}{c|l}
\text{radius interval}&p_7(r)\\\hline
(0,2(t-1))&r^3/(120t^2)\\
(2(t-1),2)&r\{r^2-4(t-1)^2\}/(80t^2)\\
(2,2t)&r\{r^2-12t^2+24t+12\}/(240t^2)\\
(2t,L)&r\{12(t+1)^2-r^2\}/(240t^2).
\end{array}
\]
For \(t>2\), the corresponding four intervals are
\[
(0,2),\quad(2,2(t-1)),\quad(2(t-1),2t),\quad(2t,L),
\]
with respective densities
\[
\frac{r^3}{120t^2},\qquad \frac r{10t^2},\qquad
\frac{r(r^2-12t^2+24t+12)}{240t^2},\qquad
\frac{r(12(t+1)^2-r^2)}{240t^2}.
\]
The cases \(t=1\) and \(t=2\) follow by merging coinciding intervals and taking parameter limits. For \(1\le t\le2\), each displayed expression is nonnegative: in the third region its potentially limiting numerator is at least \(28-12(t-1)^2\ge16\). For \(t>2\), only the third region can be negative; its quadratic numerator increases with \(r>0\), so its minimum is attained just right of \(r=2(t-1)\), where
\[
p_7\big(2(t-1)+\big)=\frac{(t-1)(-t^2+2t+2)}{15t^2}.
\]
Thus \(p_7\ge0\) almost everywhere exactly when \(t\le1+\sqrt3\). If \(t>1+\sqrt3\), it is strictly negative on a nonempty open interval. Bochner uniqueness proves that \(F_{1,t}\in\Phi_7\) precisely on the asserted closed parameter range.

**3. The five-dimensional lower bound at every ratio.** The established Schoenberg product identity \(\Omega_3(ar)^2\in\Phi_5\) holds for every \(a>0\) (also follows from the three-to-five density calculation for two equal spheres, including its endpoint atom). The Schur product theorem gives \(F_{a,b}=\Omega_3(ar)^2\Omega_3(br)^2\in\Phi_5\), for all positive \(a,b\). Nesting of the \(\Phi_d\) classes gives every smaller dimension.

**4. Why no eighth-dimensional lift exists.** The seven-dimensional radial density \(p_7\) has a strictly **upward** finite jump at \(r=2t\). For \(t>1\), the two adjacent formulas give
\[
p_7(2t+)-p_7(2t-)=\frac{2t}{15}>0.
\]
At \(t=1\) the coincident knots give a jump \(4/15>0\). Suppose \(F_{1,t}\in\Phi_8\), with nonnegative eight-dimensional radial spectral measure \(\mu_8\). By projection of a uniformly oriented eight-dimensional spectral radius \(R\) onto seven coordinates,
\[
\frac{p_7(r)}{r^6}=C\int_{R>r}\frac{\mu_8(dR)}{R^6\sqrt{R^2-r^2}},\qquad C>0.
\]
The measure \(\mu_8\) is supported in \([0,L]\): its one-coordinate projection is exactly \(q_t\), whose support is \([-L,L]\), while every positive mass at radius \(R>L\) would contribute positive projected mass outside that interval. Put \(x=r^2\) and \(H(x)=p_7(\sqrt x)/x^3\). The preceding relation reads \(H(x)=\int_{y>x}(y-x)^{-1/2}\eta(dy)\) for a nonnegative measure \(\eta\), locally finite away from zero. A second Abel integration gives
\[
A(x):=\int_x^{L^2}\frac{H(u)}{\sqrt{u-x}}\,du
=\pi\eta((x,L^2]),
\]
which must be nonincreasing in \(x>0\). But if a piecewise smooth \(H\) has a positive upward jump \(J\) at \(x_0=(2t)^2\), the jump contributes locally \(2J\{\sqrt{x_0+\delta-x}-\sqrt{x_0-x}\}\) to \(A(x)\) for \(x<x_0\), so \(A'(x)=J/\sqrt{x_0-x}+O(1)>0\) as \(x\uparrow x_0\). This contradiction excludes \(\Phi_8\). Dimension nesting excludes all \(d\ge8\).

**5. Strictness.** On the admitted \(\Phi_7\) range, the density \(p_7\) is positive on a nonempty open radial interval, giving nonzero spectral density on an open set in \(\mathbb R^7\). For \(\Phi_5\), the product of the two \(\Omega_3^2\) spectral measures contains the convolution of their positive spherical atoms, which likewise has positive density on an open annulus in \(\mathbb R^5\). Restricting to lower dimensions preserves strictness. If a finite Gram quadratic form vanished, the entire exponential polynomial \(\sum_j c_j e^{i\xi\cdot x_j}\) would vanish on an open set, hence everywhere; independence of distinct characters forces every \(c_j=0\).

## Verification
The included standalone `check.py` constructs the exact cubic-hinge convolution, differentiates its pieces, verifies all displayed seven-dimensional density formulas symbolically in both open parameter chambers, checks normalization \(\int_0^L p_7=1\) and second moment \(\int_0^L r^2p_7(r)\,dr=14(1+t^2)/3\), and checks the sharp endpoint quadratic and positive jump. It also performs exact-rational signed-density probes, including a parameter beyond the cutoff. These calculations verify the algebra; the infinite-dimensional classification and Abel obstruction are proved analytically above. Execute `python check.py` with Python 3 and SymPy.

## Relationship to prior work
Golinskii, Malamud and Oridoroga (arXiv:1502.07179v1, 25 February 2015), Theorem 4.1, prove \(\Omega_n(ar)\Omega_n(br)\in\Phi_n\setminus\Phi_{n+1}\) for unequal radii; their Theorem 4.3 establishes \(\Omega_n(r)^2\in\Phi_{2n-1}\setminus\Phi_{2n}\). In particular, their squared-sinc result gives the five-dimensional factors used above but does **not** state the dimension of their product for arbitrary scale ratio. Their Theorem 3.1 supplies the general projection transition, not this sharp ratio cutoff. Earlier dimension-walk work by Daley and Porcu, and by Porcu and Zastavnyi, provides general structural background rather than this explicit two-scale classification. An accessible earlier exact classification of equal powers of sinc covers the special case \(a=b\); it does not imply the unequal-scale threshold. The new point is the closed-form boundary \(1+\sqrt3\), including the endpoint and the nonextension certificate.

## Limitations
The theorem concerns only two **paired** positive frequencies, not four independent frequencies and not arbitrary products of Bessel kernels. The proof does not address uniform finite-configuration condition numbers. Originality is supported by bounded comparisons, not an exhaustive theorem of uniqueness across historical literature. No independent mathematical validation has yet been performed.

## References
1. L. Golinskii, M. Malamud and L. Oridoroga, *Radial positive definite functions and Schoenberg matrices with negative eigenvalues*, arXiv:1502.07179v1 (first public version dated 2015-02-25), especially Theorems 3.1, 4.1 and 4.3; https://arxiv.org/pdf/1502.07179.
2. D. J. Daley and E. Porcu, *Dimension walks and Schoenberg spectral measures*, Proceedings of the American Mathematical Society 142 (2014), 1813–1824, https://doi.org/10.1090/S0002-9939-2014-11894-6.
3. E. Porcu and V. Zastavnyi, *Generalized Askey functions and their walks through dimensions*, Expositiones Mathematicae 32 (2014), 190–198, https://doi.org/10.1016/j.exmath.2013.10.004.
