# Exact Nyquist resolvent amplification and singular-value curvature for a phase-fitted Helmholtz scheme

## Finding
For the Bernoulli phase-fitted (BPF) one-dimensional Helmholtz discretization with zero discrete impedance data, the **entire interior source-to-solution Green matrix** is explicit. With the conventions defined below, for each integer \(n\ge 2\), \(m=n-1\), and mesh phase \(0<s<\pi\), it is
\[
G_{n,s}(i,j)=-\frac{h^2}{2\mathrm{i}\,\Theta(s)\sin s}\,e^{-\mathrm{i}s|i-j|},\qquad 1\le i,j\le m.
\]
Its Frobenius norm is exactly
\[
\|G_{n,s}\|_{\mathrm F}=\frac{m h^2}{2\Theta(s)\sin s}.
\]
Furthermore, writing \(\delta=\pi-s\) and keeping \(n\) fixed while \(\delta\downarrow0\), its sharp Euclidean source-to-interior-solution norm obeys
\[
\|G_{n,s}\|_2=\frac{m h^2}{2\Theta(s)\sin s}\left[1-\frac{(m^2-1)(2m^2+7)}{90m^2}\,\delta^2+O_m(\delta^4)\right].
\]
In particular, with \(h=L/n\) and \(k=s/h\),
\[
\boxed{\lim_{s\uparrow\pi}(\pi-s)\,k\|G_{n,s}\|_2=\frac{2L}{\pi}\left(1-\frac1n\right).}
\]
Thus the **optimal fixed-mesh source stability constant** has a first-order, not second-order, Nyquist pole. The quadratic coefficient above exactly measures the first separation of the operator norm from the Frobenius upper bound. These are fixed-mesh statements; the remainder is not asserted uniform in \(n\).

## Assumptions and scope
Fix a physical interval length \(L>0\), an integer \(n\ge2\), spacing \(h=L/n\), real wavenumber \(k>0\), and phase \(s=kh\in(0,\pi)\). The interior data are arbitrary complex values \(f_1,\ldots,f_{n-1}\); both impedance data are zero. Set
\[
\Theta(s)=\frac{s^2}{4\sin^2(s/2)}.
\]
The BPF equations of Jüngel, Li, Sun, and Zhang, using their phase-fitted representation, are
\[
\Theta(s)\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}+k^2u_i=f_i\quad (1\le i\le n-1),
\]
with \(D_k^+u_0=D_k^-u_n=0\). In this nondegenerate range these discrete impedance conditions are equivalently
\[
u_1=e^{\mathrm{i}s}u_0,\qquad u_{n-1}=e^{\mathrm{i}s}u_n.
\]
Here \(G_{n,s}\in\mathbb C^{(n-1)\times(n-1)}\) maps \(f=(f_i)\) to the *interior* vector \((u_i)\). Its Euclidean operator norm is also the induced norm for the source and solution discrete \(L^2\) norm \(\|v\|_{0,h}=(h\sum_{i=1}^{n-1}|v_i|^2)^{1/2}\), since the same factor \(\sqrt h\) occurs on each side. The Frobenius norm is used as an auxiliary, explicitly calculable matrix norm, not as a claim about the worst single source.

## Proof
**Exact discrete Green kernel.** Dividing the interior equation by \(\Theta/h^2\), and using \(s^2/\Theta(s)=4\sin^2(s/2)=2-2\cos s\), gives
\[
u_{i+1}-2\cos(s)u_i+u_{i-1}=\frac{h^2}{\Theta(s)}f_i.
\]
For every fixed source index \(j\), the sequence \(e^{-\mathrm{i}s|i-j|}\) satisfies the homogeneous three-point recurrence at all \(i\ne j\) and both discrete radiation conditions. At \(i=j\), its recurrence defect is \(2e^{-\mathrm{i}s}-2\cos s=-2\mathrm{i}\sin s\). Multiplying by \(-h^2/(2\mathrm{i}\Theta\sin s)\) therefore produces the unit point source. The homogeneous recurrence has the two linearly independent solutions \(e^{\pm\mathrm{i}si}\); the left condition eliminates the left-incoming coefficient and the right condition eliminates the other, because \(\sin s\ne0\). This also proves uniqueness and hence identifies the full inverse \(G_{n,s}\).

**Frobenius identity and sharp leading constant.** Every entry of the Toeplitz phase matrix \(K_m(s)=(e^{-\mathrm{i}s|i-j|})_{ij}\) has modulus one. Its \(m^2\) entries give \(\|K_m(s)\|_{\mathrm F}=m\), proving the exact Frobenius identity. Conjugating \(K_m(\pi-\delta)\) by the diagonal unitary with entries \((-1)^i\) gives
\[
K_m(\delta)=(e^{\mathrm{i}\delta|i-j|})_{1\le i,j\le m}.
\]
At \(\delta=0\), this equals the all-ones matrix \(J\), whose unique nonzero singular value is \(m\). Continuity shows \(\|K_m(\delta)\|_2/m\to1\). Since \(\Theta(\pi)=\pi^2/4\), \(\sin(\pi-\delta)/\delta\to1\), and \(k=s/h\), the boxed limit follows with the constant \(2mh/\pi=2L(1-1/n)/\pi\).

