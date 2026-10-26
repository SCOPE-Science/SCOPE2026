# A sharp quadrupole Slepian transition for antipodal spherical caps

## Finding
Let \(d\ge3\), and let \(\sigma\) be probability-normalized surface measure on \(S^{d-1}\). For \(0<t<1\), let \(C_t=\{x\in S^{d-1}:x_d^2\ge t\}\), a pair of antipodal caps. Let \(\mathcal H_2\) be the real degree-two spherical harmonics, and let \(K_t\) be the spatial energy-concentration operator defined by \(\langle K_tf,g\rangle=\int_{C_t}fg\,d\sigma\) for \(f,g\in\mathcal H_2\), with the global \(L^2(\sigma)\) inner product. Then \(K_t\) has exactly three eigenvalue branches:

\[
\begin{aligned}
\lambda_Z(t)&=\frac{d+2}{2(d-1)B_d}\int_t^1(du-1)^2w_d(u)\,du,\\
\lambda_M(t)&=\frac{d(d+2)}{(d-1)B_d}\int_t^1u(1-u)w_d(u)\,du,\\
\lambda_E(t)&=\frac{d(d+2)}{(d-1)(d+1)B_d}\int_t^1(1-u)^2w_d(u)\,du,
\end{aligned}
\]
where \(B_d=\mathrm B(1/2,(d-1)/2)\) and \(w_d(u)=u^{-1/2}(1-u)^{(d-3)/2}\). Their multiplicities are, respectively, \(1\), \(d-1\), and \((d-2)(d+1)/2\). For every \(0<t<1\), the following **exact gap identities** hold:

\[
\lambda_Z-\lambda_M=\frac{d+2}{(d-1)B_d}(dt-1)\sqrt t(1-t)^{(d-1)/2},
\]
\[
\lambda_M-\lambda_E=\frac{2d(d+2)}{(d-1)(d+1)B_d}\sqrt t(1-t)^{(d+1)/2}>0.
\]
Consequently the sharp maximum concentration is \(\max\{\lambda_Z,\lambda_M\}\). For \(0<t<1/d\) its complete maximizing space is the \((d-1)\)-dimensional meridional family \(\mathrm{span}\{x_dx_i:1\le i<d\}\). At \(t=1/d\), the entire \(d\)-dimensional zonal-plus-meridional space maximizes. For \(1/d<t<1\), the unique maximizing line is \(\mathrm{span}\{d x_d^2-1\}\). The sharp critical cap angular radius is \(\arccos(1/\sqrt d)\).

## Assumptions and scope
The ambient field is real; \(d\) is an integer at least three, and \(0<t<1\). All integrations use probability-normalized surface measure. By a degree-two spherical harmonic we mean the restriction of a homogeneous quadratic harmonic polynomial, equivalently \(f_A(x)=x^\mathsf{T}Ax\) with real symmetric trace-zero \(A\). This is a **pure-degree** space: constants and degree-one spherical harmonics are excluded. The caps' axis is the final coordinate; rotations transfer the statement to any axis. The normalization is the energy fraction \(\int_{C_t}|f|^2d\sigma/\int_{S^{d-1}}|f|^2d\sigma\).

