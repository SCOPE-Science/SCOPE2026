# Exact Lindbladian spectrum and noise-optimal relaxation on quantum star networks

## Finding
For every integer \(n\ge3\), a single quantum excitation on the star \(K_{1,n}\) with nonzero real adjacency hopping \(g\) and strictly positive uniform site-projector dephasing \(\gamma\) has a completely explicit Liouvillian characteristic polynomial. Define
\[
S_n(z)=z\bigl((z+\gamma)^2+ng^2\bigr)+2\gamma g^2,
\qquad
T_n(z)=z\bigl((z+\gamma)^2+4ng^2\bigr)+2(n+1)\gamma g^2.
\]
Then
\[
\boxed{\det(zI-\mathcal L)=z(z+\gamma)^{n^2-3n+2}\,T_n(z)\bigl[((z+\gamma)^2+ng^2)S_n(z)\bigr]^{n-1}.}
\]
The unique stationary state is the maximally mixed state. The exact relaxation gap \(\Delta_n(g,\gamma)\) is the unique \(s\in(0,2\gamma/n)\) satisfying
\[
s\bigl((\gamma-s)^2+ng^2\bigr)=2\gamma g^2.
\]
Its unique global dephasing optimum is
\[
\boxed{\gamma_*={|g|(n-1)\over\sqrt{n-2}},\qquad\max_{\gamma>0}\Delta_n={|g|\over\sqrt{n-2}}.}
\]
For a particle initially localized at leaf \(1\), the observable difference \(q(t)=\rho_{11}(t)-\rho_{22}(t)\), where leaf \(2\) is any distinct leaf, has exactly
\[
\int_0^\infty e^{-zt}q(t)\,dt={ (z+\gamma)^2+(n-2)g^2\over S_n(z)},\qquad \operatorname{Re}z>0.
\]
Writing \(s=\Delta_n\), this contrast satisfies \(q(t)\sim R e^{-st}\), where
\[
R={ (\gamma-s)^2+(n-2)g^2\over S'_n(-s)}>0.
\]
Therefore this spectral gap is observed in a concrete localized population contrast rather than solely in operator-space modes. At the noise optimum, \(\gamma_*\sim |g|\sqrt n\) while \(\Delta_{\max}\sim |g|/\sqrt n\) as the leaf count grows.

## Assumptions and scope
The Hilbert space is \(\mathbb C^{n+1}\), whose orthonormal basis comprises a hub \(|0\rangle\) and leaves \(|j\rangle\), \(1\le j\le n\). The adjacency Hamiltonian is
\[
H=g\sum_{j=1}^n\bigl(|0\rangle\langle j|+|j\rangle\langle0|\bigr),\qquad g\in\mathbb R\setminus\{0\}.
\]
The Markovian pure-dephasing equation uses \(P_j=|j\rangle\langle j|\) with the same parameter \(\gamma>0\) at every vertex:
\[
\mathcal L(X)=-i[H,X]+\gamma\sum_{j=0}^n\left(P_jXP_j-\tfrac12\{P_j,X\}\right)
=-i[H,X]-\gamma(X-\operatorname{diag}X).
\]
Here \(\operatorname{diag}X\) removes off-diagonal entries in the site basis. Time units set \(\hbar=1\). The result concerns the full complex matrix-operator space; the gap is the negative of the greatest real part among its nonzero generator eigenvalues. This is an **adjacency**, not graph-Laplacian, Hamiltonian: on nonregular star graphs that distinction affects the dynamics.

## Proof
**Block equations.** With \(\mathbf1\in\mathbb C^n\) the all-ones leaf vector, write
\[
X=\begin{pmatrix}x&v^\mathsf T\\w&M\end{pmatrix}.
\]
Direct multiplication gives
\[
\begin{aligned}
\dot x&=-ig(\mathbf1^\mathsf T w-v^\mathsf T\mathbf1),\\
\dot v^\mathsf T&=-ig(\mathbf1^\mathsf T M-x\mathbf1^\mathsf T)-\gamma v^\mathsf T,\\
\dot w&=-ig(x\mathbf1-M\mathbf1)-\gamma w,\\
\dot M&=-ig(\mathbf1 v^\mathsf T-w\mathbf1^\mathsf T)-\gamma(M-\operatorname{diag}M).
\end{aligned}
\]
No Hermiticity assumption was used, so these equations describe the entire Liouvillian.

**Exhaustive invariant splitting.** In the five-dimensional permutation-trivial sector put \(v=a\mathbf1\), \(w=b\mathbf1\), \(M=cI+d(J-I)\), with free hub coordinate \(x\), and \(J=\mathbf1\mathbf1^\mathsf T\). In the basis \((x,a,b,c,d)\), the generator is
\[
\mathsf T=\begin{pmatrix}
0&ign&-ign&0&0\\
ig&-\gamma&0&-ig&-ig(n-1)\\
-ig&0&-\gamma&ig&ig(n-1)\\
0&-ig&ig&0&0\\
0&-ig&ig&0&-\gamma
\end{pmatrix}.
\]
Its characteristic polynomial is \(z(z+\gamma)T_n(z)\).

For each of the \(n-1\) independent vectors \(f\in\mathbb C^n\) satisfying \(\mathbf1^\mathsf Tf=0\), set \(v=af\), \(w=bf\), and
\[
M=c\operatorname{diag}f+d(f\mathbf1^\mathsf T-\operatorname{diag}f)+e(\mathbf1 f^\mathsf T-\operatorname{diag}f).
\]
This defines an invariant five-dimensional sector whose basis \((a,b,c,d,e)\) has generator
\[
\mathsf U=\begin{pmatrix}
-\gamma&0&-ig&ig&-ig(n-1)\\
0&-\gamma&ig&ig(n-1)&-ig\\
-ig&ig&0&0&0\\
0&ig&0&-\gamma&0\\
-ig&0&0&0&-\gamma
\end{pmatrix}.
\]
Its characteristic polynomial is \(\bigl((z+\gamma)^2+ng^2\bigr)S_n(z)\).

The remaining subspace consists of leaf-only matrices with zero diagonal and zero row and column sums. It has dimension \(n^2-3n+1\) for \(n\ge3\); \(\mathcal L\) acts there as multiplication by \(-\gamma\). The trivial, standard and remainder spaces have dimensions \(5\), \(5(n-1)\) and \(n^2-3n+1\), summing to \((n+1)^2\). Their characteristic polynomials give the stated complete factorization, including algebraic multiplicities and every possible coincident-root case.

**Steady state.** For any matrix \(X\),
\[
\operatorname{Re}\langle X,\mathcal L X\rangle_{\rm HS}=-\gamma\sum_{j\ne k}|X_{jk}|^2\le0.
\]
A generator eigenvector on the imaginary axis must therefore be diagonal. The Hamiltonian commutator of such a matrix vanishes only if all its diagonal entries agree across each hub–leaf edge. Connectedness forces a scalar matrix. The explicit factorization confirms that the zero eigenvalue is algebraically simple. Therefore the unique normalized stationary density matrix is \(I/(n+1)\), with strict decay in all other sectors.

**Sharp gap.** The cubic \(S_n(-s)=0\) is equivalent to
\[
s\bigl((\gamma-s)^2+ng^2\bigr)=2\gamma g^2.
\]
It has exactly one \(s\in(0,2\gamma/n)\): let \(u=(\gamma-s)/(|g|\sqrt n)>0\), \(y=s\sqrt n/|g|\), and \(A=1-2/n>0\). Then
\[
y={2u\over u^2+A},\qquad
\gamma=|g|\sqrt n\,u+{|g|\over\sqrt n}y.
\]
The second relation is strictly increasing from zero to infinity because \(y'(u)\ge-1/(4A)\), giving \(d\gamma/du\ge|g|\sqrt n(1-1/[4(n-2)])>0\) for all \(n\ge3\). It follows that the root exists uniquely, \(s<2\gamma/n\le2\gamma/3\), and \(s<\gamma\).

The other two roots of \(S_n\) lie strictly to the left of \(-s\). Indeed \(S_n(w-s)=w(w^2+aw+b)\), with \(a=2\gamma-3s>0\) and
\[
b=(\gamma-s)(\gamma-3s)+ng^2
={2(\gamma-s)(\gamma^2-3\gamma s+ns^2)\over2\gamma-ns}>0.
\]
The quadratic polynomial has roots with negative real parts. Similarly \(T_n(w-s)=w^3+aw^2+b_Tw+c_T\), with
\[
b_T=(\gamma-s)(\gamma-3s)+4ng^2,\qquad c_T=ng^2(2\gamma-3s).
\]
Both are positive, and
\[
b_T-ng^2={2\gamma(\gamma-s)(\gamma+(n-3)s)\over2\gamma-ns}>0.
\]
Thus \(ab_T>c_T\), and the cubic Routh–Hurwitz criterion makes every shifted \(T_n\)-root strictly stable. The remaining nonzero eigenvalues are at \(-\gamma\) or \(-\gamma\pm i|g|\sqrt n\), also strictly to the left of \(-s\). Therefore \(\Delta_n=s\) exactly. The value \(s\) is an eigenvalue in every standard sector, with algebraic multiplicity at least \(n-1\).

**Unique noise optimum.** Since \(\gamma\) increases strictly with \(u\), maximizing \(s\) over \(\gamma>0\) is equivalent to maximizing \(y(u)=2u/(u^2+A)\) over \(u>0\). This rational function has its unique maximum at \(u=\sqrt A\), with \(y_{\max}=1/\sqrt A\). Substitution gives exactly \(\Delta_{\max}=|g|/\sqrt{n-2}\) and \(\gamma_*=|g|(n-1)/\sqrt{n-2}\). The displayed large-\(n\) asymptotics follow immediately.

**Population witness.** Suppose \(\rho(0)=|1\rangle\langle1|\). Subtracting the population at any distinct leaf \(2\) isolates the standard representation, and its initial standard coordinates are \((a,b,c,d,e)=(0,0,1,0,0)\). Define \(p=a-b\) and \(h=d+e\). From \(\mathsf U\),
\[
\dot p=-\gamma p-ig\bigl(2c+(n-2)h\bigr),\qquad
\dot c=-igp,\qquad
\dot h=-igp-\gamma h,
\]
with initial values \(p(0)=h(0)=0\), \(c(0)=1\). Eliminating \(p,h\) after Laplace transformation gives \(\widetilde c(z)=\bigl((z+\gamma)^2+(n-2)g^2\bigr)/S_n(z)\), and \(q(t)=c(t)\). Since \(-s\) is the unique dominant \(S_n\)-root, is simple, and has strictly positive numerator and derivative \(S_n'(-s)=b>0\), its residue \(R>0\). Every other pole has smaller real part. Partial fractions thus yield \(q(t)\sim R e^{-st}\), proving that the operator gap is the actual long-time exponential decay exponent of this localized population difference.

## Verification
The standalone program `verify.py`, executable using the packages in `requirements.txt`, builds the complete \((n+1)^2\)-dimensional Lindblad superoperator independently of the invariant-subspace proof. It compares all complex eigenvalues and multiplicities against the polynomial factorization, checks the predicted gap, tests the unique optimum away from its maximizer, and checks the localized-leaf Laplace contrast against a direct superoperator resolvent. It uses numerical eigensolvers and optimization only for finite examples; the proof above establishes the theorem for all integers \(n\ge3\) and all admissible continuous parameters.

## Relationship to prior work
Exact *coherent* star-walk transition probabilities were derived by Xu (2009) using a Laplacian Hamiltonian; Salimi (2009) investigated adjacency-based quantum walks on star-product graphs. Anishchenko, Blumen and Mülken (2011) compared coherent spreading on star and complete graphs. None of these papers has the present site-projector dephasing Liouvillian. Bressanini, Benedetti and Paris (2022) examined Haken–Strobl dephasing and its numerical noise-dependent slowdown on several graphs, including stars, but used a graph-Laplacian Hamiltonian and a quantum–classical fidelity observable, not this adjacency-star full spectral polynomial or its optimal operator gap. A subsequent study of network quantum-walk stability, arXiv:2507.17880, treated Haken–Strobl noise and star-network relaxation numerically and proved uniqueness of a steady state, but did not state the exact characteristic polynomial or the sharp optimal rate derived here.

The slow cubic \(S_n\), viewed alone, also appears after parameter rescaling in the previously studied complete-graph Lindblad problem. Consequently, the standalone numerical optimum is **not** asserted to be an independent novelty beyond such a cubic reduction. The nontrivial claim here is the exhaustive **star-specific** operator-space spectrum, proof of the dominance of the leaf-difference sector over the additional star modes, and an exact observable contrast. The previously known coherent star results and generic dephasing principles are not presented as new. No claim of exhaustive publication-priority certification is made.

## Limitations
The theorem assumes a finite unweighted star, homogeneous real adjacency hopping, and identical strictly positive local dephasing at every vertex. It does not address Laplacian Hamiltonians on nonregular stars, heterogeneous or correlated noise, trapping, static disorder, interactions, finite-time mixing threshold optimization, or exact convergence constants for arbitrary initial density matrices. An unknown stronger general Lindblad symmetry theorem may imply this particular closed form; independent priority review has not been performed.

## References
1. X.-P. Xu, *Exact analytical results for quantum walks on star graph*, arXiv:0903.1149 (first posted 6 March 2009), https://arxiv.org/abs/0903.1149.
2. S. Salimi, *Continuous-time quantum walks on star graphs*, arXiv:0904.2054 (first posted 14 April 2009), https://arxiv.org/abs/0904.2054.
3. A. Anishchenko, A. Blumen, O. Mülken, *Enhancing the spreading of quantum walks on star graphs by additional bonds*, arXiv:1111.7065 (first posted 30 November 2011), https://arxiv.org/abs/1111.7065.
4. G. Bressanini, C. Benedetti, M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, *Quantum Information Processing* (2022), https://doi.org/10.1007/s11128-022-03647-x.
5. *Stability of Continuous Time Quantum Walks in Complex Networks*, arXiv:2507.17880, https://arxiv.org/abs/2507.17880.
