# A sharp dephasing-assistance threshold for thermally driven bosonic number transport

## Finding

The stationary **excitation-number** current through a detuned, thermally driven bosonic three-site chain has a unique optimal middle-site dephasing rate. For all \(J,\kappa>0\), \(\delta\in\mathbb R\), and \(n_L>n_R\ge0\), it is
\[
\gamma_*=\max\left\{0,2|\delta|-\kappa-\frac{4J^2}{\kappa}\right\}.
\]
Strict improvement over the dephasing-free current occurs if and only if
\[
|\delta|>\frac{\kappa}{2}+\frac{2J^2}{\kappa}.
\]
In the enhancement regime the exact maximum is \(\mathcal J_{\max}=J^2(n_L-n_R)/(2|\delta|)\). At and below the threshold zero dephasing remains the unique global optimum. These statements classify every nonnegative dephasing strength, not just an infinitesimal perturbation.

## Assumptions and scope

Use units with Planck's reduced constant equal to one. The three bosonic annihilation operators satisfy the canonical commutation relations. The number-conserving rotating-wave Hamiltonian is
\[
H=\omega\sum_{j=1}^3a_j^\dagger a_j+\delta a_2^\dagger a_2+J\sum_{j=1}^2(a_j^\dagger a_{j+1}+a_{j+1}^\dagger a_j),
\]
where \(J>0\), \(\delta\in\mathbb R\), and the common frequency \(\omega\) is irrelevant to excitation-number dynamics. The Lindblad generator is \(\mathcal L=-i[H,\cdot]+\mathcal L_L+\mathcal L_R+\gamma\mathcal D[a_2^\dagger a_2]\), where
\[
\mathcal L_L=\kappa(n_L+1)\mathcal D[a_1]+\kappa n_L\mathcal D[a_1^\dagger],\qquad
\mathcal L_R=\kappa(n_R+1)\mathcal D[a_3]+\kappa n_R\mathcal D[a_3^\dagger],
\]
\(\kappa>0\), \(n_L>n_R\ge0\), \(\gamma\ge0\), and \(\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\). Dephasing acts **only on site 2** with the coefficient exactly as written; coherences touching that site decay at rate \(\gamma/2\) due to this channel. The observable is the stationary number flux \(\mathcal J=2J\operatorname{Im}\langle a_2^\dagger a_1\rangle\), not a thermodynamic heat flux (which may contain boundary coherence-energy contributions). Equal contact strengths and equal nearest-neighbor hopping are essential assumptions.

## Proof

Define \(C_{ij}=\langle a_j^\dagger a_i\rangle\) (the transpose of another common covariance convention), \(h=\begin{psmallmatrix}0&J&0\\J&\delta&J\\0&J&0\end{psmallmatrix}\), and \(P=\operatorname{diag}(1,0,1)\). The exact closed second-moment equation is
\[
\dot C=-i[h,C]-\frac{\kappa}{2}\{P,C\}+\kappa\operatorname{diag}(n_L,0,n_R)-\frac{\gamma}{2}R(C),
\]
where \(R(C)_{ij}=C_{ij}\) when \(i\ne j\) and one index equals 2, and zero otherwise. The first and last diagonal equations give a conserved number current across both bonds.

Write \(q=n_L-n_R>0\), \(t=4J^2+\kappa(\kappa+\gamma)>0\), and \(B=t^2+4\delta^2\kappa^2>0\). Direct solution of all nine independent real stationary moment equations gives
\[
x=\frac{J\kappa q t}{B},\quad
u=-\frac{2\delta J\kappa^2q}{B},\quad
z=-\frac{4\delta J^2\kappa q}{B},
\]
\[
C=\begin{pmatrix}
n_L-2Jx/\kappa&u+ix&iz\\
u-ix&(n_L+n_R)/2&-u+ix\\
-iz&-u-ix&n_R+2Jx/\kappa
\end{pmatrix}.
\]
This also proves the exact middle occupation \(\langle a_2^\dagger a_2\rangle=(n_L+n_R)/2\), independent of central detuning and dephasing. Substitution into every moment equation gives zero. The solution is unique: if a Hermitian matrix \(X\) solves the homogeneous stationary equation, taking the real Hilbert--Schmidt inner product with \(X\) makes all dissipative quadratic terms nonpositive, and enforces that all entries touching an endpoint vanish. The remaining matrix is a multiple of \(P_2\); its commutator with \(h\) vanishes only when that multiple is zero, since \(J>0\). Hence the stationary covariance is unique for every allowed parameter, including \(\gamma=0\).

