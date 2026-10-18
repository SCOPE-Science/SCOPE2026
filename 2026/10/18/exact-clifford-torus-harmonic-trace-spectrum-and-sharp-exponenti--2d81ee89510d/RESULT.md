# Exact Clifford-torus harmonic trace spectrum and sharp exponential inverse instability

## Finding

Let \(S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\}\) carry probability-normalized round measure, and let the Clifford torus
\[
T=\{(2^{-1/2}e^{i\alpha},2^{-1/2}e^{i\beta}):\alpha,\beta\in\mathbb R/2\pi\mathbb Z\}
\]
carry probability-normalized angular measure. For every integer \(L\ge1\), let \(\mathcal H_{<L}\) be the sum of the complex scalar spherical-harmonic eigenspaces of degrees \(0,1,\ldots,L-1\), with the inherited \(L^2(S^3)\) norm. Restrict functions to \(T\) using \(R_L:\mathcal H_{<L}\to L^2(T)\).

**Exact range, rank and ambiguity.** The range is precisely the Fourier diamond
\[
\mathcal V_L=\operatorname{span}\{e^{i(m\alpha+n\beta)}:m,n\in\mathbb Z,\ |m|+|n|<L\}.
\]
Thus
\[
\operatorname{rank}R_L=2L^2-2L+1,\qquad
\dim\ker R_L=\frac{L(L+1)(2L+1)}6-(2L^2-2L+1).
\]
In particular restriction is injective exactly for \(L=1,2\); for \(L\ge3\) it has a completely characterized, nonzero radial ambiguity.

**All positive singular values.** Put \(a=|m|\), \(b=|n|\), \(s=a+b<L\), and \(J=\lfloor(L-1-s)/2\rfloor\). For \(0\le j\le J\), define
\[
q_{a,b,j}=
\frac{(2j+s+1)\,j!\,(j+s)!}{(j+a)!\,(j+b)!}\,2^{-s}
\left[P_j^{(b,a)}(0)\right]^2,
\qquad
\lambda_{m,n}=\sum_{j=0}^{J}q_{a,b,j},
\]
where \(P_j^{(b,a)}\) is the standard Jacobi polynomial. The nonzero eigenvalues of \(R_LR_L^*\) are exactly \(\lambda_{m,n}\), one for each frequency in \(\mathcal V_L\), counted with multiplicity; all are positive rational numbers. Equivalently, with \(U_k\) the Chebyshev polynomial of the second kind,
\[
\lambda_{m,n}=[X^mY^n]\sum_{k=0}^{L-1}(k+1)U_k\!\left(\frac{X+X^{-1}+Y+Y^{-1}}4\right).
\]
The coefficient extraction is Laurent-polynomial coefficient extraction and supplies an independent exact formula.

**Sharp inverse instability.** At every \(L\ge1\),
\[
\min_{|m|+|n|<L}\lambda_{m,n}=\frac{L}{2^{L-1}},
\qquad \|R_L^\dagger\|=\sqrt{\frac{2^{L-1}}L}.
\]
Here \(R_L^\dagger\) is the minimum-norm right inverse from \(\mathcal V_L\) to \(\mathcal H_{<L}\). For \(L\ge3\), the minimum has multiplicity precisely four and is attained only at \((m,n)=(\pm(L-1),0),(0,\pm(L-1))\); at \(L=2\) all five eigenvalues equal one, and at \(L=1\) the sole eigenvalue is one. Thus exact recovery of every admissible trace is possible, but its worst-case noise amplification grows exponentially in the harmonic cutoff.

## Assumptions and scope

All spaces and operators are complex-linear. Both measures are normalized to total mass one. The degree cutoff is strict: only spherical harmonics of degree less than the integer \(L\) are retained. The adjoint and pseudoinverse use the specified Hilbert norms. The sampling surface is the single Clifford torus with equal complex-coordinate radii; the result neither reconstructs an arbitrary function on \(S^3\) from one torus nor asserts stability uniformly in \(L\).

Write Hopf coordinates \(z_1=\cos\theta\,e^{i\alpha}\), \(z_2=\sin\theta\,e^{i\beta}\) with \(0\le\theta\le\pi/2\). The normalized round measure is \(2\sin\theta\cos\theta\,d\theta\,d\alpha\,d\beta/(2\pi)^2\). The Clifford torus is \(\theta=\pi/4\).

