# Universal weak-dephasing escape and its exact quadratic correction on mirror-protected quantum paths

## Finding

**Theorem.** Fix an integer \(L\geq 1\), a nonzero real hopping amplitude \(g\), and an absorption strength \(\kappa>0\). On the path with vertices \(-L,-L+1,\ldots,L\), let \(H\) be its nearest-neighbor hopping Hamiltonian, let \(P_j=|j\rangle\langle j|\), and let \(\mathcal L_\gamma\) be the trace-decreasing, site-dephased generator
\[
H=g\sum_{j=-L}^{L-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|),\qquad
\mathcal L_\gamma(X)=-i[H,X]-\frac{\kappa}{2}\{P_0,X\}+\gamma\left(\sum_{j=-L}^LP_jXP_j-X\right).
\]
For \(\gamma>0\) define the asymptotic survival-decay exponent by
\[
\Delta_L(\gamma)=-\max\{\operatorname{Re}z:z\in\sigma(\mathcal L_\gamma)\}.
\]
Then every eigenvalue of \(\mathcal L_\gamma\) has strictly negative real part. For sufficiently small positive \(\gamma\), the spectral abscissa is attained by a **single, simple, real eigenvalue**. Its negative has the expansion
\[
\boxed{\Delta_L(\gamma)=\frac{\gamma}{2}-\left(\frac{L}{4\kappa}+\frac{\kappa(L+1)(L+2)}{192g^2}\right)\gamma^2+O_{L,g,\kappa}(\gamma^3).}
\]
For any density matrix initially supported on the reflection-antisymmetric sector, its remaining trace has the same asymptotic exponential decay rate for sufficiently small \(\gamma>0\), with a nonzero leading amplitude. The coefficient \(1/2\) is independent of system size, coherent hopping, and absorber strength, whereas the exact quadratic correction separates an inverse-capture term from a length-dependent coherent-transport term.

## Assumptions and scope

The one-particle Hilbert space has dimension \(2L+1\); the outer path endpoints are open, not periodic. The walker is distinguishable and noninteracting, and the hopping amplitude has the same value on every edge. The central absorber removes amplitude at the rate \(\kappa\); the reduced, unabsorbed generator is trace decreasing. Site dephasing is Markovian, spatially uniform, and independent between sites, with off-diagonal decay rate \(\gamma\). The asymptotic statement fixes \(L,g,\kappa\) and then lets \(\gamma\) tend to zero; it is not uniform in growing \(L\) or singular absorber/hopping limits.

The reflection-antisymmetric orthonormal basis consists of \(|a_s\rangle=(|s\rangle-|-s\rangle)/\sqrt2\), \(1\leq s\leq L\); the reflection-symmetric basis consists of \(|0\rangle\) and \(|b_s\rangle=(|s\rangle+|-s\rangle)/\sqrt2\). Write \(P_-\) for the projector onto the antisymmetric space and \(B=\sum_{s=1}^{L}|b_s\rangle\langle b_s|\) for the noncentral symmetric projector.

## Proof

**1. Identify the complete zero-noise peripheral space.** The Hamiltonian commutes with reflection and decomposes into the antisymmetric Jacobi matrix \(H_-\) of an \(L\)-vertex path with edge weight \(g\) and the symmetric Jacobi matrix \(H_+\) on \(|0\rangle,|b_1\rangle,\ldots,|b_L\rangle\). The bright hoppings are \(t_0=\sqrt2g\) from the center to \(|b_1\rangle\) and \(t_s=g\) thereafter. The central absorber vanishes on the antisymmetric space. Its bright amplitude matrix is
\[
A_+=-iH_+-\frac{\kappa}{2}|0\rangle\langle0|.
\]
Every eigenvalue of \(A_+\) has strictly negative real part: an eigenvector with zero real part would have zero central component, forcing every remaining component to vanish by the tridiagonal recurrence because every \(t_s\neq0\). The noise-free Liouvillian therefore has purely imaginary eigenvalues only on operators supported within the dark block. There it acts as \(-i[H_-,\cdot]\), a skew-Hermitian superoperator with a semisimple spectrum. Its zero-frequency eigenspace includes the identity \(P_-\) on that block.

