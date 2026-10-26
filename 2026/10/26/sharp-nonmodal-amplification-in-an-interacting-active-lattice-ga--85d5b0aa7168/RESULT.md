# Sharp nonmodal amplification in an interacting active lattice gas

## Finding
Consider the dimensionless one-dimensional hydrodynamic equations of Kourbane-Houssene, Erignoux, Bodineau and Tailleur for an active exclusion lattice gas on the periodic interval of circumference \(L>0\):
\[
\partial_t\rho=\partial_x^2\rho-\mathrm{Pe}\,\partial_x[m(1-\rho)],\qquad
\partial_tm=\partial_x^2m-\mathrm{Pe}\,\partial_x[\rho(1-\rho)]-2m.
\]
Linearize about the homogeneous state \((\rho,m)=(r,0)\), where \(0<r<1\) and \(\mathrm{Pe}\ge0\), and restrict to perturbations with zero mean total-density perturbation. Let \(\mathcal L_{r,\mathrm{Pe}}\) denote that linearized generator on the real Hilbert space of square-integrable pairs, with natural species norm
\[
\|(u,v)\|_2^2=\int_0^L (u^2+v^2)\,dx
=2\int_0^L (\delta\rho_+^2+\delta\rho_-^2)\,dx,
\qquad u=\delta\rho_++\delta\rho_-,\ v=\delta\rho_+-\delta\rho_-.
\]
Put \(k_1=2\pi/L\) and \(Q=2+k_1^2\). Then the exact, global, necessary-and-sufficient strict-transient-amplification threshold is
\[
\boxed{\exists t>0:\ \|e^{t\mathcal L_{r,\mathrm{Pe}}}\|_{2\to2}>1
\quad\Longleftrightarrow\quad \mathrm{Pe}^2r^2>4Q.}
\]
The criterion means that *some* arbitrarily small real physical perturbation initially increases in this norm; it does not mean every initial perturbation increases.

For \(1/2<r<1\), the homogeneous state is spectrally strictly stable on the fixed-mass space exactly when
\[
\mathrm{Pe}^2(1-r)(2r-1)<Q.
\]
The spectrally stable but strictly amplifying window is therefore
\[
\boxed{\frac{4Q}{r^2}<\mathrm{Pe}^2<\frac{Q}{(1-r)(2r-1)}.}
\]
It is nonempty for every \(r\in(1/2,1)\setminus\{2/3\}\), since the squared-threshold separation is precisely
\[
\frac{Q}{(1-r)(2r-1)}-\frac{4Q}{r^2}
=\frac{Q(3r-2)^2}{r^2(1-r)(2r-1)}>0.
\]
The unique exceptional density \(r=2/3\) makes every nonzero Fourier generator self-adjoint for every nonzero activity; at zero activity all Fourier generators are diagonal. Hence transient norm amplification and strict spectral instability have coincident boundaries at \(r=2/3\). For \(0<r\le1/2\), every fixed-mass Fourier mode is spectrally strictly stable for all finite \(\mathrm{Pe}\), yet amplification still occurs above its stated threshold.

At *half filling* \(r=1/2\), every mode has the two \(\mathrm{Pe}\)-independent eigenvalues \(-k^2\) and \(-(k^2+2)\), but the maximum transient gain diverges **linearly** with activity: defining
\[
G_L(P)=\sup_{t\ge0}\|e^{t\mathcal L_{1/2,P}}\|_{2\to2},\qquad
C_L=\max_{n\ge1}\frac{k_n}{2(k_n^2+2)}
\left(\frac{k_n^2}{k_n^2+2}\right)^{k_n^2/2},\quad k_n=\frac{2\pi n}{L},
\]
one has the nonasymptotic bounds
\[
\boxed{P C_L\le G_L(P)\le P C_L+1\qquad(P\ge0),}
\]
where \(0<C_L<\infty\) and the maximum defining it is attained. Hence \(\lim_{P\to\infty}G_L(P)/P=C_L\). These statements concern the exact linearized hydrodynamic semigroup, not the finite-particle stochastic dynamics.

## Assumptions and scope
The spatial variable belongs to \(\mathbb T_L=\mathbb R/L\mathbb Z\) with periodic boundary conditions and dimensionless constant diffusion coefficient one and tumbling coefficient two, exactly as in the cited hydrodynamic equations. The real Fourier zero mode of the total-density perturbation is excluded by conserved total particle mass; the zero mode of polarization remains allowed and decays as \(e^{-2t}\). All nonzero modes \(k_n\) with both positive and negative integers are retained; \(r\in(0,1)\), \(\mathrm{Pe}\in[0,\infty)\), and \(L\in(0,\infty)\) are fixed unless the explicit large-activity limit is taken. The norm is the unweighted standard Euclidean norm on species densities; it is not a thermodynamic entropy, a weighted covariance norm, or an arbitrary change of variables. Initial perturbations are taken in \(L^2(\mathbb T_L)\), real valued, with zero mean for total density. The diffusion gives a strongly continuous analytic semigroup on this space.

