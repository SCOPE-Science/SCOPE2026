# The sharp quadratic-exponential radial covariance cone in every Euclidean dimension

## Finding
For each integer \(d\ge1\) and real parameters \(a,b\), consider the normalized isotropic function
\[
F_{a,b}(r)=e^{-r}(1+a r+b r^2),\qquad r\ge0.
\]
The kernel \(K_{a,b}(x,y)=F_{a,b}(\|x-y\|_2)\) on \(\mathbb R^d\) is positive definite **if and only if**
\[
Q_{d,a,b}(u)=1-a+(d+1)(a-3b)u+(d+1)(d+3)b u^2\ge0
\quad\text{for every }0\le u\le1.
\]
This single quadratic test has the following complete, mutually disjoint semialgebraic form:

1. \(b\le0\): \(a\le1\) and \(1+d a+d(d+1)b\ge0\).
2. \(b>0\) and \(a\ge3b\): \(a\le1\).
3. \(b>0\) and \(a\le-(2d+3)b\): \(1+d a+d(d+1)b\ge0\).
4. \(b>0\) and \(-(2d+3)b<a<3b\): \(4(d+3)b(1-a)\ge(d+1)(a-3b)^2\).

The particularly natural one-parameter quadratic deformation \(F_{0,b}\) is admissible **exactly** for
\[
-\frac{1}{d(d+1)}\le b\le\frac{4(d+3)}{9(d+1)}.
\]
At the negative boundary the spectral density has its unique zero at \(\xi=0\); at the positive boundary it has a radial double zero precisely on \(\|\xi\|_2=\sqrt{(2d+3)/3}\). In particular, the same \(F_{0,b}\) is admissible in every Euclidean dimension exactly for \(0\le b\le4/9\). Every admissible kernel is strictly positive definite on every finite set of distinct input sites.

## Assumptions and scope
The dimension \(d\) is any positive integer, both coefficients \(a,b\) are real, and the scale of the exponential is fixed to one; a different positive range scale is obtained by replacing \(r\) everywhere by \(\lambda r\) for \(\lambda>0\). Positive definiteness means that for every finite choice of points and complex coefficients, the associated Gram quadratic form is nonnegative. The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^d}e^{-i x\cdot\xi}f(x)\,dx\).

## Proof
Put \(h=(d+1)/2\) and \(C_d=2^d\pi^{(d-1)/2}\Gamma((d+1)/2)>0\). Gaussian subordination of the radial exponential, followed by the Gaussian Fourier transform, gives for every \(\lambda>0\)
\[
\widehat{e^{-\lambda\|\cdot\|_2}}(\xi)
=C_d\lambda(\lambda^2+\|\xi\|_2^2)^{-h}.
\]
For completeness, one may start from the exact identity
\[
e^{-\lambda r}=\frac{\lambda}{2\sqrt\pi}\int_0^\infty t^{-3/2}
  \exp\!\left(-\frac{\lambda^2}{4t}-t r^2\right)\,dt
\]
and use the Fourier transform \((\pi/t)^{d/2}\exp(-\|\xi\|_2^2/(4t))\) of the Gaussian. Absolute integrability allows the Fourier transform, the mixing integral, and the first two derivatives in \(\lambda\) to be interchanged near \(\lambda=1\).

Since \(r e^{-\lambda r}=-\partial_\lambda e^{-\lambda r}\) and \(r^2e^{-\lambda r}=\partial_\lambda^2e^{-\lambda r}\), differentiation and collection of terms yield the exact identity
\[
\widehat{F_{a,b}(\|\cdot\|_2)}(\xi)=
C_d(1+\|\xi\|_2^2)^{-h}\bigl[1-a+(d+1)(a-3b)u+(d+1)(d+3)b u^2\bigr],
\quad u=\frac{1}{1+\|\xi\|_2^2}.
\]
The map \(\|\xi\|_2\mapsto u\) covers \((0,1]\) and approaches zero as frequency tends to infinity. Since the Fourier transform is real continuous and integrable, Bochner's characterization (and uniqueness of the spectral measure) makes kernel positive definiteness equivalent to nonnegativity of this transform everywhere, hence to \(Q_{d,a,b}\ge0\) on the closed interval \([0,1]\).

It remains to compute the exact minimizer. The endpoints satisfy \(Q(0)=1-a\) and \(Q(1)=1+d a+d(d+1)b\). If \(b\le0\), the quadratic is concave or affine and the minimum occurs at an endpoint, proving case 1. If \(b>0\), the vertex is
\[
u_* =\frac{3b-a}{2(d+3)b}.
\]
It lies to the left of the interval when \(a\ge3b\) and to the right when \(a\le-(2d+3)b\), giving cases 2 and 3. In the remaining strict range it lies in \((0,1)\) and the minimum equals
\[
Q(u_*)=1-a-\frac{(d+1)(a-3b)^2}{4(d+3)b},
\]
which is nonnegative precisely in case 4. These exhaust all real coefficients including boundary equalities.