**Exact quadratic singular-value curvature.** Let \(D_{ij}=|i-j|\), \(F_{ij}=|i-j|^2\), and let \(\mathbf 1\) be the all-ones vector. The analytic expansion in \(\delta\) is
\[
K_m(\delta)=J+\mathrm{i}\delta D-\tfrac12\delta^2F+O_m(\delta^3).
\]
For the Hermitian square \(H(\delta)=K_m(\delta)K_m(\delta)^*\),
\[
H(0)=mJ,\quad H_1=\mathrm{i}(DJ-JD),\quad H_2=D^2-\tfrac12(FJ+JF),
\]
where \(D^2\) denotes matrix multiplication. The simple leading eigenvalue of \(H(0)\) is \(m^2\), with normalized eigenvector \(v=\mathbf1/\sqrt m\); all other eigenvalues are zero. Put \(r=D\mathbf1\) and \(R=\mathbf1^{\mathsf T}r\). Standard second-order perturbation of this isolated Hermitian eigenvalue, or direct projection of the eigenvalue equation onto \(v\) and \(v^\perp\), gives
\[
\lambda_2=v^*H_2v+\frac{\|H_1v\|^2}{m^2}
=\frac2m\sum_{i=1}^m r_i^2-\frac{R^2}{m^2}-\sum_{i,j=1}^m(i-j)^2.
\]
The requisite exact finite sums, valid also for \(m=1\), are
\[
R=\frac{m(m^2-1)}3,\qquad
\sum_i r_i^2=\frac{m(m^2-1)(7m^2-8)}{60},\qquad
\sum_{i,j}(i-j)^2=\frac{m^2(m^2-1)}6.
\]
They follow by summing \(r_i=[i(i-1)+(m-i)(m-i+1)]/2\). Substitution yields
\[
\lambda_2=-\frac{(m^2-1)(2m^2+7)}{45}.
\]
The singular-value maximum is the square root of the simple analytic eigenvalue \(m^2+\lambda_2\delta^2+O_m(\delta^4)\). Its odd Taylor coefficients vanish because \(K_m(-\delta)=\overline{K_m(\delta)}\), so \(H(-\delta)\) and \(H(\delta)\) have identical eigenvalues. Taking the square root establishes the displayed curvature coefficient. For \(m=1\), the coefficient is zero and the expansion is exact.

## Verification
The included `verify.py` checks all three nontrivial integer-sum formulas and the perturbation coefficient with exact rational arithmetic for \(1\le m\le127\). It also solves the original boundary-value linear system and compares the result against the Green-matrix product for 80 combinations of mesh dimensions and nonresonant phases, checks 80 Frobenius identities, and tests 35 singular-value asymptotic instances. Executing `python verify.py` with NumPy prints a PASS summary. These numerical tests are supplementary: the proof of the infinite limiting statement rests on the exact recurrence and perturbation calculation, not on finite samples.

## Relationship to prior work
The BPF method is defined by Jüngel, Li, Sun, and Zhang, arXiv:2605.21144, Section 2. Their Theorem 3.1 establishes a \(k\)-explicit \(L^2\) source stability bound, but its displayed coefficient \(A_0(s,ns)\) contains a \(\sec^2(s/2)\) term; at fixed \(n\), that available bound grows as \(O((\pi-s)^{-2})\). The present calculation gives the *optimal* source-only norm, proves its sharp \((\pi-s)^{-1}\) law, and finds a mesh-dependent quadratic correction. Thus it strengthens a particular stability estimate in a previously excluded singular limit; it neither replaces nor negates the method's other results.

The phase matrix is an instance of the complex-symmetric Kac–Murdock–Szegő matrix \(K_m(\rho)=(\rho^{|i-j|})\), with \(\rho=e^{-\mathrm{i}s}\). Prior literature already recognizes its rank-one value at \(\rho=-1\), and analyzes its **ordinary eigenvalues** for complex \(\rho\). The present claim is neither the invention of this Toeplitz matrix nor a general eigenvalue statement: it identifies its **largest singular value** to second order at a unit-modulus phase, and translates it into a sharp physical-source resolvent bound for the BPF impedance scheme. Known complex-parameter ordinary eigenvalues alone do not determine the singular norm of this generally nonnormal matrix.

## Limitations
The operator uses zero discrete impedance data, uniform one-dimensional grids, exact arithmetic, and the BPF equations as stated. The mesh size \(n\) is fixed in the Nyquist expansion; the \(O_m(\delta^4)\) remainder is not uniform over growing meshes. The proof does not bound floating-point error, solve variable-coefficient Helmholtz problems, or establish a corresponding bound in dimensions two or higher. The calculation does not assert that no older Green-function or complex-Toeplitz reference could imply the same explicit coefficient. Independent mathematical verification has not been performed.

## References
1. A. Jüngel, P. Li, Z. Sun, Z. Zhang, *A Bernoulli Phase-Fitted finite difference method with wavenumber-explicit analysis for the Helmholtz problem*, arXiv:2605.21144, first submitted 2026-05-20, Sections 2–3, especially equations (2.3)–(2.5) and Theorem 3.1. https://arxiv.org/abs/2605.21144
2. G. Fikioris, *Spectral properties of Kac–Murdock–Szegő matrices with a complex parameter*, Linear Algebra and its Applications 553 (2018), 182–210; arXiv:1804.08140. https://arxiv.org/abs/1804.08140
3. G. Fikioris and T. K. Mavrogordatos, *Double, borderline, and extraordinary eigenvalues of Kac–Murdock–Szegő matrices with a complex parameter*, Linear Algebra and its Applications 575 (2019); arXiv:1812.06437. https://arxiv.org/abs/1812.06437
4. N. J. Higham, *What Is the Kac–Murdock–Szegő Matrix?*, 2021. https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/