## Proof

**1. Orthonormal Hopf harmonic basis.** For integers \(m,n\), let \(a=|m|\), \(b=|n|\), \(s=a+b\). At each integer \(j\ge0\) put
\[
\Phi_{m,n,j}(\theta,\alpha,\beta)=C_{a,b,j}
(\cos\theta)^a(\sin\theta)^b P_j^{(b,a)}(\cos2\theta)e^{i(m\alpha+n\beta)},
\]
where \(C_{a,b,j}>0\) is defined by
\[
C_{a,b,j}^2=\frac{(2j+s+1)j!(j+s)!}{(j+a)!(j+b)!}.
\]
The Hopf-coordinate Laplace operator is
\[
\Delta_{S^3}=\partial_\theta^2+(\cot\theta-\tan\theta)\partial_\theta
+\frac{\partial_\alpha^2}{\cos^2\theta}
+\frac{\partial_\beta^2}{\sin^2\theta}.
\]
Direct substitution of the Jacobi differential equation gives
\(\Delta_{S^3}\Phi_{m,n,j}=-(s+2j)(s+2j+2)\Phi_{m,n,j}\). Changing variables \(x=\cos2\theta\) in Jacobi orthogonality gives exactly
\[
\int_0^{\pi/2}2\sin\theta\cos\theta\,(\cos\theta)^{2a}(\sin\theta)^{2b}
[P_j^{(b,a)}(\cos2\theta)]^2\,d\theta
=\frac{(j+a)!(j+b)!}{(2j+s+1)j!(j+s)!}.
\]
Angular orthogonality and Jacobi orthogonality therefore make these \(\Phi_{m,n,j}\) orthonormal. At each degree \(k=s+2j\), the count of such functions is \((k+1)^2\), equal to the full spherical-harmonic multiplicity on \(S^3\), establishing completeness at that degree. Thus the basis of \(\mathcal H_{<L}\) consists exactly of the triples with \(s+2j<L\).

**2. Restriction and the complete singular spectrum.** At \(\theta=\pi/4\), the basis element becomes \(v_{a,b,j}\,e^{i(m\alpha+n\beta)}\) with real coefficient
\[
v_{a,b,j}=2^{-s/2}C_{a,b,j}P_j^{(b,a)}(0).
\]
For fixed \((m,n)\), the restriction matrix has one output Fourier coordinate and input coefficients \((v_{a,b,j})_{0\le j\le J}\). Its squared nonzero singular value is \(\sum_j|v_{a,b,j}|^2=\lambda_{m,n}\). The \(j=0\) coefficient is nonzero for every \(s<L\), because \(P_0=1\); no frequency with \(s\ge L\) occurs. This proves the range, full spectrum and rank after counting lattice points in the diamond:
\(1+\sum_{s=1}^{L-1}4s=2L^2-2L+1\). The stated nullity follows from \(\dim\mathcal H_{<L}=\sum_{k=0}^{L-1}(k+1)^2\). Within each frequency block the kernel consists of precisely those coefficient vectors orthogonal to \((v_{a,b,j})_j\); these blocks give the complete ambiguity description.

**3. The sharp minimum and its equality cases.** Retain only the nonnegative \(j=0\) contribution:
\[
\lambda_{m,n}\ge q_{a,b,0}=(s+1)2^{-s}\binom{s}{a}
\ge\frac{s+1}{2^s}.
\]
The function \((s+1)2^{-s}\) is nonincreasing on integers \(s\ge0\), strictly decreasing for \(s\ge1\). Since \(s\le L-1\), this yields \(\lambda_{m,n}\ge L2^{1-L}\). For \(s=L-1\), the only radial index is \(j=0\). The four axial modes with \(a=0\) or \(b=0\) have binomial coefficient one and attain this bound. For \(L\ge3\), every \(s<L-1\) gives strict inequality and at \(s=L-1\) every nonaxial mode gives a larger binomial coefficient. When \(L=2\), the constant and four first-order modes all have value one; \(L=1\) is scalar. This establishes all sharp equality cases.