"Spectrally strictly stable" means the spectrum of the fixed-mass generator lies in the open left half-plane. At equality in the spinodal threshold the mode \(k_1\) is neutral, not strictly stable. "Strict amplification" means an operator norm strictly exceeding one at some finite positive time. At equality in the amplification threshold the semigroup is contractive and there is no strict amplification.

## Proof
**1. Exact Fourier generator.** Writing the perturbations as \(\rho=r+u\) and \(m=v\) and retaining first-order terms gives
\[
\partial_tu=u_{xx}-\mathrm{Pe}(1-r)v_x,\qquad
\partial_tv=v_{xx}-\mathrm{Pe}(1-2r)u_x-2v.
\]
For nonzero Fourier number \(k=2\pi n/L\), its amplitude vector evolves with the exact matrix
\[
A_k=\begin{pmatrix}
-k^2&-i\mathrm{Pe}\,k(1-r)\\
-i\mathrm{Pe}\,k(1-2r)&-(k^2+2)
\end{pmatrix}.
\]
Fourier Parseval identifies the full semigroup norm with the supremum of the largest Euclidean singular values of \(e^{tA_k}\) over nonzero Fourier modes, along with the harmless polarization zero mode. The Fourier pair \(k,-k\) of a real perturbation is related by complex conjugation, so each complex maximizing direction corresponds to a real sine/cosine perturbation without changing the norm ratio.

