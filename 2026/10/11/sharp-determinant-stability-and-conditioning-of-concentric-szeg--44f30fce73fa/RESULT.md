# Sharp determinant stability and conditioning of concentric Szegő orbit frames

## Finding
Fix an integer \(d\ge 2\) and a radius \(0<r<1\). For pairwise distinct points \(a_j=r e^{i\theta_j}\), with cyclically increasing real lifts \(\theta_0<\cdots<\theta_{d-1}<\theta_0+2\pi\), let \(B\) be the degree-\(d\) finite Blaschke product whose simple zeros are the \(a_j\). In \(H^2(\mathbb D)\), put
\[
 k_j(z)=\frac{\sqrt{1-r^2}}{1-\overline{a_j}z},
 \qquad \mathcal F_{\boldsymbol a}=\{B^n k_j:n\ge0,\ 0\le j<d\}.
\]
Then \(\mathcal F_{\boldsymbol a}\) is a Riesz basis. Write \(G_{\boldsymbol a}\) for the \(d\)-by-\(d\) Gram matrix of its seeds. Put \(\varepsilon_j=\theta_j-2\pi j/d\), \(\overline\varepsilon=d^{-1}\sum_j\varepsilon_j\), and
\[
 c_r=\frac{(1-r^2)^2}{4(1+r^2)^2}.
\]
Let \(G_{\mathrm{reg}}\) be the seed Gram matrix for any rotation of the regular \(d\)-gon of radius \(r\). The **sharp angular determinant-stability inequality** is
\[
 \boxed{\ \log\frac{\det G_{\mathrm{reg}}}{\det G_{\boldsymbol a}}
 \ \ge\ c_r d\sum_{j=0}^{d-1}(\varepsilon_j-\overline\varepsilon)^2.\ }
\]
Equality occurs precisely for a rotated regular polygon. For every fixed \(r\), the positive coefficient \(c_r\) cannot be increased in an inequality valid for all \(d\ge2\) and all angular configurations.

For a regular polygon, the entire seed Gram spectrum (and therefore the exact optimal lower/upper Riesz and frame bounds of the infinite orbit system) is
\[
 \boxed{\ \lambda_\ell=\frac{d(1-r^2)r^{2\ell}}{1-r^{2d}},\qquad
 0\le\ell<d.\ }
\]
Hence \(A_{d,r}=\lambda_{d-1}\), \(U_{d,r}=\lambda_0\), \(U_{d,r}/A_{d,r}=r^{-2(d-1)}\), and
\[
 \boxed{\ \det G_{\mathrm{reg}}=\left(\frac{d(1-r^2)}{1-r^{2d}}\right)^d r^{d(d-1)}.\ }
\]
In particular, for any sequence of radii \(0<r_d<1\), the corresponding regular-polygon orbit bases have frame bounds uniformly bounded above and away from zero as \(d\to\infty\) if and only if \(\sup_{d\ge2}d(1-r_d)<\infty\).

## Assumptions and scope
The Hardy norm is \(\|\sum_{n\ge0}c_n z^n\|_{H^2}^2=\sum_{n\ge0}|c_n|^2\). Every seed is the *raw normalized Szegő kernel* at a zero, with no Gram--Schmidt or Malmquist--Walsh orthogonalization. For nonregular configurations, \(B\) is any unimodular multiple of the finite Blaschke product of the displayed zeros; its phase does not affect Riesz constants or determinants. The lifts \(\theta_j\) must be ordered cyclically, with \(\theta_{j+d}=\theta_j+2\pi\); the centered deviation sum is invariant under an overall rotation and cyclic relabeling. All determinants are of the finite seed Gram, rather than a nonexistent determinant of an infinite operator. The dimensional bound is stated only for \(d\ge2\), and \(r=0,1\) are excluded.

