# Exact singular spectrum of half-turn restriction on \(SO(3)\)

## Finding
For each integer \(L\ge 1\), let \(\mathcal B_L\) be the space of complex functions on \(SO(3)\) with Wigner degrees \(0\le \ell<L\). Give \(SO(3)\) Haar probability measure. For an unoriented axis \([u]\in\mathbb{RP}^2\), put \(H_u=2uu^{\mathsf T}-I_3\) and let
\[
T_L:\mathcal B_L\longrightarrow L^2(\mathbb{RP}^2),\qquad T_Lf([u])=f(H_u),
\]
with rotation-invariant probability measure on \(\mathbb{RP}^2\). The operator has image exactly the even spherical harmonics of degrees \(0,2,\ldots,2L-2\), rank \(2L^2-L\), and nullity \(2L(L-1)(2L-1)/3\). Its positive squared singular values, with all multiplicities, are
\[
\lambda_{L,j}=\frac12\int_{-1}^{1} C^{(2)}_{2L-2}(t)P_{2j}(t)\,dt
\quad\text{with multiplicity }4j+1,\qquad 0\le j<L.
\]
Here \(P_k\) is the usual Legendre polynomial, and \(C_k^{(2)}\) is the Gegenbauer polynomial normalized by \((1-2tz+z^2)^{-2}=\sum_{k\ge0}C_k^{(2)}(t)z^k\). For \(L\ge2\), these levels are **strictly ordered**, and for every \(L\ge1\) their endpoints are
\[
\lambda_{L,0}=L,\qquad
\lambda_{L,L-1}=\frac{(2L-1)2^{4L-4}}{(4L-3)\binom{4L-4}{2L-2}}>0.
\]
Thus half-turn data determine precisely the \(2L^2-L\) visible degrees of freedom; the optimal condition number on \((\ker T_L)^\perp\) is
\[
\kappa_L=\sqrt{\frac{L(4L-3)\binom{4L-4}{2L-2}}{(2L-1)2^{4L-4}}}
\sim\left(\frac{2L}{\pi}\right)^{1/4}.
\]
The rank, nullity, and condition number refer to these normalized Hilbert-space measures, not a discretization of the axis space.

## Assumptions and scope
Every \(f\in\mathcal B_L\) is a finite sum of the matrix coefficients \(D_{mn}^{\ell}\), with integers \(0\le\ell<L\) and \(-\ell\le m,n\le\ell\). Under Haar probability, \(\sqrt{2\ell+1}D_{mn}^{\ell}\) are orthonormal. Hence
\[
\dim\mathcal B_L=\sum_{\ell=0}^{L-1}(2\ell+1)^2=(4L^3-L)/3.
\]
The axis identification \(u\sim-u\) is essential because \(H_u=H_{-u}\). On the sphere, the measure of an even function is \((4\pi)^{-1}\int_{S^2}f(u)\,d\omega(u)\), which is equivalent to probability measure on the quotient. All singular values refer to the complex Hilbert-space operator; restricting to real-valued signals does not change these numerical levels.

## Proof
**1. Reproducing kernel.** Peter–Weyl orthogonality makes the reproducing kernel of \(\mathcal B_L\)
\[
K_L(g,h)=\sum_{\ell=0}^{L-1}(2\ell+1)\chi_\ell(gh^{-1}),
\]
where \(\chi_\ell\) is the character of the \((2\ell+1)\)-dimensional irreducible representation. Therefore \(T_LT_L^*\) acts on \(L^2(\mathbb{RP}^2)\) through the kernel \(K_L(H_u,H_v)\), with no additional scale factor.

