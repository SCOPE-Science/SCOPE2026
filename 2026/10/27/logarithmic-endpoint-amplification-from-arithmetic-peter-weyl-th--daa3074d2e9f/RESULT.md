# Logarithmic endpoint amplification from arithmetic Peter–Weyl thinning on \(SU(2)\)

## Finding
For an integer \(q\ge3\), a residue \(1\le r\le q\), and \(M\ge1\), retain exactly the \(M\) irreducible \(SU(2)\) representations whose dimensions belong to \(\{r,q+r,\ldots,q(M-1)+r\}\). Let \(P_{q,r,M}\) denote the associated sum of full Peter–Weyl projections on Haar-normalized \(SU(2)\). Then
\[
\boxed{\|P_{q,r,M}\|_{L^1\to L^1}=\|P_{q,r,M}\|_{L^\infty\to L^\infty}=C_q M\log M+O_q(M),\qquad C_q=\frac8{\pi^2}\sum_{h=1}^{\lfloor(q-1)/2\rfloor}\sin\!\left(\frac{2\pi h}{q}\right)>0.}
\]
The coefficient is independent of the chosen residue. In particular, \(C_3=4\sqrt3/\pi^2\), and the first nontrivial arithmetic thinning yields \(\|P_{3,r,M}\|\sim(4\sqrt3/\pi^2)M\log M\) for every \(r=1,2,3\). In contrast, the same construction for \(q=1\) or \(q=2\) has endpoint norm \(O(M)\), with no logarithmic amplification.

## Assumptions and scope
The Haar probability measure on \(SU(2)\) and the conventional Peter–Weyl normalization are used. Its highest-weight-\(n\) irreducible representation has dimension \(n+1\); every selected irreducible contributes its entire matrix-coefficient space, not only the central character. The modulus \(q\) and residue \(r\) are fixed while \(M\to\infty\). The error constant is uniform among the finitely many residues at fixed \(q\). The statement concerns strong endpoint convolution-operator norms and makes no assertion about intermediate \(L^p\) norms or simultaneous growth of \(q\).

## Proof
Write the conjugacy class angle of a matrix in \(SU(2)\) as \(\theta\in[0,\pi]\). A representation of dimension \(d\) has character \(\chi_{d-1}(\theta)=\sin(d\theta)/\sin\theta\). The central convolution kernel of our projection is
\[
K_{q,r,M}(\theta)=\frac{T_{q,r,M}(\theta)}{\sin\theta},\qquad T_{q,r,M}(\theta)=\sum_{k=0}^{M-1}(qk+r)\sin((qk+r)\theta).
\]
Convolution by an integrable kernel has \(L^\infty\)- and \(L^1\)-operator norms equal to the \(L^1\)-mass of that kernel: a phase-sign test attains the former, and normalized approximate identities attain the latter. The Weyl integration formula consequently gives the exact identity
\[
\Lambda_{q,r,M}=\|P_{q,r,M}\|=\frac2\pi\int_0^\pi |T_{q,r,M}(\theta)|\sin\theta\,d\theta.
\]
Put \(z=e^{iq\theta}\). At \(z\ne1\), differentiating the finite geometric sum yields
\[
\sum_{k=0}^{M-1}(qk+r)e^{i(qk+r)\theta}=e^{ir\theta}\left[-\frac{qMz^M}{1-z}+\frac{qz(1-z^M)}{(1-z)^2}+\frac{r(1-z^M)}{1-z}\right].
\]
The first summand has imaginary part
\[
T_0(\theta)=-\frac{qM}{2\sin(q\theta/2)}\cos\!\left((qM+r-q/2)\theta\right).
\]
The remaining summands, denoted \(E\), obey \(\lvert E(\theta)\rvert\le C_q(\lvert1-e^{iq\theta}\rvert^{-2}+\lvert1-e^{iq\theta}\rvert^{-1})\). Set \(\Omega_M=qM+r-q/2\). Excise intervals of radius \(M^{-1}\) about every solution of \(e^{iq\theta}=1\) in \([0,\pi]\). There are finitely many such intervals at fixed \(q\). On each excised interval the elementary bound \(\lvert T\rvert\le\sum_{k<M}(qk+r)=O_q(M^2)\) gives integrated mass \(O_q(M)\). On the remaining set, the integral of \(\lvert E\rvert\sin\theta\) is \(O_q(M)\), since each second-order pole truncated at distance \(M^{-1}\) contributes at most \(O_q(M)\). By \(\bigl||T|-|T_0|\bigr|\le|E|\), it suffices to integrate \(\lvert T_0\rvert\sin\theta\) on the unexcised region.

