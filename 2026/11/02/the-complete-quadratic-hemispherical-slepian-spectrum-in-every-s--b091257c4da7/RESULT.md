# The complete quadratic hemispherical Slepian spectrum in every sphere dimension

## Finding
Let \(d\ge3\). Let \(\sigma_d\) be normalized surface measure on \(S^{d-1}\subset\mathbb R^d\), \(H=\{x\in S^{d-1}:x_1>0\}\), and \(V_2=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\), the space of complex spherical harmonics of degrees zero, one and two. Define the hemisphere concentration operator \(C_d=P_{V_2}M_{\mathbf1_H}|_{V_2}\) with the full-sphere \(L^2(\sigma_d)\) inner product.

Put
\[
\mu_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
s_{0,d}=\frac{d\mu_d}{d+1}\sqrt{\frac{3d+5}{2}},\qquad
s_{1,d}=\frac{d\mu_d}{d+1}\sqrt{d+2}.
\]
Then \(0<s_{1,d}<s_{0,d}<1\) and the **complete spectrum**, with multiplicity, is
\[
\begin{array}{c|c}
\text{Eigenvalue}&\text{Multiplicity}\\ \hline
(1+s_{0,d})/2,\ (1-s_{0,d})/2&1\text{ each}\\
(1+s_{1,d})/2,\ (1-s_{1,d})/2&d-1\text{ each}\\
1/2&d(d-1)/2.
\end{array}
\]
There are no further eigenvalues. The maximum concentration \((1+s_{0,d})/2\) has a unique complex maximizing line. The restriction map \(V_2\to L^2(H,\sigma_d)\) is injective, with exact operator condition number
\[
\kappa_d=\sqrt{\frac{1+s_{0,d}}{1-s_{0,d}}}.
\]
As \(d\to\infty\),
\[
s_{0,d}^2\to3/\pi,\quad s_{1,d}^2\to2/\pi,\quad
\kappa_d\to\sqrt{\frac{1+\sqrt{3/\pi}}{1-\sqrt{3/\pi}}}.
\]
Both squared noncentral parameters decrease strictly when the dimension is increased by two.

## Assumptions and scope
The sphere is the **surface** \(S^{d-1}\), not the solid ball. There is no radial variable, and the degree cutoff includes *all* three harmonic degrees \(0,1,2\) with complex coefficients. The positive hemisphere is \(x_1>0\); the equator has zero measure. Rotating the hemisphere changes the eigenfunctions but not the eigenvalues. Eigenvalues refer to normalized full-sphere inner products; restricting the target measure to the probability measure of the hemisphere would multiply the concentration eigenvalues by two.

The dimension of \(V_2\) is \(d(d+3)/2\). When \(d=3\), the spectrum specializes to \((1\pm3\sqrt7/8)/2\) once each, \((1\pm3\sqrt5/8)/2\) twice each, and \(1/2\) three times.

## Proof
Write \(t=x_1\), \(y_i=x_i\) for \(2\le i\le d\), and \(\mathbb E\) for integration against \(\sigma_d\). The identity
\[
\mathbf1_H=\tfrac12(1+\operatorname{sgn}t)
\]
shows that \(C_d=(I+T_d)/2\), where \(T_d=P_{V_2}M_{\operatorname{sgn}t}|_{V_2}\). Reflection \(t\mapsto-t\) makes \(T_d\) interchange the odd and even sectors.

The orthogonal decomposition under rotations of the last \(d-1\) coordinates has exactly three kinds of sectors: (i) the scalar subspace spanned by \(1,t,t^2-1/d\); (ii) the \(d-1\) mutually orthogonal vector pairs spanned by \(y_i,ty_i\); and (iii) the even traceless quadratics in \(y_2,\ldots,y_d\), of dimension \(d(d-1)/2-1\). These spaces are mutually orthogonal both on the whole sphere and under the sign multiplier, by symmetry and the elementary rotational moments. The last sector is annihilated by \(T_d\).

The needed normalized moments are
\[
\mathbb E[t^2]=\frac1d,\quad
\mathbb E[t^4]=\frac3{d(d+2)},\quad
\mathbb E[|t|]=\mu_d,\quad
\mathbb E[|t|^3]=\frac{2\mu_d}{d+1},
\]
\[
\mathbb E[y_i^2]=\frac1d,\quad
\mathbb E[t^2y_i^2]=\frac1{d(d+2)},\quad
\mathbb E[|t|y_i^2]=\frac{\mu_d}{d+1}.
\]
They follow from the beta density of \(t\) and conditional rotational symmetry of \(y\).

