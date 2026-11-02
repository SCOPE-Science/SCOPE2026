# Parity-sharp coherent absorption by Hamming spheres on quantum hypercubes

## Finding

Let \(n\ge1\) be an integer, let \(Q_n\) be the graph on \(\mathbb F_2^n\) whose edges change exactly one coordinate, and let \(J>0\). Select every vertex of the fixed-weight sphere \(L_r=\{x\in\mathbb F_2^n:|x|=r\}\), for an integer \(0\le r\le n\), as a trap. Consider the finite-dimensional no-jump Hamiltonian
\[
H=J A(Q_n)-i\Gamma,\qquad
\Gamma=\sum_{x\in L_r}\gamma_x|x\rangle\langle x|,
\qquad\gamma_x>0.
\]
The maximal nondecaying subspace is the orthogonal sum of the \(Q_n\)-adjacency eigenspaces whose wavefunctions vanish at every trap. Its exact dimension, for every \(n,r\), follows from the following **energy-resolved rank formula**. Define
\[
\begin{aligned}
\mu_i&=\binom ni-\binom n{i-1},\qquad \binom n{-1}=0,\\
K_{N,d}(a)&=[z^d](1-z)^a(1+z)^{N-a},\\
t(n,r,w)&=\min\{r,n-r,w,n-w\}.
\end{aligned}
\]
For the eigenvalue \(J(n-2w)\), with \(0\le w\le n\), the dimension of the trap-visible, or *bright*, subspace is exactly
\[
\boxed{b_{n,r}(w)=\sum_{i=0}^{t(n,r,w)}\mu_i\,\mathbf1_{\{K_{n-2i,w-i}(r-i)\ne0\}}.}
\]
Thus the total bright and dark dimensions, and the eventual absorption probability for the maximally mixed one-particle initial state, are respectively
\[
\boxed{B(n,r)=\sum_{w=0}^n b_{n,r}(w),\quad
D(n,r)=2^n-B(n,r),\quad
P_{\mathrm{capture}}=2^{-n}B(n,r).}
\]
All dimensions and limits are independent of the choices of strictly positive \(\gamma_x\).

The all-radius formula yields a sharp **odd–even full-absorption law**, with no restriction on the initial pure or mixed state:

* If \(n=2m+1\), then precisely the two central spheres \(L_m\) and \(L_{m+1}\) among single Hamming spheres are fully absorbing. Each has \(D(n,m)=D(n,m+1)=0\). Consequently, every initial state is eventually absorbed even though the trap density is of order \(n^{-1/2}\).
* If \(n=2m\), no single Hamming sphere is fully absorbing. For the central sphere \(L_m\), every Walsh energy sector has the explicit bright dimension
\[
\boxed{b_{2m,m}(w)=\binom{2m-1}{\min(w,2m-w)},\quad
D(2m,m)=2^{2m-1}-\tfrac12\binom{2m}m.}
\]
  The adjacent sphere \(L_{m-1}\) alone has
\[
\boxed{D(2m,m-1)=\tfrac12\binom{2m}m.}
\]
  But trapping on **both** \(L_{m-1}\cup L_m\) gives \(D=0\). Hence the exact minimum number of complete Hamming-weight layers needed for full absorption is one for odd dimension and two for even dimension.

For example, in \(Q_7\) the single 35-site central sphere captures every initial excitation among 128 sites. In \(Q_8\), the central 70-site sphere leaves 93 dark dimensions, the adjacent 56-site sphere leaves 35, but their union has no dark space. These statements concern eventual capture, not finite-time capture rates.

## Assumptions and scope

