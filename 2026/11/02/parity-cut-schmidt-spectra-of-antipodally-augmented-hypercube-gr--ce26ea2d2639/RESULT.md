# Parity-cut Schmidt spectra of antipodally augmented hypercube graph states

## Finding

For any \(n\ge3\), let \(FQ_n\) be the graph on \(\mathbb F_2^n\) whose distinct vertices \(x,y\) are adjacent exactly when \(x+y\) equals a standard basis vector \(e_i\) or the all-one vector \(\mathbf1\). The latter edges form an antipodal perfect matching. Associate a qubit to every graph vertex, and prepare the unweighted graph state
\[
|FQ_n\rangle=\prod_{\{x,y\}\in E(FQ_n)}CZ_{x,y}\,|+\rangle^{\otimes 2^n}.
\]
For each nonempty coordinate set \(S\subseteq[n]\), let \(t=|S|\), and split the qubits into
\[
A_S=\{x:\sum_{i\in S}x_i=0\pmod2\},\qquad
B_S=\{x:\sum_{i\in S}x_i=1\pmod2\}.
\]
The reduced state on \(A_S\) has precisely \(2^{r_{n,t}}\) nonzero eigenvalues, all equal to \(2^{-r_{n,t}}\), where
\[
r_{n,t}=\begin{cases}
2^{n-2}-2^{(n-3)/2},& n\text{ odd and }t=n,\\
2^{n-2},&\text{otherwise}.
\end{cases}
\]
In particular the von Neumann entropy in bits, every positive-order Rényi entropy, and the logarithm base two of the Schmidt rank all equal \(r_{n,t}\). The difference between a proper odd-coordinate parity cut and the corresponding cut of the ordinary cube is exactly \(2^{n-2}\) bits. At the exceptional full parity cut with \(n\) odd, a further dyadic deficit \(2^{(n-3)/2}\) occurs.

## Assumptions and scope

The integer \(n\) is at least three, so all \(n+1\) displacement types are distinct and all edges are simple. Every graph vertex carries exactly one qubit, each edge carries one standard controlled-\(Z\) interaction, and the state is pure. All coordinate sets \(S\) are nonempty and otherwise unrestricted; the two parts each contain \(2^{n-1}\) qubits. This is an entropy for a specified structured cut, **not** a claim about minimizing graph rank-width over all decompositions. The quantum state is a qubit graph state, **not** a ground state of a free-fermion hopping Hamiltonian. Entropies are measured in bits. Some graph-theory conventions use a different index for a quotient folded cube; the explicit \(2^n\)-vertex antipodally augmented definition above fixes the intended graph.

## Proof

**1. Graph-state cut-spectrum lemma.** Let \(G\) be any finite simple graph with qubit bipartition \(A\cup B\), and let \(C\) be its \(\mathbb F_2\) adjacency submatrix from \(A\) to \(B\). Controlled-\(Z\) gates confined to one part are local unitaries for this split and do not change its Schmidt spectrum. After their removal the state amplitudes are \(2^{-(|A|+|B|)/2}(-1)^{a^TCb}\). Its reduced Gram matrix has entries
\[
\rho_{a,a'}=2^{-|A|}\mathbf1_{\{C^T(a+a')=0\}}.
\]
Thus \(\rho\) is the scaled convolution operator by \(\ker C^T\); it has \(2^{\operatorname{rank}C}\) equal nonzero eigenvalues \(2^{-\operatorname{rank}C}\). This also directly proves the flatness assertion without assuming a separate spectral theorem.

**2. Characteristic-two algebra and cross-cut rank.** Write \(R_n=\mathbb F_2[y_1,\ldots,y_n]/(y_i^2)\), identified with the group algebra of \(\mathbb F_2^n\) by \(X_i=1+y_i\) for translation by \(e_i\). The antipodal translation is \(P=\prod_iX_i\). Only edges whose displacement has odd intersection with \(S\) cross the cut. Their adjacency operator over \(\mathbb F_2\), acting by multiplication on the group algebra, is
\[
D_S=\sum_{i\in S}X_i+(t\bmod2)P.
\]
Translations appearing in \(D_S\) reverse \(S\)-parity; ordered by the two parity classes, the matrix is \(\bigl(\begin{smallmatrix}0&C\\C^T&0\end{smallmatrix}\bigr)\). Consequently \(\operatorname{rank}C=\frac12\operatorname{rank}D_S\). Notice that ranks are exclusively over \(\mathbb F_2\), not over the reals.

