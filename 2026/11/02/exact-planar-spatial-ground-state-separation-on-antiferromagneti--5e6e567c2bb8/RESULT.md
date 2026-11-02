# Exact planar–spatial ground-state separation on antiferromagnetic spin rings

## Finding

For every integer \(N\ge3\), exchange constant \(J>0\), and uniform magnetic-field strength \(h\ge0\), consider classical unit spins \(s_0,\ldots,s_{N-1}\) on the cycle with periodic indices and energy
\[
H_h(s)=J\sum_{j=0}^{N-1}s_j\cdot s_{j+1}-h\sum_{j=0}^{N-1}s_j\cdot e,
\]
where \(e\) is a fixed unit vector. Write \(E_d(h)\) for the minimum with spins in \(\mathbb R^d\), where \(d=2\) means XY planar spins with \(e\) in their plane and \(d=3\) means isotropic Heisenberg spins. Put \(c_N=1\) when \(N\) is even, and \(c_N=\cos(\pi/N)\) when \(N\) is odd. Set \(h_s=2J(1+c_N)\).

**Exact spatial energy:** for every \(N\ge3\),
\[
E_3(h)=\begin{cases}
-NJc_N-\dfrac{Nh^2}{4J(1+c_N)},&0\le h\le h_s,\\
N(J-h),&h\ge h_s.
\end{cases}
\]
**Sharp dimension/parity classification:** \(E_2(h)=E_3(h)\) for every \(h\ge0\) when \(N\) is even or \(N=3\). For every odd \(N\ge5\),
\[
E_2(h)>E_3(h)\quad\text{if and only if}\quad 0<h<h_s,
\]
and equality holds at \(h=0\) and for \(h\ge h_s\).

**Quantitative weak-field separation:** for every odd \(N\ge3\), with \(c=\cos(\pi/N)\),
\[
E_2(h)=-NJc-\frac{Nh^2}{8Jc(1+c)}+O(h^3)
\quad(h\downarrow0).
\]
In particular, the zero-temperature longitudinal susceptibilities, defined by \(\chi_d=\lim_{h\downarrow0}2[E_d(0)-E_d(h)]/h^2\), satisfy
\[
\chi_2=\frac{N}{4Jc(1+c)},\qquad
\chi_3=\frac{N}{2J(1+c)},\qquad
\frac{\chi_2}{\chi_3}=\frac1{2c}.
\]
For the pentagon this ratio equals \((\sqrt5-1)/2\). It equals one for the triangle and tends to \(1/2\) as odd \(N\to\infty\).

## Assumptions and scope

These are **finite**, **zero-temperature**, **classical** spin models, with unit spin lengths, positive uniform nearest-neighbor antiferromagnetic exchange \(J\), periodic boundary conditions, and a field coupled identically to all spins. The XY field lies inside the spin plane. The claim does not cover quantum spins, easy-plane anisotropy at nonzero temperature, nonuniform couplings, or nonuniform fields. Energies count each undirected bond once. Susceptibility is the zero-field one-sided energy curvature and does not include physical gyromagnetic unit factors.

## Proof

**1. The spectral lower bound.** Set \(M=\sum_j s_j\). Fourier diagonalization of the real cyclic nearest-neighbor quadratic form, component by component, gives
\[
\sum_js_j\cdot s_{j+1}\ge -Nc_N+\frac{1+c_N}{N}|M|^2.
\tag{1}
\]
Indeed, the constant Fourier mode has eigenvalue \(1\) for the half-adjacency form, while the least remaining mode has eigenvalue \(-c_N\). Equality in (1) requires all nonconstant components to belong to its least-eigenvalue Fourier eigenspace. Minimizing the right side minus \(h M\cdot e\) over \(0\le|M|\le N\) gives the stated piecewise formula for \(E_3\). It is sharp: for odd \(N\), take the conical spiral
\[
s_j=(\sqrt{1-u^2}\cos(qj),\sqrt{1-u^2}\sin(qj),u),
\quad q=\pi-\pi/N,
\quad u=\min\{h/h_s,1\}.
\]
For even \(N\), use \(q=\pi\). Both realize equality in (1) and align the resultant with the field.

**2. Exact XY equality for even cycles and the triangle.** For even \(N\), set the XY spins to \(s_j=(u,(-1)^j\sqrt{1-u^2})\), with \(u=\min\{h/(4J),1\}\); they saturate (1). For \(N=3\), every edge is present and \(\sum_js_j\cdot s_{j+1}=(|M|^2-3)/2\). Three planar unit vectors can have any prescribed resultant length from zero through three, so the same minimum is attained by XY spins at every field.

