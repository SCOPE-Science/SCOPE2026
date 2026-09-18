# Positive-density spherical harmonics simultaneously saturating all Sogge \(L^p\) branches

## Statement

Let \(n\ge 2\), let
\[
p_n=\frac{2(n+1)}{n-1},
\qquad
\sigma_n(p)=
\begin{cases}
\frac{n-1}{4}-\frac{n-1}{2p},&2\le p\le p_n,\\[2mm]
\frac{n-1}{2}-\frac np,&p_n\le p\le\infty,
\end{cases}
\]
and let \(\mathcal H_k=\mathbb{SH}_k^n\) be the real spherical harmonics of degree \(k\) on \(\mathbb S^n\), with \(N_k=\dim\mathcal H_k\).

For every fixed density
\[
0<\rho<\frac12,
\]
there are constants \(c_{\rho,n,p},C_{n,p}>0\) such that, for all sufficiently large \(k\), one can find an orthonormal set
\[
\{u_{k,j}\}_{j=1}^{M_k}\subset \mathcal H_k,
\qquad
M_k=\lfloor \rho N_k\rfloor,
\]
with the following simultaneous property: for every fixed \(p\in[2,\infty]\) and every \(1\le j\le M_k\),
\[
c_{\rho,n,p}\,k^{\sigma_n(p)}
\le
\|u_{k,j}\|_{L^p(\mathbb S^n)}
\le
C_{n,p}\,k^{\sigma_n(p)}.
\]

Thus the *same* positive-density orthonormal family saturates the sharp Sogge growth rate on both sides of the critical exponent \(p_n\), simultaneously for all \(p\). The constants are not asserted to be uniform in \(p\).

## Context

For the round sphere, the two branches of the sharp Sogge estimate have classical, geometrically different extremizers. Highest-weight harmonics (Gaussian beams) saturate the range \(2<p\le p_n\), while zonal harmonics saturate \(p_n\le p\le\infty\).

Han recently proved that for every \(\varepsilon>0\) there are orthonormal sets of density at least \(1-\varepsilon\) saturating the high-\(p\) branch, and separately orthonormal sets of density at least \(1-\varepsilon\) saturating the low-\(p\) branch. The two constructions use different building blocks. The high-\(p\) argument is driven by large values at selected points; the low-\(p\) argument is driven by dual pairing with Gaussian beams.

The result above shows that these concentration mechanisms can be imposed on one and the same positive-density orthonormal family.

## Proof

Normalize surface measure on \(\mathbb S^n\) to have total mass one.

### 1. A well-conditioned zonal block

Fix \(\rho<1/2\), and put \(M=\lfloor \rho N_k\rfloor\).

Han's spherical-design/restricted-invertibility construction gives, after choosing a slightly larger auxiliary density and then taking a principal subfamily, normalized zonal harmonics
\[
Z_{x_1},\dots,Z_{x_M}
\]
whose Gram matrix
\[
E_Z=(\langle Z_{x_i},Z_{x_j}\rangle)_{i,j=1}^M
\]
has
\[
\lambda_{\min}(E_Z)\ge c_0^2
\]
for a constant \(c_0=c_0(\rho,n)>0\), uniformly in \(k\).

Define
\[
z_i=\sum_{j=1}^M (E_Z^{-1/2})_{ij}Z_{x_j}.
\]
Then \(z_1,\dots,z_M\) are orthonormal. Since
\[
Z_x(x)=\sqrt{N_k}
\quad\text{and}\quad
Z_{x_j}(x_i)=\sqrt{N_k}\,\langle Z_{x_j},Z_{x_i}\rangle,
\]
we have
\[
z_i(x_i)
=
\sqrt{N_k}\,(E_Z^{1/2})_{ii}
\ge c_0\sqrt{N_k}.
\]
Let
\[
U=\operatorname{span}\{Z_{x_1},\dots,Z_{x_M}\}
=\operatorname{span}\{z_1,\dots,z_M\},
\qquad
V=U^\perp,
\]
so
\[
D:=\dim V=N_k-M.
\]

### 2. A well-conditioned Gaussian-beam block inside \(V\)

