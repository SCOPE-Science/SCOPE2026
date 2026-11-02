# Two-sink capture universality and site-resolved absorption on primitive strongly regular quantum networks

## Finding

**Theorem.** Let \(G\) be any primitive strongly regular graph of parameters \((v,k,\lambda,\mu)\). For any two distinct absorbing vertices \(a,b\), any uniform nonzero real hopping constant \(J\), and any positive absorption rates at those vertices, the continuous-time single-excitation quantum walk has a five-dimensional bright subspace and a dark subspace of dimension \(v-5\). Thus the eventual capture probability from the completely mixed one-excitation state is exactly
\[
\eta_{\mathrm{mixed}}=\frac5v,
\]
and from a uniformly random initial nonabsorbing vertex is \(3/(v-2)\). Both averages are independent of absorber separation, rates, and the graph realization.

There is a stronger **site-resolved universality law**. For nonabsorbing \(x\), write \(\delta=A_{ab}\), \(\alpha=A_{ax}\), \(\beta=A_{bx}\), and \(q=v-1-k\). The two nonprincipal adjacency eigenvalues are \(r>s\), the roots of
\[
 z^2-(\lambda-\mu)z-(k-\mu)=0,
\]
with multiplicities \(m_r,m_s\). Put
\[
 c_{\theta}(1)=\frac{\theta}{k},\qquad c_{\theta}(0)=-\frac{1+\theta}{q}.
\]
Then the exact eventual capture probability is
\[
\boxed{\eta(x)=\frac1v+\sum_{\theta\in\{r,s\}}\frac{m_\theta}{v}\,
\frac{c_{\theta}(\alpha)^2+c_{\theta}(\beta)^2
 -2c_{\theta}(\delta)c_{\theta}(\alpha)c_{\theta}(\beta)}
 {1-c_{\theta}(\delta)^2}.}
\]
The two sinks each have capture probability one. Formula and multiplicities show that the complete multiset of site capture probabilities is determined by \((v,k,\lambda,\mu,\delta)\), including on nonisomorphic graphs with identical parameters.

Among nonabsorbing vertices, the classes adjacent to both sinks, to exactly one sink, and to neither have respective sizes
\[
 t_\delta,\qquad 2(k-\delta-t_\delta),\qquad v-2-2k+2\delta+t_\delta,
\]
where \(t_1=\lambda\) and \(t_0=\mu\). Hence there are at most three distinct nonsink capture probabilities. The probability is always independent of the positive absorption rates, although the finite-time dynamics need not be.

For example, the nonisomorphic Shrikhande and \(4\times4\) rook graphs both have parameters \((16,6,2,2)\). With adjacent sinks, their nonsink capture laws are identically: two sites at \(5/16\), six at \(1/4\), and six at \(7/48\). With nonadjacent sinks: two sites at \(3/10\), eight at \(1/5\), and four at \(1/5\). The fully mixed efficiency in both cases is \(5/16\).

## Assumptions and scope

A primitive strongly regular graph here is a finite undirected simple noncomplete nonempty graph, with both the graph and its complement connected, satisfying: all vertices have degree \(k\), every adjacent pair has \(\lambda\) common neighbors, and every nonadjacent pair has \(\mu\) common neighbors. Write \(A\) for its real symmetric adjacency matrix. The Hilbert space \(\mathbb C^v\) has its usual vertex basis \(\{e_x\}\). For arbitrarily chosen distinct sink vertices \(a,b\), hopping \(J\in\mathbb R\setminus\{0\}\), and rates \(\kappa_a,\kappa_b>0\), the unnormalized no-jump state evolves by
\[
 \frac{d\psi}{dt}=\left(-iJA-\tfrac12\kappa_a e_ae_a^* -\tfrac12\kappa_b e_be_b^*\right)\psi.
\]
The eventual capture efficiency of a normalized initial state is one minus the infinite-time squared norm. A mixed initial state has the corresponding trace-average efficiency. No finite-time capture rate, nonlinear interaction, disorder, or dephasing is asserted.