## Proof
**1. Orbit reduction to the seed Gram.** For a finite Blaschke product \(B\), the model space \(K_B=H^2\ominus BH^2\) has dimension \(d\): the one-factor case follows from \(BH^2=\{f:f(a)=0\}\), and the identity \(K_{UV}=K_U\oplus U K_V\) inducts over the factors. Since \(B(a_j)=0\), each \(k_j\) belongs to \(K_B\). The normalized Szegő-kernel Cauchy determinant identity below is positive for distinct nodes, so these \(d\) vectors form a basis of \(K_B\). Inner multiplication is isometric; furthermore \(\bigcap_{n\ge0}B^nH^2=\{0\}\), because membership forces a zero of every order at any zero of \(B\). Thus
\[
 H^2=\bigoplus_{n\ge0}B^nK_B
\]
orthogonally. Each orbit block has exactly seed Gram \(G_{\boldsymbol a}\), so the union is a Riesz basis with the seed Gram's extremal eigenvalues as its optimal frame and Riesz bounds.

**2. Exact determinant.** For arbitrary distinct disk points, the standard Cauchy double-alternant identity and normalization give
\[
 \det G_{\boldsymbol a}=\prod_{0\le i<j<d}
 \left|\frac{a_i-a_j}{1-\overline{a_i}a_j}\right|^2>0.
\]
Let
\[
 L_r(t)=\log\frac{2r\sin(t/2)}{|1-r^2e^{it}|},\qquad 0<t<2\pi.
\]
The function satisfies \(L_r(2\pi-t)=L_r(t)\). For \(\theta_{j+d}=\theta_j+2\pi\) and \(\Delta_{j,k}=\theta_{j+k}-\theta_j\), each unordered pair appears twice in the double sum, yielding the exact expression
\[
 \log\det G_{\boldsymbol a}=\sum_{k=1}^{d-1}\sum_{j=0}^{d-1}L_r(\Delta_{j,k}).
\]

**3. Uniform curvature and angular rigidity.** Write \(u=t/2\), \(A=(1-r^2)^2\), and \(Q=4r^2\). Direct differentiation of
\[
 L_r(t)=\log(2r\sin u)-\tfrac12\log(A+Q\sin^2u)
\]
gives
\[
 -L_r''(t)=\frac A4\left(
 \frac1{\sin^2u\,(A+Q\sin^2u)}
 +\frac{2Q\cos^2u}{(A+Q\sin^2u)^2}\right)
 \ge\frac A{4(A+Q)}=c_r.
\]
Equality in the curvature estimate occurs only at \(t=\pi\). Also \(\sum_j\Delta_{j,k}=2\pi k\). Strong Jensen concavity of \(L_r\) therefore gives
\[
 \sum_jL_r(\Delta_{j,k})\le
 d L_r(2\pi k/d)-\frac{c_r}{2}\sum_j
 (\Delta_{j,k}-2\pi k/d)^2.
\]
For \(\varepsilon_{j+d}=\varepsilon_j\), the exact finite identity
\[
 \sum_{k=1}^{d-1}\sum_j(\varepsilon_{j+k}-\varepsilon_j)^2
 =2d\sum_j(\varepsilon_j-\overline\varepsilon)^2
\]
follows by expanding squares and summing all ordered pairs. Since \(\Delta_{j,k}-2\pi k/d=\varepsilon_{j+k}-\varepsilon_j\), summing the strong-Jensen estimates over \(k\) proves the claimed global inequality. The right side is zero only for constant centered deviations, which are precisely the regular configurations; otherwise the inequality is strict.

