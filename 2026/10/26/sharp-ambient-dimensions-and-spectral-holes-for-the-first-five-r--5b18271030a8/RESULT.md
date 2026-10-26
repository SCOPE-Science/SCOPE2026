# Sharp ambient dimensions and spectral holes for the first five radial sinc powers

## Finding
For every integer \(m\in\{1,2,3,4,5\}\), define \(\varphi_m(0)=1\) and \(\varphi_m(r)=(\sin r/r)^m\) for \(r>0\). For each integer \(d\ge1\), consider the translation-invariant radial kernel \(K_{m,d}(x,y)=\varphi_m(\|x-y\|_2)\) on \(\mathbb R^d\). Then
\[
K_{m,d}\text{ is positive semidefinite on every finite configuration}
\quad\Longleftrightarrow\quad
 d\le D_m,
\qquad(D_1,D_2,D_3,D_4,D_5)=(3,5,5,7,7).
\]
All five kernels are strictly positive definite in every dimension in which they are positive semidefinite.

At the **maximal** ambient dimensions, the unique radial Bochner spectral measures have the following additional properties. For \(m=1\), the measure is uniform on the unit sphere in \(\mathbb R^3\). For \(m=2\), the \(\mathbb R^5\) measure has positive interior density on radii \((0,2)\) and a positive surface atom at radius \(2\). For \(m=3\), the \(\mathbb R^5\) spectral measure has a genuine hole \(0\le r<1\) and positive density precisely at radii \(1<r<3\). For \(m=4\), the \(\mathbb R^7\) spectral density is positive on \((0,4)\) but has a strictly upward radial jump at radius \(2\). For \(m=5\), the \(\mathbb R^7\) spectral measure again has a hole \(0\le r<1\), with positive density precisely on \(1<r<5\). These are properties of the spectral measure, not zeros of the function \(\varphi_m\).

## Assumptions and scope
Positive semidefiniteness means that \(\sum_{i,j}c_i\overline{c_j}K_{m,d}(x_i,x_j)\ge0\) for every finite family of points and complex coefficients. The dimension \(d\) is an arbitrary positive integer; the exponent \(m\) is restricted to the five stated positive integers. Sinc is normalized by \(\sin r/r\), not \(\sin(\pi r)/(\pi r)\); rescaling would not change the maximal dimensions but would rescale spectral radii.

