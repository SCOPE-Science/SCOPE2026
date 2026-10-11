# Sharp range–valence constant for finite-point Schwarz–Pick matrices

## Finding

Fix integers \(n,m\ge1\) and \(0<\rho\le1\). Suppose \(f:\mathbb D\to\rho\mathbb D\) is holomorphic and at most \(m\)-valent, counting multiplicities. For an arbitrary tuple \(Z=(z_1,\ldots,z_n)\in\mathbb D^n\), form the Hermitian matrices
\[
G_Z=\left[\frac1{(1-z_i\overline{z_j})^2}\right]_{i,j=1}^n
\]
and
\[
H_{f,Z}=\left[\frac{f'(z_i)\overline{f'(z_j)}}{(1-f(z_i)\overline{f(z_j)})^2}\right]_{i,j=1}^n.
\]
Then the **optimal universal constant** for this family is
\[
\boxed{H_{f,Z}\preceq \rho^2\min\{n,m\}\,G_Z.}
\]
That is, if \(C_{n,m}(\rho)\) is the smallest constant valid for every map and tuple under these hypotheses, then
\[
\boxed{C_{n,m}(\rho)=\rho^2\min\{n,m\}.}
\]

No properness, surjectivity, or inner-function condition is required. The class includes non-surjective maps of finite valence, which the degree-refined portion of the initiating theorem does not address.

The constant is optimal already among the elementary maps
\[
f(z)=\rho z^d,\qquad d=\min\{n,m\}.
\]
For \(\rho<1\), a family of \(d\) distinct sampling points coalescing at the interior branch point as \(r\downarrow0\) achieves the constant in the limit. For \(\rho=1\), the same generalized Rayleigh quotient is exactly \(d\) for every \(0<r<1\).

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\rho\mathbb D=\{w:|w|<\rho\}\). The valence hypothesis means that for each regular value \(w\), the sum of multiplicities of its preimages in \(\mathbb D\) is at most \(m\). A constant map is harmless because its derivative and the matrix \(H_{f,Z}\) vanish. Repeated sampling points are permitted; all inequalities are in the positive-semidefinite (Loewner) order.

The Bergman space is normalized using \(dA=\pi^{-1}dx\,dy\), giving reproducing kernel \(k_z(w)=(1-\overline z w)^{-2}\).

The statement identifies the best **uniform** constant over a whole class; it does not claim that the best constant for any one fixed non-surjective map equals this value, or classify all pairs realizing equality.

## Proof

Put \(g=f/\rho\). Then \(g:\mathbb D\to\mathbb D\) is holomorphic and at most \(m\)-valent.