Let \(Q_R\) denote an \(L^2\)-normalized real Gaussian beam obtained by rotating the normalized real part of
\[
(x_1+i x_2)^k.
\]
The rotated beams form the tight continuous frame
\[
\int_{\mathrm{SO}(n+1)} Q_R\otimes Q_R\,dR
=
\frac1{N_k}I_{\mathcal H_k}.
\]
Let \(P=P_V\) be the orthogonal projection onto \(V\), and set
\[
g_R=P Q_R.
\]
Then
\[
\int_{\mathrm{SO}(n+1)} g_R\otimes g_R\,dR
=
\frac1{N_k}P.
\]

Fix small \(\eta>0\). By compactness and equal-weight discretization, choose finitely many rotations \(R_1,\dots,R_L\) such that
\[
\left\|
\frac1L\sum_{\ell=1}^L g_{R_\ell}\otimes g_{R_\ell}
-\frac1{N_k}P
\right\|
\le \frac{\eta}{N_k}.
\]
Let \(A:\mathbb R^L\to V\) be given by \(Ae_\ell=g_{R_\ell}\). Then
\[
\|A\|_{\mathrm{HS}}^2
\ge
L(1-\eta)\frac{D}{N_k},
\qquad
\|A\|^2
\le
L\frac{1+\eta}{N_k}.
\]
Hence
\[
\frac{\|A\|_{\mathrm{HS}}^2}{\|A\|^2}
\ge
\frac{1-\eta}{1+\eta}D.
\]

Choose \(0<\delta<1\) and then \(\eta>0\) so small that
\[
\delta^2\frac{1-\eta}{1+\eta}(1-\rho)>\rho.
\]
This is possible exactly because \(\rho<1/2\).

Apply the Spielman--Srivastava form of restricted invertibility. For all sufficiently large \(k\), it yields at least \(M\) projected beams whose Gram matrix has its least eigenvalue bounded below by a constant
\[
c_1^2=c_1^2(\rho,n)>0.
\]
Indeed, the selected cardinality is at least
\[
\delta^2\frac{\|A\|_{\mathrm{HS}}^2}{\|A\|^2}
\]
up to an integer part, while the lower spectral bound supplied by restricted invertibility is at least
\[
(1-\delta)^2\frac{\|A\|_{\mathrm{HS}}^2}{L}
\ge
(1-\delta)^2(1-\eta)\frac{D}{N_k}.
\]
If more than \(M\) vectors are selected, take any \(M\) of them; Cauchy interlacing preserves the same lower bound for the corresponding principal Gram matrix.

Relabel these projected beams as
\[
g_i=P Q_i,\qquad i=1,\dots,M,
\]
and write their Gram matrix as \(E_G\). Set
\[
q_i=\sum_{j=1}^M(E_G^{-1/2})_{ij}g_j.
\]
Then \(q_1,\dots,q_M\) are orthonormal vectors in \(V\), and
\[
\langle q_i,Q_i\rangle
=
\langle q_i,g_i\rangle
=
(E_G^{1/2})_{ii}
\ge c_1.
\]

### 3. Mix the two concentration mechanisms

For each \(i\), choose \(s_i\in\{-1,1\}\) so that
\[
\bigl|\langle z_i+s_iq_i,Q_i\rangle\bigr|
\ge
\langle q_i,Q_i\rangle
\ge c_1.
\]
This is always possible because for real numbers \(a,b\),
\[
\max\{|a+b|,|a-b|\}\ge |b|.
\]

Define
\[
u_i=\frac{z_i+s_iq_i}{\sqrt2}.
\]
Since the two orthonormal families lie in the orthogonal subspaces \(U\) and \(V\),
\[
\langle u_i,u_j\rangle=\delta_{ij}.
\]

Moreover \(Z_{x_i}\in U\) and \(q_i\in V\), so the reproducing identity gives
\[
q_i(x_i)=\sqrt{N_k}\,\langle q_i,Z_{x_i}\rangle=0.
\]
Consequently
\[
u_i(x_i)=\frac{z_i(x_i)}{\sqrt2}
\ge \frac{c_0}{\sqrt2}\sqrt{N_k}.
\]
At the same time,
\[
|\langle u_i,Q_i\rangle|
\ge \frac{c_1}{\sqrt2}.
\]

Thus every \(u_i\) simultaneously retains a zonal point peak and a nontrivial Gaussian-beam dual pairing.

### 4. The low-\(p\) branch