Taking the left-bond flux gives the **exact rational current**
\[
\mathcal J(\gamma)=2Jx=\frac{2J^2\kappa q t}{t^2+4\delta^2\kappa^2}.
\]
The map \(\gamma\mapsto t=t_0+\kappa\gamma\) is a bijection from \([0,\infty)\) onto \([t_0,\infty)\), with \(t_0=4J^2+\kappa^2\). Set \(a=2|\delta|\kappa\). The derivative of \(f(t)=t/(t^2+a^2)\) is \(f'(t)=(a^2-t^2)/(t^2+a^2)^2\). Therefore its unique global maximizer on that half-line is \(t_*=\max\{t_0,a\}\), including the threshold \(a=t_0\), where it is still unique. Solving \(t_*=t_0+\kappa\gamma_*\) yields the advertised optimizer and threshold. When \(a>t_0\), substituting \(t=a\) gives \(\mathcal J_{\max}=J^2q/(2|\delta|)\) and enhancement ratio \(\mathcal J_{\max}/\mathcal J(0)=\frac12(a/t_0+t_0/a)>1\). When \(\delta=0\), \(f(t)=1/t\) decreases strictly, so no singular special case remains.

## Verification

Two attached standalone programs check distinct parts of the claim. Run `python check_symbolic.py` (SymPy) to substitute the displayed covariance into all nine steady moment equations over symbolic real parameters; all nine residuals vanish identically. Run `python check_numeric.py` (NumPy) to solve independently generated nine-real-variable covariance systems for 256 randomized parameter sets and compare to the displayed exact solution; then test the global optimum against 1,750 sampled competitor rates. Both programs passed when executed from the embedded deliverable. These checks complement, but do not replace, the exact algebraic proof and derivative-sign argument.

## Relationship to prior work

Asadian, Manzano, Tiersch and Briegel (2012) establish the bosonic lattice, thermal Lindblad contacts and second-moment heat-transport formalism, and solve uniform-frequency chains with spatially uniform local dephasing. Their homogeneous dispersion and dephasing formulas do not directly yield a selectively dephased, centrally detuned trimer's global optimizer. Contreras-Pulido, Bruderer, Huelga and Plenio (2014) show dephasing-assisted steady current in a detuned **Coulomb-blockaded electronic** triple dot driven by injection and extraction, with dephasing applied at all sites; its currents have different denominators and different Lindblad sources. Their threshold does not imply the present bosonic thermal-reservoir, single-dephased-site formula merely through relabeling. Žnidarič and Horvat (2012) analyze an XX-chain/disordered-chain transport problem with dephasing and a thermodynamic-limit conductivity optimum, not the exact finite three-oscillator thermal-drive classification.

The contribution is the explicit steady **number-current** phase boundary and its unique optimal dephasing rate, not the general phenomenon of noise-enhanced transport. Priority cannot be conclusively established from search coverage; an equivalent theorem in unexamined primary work remains a residual risk.

## Limitations

This result assumes a number-conserving rotating-wave bosonic chain of precisely three sites, identical nearest-neighbor hopping, equal Markovian boundary damping rates, time-independent bath occupations, and Lindblad pure dephasing on the **central** site only. It is not a statement about interacting bosons, fermionic Coulomb blockade, heat/energy flow (with potentially nonzero boundary coherence contributions), time-dependent controls, dephasing at the endpoints, or chains of other lengths. Analytical uniqueness was established for stationary second moments; global uniqueness of the full infinite-dimensional bosonic density operator is not independently asserted. The outcome is a theoretical exactly soluble benchmark, with no experimental or priority certification claimed.

## References

1. A. Asadian, D. Manzano, M. Tiersch and H. J. Briegel, *Heat transport through lattices of quantum harmonic oscillators in arbitrary dimensions*, arXiv:1204.0904, first publicly submitted 2012-04-04, https://arxiv.org/html/1204.0904v1 .
2. L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga and M. B. Plenio, *Dephasing-assisted transport in linear triple quantum dots*, arXiv:1407.0924, first publicly submitted 2014-07-03, https://arxiv.org/html/1407.0924v2 .
3. M. Žnidarič and M. Horvat, *Transport in a disordered tight-binding chain with dephasing*, arXiv:1207.5952, first publicly submitted 2012-07-25, https://arxiv.org/html/1207.5952v2 .
