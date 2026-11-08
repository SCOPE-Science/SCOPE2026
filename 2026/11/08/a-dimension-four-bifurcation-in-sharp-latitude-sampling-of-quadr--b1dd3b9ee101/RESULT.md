# A dimension-four bifurcation in sharp latitude sampling of quadratic spherical harmonics

## Finding

Let \(d\geq3\), let \(\mathcal H_2(S^{d-1})\) be the complex vector space of restrictions to the unit sphere of homogeneous harmonic quadratic polynomials, equipped with normalized spherical \(L^2\) norm, and fix \(0<z<1\). Write \(\nu_{d,z}\) for the probability measure giving half its mass to each latitude \(x_1=+\sqrt z\) and \(x_1=-\sqrt z\), with normalized conditional surface measure on each latitude. The latitude restriction Gram operator \(C_{d,z}\) on \(\mathcal H_2\) is defined by
\[
\langle C_{d,z}f,g\rangle_{S^{d-1}}=\int f(x)\overline{g(x)}\,d\nu_{d,z}(x).
\]
Its complete eigenvalue spectrum is the following three bands, where multiplicities are complex dimensions:
\[
\begin{array}{c|c}
\lambda_0(d,z)=\dfrac{(d+2)(dz-1)^2}{2(d-1)}&1\\[3pt]
\lambda_1(d,z)=\dfrac{d(d+2)}{d-1}z(1-z)&d-1\\[3pt]
\lambda_2(d,z)=\dfrac{d(d+2)}{(d-1)(d+1)}(1-z)^2&\dfrac{(d-2)(d+1)}2.
\end{array}
\]
Thus all pure quadrupoles are stably determined from one non-equatorial latitude (or its antipodally balanced pair) precisely when \(z\ne1/d\). The exceptions \(z=0,1\), if included as degenerate limiting observations, are also noninjective.

The sharp, globally E-optimal latitude means maximization of \(\lambda_{\min}(C_{d,z})\) over \(0<z<1\), with this fixed probability normalization. Put
\[
z_-(d)=\frac{2d-\sqrt{d(3d-2)}}{d(d+2)},\qquad
z_+(d)=\frac{1+\sqrt{2d/(d+1)}}{d+\sqrt{2d/(d+1)}}.
\]
The complete set of maximizing squared heights is
\[
\operatorname{argmax}_{0<z<1}\lambda_{\min}(C_{d,z})=
\begin{cases}
\{z_-(3)\},&d=3,\\
\{z_-(4),z_+(4)\},&d=4,\\
\{z_+(d)\},&d\ge5.
\end{cases}
\]
At \(d=4\), both designs have the same exact sharp lower bound \((11-2\sqrt{10})/9\). For \(d\ge5\), the optimum lower bound is
\[
\frac{d(d+2)(d-1)}{(d+1)\bigl(d+\sqrt{2d/(d+1)}\bigr)^2}\xrightarrow[d\to\infty]{}1,
\]
and \(d z_+(d)\to1+\sqrt2\). For \(d=3\), the sharp lower bound is \((11-\sqrt{21})/10\). No theorem about all harmonic degrees or arbitrary observation geometry is asserted.

## Assumptions and scope

The sphere \(S^{d-1}\subset\mathbb R^d\) carries normalized rotation-invariant surface probability. All latitude measures are probability measures, **not** unnormalized ambient surface measures. In the above definition \(\nu_{d,z}\) is supported on two smooth \((d-2)\)-spheres for \(0<z<1\); the northern latitude alone induces exactly the same Gram operator on even quadratic harmonics, because \(f(-x)=f(x)\). Thus antipodal balancing is optional for this particular even harmonic band, not an additional independent measurement. The result applies to complex coefficients and to the corresponding real Hilbert space.

We optimize the absolute smallest Gram eigenvalue (E-optimal lower frame bound), **not** the ratio of largest to smallest eigenvalues. We do not claim optimality over measures not supported on one latitude pair, arbitrary weights, combined harmonic degrees, or discrete point samples.

## Proof

Every \(f\in\mathcal H_2\) has a unique representation \(f(x)=x^{\mathsf T}Ax\) with complex symmetric traceless \(d\times d\) matrix \(A\). The fourth spherical moment identity gives
\[
\|f\|_{L^2(S^{d-1})}^2=\frac{2}{d(d+2)}\operatorname{tr}(AA^*).
\]
Write \(x=(s\sqrt z,\sqrt{1-z}\,y)\), where the sign \(s\) is equally likely \(\pm1\), and \(y\) is uniform on \(S^{d-2}\subset\mathbb R^{d-1}\). Decompose orthogonally
\[
A=\begin{pmatrix}a&b^{\mathsf T}\\b&-\frac a{d-1}I+B\end{pmatrix},
\quad \operatorname{tr}B=0.
\]
Then the restriction polynomial splits into three pairwise orthogonal spherical harmonic orders on the latitude:
\[
f(x)=\underbrace{\frac{dz-1}{d-1}a}_{\text{constant}}
+\underbrace{2s\sqrt{z(1-z)}\,b^{\mathsf T}y}_{\text{linear}}
+\underbrace{(1-z)y^{\mathsf T}By}_{\text{traceless quadratic}}.
\]
The normalized moments on \(S^{d-2}\) are
\[
\mathbb E|b^{\mathsf T}y|^2=\frac{\|b\|^2}{d-1},\qquad
\mathbb E|y^{\mathsf T}By|^2=\frac{2\operatorname{tr}(BB^*)}{(d-1)(d+1)}.
\]
The ambient coefficient norms of the three blocks are respectively \(d|a|^2/(d-1)\), \(2\|b\|^2\), and \(\operatorname{tr}(BB^*)\). Dividing the latitude norm of each block by its ambient spherical norm gives exactly \(\lambda_0,\lambda_1,\lambda_2\) above, with dimensions \(1,d-1,((d-1)d/2)-1\). This proves the spectrum, the multiplicities, and the injectivity boundary.