## Proof
Put \(U=x_d^2\) for \(x\) uniformly distributed on the sphere. Its density is \(w_d(u)/B_d\) on \((0,1)\). Conditional on \(U=u\), the equatorial coordinates are \(x'=\sqrt{1-u}\,Y\), where \(Y\) is uniform on \(S^{d-2}\), independent of the sign of \(x_d\). Write each trace-zero quadratic, uniquely, as a linear combination of the following orthogonal types:

\[
Z:\quad d x_d^2-1;\qquad M:\quad x_dx_i\ (1\le i<d);\qquad E:\quad x'^\mathsf{T}Bx',\quad B=B^\mathsf{T},\ \operatorname{tr}B=0.
\]
The three spaces have dimensions \(1\), \(d-1\), and \((d-2)(d+1)/2\), respectively. They are pairwise orthogonal both globally and after multiplication by the indicator of \(C_t\): conditional sign symmetry eliminates \(M\)-cross terms, and rotational symmetry makes the conditional mean of every \(E\)-element zero. Rotational invariance also makes the restricted energy quadratic form a scalar multiple of the global one on each of \(M\) and \(E\) (equivalently, use the invariant second and fourth moments of \(Y\)). Thus these three subspaces are eigenspaces.

For \(Z\) the conditional squared amplitude is \((du-1)^2\). For every \(M\)-element it is a positive constant times \(u(1-u)\). For every \(E\)-element it is a positive constant times \((1-u)^2\). The constants cancel on dividing the cap energy by the full-sphere energy. The beta moments \(\mathbb E U=1/d\) and \(\mathbb E U^2=3/[d(d+2)]\) give the three denominators
\[
\mathbb E( dU-1)^2=\frac{2(d-1)}{d+2},\qquad \mathbb E[U(1-U)]=\frac{d-1}{d(d+2)},\qquad \mathbb E(1-U)^2=\frac{(d-1)(d+1)}{d(d+2)}.
\]
These yield the asserted integral expressions and multiplicities.

For the exact spectral gaps, set \(g(u)=\sqrt u(1-u)^{(d-1)/2}\) and \(h(u)=\sqrt u(1-u)^{(d+1)/2}\). Direct differentiation gives
\[
2\frac d{du}[(1-du)g(u)]=\bigl[(du-1)^2-2du(1-u)\bigr]w_d(u)
\]
and
\[
-2h'(u)=\bigl[(d+1)u(1-u)-(1-u)^2\bigr]w_d(u).
\]
Both \(g(1)\) and \(h(1)\) vanish. Integrating these identities from \(t\) to one, and multiplying by the common normalizing factors in the three eigenvalue formulas, proves both displayed spectral-gap identities. The second gap is strictly positive in the stated open interval; the sign of the first is precisely the sign of \(dt-1\). These strict comparisons give every maximizing space, including the equality case, and conclude the proof.

## Verification
The complete proof is analytic for all \(d\ge3\). The accompanying `check_quadrupole.py` independently evaluates the beta-weighted integrals and gap identities at several dimensions and cap thresholds. Run `python check_quadrupole.py` with SciPy installed. The script is a numerical regression check, not a substitute for the exact integral and derivative arguments.

## Relationship to prior work
Simons, Dahlen and Wieczorek (2004/2006) formulate spherical spatiospectral concentration and the classical Slepian spectral matrix, especially for a single polar cap and full low-pass harmonic bands. Simons and Dahlen (2006) explicitly treat antipodal double polar caps on \(S^2\), splitting their full low-pass problem by order and parity; their equations (82)–(89) and §5.2 provide a computational framework. The present assertion concerns **only pure degree two**, includes **all real dimensions \(d\ge3\)**, and determines **analytically the complete maximizing subspace and universal sharp switch at \(t=1/d\)**. The earlier general kernels can be specialized to recover individual low-dimensional matrix entries; this work does not claim the Slepian construction or the cap-kernel decomposition is new.

## Limitations
The result does not identify optimal functions in spaces that also admit spherical harmonic degrees zero, one, or greater than two. It makes no assertion about nonsymmetric regions, non-antipodal caps, noisy measurements, or optimality among all bandwidths. The \(t=0\) and \(t=1\) endpoints are excluded because their operators are scalar with larger degeneracy. Earlier general Slepian kernels imply computations in dimension three; the precise global priority of this closed-form dimension-uniform crossing remains subject to broader bibliographic examination.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (first public version 2004-08-31), later SIAM Review 48 (2006), 504–536. https://arxiv.org/abs/math/0408424
2. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, arXiv:math/0603271 (first public version 2006-03-11), later Geophysical Journal International 166 (2006), 1039–1061. https://arxiv.org/abs/math/0603271