For the scalar sector let
\[
e_0=1,\quad e_2=\frac{t^2-1/d}{\sqrt{2(d-1)/(d^2(d+2))}},\quad o=\sqrt d\,t.
\]
This is an orthonormal basis with even members \(e_0,e_2\) and odd member \(o\). In this order \(T_d\) has matrix
\[
\begin{pmatrix}0&0&a\\0&0&b\\a&b&0\end{pmatrix},\quad
 a=\sqrt d\,\mu_d,\quad
 b=\frac{\sqrt d\,\mu_d}{d+1}\sqrt{\frac{(d-1)(d+2)}2}.
\]
Hence its eigenvalues are \(0,\pm\sqrt{a^2+b^2}\), and a direct simplification gives \(a^2+b^2=s_{0,d}^2\). Its normalized positive/negative eigenfunctions are
\[
\frac1{\sqrt2}\left(\frac{ae_0+be_2}{s_{0,d}}\pm o\right),
\]
while the centered one is \((-be_0+ae_2)/s_{0,d}\).

For each \(i=2,\ldots,d\) use the orthonormal vector pair \(e_i=\sqrt d\,y_i\), \(o_i=\sqrt{d(d+2)}\,ty_i\). The sign operator on their span has matrix \(\begin{psmallmatrix}0&s_{1,d}\\s_{1,d}&0\end{psmallmatrix}\), because
\[
\langle e_i,T_do_i\rangle=d\sqrt{d+2}\,\mathbb E[|t|y_i^2]
=\frac{d\sqrt{d+2}\,\mu_d}{d+1}.
\]
Its positive/negative eigenvectors are \((e_i\pm o_i)/\sqrt2\). The traceless-tangential sector and the centered scalar vector account for \(d(d-1)/2\) midpoint eigenvalues. All multiplicities sum to \(d(d+3)/2\), proving completeness.

The identity \(s_{0,d}^2-s_{1,d}^2=d^2\mu_d^2/[2(d+1)]>0\) proves the unique top eigenspace. Both parameters are less than one, since a nonzero polynomial of degree at most two cannot vanish on an open hemisphere: concentration is strictly between zero and one for every nonzero \(f\in V_2\). Thus the two extreme eigenvalues are the unique maximum/minimum, and the condition number of the restriction map is as stated.

Finally \(\mu_{d+2}=d\mu_d/(d+1)\) yields
\[
\frac{s_{0,d+2}^2}{s_{0,d}^2}=\frac{(d+2)^2(3d+11)}{(d+3)^2(3d+5)}<1,\qquad
\frac{s_{1,d+2}^2}{s_{1,d}^2}=\frac{(d+2)(d+4)}{(d+3)^2}<1.
\]
The numerator difference in the first inequality is \(d+1\). The asymptotics follow from \(\mu_d\sim\sqrt{2/(\pi d)}\).

## Verification
Run `python check.py` after installing the packages in `requirements.txt`. The code separately assembles the *full* generalized Slepian eigenproblem in a monomial basis using gamma-product formulas for full-sphere and half-sphere moments. It compares all eigenvalues against the closed formula for every integer \(3\le d\le10\); this comprises 268 eigenvalue comparisons. It also checks the special \(d=3\) values and rational inequalities governing dimension-step monotonicity. The run returned `ALL_CHECKS_PASS`. The code is corroborating finite evidence, not a proof for all dimensions.

## Relationship to prior work
Simons, Dahlen and Wieczorek (2006) establish spherical Slepian concentration and spherical-cap matrices on the ordinary two-sphere; their general integral-matrix formula entails computation of any fixed degree-two example in that dimension, which is prior art. Michel, Plattner and Seibert (2021) establish the scalar, vector and tensor cap framework, still on the two-sphere in \(\mathbb R^3\). Roddy and McEwen (2021) use such spectra for localized spherical wavelets. A separate known hemisphere parity law accounts for the centered eigenvalues on \(S^2\), without supplying this dimension-dependent pair of noncentral levels. The focus here is the complete **arbitrary-dimensional** low-pass quadratic spectrum, closed-form sharp conditioning, and full extremizing eigenspaces; no general spherical concentration principle or center-multiplicity mechanism is claimed as new.

## Limitations
Historical priority is provisional. General spherical-cap matrix formulas could subsume portions through specialization, especially in \(d=3\); exact dimension-uniform formulas were not located in the checked texts and records, but an unindexed equivalent remains possible. The result concerns the hemisphere, a complete degree-two low-pass harmonic band, exact noiseless norm ratios, and \(d\ge3\); it does not provide higher-degree spectra, noisy reconstruction bounds, or arbitrary-cap formulas. No independent mathematical audit has been performed.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review **48** (2006), 504–536, DOI: 10.1137/S0036144504445765; public preprint arXiv:math/0408424.
2. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first made public 2021-03-26.
3. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023 (2021), DOI: 10.1109/TSP.2022.3233309.