The walk has a single coherent particle and uniform, nonzero, real nearest-neighbor hopping on the unweighted binary hypercube. Every vertex of each specified Hamming sphere carries some strictly positive loss; these strengths need not be equal. All dark dimensions refer to the no-jump norm \(\lim_{t\to\infty}\|e^{-itH}\psi\|^2\), or its density-matrix extension, and are not counts of stationary eigenvectors of a trace-preserving Lindbladian. In the two-sphere assertion the loss support is the union of the two complete layers; arbitrary partial layers are not covered. The term *minimum number of layers* means among supports which are unions of complete fixed-Hamming-weight spheres centered at the same vertex, not among all possible absorber sets.

## Proof

**1. Reduction to frequency-shell restriction.** For each \(T\subseteq[n]\), let \(\chi_T(S)=(-1)^{|S\cap T|}\). The Walsh characters form an orthogonal basis and
\[
A(Q_n)\chi_T=(n-2|T|)\chi_T.
\]
Therefore the eigenspace of energy \(J(n-2w)\) is the span of characters with \(|T|=w\), of dimension \(\binom nw\). Evaluating a vector of coefficients on the trap sphere \(|S|=r\) is precisely the rectangular signed incidence matrix
\[
M_{r,w}(S,T)=(-1)^{|S\cap T|},\qquad |S|=r,\quad |T|=w.
\]
The dimension of the visible part of energy sector \(w\) equals \(\operatorname{rank}M_{r,w}\), so the dark dimension equals \(\sum_w[\binom nw-\operatorname{rank}M_{r,w}]\).

**2. Harmonic incidence decomposition.** Write \(V_j\) for complex arrays indexed by \(j\)-subsets of \([n]\), and let the inclusion raising operator \(U_j:V_j\to V_{j+1}\) sum coefficients over immediate contained subsets; its adjoint is the down operator \(D_{j+1}\). Direct subset counting gives
\[
D_{j+1}U_j-U_{j-1}D_j=(n-2j)I_{V_j}.
\]
For \(0\le i\le\lfloor n/2\rfloor\), the harmonic coefficient space \(\mathcal H_i=\ker D_i\) has dimension \(\mu_i=\binom ni-\binom n{i-1}\). Indeed, below the midpoint the commutator and adjointness imply that the raising maps are injective and the down maps surjective. For \(i\le j\le n-i\), put
\[
(I_{j,i}h)(T)=\sum_{\substack{I\subseteq T\\|I|=i}}h(I),\qquad |T|=j.
\]
Repeated application of the same commutator proves \(I_{j,i}\) injective on \(\mathcal H_i\), with squared norm \(\binom{n-2i}{j-i}\|h\|^2\); lifts from different \(i\) are orthogonal. The dimension identity \(\sum_{i=0}^{\min(j,n-j)}\mu_i=\binom nj\) therefore gives the complete orthogonal decomposition
\[
V_j=\bigoplus_{i=0}^{\min(j,n-j)} I_{j,i}\mathcal H_i.
\]
These arguments are the standard Boolean-lattice harmonic and symmetric-chain decomposition; they are not claimed as new.

**3. Exact restriction scalar.** Fix \(i\le\min(r,n-r,w,n-w)\) and \(h\in\mathcal H_i\). Interchanging the sums over \(w\)-sets \(T\) and the \(i\)-sets \(I\subseteq T\) gives
\[
\begin{aligned}
(M_{r,w}I_{w,i}h)(S)&=\sum_{|I|=i}h(I)g(|I\cap S|),\\
g(j)&=(-1)^j[z^{w-i}](1-z)^{r-j}(1+z)^{n-r-i+j}.
\end{aligned}
\]
Expand \(g(j)\) in the Newton basis \(\binom ja\), for \(0\le a\le i\). For every \(a<i\),
\[
\sum_{|I|=i}h(I)\binom{|I\cap S|}{a}=0,
\]
because each coefficient is a sum of \(i\)-set coefficients over supersets of an \(a\)-set, and \(D_i h=0\) implies all lower contractions vanish. At \(a=i\), the corresponding sum is \((I_{r,i}h)(S)\). The coefficient of \(\binom ji\) is the \(i\)th finite difference \(\Delta^i g(0)\). The generating function in \(j\) is a geometric power with ratio \(-(1+z)/(1-z)\), yielding exactly
\[
\boxed{M_{r,w}I_{w,i}h=(-2)^i K_{n-2i,w-i}(r-i)\, I_{r,i}h.}
\]
No other harmonic components interact. Since both lifts are injective, each \(i\) contributes precisely \(\mu_i\) to the rank if and only if this coefficient is nonzero. This proves the all-radius energy-resolved rank formula, including the degenerate endpoints.

