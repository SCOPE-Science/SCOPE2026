# A five-valued sitewise quantum-capture law on prime-sided square grids

## Finding

Let \(p\ge3\) be an odd prime, \(n=p-1\), and \(G=P_n\square P_n\), with vertices \((x,y)\) indexed by \(1\le x,y\le n\). A single excitation evolves under the uniform adjacency-hopping Hamiltonian with positive hopping \(J\) and a single irreversible absorber of positive rate \(\kappa\) at \((1,1)\). Define its eventual capture probability from a basis state at \((x,y)\) by
\[
\eta_{x,y}=1-\lim_{t\to\infty}\left\|e^{-itH_{\mathrm{eff}}}|x,y\rangle\right\|^2,
\qquad H_{\mathrm{eff}}=J(A\otimes I+I\otimes A)-i\kappa|1,1\rangle\langle1,1|,
\]
where \(A\) is the adjacency matrix of \(P_n\). Then, for every \(J,\kappa>0\),
\[
\boxed{\eta_{x,y}=\begin{cases}
1,&x=y\in\{1,n\},\\
1-\frac{5}{6p},&x=y\notin\{1,n\},\\
\frac12,&x-y\text{ is odd},\\
\frac12-\frac{5}{6p},&|x-y|=2,\\
\frac12-\frac1p,&x\ne y\text{ and }|x-y|\ge4\text{ is even}.
\end{cases}}
\]
All five cases are disjoint and exhaustive; empty classes are permitted at the smallest primes. In this domain, **the only localized starting sites captured with certainty are the absorber itself and the opposite diagonal corner**. The multiplicities of the five cases, in displayed order, are
\[
2,\quad n-2,\quad \frac{n^2}{2},\quad 2(n-2),\quad\frac{n^2}{2}-3n+4.
\]
For \(p=3\), only the first and third classes occur. For \(p=5\), the final class is empty; from \(p\ge7\) all five occur. The exact uniform-site average is \(\frac12+\frac1{n^2}\); this average and the active-subspace dimension were previously known and are not claimed as new here.

## Assumptions and scope

The grid uses open path boundaries, not a periodic torus. The hopping is homogeneous and *adjacency based*, with no degree-dependent on-site potential. The absorber removes single-excitation probability at exactly one corner. The one-site loss term is \(-i\kappa|1,1\rangle\langle1,1|\) with \(\kappa>0\), so the instantaneous norm-loss rate is \(2\kappa|\langle1,1|\psi(t)\rangle|^2\). The result concerns the infinite-time integrated absorption probability, not a finite-time speed or hitting time. Every \(p\) in the statement is an odd prime. Both \(J\) and \(\kappa\) are arbitrary positive real numbers.

## Proof

**1. Spectral reduction and guaranteed decay of the accessible component.** The normalized path eigenvectors and corresponding eigenvalues are
\[
\phi_j(x)=\sqrt{\frac2p}\sin\!\left(\frac{\pi jx}{p}\right),\qquad
\lambda_j=2\cos\!\left(\frac{\pi j}{p}\right),\qquad 1\le j,x\le n.
\]
The grid eigenmodes are \(\phi_j\otimes\phi_k\), with energies \(J(\lambda_j+\lambda_k)\). Since \(p\) is prime, every \(\phi_j(1)\) is nonzero. If \(E_s\) is the orthogonal projector onto a distinct energy eigenspace of the Hermitian grid Hamiltonian, its bright direction is \(E_s|1,1\rangle\). Its orthogonal complement within that eigenspace consists of exactly those energy eigenvectors that vanish at the absorber. The sum of these dark directions reduces both the Hermitian Hamiltonian and \(H_{\mathrm{eff}}\). On its orthogonal complement, an eigenvector of \(H_{\mathrm{eff}}\) with a real eigenvalue would have zero overlap at the absorber by taking the imaginary part of its eigenvalue identity, contradicting the definition of the bright subspace. Finite dimensionality then forces exponential decay of all bright components. Hence \(\eta_{x,y}=\langle x,y|P_{\mathrm b}|x,y\rangle\), where \(P_{\mathrm b}\) is the sum of the rank-one projectors onto the nonzero vectors \(E_s|1,1\rangle\).

**2. Every energy collision is known exactly.** Set \(m=(p-1)/2\). The \(m\) real numbers \(\beta_j=2\cos(\pi j/p)\), \(1\le j\le m\), are linearly independent over \(\mathbb Q\). To see this, let \(\zeta=e^{2\pi i/p}\) and \(h=(p+1)/2\). Then \(\beta_j=(-1)^j(\zeta^{hj}+\zeta^{-hj})\). As \(j\) ranges from \(1\) to \(m\), the pairs \(\{hj,-hj\}\) partition the nonzero residues modulo \(p\). A rational linear dependence would give a polynomial of degree at most \(p-1\) that vanishes at \(\zeta\) and has zero constant term. It must be a scalar multiple of \(1+X+\cdots+X^{p-1}\), whose constant term is nonzero unless the scalar is zero. Thus the asserted independence holds. Since \(\lambda_{p-j}=-\lambda_j\), distinct sums of two eigenvalues coincide only by exchanging \(j,k\), or when both sums are zero. The zero-energy eigenspace consists precisely of the \(n\) ordered modes \((j,p-j)\).

**3. The bright projector.** Let \(T|x,y\rangle=|y,x\rangle\) be coordinate swap and \(P_+=(I+T)/2\). Away from energy zero, a nondegenerate \((j,j)\) mode or the symmetric combination of the exchanged \((j,k)\) modes is precisely the bright direction, since the absorber lies on the diagonal. At energy zero, the symmetric zero-energy eigenspace has dimension \(n/2\), but only the projection of the absorber onto that eigenspace is bright. Denote by \(P_{0,+}\) the projector onto the symmetric zero-energy eigenspace and by \(P_{0,w}\) the rank-one projector onto \(q=E_0|1,1\rangle\). Consequently,
\[
P_{\mathrm b}=P_+-P_{0,+}+P_{0,w}.
\]
This is an exact orthogonal-projector identity, not a perturbative approximation.

