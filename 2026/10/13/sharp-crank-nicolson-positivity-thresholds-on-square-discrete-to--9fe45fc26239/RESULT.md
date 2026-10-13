# Sharp Crank–Nicolson positivity thresholds on square discrete tori

## Finding
For every integer \(n\ge3\), let \(L_n\) be the combinatorial Laplacian on the square periodic lattice \(C_n\square C_n\), with one unit-rate edge to each of the four nearest neighbors (the four neighbors are distinct for \(n\ge3\)). Define the Crank–Nicolson matrix for the discrete heat equation \(u'=-L_nu\) by
\[
T_n(h)=\left(I+\frac h2L_n\right)^{-1}\left(I-\frac h2L_n\right),\qquad h\ge0.
\]
Put \(s=h/2\), \(\Lambda_{jk}=4-2\cos(2\pi j/n)-2\cos(2\pi k/n)\), and
\[
G_n(s)=\frac1{n^2}\sum_{j,k=0}^{n-1}\frac1{1+s\Lambda_{jk}}.
\]
There is a unique \(s_n>0\) satisfying \(G_n(s_n)=1/2\). **Exactly** for \(0\le h\le2s_n\), the Crank–Nicolson matrix is entrywise nonnegative (and hence doubly stochastic). For \(h>2s_n\), precisely its diagonal entries become negative; every off-diagonal entry is strictly positive whenever \(h>0\). The thresholds strictly decrease with torus size:
\[
s_3>s_4>\cdots>s_\infty>0,\qquad s_3=\frac{1+\sqrt{57}}{28}.
\]
The limiting threshold \(s_\infty\) is the unique positive solution of
\[
\frac{2}{\pi(1+4s_\infty)}K\!\left(\frac{4s_\infty}{1+4s_\infty}\right)=\frac12,
\qquad K(k)=\int_0^{\pi/2}\frac{dt}{\sqrt{1-k^2\sin^2t}}.
\]
Numerically, \(s_\infty=0.294098641842814\ldots\), so the limiting **physical step** is \(2s_\infty=0.588197283685628\ldots\), strictly larger than the direct nonnegative-stencil sufficient bound \(h\le1/2\).

The convergence is exponentially fast, with an explicit global bound. Let \(r=4s_\infty/(1+4s_\infty)\in(0,1)\) and \(a=(1+\sqrt{57})/28\). Then every \(n\ge3\) satisfies
\[
0<s_n-s_\infty\le\frac{(1+8a)^2r^n}{(1-r^n)^2}.
\]
These statements are one characterization of the exact finite-size and thermodynamic positivity frontier for the stated unmodified scheme.

## Assumptions and scope
The vertices are \((j,k)\in(\mathbb Z/n\mathbb Z)^2\), and \(L_n=4I-A_n\), where \(A_n\) has one unit entry for each cardinal nearest neighbor. There is no spatial mesh-length scaling hidden in \(L_n\): for a physical square mesh spacing \(\Delta x\) and diffusion coefficient \(D\), the dimensionless \(h\) here is \(D\Delta t/(\Delta x)^2\). Entrywise positivity means the evolution preserves **every** nonnegative vector, not just selected smooth initial data. At \(h=0\), \(T_n(0)=I\); no strict off-diagonal positivity is claimed there. Only equal square periods \(n\times n\) and unit isotropic coupling are included.

## Proof
**1. All signs reduce to one diagonal Green value.** Set \(B_n(s)=I+sL_n\). The matrix \(B_n(s)\) is a nonsingular irreducible \(M\)-matrix for \(s>0\), and
\[
B_n(s)^{-1}=\int_0^\infty e^{-t}e^{-stL_n}\,dt
\]
is strictly positive entrywise. Since \(T_n(2s)=2B_n(s)^{-1}-I\), every off-diagonal entry of \(T_n(2s)\) is positive. Translation symmetry makes all diagonal entries identical. Fourier diagonalization yields \((B_n(s)^{-1})_{vv}=G_n(s)\) at every vertex \(v\). Hence \(T_n(2s)\ge0\) entrywise exactly when \(G_n(s)\ge1/2\). Also \(T_n(2s)\mathbf1=\mathbf1\), and symmetry gives column sums one. The Fourier eigenvalues satisfy \(\Lambda_{00}=0\), \(0<\Lambda_{jk}\le8\) otherwise. Therefore \(G_n(0)=1\), \(G_n'(s)<0\), and \(G_n(s)\to1/n^2<1/2\) as \(s\to\infty\). The crossing \(s_n\) exists and is unique. For \(n=3\), the Laplacian eigenvalues are \(0,3,6\) with multiplicities \(1,4,4\), respectively, and \(G_3(s)=\bigl(1+4/(1+3s)+4/(1+6s)\bigr)/9\). Thus the threshold equation is \(14s^2-s-1=0\) and gives the stated \(s_3\).

**2. Strict size monotonicity and limit.** On \(\mathbb Z^2\), define the massive Green kernel
\[
g_s(p,q)=\int_0^\infty e^{-(1+4s)t}I_{|p|}(2st)I_{|q|}(2st)\,dt,
\]
where \(I_m\) is the usual modified Bessel function of integer order. Periodizing the nearest-neighbor heat kernel gives
\[
G_n(s)=\sum_{(p,q)\in\mathbb Z^2}g_s(np,nq).
\]
For every \(z>0\), \(I_0(z)>I_1(z)>I_2(z)>\cdots>0\). One elementary justification is to consider the one-dimensional heat kernel \(u_m(t)=e^{-2t}I_m(2t)\) and its differences \(v_m=u_m-u_{m+1}\) on the nonnegative half-line. They obey \(v'_0=-3v_0+v_1\) and \(v'_m=v_{m-1}-2v_m+v_{m+1}\) for \(m\ge1\), starting from \(v_0(0)=1\), \(v_m(0)=0\) for \(m\ge1\); positivity and irreducibility of this cooperative system give \(v_m(t)>0\) for \(t>0\). Thus \(g_s(p,q)\) strictly decreases in each absolute coordinate. Every nonzero term of the periodization sum for size \(n\) therefore strictly exceeds its counterpart for size \(n+1\), so \(G_n(s)>G_{n+1}(s)\) for each \(s>0\). Since each \(G_n\) strictly decreases in \(s\), its \(1/2\)-crossings satisfy \(s_n>s_{n+1}\). The Green kernel has unit total mass, so the sum over the nonzero images tends to zero and \(G_n(s)\downarrow g_s(0,0)\) for each fixed \(s>0\).

Integrating the infinite-lattice Fourier symbol yields
\[
G_\infty(s)=g_s(0,0)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}\frac{d\theta\,d\phi}{1+4s-2s\cos\theta-2s\cos\phi}
=\frac{2}{\pi(1+4s)}K\!\left(\frac{4s}{1+4s}\right).
\]
The last equality follows by integrating one angular variable via \(\int_0^{2\pi}(a-b\cos\phi)^{-1}d\phi=2\pi/\sqrt{a^2-b^2}\), then using the tangent half-angle substitution and the defining complete-elliptic-integral substitution. This identity is the classical square-lattice Green integral, not a novelty assertion. The function \(G_\infty\) decreases continuously from one to zero, so it has a unique \(1/2\)-crossing. Monotone convergence of \(G_n\), together with \(s_n\le s_3\), yields \(s_n\downarrow s_\infty\).

**3. Quantitative rate.** Write \(P=A_{\mathbb Z^2}/4\) for the simple nearest-neighbor transition kernel, and \(r_s=4s/(1+4s)\). The geometric resolvent expansion is
\[
g_s(p,q)=(1-r_s)\sum_{\ell\ge0}r_s^\ell (P^\ell)_{(0,0),(p,q)}.
\]
A path to \((p,q)\) has length at least \(|p|+|q|\), hence \(0\le g_s(p,q)\le r_s^{|p|+|q|}\). At \(s=s_\infty\), summing all nonzero periodization images gives
\[
0<G_n(s_\infty)-\tfrac12\le\left(\frac{1+r^n}{1-r^n}\right)^2-1=\frac{4r^n}{(1-r^n)^2}.
\]
For \(0\le s\le a=s_3\), \(-G_n'(s)=n^{-2}\sum\Lambda_{jk}/(1+s\Lambda_{jk})^2\ge4/(1+8a)^2\), using \(\Lambda_{jk}\le8\) and \(n^{-2}\sum\Lambda_{jk}=4\). The mean-value theorem applied between \(s_\infty\) and \(s_n\) gives the claimed exponential bound. This completes the proof.

## Verification
The accompanying `verify.py` uses Python's standard library only. It constructs exact rational Crank–Nicolson matrices on the \(3\times3\) and \(4\times4\) tori at two rational parameter values, verifies all row sums and strict off-diagonal signs, and compares rational diagonal resolvent entries against the Fourier formula. It then checks the exact \(n=3\) root identity, computes threshold roots for ten finite tori, evaluates the limiting elliptic integral independently through the arithmetic-geometric mean, and checks the explicit exponential envelope. Run with `python3 verify.py`. The output is `VERIFY_OK 714 rational matrix entries and Fourier/elliptic thresholds`. This finite checker is not a substitute for the preceding all-\(n\) proof.

## Relationship to prior work
The general identity \(T=2(I+sL)^{-1}-I\), and the reduction of positivity to resolvent diagonals for irreducible Markov generators, are elementary and previously known. Faragó, Korotov and Szabó (2010) analyze nonnegativity for one- and two-dimensional heat discretizations; their full text proves exact one-dimensional bounds and gives sufficient two-dimensional conditions for rectangular homogeneous Dirichlet problems, explicitly noting that necessary-and-sufficient two-dimensional criteria were not obtained there. Higueras and Roldán (2023) give sharp finite-size Crank–Nicolson positivity and contractivity criteria for the **one-dimensional Dirichlet** problem. The classical elliptic evaluation of the square-lattice Green kernel predates this finding (Morita, 1971). The contribution asserted here is specifically the all-size **two-dimensional periodic square-torus** positivity cutoff, strict size ordering, elliptic thermodynamic limit and quantitative finite-size decay. These are not implied as numerical thresholds by a general diagonal-positivity criterion alone.

## Limitations
Only the stated linear, isotropic, nearest-neighbor periodic square lattice and unmodified Crank–Nicolson step are covered. No claim is made for Dirichlet boundaries, anisotropic meshes, nonlinear heat equations, different integrators or exact arithmetic behavior of a floating-point implementation. The limiting elliptic value is defined by a proved unique equation; its printed decimals are approximate. Historical literature might contain an equivalent periodic-two-dimensional specialization not identified in the accessed material, including an incompletely accessible periodic-diffusion manuscript cited by Higueras and Roldán. The mathematical proof here is independent of any historical novelty assertion; no independent validation has been performed.

## References
- T. Morita, “Useful Procedure for Computing the Lattice Green's Function—Square, Tetragonal, and bcc Lattices,” *Journal of Mathematical Physics* **12** (1971), 1744–1747, DOI: 10.1063/1.1665800; publication date recorded as 1971-08-01. https://cir.nii.ac.jp/crid/1360292618700564608
- I. Faragó, S. Korotov and T. Szabó, “Non-negativity preservation of the discrete nonstationary heat equation in 1D and 2D,” *Aplimat—Journal of Applied Mathematics* **3** (2010), 60–81. https://www.researchgate.net/publication/236611280_Non-negativity_preservation_of_the_discrete_nonstationary_heat_equation_in_1D_and_2D
- I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066 (first submitted 2023-01-03). https://arxiv.org/abs/2301.01066
- A. J. Guttmann, “Lattice Green functions in all dimensions,” arXiv:1004.1435 (first submitted 2010-04-08). https://arxiv.org/abs/1004.1435