**Step 1: range contraction is positive-semidefinite.** The Bergman kernel series is
\[
\frac1{(1-u\overline v)^2}=\sum_{k=0}^{\infty}(k+1)u^k\overline v^{\,k},\qquad |u|,|v|<1.
\]
For the vectors \(v_k=(g'(z_i)g(z_i)^k)_{i=1}^n\), this identity gives
\[
\rho^2H_{g,Z}-H_{\rho g,Z}
=\rho^2\sum_{k=0}^{\infty}(k+1)(1-\rho^{2k})v_kv_k^*\succeq0.
\]
Hence
\[
H_{f,Z}\preceq\rho^2H_{g,Z}.
\]
The series converges in finite-dimensional matrix norm at every fixed tuple.

**Step 2: finite-point control.** Tian's finite-point Schwarz–Pick theorem gives, for every disk self-map \(g\),
\[
H_{g,Z}\preceq nG_Z.
\]
Therefore
\[
H_{f,Z}\preceq n\rho^2G_Z.
\]

**Step 3: the independent finite-valence control.** Define the derivative-weighted composition operator on the normalized Bergman space \(A^2(\mathbb D)\) by
\[
(W_gh)(z)=g'(z)h(g(z)).
\]
The holomorphic area formula, valid without properness, gives
\[
\begin{aligned}
\|W_gh\|_{A^2}^2
&=\int_{\mathbb D}|g'(z)|^2|h(g(z))|^2\,dA(z)\\
&=\int_{\mathbb D}N_g(w)|h(w)|^2\,dA(w)\\
&\le m\|h\|_{A^2}^2,
\end{aligned}
\]
where \(N_g(w)\) counts preimages with multiplicities and is zero outside the image. Thus \(\|W_g\|\le\sqrt m\). On reproducing kernels, \(W_g^*k_{z}=\overline{g'(z)}k_{g(z)}\). Taking Gram matrices gives
\[
H_{g,Z}\preceq mG_Z.
\]
Combining this with Step 2 and Step 1 proves
\[
H_{f,Z}\preceq\rho^2\min\{n,m\}G_Z.
\]

**Step 4: exact sharpness at a coalescing fiber.** Put \(d=\min\{n,m\}\) and choose \(f(z)=\rho z^d\), which is at most \(m\)-valent. For \(d\ge2\), let \(\omega_j=e^{2\pi i(j-1)/d}\), \(z_j=r\omega_j\) for \(0<r<1\), and \(v=(\omega_j^{d-1})_{j=1}^d\). A Fourier expansion of the Bergman kernel gives the exact eigenvalue identities
\[
G_Zv=\frac{d^2r^{2d-2}}{(1-r^{2d})^2}v
\]
and
\[
H_{f,Z}v=\frac{d^3\rho^2r^{2d-2}}{(1-\rho^2r^{2d})^2}v.
\]
Indeed, the Fourier mode of order \(d-1\) in \(G_Z\) selects precisely the terms with indices \(d-1,2d-1,3d-1,\ldots\), and all image points \(f(z_j)=\rho r^d\) agree, so \(H_{f,Z}\) has rank one along \(v\).

Their generalized Rayleigh quotient is
\[
\frac{v^*H_{f,Z}v}{v^*G_Zv}
=d\rho^2\left(\frac{1-r^{2d}}{1-\rho^2r^{2d}}\right)^2
\longrightarrow d\rho^2\qquad (r\downarrow0).
\]
For \(d=1\), the same limiting quotient is obtained with the single point \(z_1=r\) and \(f(z)=\rho z\) (or directly at the origin). If \(n>d\), append any further points of the disk to the initial \(d\) distinct points. Every valid \(n\)-point Loewner inequality must hold for the leading \(d\)-by-\(d\) principal block. Consequently no universal constant smaller than \(d\rho^2\) is possible. This proves the asserted optimality.

## Verification

The two positive-semidefinite estimates arise from independent mechanisms: nonnegative Bergman Taylor coefficients for the image-radius factor and the analytic area formula for the multiplicity factor. The finite-point factor comes from the initiating theorem. These three estimates are combined in the correct Loewner order; taking a scalar minimum is justified because each is separately valid.

For the extremal model, the exact eigenvalue ratio was independently recomputed both from the discrete Fourier series and by finite-matrix evaluation for several degrees and radii. The formula is analytic, and the proof of optimality does not depend on numerical sampling.

The normalized area convention was checked, including \(\|z^k\|_{A^2}^2=1/(k+1)\). No hidden finite-enumeration step is used.

## Relationship to prior work

Tian's 2026 paper establishes \(H_{g,Z}\preceq nG_Z\) for arbitrary self-maps and strengthens it to \(\min\{n,d\}\,G_Z\) for **finite Blaschke products of degree** \(d\). The inspected full six-page version neither controls the image-radius parameter nor extends degree refinement to arbitrary finite-valent nonproper maps. Its sharpness example uses a boundary-fiber limit for an inner map.

The present theorem identifies a different three-parameter sharp constant \(\rho^2\min\{n,m\}\), where \(m\) is a *valence bound* rather than an inner-function degree and \(\rho\) is a strict image-radius bound. It also gives a different sharpness mechanism: for \(\rho<1\) the detecting points coalesce at an **interior critical point**, not at the boundary.

Badea and Renard's 2024 work establishes operator-theoretic multi-point Schwarz–Pick inequalities based on hyperbolic divided differences. Its checked results do not state this Bergman Gram-matrix constant with combined valence and range constraints. Classical area change of variables supplies the multiplicity mechanism but does not by itself yield the sharp finite-point constant involving both \(n\) and \(\rho\).

## Limitations

This is an exact **uniform** inequality. It does not give the optimal individual matrix constant for each fixed map and point tuple.

The valence restriction is essential for the factor \(m\); without it the initiating result still supplies the \(n\) bound. The stated range parameter is a disk centered at the origin, not an arbitrary translated or conformally varying target.

The proof uses the already-proved finite-point theorem as one input; it does not reprove that source's general sharp \(n\) bound. It gives no higher-dimensional or weighted-Bergman generalization.

## References

1. James Tian, *A finite-Point Schwarz-Pick Inequality*, arXiv:2608.10443v1, first posted 11 August 2026, especially Theorem 2.1 and its Bergman Gram-matrix formulation.
2. Cătălin Badea and Axel Renard, *Schwarz-Pick type inequalities from an operator theoretical point of view*, Journal of Mathematical Analysis and Applications 540 (2024), 128578; arXiv:2405.01357v2.
3. Alan F. Beardon and C. David Minda, *A multi-point Schwarz-Pick lemma*, Journal d'Analyse Mathématique 92 (2004), 81–104.
