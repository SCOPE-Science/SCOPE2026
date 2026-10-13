# Exact collision-dark space for two quantum walkers on any weighted open path

## Finding
For every finite weighted open path with nonzero nearest-neighbor hopping, full on-site coincidence loss removes the entire exchange-symmetric two-particle sector and no part of the exchange-antisymmetric sector. This holds for arbitrarily nonuniform on-site potentials, complex hopping phases, arbitrary real exchange-symmetric diagonal pair interactions, and arbitrary strictly positive collision-loss rates.

The complete loss-free two-particle subspace is therefore \(\wedge^2\mathbb C^n\) of dimension \(n(n-1)/2\). The complement of the span of all collision-detection Krylov vectors vanishes in the symmetric sector. For every initial density operator, the surviving two-particle mass converges exponentially to its initial antisymmetric weight, regardless of the rates or the diagonal interactions.

## Assumptions and scope
Let \(n\ge2\). Label an open path by \(1,\ldots,n\). Let \(J=J^\dagger\) be tridiagonal with \(J_{j,j+1}\ne0\) for all \(1\le j<n\); all \(J_{jj}\) are real and otherwise arbitrary. In particular, complex hopping is permitted. Choose arbitrary real numbers \(V_{ij}=V_{ji}\) and strictly positive \(\gamma_j\). The ordered-particle Hilbert space is \(\mathcal H=\mathbb C^n\otimes\mathbb C^n\), with standard basis \(|i,j\rangle\). Define
\[
H=J\otimes I+I\otimes J+\sum_{i,j=1}^nV_{ij}|i,j\rangle\langle i,j|,
\quad D=\sum_{j=1}^n\gamma_j|j,j\rangle\langle j,j|,
\quad K=H-\frac i2D.
\]
The exchange involution is \(F|i,j\rangle=|j,i\rangle\), with \(P_{\pm}=(I\pm F)/2\). The conditional no-collision evolution is \(E_t=e^{-itK}\). The survival probability for normalized \(\rho\ge0\), \(\operatorname{Tr}\rho=1\), is \(\operatorname{Tr}(E_t\rho E_t^\dagger)\).

**Theorem.** The largest \(H\)-invariant subspace of \(\ker D\) is \(P_-\mathcal H\). Consequently \(\dim P_-\mathcal H=n(n-1)/2\), the smallest \(H\)-invariant subspace containing all \(|j,j\rangle\) is exactly \(P_+\mathcal H\), and for every fixed choice of the above parameters there exist \(c>0\) and \(C_0>0\) such that
\[
\|E_t-e^{-itH}P_-\|\le C_0e^{-ct}\qquad(t\ge0).
\]
For any density matrix \(\rho\), a possibly different \(C_{\rho}>0\) gives
\[
\|E_t\rho E_t^\dagger-e^{-itH}P_-\rho P_-e^{itH}\|_1\le C_{\rho}e^{-ct}.
\]
Hence
\[
\lim_{t\to\infty}\operatorname{Tr}(E_t\rho E_t^\dagger)=\operatorname{Tr}(P_-\rho),
\quad
\lim_{t\to\infty}\|E_t|u,v\rangle\|^2=\frac{1-|\langle u,v\rangle|^2}{2}
\]
for normalized single-particle vectors \(u,v\). In particular, initial distinct-site localized configurations have survival \(1/2\), while same-site configurations have survival zero. All exchange-symmetric preparations are eventually fully lost; antisymmetric preparations never suffer these losses.

## Proof
**1. Exchange-sector decomposition.** Since \(V_{ij}=V_{ji}\), both \(H\) and \(D\) commute with \(F\). Moreover \(DP_-=0\). Therefore \(K\) reduces to the orthogonal direct sum of the Hermitian restriction \(H_-\) and the dissipative restriction \(K_+=H_+-iD_+/2\).

**2. Strict diagonal unique continuation in the symmetric sector.** Suppose \(Hf=\lambda f\), \(f_{ij}=f_{ji}\), and \(f_{jj}=0\) for all \(j\). Adopt the convention that all coefficients outside \(\{1,\ldots,n\}\) vanish. At \((j,j)\) the eigen-equation, using \(f_{jj}=0\), reads
\[
0=2J_{j,j-1}f_{j-1,j}+2J_{j,j+1}f_{j,j+1}.
\]
At \(j=1\) this gives \(f_{1,2}=0\); then, proceeding through \(j=2,\ldots,n-1\), it implies \(f_{j,j+1}=0\) for every adjacent pair because all corresponding couplings are nonzero.

Induct on the separation \(r=j-i\ge2\). Assume \(f_{ij}=0\) at every separation below \(r\). Apply \((H-\lambda)f=0\) to \((i,i+r-1)\). The potential term and the longitudinal on-site terms vanish, as do the two inward-hopping contributions. Thus the only possibly nonzero terms are
\[
0=J_{i,i-1}f_{i-1,i+r-1}+J_{i+r-1,i+r}f_{i,i+r}.
\]
At \(i=1\), the first term is absent, so \(f_{1,1+r}=0\). Successive \(i=2,3,\ldots,n-r\) then force \(f_{i,i+r}=0\), using the previously vanishing left term and nonzero right hopping. This holds through \(r=n-1\), giving \(f=0\). The argument uses neither distinct eigenvalues nor translational symmetry and works with arbitrary complex adjacent couplings and any exchange-symmetric diagonal pair potential.