**2. Prove universality and uniqueness of the first-order decay.** Set \(\mathcal D(X)=\sum_jP_jXP_j-X\). Directly projecting the site measurements to the antisymmetric block gives, for \(X=P_-XP_-\),
\[
P_-\mathcal D(X)P_-=-X+\frac12\sum_{s=1}^{L}\langle a_s|X|a_s\rangle|a_s\rangle\langle a_s|.
\]
Thus, with the Hilbert--Schmidt inner product,
\[
\operatorname{Re}\langle X,P_-\mathcal D(X)P_-\rangle
=-\|X\|_2^2+\frac12\sum_s|\langle a_s|X|a_s\rangle|^2\leq-\frac12\|X\|_2^2.
\]
Equality holds precisely for matrices diagonal in the \(|a_s\rangle\) basis. If a nonzero diagonal matrix is an eigenoperator of \(-i[H_-,\cdot]\), its eigenfrequency is zero (inspect diagonal commutator entries); connectedness of the path then forces it to be a scalar multiple of \(P_-\). Spectral perturbation of the semisimple noise-free peripheral eigenvalues therefore yields real-part first-order coefficients at most \(-1/2\), with equality only for the one-dimensional eigendirection \(P_-\). More precisely, in each unperturbed frequency sector, the projected dissipator is contractive after shifting by \(1/2\), so that the equality eigenvalue is semisimple. Consequently, the eigenbranch issuing from \(P_-/L\) has first coefficient \(-1/2\), is simple and spectrally dominant for all sufficiently small positive \(\gamma\). Hermiticity preservation makes this isolated branch real.

**3. Reduce the quadratic correction to one finite Lyapunov problem.** Normalize the right peripheral eigenoperator as \(X_0=P_-/L\). Its left eigenfunctional is \(Y=P_-\), with \(\operatorname{Tr}(YX_0)=1\). The dephasing action is exactly
\[
\mathcal D(X_0)=-\frac{P_-}{2L}+\frac{B}{2L}.
\]
The first-order eigenvector equation permits the purely symmetric correction \(X_1=T/(2L)\), where \(T\) is the unique Hermitian solution
\[
A_+T+TA_+^\dagger=-B.
\]
Uniqueness follows from the strict spectral stability of \(A_+\), with \(T=\int_0^\infty e^{A_+t}Be^{A_+^\dagger t}\,dt\). Pairing the second-order eigenvalue equation with \(Y\) gives
\[
\lambda_2=\operatorname{Tr}(P_-\mathcal D(X_1))=\frac{\operatorname{Tr}(BT)}{4L},
\]
because the dephasing of a symmetric-sector operator deposits one-half of each noncentral symmetric position-diagonal entry into the antisymmetric sector.

**4. Solve the Lyapunov equation in closed form for every length.** Index the bright basis by \(0,1,\ldots,L\) and define \(\beta_j=L+1-j\). Its Hermitian solution has \(T_{00}=L/\kappa\), and for \(1\le j\le L\),
\[
T_{0j}=\begin{cases}-i\beta_j/(2\sqrt2g),&j\text{ odd},\\0,&j\text{ even};\end{cases}
\]
whereas for \(1\le i\le j\le L\),
\[
T_{ij}=\begin{cases}
L/\kappa+\kappa i\beta_i/(8g^2),&i=j,\\
\kappa i\beta_j/(8g^2),&i<j\text{ and }j-i\text{ even},\\
-i\beta_j/(2g),&i<j\text{ and }j-i\text{ odd}.
\end{cases}
\]
All remaining entries are fixed by \(T_{ji}=\overline{T_{ij}}\). Here is a direct entrywise verification, avoiding reliance on a numerical solver. For indices \(0\le i\le j\le L\), the \((i,j)\) entry of \(A_+T+TA_+^\dagger\) is
\[
-i\bigl(t_{i-1}T_{i-1,j}+t_iT_{i+1,j}-t_{j-1}T_{i,j-1}-t_jT_{i,j+1}\bigr)-\frac\kappa2(\mathbf1_{i=0}+\mathbf1_{j=0})T_{ij},
\]
with all nonexistent edge terms defined as zero. For \(i=j\ge1\), the adjacent imaginary entries give \(\beta_{i+1}-\beta_i=-1\), also at the final endpoint with \(\beta_{L+1}=0\). At \((0,0)\), the hopping contribution is \(L\) and the sink contributes \(-L\). For gaps of at least two, equal-parity entries cancel using \(\beta_{j-1}+\beta_{j+1}=2\beta_j\), and opposite-parity entries cancel using \((i-1)+(i+1)=2i\); the missing boundary terms follow from the zero conventions. For adjacent gaps the common \(L/\kappa\) parts of the two diagonals cancel. For \(i=0\), the specially weighted edge \(t_0=\sqrt2g\) and the term \(-\kappa T_{0j}/2\) cancel exactly. Therefore the displayed matrix obeys \(A_+T+TA_+^\dagger=-B\) at every entry, as required.

