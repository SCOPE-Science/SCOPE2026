# Exterior-state adjacency–Laplacian equivalence on weighted split joins

## Finding
Let \(r,s\geq1\), \(\eta>0\), and \(\alpha\geq0\). Form a weighted graph by assigning weight \(\alpha\) to each pair of the \(r\) central vertices, assigning weight \(\eta\) to every edge between the center and an independent class of \(s\) exterior vertices, and assigning no edges within the exterior class. Let \(A\) be its real symmetric weighted adjacency matrix, \(D\) its weighted-degree diagonal, and \(L=D-A\) its positive combinatorial weighted Laplacian.

For an exterior start vertex \(v\), write \(p_A(w,t)=|(e^{itA})_{wv}|^2\) and \(p_L(w,t)=|(e^{itL})_{wv}|^2\), for every vertex \(w\) and real time \(t\). The following three assertions are equivalent:

1. \(p_A(w,t)=p_L(w,t)\) for every vertex \(w\) and every \(t\in\mathbb R\).
2. For any one fixed central vertex \(c\), the coefficients of \(t^4\) in the Taylor series at zero of \(p_A(c,t)\) and \(p_L(c,t)\) agree.
3. \[\boxed{\alpha(r-1)=\eta|r-s|.}\]

Indeed the exact fourth-order witness is
\[p_A(c,t)-p_L(c,t)=-\frac{\eta^2}{12}\left[\alpha^2(r-1)^2-\eta^2(r-s)^2\right]t^4+O(t^6).\]

The criterion has two geometrically distinct parts. If \(s\leq r\), it is precisely the weighted-regularity condition \(\alpha(r-1)+\eta s=\eta r\), which makes the adjacency walk and the *signed*-Laplacian walk \(e^{-itL}\) equal as unitary matrices up to a global phase; the positive-L evolution \(e^{itL}\) is related by complex conjugation, which preserves measured probabilities. If \(s>r\), the condition becomes \(\alpha(r-1)=\eta(s-r)\); for \(r\geq2\) this is a genuinely irregular, continuously tunable positive-weight family exhibiting the weaker, exterior-state probability equivalence. For unit edge weights \(\alpha=\eta=1\) and \(r\geq2\), equivalence holds exactly when \(s=1\) (the regular complete graph) or \(s=2r-1\) (the irregular family identified numerically by Wong and Lockhart).

## Assumptions and scope
All graph vertices are labeled but otherwise exchangeable inside each of the two classes. The graph is finite and connected because \(\eta>0\). No assumption of distinct adjacency eigenvalues is made. The singleton center \(r=1\) has no internal edges, so \(\alpha\) is formally arbitrary and the criterion holds only when \(s=1\). At \(s=r\), the criterion requires \(\alpha(r-1)=0\), giving a regular weighted complete bipartite graph when \(r>1\). The Hamiltonians are compared at the same physical time and with the same weighted edges. A change of global sign or global phase does not alter the measured probabilities. The conclusion concerns initial basis vectors in the exterior class, not arbitrary initial superpositions or all possible central start vertices.

## Proof
**Step 1: invariant decomposition and exact central transition probabilities.** Let \(|c\rangle\) and \(|o\rangle\) be the normalized uniform center and exterior class vectors. The two-dimensional subspace they span is invariant under both \(A\) and \(K=A-D=-L\); their matrices in the ordered basis \((|c\rangle,|o\rangle)\) are
\[
A_2=\begin{pmatrix}\alpha(r-1)&\eta\sqrt{rs}\\\eta\sqrt{rs}&0\end{pmatrix},\qquad
K_2=\begin{pmatrix}-\eta s&\eta\sqrt{rs}\\\eta\sqrt{rs}&-\eta r\end{pmatrix}.
\]
The exterior vectors orthogonal to \(|o\rangle\) form a dark subspace on which \(A\) is zero and \(K\) acts as the scalar \(-\eta r\). The central contrast subspace cannot be excited from an exterior basis state because all center–exterior couplings are identical.

Set \(q=r+s\) and \(\Delta=\sqrt{\alpha^2(r-1)^2+4\eta^2rs}\). A direct two-level matrix exponential gives, for an arbitrary individual central vertex \(c\) and exterior starting vertex \(v\),
\[
p_A(c,t)=\frac{4\eta^2}{\Delta^2}\sin^2\frac{\Delta t}{2},\qquad
p_L(c,t)=\frac{4}{q^2}\sin^2\frac{\eta qt}{2}.
\]
Here \(\Delta>0\), and the nonzero gap for \(K_2\) is \(\eta q\): its eigenvalues are \(0,-\eta q\). Expanding \(4\sin^2(z t/2)/z^2=t^2-z^2t^4/12+O(t^6)\) yields the claimed exact fourth-order difference. Consequently condition 1 implies condition 2, which implies \(\Delta^2=\eta^2q^2\). Expanding this equality and canceling \(4\eta^2rs\) gives
\[\alpha^2(r-1)^2=\eta^2(r-s)^2.\]
Both sides of \(\alpha(r-1)\) and \(\eta|r-s|\) are nonnegative; therefore this squared equality is exactly condition 3.

**Step 2: sufficiency on the center.** Under condition 3, \(\Delta=\eta q\). Thus the central target probabilities in Step 1 agree for all real \(t\).