**3. All ordinary parity cuts.** A basic algebraic fact: if \(f\in R_n\) has zero constant term and a nonzero degree-one coefficient, multiplication by \(f\) has rank \(2^{n-1}\). Indeed write \(f=a+y_jb\), with \(a,b\) independent of \(y_j\) and \(b\) a unit (constant coefficient one). Substituting \(y_j\mapsto f\), fixing the other generators, is an algebra automorphism: its inverse sends \(y_j\) to \((y_j+a)b^{-1}\), because every zero-constant element of \(R_n\) squares to zero. Multiplication by \(f\) therefore has the rank of multiplication by \(y_j\), namely \(2^{n-1}\).

If \(t\) is even, \(D_S=\sum_{i\in S}y_i\) has a nonzero linear part. If \(t\) is odd and \(t<n\), its constant part cancels and its degree-one part is \(\sum_{i\notin S}y_i\), also nonzero. Hence in both cases \(\operatorname{rank}C=2^{n-2}\), as asserted.

**4. The exceptional odd-dimensional full parity cut.** Assume \(t=n=2m+1\) with \(m\ge1\), and write \(h_i=PX_i\), where \(P^2=X_i^2=1\). Multiplying the cut operator \(D_S=P+\sum_iX_i\) by invertible \(P\) gives \(1+\sum_ih_i\). The \(h_i\) are even-weight translations, their product is one, and \(h_1,\ldots,h_{2m}\) form a basis for the index-two even-translation subgroup. Therefore multiplication on the full group algebra is two identical copies of multiplication by
\[
Q_m=1+\sum_{i=1}^{2m}h_i+\prod_{i=1}^{2m}h_i
\]
on the \(2^{2m}\)-dimensional group algebra of the even-translation subgroup. Since \(\operatorname{rank}C=\frac12\operatorname{rank}D_S\), the desired entropy is \(\operatorname{rank}(\times Q_m)\).

Set \(Q_0=0\) and, for the induction from \(m-1\) to \(m\), let \(q=\prod_{i=1}^{2m-2}h_i\), \(a=qh_{2m-1}\), \(b=qh_{2m}\). Together with the preceding \(h_i\), the new \(a,b\) are independent group generators and
\[
Q_m=Q_{m-1}+q(1+a)(1+b).
\]
The nilpotents \(u=1+a\) and \(v=1+b\) satisfy \(u^2=v^2=0\). Since \(q\) is a unit in the earlier-variable subalgebra, replacing \(u\) by \(qu\) while fixing \(v\) and the earlier variables is a ring automorphism. Applying this step inductively shows that multiplication by \(Q_m\) is conjugate, as a linear map, to multiplication by
\[
\omega_m=\sum_{j=1}^m u_jv_j
\]
on \(R=\bigotimes_{j=1}^m\mathbb F_2[u_j,v_j]/(u_j^2,v_j^2)\). The proof uses an explicit algebra change of variables, not a numerical conjecture.

Now \(\omega_m^2=0\), so multiplication is a differential \(d\) on this \(4^m\)-dimensional vector space. Each four-dimensional factor splits into the acyclic two-dimensional subcomplex \(\operatorname{span}\{1,u_jv_j\}\), with differential \(1\mapsto u_jv_j\), plus the zero-differential two-dimensional subcomplex \(\operatorname{span}\{u_j,v_j\}\). The tensor differential is the sum of these local differentials (in characteristic two). Any tensor factor of the acyclic type makes its tensor complex contractible, while the unique all-zero-differential summand contributes \(2^m\) homology dimensions. Thus
\[
\dim\ker d-\dim\operatorname{im}d=2^m,
\quad 4^m=2\operatorname{rank}d+2^m,
\quad \operatorname{rank}d=2^{2m-1}-2^{m-1}.
\]
Replacing \(n=2m+1\) proves the exceptional formula.

