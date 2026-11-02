# Two-leaf coherent capture on complete branching trees: an exact totient placement law

## Finding

**Theorem (exact two-absorber bright dimension).** For integers \(b\geq3\) and \(L\geq1\), let \(T_{b,L}\) be the finite rooted tree in which each vertex at depths \(0,1,\ldots,L-1\) has exactly \(b\) children and every leaf has depth \(L\). Its number of sites is
\[
N_{b,L}=\frac{b^{L+1}-1}{b-1}.
\]
Let \(A\) be the ordinary real symmetric *adjacency* matrix of this tree, with unit hopping on each edge and zero on-site energies. For distinct leaves \(s,t\), let their lowest common ancestor have depth \(L-h\), equivalently their graph distance is \(2h\), where \(1\leq h\leq L\). Define
\[
D(m)=\sum_{q=2}^{m+2}\varphi(q) \qquad(m\geq0),
\]
where \(\varphi\) is Euler's totient function. Then the bright (reachable) subspace
\[
\mathcal K_{s,t}=\operatorname{span}\{A^k e_s,A^k e_t:0\leq k<N_{b,L}\}
\]
has **exact** dimension
\[
\boxed{\dim\mathcal K_{s,t}=D(L)+D(h-1).}
\]

For arbitrary fixed rates \(\gamma_s,\gamma_t>0\), introduce local irreversible capture via
\[
H_{\mathrm{eff}}=A-i\gamma_s e_se_s^* -i\gamma_t e_te_t^*,
\qquad \psi(z)=e^{-iH_{\mathrm{eff}}z}\psi(0).
\]
The eventual absorbed probability for any initial density matrix \(\rho_0\) is precisely
\[
P_{\mathrm{capture}}(\rho_0)
=\operatorname{tr}(\Pi_{\mathcal K_{s,t}}\rho_0),
\]
with \(\Pi_{\mathcal K_{s,t}}\) the orthogonal projection onto the displayed subspace. In particular, for the maximally mixed one-excitation state \(\rho_0=I/N_{b,L}\),
\[
\boxed{P_{\mathrm{capture}}=\frac{D(L)+D(h-1)}{N_{b,L}}.}
\]
For the uniform mixture over the \(N_{b,L}-2\) nonabsorbing sites, the answer is \((D(L)+D(h-1)-2)/(N_{b,L}-2)\). Both formulas are independent of the two *positive* absorption rates.

The capture fraction increases **strictly** with the leaf separation \(2h\). Thus the optimal absorber pair consists of leaves in different first-level branches, and the worst pair is two siblings. The respective exact bright dimensions are \(D(L)+D(L-1)\) and \(D(L)+1\). At fixed \(b\geq3\), the maximal bright dimension is \(6L^2/\pi^2+O(L\log L)\), while \(N_{b,L}\) grows exponentially; hence even optimally placed two absorbers have vanishing asymptotic capture probability from the maximally mixed state.

## Assumptions and scope

The vertex set is labeled by all words of length at most \(L\) over a \(b\)-symbol alphabet; edges join each word to its one-letter extensions. The hopping Hamiltonian is *adjacency*, not the degree-normalized walk, graph Laplacian, or a disordered Hamiltonian. The effective Hamiltonian convention gives a squared-norm loss rate \(2\gamma_s|\langle e_s,\psi\rangle|^2+2\gamma_t|\langle e_t,\psi\rangle|^2\). The initial density matrix is any positive semidefinite trace-one matrix on the single-excitation site Hilbert space. All limits are at fixed finite \(b,L\), positive fixed capture rates, and evolution time \(z\to\infty\). We require \(b\geq3\), \(L\geq1\), and two distinct leaves.

## Proof

**1. Exact distinct adjacency spectrum.** For \(m\geq1\), set \(p_0(x)=1\), \(p_1(x)=x\), and \(p_{m+1}(x)=xp_m(x)-bp_{m-1}(x)\). The tridiagonal radial adjacency matrix on \(m\) levels has off-diagonals \(\sqrt b\) and characteristic polynomial \(p_m\); hence its eigenvalues are
\[
\lambda_{m,j}=2\sqrt b\cos\left(\frac{j\pi}{m+1}\right),
\quad 1\leq j\leq m.
\]
Decompose functions on the tree into the root-radial part, and at each interior vertex the \(b-1\) mutually orthogonal child-antisymmetric branch spaces, extended radially down each of the remaining levels. Each branch space is a Jacobi block of one of lengths \(1,\ldots,L\); the root-radial block has length \(L+1\). These blocks span all vertices: their dimension sum is \(L+1+\sum_{d=0}^{L-1}b^d(b-1)(L-d)=N_{b,L}\). Thus the full eigenvalue *set* is the union of the roots \(\{\lambda_{m,j}:1\leq m\leq L+1,1\leq j\leq m\}\). Cosine is injective on \((0,\pi)\). Distinct roots correspond to reduced rational numbers \(j/(m+1)\) with denominators \(2\) through \(L+2\). Consequently the number of distinct eigenvalues is exactly \(D(L)\). This distinct-spectrum fact and its tridiagonal decomposition are established background in work on finite branching-tree spectra, rather than a standalone novelty claim here.