The singularities of \(T_0\) at \(0\), and at \(\pi\) when \(q\) is even, have vanishing Weyl weight \(\sin\theta\); they contribute only \(O_q(M)\). Away from the poles the integrand is also \(O_q(M)\). The interior poles are exactly \(\theta_h=2\pi h/q\) for \(1\le h\le\lfloor(q-1)/2\rfloor\). For \(t=\theta-\theta_h\) sufficiently small,
\[
\frac{q\sin\theta}{2|\sin(q\theta/2)|}=\frac{\sin\theta_h}{|t|}+O_q(1),
\]
so the pole neighborhood produces
\[
M\sin\theta_h\int_{1/M<|t|<\delta}\frac{|\cos(\Omega_M(\theta_h+t))|}{|t|}\,dt+O_q(M).
\]
For \(\Omega_M=qM+O_q(1)\), periodic averaging gives the uniform logarithmic lemma
\[
\int_{1/M}^{\delta}\frac{|\cos(\Omega_M t+\phi_M)|}{t}\,dt=\frac2\pi\log M+O_q(1)
\]
for arbitrary phases \(\phi_M\). Indeed \(\lvert\cos x\rvert-2/\pi\) has a bounded periodic primitive; integrate by parts after the substitution \(u=\Omega_M t\). The lower endpoint \(\Omega_M/M\) stays bounded away from zero, so the primitive contributes only a bounded error uniformly in the phase. Both sides of the interior pole therefore contribute \((4/\pi)M\sin\theta_h\log M+O_q(M)\) before Haar normalization. Multiplying by \(2/\pi\) and summing proves the displayed coefficient and remainder. For \(q=1,2\), there are no interior poles, and the same estimates give \(O(M)\). This completes the proof.

## Verification
The standalone `verify.py` evaluates the character sum independently by finite summation and by its geometric rational identity, and computes the exact integral formula numerically by midpoint quadrature. It checks all modulus-residue choices for \(q=2,3,4,5,7\) at multiple truncations (8,288 finite assertions). Numerical differences of \(\Lambda_{q,r,M}/M\) over logarithmic scales corroborate \(C_3=0.7019737518\ldots\), \(C_4=0.8105694691\ldots\), and \(C_5=1.2473381554\ldots\). The finite tests do not substitute for the uniform logarithmic-averaging and error estimates in the proof.

## Relationship to prior work
Grow and Myers (2020, arXiv:2005.11245v1) establish the relevant \(SU(2)\) Fourier-partial-sum setting and use the classical representation and character decomposition to investigate pointwise convergence. Their full available text treats consecutive truncations and convergence phenomena, not the above arithmetic-progression endpoint constants. Their 2021 sequel similarly treats convergence in compact Lie groups. The 1986 sharp-order estimates of Giulini and Travaglini concern standard Dirichlet kernels on compact Lie groups.

Two nearby explicitly inspected mathematical results determine respectively the endpoint norm of a *single* full Peter–Weyl block and the sharp leading coefficient for the *consecutive* low-pass sum of blocks on \(SU(2)\). Neither entails the logarithmic enhancement for retaining every \(q\)-th block. The difference is structural: thinning inserts root-of-unity singularities at interior conjugacy angles where the Weyl weight is nonzero, whereas all-block truncations lack these interior poles.

## Limitations
The modulus is fixed as the number of retained representations grows. This is not a result for arbitrary sparse sets of highest weights, all compact groups, or general multiplier norms. The exact positive logarithmic coefficient proves distinct behavior from consecutive cutoffs, but a related theorem under different spectral-sampling terminology could still exist in older literature not exhaustively searched. No independent mathematical audit is claimed.

## References
1. D. Grow and D. Myers, *Almost everywhere convergence of Fourier series on SU(2): the case of Hölder continuous functions*, arXiv:2005.11245v1 (first public 22 May 2020), https://arxiv.org/html/2005.11245v1.
2. D. Grow and D. Myers, *Almost everywhere convergence of Fourier series on compact connected Lie groups*, arXiv:2108.12997v1 (2021), https://arxiv.org/html/2108.12997v1.
3. S. Giulini and G. Travaglini, *Sharp Estimates for Lebesgue Constants on Compact Lie Groups*, J. Functional Analysis 68 (1986), 106–116, DOI 10.1016/0022-1236(86)90059-5.
4. C. Meaney, *Unbounded Lebesgue Constants on Compact Groups*, Monatshefte für Mathematik 91 (1981), 119–130, DOI 10.1007/BF01295142.