**5. Comparison with the unaugmented hypercube.** For \(Q_n\) (antipodal edges absent) the parity-crossing operator is \(D_S^{\rm cube}=\sum_{i\in S}X_i\). For odd \(t\) this has constant coefficient one and hence is an invertible element of the local group algebra, giving cut rank \(2^{n-1}\); for even \(t\) it has nonzero linear part and gives rank \(2^{n-2}\). Thus adding the entire antipodal perfect matching selectively *reduces* rather than increases entanglement for every odd \(t\), with the additional odd-dimensional full-parity correction quantified above.

## Verification

The standalone `verify.py` constructs every actual cross-cut adjacency matrix over \(\mathbb F_2\) and performs independent pivot elimination. It checks all nonempty coordinate subsets for dimensions \(3\le n\le9\), plus every representative subset size for \(n=10,11\), totaling **1030 exact cut-rank checks**. It additionally constructs the full controlled-\(Z\) state-vector amplitudes and directly diagonalizes reduced density matrices for six small cases at dimensions three and four (using NumPy). All checks passed. Run `python3 verify.py` (Python 3; NumPy required only for the final reduced-state numerical tests). See `verification_output.txt`. These are finite corroborations; the proof above establishes all \(n\ge3\).

## Relationship to prior work

Hein, Eisert and Briegel's general graph-state Schmidt cut-rank theorem (initial public version 2003) supplies the standard background rule, also reconstructed independently in Step 1. Hashizume and collaborators (2021) analyzed ordinary hypercube graph states for quantum scrambling, including sampled cut ranks, but not the antipodally augmented graph and the exhaustive structured parity-cut spectrum here. Wang and collaborators (2011) specify the same \(2^n\)-vertex folded-cube network and study its graph crossing number rather than mod-two cut ranks. Published 2014 spectral-index treatments of folded cubes concern **real** adjacency eigenvalues, not the \(\mathbb F_2\) rank needed here. The reported entropy for the even-dimensional full Hamming parity cut of the ordinary hypercube is already available separately; no novelty is claimed for that bare-cube subcase. The contribution asserted here is the antipodal augmentation's exact all-coordinate-parity-cut law and its exceptional odd-dimensional correction. The literature comparison is best-knowledge rather than a proof that an equivalent older binary adjacency-rank lemma does not exist.

## Limitations

No result is asserted for arbitrary bipartitions, graph states in other local dimensions, noisy preparations, free-fermion ground states or operational quantum-code performance. The mathematical novelty assessment is provisional: older algebraic coding theory or binary graph-rank formulas could imply this evaluation without using quantum terminology. Direct density-matrix tests necessarily cover only small examples; higher-dimensional tests use exact binary rank instead.

## References

- M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first public 2003-07-18), especially Section III.2. https://arxiv.org/html/quant-ph/0307130v7
- H. Wang, Y. Yang, Y. Zhou, W. Zheng and G. Wang, *The crossing number of folded hypercubes*, arXiv:1101.3386 (2011-01-18). https://arxiv.org/abs/1101.3386
- T. Hashizume, G. Bentsen, S. Weber and A. J. Daley, *Deterministic Fast Scrambling with Neutral Atom Arrays*, arXiv:2102.13117 (2021-02-25), main text and graph-state Supplement. https://arxiv.org/html/2102.13117v3
- J.-B. Liu, X.-F. Pan and J. Cao, *Some Properties on Estrada Index of Folded Hypercubes Networks*, *Abstract and Applied Analysis* (2014). https://doi.org/10.1155/2014/167623
- L. Vinet and collaborators, *Absence of logarithmic enhancement in the entanglement scaling of free fermions on folded cubes*, *Journal of Physics A* (2023). https://doi.org/10.1088/1751-8121/ad0f4a