**2. Every eigenvalue is visible from one leaf.** Fix a spectral value \(\lambda\) and the spectral projector \(P_\lambda\). If \(P_\lambda e_s=0\), all \(\lambda\)-eigenvectors have value zero at leaf \(s\). The rooted automorphism group acts transitively on the leaves and preserves each eigenspace, so every such eigenvector vanishes at every leaf. The eigen-equation at a leaf then forces its parent to vanish; induction from the outermost level inwards forces the entire eigenvector to be zero. Contradiction. Hence \(P_\lambda e_s\ne0\) for every eigenvalue. Therefore the single-leaf Krylov dimension is \(D(L)\).

**3. Exactly when the second leaf adds a spectral direction.** Fix \(s,t\) with lowest common ancestor \(v\) at depth \(L-h\). Write \(U\) for the common rooted child-subtree, isomorphic to \(T_{b,h-1}\), and let \(B\) be its adjacency. If \(\lambda\notin\operatorname{spec}(B)\), then the restriction of any full-tree eigenvector \(f\) to any child branch of \(v\) satisfies
\[
(\lambda I-B)f_{\mathrm{branch}}=f(v)e_{\mathrm{branch\ root}}.
\]
Uniqueness of the solution shows that these restrictions agree at corresponding leaf positions. Applying rooted automorphisms within the child subtrees then shows \(f(s)=f(t)\) for every \(\lambda\)-eigenvector. Equivalently, \(P_\lambda e_s=P_\lambda e_t\); the two sites contribute one direction at this eigenvalue.

Conversely suppose \(\lambda\in\operatorname{spec}(B)\). By the preceding leaf-visibility argument on \(U\), take an eigenvector \(w\) of \(B\) that is nonzero at the position corresponding to \(s\) (and, after identifying branches, to \(t\)). Choose a third child branch of \(v\), possible since \(b\geq3\). On the three branches place respectively the same copy of \(w\), scaled by coefficients \((1,0,-1)\), and zero on all other vertices; this is a full-tree \(\lambda\)-eigenvector, because its branch-root amplitudes sum to zero at \(v\). Repeating with coefficients \((0,1,-1)\) yields a second eigenvector. Their values at \((s,t)\) are respectively \((w_s,0)\) and \((0,w_s)\). Thus \(P_\lambda e_s,P_\lambda e_t\) are linearly independent. This proves that each eigenvalue of the small subtree contributes *two* bright directions, while every other eigenvalue contributes exactly one. Since \(\operatorname{spec}(B)\subseteq\operatorname{spec}(A)\), the rank is
\[
\dim\mathcal K_{s,t}
=|\operatorname{spec}(A)|+|\operatorname{spec}(B)|
=D(L)+D(h-1).
\]
Here the spectral decomposition of the cyclic space follows by polynomial interpolation: for real symmetric \(A\), the \(A\)-orbit of the two site vectors is the orthogonal sum over \(\lambda\) of \(\operatorname{span}\{P_\lambda e_s,P_\lambda e_t\}\).

**4. Capture law and optimal placement.** The invariant orthogonal decomposition \(\mathbb C^N=\mathcal K_{s,t}\oplus\mathcal K_{s,t}^\perp\) reduces \(A\), and both loss projectors vanish on \(\mathcal K_{s,t}^\perp\). All states there retain norm forever. On \(\mathcal K_{s,t}\), the evolution generator is \(G=-iA-\Gamma\), where \(\Gamma=\gamma_se_se_s^*+\gamma_te_te_t^*\geq0\). If an eigenvalue of \(G\) had zero real part, its eigenvector \(x\ne0\) would satisfy \(\langle x,\Gamma x\rangle=0\), so \(\langle e_s,x\rangle=\langle e_t,x\rangle=0\), and would be an eigenvector of \(A\). It would consequently be orthogonal to every generator of \(\mathcal K_{s,t}\), contradicting \(x\in\mathcal K_{s,t}\). Thus all eigenvalues of \(G\) have strictly negative real part, so its finite-dimensional semigroup decays to zero, and the final captured weight is exactly the initial bright-space weight. Since \(e_s,e_t\in\mathcal K_{s,t}\), the nontrap-uniform formula follows by subtracting the two diagonal projector traces. Finally \(D(h)-D(h-1)=\varphi(h+2)>0\), proving strict monotonicity, with the displayed optimum and asymptotic from the classical summatory-totient estimate.