**4. Reconstruction and noise amplification.** If \(g=\sum_{|m|+|n|<L}\widehat g(m,n)e^{i(m\alpha+n\beta)}\), its unique minimum-\(L^2(S^3)\)-norm extension is
\[
R_L^\dagger g=
\sum_{|m|+|n|<L}\frac{\widehat g(m,n)}{\lambda_{m,n}}
\sum_{j=0}^{\lfloor(L-1-|m|-|n|)/2\rfloor}
\overline{v_{|m|,|n|,j}}\,\Phi_{m,n,j}.
\]
Orthogonality gives \(\|R_L^\dagger g\|_2^2=\sum_{m,n}|\widehat g(m,n)|^2/\lambda_{m,n}\). Hence the operator norm is precisely \(\min\lambda_{m,n}^{-1/2}\), attained on the top axial Fourier modes (or every mode for \(L=1,2\)).

**5. Independent reproducing-kernel identity.** The spherical addition formula on \(S^3\), with probability normalization, is
\(K_k(x,y)=(k+1)U_k(x\cdot y)\) in the degree-\(k\) eigenspace. For torus points, \(x\cdot y=(\cos(\alpha-\alpha')+\cos(\beta-\beta'))/2\). Consequently \(R_LR_L^*\) is a convolution operator on the torus with kernel \(\sum_{k=0}^{L-1}(k+1)U_k((\cos u+\cos v)/2)\), so its Fourier eigenvalues are the displayed Laurent coefficients. This gives the second formula without using the Jacobi normalization.

## Verification

The included standalone `check_exact.py` uses exact rational arithmetic to compute the singular eigenvalues independently from (i) the Jacobi norm/evaluation formula and (ii) the Chebyshev addition-kernel Laurent coefficients. For every integer cutoff \(1\le L\le9\) and every admissible Fourier frequency, these agree identically. It additionally checks the range size, dimension trace \(\operatorname{tr}(R_LR_L^*)=\dim\mathcal H_{<L}\), sharp minimum, and its equality multiplicity. Run from the package directory with `python check_exact.py` using the standard library (the script does not require numerical approximations). The all-\(L\) statement is proved in the four arguments above; the finite checks are independent regression tests, not the infinite proof.

## Relationship to prior work

The scalar Hopf-harmonic basis and Jacobi normalization are classical; explicit coordinates and a mode basis are supplied in Ben Achour–Huguet–Queva–Renaud (2015). Dowker (2009) treats harmonics and the Hopf map on quotient three-spheres. Sampling theorems of Gräf–Potts (2009) and McEwen–Büttner–Leistedt–Peiris–Wiaux (2015) sample the full rotation group rather than fix one two-dimensional Clifford torus. Han (2024) analyzes semiclassical measures of special spherical harmonics supported along a family of Clifford tori, not the finite-band trace map. The result here is specifically the complete trace spectrum, exact Fourier-diamond range, optimal pseudoinverse and sharp exponential smallest singular value for this single torus; these statements are not supplied by those sources as stated. The proof deliberately derives the trace results from the classical basis instead of claiming the basis itself is new.

## Limitations

The only global new quantitative stability result asserted is the smallest positive singular value and its exact inverse norm; there is no formula for the largest positive singular value beyond the finite positive sums above. The theorem concerns exact restriction with normalized Hilbert norms, not finite noisy point sampling, arbitrary embedded tori, general metrics, or the recovery of coefficients inside the nullspace. A broader but unlocated general trace theorem could still subsume the claim; the literature comparison is substantial but cannot establish absolute global novelty. No independent mathematical audit has been performed.

## References

- J. S. Dowker, *Harmonics on the factored three-sphere and the Hopf map*, arXiv:0909.3380 (first submitted 2009-09-18), https://arxiv.org/abs/0909.3380.
- J. Ben Achour, E. Huguet, J. Queva, J. Renaud, *Explicit vector spherical harmonics on the 3-sphere*, arXiv:1505.03426 (first submitted 2015-05-13), especially Section II on scalar Hopf modes, https://arxiv.org/abs/1505.03426.
- M. Gräf and D. Potts, *Sampling sets and quadrature formulae on the rotation group*, TU Chemnitz preprint 8 (2009), https://www.tu-chemnitz.de/mathematik/preprint/2009/PREPRINT_08.php.
- J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris, Y. Wiaux, *A novel sampling theorem on the rotation group*, arXiv:1508.03101 (first submitted 2015-08-13), https://arxiv.org/abs/1508.03101.
- X. Han, *The semiclassical measure of certain spherical harmonics on the three-sphere*, arXiv:2411.08146 (first submitted 2024-11-12), https://arxiv.org/abs/2411.08146.
