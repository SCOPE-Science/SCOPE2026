# Boundary-Gaussian singular spectrum of disk transfer between the first two Landau levels

## Finding
Fix the Gaussian measure \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\). Let \(\mathcal L_0\) and \(\mathcal L_1\) be the analytic and true first-excited Gaussian Fock (Landau) levels defined below. For \(x>0\), write \(D_x=\{z:|z|^2<x\}\) and consider the **interlevel disk transfer**
\[
T_x=P_1M_{\mathbf1_{D_x}}|_{\mathcal L_0}:\mathcal L_0\longrightarrow\mathcal L_1,
\]
where \(P_1\) is orthogonal projection onto \(\mathcal L_1\). The complete sequence of its positive singular values, indexed with multiplicity by angular degree \(n\ge0\), is
\[
\boxed{a_n(x)=\frac{x^{n+1}e^{-x}}{\sqrt{n!(n+1)!}}.}
\]
This transfer is compact and belongs to every \(\mathcal S_p\), \(0<p<\infty\). The sequence is strictly log-concave; two adjacent degrees tie as maximizers exactly at \(x=\sqrt{(n+1)(n+2)}\). Its Hilbert–Schmidt norm obeys the exact special-function identity
\[
\boxed{\|T_x\|_{\mathcal S_2}^2=x e^{-2x}I_1(2x),}
\]
where \(I_1\) is the modified Bessel function.

A sharp, global norm inequality and a universal edge profile hold:
\[
\boxed{\|T_x\|<(2\pi)^{-1/2}\quad(x>0),\qquad
\lim_{x\to\infty}\|T_x\|=(2\pi)^{-1/2},}
\]
\[
\boxed{\lim_{x\to\infty}a_{\lfloor x+u\sqrt{x}\rfloor}(x)
 =(2\pi)^{-1/2}e^{-u^2/2}\quad(u\in\mathbb R).}
\]
For every fixed finite real \(p>0\), the **complete Schatten-power edge law** is
\[
\boxed{\lim_{x\to\infty}\frac1{\sqrt{x}}\sum_{n=0}^{\infty}a_n(x)^p
 =\frac{(2\pi)^{(1-p)/2}}{\sqrt p}.}
\]
Writing \(C=(2\pi)^{-1/2}\), every fixed threshold \(0<\eta<C\) satisfies the sharp counting law
\[
\boxed{\lim_{x\to\infty}\frac1{\sqrt{x}}\#\{n\ge0:a_n(x)>\eta\}
=2\sqrt{2\log(C/\eta)}.}
\]
Although \(T_x\to0\) strongly as \(x\to\infty\), its operator norms approach \(C>0\): the active singular modes escape to angular degrees of order \(x\).

## Assumptions and scope
Let \(L^2(\mu)\) be the Gaussian Hilbert space on \(\mathbb C\) with inner product linear in its first argument. Define \(u_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), and \(\mathcal L_0=\overline{\mathrm{span}}\{u_n:n\ge0\}\). Define
\[
v_{-1}(z)=\overline z,\qquad
v_n(z)=\frac{z^n(n+1-|z|^2)}{\sqrt{(n+1)!}},\qquad n\ge0,
\]
and \(\mathcal L_1=\overline{\mathrm{span}}\{v_{-1},v_n:n\ge0\}\). These vectors form an orthonormal basis of the eigenspace of \(-\partial_z\partial_{\overline z}+\overline z\partial_{\overline z}\) with eigenvalue one, and \(\mathcal L_0\perp\mathcal L_1\). The disk radius \(\sqrt{x}\) is arbitrary positive. For \(0<p<1\), \(\mathcal S_p\) refers to the usual Schatten quasi-ideal and \(\sum s_j^p\) to its quasi-norm power. Limits in \(p\) and \(\eta\) hold at each fixed parameter; no uniform-in-\(p\) or moving-threshold assertion is made.

## Proof
**Basis normalization and interlevel diagonalization.** Writing \(t=|z|^2\), the Gaussian radial measure is \(e^{-t}dt\). Thus \(\int_0^\infty t^n e^{-t}dt=n!\), \(\int_0^\infty t^n(n+1-t)e^{-t}dt=0\), and
\[
\int_0^\infty t^n(n+1-t)^2e^{-t}dt=(n+1)!.
\]
Distinct angular degrees are orthogonal. These identities prove the asserted bases, including the exceptional degree \(-1\). Multiplication by a disk indicator preserves angular degree, so \(T_xu_n=\langle\mathbf1_{D_x}u_n,v_n\rangle v_n\), without a component along \(v_{-1}\). Integration of an exact derivative gives
\[
\langle\mathbf1_{D_x}u_n,v_n\rangle
=\frac1{\sqrt{n!(n+1)!}}\int_0^x t^n(n+1-t)e^{-t}dt
=\frac{x^{n+1}e^{-x}}{\sqrt{n!(n+1)!}}.
\]
The coefficients are positive and decay factorially for fixed \(x\). This proves the complete singular-value statement, compactness and membership in all positive Schatten classes. It also shows that \(T_x^*T_x\) has no zero eigenvalue, while \(T_xT_x^*\) has one additional zero eigenvector \(v_{-1}\).

**Modal transitions and Hilbert–Schmidt identity.** The exact ratio is
\[
\frac{a_{n+1}(x)}{a_n(x)}=\frac{x}{\sqrt{(n+1)(n+2)}},
\]
which decreases strictly with \(n\); hence the modal transitions and log-concavity. Squaring the coefficients and using the defining series \(I_1(2x)=\sum_{n\ge0}x^{2n+1}/[n!(n+1)!]\) gives the Bessel identity.