## Verification

A standalone, standard-library Python script `checker.py` constructs the exact integer adjacency action and performs Gaussian elimination over two separate prime fields on all cyclic vectors. For \(b=3\) and \(L=1,2,3,4\), \(b=4\) and \(L=1,2,3\), and \(b=5,6\) with \(L=1,2\), all tested two-leaf distances have the claimed rank modulo both primes. The 121-vertex, three-branch, depth-four case has bright dimensions \(12,14,16,20\) for \(h=1,2,3,4\). Additional noncanonical leaf pairs verify the dependence on lowest-common-ancestor depth. A boundary test establishes that the theorem does not extend unchanged to binary branching: for \(b=2,L=2,h=2\), the true bright rank is \(6\), whereas substituting into the \(b\geq3\) formula incorrectly gives \(8\). See `checker_output.txt` for complete recorded results.

Modular computations are tests, not a proof over the rationals or for arbitrary depth. The universal assertion is established by the spectral argument above; no large-depth enumeration or numerical long-time extrapolation is assumed.

## Relationship to prior work

Mülken, Bierbaum and Blumen (2006) studied coherent transport and recurrences in dendrimers, with a different dendrimer branching convention and a degree-based connectivity Hamiltonian; they do not give the two-leaf, positive-rate capture classification here. Mülken and collaborators (2007) studied coherent transfer *with traps*, mainly on linear systems and in the intermediate-time survival regime. Novo and collaborators (2014) developed the general invariant/Krylov-subspace method for transport and illustrated a **single root trap on a binary tree**; the general projection principle in step 4 is therefore not new. Lin and Zhang (2013) derived trapping-time expressions for **classical random walks** on Cayley trees, a different model and metric. Scarabotti (2005/2006) derived finite \(q\)-ary tree adjacency spectral formulas; its underlying spectral facts are prior art. Zhang (2023) also discusses distinct eigenvalues of level-symmetric trees. The specific new comparison target is the exact *two-peripheral-site* bright-rank increment \(D(h-1)\), its sharp \(b\geq3\) branching condition, and the consequent all-separations capture-placement law. None of the accessible inspected portions established those claims; historical novelty is necessarily provisional.

## Limitations

The exact law concerns homogeneous adjacency hopping, a perfectly complete finite rooted \(b\)-ary tree, two leaves as absorbers, and strictly positive loss rates. It does not provide capture-time distributions or convergence rates, and it need not survive disorder, on-site energies, dephasing, interactions, different trap locations, or a graph Laplacian in place of adjacency. The binary case violates the displayed formula, as verified above. Claims about the *infinite* tree are limited to the normalized finite-tree sequence stated, not an infinite-volume spectral-dynamics theorem. A relevant full spectral-decomposition paper of Scarabotti was available only through its abstract and bibliographic record, so complete priority comparison remains an outstanding limitation.

## References

1. O. Mülken, V. Bierbaum and A. Blumen, “Coherent exciton transport in dendrimers and continuous-time quantum walks,” first public preprint 2006-02-02, https://arxiv.org/abs/cond-mat/0602040 .
2. O. Mülken, A. Blumen, T. Amthor, C. Giese, M. Reetz-Lamour and M. Weidemüller, “Survival Probabilities in Coherent Exciton Transfer with Trapping,” preprint 2007-05-25, https://arxiv.org/abs/0705.3700 .
3. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, “Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs,” preprint 2014-12-22, https://arxiv.org/abs/1412.7209 .
4. Y. Lin and Z. Zhang, “Influence of trap location on the efficiency of trapping in dendrimers and regular hyperbranched polymers,” preprint 2013-02-21, https://arxiv.org/abs/1302.5227 .
5. F. Scarabotti, “The Discrete Sine Transform and the Spectrum of the Finite q-ary Tree,” SIAM J. Discrete Math. 19, 1004–1010, DOI: 10.1137/S0895480104445344 .
6. Y. Zhang, “Upper bounds for PSD propagation time and zero forcing in shadow graphs,” doctoral dissertation, Drexel University, June 2023, DOI: 10.17918/00001629 .