**2. Half-turn character identity.** The product of half-turns around axes \([u]\) and \([v]\) has rotation half-angle with cosine \(|u\cdot v|\). The \(SO(3)\) character identity \(\chi_\ell(R_\theta)=U_{2\ell}(\cos(\theta/2))\) therefore gives
\[
\chi_\ell(H_uH_v)=U_{2\ell}(u\cdot v),
\]
where \(U_k(\cos\theta)=\sin((k+1)\theta)/\sin\theta\), and evenness removes the absolute value. The elementary Chebyshev sum and derivative identities
\[
\sum_{\ell=0}^{L-1}T_{2\ell+1}(t)=\tfrac12U_{2L-1}(t),\qquad T_k'(t)=kU_{k-1}(t),
\]
imply
\[
K_L(H_u,H_v)=\sum_{\ell=0}^{L-1}(2\ell+1)U_{2\ell}(u\cdot v)
=\tfrac12 U_{2L-1}'(u\cdot v)=C^{(2)}_{2L-2}(u\cdot v).
\]
The final identity also follows directly by differentiating the generating function for \(U_k=C_k^{(1)}\): \(\frac{d}{dt}C_n^{(1)}=2C_{n-1}^{(2)}\).

**3. Complete eigenvalue and rank decomposition.** The kernel is an even polynomial of degree \(2L-2\). The probability-normalized Funk–Hecke formula applied to the spherical harmonic \(Y_{km}\) gives its eigenvalue \(\frac12\int_{-1}^{1}C_{2L-2}^{(2)}(t)P_k(t)\,dt\). Odd degrees do not descend to \(\mathbb{RP}^2\), and orthogonality forces vanishing for even \(k>2L-2\). The remaining multiplicities are \(4j+1\). Steps 4 and 5 prove every one of these levels is positive, so the range equals the full even-degree band. Hence
\[
\operatorname{rank}T_L=\sum_{j=0}^{L-1}(4j+1)=2L^2-L,
\]
and subtracting from \(\dim\mathcal B_L\) yields the stated nullity.

**4. Strict order.** Integrating \(C^{(2)}_{2L-2}=U_{2L-1}'/2\), and using \(U_{2L-1}(1)=2L\) and \(U_{2L-1}(-1)=-2L\), gives \(\lambda_{L,0}=L\). For \(0\le j<L-1\), integration by parts (the boundary term vanishes because \(P_{2j}(\pm1)=P_{2j+2}(\pm1)=1\)), together with \(P'_{2j+2}-P'_{2j}=(4j+3)P_{2j+1}\), yields
\[
\lambda_{L,j}-\lambda_{L,j+1}=\frac{4j+3}{4}\int_{-1}^{1}U_{2L-1}(t)P_{2j+1}(t)\,dt.
\]
Write \(t=\cos\theta\). The integral becomes \(\int_0^\pi\sin(2L\theta)P_{2j+1}(\cos\theta)\,d\theta\). For every \(m\ge0\), the finite Fourier expansion
\[
P_m(\cos\theta)=4^{-m}\sum_{r=0}^{m}\binom{2r}{r}\binom{2(m-r)}{m-r}\cos((m-2r)\theta)
\]
has positive coefficients; it follows by comparing the coefficient of \(z^m\) in \((1-2z\cos\theta+z^2)^{-1/2}=(1-ze^{i\theta})^{-1/2}(1-ze^{-i\theta})^{-1/2}\). Here \(m=2j+1\le2L-3\), and every frequency \(k=m-2r\) is odd with \(|k|<2L\), so
\[
\int_0^\pi\sin(2L\theta)\cos(k\theta)\,d\theta
=\frac{4L}{4L^2-k^2}>0.
\]
Thus every consecutive difference is strictly positive. This argument is valid also for the smallest nontrivial bandwidth \(L=2\); for \(L=1\), the ordering contains one level and is vacuous.

**5. Positive bottom level.** Put \(n=2L-2\). The top-degree Legendre coefficient of \(C_n^{(2)}\) is the quotient of their leading coefficients,
\[
\frac{(n+1)2^n}{2^{-n}\binom{2n}{n}}=
\frac{(n+1)2^{2n}}{\binom{2n}{n}}.
\]
Because Legendre polynomials are orthogonal and \(\frac12\int_{-1}^{1}P_n^2=1/(2n+1)\), this coefficient divided by \(2n+1\) is precisely \(\lambda_{L,L-1}\). It is strictly positive, and step 4 then proves all levels strictly positive. Finally, the condition number follows by taking the square root of the largest-to-smallest eigenvalue ratio. The asymptotic follows from \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\).