**4. Odd dimension.** Take \(n=2m+1\), \(r=m\). The critical Krawtchouk generating function on harmonic sector \(i\) becomes
\[
(1-z)^{m-i}(1+z)^{m+1-i}=(1+z)(1-z^2)^{m-i}.
\]
Every coefficient in the range \(0\le w-i\le2(m-i)+1\) is nonzero: even and odd powers use distinct nonzero binomial coefficients. Hence \(M_{m,w}\) is injective for every \(w\) and \(D=0\). Complementing all trap bits gives the same ranks for \(r=m+1\). For any other \(r\), \(\binom nr<\binom nm\), so the dimension-\(\binom nm\) middle energy eigenspace cannot inject into the smaller space of trap amplitudes. This proves uniqueness of the two fully absorbing single spheres.

**5. Even dimension and complementary parity.** Let \(n=2m\). At \(r=m\), the harmonic-sector polynomial is \((1-z^2)^{m-i}\); its coefficient is nonzero exactly when \(w-i\) is even. Summing the alternating-index harmonic dimensions gives
\[
 b_{2m,m}(w)=\sum_{\substack{0\le i\le t\\i\equiv w\ (\mathrm{mod}\ 2)}}\left(\binom{2m}i-\binom{2m}{i-1}\right)
 =\binom{2m-1}{t},\quad t=\min(w,2m-w).
\]
Summing over all \(w\) yields \(B(2m,m)=2^{2m-1}+\tfrac12\binom{2m}m\), giving the asserted central dark dimension.

At \(r=m-1\), a harmonic sector \(i\le m-1\) instead has polynomial
\[
(1-z)^{m-1-i}(1+z)^{m+1-i}
=(1+z)^2(1-z^2)^{m-1-i}.
\]
All its coefficients are nonzero within the allowed range **except** for the central coefficient \(w-i=m-i\), which vanishes exactly when \(m-i\) is even. To see this directly, the odd-degree coefficients are twice a signed binomial coefficient. For even degree \(2j\), the coefficient is \((-1)^j[\binom{m-1-i}{j}-\binom{m-1-i}{j-1}]\), vanishing exactly when \(2j=m-i\). Thus \(M_{m-1,w}\) is injective for all \(w\ne m\). In the middle energy sector, it sees precisely the harmonic sectors of parity opposite to those seen by \(M_{m,m}\); its rank is \(\binom{2m-1}{m-1}=\tfrac12\binom{2m}m\). Consequently its dark dimension is \(\tfrac12\binom{2m}m\), and stacking the restriction matrices for the two adjacent spheres is injective in every energy sector.

No single sphere is fully absorbing in even dimension: all noncentral spheres have fewer than \(\binom{2m}m\) rows and cannot inject the middle energy eigenspace, whereas the central sphere has the positive dark dimension displayed above. This proves the optimal layer-count assertion.