Its diagonal gives
\[
\operatorname{Tr}(BT)=\sum_{s=1}^{L}\left(\frac L\kappa+\frac{\kappa s(L+1-s)}{8g^2}\right)
=\frac{L^2}{\kappa}+\frac{\kappa L(L+1)(L+2)}{48g^2},
\]
using \(\sum_{s=1}^{L}s(L+1-s)=L(L+1)(L+2)/6\). Substitution into the preceding second-order expression yields
\[
\lambda(\gamma)=-\frac{\gamma}{2}+
\left(\frac{L}{4\kappa}+\frac{\kappa(L+1)(L+2)}{192g^2}\right)\gamma^2+O_{L,g,\kappa}(\gamma^3).
\]
Since this branch is the unique spectral abscissa for sufficiently small \(\gamma>0\), its negative is \(\Delta_L(\gamma)\).

**5. Prove strict absorption and the operational survival statement.** For any matrix \(X\),
\[
\operatorname{Re}\langle X,\mathcal L_\gamma X\rangle
=-\frac\kappa2(\|P_0X\|_2^2+\|XP_0\|_2^2)
-\gamma\sum_{j\ne k}|X_{jk}|^2.
\]
An eigenmatrix of real-part-zero eigenvalue would therefore be diagonal, vanish at the center, and commute with the connected path Hamiltonian, hence vanish identically. Thus the spectrum is strictly stable for every \(\gamma>0\). At small positive \(\gamma\), the isolated leading spectral projector approaches the rank-one superoperator \(X\mapsto\operatorname{Tr}(P_-X)P_-/L\). It has positive trace output for every initially normalized state supported on the dark sector. Spectral separation implies its survival probability has a positive multiple of \(e^{-\Delta_L(\gamma)t}\) as the leading term.

## Verification

A standalone numerical cross-check is supplied in `verify.py`, with dependencies in `requirements.txt`. Run `python verify.py` after installing NumPy and SciPy. It reconstructs the bright block and proposed \(T\), tests the Lyapunov residual against a numerical Lyapunov solver for eight path half-lengths and four parameter choices, and independently assembles the dense trace-decreasing superoperator for four half-lengths at three weak-dephasing values. The observed output for the supplied code is `VERIFY_OK bright_lyapunov=32 dense_spectra=36 quadratic_coefficients=36 max_matrix_residual=1.29e-12`. These are finite cross-checks, not a proof for unbounded \(L\) or for arbitrary real parameters; the preceding symbolic argument supplies the all-length result.

## Relationship to prior work

The existence of reflection-protected path dark states and the possibility of removing them with dephasing are **known**. Caruso and collaborators had already constructed sink-plus-site-dephasing Lindblad networks and stated the weak-dephasing trapping-time scale as order \(1/\gamma\) for fully connected graphs. Le, Donati, Severini and Caruso discuss path symmetry-point dark states and noise-assisted suppression of dark subspaces; their path discussion and the later network results supply the closest explicit physical setup. Marais and collaborators analytically study decoherence-assisted transfer, primarily in fully connected networks coupled to environmental spins; Jeske, Vogt and Cole study spatially correlated noise in chains. These works establish context and several underlying approaches, not the all-length central-sink weak-dephasing spectral expansion proved here. In particular, general knowledge that dephasing destroys a dark state does not specify which Liouvillian eigenvalue dominates weak-noise absorption or give the exact inverse-capture and coherent-transport quadratic coefficient. Broader general perturbation theory applies as a *method*, but requires the explicit, nontrivial bright-block Lyapunov solution supplied above. No assertion is made that dark states, quantum-jump master equations, or standard Liouvillian perturbation theory originated with this result.

## Limitations

The exact error term is at fixed \(L,g,\kappa\); it is not uniform in large-system or singular-coupling limits. The coefficient depends on the convention that a site off-diagonal density-matrix element dephases at rate \(\gamma\), and that the center has population absorption rate \(\kappa\). The claimed rate is an **asymptotic survival exponent**, not the mean absorption time or an optimal finite-time transfer probability. The theorem does not cover a displaced sink, uneven hoppings, correlated dephasing, multiple particles, or other graph families. Published-work priority is not independently audited, and an unidentified stronger theorem could possibly imply this specialization.

## References

1. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454 (first public January 28, 2009), subsequently The Journal of Chemical Physics **131**, 105106. Lawful full text: `https://arxiv.org/pdf/0901.4454`.
2. A. Marais, I. Sinayskiy, A. Kay, F. Petruccione, and A. Ekert, *Decoherence-assisted transport in quantum networks*, New Journal of Physics **15**, 013038 (public online January 17, 2013), DOI: `10.1088/1367-2630/15/1/013038`. Lawful full text: `https://arxiv.org/pdf/1401.6660` (arXiv uploaded subsequently).
3. J. Jeske, N. Vogt, and J. H. Cole, *Excitation- and state-transfer through spin chains in the presence of spatially correlated noise*, arXiv:1308.3042 (2013); full text: `https://ar5iv.labs.arxiv.org/html/1308.3042`.
4. T. P. Le, L. Donati, S. Severini, and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017); full text: `https://arxiv.org/pdf/1707.07482`.