Let \(b_m\) be the density of the sum of \(m\) independent uniform variables on \([-1,1]\). For \(r\ge0\), let
\[
b_m(r)=\frac1{2^m(m-1)!}\sum_{j=0}^m(-1)^j\binom mj(m-2j-r)_+^{m-1},
\]
with the evident characteristic-function interpretation at \(m=1\). Put \(\mathcal Df=-r^{-1}f'(r)\), using distributional derivatives across positive knots. The radial Fourier spectral density (with respect to Euclidean volume) in odd dimension \(2k+1\) is \((2\pi)^{-k}\mathcal D^k b_m\), whenever the latter is a nonnegative radial measure. Distributional delta terms must be retained; regular pieces alone are insufficient.

## Proof
**Radial dimension walk.** The one-dimensional characteristic function of \(b_m\) is \(\varphi_m(|t|)\). The radial Fourier inversion identity in successive odd dimensions gives \(p_{d+2}(r)=-(2\pi r)^{-1}p_d'(r)\) on positive radii, valid distributionally, starting with \(p_1=b_m\). Uniqueness of Fourier transforms and Bochner's theorem imply that \(\varphi_m\) is radially positive definite in dimension \(2k+1\) exactly when this radial spectral distribution extends to a nonnegative finite rotationally invariant measure. The formulas below have total mass one because their Fourier transforms equal \(\varphi_m\) and \(\varphi_m(0)=1\). All radial singularities at the origin are locally integrable after multiplication by the appropriate volume element.

**Exact positive spectra.** In what follows \(r>0\), and omitted intervals have zero density. For \(m=1\), \(b_1=1/2\) on \((0,1)\); thus \(\mathcal D b_1=\tfrac12\delta_1\) is a positive measure, establishing dimension \(3\).

For \(m=2\),
\[
\mathcal D^2 b_2(r)=\frac{\mathbf1_{(0,2)}(r)}{4r^3}+\frac1{16}\delta_2.
\]
Both terms are positive. For \(m=3\),
\[
\mathcal D^2 b_3(r)=\frac{3\mathbf1_{(1,3)}(r)}{8r^3}.
\]
For \(m=4\),
\[
\mathcal D^3 b_4(r)=
\begin{cases}3/(32r^3),&0<r<2,\\(48-r^2)/(32r^5),&2<r<4,\\0,&r>4.
\end{cases}
\]
For \(m=5\),
\[
\mathcal D^3 b_5(r)=
\begin{cases}0,&0<r<1,\\5(r^2-1)/(32r^5),&1<r<3,\\5(25-r^2)/(64r^5),&3<r<5,\\0,&r>5.
\end{cases}
\]
The signs establish positivity in dimensions \(3,5,5,7,7\), respectively. Their restrictions to lower-dimensional linear subspaces are likewise positive semidefinite. Each measure has positive mass away from the origin. The standard strictness criterion for nonconstant radial positive-definite functions in dimension at least two, and direct Fourier uniqueness in dimension one, imply strict positive definiteness at pairwise distinct points.

**Exclusion of higher odd dimensions.** For \(m=1\), a further dimension walk differentiates \(\delta_1\), which cannot be a nonnegative measure. For \(m=2\), the positive atom \(\tfrac1{16}\delta_2\) in \(\mathcal D^2b_2\) likewise produces a nonzero derivative of a delta on the next walk. For \(m=3\), \(\mathcal D^2b_3\) has upward jump \(3/8\) at \(r=1\); the next walk produces the negative atom \(-\tfrac38\delta_1\). For \(m=4\), \(\mathcal D^3b_4\) has upward jump \(1/32\) at \(r=2\), so the next walk has a negative atom \(-\tfrac1{64}\delta_2\). For \(m=5\), on \(1<r<3\) the next density is
\[
\mathcal D^4b_5(r)=\frac{5(3r^2-5)}{32r^7},
\]
which is negative for \(1<r<\sqrt{5/3}\). Thus the first excluded **odd** dimensions are \(5,7,7,9,9\).

**Exclusion of the intervening even dimensions.** Suppose a radial positive-definite kernel on \(\mathbb R^{d}\) extended to \(\mathbb R^{d+1}\). The unique rotationally invariant Bochner measure in dimension \(d\) would then be the orthogonal projection of a rotationally invariant positive measure in dimension \(d+1\). Conditional on an upper-dimensional sphere of positive radius \(R\), that projection has Lebesgue density proportional to \((R^2-r^2)^{-1/2}\mathbf1_{r<R}\); hence any positive mixture is absolutely continuous on \(r>0\). This excludes \(m=1,2\) because their maximal-odd-dimensional spectra have positive-radius atoms. It also excludes \(m=3,5\): every nonzero such mixture is strictly positive on some entire ball about the origin, whereas their maximal-odd-dimensional spectra vanish throughout the ball of radius \(1\).

For \(m=4\), put \(s=r^2\) and write its (unnormalized) dimension-seven spectral density as \(H(s)\). If it were the projection of a positive radial measure in dimension eight, then for a positive measure \(\mu\) we would have \(H(s)=\int_{u>s}(u-s)^{-1/2}\mu(du)\). Abel composition and Tonelli would force
\[
G(s):=\int_s^\infty(t-s)^{-1/2}H(t)\,dt=\pi\mu((s,\infty))
\]
to be nonincreasing. However \(H\) has the **upward** jump \(J=1/32\) at \(s=4\). Subtracting \(J\mathbf1_{s>4}\) locally leaves a continuous piecewise smooth function. The Abel integral of the jump has derivative \(J/\sqrt{4-s}+O(1)\) as \(s\uparrow4\), while the continuous remainder contributes only bounded derivative there. Hence \(G'(s)>0\) sufficiently close to \(4\) from below, contradiction. Normalizing constants are positive and do not affect this argument. Thus \(m=4\) also fails in the intervening dimension eight.

These exclusions, together with nestedness of radial positive-definite classes in dimension, prove the claimed sharp integer-dimensional cutoffs.

## Verification
Run `python check_sinc.py` with SymPy installed. The program reconstructs \(b_m\) from its finite truncated-power formula, applies the exact rational differential operator, and checks all spectral-density pieces, discontinuity coefficients and negative obstruction signs using symbolic identities. The program is a finite exact algebra verification of displayed formulas; the dimension-walk and Abel/projection arguments above supply the infinite-configuration and all-dimensional conclusions.

## Relationship to prior work
Schoenberg's radial Bochner representation, as reviewed by Gneiting, supplies the general positivity criterion and nestedness across Euclidean dimensions. Abel and Kushnirevych develop precise one-variable Fourier–B-spline identities for sinc powers. The present statement instead determines the first five **maximal Euclidean spatial dimensions**, their distinctive inner spectral holes and boundary singularities, and rules out the intervening even dimensions by projection obstructions. The cited literature supplies mathematical tools but, in the material inspected, does not state this combined sharp classification.

## Limitations
The classification is only for the first five positive integer powers; it makes no assertion about all higher integers or noninteger powers. The distributional spectral descriptions are exact but do not estimate conditioning of finite kernel Gram matrices. An equivalent formulation could exist in older, difficult-to-index radial-harmonic-analysis or spline literature. No independent mathematical validation has been performed.

## References
1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, originally posted 2011-11-30. In particular Section 2 reviews Schoenberg's Euclidean radial representation and nested classes.
2. U. Abel and V. Kushnirevych, *Sinc integrals revisited*, Mathematische Semesterberichte 70 (2023), 147–164, DOI:10.1007/s00591-023-00342-5. Sections 2–4 give one-variable sinc-power and cardinal B-spline Fourier identities.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536 (background radial positivity).
