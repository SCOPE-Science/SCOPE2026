# Mixed-boundary thermal-mode tomography and sharp arithmetic heating bounds

## Finding
Consider the standard equal-mass nearest-neighbor harmonic chain with \(N\ge2\) mobile sites, a mechanically free left end, a fixed right end, and identical positive viscous damping at each mobile site. Each site has an independent local Langevin reservoir with nonnegative temperature \(T_j\), and the chain has positive spring stiffness. Let \(\Theta_k\) be the stationary kinetic temperature of normal mode \(k\), i.e. twice its mean kinetic energy in units with Boltzmann's constant and mass equal to one.

Put \(M=2N+1\), \(0\le j,k<N\), and
\[
Q_{kj}=\frac{2}{M}\left[1+\cos\left(\frac{\pi(2k+1)(2j+1)}{M}\right)\right].
\]
Then \(\Theta=QT\), and the *exact inverse and squared-transfer identities* are
\[
\boxed{Q^2=\frac{I+2\mathbf1\mathbf1^{\mathsf T}}{M},\qquad
T=M Q\Theta-2(\mathbf1^{\mathsf T}\Theta)\mathbf1.}
\]
All \(N\) bath temperatures are uniquely recoverable from the \(N\) modal kinetic temperatures. The singular values of \(Q\) are \(1\) once and \(M^{-1/2}\) with multiplicity \(N-1\), so its exact Euclidean condition number is \(\sqrt M\). The set of physically attainable modal-temperature vectors for nonnegative baths is exactly the simplicial cone
\[
\boxed{M(Q\Theta)_j\ge2\sum_{k=0}^{N-1}\Theta_k \quad(0\le j<N).}
\]
For strictly positive reservoirs all these inequalities are strict. The inverse, feasibility criterion, and sharp stability hold for every positive spring constant and damping coefficient.

Furthermore, let \(H=\sum_{j=0}^{N-1}T_j>0\) be a prescribed total heating budget, fix a mode \(k\), and put \(g=\gcd(2k+1,M)\). Over all nonnegative bath allocations of total \(H\), the exact attainable extrema are
\[
\boxed{\Theta_k^{\max}=\frac{2H}{M}\left(1+\cos\frac{\pi g}{M}\right),}
\]
\[
\boxed{\Theta_k^{\min}=\begin{cases}0,&g>1,\\
\frac{2H}{M}(1-\cos\frac{2\pi}{M}),&g=1.
\end{cases}}
\]
The maximum is attained by placing all heat on any one of exactly \(g\) maximizing bath sites, or by distributing it among them. If \(g>1\), exactly \((g-1)/2\) bath sites are perfectly dark to mode \(k\); allocations supported on those sites attain zero modal heating. For \(g=1\), precisely one minimizing site exists and the minimum is strictly positive. For strictly positive bath temperatures and fixed \(H\), these are sharp suprema and infima, attained only when the selected extremizing set includes every site (not for \(N\ge2\)).

The common modal-temperature sum is conserved: \(\sum_k\Theta_k=H\). Consequently the inverse geometry and arithmetic extrema describe redistributing—not creating—modal kinetic temperature.

## Assumptions and scope
The mechanical stiffness on \(N\) mobile sites is \(\kappa L\), where \(\kappa>0\), \(L_{00}=1\), \(L_{jj}=2\) for \(1\le j<N\), \(L_{j,j+1}=L_{j+1,j}=-1\), and other entries vanish. In vector form the dynamics are
\[
\ddot X=-\gamma\dot X-\kappa LX+\xi,
\qquad
\mathbb E[\xi_i(t)\xi_j(s)]=2\gamma T_j\delta_{ij}\delta(t-s),
\]
where \(\gamma>0\). The stationary system is stable because \(L\) is positive definite and damping is positive. Every \(T_j\ge0\); its positivity is not assumed in the algebra. The mobile indices \(j=0,\ldots,N-1\) and normal-mode indices \(k=0,\ldots,N-1\) start at zero. \(\Theta_k=\mathbb E[(u_k^{\mathsf T}\dot X)^2]\) for unit-normalized real eigenvectors \(u_k\) of \(L\), indexed by increasing eigenfrequency. Only same-site modal energies are used, not cross-mode correlations.