**3. Strict XY separation on every longer odd cycle.** Suppose odd \(N\ge5\), \(0<h<h_s\), and an XY minimizer attains \(E_3(h)\). Equality in (1) and in the completed-square field bound forces \(|M|=Nh/h_s\), strictly between zero and \(N\). Encode the planar spins by unit complex numbers \(z_j\). With \(m=(N-1)/2\) and the primitive root \(t=\exp(2\pi i m/N)\), equality in (1) forces
\[
z_j=A+Bt^j+Ct^{-j}.
\tag{2}
\]
The unit-modulus identity \(|z_j|^2=1\) has Fourier coefficients \(B\overline C\) at frequency two and \(B\overline A+A\overline C\) at frequency one. Since frequencies \(0,\pm1,\pm2\) are distinct modulo every odd \(N\ge5\), these coefficients separately vanish. Thus \(B\overline C=0\) and \(B\overline A+A\overline C=0\), which imply that (2) contains only a single nonzero monomial. Hence \(|M|=N\) (constant spins) or \(|M|=0\) (pure spiral), a contradiction. As the XY configuration space is compact, the unattained lower bound is a **strict** energy gap. At zero field the planar pure spiral realizes (1); at or above saturation the planar aligned configuration realizes it. This completes the global equality classification.

**4. Weak-field XY coefficient.** At \(h=0\), the complete XY ground-state set on an odd cycle consists of the two chiral spiral families \(\theta_j=qj+\phi\) and \(\theta_j=-qj+\phi\), \(q=\pi-\pi/N\). This follows from equality in (1) at \(M=0\) and the same Fourier constant-modulus argument without the constant term. Write \(\theta_j=qj+\phi+v_j\) with \(\sum_jv_j=0\). With \(c=\cos(\pi/N)>0\), the energy expansion uniformly in \(\phi\) is
\[
H_h=-NJc+\frac{Jc}{2}\sum_j(v_{j+1}-v_j)^2
+h\sum_j\sin(qj+\phi)v_j+O(\|v\|^3+h\|v\|^2).
\tag{3}
\]
The cycle Laplacian \(L\) sends \(b_j=\sin(qj+\phi)\) to \(2(1+c)b_j\) and \(\sum_jb_j^2=N/2\). Minimizing the displayed quadratic over mean-zero \(v\) therefore subtracts
\[
\frac{h^2}{2Jc}\,b^\mathsf TL^+b
=\frac{Nh^2}{8Jc(1+c)}.
\]
The Laplacian has a strictly positive spectral gap on mean-zero vectors, uniformly over the compact ground-state phase families. A compactness argument excludes distant configurations for small \(h\), and uniform implicit minimization gives \(v=O(h)\), justifying the stated \(O(h^3)\) remainder. The two chiralities yield the same coefficient. The exact Heisenberg formula then gives both susceptibilities and their ratio.

## Verification

Running `python check.py` with NumPy and SciPy performs 97 checks: 61 independent Fourier/susceptibility/nonlinear ground-state comparisons and 36 interior-gap/even-parity equality comparisons, at several ring sizes, fields, and couplings. The finite optimizations corroborate but do not establish the infinite family of inequalities; the Fourier bound, equality obstruction, and local Hessian proof do that. The physical-field normalization and cyclic-bond counting are explicitly fixed above.

## Relationship to prior work

Schmidt and Luban (2002), especially §§6.3.1–6.3.2, prove the spatial-spin spectral parabola and identify numerically a strict coplanar deficit for the pentagon at intermediate magnetization; they expressly do not claim a rigorous proof of that pentagon deficit. Formula (1) and the spatial energy are established background, not new. The additional conclusions here are the **rigorous exact planar-versus-spatial equality classification for every finite cycle**, the odd-cycle Fourier rigidity argument, and the exact weak-field planar curvature and susceptibility ratio. Their energy uses twice our single-bond convention, so direct formula comparisons require that normalization change.

Konstantinidis (2014) studies odd **open** classical chains with biquadratic exchange, which have a residual zero-field moment rather than the frustrated periodic spiral here. Owerre and Nsofini (2015) study tunneling and odd-spin solitons in a different quantum/anisotropic setting. Neither directly supplies the stated XY/Heisenberg parity classification or coefficient.

## Limitations

The equality result concerns **global** ground-state energies, not metastable stationary configurations or finite-temperature magnetic susceptibility. No assertion is made that the small-field \(O(h^3)\) correction is generically nonzero. The comparison is a finite-size classical statement, not a thermodynamic phase transition. Independent scientific validation and final historical-priority assessment have not been performed; a more general unpublished rigidity theorem could cover the Fourier equality argument.

## References

1. H.-J. Schmidt and M. Luban, *Classical ground states of symmetrical Heisenberg spin systems*, first public arXiv submission 2002-09-06, arXiv:cond-mat/0209157, https://arxiv.org/abs/cond-mat/0209157 (especially §§1, 2, 6.3.1–6.3.2).
2. N. P. Konstantinidis, *Zero-Temperature Configurations of Short Odd-Numbered Classical Spin Chains with Bilinear and Biquadratic Exchange Interactions*, first public arXiv submission 2014-05-22, arXiv:1405.5931, https://arxiv.org/abs/1405.5931.
3. S. A. Owerre and J. Nsofini, *Antiferromagnetic molecular nanomagnets with odd-numbered coupled spins*, first public arXiv submission 2015-02-19, arXiv:1502.05684, https://arxiv.org/abs/1502.05684.