**Global norm, strictness, and spectral escape.** For fixed \(n\), the function \(x\mapsto a_n(x)\) is uniquely maximized at \(x=n+1\), where
\[
b_n=a_n(n+1)=\frac{e^{-(n+1)}(n+1)^{n+1/2}}{n!}.
\]
Its ratio is \(b_{n+1}/b_n=e^{-1}(1+1/(n+1))^{n+3/2}>1\), since \(\log(1+t)>2t/(2+t)\) for every \(t>0\). Stirling's formula gives \(b_n\uparrow C=(2\pi)^{-1/2}\). For each fixed \(x\), the factorial decay makes \(\|T_x\|\) a maximum of finitely many relevant coefficients, hence strictly less than \(C\). Evaluating at \(x=n+1\) proves the supremum \(C\); the local limit below shows \(\|T_x\|\to C\) as \(x\to\infty\). Each fixed \(a_n(x)\to0\), and the norms are uniformly bounded, so a finite-coordinate approximation in \(\mathcal L_0\) proves \(T_x\to0\) strongly.

**Gaussian spectral edge and Schatten powers.** There is the exact Poisson mass representation
\[
a_n(x)=\sqrt{n+1}\;\Pr\{\operatorname{Pois}(x)=n+1\}.
\]
Using Stirling's formula uniformly on \(n=x+u\sqrt{x}+O(1)\) with bounded \(u\), the logarithm of this expression tends to \(-\tfrac12\log(2\pi)-\tfrac12u^2\), proving the local Gaussian limit. To justify global summation, let \(m=n+1\). The elementary bound \(\log(m! )\ge m\log m-m+\tfrac12\log(2\pi m)\) gives
\[
a_{m-1}(x)\le (2\pi)^{-1/2}\exp[-xH(m/x)],\qquad
H(y)=y\log y-y+1.
\]
For \(y\in[1/2,2]\), \(H(y)\ge c(y-1)^2\) with a positive absolute \(c\); outside this interval \(H(y)\ge c_1|y-1|\) for some \(c_1>0\). Consequently, all fixed positive powers of the coefficients have uniformly negligible rescaled tails outside \(|m-x|\le A\sqrt{x}\), in the sequential limit \(x\to\infty\) and then \(A\to\infty\). The central Riemann sum therefore converges to
\[
\int_{\mathbb R}(2\pi)^{-p/2}e^{-pu^2/2}du
=(2\pi)^{(1-p)/2}/\sqrt p.
\]
This is an actual infinite-sum domination argument, not numerical extrapolation. Finally, strict unimodality and the same uniform Gaussian limit identify the endpoints of \(\{n:a_n(x)>\eta\}\) at rescaled positions \(\pm\sqrt{2\log(C/\eta)}\), proving the counting law. The endpoint convention changes the count by at most two and not its limit.

## Verification
The accompanying self-contained numerical program `verify.py` checks the exact coefficient by independent radial quadrature, the mode ratios, strict global norm bounds on finite samples, the Bessel Hilbert–Schmidt series identity, and the large-radius Gaussian, Schatten and counting approximations. It uses Python 3 with NumPy and SciPy and prints a count of passed finite assertions. Finite checks do not certify the all-radius, all-exponent or infinite-dimensional conclusions; those follow from the analytic proof above.

## Relationship to prior work
Gröchenig–Jaming–Malinnikova (arXiv:1811.03937, first posted 2018-11-09) investigate cross-Wigner/STFT zeros and discuss Hermite/polyanalytic phase-space analysis, not cross-Landau hard-disk transfer spectra. Abreu–Gröchenig–Romero (arXiv:1704.03042, first posted 2017-04-10; journal 2019), notably their Section 4, diagonalize **same-window** Hermite Toeplitz localization on disks and analyze one-level concentration, rather than singular values of the off-diagonal map between distinct Landau levels. Keller–Luef (2021) establish polyanalytic Toeplitz symbolic calculus and Bargmann isomorphisms, not the discontinuous disk interlevel norm constant or edge law. Leschke–Sobolev–Spitzer (2020/2021) establish Landau projection entropy area laws and full-level trace asymptotics; the present interlevel singular-value identity and exact sharp constants are not stated in the inspected theorems. The monomial/Gaussian machinery is known; the claim here is specifically the complete *cross-level disk* spectrum together with its global strict norm constant and its full \(p\)-dependent edge/counting laws. No general theorem for arbitrary masks is asserted.

## Limitations
The geometry is a concentric hard disk, the ambient space is one complex dimension, and the transfer is strictly from Landau level zero to level one. Higher-level transfers, nonradial masks, joint large-order limits, and moving \(p\) or \(\eta\) are not covered. Strong evidence of distinctness from the inspected related results does not rule out an earlier equivalent formula under a different normalization, especially in the physics literature. Independent validation has not been performed.

## References
- K. Gröchenig, P. Jaming, E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937 (first publicly posted 2018-11-09); doi:10.1007/s13163-019-00335-w.
- L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic Analysis in Phase Space and Finite Weyl–Heisenberg Ensembles*, arXiv:1704.03042 (first publicly posted 2017-04-10), Journal of Statistical Physics (2019), doi:10.1007/s10955-019-02226-2, Section 4.
- J. Keller, F. Luef, *Polyanalytic Toeplitz Operators: Isomorphisms, Symbolic Calculus and Approximation of Weyl Operators*, Journal of Fourier Analysis and Applications (2021), doi:10.1007/s00041-021-09843-0.
- H. Leschke, A. V. Sobolev, W. Spitzer, *Asymptotic Growth of the Local Ground-State Entropy of the Ideal Fermi Gas in a Constant Magnetic Field*, Communications in Mathematical Physics (2021), doi:10.1007/s00220-020-03907-w.