## Proof
**1. Forward transfer.** The unit eigenvectors of the mixed free/fixed stiffness are
\[
u_{jk}=\sqrt{\frac4M}\cos\left(\frac{\pi(2j+1)(2k+1)}{2M}\right).
\]
The spectral noise intensity in mode \(k\) is \(2\gamma\sum_j u_{jk}^2T_j\). For the scalar damped oscillator, the stationary kinetic variance equals its noise intensity divided by \(2\gamma\). Therefore \(\Theta_k=\sum_j u_{jk}^2 T_j\), giving \(Q_{kj}=u_{jk}^2\) exactly. This is the established forward modal-temperature relation of Falasco et al., Eq. (11); it is not claimed as new.

**2. Inverse and singular values.** Let \(C_{kj}=\cos(\pi(2k+1)(2j+1)/M)\) and \(J=\mathbf1\mathbf1^{\mathsf T}\). The finite odd-frequency cosine sums give
\[
C\mathbf1=\tfrac12\mathbf1,
\qquad C^2=\frac M4I-\frac12J.
\]
Indeed, for each integer \(s\) with \(1\le|s|<M\),
\[
\sum_{j=0}^{N-1}\cos\left(\frac{2\pi s(2j+1)}M\right)=-\frac12,
\]
whereas the sum for \(s=0\) is \(N\). Applying the product-to-sum identity to \(C_{kj}C_{j\ell}\) yields the displayed square identity; the single odd-frequency sum gives \(C\mathbf1=\mathbf1/2\). Because \(Q=2(J+C)/M\), \(J^2=NJ\), and \(JC=CJ=J/2\), direct multiplication proves
\[
Q^2=\frac{I+2J}{M}.
\]
Also \(Q\mathbf1=\mathbf1\), so \(Q\) preserves the sum. Multiply \(\Theta=QT\) by \(M Q-2J\): since \((M Q-2J)Q=I\), the inverse formula follows. The square identity gives a singular value of \(1\) in direction \(\mathbf1\), and \(M^{-1/2}\) on its orthogonal complement. Since \(N\ge2\), both occur, yielding the exact condition number \(\sqrt M\). For all vectors \(h\),
\[
\|Qh\|_2^2=\frac{\|h\|_2^2+2(\mathbf1^{\mathsf T}h)^2}{M}.
\]
In particular, the inverse amplifies any mean-zero modal measurement error by precisely \(\sqrt M\). Invertibility identifies the nonnegative bath cone exactly by substituting the inverse and requiring its coordinates nonnegative. Linear invertibility also establishes that this cone is simplicial.

**3. Arithmetic heating envelopes.** Set \(m=2k+1\), \(r=2j+1\) and \(g=\gcd(m,M)\). The attainable \(r\) are exactly the odd integers \(1,3,\ldots,M-2\). Since \(m/g\) is invertible modulo \(2M/g\), the closest attainable residues of \(mr\) to zero modulo \(2M\) are precisely \(\pm g\). Hence the largest \(\cos(\pi mr/M)\) is \(\cos(\pi g/M)\). The congruences \(mr\equiv\pm g\pmod{2M}\) yield exactly \(g\) sites in the allowed half-range \(r<M\): this uses pairing of \(r\) with \(2M-r\).