For \(2<p\le p_n\), let \(p'=p/(p-1)\). The normalized Gaussian beams satisfy
\[
\|Q_i\|_{L^{p'}(\mathbb S^n)}
\asymp_{n,p}
k^{-\sigma_n(p)}.
\]
Therefore Hölder's inequality gives
\[
\frac{c_1}{\sqrt2}
\le
|\langle u_i,Q_i\rangle|
\le
\|u_i\|_p\|Q_i\|_{p'},
\]
hence
\[
\|u_i\|_p\gtrsim_{\rho,n,p} k^{\sigma_n(p)}.
\]

### 5. The high-\(p\) branch

The pointwise lower bound is
\[
|u_i(x_i)|\gtrsim_{\rho,n}\sqrt{N_k}
\asymp_n k^{(n-1)/2}.
\]
For every \(L^2\)-normalized degree-\(k\) harmonic, the standard gradient estimate gives
\[
\|\nabla u\|_\infty\lesssim_n k^{(n+1)/2}.
\]
Hence the lower bound at \(x_i\) persists, with a smaller constant, throughout a geodesic ball of radius \(c_{\rho,n}/k\). Such a ball has measure comparable to \(k^{-n}\). Therefore, for \(p_n\le p<\infty\),
\[
\|u_i\|_p
\gtrsim_{\rho,n,p}
k^{(n-1)/2}k^{-n/p}
=
k^{\sigma_n(p)}.
\]
For \(p=\infty\), the value at \(x_i\) gives the lower bound directly.

The matching upper bounds in all ranges are exactly Sogge's sharp estimates. At \(p=2\), \(\|u_i\|_2=1\).

This proves the theorem.

## Interpretation

The critical Sogge exponent separates two different classical concentration models, but it does not force an eigenfunction to choose one of them. A positive-density orthonormal family can carry both a point-scale peak and a geodesic-scale dual signature strongly enough to be extremal for every \(L^p\) exponent simultaneously.

The threshold \(1/2\) here comes from this two-subspace construction: an \(M\)-dimensional zonal block is paired with an \(M\)-dimensional beam block inside its orthogonal complement. No claim is made that density \(1/2\) is optimal, or that simultaneous maximizers cannot have density approaching one.

## Prior literature and originality boundary

Han's 2026 paper proves density arbitrarily close to one separately for the high-\(p\) and low-\(p\) branches. Its statements are branch-specific, and its proof explicitly switches from zonal harmonics to Gaussian beams because each mechanism alone does not recover the other branch. The present claim is the simultaneous intersection statement for one orthonormal family, together with the projected-frame construction above.

The ingredients consisting of the sharp Sogge bounds, zonal and highest-weight extremizers, Gaussian-beam \(L^r\) norms, the tight rotational frame, gradient propagation, and restricted invertibility are prior results and are not claimed as new.

To the best of our knowledge, searches for simultaneous/all-exponent Sogge saturation, mixed zonal/Gaussian-beam spherical harmonics, and a common positive-density orthonormal family did not locate this statement. Because the construction is short once the two recent branchwise constructions are placed side by side, an unrecorded folklore observation or very recent parallel observation remains a meaningful originality risk.

## Limitations

- The result is for round spheres \(\mathbb S^n\), \(n\ge2\).
- It gives every fixed density \(\rho<1/2\), not density \(1/2\), full density, or a complete eigenbasis.
- It does not show that \(1/2\) is a sharp simultaneous-density threshold.
- Constants may depend on \(p\), \(n\), and \(\rho\); no uniform-in-\(p\) estimate is claimed.
- It does not extend the construction to general compact manifolds.
- No independent validation has been performed.

## References

1. X. Han, *Spherical harmonics with maximal \(L^p\) norm growth*, arXiv:2609.14023v1 (2026).
2. X. Han, *Spherical harmonics with maximal \(L^p\) (\(2<p\le6\)) norm growth*, J. Geom. Anal. 26 (2016), 378--398; arXiv:1404.5016.
3. D. A. Spielman and N. Srivastava, *An elementary proof of the restricted invertibility theorem*, Israel J. Math. 190 (2012), 83--91; arXiv:0911.1114.
4. C. D. Sogge, *Oscillatory integrals and spherical harmonics*, Duke Math. J. 53 (1986), 43--65.