**2. Exact norm threshold without diagonalization.** The Hermitian part \(H_k=(A_k+A_k^*)/2\) is
\[
H_k=\begin{pmatrix}
-k^2&-i\mathrm{Pe}\,kr/2\\
i\mathrm{Pe}\,kr/2&-(k^2+2)
\end{pmatrix},
\]
whose maximal eigenvalue is
\[
\omega_k=-k^2-1+\sqrt{1+(\mathrm{Pe}\,kr/2)^2}.
\]
For every Fourier solution \(w'=A_kw\), the exact energy identity \(\frac{d}{dt}\|w\|^2=2\langle w,H_kw\rangle\) shows that if every \(\omega_k\le0\), all modes, hence the full semigroup, are contractive. Conversely if some \(\omega_k>0\), its Hermitian-part top eigenvector has positive initial derivative of squared norm and thus strictly amplifies at sufficiently small positive time, producing an admissible real zero-mean perturbation. Since \(k\ne0\), the condition \(\omega_k>0\) is equivalent by squaring positive sides to
\[
\mathrm{Pe}^2r^2>4(k^2+2).
\]
The right side is smallest at \(k=k_1\), proving the global if-and-only-if threshold including its equality case. All higher modes are simultaneously controlled by the same energy inequality; no finite spectral cutoff is used.

**3. Modal threshold and the exceptional density.** Direct multiplication yields
\[
\big(A_k+(k^2+1)I\big)^2
=\big[1+\mathrm{Pe}^2k^2(1-r)(2r-1)\big]I.
\]
Thus the modal eigenvalues are
\[
\lambda_\pm(k)=-k^2-1\pm\sqrt{1+\mathrm{Pe}^2k^2(1-r)(2r-1)},
\]
with a complex square root if the argument is negative. For \(r\le1/2\) the square-root real part is at most one, so the real part of both eigenvalues is negative for every nonzero \(k\). For \(r>1/2\), the positive branch has negative real part precisely when \(\mathrm{Pe}^2(1-r)(2r-1)<k^2+2\); demanding this for all modes reduces to \(k_1\). Subtraction of this exact spinodal boundary and the norm threshold yields
\[
\frac{Q}{(1-r)(2r-1)}-\frac{4Q}{r^2}
=\frac{Q\,[r^2-4(1-r)(2r-1)]}{r^2(1-r)(2r-1)}
=\frac{Q(3r-2)^2}{r^2(1-r)(2r-1)}.
\]
It vanishes only at \(r=2/3\). At precisely that density, the off-diagonal entries of \(A_k\) are complex conjugates, so every \(A_k\) is Hermitian. Conversely, at nonzero activity and nonzero wave number these entries are conjugates only at this density (although all modes are diagonal when activity is zero). For this density, eigenvalue stability implies norm contractivity and no stable amplification. On either side of \(2/3\), the open window between the two sharp thresholds is nonempty and has all eigenmodes decaying exponentially even though some initial states gain norm before decaying.

**4. Half-filling gain law.** When \(r=1/2\), the lower-left entry of \(A_k\) vanishes. The matrix exponential can therefore be computed without spectral eigenvector conditioning:
\[
e^{tA_k}=\begin{pmatrix}
e^{-k^2t}&-i(Pk/4)e^{-k^2t}(1-e^{-2t})\\
0&e^{-(k^2+2)t}
\end{pmatrix}.
\]
Its off-diagonal magnitude has unique maximum, for \(k>0\), at
\[
t_k=\frac12\log\left(1+\frac2{k^2}\right),
\quad\max_{t\ge0}\frac{k}{4}e^{-k^2t}(1-e^{-2t})
=\frac{k}{2(k^2+2)}\left(\frac{k^2}{k^2+2}\right)^{k^2/2}=C_k.
\]
For every time and every Fourier mode, the operator matrix equals its off-diagonal nilpotent part plus a diagonal contraction, hence the largest singular value lies between its off-diagonal magnitude and that magnitude plus one. Taking the supremum over time and integer \(k_n\) proves \(P C_L\le G_L(P)\le P C_L+1\). Because \(C_k\le1/(2k)\to0\) as \(k\to\infty\) and \(C_{k_1}>0\), the discrete maximum is finite and attained. In particular, eigenvalues independent of activity do not impose any activity-uniform bound on the full semigroup norm.

## Verification
The independent standalone file `verify.py` symbolically checks the Fourier matrix-square identity, Hermitian-part off-diagonal, determinant and half-filling triangularity, and the algebraic squared-width identity. It samples exact two-by-two matrix exponentials with SciPy, including a stable yet amplifying example with \((r,\mathrm{Pe},k)=(0.6,6,1)\), whose largest modal eigenvalue is approximately \(-0.03022844\) while a transient singular value reaches approximately \(1.019093\). At the exceptional density, \((r,\mathrm{Pe},k)=(2/3,5,1)\), the sampled peak is exactly one within numerical precision. For \(L=2\pi\), among the first 1000 Fourier modes sampled by the script the first has the largest value, approximately \(0.096225044865\), and the script checks corresponding large-activity gain brackets. This finite sample is not used to establish an all-mode maximizing index or the theorem. These finite computations are illustrations and algebraic crosschecks; the if-and-only-if statement is proved by the energy identity for every Fourier mode in the preceding argument.

To reproduce: execute `python verify.py` with Python, NumPy, SymPy and SciPy installed. The expected last line is `PASS: symbolic identities, stable nonmodal witnesses, half-filling gain bounds.`

## Relationship to prior work
Kourbane-Houssene et al. derive the exact nonlinear lattice-gas hydrodynamics and its ordinary eigenvalue spinodal criterion, including the finite-circumference onset; that spectral criterion is explicitly treated here as **known**. Agranov et al. give the same homogeneous-state Fourier linearization and compute steady-state fluctuation covariances using its forced propagator. Jose, Dandekar and Ramola diagonalize the related conjugate linearized Fourier matrix to compute current cumulants. These works determine the relevant deterministic generator and modal/eigenvalue physics, but the inspected materials do not report the unweighted species-norm transient-amplification phase portrait, its unique density \(2/3\) collapse, or the uniform activity-asymptotic operator-gain constant at half filling. A general two-dimensional triangular-semigroup contractivity calculation covers the isolated half-filling contractivity test as a mathematical special case; no novelty is attributed to that general matrix criterion by itself. The distinct contribution is its exact coupled-lattice-gas norm-versus-spectrum phase portrait and the quantified unbounded gain with an optimized all-mode coefficient.

## Limitations
This is linear response about a uniform state; it does not assert nonlinear transient growth for all finite disturbances, microscopic stochastic amplification, an experimental protocol, or a stochastic noise covariance bound. The chosen norm is intrinsic to Euclidean plus/minus species-density perturbations; a differently weighted norm can change transient thresholds. The infinite-space limit \(L\to\infty\) and finite microscopic-system corrections are not analyzed. The computation checker illustrates selected modes but is not the infinite-dimensional proof. A possibly unindexed direct treatment of the same nonmodal operator norm could reduce originality; no exhaustive literature uniqueness claim is made. No independent review or validation is claimed.

## References
1. M. Kourbane-Houssene, C. Erignoux, T. Bodineau, J. Tailleur, *Exact Hydrodynamic Description of Active Lattice Gases*, arXiv:1801.08952 (initial posting 2018-01-26), Physical Review Letters **120**, 268003 (2018), https://arxiv.org/abs/1801.08952.
2. T. Agranov, S. Ro, Y. Kafri, V. Lecomte, *Exact fluctuating hydrodynamics of active lattice gases: Typical fluctuations*, arXiv:2104.14650 (2021), https://arxiv.org/abs/2104.14650.
3. S. Jose, R. Dandekar, K. Ramola, *Current fluctuations in an interacting active lattice gas*, arXiv:2301.10680 (2023), https://arxiv.org/abs/2301.10680.