**4. Optimality of the stability coefficient.** For \(d=2\), take \(\theta_0=0\), \(\theta_1=\pi+h\), with \(h\to0\). Then \(d\sum_j(\varepsilon_j-\overline\varepsilon)^2=h^2\). The exact determinant relation gives
\[
 \log\frac{\det G_{\mathrm{reg}}}{\det G_{\boldsymbol a}}
 =2\bigl[L_r(\pi)-L_r(\pi+h)\bigr]
 =c_r h^2+O_r(h^4),
\]
because \(L_r'(\pi)=0\) and \(-L_r''(\pi)=c_r\). No larger coefficient works uniformly in the allowed degrees and angles.

**5. Complete regular spectrum.** Put \(\omega=e^{2\pi i/d}\) and \(a_j=r\omega^j\). With a consistent Gram convention,
\[
 (G_{\mathrm{reg}})_{ij}
 =\frac{1-r^2}{1-r^2\omega^{i-j}}
 =(1-r^2)\sum_{n\ge0}r^{2n}\omega^{n(i-j)}.
\]
The cyclic Fourier vector \((\omega^{\ell j})_{j=0}^{d-1}\) has eigenvalue
\[
 d(1-r^2)\sum_{s\ge0}r^{2(\ell+sd)}
 =\frac{d(1-r^2)r^{2\ell}}{1-r^{2d}}.
\]
Their product proves the determinant formula. The smallest and largest eigenvalues are the optimal bounds by Step 1. The condition number is \(r^{-2(d-1)}\). Since the eigenvalues have arithmetic mean one (unit diagonal), uniform two-sided frame bounds are equivalent to a uniform condition number. Finally \(\sup_d r_d^{-2(d-1)}<\infty\) is equivalent to \(\sup_d d(1-r_d)<\infty\): use \(1-r\le-\log r\), and for sufficiently large \(d\) in the bounded regime use \(-\log r\le 2(1-r)\) when \(r\ge1/2\). Finitely many small degrees have positive fixed bounds.

## Verification
The standalone Python 3 file `verify_szego_ring.py` runs finite numerical checks of the displayed Gram matrix and full discrete-Fourier spectrum for 32 degree/radius instances; compares determinant and stability inequalities for 945 random circular configurations; and tests the quadratic-sharpness limit for three radii. It printed `PASS: 32 regular spectra, 945 jittered configurations, 3 sharpness sequences`. Run `python verify_szego_ring.py` with the standard library. The proof above, not the finite tests, establishes all-degree correctness.

## Relationship to prior work
Aguilera and Carando [1, Theorem 2.6 and Example 2.7] show that a degree-\(d\) Blaschke multiplier admits orbit bases using a *Malmquist--Walsh orthonormal generator set*. That existence theorem does not supply the conditioning, optimal radius-constrained positions, or universal sharp jitter penalty for the **unorthogonalized point-evaluation kernels** analyzed here. Karvonen, Särkkä and Tanaka [2] motivate kernel-determinant Fekete designs but treat an approximate construction and a Gaussian real-variable case, rather than this exact Hardy-model-space orbit Gram. Broader classical Fekete-energy or circle-concavity results could yield the placement part; the specific quantitative constant and exact orbit conditioning are the distinct comparison points. The angle-Jensen mechanism and kernel determinant formula are classical ingredients; novelty is not claimed for those ingredients individually.

## Limitations
This theorem is restricted to distinct simple zeros on one circle, raw normalized Szegő seeds, and multiplication by the corresponding finite Blaschke product. D-optimality means maximizing the determinant; it does **not** assert that the regular configuration maximizes the smallest eigenvalue or minimizes the spectral condition number among every irregular configuration. It does not cover repeated zeros, mixed radii, weighted Hardy spaces or multivariate Hardy spaces. The all-degree analytic argument is not an independently audited proof. Existing unindexed equivalent circle-energy results are a residual originality risk.

## References
[1] A. Aguilera and D. Carando, *Frames of orbits of multiplication operators on Hardy spaces*, arXiv:2606.00912v1, 30 May 2026, https://arxiv.org/abs/2606.00912.

[2] T. Karvonen, S. Särkkä, and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, Numerical Algorithms 87 (2021), 445–468; arXiv:1912.07316, https://arxiv.org/abs/1912.07316.

[3] M. Gaál, B. Nagy, Z. Nagy-Csiha, and Sz. Gy. Révész, *Minimal Energy Point Systems on the Unit Circle and the Real Line*, SIAM J. Math. Anal. 52 (2020), 6281–6296, https://doi.org/10.1137/19M1302971.