**6. Minimum-norm reconstruction.** Let \(Q_{2j}\) be orthogonal projection to the degree-\(2j\) spherical harmonic subspace on \(\mathbb{RP}^2\). For any data \(y\) in the range,
\[
f_{\min}=T_L^*\left(\sum_{j=0}^{L-1}\lambda_{L,j}^{-1}Q_{2j}y\right)
\]
is the unique reconstruction of smallest \(L^2(SO(3))\) norm. Every other signal with these data differs from it by an arbitrary element of \(\ker T_L\).

## Verification
The included `checker.py` uses only Python standard-library exact fractions and polynomial recurrences. Running `python3 checker.py` checks the character-kernel identity, all rational eigenvalue integrals, strict ordering, bottom-level formula, eigenvalue trace, and rank for \(1\le L\le12\). In particular, it obtains eigenvalue lists \((2,8/5)\) for \(L=2\) and top and bottom levels \(3,128/63\) for \(L=3\). These **finite** checks are corroboration only; the proof for every \(L\ge1\) is analytic in Steps 1–6.

## Relationship to prior work
Bernstein and Pesenson study the rotational Radon transform and reconstruction from averages over one-dimensional rotation fibers, with data indexed by pairs of directions; their exact bandlimited reconstruction is not the trace on the half-turn conjugacy class. McEwen and collaborators derive a full \(SO(3)\) equiangular sampling theorem recovering every Wigner coefficient from approximately cubic-in-bandwidth samples; they do not give the rank, exact trace spectrum, or conditioning for data restricted to the half-turn surface. The standard Peter–Weyl and Funk–Hecke identities are essential prior tools, but by themselves do not state the strictly decreasing closed-spectrum law and its sharp polynomial condition-number scaling for this natural conjugacy-class restriction. General compact-group Fourier restriction inequalities concern different norms and often different sets. Published results on conjugacy-class sampling of finite permutation groups have a different underlying group and representation space. No claim is made that abstract reproducing-kernel or trace-operator frameworks are new.

## Limitations
Half-turn data do **not** determine an arbitrary bandlimited function on \(SO(3)\); they determine only the orthogonal quotient by the explicitly dimensioned nullspace. No finite quadrature or finite axis set is specified, and no claim about noisy discrete sampling is made. The spectral decomposition assumes the full Wigner band and the probability normalizations above. Possible historical equivalent formulas from general representation-theoretic trace or spherical polynomial theory remain a residual bibliographic risk; the references below and contemporary published results were compared by the actual operators and implications. Independent verification has not been performed.

## References
- S. Bernstein and I. Z. Pesenson, *The Radon transform on SO(3): motivations, generalizations, discretization*, arXiv:1210.2652, first public version 2012-10-09, https://arxiv.org/pdf/1210.2652.
- J. D. McEwen et al., *A novel sampling theorem on the rotation group*, arXiv:1508.03101, first public version 2015-08-13, https://arxiv.org/html/1508.03101v2.
- Y. Zhang, *On Fourier restriction type problems on compact Lie groups*, arXiv:2005.11451, 2020, https://arxiv.org/html/2005.11451v5 (later contextual literature, not the archive-dating source).
- Standard mathematical identities used explicitly above: Peter–Weyl orthogonality and character formula for \(SO(3)\); Funk–Hecke formula for probability-normalized sphere; Legendre polynomial recurrence, orthogonality, and cosine expansion.
