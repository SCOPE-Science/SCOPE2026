# All-degree spectral and rank classification for icosahedral spherical-harmonic sampling

## Finding
Let \(X\) be the twelve vertices of a regular icosahedron on the unit sphere \(S^2\). For each integer \(\ell\ge0\), write \(\mathcal H_\ell\) for the complex spherical harmonics of *exact* degree \(\ell\), with norm from probability surface measure \(d\omega/(4\pi)\), and let \(E_\ell:\mathcal H_\ell\to\mathbb C^{12}\) be \((E_\ell f)_x=f(x)/\sqrt{12}\). Set \(p_\ell=P_\ell(1/\sqrt5)\), where \(P_\ell\) is the Legendre polynomial normalized by \(P_\ell(1)=1\).

The complete nonzero-capable squared singular spectrum of \(E_\ell\), including eigenvalues that may vanish at exceptional degrees, is as follows; an additional six zero eigenvalues occur on the parity-incompatible part of the twelve-dimensional sample space:

* If \(\ell\) is even, the two eigenvalues are \(\frac{2\ell+1}{6}(1+5p_\ell)\), multiplicity one, and \(\frac{2\ell+1}{6}(1-p_\ell)\), multiplicity five.
* If \(\ell\) is odd, they are \(\frac{2\ell+1}{6}(1+\sqrt5\,p_\ell)\) and \(\frac{2\ell+1}{6}(1-\sqrt5\,p_\ell)\), each with multiplicity three.

The exact rank is \(1\) at \(\ell=0\); \(3\) at \(\ell\in\{1,3\}\); \(5\) at \(\ell\in\{2,4,8,14\}\); and \(6\) at every other degree. In particular, **every degree \(\ell\ge15\) interpolates arbitrary sample data with the required antipodal parity**. Degree fourteen is the last failure, so this permanent-recovery threshold is sharp. When the six parity-compatible eigenvalues are positive, their extreme ratio gives the exact least-norm interpolation condition number; the ratio tends to one at rate \(O(\ell^{-1/2})\) after dividing out the common factor \((2\ell+1)/6\).

## Assumptions and scope
The twelve vertices are on a unit, centered *regular* icosahedron; orientations do not matter. The domain comprises one exact harmonic degree and is not a sum of degrees. All singular values are squared, and all normalization factors are fixed by the preceding definitions. Antipodal sample values obey \(y(-x)=(-1)^\ell y(x)\); their dimension is six. The rank refers to complex-linear evaluation; the real-harmonic version has the same rank.