## Proof

**1. Adjacency algebra and spectral projectors.** Strong regularity yields
\[
 A^2=(k-\mu)I+(\lambda-\mu)A+\mu\mathbf1\mathbf1^T.
\]
Therefore \(A\) has exactly three distinct eigenvalues \(k,r,s\). Let \(E_k=\mathbf1\mathbf1^T/v\) and \(E_r,E_s\) be the orthogonal spectral projectors; then \(m_\theta=\mathrm{tr}(E_\theta)\), with explicit multiplicities
\[
 m_r=\frac{-k-(v-1)s}{r-s},\qquad m_s=v-1-m_r.
\]
Each \(E_\theta\) is a linear combination of \(I,A,\mathbf1\mathbf1^T\). Its diagonal entries are \(m_\theta/v\). From \(AE_\theta=\theta E_\theta\), the adjacent entry is \((m_\theta/v)\theta/k\); row sum zero gives the nonadjacent entry \(-(m_\theta/v)(1+\theta)/q\). Thus for distinct \(x,y\)
\[
 E_\theta(x,y)=\frac{m_\theta}{v}c_\theta(A_{xy}).
\]

**2. Strict two-sink independence.** A primitive strongly regular graph is connected, regular, and nonbipartite; its complement is likewise connected, regular, and nonbipartite. Indeed a connected bipartite strongly regular graph is complete bipartite and has disconnected complement. The elementary strict spectral radius inequalities consequently give \(|r|,|s|<k\) and \(|1+r|,|1+s|<q\), since the corresponding nonprincipal eigenvalues of the complement are \(-1-r,-1-s\). Hence \(|c_\theta(\delta)|<1\) for either sink adjacency \(\delta\). Therefore the two vectors \(E_\theta e_a,E_\theta e_b\) are linearly independent for each \(\theta=r,s\), because their Gram matrix is
\[
 U^*E_\theta U=\frac{m_\theta}{v}
 \begin{pmatrix}1&c_\theta(\delta)\\c_\theta(\delta)&1\end{pmatrix},
 \qquad U=(e_a,e_b).
\]
The principal eigenspace contributes the single vector \(\mathbf1\). Since the three eigenspaces are mutually orthogonal, the space
\[
 \mathcal B=\operatorname{span}\{A^je_a,A^je_b:0\le j\le2\}
 =\operatorname{ran}(E_kU)\oplus\operatorname{ran}(E_rU)\oplus\operatorname{ran}(E_sU)
\]
has dimension \(1+2+2=5\). Its orthogonal complement is \(A\)-invariant and annihilated by both sinks.

**3. Equality of the absorbing and bright spaces.** The no-jump generator preserves \(\mathcal B\) and its orthogonal complement. On \(\mathcal B^\perp\) the evolution is unitary, so no norm is lost. Suppose an eigenvector of the restriction to \(\mathcal B\) had an eigenvalue with zero real part. The real part of its Rayleigh quotient would give \(\kappa_a|\psi_a|^2+\kappa_b|\psi_b|^2=0\). Thus both sink amplitudes vanish, and the eigenvector must be an eigenvector of \(A\) orthogonal to \(e_a,e_b\), contradicting its membership in \(\mathcal B\). Every restricted eigenvalue therefore has strictly negative real part, hence its semigroup decays. Consequently for every initial density matrix \(\rho\), eventual absorption is \(\mathrm{Tr}(P_{\mathcal B}\rho)\). This establishes both rate independence and the mixed efficiency \(\operatorname{tr}(P_\mathcal B)/v=5/v\).

**4. Exact site probability.** By orthogonality of the eigenspaces and the invertible two-by-two Gram matrices,
\[
 P_\mathcal B=E_k+\sum_{\theta\in\{r,s\}}
 E_\theta U(U^*E_\theta U)^{-1}U^*E_\theta.
\]
Taking the diagonal entry at \(x\) and substituting the entries in step 1 gives precisely the displayed boxed formula for nonsink \(x\). Each sink belongs to \(\mathcal B\), so its diagonal is one. The trace is five; therefore nonsink diagonal entries sum to three and their uniform mean is \(3/(v-2)\).