For sharp global optimization, on \(0\le z\le1/d\) the functions \(\lambda_0\) and \(\lambda_1\) are respectively strictly decreasing and strictly increasing; their unique crossing in this interval is \(z_-(d)\), obtained from \(d(d+2)z^2-4dz+1=0\). At this point \(\lambda_2>\lambda_1\), since \(\lambda_1/\lambda_2=(d+1)z/(1-z)<1\) whenever \(z<1/(d+2)\), and \(z_-<1/(d+2)\) follows from \(\sqrt{d(3d-2)}>d\). Thus the unique maximum of the full minimum on this left interval is
\[
L_d=\lambda_0(d,z_-)=\lambda_1(d,z_-).
\]
For \(1/d\le z<1\), \(\lambda_1>\lambda_2\), so only \(\lambda_0\) (strictly increasing) and \(\lambda_2\) (strictly decreasing) compete. Their unique crossing is \(z_+\) and the unique right-interval maximum is
\[
R_d=\lambda_0(d,z_+)=\lambda_2(d,z_+).
\]
To compare the two candidates across dimensions without an unproved numerical sign comparison, set \(w=dz\in[0,1]\) on the left. Then
\[
\lambda_0=\frac{d+2}{2(d-1)}(1-w)^2,\qquad
\lambda_1=\frac{d+2}{d-1}w(1-w/d).
\]
For every fixed \(0\le w\le1\), both expressions are nonincreasing as the real parameter \(d\ge3\) increases, and both strictly decrease whenever \(0<w<1\). The first assertion is immediate, and for the second the derivative of \((d+2)(d-w)/(d(d-1))\) is
\[
\frac{d^2(w-3)+w(4d-2)}{d^2(d-1)^2}<0,
\]
since the numerator is at most \(-2(d-1)^2\). The left-branch maximizer always has \(0<w<1\); hence \(L_d\) strictly decreases in \(d\).

For the right interval put \(t=(dz-1)/(1-z)\in[0,\infty)\), so \(z=(1+t)/(d+t)\). Then
\[
\lambda_0=G_d(t)\frac{t^2}{2},\qquad
\lambda_2=G_d(t)\frac{d}{d+1},\qquad
G_d(t)=\frac{(d+2)(d-1)}{(d+t)^2}.
\]
The optimum is at \(t_d=\sqrt{2d/(d+1)}>1\). At every fixed \(t\ge1\), both displayed expressions increase strictly with \(d\): indeed
\[
\frac{\partial G_d(t)}{\partial d}=\frac{2dt-d+t+4}{(d+t)^3}>0,
\]
and \(d/(d+1)\) also increases. Evaluating the new dimension at the old optimum shows that \(R_d\) strictly increases with \(d\). Finally direct substitution at \(d=4\) yields \(L_4=R_4=(11-2\sqrt{10})/9\). Hence \(L_3>R_3\), while \(R_d>L_d\) for all integers \(d\ge5\), and all equality cases are exactly those stated. The stated limit follows directly from the \(z_+\) expression.

## Verification

The accompanying `check_latitude.py` constructs the unrestricted ambient and latitude fourth-moment Gram matrices on a full traceless-symmetric basis, using separate coordinate moment formulas rather than the three-block eigenvalue derivation. It diagonalizes their generalized eigenproblem in dimensions \(3\) through \(12\) for five rational squared heights per dimension, then tests the exact optimizer branches, eigenvalue crossings and grid upper bounds through dimension \(100\). It passed 834 assertions in the provided environment; these finite tests are cross-checks, not a replacement for the proof for all \(d\ge3\). Run `python check_latitude.py` with NumPy and SciPy installed.

## Relationship to prior work

Xiao and Zhuang (first publicly posted March 9, 2023) study spherical designs and spherical tight framelets for signal processing. Their continuous and discrete representation framework motivates stable measurement geometry but their analysis is not the present exact three-sector latitude trace spectrum and sharp dimension-dependent E-optimality statement. Nafees, Khalid, Kennedy, and McEwen (2017) optimize the conditioning of several discrete iso-latitude spherical harmonic transform matrices by an elimination scheme; those matrices, full low-pass spaces and discrete measurements are not the pure-degree-two continuous trace Gram operator here. The classical fourth-moment identity and the separation of spherical harmonics by latitude are used as known tools, not claimed as discoveries. Published results on equatorial traces of quadratic harmonics concern great subspheres with different normals, not a single nongeodesic latitude; their spectral conclusions do not imply the present latitude optimization.

## Limitations

The novel contribution asserted is the global E-optimal classification and dimension-four double optimum **within the precisely defined one-latitude observation family**, together with its exact normalization and full spectrum. Some component moment identities are standard. Earlier representation-theoretic or spherical experimental-design literature may contain an equivalent closed-form optimality classification; independent historical priority review has not been performed. The sample model is continuous and noiseless, and optimizes the lower frame bound under unit-probability measurement normalization. No global optimum among arbitrary spherical measures, finite point designs, wider harmonic bands, or other noise models is established.

## References

1. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, March 9, 2023; SIAM J. Imaging Sciences 16 (2023), 2072–2104. https://arxiv.org/abs/2303.05365
2. W. Nafees, Z. Khalid, R. A. Kennedy, J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497v1, September 8, 2017. https://arxiv.org/abs/1709.02497
3. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023v1, June 3, 2021; IEEE Trans. Signal Processing 70 (2022), 6142–6153. https://arxiv.org/abs/2106.02023