## Proof
**Geometry and compressed kernel.** Write \(X=\{\pm u_1,\ldots,\pm u_6\}\) for unit representatives of the six antipodal axes. Directly from the coordinates \((0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\), divided by \(\sqrt{1+\varphi^2}\), with \(\varphi=(1+\sqrt5)/2\), we obtain \(|u_i\cdot u_j|=1/\sqrt5\) when \(i\ne j\), and \(\sum_i u_i u_i^{\mathsf T}=2I_3\). Hence \(C_{ii}=0\), \(C_{ij}=\sqrt5(u_i\cdot u_j)\) for \(i\ne j\) defines a real symmetric matrix satisfying \(C^2=5I_6\): indeed \(I_6+C/\sqrt5\) is the Gram matrix of the six unit vectors and has spectrum \(2^{[3]},0^{[3]}\). Thus \(C\) has eigenvalues \(\sqrt5\) and \(-\sqrt5\), each three times.

The spherical-harmonic addition formula in probability normalization is \(\sum_{m=-\ell}^{\ell}Y_{\ell m}(x)\overline{Y_{\ell m}(y)}=(2\ell+1)P_\ell(x\cdot y)\). Consequently \(E_\ell E_\ell^*\) has entries \((2\ell+1)P_\ell(x\cdot y)/12\). Parity makes its action vanish on six incompatible antipodal directions. Compressing to compatible orthonormal vectors \((e_{u_i}+(-1)^\ell e_{-u_i})/\sqrt2\) gives the six-by-six matrix \(\frac{2\ell+1}{6}(P_\ell(u_i\cdot u_j))_{i,j}\).

If \(\ell\) is even, the compressed matrix is \(\frac{2\ell+1}{6}[(1-p_\ell)I_6+p_\ell J_6]\), with one eigenvalue \(\frac{2\ell+1}{6}(1+5p_\ell)\) and five \(\frac{2\ell+1}{6}(1-p_\ell)\). If \(\ell\) is odd, the matrix is \(\frac{2\ell+1}{6}(I_6+p_\ell C)\), yielding the two stated threefold eigenvalues. Nonzero eigenvalues of \(E_\ell^*E_\ell\) and \(E_\ell E_\ell^*\) coincide, proving the spectral formula.

**Exhaustive exceptional-degree classification.** For even \(\ell\), rank loss occurs only at \(p_\ell=-1/5\) or \(p_\ell=1\); the latter equals one only for \(\ell=0\) because \(|P_\ell(t)|<1\) for \(\ell\ge1\), \(|t|<1\). For odd \(\ell\), loss occurs only when \(p_\ell=\pm1/\sqrt5\). The classical Bernstein bound, with \(\theta=\arccos(1/\sqrt5)\), gives for \(\ell\ge1\)
\[|P_\ell(1/\sqrt5)|<\sqrt{\frac{2}{\pi\ell\sin\theta}}=\sqrt{\frac{\sqrt5}{\pi\ell}}.\]
This is less than \(1/\sqrt5\) for every odd \(\ell\ge5\), and less than \(1/5\) for every even \(\ell\ge18\). Thus only a finite exact list remains. The Legendre three-term recurrence \((\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t)\), starting at \(P_0=1\), \(P_1=t\), yields \(p_1=1/\sqrt5\), \(p_3=-1/\sqrt5\), and for even degrees \(0,2,4,6,8,10,12,14,16\) respectively
\[1,-\tfrac15,-\tfrac15,\tfrac{41}{125},-\tfrac15,-\tfrac{131}{3125},\tfrac{3301}{15625},-\tfrac15,\tfrac{3223}{78125}.\]
These are the entire exceptional list. Rank six therefore holds for every \(\ell\ge15\), while degree fourteen has rank five.

**Interpolation cost.** When the six parity-compatible eigenvalues are positive, the pseudoinverse of \(E_\ell\) is bounded by their smallest square-root reciprocal, and this constant is attained on the associated eigenvector. The exact squared condition number is the ratio of the displayed largest to smallest positive eigenvalues. Bernstein's bound implies \(p_\ell=O(\ell^{-1/2})\), hence the two levels are asymptotically equal; their ratio is \(1+O(\ell^{-1/2})\). This proves asymptotic tightness on the six-dimensional compatible output space, not a uniform bound on reconstructing an arbitrary \((2\ell+1)\)-dimensional harmonic input.

## Verification
The accompanying independently assembled spherical-harmonic evaluation program computes the twelve vertices, their coordinate Gram matrix, and exact-degree harmonic values via associated Legendre functions. For each integer degree from zero through twenty-five, it compares all twelve numerical Gram eigenvalues to the closed spectrum, with absolute tolerance \(10^{-10}\). It also prints exact symbolic Legendre values for the finite list. The finite test does not establish the all-degree assertion, which follows from the stated analytic proof and Bernstein inequality.

## Relationship to prior work
Bannai, Okuda and Tagami (2013, arXiv:1308.5101, Introduction) explicitly identify the antipodal half-icosahedron as a harmonic-index design in degrees eight and fourteen; the lower-degree cancellations follow from its classical spherical five-design strength. These **known cancellations are not claimed as discoveries**. Their design criterion concerns vanishing sums of harmonics, not the present full six-dimensional evaluation Gram spectrum, its two-level singular values at every degree, or the sharp permanent interpolation threshold.

Bilbao-Ahedo and collaborators (2017, arXiv:1701.06617, Section 4.2 and Table 3) analyze finite-rank covariance matrices on icosahedron-derived grids. At the twelve base vertices they report numerical ranks of *sums* of degrees, including the degree-three block, but not the all-degree individual-level Gram formula or its all-degree exceptions. Khalid, Kennedy and McEwen (2014, arXiv:1403.4661) develop iso-latitude sampling of general bandlimited spherical signals, rather than this exact symmetric twelve-point operator. Zheng and Doerschuk (SIAM J. Math. Anal., doi:10.1137/S0036141098341770) construct symmetry-adapted icosahedral harmonics and are relevant potential prior art; their full paper was not accessible in this review.

## Limitations
The result is limited to a regular icosahedron and one fixed spherical-harmonic degree. Six compatible sample values do not identify the full harmonic of degree \(\ell\ge3\), whose dimension exceeds six; only its least-norm interpolation from those values is quantified. The Bernstein estimate bounds exceptional degrees but is not the optimal asymptotic constant. A potentially equivalent decomposition in early icosahedral representation-theory literature cannot be excluded from the available full-text evidence. The stated originality assessment is literature-limited and is not independent certification.

## References
1. Y. Zheng and P. C. Doerschuk, *Explicit Computation of Orthonormal Symmetrized Harmonics with Application to the Identity Representation of the Icosahedral Group*, SIAM J. Math. Anal. 32 (2000), 538–554. DOI: 10.1137/S0036141098341770. Publisher lists public online date 2006-08-01; full text was not available.
2. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (first posted 2013-08-23), especially page 3.
3. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (2014-03-19).
4. J. Bilbao-Ahedo et al., *On the regularity of the covariance matrix of a discretized scalar field on the sphere*, arXiv:1701.06617 (2017-01-23), Section 4.2, Table 3.
5. W. Gautschi and C. Giordano, *Luigi Gatteschi's work on asymptotics of special functions and their zeros*, Numer. Algorithms 49 (2008), Section 5.3, Bernstein inequality (56). DOI: 10.1007/s11075-008-9208-5 (public online date 2008-05-20).
6. N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Proc. Cambridge Philos. Soc. 54 (1958), 28–38. DOI: 10.1017/S0305004100033156 (full text not inspected).