**4. Diagonal of the symmetric zero-energy projector.** For \(1\le j\le m\), the orthonormal symmetric zero modes are
\[
z_j=\frac{\phi_j\otimes\phi_{p-j}+\phi_{p-j}\otimes\phi_j}{\sqrt2}.
\]
The identity \(\phi_{p-j}(x)=(-1)^{x+1}\phi_j(x)\) shows that \(z_j(x,y)=0\) when \(x-y\) is odd. If \(x-y\) is even, the squared amplitudes sum to \(\sum_{j=1}^n\phi_j(x)^2\phi_j(y)^2\). A finite Fourier sum gives, for \(1\le x,y<p\),
\[
\sum_{j=1}^n\phi_j(x)^2\phi_j(y)^2=
\frac1p\left(1+\frac{\mathbf1_{x=y}+\mathbf1_{x+y=p}}2\right).
\]
Because \(p\) is odd, \(x+y=p\) cannot hold when \(x-y\) is even. Therefore
\[
\langle x,y|P_{0,+}|x,y\rangle
=\frac{\mathbf1_{x-y\text{ even}}}{p}\left(1+\frac{\mathbf1_{x=y}}2\right).
\]
The parity restriction in this formula is essential.

**5. The zero-energy bright direction is supported at diagonal and separation two.** Write \(w_j=\phi_j(1)\). Since \(w_{p-j}=w_j\) and \(w_j^2=(4-\lambda_j^2)/(2p)\), we obtain
\[
q(x,y)=(-1)^{y+1}\sum_{j=1}^nw_j^2\phi_j(x)\phi_j(y)
=\frac{(-1)^{y+1}}{2p}(4I-A^2)_{xy}.
\]
Here \(\|q\|^2=\sum_jw_j^4=3/(2p)\), from the diagonal matrix entry \((4I-A^2)_{11}=3\). For path adjacency, \((A^2)_{xy}=\deg(x)\mathbf1_{x=y}+\mathbf1_{|x-y|=2}\), with \(\deg(x)=1\) at endpoints and \(2\) elsewhere. Therefore
\[
\langle x,y|P_{0,w}|x,y\rangle
=\frac{\left[(4-\deg(x))\mathbf1_{x=y}-\mathbf1_{|x-y|=2}\right]^2}{6p}.
\]
Finally \(\langle x,y|P_+|x,y\rangle=(1+\mathbf1_{x=y})/2\). Substituting the last three diagonal identities into the formula for \(P_{\mathrm b}\) gives the five cases and their exact coefficients. Counting ordered pairs by coordinate parity and diagonal separation gives the stated five class sizes. All nonendpoint-diagonal probabilities are strictly below one; the endpoint diagonal probabilities equal one. This proves the precise full-capture criterion. The result is independent of \(J,\kappa>0\) because these parameters change decay rates but not the dark/bright orthogonal decomposition.

## Verification

The standalone `verify.py` recomputes the grid spectral eigenvectors, groups equal energies, projects every site onto each absorber-bright energy direction, and compares the resulting probabilities with the five-case formula. It also computes finite-time evolution under the non-Hermitian loss Hamiltonian as a separate dynamical check. Its recorded output is in `verification_output.txt`. Tests covered eight primes \(p\in\{3,5,7,11,13,17,19,23\}\), all 1,364 sites, and three non-Hermitian propagation comparisons. The largest direct spectral-site discrepancy was approximately \(2.78\times10^{-15}\). The symbolic Fourier and projector argument above, not those finite tests, proves the theorem for all odd primes.

## Relationship to prior work

Varbanov, Krovi, and Brun develop general absorption and dark-subspace criteria for continuous-time quantum walks under a measurement-based model. Anishchenko, Blumen, and Mülken study transport on two-dimensional random-bond lattices with boundary trapping sites. Novo and collaborators, and Razzoli, Paris, and Bordone, establish the general trapping/Krylov-subspace methodology for coherent quantum networks. These precedents motivate the finite-grid problem, but their inspected statements and sections do not give the displayed corner-trap five-valued site law. An earlier exact calculation on the same isotropic prime-sided square grid determines the mixed-initial-state capture average and active-space dimension, as well as selected two-absorber dimensions. This antecedent is explicitly excluded from the novelty claim: knowing a projector's rank or trace does not determine its complete sitewise diagonal. The additional result here is the all-vertex five-class spatial law, with its opposite-corner full capture and separation-two anomaly. Historical coverage is not claimed exhaustive.

## Limitations

Only odd-prime shifted side lengths, uniform adjacency hopping, a single positive-rate corner absorber, pure basis-state launches, and infinite-time capture are classified. This result does not describe arbitrary composite lengths, degree-weighted graph Laplacians, disorder, decoherence, multiple absorbers, or capture-time distributions. The proof is analytic; finite checks are illustrative rather than exhaustive for all sizes. The originality comparison is based on the located literature and available exact comparison statements and is not an independent priority certification.

## References

1. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first posted 2008-03-24), https://arxiv.org/abs/0803.3446 .
2. A. Anishchenko, A. Blumen, and O. Mülken, *Geometrical aspects of quantum walks on random two-dimensional structures*, arXiv:1309.2827 (first posted 2013-09-11), https://arxiv.org/abs/1309.2827 .
3. L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, Scientific Reports 5, 13304 (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4557070/ .
4. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794 (2020), https://pmc.ncbi.nlm.nih.gov/articles/PMC7826824/ .