For \(a=0\), if \(b\le0\) the endpoint condition becomes \(b\ge-1/[d(d+1)]\); if \(b>0\), the vertex is always interior and the minimum condition becomes \(b\le4(d+3)/[9(d+1)]\). At the lower endpoint, \(Q(1)=0\) and \(Q(u)>0\) for \(u<1\). At the upper endpoint, the unique zero is the quadratic vertex \(u=3/[2(d+3)]\), equivalent to \(\|\xi\|_2^2=(2d+3)/3\). The upper endpoint decreases strictly toward \(4/9\) as the dimension tends to infinity, while the lower endpoint increases to zero; intersection over all dimensions gives \([0,4/9]\).

Finally, admissibility gives a continuous nonnegative spectral density that is strictly positive off at most two frequency spheres. Thus its positivity set contains an open ball. For any distinct sites and nonzero coefficient vector, the exponential polynomial in the Bochner integral cannot vanish on that entire open ball (analytic uniqueness and linear independence of distinct point masses), so the Gram quadratic form is strictly positive.

## Verification
The supplied exact-arithmetic checker reproduces the Fourier polynomial coefficients from the differentiation identities and tests the one-parameter endpoint formulas in multiple dimensions using rational arithmetic. These computations corroborate the algebra, whereas the proof for arbitrary dimension and real parameters is the preceding analytic argument. For instance, in dimension \(d=1\) the sharp quadratic range is \([-1/2,8/9]\); in dimension \(d=3\) it is \([-1/12,2/3]\). Parameters beyond either endpoint produce an open frequency region with negative Fourier transform, giving strict necessity.

## Relationship to prior work
Rasmussen and Williams (2006, Chapter 4, §4.2) describe the Matérn covariance functions and their positive spectral densities, including the classical exponential, linear-exponential, and quadratic-exponential kernels. Their examples furnish the natural fixed-range basis but do not state the sign-indefinite coefficient region or its sharp dimension dependence. In particular, for \(b>0\), the function \(F_{0,b}\) is **not** a nonnegative linear combination of \(e^{-r}\), \((1+r)e^{-r}\), and \((1+r+r^2/3)e^{-r}\): matching the quadratic coefficient forces the last weight \(3b\), matching the linear coefficient then forces the middle weight \(-3b\). The present result supplies an exact positive-definiteness test despite that negative mixture coefficient.

Bhatia and Jain (2014, arXiv:1409.7479v1) study dimension-dependent positive definiteness for different rational radial kernels, giving relevant context but not this exponential-polynomial coefficient cone. Golinskii, Malamud and Oridoroga (2015, arXiv:1502.07179v1) discuss strict dimension boundaries for Schoenberg classes; their public abstract concerns Bessel-type kernels rather than this coefficient family. The general Bochner criterion and the known Matérn transforms underlie our proof; the specific coefficient phase diagram is the new claim, not a new Fourier or Bochner theorem.

## Limitations
The classification covers only degree-two polynomials multiplying a single common exponential scale. It does not classify mixtures of different scales, non-Euclidean distance kernels, higher polynomial degrees, or conditional positive definiteness. Exact positivity of the spectral density at boundary parameters is compatible with its vanishing on a sphere or at zero. No claim of independent validation or comprehensive literature priority is made. A 2016 study of multi-length-scale correlation operators could not be inspected in full, and unindexed equivalent coefficient inequalities remain a residual priority risk.

## References
- C. E. Rasmussen and C. K. I. Williams, *Gaussian Processes for Machine Learning*, MIT Press (2006), Chapter 4, §4.2, especially the Matérn covariance formulas. https://gaussianprocess.org/gpml/chapters/RW4.pdf
- R. Bhatia and T. Jain, *On some positive definite functions*, arXiv:1409.7479v1, first posted 2014-09-26. https://arxiv.org/abs/1409.7479
- L. Golinskii, M. Malamud and L. Oridoroga, *Radial positive definite functions and Schoenberg matrices with negative eigenvalues*, arXiv:1502.07179v1, first posted 2015-02-25. https://arxiv.org/abs/1502.07179
- S. C. Mirouze et al., *A multiple length scale correlation operator for ocean data assimilation*, *Tellus A* 68 (2016), DOI 10.3402/tellusa.v68.29744; limited abstract and indexed section access only.