**3. Exact dark space.** Every vector in \(P_-\mathcal H\) has zero diagonal and is carried by \(H\) into that same subspace. Conversely, any nonzero \(H\)-invariant subspace in \(P_+\mathcal H\cap\ker D\) contains a Hermitian eigenvector of \(H_+\); Step 2 excludes one. More generally, any \(H\)-invariant subspace inside \(\ker D\) has a basis of \(H\)-eigenvectors. For each such eigenvector \(f\), its symmetric part \(P_+f\) is itself an eigenvector of \(H\) and is still in \(\ker D\), since \(H,D\) commute with exchange. Step 2 forces \(P_+f=0\). Hence every invariant collision-dark subspace is contained in \(P_-\mathcal H\), proving maximality. By Hermitian duality, the \(H\)-cyclic span of \(\{|j,j\rangle:1\le j\le n\}\) has orthogonal complement equal to this dark space; hence it is exactly \(P_+\mathcal H\) and has dimension \(n(n+1)/2\).

**4. Exponential asymptotics.** For any eigenpair \(K_+x=zx\), the dissipativity identity is
\[
\operatorname{Im}z\,\|x\|^2=-\tfrac12\langle x,Dx\rangle\le0.
\]
If equality held, then \(Dx=0\) (since \(D\) is positive semidefinite), and \(H_+x=zx\). Step 2 would force \(x=0\), a contradiction. All finitely many eigenvalues of \(K_+\) therefore lie strictly below the real axis. Jordan normal form implies \(\|e^{-itK_+}\|\le C_0e^{-ct}\) for suitable positive constants. The antisymmetric part is exactly \(e^{-itH}P_-\); norm bounds on the two cross terms and the symmetric square term prove the trace-norm estimate. Taking traces yields the survival law. Finally \(\langle u,v|F|u,v\rangle=|\langle u,v\rangle|^2\), proving the product-input formula.

**5. Why the open-path condition matters.** On the unweighted four-cycle with the standard adjacency matrix, the normalized symmetric vector
\[
\tfrac12\bigl(|0,2\rangle+|2,0\rangle-|1,3\rangle-|3,1\rangle\bigr)
\]
has zero amplitude on every coincidence site and is a zero-energy eigenvector of \(J\otimes I+I\otimes J\). It is a further dark mode, so the claimed classification does not extend to arbitrary graphs.

## Verification
The standalone checker `verification/verify.py` tests 48 seeded instances with dimensions \(2\le n\le7\), independent random nonzero complex hopping amplitudes, disordered diagonal energies, arbitrary real exchange-symmetric diagonal pair interactions, and nonuniform positive collision rates. It checks Hermitian spectral dark dimensions, swap commutation, and the large-time no-jump survival of 144 randomized initial states. It separately checks the exact four-cycle boundary eigenvector. The principal result is proved by the all-dimensional recurrence and dissipativity argument above; finite tests alone would not certify it.

To reproduce: install NumPy and SciPy as specified in `verification/requirements.txt`, then execute `python verification/verify.py` from the extracted package root. Exact test output is preserved in `verification/output.txt`.

## Relationship to prior work
Foss-Feig, Daley, Thompson, and Rey [1] prove the physical antisymmetry mechanism in a two-site well and in a one-dimensional harmonic trap. Their appendix describes extending its argument to a one-dimensional Hubbard chain as straightforward but does not give the present arbitrary weighted-path theorem with arbitrary exchange-symmetric diagonal pair interactions, a complete detection-span classification, and an all-density-matrix asymptotic formula. Thus antisymmetry protection and the two-site 50-percent example are **prior findings**, not claimed as new here.

Qin and coauthors [2] analyze coherent interacting two-particle one-dimensional quantum walks without the present complete coincidence-loss observation theorem. Van Horssen and Garrahan [3] study nearest-neighbor pair loss in a hard-core periodic reaction-diffusion chain, with a different monitored subspace. Marché and colleagues [4] analyze exact two-body on-site loss for uniform periodic/continuum gases and show that a fermionic triplet component does not decay, while deriving size-dependent decay exponents for the lossy symmetric component. They do not establish the weighted-open-path unique-continuation result or the full arbitrary-interaction/rate classification. The contribution here is the rigorous finite, disordered, interacting, fully monitored open-path universality, **not** discovery of exchange-protected dark states.

## Limitations
This is a finite-dimensional, exact long-time result; the constants \(c,C_0,C_{\rho}\) depend on the fixed parameters and need not be uniform as hopping or loss rates approach zero or system size grows. The theorem does not determine optimal finite-time loss rates, many-particle loss laws, behavior under exchange-breaking interactions, partial monitoring, long-range hopping, periodic boundaries, or non-Hermitian dynamics with gain. If even one path link vanishes, the proof no longer applies. The novelty comparison does not exclude unknown equivalent specialized results; publication priority and independent mathematical review remain open.

## References
[1] M. Foss-Feig, A. J. Daley, J. K. Thompson, A. M. Rey, *Steady-state many-body entanglement of hot reactive fermions*, arXiv:1207.4741v1 (first public 2012-07-19), https://arxiv.org/html/1207.4741v1 , especially the two-particle discussion and Appendix A.

[2] *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349v1 (2014), https://arxiv.org/abs/1402.3349 .

[3] M. van Horssen and J. P. Garrahan, *Open quantum reaction-diffusion dynamics: absorbing states and relaxation*, arXiv:1411.7913v1 (2014), https://arxiv.org/abs/1411.7913 .

[4] A. Marché, H. Yoshida, A. Nardin, H. Katsura, L. Mazza, *Universality and two-body losses: lessons from the effective non-Hermitian dynamics of two particles*, arXiv:2405.04789v1 (first public 2024-05-08), https://arxiv.org/html/2405.04789v2 , Sections II–III and Appendix A.