The cosine reaches \(-1\) exactly when \(mr\equiv M\pmod{2M}\), equivalent to \(r\equiv M/g\pmod{2M/g}\). For \(g>1\), its valid solutions are
\[
r=(2\ell+1)\frac{M}{g},\qquad 0\le\ell<\frac{g-1}{2},
\]
which gives precisely \((g-1)/2\) dark sites. For \(g=1\), the only solution would be \(r=M\), excluded from the mobile sites. Because multiplication by \(m\) permutes the odd residue classes modulo \(2M\) and the allowed sites contain one representative from each pair \(\{r,2M-r\}\) except \(r=M\), the nearest residue to \(M\) is \(M\pm2\), attained at precisely one site. This proves the minimum cosine \(-\cos(2\pi/M)\). Finally, the fixed-budget modal temperature is a linear convex combination \(\Theta_k=H\sum_j (T_j/H)Q_{kj}\); its extrema equal \(H\) times the minimum and maximum matrix entries and attainments are exactly the distributions supported on the extremizing sites. The strict-temperature statement follows by positive approximation.

## Verification
Run `python checker.py` with NumPy and SciPy. The standalone checker independently diagonalizes the mixed-boundary stiffness and solves the continuous-time Langevin stationary Lyapunov equation, alongside transfer identities, inversions, and arithmetic extrema. In the completed verification, 745 matrix/recovery/norm tests, 36,055 arithmetic comparisons, and 44 independent Lyapunov tests passed. Finite numerical tests are not a proof for unbounded \(N\); the preceding finite trigonometric identities and modular argument are the proof.

For illustration take \(N=4\), \(M=9\), and mode \(k=1\). Then \(g=\gcd(3,9)=3\). Exactly one bath site, \(j=1\), is dark to this mode, while \(j=0,2,3\) each maximize its response. With total budget \(H\), its exact attainable heating interval is \([0,H/3]\).

## Relationship to prior work
The earlier paper by Falasco, Baiesi, Molinaro, Conti and Baldovin (2015) derives the forward mixed-boundary modal-temperature formula and explores how boundary conditions affect mode energies. It also gives an inverse reconstruction of *reflection-paired* temperatures for free boundaries. Thus neither the linear Langevin model nor the forward cosine-square response nor the free-boundary inverse is new. The present theorem concerns a distinct set of conclusions not supplied there: complete mixed-boundary inverse, exact nonnegative realizability cone, exact singular-value amplification, and gcd-selected sharp heating extrema and dark-bath multiplicities. All are derived from its known forward equation, so the relationship is close and historical priority for the consequences remains a risk. Standard odd-length discrete cosine transform identities underpin the matrix calculation; no novelty is claimed for general Fourier orthogonality. Published mathematical-record and literature queries did not reveal equivalent statements, but absence from search cannot certify novelty.

## Limitations
The result assumes equal masses, nearest-neighbor uniform positive springs, sitewise identical damping, independent white Langevin noise, and exactly one free and one fixed mechanical boundary. It does not assert that all mode temperature covariances vanish: off-diagonal noise and modal correlations can persist. Nor does it generalize to boundary-only thermal reservoirs, nonlinear oscillator interactions, arbitrary temperature measurement noise, or finite-sample estimation. The condition number is Euclidean and exact for the mathematical forward operator; physical measurement uncertainties may depend on mode. The original source's forward formula is strong prior coverage, so all originality conclusions for the new inverse/arithmetic classification remain provisional until independent examination.

## References
1. G. Falasco, M. Baiesi, L. Molinaro, L. Conti and F. Baldovin, *Energy repartition for a harmonic chain with local reservoirs*, arXiv:1505.05088 (first public preprint 2015-05-19); Phys. Rev. E 92, 022129 (2015), https://doi.org/10.1103/PhysRevE.92.022129. Relevant original formulas: Eqs. (6), (8), (9)–(12), Appendix A Eq. (A13), and Appendix C.
2. *Discrete cosine transform*, discussion of odd-length types V–VIII and boundary conventions, https://en.wikipedia.org/wiki/Discrete_cosine_transform. Background transform context only; the finite trigonometric identities used here are proved above.