**6. From spectral ranks to loss dynamics.** The anti-Hermitian part of \(H\) is \(-i\Gamma\le0\), so \(e^{-itH}\) is contractive. Any real-eigenvalue eigenvector \(v\) of \(H\) obeys \(\langle v,\Gamma v\rangle=0\), hence \(\Gamma v=0\) and \(JA v=\lambda v\). Conversely all such Walsh eigenvectors are nondecaying. Contractivity rules out nontrivial Jordan blocks on the real axis, while the other finite-dimensional spectral modes decay. The real-axis eigenspace is reducing under both \(JA\) and \(\Gamma\), hence the long-time survival of any initial density matrix \(\rho\) is its trace weight on the orthogonal dark projector \(P_{\rm dark}\):
\[
\lim_{t\to\infty}\operatorname{tr}(e^{-itH}\rho e^{itH^\dagger})
=\operatorname{tr}(P_{\rm dark}\rho).
\]
For \(\rho=I/2^n\), eventual capture is exactly \(1-D/2^n\). All results are independent of the numerical positive trap rates.

## Verification

The accompanying standalone standard-library checker `artifacts/verify.py` constructs the rectangular signed subset-intersection matrices independently of the harmonic formula and computes exact modular ranks for all radii and energy shells in dimensions \(1\le n\le8\): **284 complete shell-rank comparisons**. It separately constructs site-basis adjacency observability matrices \([P_T;P_TA;\ldots;P_TA^n]\) for all single-shell supports through dimension six and for two-shell supports in even dimensions, giving **30 physical observability-rank comparisons**. It tests 8 parity formulas and 24 energy-sector two-shell injectivity assertions. Execution from the supplied file gives

`VERIFY_OK krylov=30 parity=8 spectral=284 two_shell=24`

Run `python3 artifacts/verify.py`. Characteristic-zero statements rely on the analytic proof above, not modular finite tests; the modular rank calculations provide exact finite corroboration only.

## Relationship to prior work

Moore and Russell [1] diagonalize continuous-time hypercube walks using Fourier modes, but do not classify loss at an entire Hamming sphere. Varbanov, Krovi and Brun [2] study absorption and dark states for hitting a target, without the every-initial-state shell-rank and parity classification here. The Boolean-lattice harmonic/incidence machinery is established by Srinivasan [3] and Filmus [4]; the present proof uses and credits it rather than claiming the decomposition itself. A published all-degree Fourier-sampling theorem for **nonbinary** Hamming spheres [5] and a binary degree-at-most-two Walsh-band shell spectrum [6] are close mathematical comparisons; neither inspected result states the all-energy exact-degree signed restriction ranks or their physical full-absorption consequence. Prior calculations of loss starting specifically at the hypercube origin concern one initial state, and results for Hamming **balls** concern a different trap support; neither implies a complete single-sphere dark projector. A 2026 spin-coupled coined Grover-walk preprint [7] also concerns central-layer parity, but operates on a different quantum walk and was accessible only at the abstract level.

## Limitations

The classification applies to classical graph-adjacency **single-particle coherent quantum dynamics**, not arbitrary quantum walks, disordered edges, missing trap sites or general Lindblad dynamics with dephasing and pumping. The location and number of complete Hamming layers, not the total number of individual trap vertices needed among unrestricted sets, are optimized. The theorem does not give finite-time relaxation rates; arbitrary positive loss strengths can change those rates. General Boolean-lattice harmonic methods are longstanding, so an equivalent implicit specialization in historical Terwilliger or association-scheme literature remains a meaningful priority risk.

## References

[1] C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137, first public 2001-04-29, https://arxiv.org/abs/quant-ph/0104137.

[2] M. Varbanov, H. Krovi and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446, first public 2008-03-24, https://arxiv.org/abs/0803.3446.

[3] M. K. Srinivasan, *Symmetric chains, Gelfand–Tsetlin chains, and the Terwilliger algebra of the binary Hamming scheme*, arXiv:1001.0280, first public 2010-01-02, https://arxiv.org/abs/1001.0280.

[4] Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, first public 2014-06-01, https://arxiv.org/abs/1406.0142.

[5] *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.

[6] *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95.

[7] C. Wang, *Harmonic Reduction of Spin-Coupled Grover Walks on Hypercubes via Quantum Bernoulli Noises*, arXiv:2610.14467, first public 2026-10-10, https://arxiv.org/abs/2610.14467.