**5. Population universality.** For adjacent sinks, their common neighbors number \(\lambda\), while for nonadjacent sinks they number \(\mu\). Each sink has \(k-\delta\) neighbors other than the opposite sink; subtract common neighbors to obtain exactly-one and neither class counts. These counts and the boxed efficiency depend only on the strongly regular parameters and sink adjacency, proving the full site-resolved universality statement.

**Boundary.** The primitive assumption matters. In the imprimitive complete tripartite graph \(K_{2,2,2}\), sinks in the same part have a three-dimensional bright space, while sinks in different parts have a five-dimensional one; hence a universal five-dimensional statement fails without the assumption.

## Verification

The standalone `verify.py` uses independent singular-value decompositions of the Krylov matrix and the projector formula, checking all \(598\) sink pairs on seven primitive examples (cycle of length five, Petersen, \(4\times4\) rook, Shrikhande, triangular graph on six points, Paley graph of order thirteen, and Clebsch). It checks every vertex of every pair, including the corresponding \(8{,}849\) site-level formulas, rank, sink normalization, trace, and nonsink sum. The maximum projector discrepancy over these examples is below \(1.6\times10^{-15}\). Both sink-placement cases on \(K_{2,2,2}\) were checked. `exact_examples.py` independently confirms the symbolic fractions and population sums for selected families. Both programs require the dependencies in `requirements.txt`; their actual executed output is in `verification_output.txt`.

These finite tests support the reasoning but are not a proof for arbitrary graph orders. The unrestricted result is justified by the spectral argument above.

## Relationship to prior work

Novo et al. (public preprint of December 22, 2014) establish Krylov reduction for quantum transport, with a single trap and examples such as complete graphs and hypercubes. Razzoli, Paris and Bordone (public preprint November 27, 2020) treat graph transport with **one** absorbing vertex, including strongly regular graphs. Both give underlying techniques and single-trap benchmarks, not the present two-trap complete parameter-and-placement law. Li et al. (2019) address **two marked vertices** on strongly regular graphs using **Hermitian loop potentials for unitary spatial search**; such coherent marking is not the same evolution as irreversible absorption. Only its accessible abstract and introductory preview were examined, so possible stronger coverage elsewhere in the article is a residual priority risk. This result builds on standard projector and adjacency-algebra identities; none of those standard ingredients is claimed as new.

The general \(5/v\) identity includes special highly symmetric strongly regular graph families, and the distinctive assertion assessed here is the simultaneous all-primitive-graph bright-rank law and the full per-site efficiency distribution depending only on \((v,k,\lambda,\mu,\delta)\).

## Limitations

The theorem assumes finite primitive strongly regular graphs, a uniform real hopping amplitude, precisely two distinct absorbing sites with strictly positive rates, and the no-jump one-excitation quantum dynamics. Zero rates, imprimitive strongly regular graphs, disorder, dephasing, finite-time absorption, multiple simultaneous excitations, and three or more sinks are not classified. The mathematical conclusion is internally checked but has not undergone independent peer review; inaccessible historical full texts leave residual priority uncertainty.

## References

- L. Novo, S. Chakraborty, M. Mohseni, H. Neven, Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (public December 22, 2014); *Scientific Reports* **5**, 13304 (2015), https://arxiv.org/abs/1412.7209.
- L. Razzoli, M. G. A. Paris, P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794 (public November 27, 2020); *Entropy* **23**, 85 (2021), https://arxiv.org/abs/2011.13794.
- X. Li, H. Chen, Y. Ruan, Z. Liu, W. Liu, *Continuous-time quantum walks on strongly regular graphs with loops and its application to spatial search for multiple marked vertices*, *Quantum Information Processing* **18**, 195 (2019), https://doi.org/10.1007/s11128-019-2250-5.