**Step 3: sufficiency on the exterior class.** Let \(f_A(t)=\langle o|e^{itA_2}|o\rangle\) and \(f_K(t)=\langle o|e^{itK_2}|o\rangle\). Using the eigenvalues of \(K_2\) and the normalized all-ones eigenvector of its zero eigenvalue, we obtain
\[f_K(t)=\frac{s}{q}+\frac{r}{q}e^{-i\eta qt}.\]
For exterior vertices \(v,w\), the invariant decomposition implies
\[
(e^{itA})_{wv}=\delta_{wv}+\frac{f_A(t)-1}{s},\qquad
(e^{itK})_{wv}=e^{-i\eta rt}\delta_{wv}+\frac{f_K(t)-e^{-i\eta rt}}{s}.
\]
If \(s\leq r\), condition 3 gives \(\alpha(r-1)=\eta(r-s)\), and the eigenvalues of \(A_2\) are \(\eta r,-\eta s\). Its exterior diagonal amplitude is
\[f_A(t)=\frac{s}{q}e^{i\eta rt}+\frac{r}{q}e^{-i\eta st}=e^{i\eta rt}f_K(t).\]
Hence \((e^{itA})_{wv}=e^{i\eta rt}(e^{itK})_{wv}\).

If \(s\geq r\), condition 3 instead gives \(\alpha(r-1)=\eta(s-r)\). The two eigenvalues of \(A_2\) are now \(\eta s,-\eta r\), and
\[f_A(t)=\frac{r}{q}e^{i\eta st}+\frac{s}{q}e^{-i\eta rt}=e^{-i\eta rt}\overline{f_K(t)}.\]
Hence \((e^{itA})_{wv}=e^{-i\eta rt}\overline{(e^{itK})_{wv}}\). In both cases exterior target *moduli* agree for every \(t\), and so do central moduli by Step 2. Since \(K=-L\) and \(L\) is real, \(|(e^{itK})_{wv}|=|(e^{itL})_{wv}|\). This proves condition 3 implies condition 1.

**Boundary and unit-weight cases.** For \(r=1\), condition 3 reads \(0=\eta|1-s|\), so \(s=1\); \(\alpha\) describes no edge and is irrelevant. For \(r\geq2\), setting \(\alpha=\eta=1\) yields \(r-1=|r-s|\), whence \(s=1\) or \(s=2r-1\), with no additional integer solutions. The proof does not depend on finite enumeration.

## Verification
The accompanying standalone file `verify.py` independently constructs the full matrices \(A\) and \(A-D\) and compares exterior-column transition probabilities using numerical diagonalization for 151 admissible matching parameter profiles, six times each and all exterior start and target vertices. The maximum absolute discrepancy over 121,212 checked entries was approximately \(1.67\times10^{-14}\). A separate exact rational check verifies the algebraic fourth-order gap identity for 1,980 parameter choices. Off-criterion examples display nonzero differences, and selected unweighted cases test a central-start boundary. Run `python verify.py` with Python 3 and NumPy installed. The universally quantified assertion is proved above; these finite calculations only corroborate it.

## Relationship to prior work
Wong and Lockhart, *Equivalent Laplacian and Adjacency Quantum Walks on Irregular Graphs* (2021, arXiv:2107.05580, Sec. IV, eighth family), already identified the unweighted split graphs with \(s=2r-1\) by numerical investigation and established individual small-graph cases analytically. That unweighted family and the general definition of probability equivalence are **prior work**, not newly claimed discoveries. The present result classifies **all** nonnegative uniform internal clique couplings and positive cross couplings at fixed two-class sizes, proves a necessary-and-sufficient condition for all exterior starting vertices, and makes equality of one fourth-order transition coefficient sufficient for the entire time-dependent probability vector. The regular weighted branch follows the classical trivial global-phase argument; mathematical novelty resides in the exact converse, the nonregular tunable branch, and local-to-global equivalence.

Kirkland and Monterde, *Quantum walks on join graphs* (2023, arXiv:2312.06906, especially Secs. 2–3), derive general adjacency and Laplacian transition formulas and study periodicity, cospectrality and perfect state transfer on weighted joins. Those general formulas are relevant tools from which specialized computations might be derived, but the inspected statements do not assert the present cross-Hamiltonian probability-equivalence characterization or quartic-coefficient test. This possible implication through additional algebra remains an originality limitation.

Qu and collaborators' *Experimental Investigation of Equivalent Laplacian and Adjacency Quantum Walks on Irregular Graphs* (2022, doi:10.1103/PhysRevA.105.062448) experimentally investigates equivalent walks on small graphs; its accessible abstract does not establish the general classification. A negative search result is not proof of absolute novelty.

## Limitations
The result requires uniform positive cross coupling and uniform nonnegative internal clique coupling, not arbitrary edge weights or all graph joins. It concerns initial states localized on exterior vertices, not arbitrary coherent superpositions or all start states. The classification compares unscaled Hamiltonians at equal times. It does not classify every irregular graph exhibiting equivalence. The full implications of existing general weighted-join spectral formulas could conceal an equivalent theorem not expressed in these terms; independent literature assessment is still needed. Numerical verification does not replace the analytical proof. No independent audit is asserted.

## References
1. T. G. Wong and J. Lockhart, *Equivalent Laplacian and Adjacency Quantum Walks on Irregular Graphs*, arXiv:2107.05580 (first submitted 2021-07-12), *Physical Review A* **104**, 042221 (2021), https://arxiv.org/html/2107.05580v2 .
2. S. Kirkland and H. Monterde, *Quantum walks on join graphs*, arXiv:2312.06906 (first submitted 2023-12-12), https://arxiv.org/html/2312.06906v1 .
3. Qu et al., *Experimental Investigation of Equivalent Laplacian and Adjacency Quantum Walks on Irregular Graphs*, *Physical Review A* **105**, 062448 (2022), https://doi.org/10.1103/PhysRevA.105.062448 .
